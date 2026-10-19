

# Generated at 2022-06-13 22:12:21.212743
# Unit test for constructor of class Formatting
def test_Formatting():
    content = '{"name": "httpie", "description": "Command line HTTP client"}'
    mime = 'application/json'
    output = Formatting(['format', 'colors']).format_body(content, mime)

    # output must be a string
    assert isinstance(output, str)

# Generated at 2022-06-13 22:12:28.205928
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('json') == None
    assert Conversion.get_converter('json2') == None
    assert Conversion.get_converter('application/json') == None
    for converter_class in plugin_manager.get_converters():
        if converter_class.supports('application/json'):
            assert isinstance(Conversion.get_converter('application/json'), converter_class)



# Generated at 2022-06-13 22:12:31.560742
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    db = Formatting(['colors'], env=Environment(), colors=True)
    print(db.format_body('{"name":"x"}',"application/json"))



# Generated at 2022-06-13 22:12:41.736773
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Test get_converter with invalid mime
    if Conversion.get_converter("application/json-seq"):
        print("Test get_converter with invalid mime FAILED")
    else:
        print("Test get_converter with invalid mime SUCCESSFUL")
    # Test get_converter with valid mime
    if Conversion.get_converter("application/json"):
        print("Test get_converter with valid mime SUCCESSFUL")
    else:
        print("Test get_converter with valid mime FAILED")


# Generated at 2022-06-13 22:12:50.136568
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    available_plugins = plugin_manager.get_formatters_grouped()
    enabled_plugins = []
    for group in ["html"]:
        for cls in available_plugins[group]:
           p = cls(env=Environment())
           if p.enabled:
               enabled_plugins.append(p)

    content = '["foo", {"bar":["baz", null, 1.0, 2]}]'
    mime = "application/json"
    if is_valid_mime(mime):
        for p in enabled_plugins:
            content = p.format_body(content, mime)
        return content


# Generated at 2022-06-13 22:13:03.266626
# Unit test for constructor of class Formatting
def test_Formatting():
    try:
        assert isinstance(Formatting([], None), Formatting)
    except (AssertionError, TypeError):
        print("Exception in test_Formatting of formatter.py")
    try:
        assert isinstance(Formatting([], Environment()), Formatting)
    except (AssertionError, TypeError):
        print("Exception in test_Formatting of formatter.py")
    try:
        assert isinstance(Formatting(['colors'], Environment()), Formatting)
    except (AssertionError, TypeError):
        print("Exception in test_Formatting of formatter.py")

# Generated at 2022-06-13 22:13:13.841741
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    """
    Test format_headers method
    """
    headers = """HTTP/1.1 200 OK\r\nContent-Length: 0\r\nCache-Control: private, max-age=31536000\r\nContent-Type: text/html; charset=UTF-8\r\nDate: Tue, 22 Sep 2020 05:16:35 GMT\r\nExpires: Wed, 21 Sep 2021 05:16:35 GMT\r\nP3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."\r\nServer: gws\r\nX-XSS-Protection: 0\r\nX-Frame-Options: SAMEORIGIN\r\n\r\n"""
    p = Formatting(['colors'])

# Generated at 2022-06-13 22:13:15.572548
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion.get_converter('application/json')
    print(c)

# Generated at 2022-06-13 22:13:18.588533
# Unit test for constructor of class Formatting
def test_Formatting():
    a = Formatting(['colors'])
    assert a
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
"""

# Generated at 2022-06-13 22:13:29.738006
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("application/json"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("application/x-www-form-urlencoded"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("application/xml"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("multipart/form-data"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("text/csv"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("text/html"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("text/javascript"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("text/plain"), ConverterPlugin)

# Generated at 2022-06-13 22:13:36.812634
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['json', 'table']
    env = Environment()
    env.stdin_isatty = True
    kwargs = {'stream': sys.stdin}
    f1 = Formatting(groups, env, **kwargs)
    assert f1 is not None
    return



# Generated at 2022-06-13 22:13:38.617992
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=["colors"], env=Environment(), style="linux")
    assert f.enabled_plugins !=None

# Generated at 2022-06-13 22:13:44.932398
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # base is mime
    assert isinstance(Conversion.get_converter("text/plain"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("application/json"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("application/xml"), ConverterPlugin)
    # base is invalid
    assert Conversion.get_converter("plain") is None
    assert Conversion.get_converter("text") is None
    assert Conversion.get_converter("file/txt") is None
    assert Conversion.get_converter("application/") is None
    assert Conversion.get_converter("/xml") is None
    assert Conversion.get_converter("/") is None



# Generated at 2022-06-13 22:13:50.263950
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Setup
    converter_class = plugin_manager.get_converters()[0]
    # Exercise
    result = Conversion.get_converter(converter_class.MIME)
    # Verify
    assert result == converter_class(converter_class.MIME)
    # Cleanup



# Generated at 2022-06-13 22:13:54.737117
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert converter.mime == "application/json"

# Generated at 2022-06-13 22:14:05.040461
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('application/json'), ConverterPlugin) is True
    assert isinstance(Conversion.get_converter('application/xml'), ConverterPlugin) is True
    assert isinstance(Conversion.get_converter('text/plain'), ConverterPlugin) is True

    # Wrong type of argument
    assert Conversion.get_converter(123) is None

    # Argument is empty
    assert Conversion.get_converter('') is None

    # Argument is MIME-type but not supported by HTTpie
    assert Conversion.get_converter('application/zip') is None

# Generated at 2022-06-13 22:14:18.750545
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ["JSON"]
    env = Environment()

# Generated at 2022-06-13 22:14:28.518374
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.output.formatters.colors import ColorsFormatter
    from httpie.output.formatters.json import JSONFormatter
    from httpie.output.formatters.format import Formatter
    from httpie.output.formatters.utils import get_lexer

    supported_mime = [
        "application/json",
        "application/json; charset=UTF-8",
        "text/html",
        "text/html; charset=ISO-8859-4",
        "application/javascript",
        "application/javascript; charset=UTF-8",
        "text/css",
        "text/css; charset=UTF-8",
        "text/plain",
        "text/plain; charset=UTF-8"
    ]


# Generated at 2022-06-13 22:14:32.356399
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    environment = Environment()
    environment.config['output_options']['format'] = 'none'
    environment.config['colors'] = False
    format = Formatting(groups=['output'], env=environment)
    assert format.format_headers('headers') == 'headers'

# Generated at 2022-06-13 22:14:42.504702
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatting_obj = Formatting(['highlight', 'colors'], env=Environment())
    str_in = """HTTP/1.1 200 OK
Host: https://localhost:5000/
Date: Sun, 12 May 2019 19:29:28 GMT
Server: Werkzeug/0.14.1 Python/3.7.3
Content-Type: text/html; charset=utf-8
Content-Length: 22

<h1>Hello, World</h1>
"""

# Generated at 2022-06-13 22:14:55.941326
# Unit test for method format_headers of class Formatting

# Generated at 2022-06-13 22:15:10.596857
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.plugins.builtin import HTTPHeadersFormatOneProcessor
    from httpie.plugins.builtin import HTTPHeadersProcessor
    from httpie.plugins.builtin import JSONProcessor
    from httpie.plugins.builtin import HTTPFormProcessor
    groups = ['headers', 'body']
    f = Formatting(groups=groups)
    assert f.enabled_plugins == [HTTPHeadersFormatOneProcessor(), HTTPHeadersProcessor()]
    groups = ['headers', 'body']
    with Environment() as env:
        env.stdout.isatty = True
        f = Formatting(groups=groups)
        assert f.enabled_plugins == [HTTPHeadersFormatOneProcessor(), HTTPHeadersProcessor(), JSONProcessor(), HTTPFormProcessor()]

# Generated at 2022-06-13 22:15:13.431625
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    s = Formatting.format_body('{"greeting": "hello"}', 'application/json')
    print(s)


# Generated at 2022-06-13 22:15:15.508923
# Unit test for constructor of class Formatting
def test_Formatting():
    fmt = Formatting(['body'], env = Environment())
    assert fmt is not None

# Generated at 2022-06-13 22:15:26.831284
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n"
    formatting = Formatting(["colors", "format", "format_options"], env)
    assert formatting
    assert isinstance(formatting, Formatting)
    format_headers = formatting.format_headers(headers)
    assert format_headers == "\x1b[94mHTTP/1.1\x1b[0m \x1b[92m200\x1b[0m \x1b[93mOK\x1b[0m\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n"


# Generated at 2022-06-13 22:15:29.859588
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ["pretty"]
    env = Environment()
    kwargs = {"test": "test"}
    f = Formatting(groups=groups, env=env, **kwargs)
    assert f.enabled_plugins[0].__class__.__name__ == "Pretty"


# Generated at 2022-06-13 22:15:42.683459
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fmter = Formatting(['Colorized'])

# Generated at 2022-06-13 22:15:47.137747
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment(args_string="--verbose")
    groups = [
        'colors',
        'format'
    ]

    f = Formatting(groups=groups, env=env)
    assert f.enabled_plugins is not None

# Generated at 2022-06-13 22:15:48.888448
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting(['color'], color=True, style='solarized')

# Generated at 2022-06-13 22:15:52.462771
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert str(type(converter)) == "<class 'httpie.plugins.converter.application.json.JSONConverter'>"

# Generated at 2022-06-13 22:16:05.217246
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    f = Formatting(['Default'])
    request = '''GET / HTTP/1.1\r\nHost: localhost\r\nUser-Agent: httpie/0.9.9\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\n\r\n'''
    response = '''HTTP/1.1 200 OK\r\nHost: localhost\r\nUser-Agent: httpie/0.9.9\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\n\r\n'''
    assert f.format_headers(request) == request
    assert f.format_headers(response) == response

# Generated at 2022-06-13 22:16:15.668050
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Setup
    environment = Environment()
    groups = ['json', 'colors']
    kwargs = {}
    formatting = Formatting(groups, environment, **kwargs)

    # Exercise
    test_data = [
        {'mime': 'application/json', 'content': '{"key": "value"}',
         'expected': '{\n    "key": "value"\n}\n'},
        {'mime': 'text/plain', 'content': '{"key": "value"}',
         'expected': '{"key": "value"}'},
        {'mime': 'text/plain', 'content': '{"key": "value"}',
         'expected': '{"key": "value"}'}
    ]


# Generated at 2022-06-13 22:16:30.399233
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Create a Formatting object to test
    test_obj = Formatting(["body"])

    # Create some fake data
    test_str = "fake out"
    test_mime = "application/json"

    # Test assertions
    # This test also serves as proof of concept for how to add
    # and use new formatters
    assert test_obj.format_body(test_str, test_mime) == test_str

# Generated at 2022-06-13 22:16:31.769488
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting.__init__

# Generated at 2022-06-13 22:16:39.890411
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    for mime in plugin_manager.get_converters_supported_mimes():
        from httpie.plugins.builtin import JSONConverter
        if mime == 'application/json':
            assert isinstance(Conversion.get_converter(mime), JSONConverter)
        else:
            assert not isinstance(Conversion.get_converter(mime), JSONConverter)


# Generated at 2022-06-13 22:16:47.201466
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    assert Formatting(['colors']).format_headers('Content-Type: application/json') == 'Content-Type: application/json'
    assert Formatting(['colors']).format_headers('Content-Type: application/json\nContent-Length: 10') == 'Content-Type: application/json\nContent-Length: 10'
    assert Formatting(['colors']).format_headers('Content-Type: application/json\nContent-Length: 10\n') == 'Content-Type: application/json\nContent-Length: 10\n'


# Generated at 2022-06-13 22:16:57.102366
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    from httpie.plugins.converter.json import JSONConverter
    from httpie.plugins.converter.urlencoded import URLEncodedConverter

    assert type(Conversion.get_converter('application/json')) is JSONConverter
    assert type(Conversion.get_converter('application/x-www-form-urlencoded')) is URLEncodedConverter
    assert ConverterPlugin.supports('application/json')
    assert ConverterPlugin.supports('application/x-www-form-urlencoded')
    assert not ConverterPlugin.supports('application/xml')
    assert Conversion.get_converter('application/xml') is None

# Generated at 2022-06-13 22:17:00.338597
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    assert converter.supports('application/json') is True

# Generated at 2022-06-13 22:17:02.696634
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    result = Conversion.get_converter('text/html')
    assert result == ConverterPlugin


# Generated at 2022-06-13 22:17:12.669673
# Unit test for constructor of class Formatting
def test_Formatting():
    fmt = Formatting([])
    assert fmt.enabled_plugins == []
    fmt = Formatting(['colors'])
    assert len(fmt.enabled_plugins) == 1
    fmt = Formatting(['colors', 'format'])
    assert len(fmt.enabled_plugins) == 2
    fmt = Formatting(['colors', 'format', 'colors'])
    assert len(fmt.enabled_plugins) == 2
    fmt = Formatting(['colors', 'header'])
    assert len(fmt.enabled_plugins) == 2

# Generated at 2022-06-13 22:17:19.861093
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatted_headers = Formatting(groups=["headers"]).format_headers("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept")
    assert(formatted_headers == "Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept\r\n")


# Generated at 2022-06-13 22:17:29.902712
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.context import Environment
    import re
    env = Environment()
    formatter = Formatting(groups=['curl'])
    headers = formatter.format_headers(headers="content-length:12")
    #first replace all the white-spaces with empty string
    #then split the ':' and get the first part
    all_keys_in_headers = [re.sub('\W+','',element.split(':')[0]).lower() for element in headers.split('\n') if len(element) > 0]
    print(all_keys_in_headers)
    assert "content-length" in all_keys_in_headers


# Generated at 2022-06-13 22:17:34.983474
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():

    fmt = Formatting(groups=["colors"])

    assert fmt.format_headers("Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8") == \
           "Accept:\x1b[93mtext/html\x1b[0m,\x1b[93mapplication/xhtml+xml\x1b[0m,\x1b[93mapplication/xml\x1b[0m;q=0.9,\x1b[93mimage/webp\x1b[0m,*/*;q=0.8"


# Generated at 2022-06-13 22:17:47.747268
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    f = Formatting(['colors'], env=Environment())
    headers = "Host: 127.0.0.1\r\n" \
              "Accept: */*\r\n" \
              "Accept-Encoding: gzip, deflate\r\n" \
              "Connection: keep-alive\r\n" \
              "Content-Length: 36\r\n" \
              "Content-Type: application/x-www-form-urlencoded\r\n" \
              "User-Agent: HTTPie/1.0.0\r\n" \
              "\r\n" \
              "var1=val1&var2=val2&var3=val3\n"

# Generated at 2022-06-13 22:17:48.753127
# Unit test for constructor of class Formatting
def test_Formatting():
    pass

# Generated at 2022-06-13 22:17:54.393562
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    format_config = Formatting(groups=['colors'])
    #assert format_config.format_body("1234567890", "text/html") == "1234567890"
    assert format_config.format_body("1234567890", "text/html")

# Generated at 2022-06-13 22:17:57.055305
# Unit test for constructor of class Formatting
def test_Formatting():
    assert "Formatting" == Formatting.__name__
    assert Formatting("groups", "env", kwargs="value").enabled_plugins == []


# Generated at 2022-06-13 22:18:02.816133
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Test when httpie.plugins.builtin.converters.JSONConverterPlugin.supports return True
    assert Conversion.get_converter("application/json") == JSONConverterPlugin("application/json")

    # Test when httpie.plugins.builtin.converters.JSONConverterPlugin.supports return False
    assert Conversion.get_converter("application/xml") is None

# Generated at 2022-06-13 22:18:14.426519
# Unit test for constructor of class Formatting
def test_Formatting():
    import json
    import requests
    import sys
    import os
    from httpie.input import ParseError
    from httpie.cli import parser
    from httpie import ExitStatus, __version__


# Generated at 2022-06-13 22:18:23.287982
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins.formatter.colors import ColorsFormatter
    from httpie.plugins.formatter.format import FormatFormatter
    from httpie.plugins.formatter.json import JSONFormatter
    from httpie.plugins.formatter.pretty import PrettyFormatter
    from httpie.plugins.formatter.colors_256 import Colors256Formatter

    colors_formatter = ColorsFormatter()
    colors256_formatter = Colors256Formatter()
    format_formatter = FormatFormatter()
    json_formatter = JSONFormatter()
    pretty_formatter = PrettyFormatter()


# Generated at 2022-06-13 22:18:28.407496
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("application/json")

# Generated at 2022-06-13 22:18:30.092982
# Unit test for constructor of class Formatting
def test_Formatting():
    assert hasattr(Formatting, "format_headers")
    assert hasattr(Formatting, "format_body")

# Generated at 2022-06-13 22:18:41.166280
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Instantiation of object x
    groups = ["highlight", "colors", "syntax"]
    x = Formatting(groups)

    # Data
    headers = "HTTP/1.1 200 OK\nServer: nginx\nDate: Sun, 15 May 2016 22:11:07 GMT\nContent-Type: application/json\nConnection: keep-alive\nAccess-Control-Allow-Credentials: true\nAccess-Control-Allow-Origin: *\nContent-Length: 116\n\n"

# Generated at 2022-06-13 22:18:49.633225
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    environment = Environment()
    environment.stdout = sys.stdout
    environment.colors = environment.COLORS_16BIT
    environment.config.output_options.prettifiers = ['colors']
    formatter = Formatting(groups=['colors'], env=environment, groups=['colors'], env=environment, colors=environment.colors)
    headers = formatter.format_headers('Content-Length: 200\nContent-Type: text/plain\n')
    assert headers == '\x1b[38;5;144mContent-Length\x1b[39m: 200\n\x1b[38;5;144mContent-Type\x1b[39m: text/plain\n'

# Generated at 2022-06-13 22:19:02.252644
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # setting up some fake data
    my_formatters = ['unicode', 'colors']
    my_plugin = Formatting(my_formatters)

    # this is the header data we will be using:
    header_data = 'HTTP/1.1 200 OK\r\n' \
                  'Content-Length: 5\r\n' \
                  'Content-Type: application/json; charset=utf-8\r\n' \
                  'ETag: b23c33e220121b8bd8c3a7b3a3f3eb3e\r\n' \
                  'Server: ExampleWS/1.0'
    out_data = my_plugin.format_headers(header_data)

    # make sure we have the same number of lines
    assert header_data.count('\n') == out

# Generated at 2022-06-13 22:19:05.145042
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors']
    env = Environment()

    formatting = Formatting(groups, env)

    assert formatting.enabled_plugins[0].env == env


# Generated at 2022-06-13 22:19:09.975846
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter(None), object)
    assert isinstance(Conversion.get_converter("abc"), object)
    assert isinstance(Conversion.get_converter("application/json"), object)
    assert isinstance(Conversion.get_converter("application/json+json"), object)

# Generated at 2022-06-13 22:19:19.976427
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    """
    test for Formatting.format_headers(headers: str) -> str
    """
    class TestPlugin:
        def format_headers(self, headers: str) -> str:
            return headers.replace(',', ';')

    args = Namespace(prettify=[])
    env = Environment()
    available_plugins = plugin_manager.get_formatters_grouped()
    available_plugins['prettify'] = [TestPlugin]

    testFormatting = Formatting(groups=['prettify'], env=env, args=args)
    headers = testFormatting.format_headers('Content-Type: application/json, Content-Length: 11')
    assert headers == 'Content-Type: application/json; Content-Length: 11'

# Generated at 2022-06-13 22:19:22.897800
# Unit test for constructor of class Formatting
def test_Formatting():
    Formatting(['table'])


if __name__ == "__main__":
    test_Formatting()

# Generated at 2022-06-13 22:19:29.042014
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.output.formatters import JSONFormatter
    from httpie.formatting import Formatting
    json_formatter = JSONFormatter()
    env = Environment()
    env.stdout.isatty = lambda: True
    formatting = Formatting(groups=['JSON'], env=env)
    assert formatting.format_headers(json_formatter.render_headers([('Header', 'Value')])) == '\x1b[37mHeader: \x1b[0m\x1b[33m"Value"\x1b[0m\n'



# Generated at 2022-06-13 22:19:41.972435
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():

    # def format_headers(self, headers: str) -> str:
    #     for p in self.enabled_plugins:
    #         headers = p.format_headers(headers)
    #     return headers

    headers = 'HTTP/1.1 200 OK\r\n'

    f = Formatting(env=Environment(colors=False, stdout_isatty=False),
                   **{'indent': 3, 'indent_body': 3})
    result1 = f.format_headers(headers)
    assert result1 == 'HTTP/1.1 200 OK\r\n'

    f = Formatting(env=Environment(colors=False, stdout_isatty=False),
                   **{'indent': 4, 'indent_body': 4})
    result2 = f.format_headers(headers)
   

# Generated at 2022-06-13 22:19:49.644539
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    fmt = Formatting(['colors'], style='solarized')
    assert fmt.enabled_plugins[0].enabled == True
    content = '{"test": "abcd"}'
    mime = 'application/json'
    assert fmt.format_body(content, mime) == '\x1b[38;5;8m{\x1b[0m\n    \x1b[38;5;40m"test"\x1b[0m\x1b[38;5;8m:\x1b[0m \x1b[38;5;245m"abcd"\x1b[0m\n\x1b[38;5;8m}\x1b[0m\n'

# Generated at 2022-06-13 22:19:54.822609
# Unit test for constructor of class Formatting
def test_Formatting():
    try:
        assert str(Formatting()) != None
        assert str(Formatting(groups=[])) != None
        assert str(Formatting(groups=['colors', 'formatters'])) != None
    except:
        return False
    return True


# Generated at 2022-06-13 22:20:02.995316
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    Formatting_instance = Formatting(groups = ["default", "colors"])
    json = '''{
    "this": "That",
    "some": {
        "a": "b"
    },
    "isTrue": true
}'''
    print(Formatting_instance.format_body(json, "application/json"))
    print(is_valid_mime(json))

if __name__ == "__main__":
    test_Formatting_format_body()

# Generated at 2022-06-13 22:20:05.028131
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # MIME type JSON
    assert (Conversion.get_converter("application/json") is not None)

# Generated at 2022-06-13 22:20:07.618406
# Unit test for constructor of class Formatting
def test_Formatting():
    format = Formatting(['colors'])
    assert format.enabled_plugins



# Generated at 2022-06-13 22:20:13.097295
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.output.streams import STDOUT_ENCODING
    from httpie.cli import get_parser
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.builtin import HTTPHeadersFormatter
    class TestFormatterPlugin(FormatterPlugin):
        name = 'test'
        description = 'test'
        def format_headers(self, headers):
            return 'test'
    parser = get_parser()
    args = parser.parse_args(['--pretty', 'all', '-v', 'http://example.com:80/'])
    output_options = vars(args)
    assert isinstance(Formatting(['Colors', 'HTTP Headers', 'HTTPBodyColors']).format_headers ('test'), str)

# Generated at 2022-06-13 22:20:18.851413
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    print("\n========== Unit testing for method format_headers of class Formatting==========")
    print("Formatted Headers: ", Formatting(groups=['colors']).format_headers("HTTP/1.1 200 OK\nContent-Type: text/plain\nContent-Length: 12\n\nhello world"))



# Generated at 2022-06-13 22:20:30.355811
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    print('# Unit test for method format_headers of class Formatting')
    print('## Case 1: There should be no processing for headers with normal strings')
    f = Formatting(groups=['colors'])
    out = f.format_headers('a:b')
    assert out == 'a:b'
    print('## Case 2: Color and syntax highlighting should be applied to headers with Json strings')
    out = f.format_headers('a:{"a":123}')
    assert out == 'a:\x1b[39m{\x1b[39m\n    \x1b[32;1m"a"\x1b[39;22m\x1b[32m: \x1b[39m\x1b[33m123\x1b[39m\n\x1b[39m}'

# Generated at 2022-06-13 22:20:36.121722
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not Conversion.get_converter('')
    assert not Conversion.get_converter('/')
    assert not Conversion.get_converter('/xml')
    assert not Conversion.get_converter('text')
    assert not Conversion.get_converter('text/')
    assert not Conversion.get_converter('text/a+b')



# Generated at 2022-06-13 22:20:41.366900
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    result = Conversion.get_converter('application/json')
    assert result is not None


# Generated at 2022-06-13 22:20:46.874283
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Test 1
    mime = "application/json"
    result = Conversion.get_converter(mime)
    assert result.mime == mime

    # Test 2
    mime = "text/html"
    result = Conversion.get_converter(mime)
    assert result is None


# Generated at 2022-06-13 22:20:57.032440
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():

    # Test Case: using the default ENABLE_FORMATTERS in environment
    formatting = Formatting(groups=[])
    # input and expected output
    headers = '''content-type: text/plain; charset=utf-8
cache-control: no-cache
content-length: 20

'''
    headers_expected = '''content-type: text/plain; charset=utf-8
cache-control: no-cache
content-length: 20

'''
    assert formatting.format_headers(headers) == headers_expected

    # Test Case: using ENABLE_FORMATTERS = [] in environment
    # Environment(ENABLE_FORMATTERS = []) means not to format the header
    formatting = Formatting(groups=[], ENABLE_FORMATTERS = [])

# Generated at 2022-06-13 22:21:00.582601
# Unit test for constructor of class Formatting
def test_Formatting():
    f1 = Formatting(['HEADERS'])
    assert len(f1.enabled_plugins) == 1
    f2 = Formatting(['BODY'])
    assert len(f2.enabled_plugins) == 1



# Generated at 2022-06-13 22:21:10.701418
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    f = Formatting(groups=['headers'], env=env)
    headers = "Content-Type: application/json\n" \
              "Content-Length: 42\n" \
              "Date: Fri, 27 Jun 2014 15:07:22 GMT\n" \
              "Connection: Keep-Alive\n"
    expected = "Content-Type: application/json\n" \
               "Content-Length: 42\n" \
               "Date: Fri, 27 Jun 2014 15:07:22 GMT\n" \
               "Connection: Keep-Alive\n"
    actual = f.format_headers(headers)
    assert expected == actual

# Generated at 2022-06-13 22:21:17.747594
# Unit test for constructor of class Formatting
def test_Formatting():
    # Given
    env = Environment()
    converter = Conversion()
    class1 = Formatting(["colors"], env, converter=converter)
    class2 = Formatting(["colors"], env)
    # When
    # Then
    assert class1.enabled_plugins[0]._converter == converter
    assert class1.enabled_plugins[0]._converter == class2.enabled_plugins[0]._converter

# Generated at 2022-06-13 22:21:22.776994
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime_in = 'application/json'
    converter = Conversion.get_converter(mime_in)
    assert converter != None
    assert converter.mime == mime_in
    assert converter.content_type == 'application/json'
    mime_in = 'xyz'
    converter = Conversion.get_converter(mime_in)
    assert converter == None

# Generated at 2022-06-13 22:21:30.256839
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.output.streams import STDOUT
    f = Formatting(env=Environment(stdout=STDOUT))
    headers = 'HTTP/1.1 200 OK\r\n' \
              'Content-Length: 14\r\n' \
              'Content-Type: text/html\r\n' \
              'Date: Wed, 20 May 2020 10:42:42 GMT\r\n\r\n'
    result = f.format_headers(headers)
    assert (headers == result)

# Generated at 2022-06-13 22:21:33.677865
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    groups = ['colors', 'colors']
    ret = Formatting(groups)
    assert ret.enabled_plugins == available_plugins['colors']

# Generated at 2022-06-13 22:21:36.360855
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    h = Formatting(['color'])
    body = h.format_body('test', 'application/json')
    assert body == 'test'


# Generated at 2022-06-13 22:21:43.495406
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    f = Formatting(['colors'], env, stream=None)
    assert len(f.enabled_plugins) > 0

# Generated at 2022-06-13 22:21:48.549176
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    f = Formatting(['colors'], style='monokai')
    assert f.format_headers('Content-Type: application/json\n') == '\x1b[38;5;208mContent-Type\x1b[39m: \x1b[38;5;208mapplication/json\x1b[39m'



# Generated at 2022-06-13 22:21:55.242117
# Unit test for constructor of class Formatting

# Generated at 2022-06-13 22:22:07.785116
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # test raw body, json, html and css
    resp = {'mime': 'text/plain', 'body': '{"name":"John"}'}
    available_plugins = plugin_manager.get_formatters_grouped()
    p = Formatting(available_plugins)
    content = p.format_body(resp['body'], resp['mime'])
    assert content == '{\n    "name": "John"\n}'
    
    resp['mime'] = 'application/json'
    content = p.format_body(resp['body'], resp['mime'])
    assert content == '{\n    "name": "John"\n}'
    
    resp['body'] = '<html><body><h1>Hello world</h1></body></html>'

# Generated at 2022-06-13 22:22:16.857747
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    from httpie.plugins.formatter.convert import JSONConverter, \
        JSONConverterException

    for mimetype in ('application/json', 'application/json+ld',
                     'application/hal+json', 'text/json',
                     'text/x-json', 'text/x-javascript',
                     'application/javascript', 'text/javascript',
                     'application/vnd.org.gtug.json-patch+json',
                     'application/vnd.api+json', 'application/vnd.geo+json'):
        assert isinstance(Conversion.get_converter(mimetype),
                          JSONConverter)
