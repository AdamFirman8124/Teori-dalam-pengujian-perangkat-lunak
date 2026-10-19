

# Generated at 2022-06-13 22:12:29.105172
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # availabe_plugins = {
    #     'pretty': [PrettyJsonFormatter, PrettyJsonPlugin],
    #     'format': [JsonFormatter, JsonPlugin],
    #     'formatvars': [FormatVariablesPlugin, FormatVariablesProcessor]
    # }
    # enabled_plugins = [PrettyJsonPlugin, FormatVariablesPlugin]
    # headers = '{"id":1,"info":"httpie"}'
    # for p in enabled_plugins:
    #     headers = p.format_headers(headers)
    #     print(headers)
    # outputs:
    # {
    #     id: 1,
    #     info: httpie
    # }
    # {
    #     id: 1,
    #     info: httpie
    # }
    pass

# Generated at 2022-06-13 22:12:32.534231
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    print("format_headers")
    groups = ["TestFormatter"]

# Generated at 2022-06-13 22:12:36.702685
# Unit test for constructor of class Formatting
def test_Formatting():
    fmt = Formatting(['colors'], env=Environment())
    assert fmt.enabled_plugins[0].name == 'Colors'
    assert fmt.enabled_plugins[0].get_config_dict() == {'env': Environment()}

# Generated at 2022-06-13 22:12:49.091679
# Unit test for method format_body of class Formatting

# Generated at 2022-06-13 22:12:51.505985
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('text/html'), ConverterPlugin)

# Generated at 2022-06-13 22:13:00.825237
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatter = Formatting(groups=['colors'], env=Environment(), **{
        'theme': 'solarized',
        'style': 'solarized',
        'colors': {'status': 'red'}
    })
    headers = formatter.format_headers('200 OK\nContent-Type: text\n\n')
    assert headers == '\x1b[31m200 OK\n\x1b[mContent-Type: text\n\n'

# Generated at 2022-06-13 22:13:05.588586
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    for pattern in ["html", "xml", "json", "json-lines"]:
        try:
            converter = Conversion.get_converter(pattern)
            assert (converter is not None)
            assert (not isinstance(converter, Exception))
        except Exception as e:
            print(e)

# Generated at 2022-06-13 22:13:08.619894
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('application/json'),
                      ConverterPlugin) is True

# Generated at 2022-06-13 22:13:21.800382
# Unit test for constructor of class Formatting
def test_Formatting():


    # test for case 1
    import os
    import sys
    p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(p)
    from httpie.plugins.registry import *
    from httpie.plugins.base import *

    class TestFormattingPlugin(FormatterPlugin):
        name = 'test_formatting_plugin'

    class TestFormattingPlugin2(FormatterPlugin):
        name = 'test_formatting_plugin2'

    class TestFormattingPlugin3(FormatterPlugin):
        name = 'test_formatting_plugin3'

    plugin_manager.register(TestFormattingPlugin)
    plugin_manager.register(TestFormattingPlugin2)

# Generated at 2022-06-13 22:13:30.512004
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatted_headers = Formatting(['highlight', 'colors'],
                                   color=True,
                                   style='paraiso-dark').format_headers('Token: Bearer 1234567890')
    assert formatted_headers == '\033[94m\033[1mToken\033[0m\033[39m: Bearer ' \
                                '\033[93m\033[1m1234567890\033[0m\033[39m'



# Generated at 2022-06-13 22:13:37.493318
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors', 'format', 'format_options', 'styles']
    env = Environment()

# Generated at 2022-06-13 22:13:45.002220
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():

    # MIME type application/json
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    assert converter is not None

    assert converter.mime == mime
    assert converter.supports(mime)

    content = "[{\"a\": 1, \"b\": 2}, {\"a\": 3, \"b\": 4}]"
    assert converter.encode(content) == "--json-seq\n[{\"a\": 1, \"b\": 2}, {\"a\": 3, \"b\": 4}]\n--json-seq--\n"
    assert converter.decode(converter.encode(content)) == content


# MIME type application/x-www-form-urlencoded
    mime = 'application/x-www-form-urlencoded'

# Generated at 2022-06-13 22:13:47.651074
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert(Conversion.get_converter("application/json"))
    assert(Conversion.get_converter("text/plain"))
    assert(Conversion.get_converter("application/xml"))


# Generated at 2022-06-13 22:13:50.213098
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fmt1 = Formatting(["color"])
    assert "\033[32m" in fmt1.format_headers("HTTP/1.1 200 OK")
    fmt2 = Formatting([])
    assert "\033[32m" not in fmt2.format_headers("HTTP/1.1 200 OK")


# Generated at 2022-06-13 22:13:58.593264
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(groups=["format", "colors", "colors-cli"])
    data_1 = f.format_body(
        '{"id": 1, "name": "Test"}', 'application/json')
    data_2 = f.format_body(
        '{"id": 1, "name": "Test"}', 'application/administrator')
    assert data_1 != data_2
    assert data_1 == """\
{
    "id": 1,
    "name": "Test"
}
"""



# Generated at 2022-06-13 22:14:09.566521
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from .helpers import get_response as mock_get_response
    groups = ['json']
    types = {'json': 'application/json'}
    env = Environment()
    kwargs = {}
    f = Formatting(groups, env, **kwargs)
    response_content = mock_get_response()
    formatted_content = f.format_body(response_content, types['json'])
    if (groups[0] != 'all'):  # If it is not the group all
        assert len(formatted_content.strip().split('\n')) != len(response_content.strip().split('\n'))
    else:  # Otherwise
        assert len(formatted_content.strip().split('\n')) == len(response_content.strip().split('\n'))

# Generated at 2022-06-13 22:14:14.901890
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('application/json'), ConverterPlugin)
    assert not Conversion.get_converter('text/html')
    assert Conversion.get_converter('text/html') == None
    assert Conversion.get_converter('json') == None


# Generated at 2022-06-13 22:14:20.668642
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter: Optional[ConverterPlugin] = Conversion.get_converter('application/json')
    assert converter is not None

    converter: Optional[ConverterPlugin] = Conversion.get_converter('application/yaml')
    assert converter is not None



# Generated at 2022-06-13 22:14:29.852039
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    assert isinstance(Conversion.get_converter(mime), ConverterPlugin)
    mime = 'application/xml'
    assert isinstance(Conversion.get_converter(mime), ConverterPlugin)
    mime = 'text/'
    assert Conversion.get_converter(mime) is None
    mime = ''
    assert Conversion.get_converter(mime) is None
    mime = 'application/javascript'
    assert Conversion.get_converter(mime) is None

# # Unit test for class Formatting
# def test_Formatting():
#     groups = ['colors']
#     kwargs = {'colors': {'tag_error': '33'},
#               'compress_level': 6}
#    

# Generated at 2022-06-13 22:14:35.466452
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'Mime/type'
    converter = Conversion.get_converter(mime)
    assert isinstance(converter, ConverterPlugin)
    assert converter.supports(mime)


# Generated at 2022-06-13 22:14:40.941225
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert converter is not None

# Generated at 2022-06-13 22:14:53.157136
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # https://tools.ietf.org/html/rfc7159
    JSON_MIME = "application/json"
    assert is_valid_mime(JSON_MIME)
    converter = Conversion.get_converter(JSON_MIME)
    assert converter
    j = converter.loads(b'["foo", {"bar":["baz", null, 1.0, 2]}]')
    assert [u'foo', {u'bar': [u'baz', None, 1.0, 2]}] == j

    # https://tools.ietf.org/html/rfc6839
    HTML_MIME = "text/html"
    assert is_valid_mime(HTML_MIME)
    converter = Conversion.get_converter(HTML_MIME)
    assert converter

# Generated at 2022-06-13 22:15:00.251177
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_Formatting = Formatting(groups=["Colors"])
    assert test_Formatting.format_headers("Content-Type: text/plain\nServer: nginx/1.14.0 (Ubuntu)") == \
        '\x1b[37m\x1b[1mContent-Type\x1b[0m: \x1b[36mtext/plain\x1b[0m\n\x1b[37m\x1b[1mServer\x1b[0m: \x1b[36mnginx/1.14.0 (Ubuntu)\x1b[0m'


# Generated at 2022-06-13 22:15:04.590517
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion.get_converter("application/json")
    # Test if converter class is returned correctly
    assert c.__class__.__name__ == "JsonConverter"


# Generated at 2022-06-13 22:15:13.934720
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.builtin import JSONFormatter
    from httpie.plugins.registry import plugin_manager
    from httpie import ExitStatus
    from httpie.compat import is_windows
    from httpie.client import JSON_ACCEPT

    import sys
    import json
    import collections

    # Test for empty body
    fm = Formatting(['builtin'], env=Environment(stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr,
                                                 colors=False, verify=True, debug=False))
    content = fm.format_body('', JSON_ACCEPT)

# Generated at 2022-06-13 22:15:19.091586
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('text/html')
    assert converter.supports('text/html') is True
    assert converter.supports('text/html; charset=utf-8') is True
    assert converter.supports('application/json; charset=utf-8') is False

# Generated at 2022-06-13 22:15:28.939786
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    f = Formatting(groups=['shell-compact', 'colors'])
    h = 'HTTP/1.1 200 OK\nAccept-Ranges: bytes\nCache-Control: max-age=604800\n\
Content-Encoding: gzip\nContent-Type: text/html; charset=UTF-8\nDate: Mon, 23\
 May 2016 11:38:35 GMT\nEtag: "359670651+gzip"\nExpires: Mon, 30 May 2016\
 11:38:35 GMT\nLast-Modified: Fri, 09 Aug 2013 23:54:35 GMT\nServer: ECS\
(oxr/831F)\nVary: Accept-Encoding, Cookie\nX-Cache: HIT\n\n'

# Generated at 2022-06-13 22:15:32.375680
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert str(converter) == "JSONConverter"

# Generated at 2022-06-13 22:15:38.278023
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors', 'format']
    env = Environment()
    f = Formatting(groups, env, style='solarized')
    assert len(f.enabled_plugins) == 2
    assert f.enabled_plugins[0].info == 'colored'
    assert f.enabled_plugins[1].info == 'formatted'

# Generated at 2022-06-13 22:15:41.946656
# Unit test for constructor of class Formatting
def test_Formatting():
    testGroup = []
    testGroup.append("testgroup1")
    testGroup.append("testgroup2")
    formatting = Formatting(testGroup)
    assert formatting.enabled_plugins == []


# Generated at 2022-06-13 22:15:58.588822
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    args = ["json", "highlight"]
    input_headers = ""
    expected_output = "headers:\n\tAccept-Encoding: gzip, deflate\n\tConnection: keep-alive\n\tHost: 127.0.0.1:9001\n"
    actual_output = Formatting(args).format_headers(input_headers)
    assert actual_output == expected_output

    args = ["json", "highlight"]
    input_headers = "Accept-Encoding: gzip, deflate\nConnection: keep-alive\nHost: 127.0.0.1:9001\n"

# Generated at 2022-06-13 22:15:59.270021
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    pass

# Generated at 2022-06-13 22:16:02.358139
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    fmt = Formatting(['formatters'], env)
    assert len(fmt.enabled_plugins) == 1

if __name__ == "__main__":
    test_Formatting()

# Generated at 2022-06-13 22:16:08.168919
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """This is a unit test for method get_converter of class Conversion"""
    mime = "application/json"
    assert is_valid_mime(mime)

    converter = Conversion.get_converter(mime)
    assert isinstance(converter, ConverterPlugin)


# Generated at 2022-06-13 22:16:15.429262
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # 
    class TestFormatterPlugin:
        def __init__(self, env=None, **kwargs):
            pass
        def format_body(self, content, mime):
            return content
    plugin_manager.formatter_plugins = [TestFormatterPlugin]
    f = Formatting([])
    assert f.format_body('test', 'text/plain') == 'test'
    # does not execute format_body for unsupported mime type
    assert f.format_body('test', 'invalid mime type') == 'test'

# Generated at 2022-06-13 22:16:32.719602
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = "application/json"
    conversion = Conversion()
    converter_class = conversion.get_converter(mime) 
    assert converter_class.mime_type == mime
    assert converter_class.supported_mime_types == ['application/json']
    mime = "text/json"
    conversion = Conversion()
    converter_class = conversion.get_converter(mime) 
    assert converter_class.mime_type == mime 
    assert converter_class.supported_mime_types == []
    mime = "application/xml"
    conversion = Conversion()
    converter_class = conversion.get_converter(mime) 
    assert converter_class.mime_type == mime 
    assert converter_class.supported_mime_types == ['application/xml']


# Generated at 2022-06-13 22:16:42.018350
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    '''
    This method will test the format_headers function of the Formatting class.
    :return: True or False
    '''
    headers = 'Host: localhost\nUser-Agent: HTTPie/0.9.2\nAccept-Encoding: gzip, deflate\nAccept: application/json, */*\nConnection: keep-alive'
    groups = ['colors', 'format', 'colors']

    env = Environment()
    formatting = Formatting(groups, env)
    content = formatting.format_headers(headers)
    assert content == 'Host: localhost\nUser-Agent: HTTPie/0.9.2\nAccept-Encoding: gzip, deflate\nAccept: application/json, */*\nConnection: keep-alive'




# Generated at 2022-06-13 22:16:54.104838
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatting = Formatting(groups=['json'], env=Environment(colors=True))
    input = b'{"a": "b", "c": 1}'
    output = formatting.format_body(input, mime='application/json')
    assert output == b'{\n    \x1b[34;1m"a"\x1b[39;49;22m: \x1b[33m"b"\x1b[39;49;22m,\n    \x1b[34;1m"c"\x1b[39;49;22m: \x1b[33m1\x1b[39;49;22m\n}'



# Generated at 2022-06-13 22:16:59.265908
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=['colors'])
    # f.enabled_plugins is a list of plugins with class name starting with 'Colors'
    assert all([plugin.__class__.__name__.startswith('Colors') for plugin in f.enabled_plugins])

# Generated at 2022-06-13 22:17:01.713968
# Unit test for constructor of class Formatting
def test_Formatting():
    fmt = Formatting()
    print(fmt.format_headers(''))


# Generated at 2022-06-13 22:17:16.770321
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    assert Formatting.format_body('{"name": "tonny"}', "application/json") == '{\n    "name": "tonny"\n}'

# Generated at 2022-06-13 22:17:28.369131
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Instantiate the Formatting class
    f = Formatting(["colors"], env=Environment())
    
    # Test case 1: content is empty
    print("Test case 1: content is empty")
    test_content = ""
    if f.format_body(test_content, "application/json") == test_content:
        print("Passed")
    else:
        print("Failed")

    # Test case 2: content is an empty json
    print("")
    print("Test case 2: content is an empty json")
    test_content = "{\n\n}"
    if f.format_body(test_content, "application/json") == test_content:
        print("Passed")
    else:
        print("Failed")

    # Test case 3: content is an empty html file
    print("")
   

# Generated at 2022-06-13 22:17:35.258676
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
	input_data = "What is your name?"
	input_mime = "text/plain"
	expected_data = "What is your name?"
	output_data = Formatting(groups=["text"]).format_body(input_data, input_mime)
	print("Input: ", input_data)
	print("Input MIME: ", input_mime)
	print("EXPECTED: ", expected_data)
	print("OUTPUT: ", output_data)
	assert output_data == expected_data

# Generated at 2022-06-13 22:17:42.969672
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """
    Unit test for method format_body of class Formatting
    """
    groups = ["format", "colors"]
    kwargs = {}
    mime = "test"
    content = '{test}'
    f = Formatting(groups=groups, **kwargs)
    test_result = f.format_body(content, mime)

    assert test_result == content
    assert type(test_result) == str


# Generated at 2022-06-13 22:17:51.132880
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    print("Testing method format_headers of class Formatting...")

# Generated at 2022-06-13 22:17:55.902897
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("rfc")
    assert converter is None
    converter = Conversion.get_converter("application/json")
    assert "application/json" == converter.mime



# Generated at 2022-06-13 22:18:05.741369
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    plugin_manager.load_converters()
    assert isinstance(Conversion.get_converter('application/json'), ConverterPlugin)
    assert Conversion.get_converter('application/json').__class__.__name__ == 'JsonConverter'
    assert isinstance(Conversion.get_converter('application/vnd.api+json'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('application/jsonxml'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('application/xml'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('application/x-www-form-urlencoded'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('application/x-yaml'), ConverterPlugin)

# Generated at 2022-06-13 22:18:09.998805
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    cv = Conversion.get_converter("application/json")
    assert cv.mime == "application/json"
    assert cv.__class__.__name__ == "JSONConverter"



# Generated at 2022-06-13 22:18:18.452859
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    assert "test" == Formatting([]).format_body("test", "")
    assert "test" == Formatting([], to_string=True).format_body("test", "")
    assert "test" == Formatting([], to_string=False).format_body("test", "")

    assert "test" == Formatting(["colors"]).format_body("test", "")
    assert "test" == Formatting(["colors"], to_string=True).format_body("test", "")
    assert "test" == Formatting(["colors"], to_string=False).format_body("test", "")

    assert "test" == Formatting(["colors"], to_string=False).format_body("test", "")
    assert '\033[1;32m"test"\033[0m' == Formatting

# Generated at 2022-06-13 22:18:25.310646
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    p1 = Formatting(['colors'])
    mime = 'application/json'
    content = '{ "test": "data" }'

    content = p1.format_body(content, mime)
    assert content == '{\n  "test": "data"\n}\n'

# Generated at 2022-06-13 22:18:48.761749
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    a = Formatting(groups=[])
    text = """HTTP/1.0 200 OK\r
    Content-Type: application/json\r
    Content-Length: 2\r
    \r
    {}\r
    HTTP/1.0 200 OK\r
    Content-Type: text/html\r
    Content-Length: 2\r
    \r
    {}\r
    \r
    """
    ans = """HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 2
    
    {}
    HTTP/1.0 200 OK
    Content-Type: text/html
    Content-Length: 2
    
    {}
    
    """
    assert(ans == a.format_headers(text))
    a = Formatting(groups=['colors'])

# Generated at 2022-06-13 22:18:59.310730
# Unit test for constructor of class Formatting
def test_Formatting():
    # empty groups
    f = Formatting([])
    assert f.enabled_plugins == []
    # none exists group
    f = Formatting(["none_exist"])
    assert f.enabled_plugins == []
    # group not enabled
    plugin_manager.register_plugin(JSONDeserializationPlugin())
    f = Formatting(["json"])
    assert f.enabled_plugins == []
    plugin_manager.unregister_plugin(JSONDeserializationPlugin)
    # normal case
    plugin_manager.register_plugin(JSONDeserializationPlugin())
    f = Formatting(["json"], json=True)
    assert isinstance(f.enabled_plugins[0], JSONDeserializationPlugin)
    plugin_manager.unregister_plugin(JSONDeserializationPlugin)



# Generated at 2022-06-13 22:19:01.533508
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert converter != None

# Generated at 2022-06-13 22:19:09.569679
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    mock = Formatting(['colors'], colors=True)
    assert mock.format_headers('HTTP/1.1 200 OK\r\nContent-Type: application/json') == '\x1b[37m\x1b[1mHTTP/1.1 \x1b[32m\x1b[1m200 \x1b[32m\x1b[22m\x1b[37m\x1b[22mOK\r\nContent-Type: application/json\x1b[39m\x1b[22m'


# Generated at 2022-06-13 22:19:14.226083
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion.get_converter('text/html')
    assert c.__class__.__name__ == 'HTMLConverter'
    assert c.supports('text/html')
    assert c.mime == 'text/html'


# Generated at 2022-06-13 22:19:16.000227
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    expected_result = ConverterPlugin("text/html")
    actual_result = Conversion.get_converter("text/html")
    assert actual_result is not None

# Generated at 2022-06-13 22:19:17.905769
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    formatting = Formatting(groups=['colors'], env = env)



# Generated at 2022-06-13 22:19:25.693399
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=['colors'])
    assert f.enabled_plugins
    assert isinstance(f.enabled_plugins[0], (ConverterPlugin,))
    assert f.enabled_plugins[0].supports('text/html')
    assert f.enabled_plugins[0].__class__.__name__ == 'HtmlToTerminalConverter'
    assert f.enabled_plugins[0].__class__.mime_types == {'text/html'}
    assert f.enabled_plugins[0].enabled == True


# The following tests for PrecisionPlugin were extracted from tests for HttpResponse

# Generated at 2022-06-13 22:19:36.827293
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_data = ['/home/travis/build/jakubroztocil/httpie/tests/data/headers-0.txt', '/home/travis/build/jakubroztocil/httpie/tests/data/headers-1.txt', '/home/travis/build/jakubroztocil/httpie/tests/data/headers-2.txt']
    groups = ['formatter', 'colors']
    env = Environment()
    kwargs = {}
    formatter = Formatting(groups, env, **kwargs)
    for test_file in test_data:
        with open(test_file) as f:
            ret = formatter.format_headers(f.read())
            print(ret)


# Generated at 2022-06-13 22:19:47.595966
# Unit test for constructor of class Formatting
def test_Formatting():
    # testing constructor with given parameters and no keyword arguments
    expected = {'AvailableProcessors': ['Processor1', 'Processor2', 'Processor3']}
    actual = []
    available_plugins = {'AvailableProcessors': ['Processor1', 'Processor2', 'Processor3']}

    for group in ['AvailableProcessors']:
        for cls in available_plugins[group]:
            actual.append(cls)

    assert len(expected) == len(actual)
    assert all(elem in expected for elem in actual)

    # testing constructor with given parameters, mime_types and keyword arguments
    expected = {'key': 'value'}
    actual = Formatting(['AvailableProcessors'], mime_types=['MIME1', 'MIME2'], key='value').enabled_plugins


# Generated at 2022-06-13 22:20:03.269976
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """Test method get_converter."""
    converter = Conversion.get_converter(None)
    assert converter is None

    converter = Conversion.get_converter("application/json")
    assert converter is not None


# Generated at 2022-06-13 22:20:05.775494
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=['colors'], env=Environment())
    assert(type(f.enabled_plugins).__name__ == 'list')
    assert(type(f.enabled_plugins[0]).__name__ == 'ColorsFormatter')

# Generated at 2022-06-13 22:20:09.671239
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    obj = Formatting(groups=["json"])
    assert obj.format_body("{\"a\":\"b\"}", "application/json") == "{\"a\":\"b\"}"


# Generated at 2022-06-13 22:20:19.290695
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c1 = Conversion.get_converter('application/json')
    assert c1.mimetype == 'application/json'
    c2 = Conversion.get_converter('application/json; charset=UTF-8')
    assert c2.mimetype == 'application/json'
    assert c2.charset == 'UTF-8'
    c3 = Conversion.get_converter('text/json; charset=UTF-8')
    assert c3.mimetype == 'text/json'
    assert c3.charset == 'UTF-8'

# Generated at 2022-06-13 22:20:25.568121
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    import httpie
    httpie.plugins.registry.plugin_manager.load_installed()
    formatter = Formatting(['format'])
    assert formatter.format_body('<html>', 'application/html') == '<html>'
    assert formatter.format_body('[1,2,3]', 'application/json') == '[1,2,3]'

# Generated at 2022-06-13 22:20:31.631310
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins.builtin import HTTPHeaders
    env = Environment()
    env.stdout = BytesIO()
    available_plugins = plugin_manager.get_formatters_grouped()
    group = 'headers'
    for cls in available_plugins[group]:
        p = cls(env=env)

# Generated at 2022-06-13 22:20:38.993423
# Unit test for constructor of class Formatting
def test_Formatting():
    # Validate that constructor returns list of plugins
    # when a list of valid plugin names is given.
    f = Formatting(["colors"])
    assert len(f.enabled_plugins) > 0
    # Validate that constructor returns empty list when
    # the list is empty.
    f = Formatting([])
    assert len(f.enabled_plugins) == 0
    # Validate that constructor returns empty list when
    # the list is None.
    f = Formatting(None)
    assert len(f.enabled_plugins) == 0

# Generated at 2022-06-13 22:20:45.123339
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    env = Environment()
    kwargs = {}
    groups = ['advanced']
    formatting = Formatting(groups, env, **kwargs)
    headers_string = '''
HTTP/1.1 200 OK
Date: Tue, 23 Jun 2015 11:38:34 GMT
ETag: "1d3-51f6609240717"
Content-Type: application/json;name="item"

'''
    expected_headers_string = '''
HTTP/1.1 200 OK
Date: Tue, 23 Jun 2015 11:38:34 GMT
ETag: "1d3-51f6609240717"
Content-Type: application/json;name="item"

'''
    assert formatting.format_headers(headers_string) == expected_headers_string


# Generated at 2022-06-13 22:20:47.020544
# Unit test for constructor of class Formatting
def test_Formatting():
    a = Formatting(groups=['colors'])
    print(a)

# Generated at 2022-06-13 22:20:50.133770
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    print("Testing method format_headers of class Formatting")
    env = Environment()
    headers = '{"hello":"world"}'
    formatter = Formatting(groups=['JSON'], env=env)
    print("Actual Result")
    print(formatter.format_headers(headers))
    print("Expected Result")
    print("""{
    "hello": "world"
}""")



# Generated at 2022-06-13 22:21:04.375135
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("application/json") == None

# Generated at 2022-06-13 22:21:10.653944
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins.builtin import HTTPHeadersProcessor

    result = Formatting(['HTTPHeadersProcessor']).format_headers('{"Name": "Elon Musk"}')
    assert result == '{\n    "Name": "Elon Musk"\n}'


# Generated at 2022-06-13 22:21:16.322311
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("text/html"), ConverterPlugin)
    assert Conversion.get_converter("text/html").mime == "text/html"
    assert not Conversion.get_converter("text/plain")
    assert not Conversion.get_converter("abc")



# Generated at 2022-06-13 22:21:19.577380
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ["colors", "format", "key-value"]
    env = Environment()
    formatting = Formatting(groups, env)
    assert isinstance(formatting, Formatting)


# Generated at 2022-06-13 22:21:30.046890
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors']
    env = Environment()
    # test for 12 different plugins
    for plugin in ['colors', 'colors', 'colors', 'colors', 'colors', 'colors', 'colors',\
        'colors', 'colors', 'colors', 'colors', 'colors']:
        kwargs = {'theme': plugin}
        assert Formatting(groups, env=env, **kwargs).enabled_plugins[0].env == env
        assert Formatting(groups, env=env, **kwargs).enabled_plugins[0].theme == kwargs['theme']


# Generated at 2022-06-13 22:21:40.045560
# Unit test for constructor of class Formatting
def test_Formatting():
    def test1(groups: List[str], env=Environment(), **kwargs):
        """
        :param groups: names of processor groups to be applied
        :param env: Environment
        :param kwargs: additional keyword arguments for processors

        """
        available_plugins = plugin_manager.get_formatters_grouped()
        enabled_plugins = []
        for group in groups:
            for cls in available_plugins[group]:
                p = cls(env=env, **kwargs)
                if p.enabled:
                    enabled_plugins.append(p)
        return enabled_plugins

    def test2(headers: str):
        for p in enabled_plugins:
            headers = p.format_headers(headers)
        return headers


# Generated at 2022-06-13 22:21:50.625050
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.compat import urlsplit, parse_qsl
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    from httpie.output.streams import get_binary_stream
    from httpie.output.streams import DEFAULT_STREAM
    from httpie.output.utils import get_binary_stream_kwargs
    from httpie.plugins.default import HTMLFormatter
    from httpie.plugins.default import PrettyFormatter
    from httpie.plugins.default import JSONFormatter
    env = Environment()
    stream = get_binary_stream(stream_name=DEFAULT_STREAM, 
                               is_tty=env.is_windows,
                               **get_binary_stream_kwargs(env))
    header = '' 

# Generated at 2022-06-13 22:21:53.784507
# Unit test for constructor of class Formatting
def test_Formatting():
    a = Formatting(['colors'], Environment())
    assert a.enabled_plugins != []
    assert len(a.enabled_plugins) == 1
    assert not a.enabled_plugins[0] is None
    assert a.enabled_plugins[0].__class__.__name__ == "ColorsFormatter"


# Generated at 2022-06-13 22:21:58.354231
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    expected = 'application/json'
    actual = Conversion.get_converter(expected).mime
    assert actual == expected, 'Test result should be json'


# Generated at 2022-06-13 22:22:05.361645
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not is_valid_mime('')
    assert not is_valid_mime('ab')
    assert not is_valid_mime('a/b/c')
    assert is_valid_mime('a/b')

    assert Conversion.get_converter('') is None

    assert Conversion.get_converter('a/b').mime == 'a/b'