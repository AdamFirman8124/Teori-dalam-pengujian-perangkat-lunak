

# Generated at 2022-06-13 22:12:20.298854
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    import sys
    import random
    import os
    import pytest

    from io import StringIO

    from httpie.plugins import ConverterPlugin, FormatterPlugin
    from httpie.output.streams import write_bytes

    class HTMLFormatter(FormatterPlugin):
        media_type = 'text/html'
        def format_body(self, body: bytes, media_type: str) -> bytes:
            return body.replace(b'<', b'[')
    FormatterPlugin.__registry__.append(HTMLFormatter)

    class MockArgs:
        output_options = ('stdout',)
        output_options_handled = {'stdout': None}
        input_file = None
        output_file = None
        output_file_bak = None
        output_file_part = None
        formatter_plugins

# Generated at 2022-06-13 22:12:21.440015
# Unit test for constructor of class Formatting
def test_Formatting():
    # TODO
    pass

# Generated at 2022-06-13 22:12:27.851781
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    content = '{"hello": "world"}'
    mime = 'application/json'
    f = Formatting(groups=['json'])
    assert f.format_body(content, mime) == '{\n    "hello": "world"\n}'
    content = '1'
    mime = 'text/plain'
    assert f.format_body(content, mime) == '1'

# Generated at 2022-06-13 22:12:35.810671
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment(headers=True)
    formatting = Formatting(['colors'], env)
    headers = """HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 13
Content-Type: application/json
Date: Wed, 13 Sep 2017 14:23:54 GMT
Link: </collection?page=2>; rel="next"

{
    "text": "Hello, world!"
}
"""
    actual = formatting.format_headers(headers)

# Generated at 2022-06-13 22:12:48.483577
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    plugins = """
    {
        "formatters": {
            "colors": [
                "httpie.plugins.builtin.formatters.colors:ColorsFormatter"
            ]
        }
    }
    """
    plugin_manager.skip_load = True
    plugin_manager.load_plugins(plugins)
    output  = """
    HTTP/1.1 200 OK
    Date: Tue, 10 Jul 2018 14:08:19 GMT
    Server: Apache
    X-Powered-By: PHP/5.3.3
    Content-Length: 0
    Content-Type: text/html
    
    
    """
    formatting = Formatting(groups=["colors"], env=Environment())
    assert formatting.format_headers(output) == output


# Generated at 2022-06-13 22:12:52.228689
# Unit test for method format_headers of class Formatting

# Generated at 2022-06-13 22:12:54.253294
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.cli import builtin_plugins

    assert len(builtin_plugins) == 5

# Generated at 2022-06-13 22:13:06.005201
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    import httpie.context
    import pprint
    env = httpie.context.Environment()
    fmt = Formatting(env=env, groups=['bodies'],
                     pretty=False)
    # fmt = Formatting(env=env, groups=['bodies'],
    #                  pretty='all')
    if not fmt.enabled_plugins:
        return
    # JSON
    f = open('../tests/fixtures/raw_json.txt', 'r')
    raw = f.read()
    f.close()
    print(raw, end='\n\n')
    formatted = fmt.format_body(raw, 'application/json')
    print(formatted, end='\n\n')
    # XML
    f = open('../tests/fixtures/raw_xml.txt', 'r')
    raw = f

# Generated at 2022-06-13 22:13:19.394285
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Test case
    # input: headers == "HTTP/1.1 200 OK"
    #        groups == ["HTTPiePluginPrettyHTTPHeaderProcessor"]
    #        env == Environment()
    #        kwargs == {}
    # expected: "HTTP/1.1 200 OK"
    fmt = Formatting(["HTTPiePluginPrettyHTTPHeaderProcessor"], env=Environment())
    assert "HTTP/1.1 200 OK" == fmt.format_headers("HTTP/1.1 200 OK")

    # Test case
    # input: headers == "HTTP/1.1 200 OK"
    #        groups == ["HTTPiePluginPrettyHTTPHeaderProcessor", "HTTPiePluginPrettyHTTPDateResponseProcessor"]
    #        env == Environment()
    #        kwargs == {}
    # expected: "HTTP/1.1 200 OK\nDate:

# Generated at 2022-06-13 22:13:24.106991
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('') is None
    assert Conversion.get_converter('foo') is None
    assert Conversion.get_converter('foo/') is None
    assert Conversion.get_converter('/foo') is None



# Generated at 2022-06-13 22:13:34.836326
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # convert_mime = "application/xml"
    # converter = Conversion.get_converter(convert_mime)
    # converter_class = converter.__class__
    # assert converter_class.__name__ == "ConvertXml"

    convert_mime = "application/json"
    converter = Conversion.get_converter(convert_mime)
    converter_class = converter.__class__
    assert converter_class.__name__ == "ConvertJson"

# Generated at 2022-06-13 22:13:38.727227
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(['colors'])
    f = Formatting(['colors', 'format'])
    try:
        f = Formatting(['colors', 'format', 'bogus'])
    except KeyError:
        pass

# Generated at 2022-06-13 22:13:43.518727
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['py', 'json', 'html']
    env = Environment()
    formatter = Formatting(groups=groups, env=env)

    print("Loaded plugins:")
    for plugin in formatter.enabled_plugins:
        print("\t" + plugin.name)


# Example from the command line:
    
# Run: python3 formatting.py py json html
# Output:

# Loaded plugins:
# 	Pygments
# 	JSONFormatter
# 	HTMLFormatter

# Generated at 2022-06-13 22:13:54.433779
# Unit test for constructor of class Formatting
def test_Formatting():
    class FormatterPluginTEST(ConverterPlugin):
        pass

    class FormatterPluginTEST2(ConverterPlugin):
        pass

    class ConverterPluginTEST(ConverterPlugin):
        pass

    class ConverterPluginTEST2(ConverterPlugin):
        pass

    plugin_manager.register(FormatterPluginTEST)
    plugin_manager.register(FormatterPluginTEST2)
    plugin_manager.register(ConverterPluginTEST)
    plugin_manager.register(ConverterPluginTEST2)

    assert(Formatting(groups=['headers', 'body'], env=Environment(), **{}).enabled_plugins ==
           [FormatterPluginTEST(), FormatterPluginTEST2()])

# Generated at 2022-06-13 22:13:59.150046
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter(None) is None

    random_data = 'random data'
    assert Conversion.get_converter(random_data).convert_data(random_data) == random_data



# Generated at 2022-06-13 22:14:03.510689
# Unit test for constructor of class Formatting
def test_Formatting():
    assert 'JSON' in Formatting(['json', 'colors']).enabled_plugins[0].__str__()
    assert 'HTMLList' in Formatting(['html', 'colors']).enabled_plugins[0].__str__()

# Generated at 2022-06-13 22:14:17.361602
# Unit test for constructor of class Formatting
def test_Formatting():
    # test case 1
    assert Formatting([]).enabled_plugins == []
    # test case 2
    assert Formatting(["colors"]).enabled_plugins == []
    # test case 3
    mime = "text/plain"    
    env = Environment()
    kwargs = {"--variant": "light"}
    assert Formatting(["json", "colors"]).enabled_plugins == []
    assert Formatting(["json", "colors"], env, **kwargs).enabled_plugins == []
    assert Formatting(["json"]).enabled_plugins == []
    assert Formatting(["json"], env, **kwargs).enabled_plugins == []
    # test case 4
    assert Formatting(["json", "colors"]).enabled_plugins == []

# Generated at 2022-06-13 22:14:28.071581
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = 'Content-Type: text/html; charset=UTF-8\r\nConnection: close\r\nServer: Apache/2.2.14 (Ubuntu)\r\n\r\n'
    assert Formatting(['origins']).format_headers(headers) == 'Content-Type: text/html; charset=UTF-8\r\nConnection: close\r\nServer: Apache/2.2.14 (Ubuntu)\r\n\r\n'

# Generated at 2022-06-13 22:14:31.038791
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    env.content_type = "text/html"
    env.semver = "0.0"
    cls = Formatting(['colors'], env)
    assert cls

# Generated at 2022-06-13 22:14:42.260036
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Case 1: when headers is None
    f = Formatting(groups=[])
    headers = None
    expected = None
    actual = f.format_headers(headers)
    assert expected == actual

    # Case 2: when headers is empty
    f = Formatting(groups=[])
    headers = ""
    expected = ""
    actual = f.format_headers(headers)
    assert expected == actual

    # Case 3: when headers have one empty line
    f = Formatting(groups=[])
    headers = "\n"
    expected = "\n"
    actual = f.format_headers(headers)
    assert expected == actual

    # Case 4: when headers have one normal line
    f = Formatting(groups=[])
    headers = "content-type: application/json"
    expected = "content-type: application/json"
   

# Generated at 2022-06-13 22:14:48.043358
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    expected = 'GET / HTTP/1.1\nHost: example.com\n\n'
    fmt = Formatting(['HTTPieFormatter'])
    out = fmt.format_headers('GET / HTTP/1.1\r\nHost: example.com\r\n')
    assert(expected == out)
    fmt = Formatting(['HTTPieFormatter', 'PrettyFormatter'])
    out = fmt.format_headers('GET / HTTP/1.1\r\nHost: example.com\r\n')
    assert(expected == out)
    fmt = Formatting(['PrettyFormatter'])
    out = fmt.format_headers('GET / HTTP/1.1\r\nHost: example.com\r\n')
    assert(expected == out)

# Generated at 2022-06-13 22:14:56.527549
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie import __main__
    from httpie.core import main
    args = [
        '-b',
        'json'
    ]

    parser = __main__.get_parser()
    args = parser.parse_args(args)
    kwargs = vars(args)
    env = Environment()
    f = Formatting(env=env, groups=kwargs['format'], colors=kwargs['colors'])
    print(f.format_body("""{"a":1}""","application/json"))


if __name__ == '__main__':
    test_Formatting()

# Generated at 2022-06-13 22:14:57.578053
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting([])

# Generated at 2022-06-13 22:15:09.454379
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    input_headers = r'''GET / HTTP/1.1
Host: localhost:8080
Connection: keep-alive
Content-Length: 10
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
Accept: */*
Referer: http://localhost:8080/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
'''

# Generated at 2022-06-13 22:15:15.248410
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # 1. test with invalid mime, only one converter is available
    converter = Conversion.get_converter('invalid/value')
    converter_class = plugin_manager.get_converters()[0]
    assert converter.__class__ == converter_class

    # 2. test with valid mime, only one converter is available
    converter = Conversion.get_converter('application/json')
    converter_class = plugin_manager.get_converters()[0]
    assert converter.__class__ == converter_class

    # 3. TODO test with multiple converters


# Generated at 2022-06-13 22:15:26.973933
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    print("Formatting_format_headers: ")
    import requests
    import httpie.plugins.builtin.formatter
    import httpie.plugins.builtin.formatters.headers

    headers = {
        "Content-Type": "application/json",
        "X-Something-Else": "Lol"
    }

    headers_string = httpie.plugins.builtin.formatters.headers.HTTPLogFormatter.get_headers(headers)
    print("headers_string " + headers_string)

    env = Environment()
    formatter = httpie.plugins.builtin.formatter.Formatter(env=env, colors=False)
    f = Formatting(['headers', 'format'], env=env, formatter=formatter, colors=False)

# Generated at 2022-06-13 22:15:39.985329
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors']  # List of processor groups to be applied
    env = Environment()
    # Additional keyword arguments for processors
    kwargs = {"colors": False, "format": "pretty", "explode": True}
    # Creating object of Formatting class
    format_obj = Formatting(groups, env, **kwargs)
    # Unit test for format_headers
    # headers = "Date: Sun, 16 Jun 2019 17:59:56 GMT\n" \
    #           "Content-Type: application/json; charset=utf-8\n" \
    #           "Content-Length: 159\n" \
    #           "Connection: keep-alive\n" \
    #           "Server: nginx/1.13.0\n" \
    #           "Access-Control-Allow-Origin: *\n

# Generated at 2022-06-13 22:15:47.474935
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    f = open("test.txt", "w")
    f.write('{"id": "d290f1ee-6c54-4b01-90e6-d701748f0851", "name": "Foo"}')
    f.close()
    f = open("test.txt", "r")
    content = f.read()
    print(content)
    f.close()
    converter = Conversion.get_converter("application/json")
    assert converter.can_handle_format is True
    assert converter.format == "application/json"
    result = converter.decode(content)
    print(result)



# Generated at 2022-06-13 22:15:56.492900
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # unit test for method format_headers of class Formatting
    test_headers = 'HTTP/1.1 200 OK\r\nDate: Wed, 02 Mar 2016 10:25:41 GMT\r\nServer: Apache/2.4.7 (Ubuntu)\r\nVary: Accept-Encoding\r\nContent-Length: 1\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    formatting = Formatting([], env=Environment(colors=256))
    assert formatting.format_headers(test_headers) == test_headers


# Generated at 2022-06-13 22:16:00.271718
# Unit test for constructor of class Formatting
def test_Formatting():
    instance = Formatting(["header"])
    assert not instance.enabled_plugins
    
    instance = Formatting(["body"])
    assert not instance.enabled_plugins

# Generated at 2022-06-13 22:16:08.730646
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    # test for one of the two enabled plugins
    for cls in available_plugins['highlighting']:
        p = cls()
        if p.enabled:
            assert cls

    # test for the disabled plugin
    for cls in available_plugins['pretty']:
        p = cls()
        assert not p.enabled

# Generated at 2022-06-13 22:16:17.153379
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.context import Environment

    class TestFormatting(Formatting):
        def __init__(self, groups: List[str], env=Environment(), **kwargs):
            from plugins.formatter.colors import ColorFormatterPlugin
            from plugins.formatter.format import FormatFormatterPlugin

            self.enabled_plugins = [ColorFormatterPlugin(env=env, **kwargs), FormatFormatterPlugin(env=env, **kwargs)]

    # headers = 'HTTP/1.1 200 OK\r\n'\
    #         b'Content-Length: 12\r\n'\
    #         b'Content-Type: application/json\r\n'\
    #         b'Content-Encoding: utf-8\r\n'\
    #         b'Date: Thu, 16 May 2019 15:40:01

# Generated at 2022-06-13 22:16:29.143044
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    res = Formatting(['headers', 'body'], env)
    assert res.enabled_plugins[0].name == 'headers'
    assert res.enabled_plugins[1].name == 'body'



# Generated at 2022-06-13 22:16:31.710185
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting(groups = ['all', 'group 2']) is not None


# Generated at 2022-06-13 22:16:47.232380
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    h1 = "content-type:text/plain\n"
    h2 = "Content-Type:text/plain\n"
    h3 = "Content-Type:application/json\n"
    h4 = "Content-Type:application/json;charset=UTF-8\n"
    headers_1 = Formatting(['colors']).format_headers(h1)
    headers_2 = Formatting(['colors']).format_headers(h2)
    headers_3 = Formatting(['colors']).format_headers(h3)
    headers_4 = Formatting(['colors']).format_headers(h4)
    assert headers_1 == "\x1b[37mcontent-type:\x1b[39;49;00mtext/plain\n"

# Generated at 2022-06-13 22:16:49.744822
# Unit test for constructor of class Formatting
def test_Formatting():
    assert isinstance(Formatting(['body']), Formatting)

# Generated at 2022-06-13 22:16:50.270205
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    pass

# Generated at 2022-06-13 22:16:53.164061
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    f = Formatting(['colors'], env=env, indent=4)


# Generated at 2022-06-13 22:17:07.131138
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json').mime == 'application/json'
    assert Conversion.get_converter('text/html').mime == 'text/html'
    assert Conversion.get_converter('text/plain').mime == 'text/plain'
    assert not Conversion.get_converter('text')
    assert not Conversion.get_converter('/')
    assert not Conversion.get_converter('/plain')
    assert not Conversion.get_converter('plain')
    assert not Conversion.get_converter('plain/')
    assert not Conversion.get_converter('p/plain')
    assert not Conversion.get_converter('text/p')
    assert not Conversion.get_converter('text/plain/')
    assert not Conversion.get_conver

# Generated at 2022-06-13 22:17:15.638787
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    json_mime = 'application/json'
    json_converter = Conversion.get_converter(json_mime)
    assert json_converter.supports(json_mime)

    xml_mime = 'application/xml'
    xml_converter = Conversion.get_converter(xml_mime)
    assert xml_converter.supports(xml_mime)

    not_json_mime = 'text/plain'
    not_json_converter = Conversion.get_converter(not_json_mime)
    assert not_json_converter is None


# Generated at 2022-06-13 22:17:32.242696
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():

    env = Environment(colors = False)
    groups = ['formatters']

    initial_headers = 'Content-Length: 22\nDate: Tue, 05 Nov 2019 07:57:26 GMT\nETag: "5dbb761c-16"\n\n'

    expected_output = 'Content-Length: 22\nDate: Tue, 05 Nov 2019 07:57:26 GMT\nETag: "5dbb761c-16"\n\n'

    formatting = Formatting(groups, env, )
    output = formatting.format_headers(initial_headers)

    assert output == expected_output



# Generated at 2022-06-13 22:17:45.760180
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """
    Check the format body function.
    """

# Generated at 2022-06-13 22:17:54.469387
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import httpie.plugins.builtin
    import httpie.cli.argtypes
    env = httpie.cli.argtypes.KeyValueArgType.env
    httpie.plugins.builtin.json_format.JSONFormatter(env=env)
    httpie.plugins.builtin.xml_format.XMLFormatter(env=env)

    header = {"Content-Type": "text/plain", "content-length": "1"}
    formatter = Formatting(['json', 'xml'], env)
    formatter.format_headers(header)
    assert header['content-length'] == '1'

    header = {"Content-Type": "text/xml", "content-length": "1"}
    formatter.format_headers(header)
    assert header['content-length'] == '1'


# Generated at 2022-06-13 22:18:02.933311
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    assert Formatting(['json', 'colors']).format_body("""{
  "test" : "test"
}""", 'application/json') == """\x1b[1m\x1b[34m{\x1b[39m
  \x1b[1m\x1b[34m"test"\x1b[39m \x1b[1m\x1b[93m:\x1b[39m \x1b[1m\x1b[32m"test"\x1b[39m
\x1b[34m}\x1b[39m"""


# Generated at 2022-06-13 22:18:05.976522
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(["colors"])
    assert isinstance(f.enabled_plugins, list)



# Generated at 2022-06-13 22:18:11.736764
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    content = {"foo": ["bar", "baz"]}
    mime = "application/json"
    result = Formatting([]).format_body(json.dumps(content), mime)
    content_right = {"foo": ["bar", "baz"]}
    content_right = json.dumps(content_right, indent=4, sort_keys=True)
    assert result == content_right


# Generated at 2022-06-13 22:18:16.615014
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    class A:
        p = Formatting(groups=["headers"])
        def test(self):
            output = self.p.format_headers('test:test\ntest2:test2\n')
            return output
    def test_format_headers():
        a = A()
        output = a.test()
        assert "test" in output
    test_format_headers()

# Generated at 2022-06-13 22:18:24.812541
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    data1 = {
        'url': 'http://www.google.com',
        '--form': [],
        'HEADER': 'value',
        'method': 'GET',
        '__o': 'json',
        '--pretty': 'all'
    }
    env = Environment(stdin=io.StringIO(),
                      stdout=io.StringIO(),
                      stderr=io.StringIO(),
                      request_counter=0)
    json_ = json.dumps({'test': 'value'})
    expected = Formatting([], env=env).format_body(json_, 'application/json')
    formatter = Formatting(['json'], env=env)
    actual = formatter.format_body(json_, 'application/json')
    # actual_2 = formatter.format_body(json

# Generated at 2022-06-13 22:18:27.634414
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting([])
    assert Formatting(['colors'])

# Generated at 2022-06-13 22:18:38.125783
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    """Unit test for method format_headers of class Formatting"""
    from httpie.context import Environment
    from httpie.plugins.builtin import JSONFormatter

    env = Environment()
    formatting = Formatting(['json'], env=env)
    assert formatting
    assert len(formatting.enabled_plugins) == 1

# Generated at 2022-06-13 22:18:58.004020
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.registry import plugin_manager
    from httpie.context import Environment
    from httpie.core import main
    
    class TestFormatterPlugin(FormatterPlugin):
        def __init__(self, **kwargs):
            super(TestFormatterPlugin, self).__init__(**kwargs)
            self.name = 'Test'
            self.description = 'Test plug-in.'
            self.enabled = True
        
        def format_headers(self, headers):

            return 'This is a formatter plugin named {}.'.format(self.name)

    plugin_manager.register(TestFormatterPlugin)

    env = Environment()
    Formatting.get_formatters(env)

    Formatting.format_headers('foo bar')

# Generated at 2022-06-13 22:19:00.720408
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert(converter.mimetype == "application/json")


# Generated at 2022-06-13 22:19:08.560752
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    test_data = ["application/json", "application/xml", "application/yaml", "text/html", "text/plain"]
    for data in test_data:
        assert(Conversion.get_converter(data) != None)
    assert(Conversion.get_converter("") == None)
    assert(Conversion.get_converter("invalid-data") == None)
    assert(Conversion.get_converter("application/xml/invalid-data") == None)


# Generated at 2022-06-13 22:19:12.316616
# Unit test for constructor of class Formatting
def test_Formatting():
    a = Formatting(['colors'])
    b = Formatting(['colors'])
    assert a.enabled_plugins[0].__class__ == b.enabled_plugins[0].__class__

# Generated at 2022-06-13 22:19:17.043215
# Unit test for constructor of class Formatting
def test_Formatting():
    env_ = Environment()
    env_.colors = False
    formatting = Formatting(['FormatTable'], env=env_)
    print(formatting.format_headers('{"status": "1"}'))
    print(formatting.format_body('{"status": "1"}', 'application/json'))

# Generated at 2022-06-13 22:19:19.431047
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    output = Conversion.get_converter("text/html")
    assert output is not None

# Generated at 2022-06-13 22:19:22.589767
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    cm = Conversion.get_converter('application/json')
    assert str(cm) == 'Converter(application/json)'



# Generated at 2022-06-13 22:19:26.449149
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    groups = ['colors']
    kwargs = {'prettify': False}
    #TODO: hint: what will be the value of available_plugins?
    available_plugins = plugin_manager.get_formatters_grouped()

    instance = Formatting(groups, env, **kwargs)
    assert isinstance(instance, Formatting)

test_Formatting()

# Generated at 2022-06-13 22:19:29.430512
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = "application/json"
    
    converter = Conversion.get_converter(mime)
    
    assert converter.mime == mime
    

# Generated at 2022-06-13 22:19:35.338995
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors', 'format']
    env=Environment()
    kwargs = {}
    f = Formatting(groups, env, **kwargs)
    assert len(f.enabled_plugins) == 4
    assert f.format_headers("") == ""
    assert f.format_body("", 'text/plain') == ""

# Generated at 2022-06-13 22:19:54.545833
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    screen_size = os.get_terminal_size().columns
    formatting = Formatting(['headers'])
    test_case_1 = formatting.format_headers('HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n')
    expected_result_1 = 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n'
    test_case_2 = formatting.format_headers('HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n')
    expected_result_2 = 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n'

# Generated at 2022-06-13 22:20:00.695630
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    env = Environment(stdout_isatty=False)
    fmt = Formatting(['colors'], env=env)
    fmt.format_body('red', 'test')
    from httpie.plugins.builtin import Formatter

    assert Formatter(env=env).enabled
    assert not fmt.enabled_plugins[0].enabled

# Generated at 2022-06-13 22:20:08.795875
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.compat import is_windows
    from httpie.context import Environment
    from httpie.plugins.builtin import HTTPHeadersProcessor
    from httpie.plugins import plugin_manager
    from httpie.output.streams import get_output_stream

    plugin_manager.clear()
    plugin_manager.load_installed_plugins()

# Generated at 2022-06-13 22:20:14.085204
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['http']
    try:
        # Create object of class Environment
        env = Environment()
    except:
        print('Error: object of class Environment cannot be created!')

    obj = Formatting(groups, env)
    try:
        assert obj.enabled_plugins
    except:
        print('Error: object of class Formatting cannot be created!')



# Generated at 2022-06-13 22:20:26.709160
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    group_list = ['colors']
    kwargs = {'colors': True}
    for_class = Formatting(group_list, **kwargs)

# Generated at 2022-06-13 22:20:38.856777
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins.builtin import ASCIIFold
    from httpie.plugins import FormatterPlugin
    import pytest

    class DummyProcessor(FormatterPlugin):
        def format_headers(self, headers):
            print('hello')
            return headers

    class AnotherProcessor(FormatterPlugin):
        def format_headers(self, headers):
            print('another')
            return headers

    orig_fmt_grp = plugin_manager.get_formatters_grouped()
    plugin_manager.get_formatters_grouped.cache_clear()
    plugin_manager.available[ASCIIFold.name] = None
    plugin_manager._add_plugin(DummyProcessor)
    plugin_manager._add_plugin(AnotherProcessor)
    env = Environment()

# Generated at 2022-06-13 22:20:43.952327
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins.registry import plugin_manager
    from httpie import Environment
    from httpie.context import CONTEXT_NAME

    env = Environment(vars={CONTEXT_NAME: 'test'}, colors=256)
    for formatters_group in plugin_manager.get_formatters_grouped():
        for formatter in plugin_manager.get_formatters_grouped()[formatters_group]:
            if formatter.enabled and formatter.enabled(env=env):
                if formatter.format_headers(test_string) == test_result:
                    return True
    return False


# Generated at 2022-06-13 22:20:50.764590
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not Conversion.get_converter('')

    assert not Conversion.get_converter('text/plain')

    assert not Conversion.get_converter('application/json;abc')

    assert not Conversion.get_converter('parquet')

    assert not Conversion.get_converter('text/plain/')

    assert not Conversion.get_converter('text//plain')

# Generated at 2022-06-13 22:20:54.807285
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    test_class = Formatting(['formatting'])
    assert (test_class.format_body("{\"var1\":1, \"var2\":2, \"var3\":3}", "application/json") ==
            "\n{\n    \"var1\": 1,\n    \"var2\": 2,\n    \"var3\": 3\n}\n")

# Generated at 2022-06-13 22:21:02.441629
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins.builtin import HTTPPrettyJSONFormatter
    class FakeFormatter:
        def format_body(self, content: str, mime: str) -> str:
            return content + mime

    class FakeEnvironment(Environment):
        stdin_isatty = False

    test_content = '{ "id": 1, "name": "Test" }'
    test_content_json = '{\n    "id": 1,\n    "name": "Test"\n}'
    f = Formatting(['json'], env=FakeEnvironment())
    assert f.format_body(test_content, 'application/json') == test_content_json

    f.enabled_plugins.append(FakeFormatter())

# Generated at 2022-06-13 22:21:19.088982
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(['colors'], )
    assert f.format_body("{}", 'application/json') == "{}"
    assert f.format_body("<a>b</a>",
                         'application/xml') == '\x1b[38;5;39m<a>\x1b[0m\x1b[38;5;39mb\x1b[0m\x1b[38;5;39m</a>\x1b[0m'

# Generated at 2022-06-13 22:21:30.256852
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    groups = ["colors"]
    fmt = Formatting(groups, env)
    headers = "Content-Type: application/json\r\nUser-Agent: curl/7.29.0\r\nHost: 127.0.0.1:5000";
    expected = ("Content-Type: \x1b[01;34mapplication/json\x1b[0m\r\n"
                "User-Agent: curl/7.29.0\r\n"
                "Host: 127.0.0.1:5000")
    assert fmt.format_headers(headers) == expected



# Generated at 2022-06-13 22:21:31.663961
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert(Conversion.get_converter("application/json"))
    

# Generated at 2022-06-13 22:21:33.528903
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json') is not None

# Generated at 2022-06-13 22:21:41.930420
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    formatting = Formatting(groups=["colors"], env=env)
    headers = formatting.format_headers("HTTP/1.1 200 OK\n\n")
    assert headers.startswith(env.color.colorize('HTTP/1.1', "status"))



# Generated at 2022-06-13 22:21:51.504450
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    groups = ['colors']
    kwargs = {}
    import httpie.plugins
    available_plugins = httpie.plugins.plugin_manager.get_formatters_grouped()
    enabled_plugins = []
    for group in groups:
        for cls in available_plugins[group]:
            p = cls(**kwargs)
            if p.enabled:
                enabled_plugins.append(p)
    # Test Case 1
    headers = "Content-Type: application/json"
    output = enabled_plugins[0].format_headers(headers)
    assert output == "\x1b[37m" + headers + "\x1b[0m" + "\n"
    # Test Case 2
    headers = "foo: bar"
    output = enabled_plugins[0].format_headers(headers)

# Generated at 2022-06-13 22:22:06.156072
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """Test format_body method of class Formatting"""
    content = '{"data": {"date": "2019-12-11","daily_number": 60}}'
    # check format_body of class Formatting
    # The test case is with "json" as the parameter,
    # and the expected output is with format json
    assert Formatting(['json']).format_body(content, 'application/json') == '{\n    "data": {\n        "date": "2019-12-11",\n        "daily_number": 60\n    }\n}'
    # The test case is with "form" as the parameter,
    # and the expected output is with format form

# Generated at 2022-06-13 22:22:10.696288
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    f = Formatting(groups=["colors"], env=env)
    f._colorize = lambda x: x + "coloured"
    output = f.format_headers("text color")
    assert output == "text colour"
