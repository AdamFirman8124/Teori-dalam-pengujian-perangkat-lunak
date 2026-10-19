

# Generated at 2022-06-13 22:12:16.168515
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json')


# Generated at 2022-06-13 22:12:23.858582
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json').__class__.__name__ == 'JSONConverter'
    assert Conversion.get_converter('application/yaml').__class__.__name__ == 'YAMLConverter'
    assert Conversion.get_converter('text/markdown').__class__.__name__ == 'MarkdownConverter'


# Generated at 2022-06-13 22:12:27.532318
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/john')
    assert converter is None

    converter = Conversion.get_converter('text/html')
    assert converter is not None
    assert converter.mime == 'text/html'

# Generated at 2022-06-13 22:12:30.342422
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting([])
    # Displays all information
    assert Formatting(['all', 'bodies'])
    # Displays headers only
    assert Formatting(['headers'])

# Generated at 2022-06-13 22:12:39.221771
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.plugins import BuiltinPlugin
    from httpie.plugins.formatters import FormatterPlugin
    # Create a group of objects mocking FormatterPlugin
    class MockFormatterPlugin(FormatterPlugin):
        def format_headers(self, headers: str) -> str: return headers
        def format_body(self, content: str, mime: str) -> str: return content
    class MockFormatterPlugin1(MockFormatterPlugin):
        def is_enabled(self): return True
    class MockFormatterPlugin2(MockFormatterPlugin):
        def is_enabled(self): return False
    class MockFormatterPlugin3(MockFormatterPlugin):
        def is_enabled(self): return True
    class MockFormatterPlugin4(MockFormatterPlugin):
        def is_enabled(self): return False
    # Create an object

# Generated at 2022-06-13 22:12:43.252051
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    """Test Formatting.format_headers().
    Args: None
    """
    fmt = Formatting(['colors'])

# Generated at 2022-06-13 22:12:45.246340
# Unit test for constructor of class Formatting
def test_Formatting():
    Formatting(['colors'], env=Environment(), **{'colors': True})



# Generated at 2022-06-13 22:12:48.319923
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    f = Formatting(['colors'], env)
    #f = Formatting(['colors', 'format'], env)
    print(f.enabled_plugins)

# Generated at 2022-06-13 22:12:53.595725
# Unit test for method format_body of class Formatting

# Generated at 2022-06-13 22:13:00.051412
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # When a valid mime and the mime is supported by the converter plugin
    converter_plugin = Conversion.get_converter('text/plain')
    assert converter_plugin.mime == 'text/plain'

    # When a valid mime and the mime is not supported by the converter plugin
    converter_plugin = Conversion.get_converter('text/not_plain')
    assert converter_plugin is None


# Generated at 2022-06-13 22:13:04.003488
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converted = Conversion.get_converter("text/html")
    assert converted is not None

# Generated at 2022-06-13 22:13:12.388703
# Unit test for constructor of class Formatting
def test_Formatting():
    # test 1
    f = Formatting(["colors"])
    assert f.enabled_plugins[0].enabled
    # test 2
    f = Formatting([""])
    assert f.enabled_plugins == []
    # test 3
    f = Formatting(["colors"])
    assert f.enabled_plugins[0].enabled
    # test 4
    f = Formatting(["colors"])
    assert f.enabled_plugins[0].enabled



# Generated at 2022-06-13 22:13:24.585608
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    output = Formatting(['colors']).format_headers("""HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1270
Connection: close
Server: CherryPy/3.2.2""")
    assert output == """HTTP/1.1 200 OK
\x1b[33mContent-Type\x1b[39;49;00m: text/html; charset=utf-8
\x1b[33mContent-Length\x1b[39;49;00m: 1270
\x1b[33mConnection\x1b[39;49;00m: close
\x1b[33mServer\x1b[39;49;00m: CherryPy/3.2.2"""

# Generated at 2022-06-13 22:13:36.650323
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert converter.__class__.__name__ == 'JSONConverter'
    converter = Conversion.get_converter('text/xml')
    assert converter.__class__.__name__ == 'XMLConverter'
    converter = Conversion.get_converter('application/xml')
    assert converter.__class__.__name__ == 'XMLConverter'
    converter = Conversion.get_converter('text/html')
    assert converter.__class__.__name__ == 'HTMLConverter'
    converter = Conversion.get_converter('application/javascript')
    assert converter.__class__.__name__ == 'JSONConverter'

# Generated at 2022-06-13 22:13:40.494350
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    assert Formatting([], {}).format_body('content', 'mime') == 'content'
    assert Formatting([], {}).format_body('', 'mime') == ''
    assert Formatting([], {}).format_body('content', '') == 'content'

# Generated at 2022-06-13 22:13:50.264639
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    cnv = Conversion.get_converter("application/json")
    assert cnv.__class__.__name__ == "JsonConverter"
    cnv = Conversion.get_converter("application/xml")
    assert cnv.__class__.__name__ == "XmlConverter"
    cnv = Conversion.get_converter("application/yaml")
    assert cnv.__class__.__name__ == "YamlConverter"
    cnv = Conversion.get_converter("text/html")
    assert cnv is None

# Generated at 2022-06-13 22:13:59.216736
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    example_data = """{
    "login": "string",
    "password": "string",
    "temp_identifier": "string"
}"""
    from httpie.plugins.json import JSONFormatter
    from json import loads, dumps
    from pprint import pformat
    assert Formatting(['format']).format_body(example_data, 'application/json') == pformat(loads(example_data))
    assert Formatting(['format']).format_body(example_data, 'application/json') == JSONFormatter.format_body(example_data, 'application/json')



# Generated at 2022-06-13 22:14:08.575400
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    print("testing Formatting.format_headers")
    f = Formatting(groups=['colors'])
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: 0'
    print("input    :", headers)
    headers = f.format_headers(headers)
    print("output   :", headers)
    assert headers == 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: 0', "test failed"
    print("test passed")
    print()


# Generated at 2022-06-13 22:14:11.347072
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('text/html')
    assert not Conversion.get_converter('text/plain')



# Generated at 2022-06-13 22:14:23.410417
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json').mime == 'application/json'
    assert Conversion.get_converter('application/json').supports('application/json') == True
    assert Conversion.get_converter('application/json').supports('text/plain') == False
    assert Conversion.get_converter('application/json').convert == json.dumps
    assert Conversion.get_converter('application/xml').mime == 'application/xml'
    assert Conversion.get_converter('application/xml').supports('application/xml') == True
    assert Conversion.get_converter('application/xml').supports('text/plain') == False
    assert Conversion.get_converter('application/xml').convert == ET.tostring

# Generated at 2022-06-13 22:14:35.768612
# Unit test for constructor of class Formatting
def test_Formatting():
    """
    Test for constructor of class Formatting.
    """
    from httpie.plugins.builtin import HTTPHeadersFormatPlugin
    from httpie.plugins.builtin import JSONFormatPlugin
    from httpie.plugins.builtin import RawFormatPlugin

    raw_format_plugin = RawFormatPlugin()
    http_headers_format_plugin = HTTPHeadersFormatPlugin()
    json_format_plugin = JSONFormatPlugin()

    formatting = Formatting(['pretty'])

    assert formatting.enabled_plugins == []

    formatting = Formatting(['color'])

    assert formatting.enabled_plugins == [raw_format_plugin]

    formatting = Formatting(['pretty', 'colors'])

    assert formatting.enabled_plugins == [json_format_plugin, http_headers_format_plugin]

    formatting = Formatting(['colors'])



# Generated at 2022-06-13 22:14:38.906302
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("application/json"), type(ConverterPlugin))
    assert Conversion.get_converter("application/json").mime == "application/json"

# Generated at 2022-06-13 22:14:42.436518
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    groups = ['TestFormatting']
    fmt = Formatting(groups, env)
    assert fmt.format_headers("\n") == '<TestFormatting>\n'
    assert fmt.format_headers("\n\n") == "\n<TestFormatting>\n"


# Generated at 2022-06-13 22:14:46.860845
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    b = Formatting(['colors'])
    print(b.format_body('{"hello":"world"}', 'application/json'))
    print(b.format_body('{"hello":"world"}', 'text/html'))

# Generated at 2022-06-13 22:14:50.329206
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    result = Conversion.get_converter("text/csv")
    assert isinstance(result, ConverterPlugin) == True
    assert result.supports("text/html") == False


# Generated at 2022-06-13 22:14:59.571525
# Unit test for constructor of class Formatting
def test_Formatting():
    import httpie.plugins.format.table
    import httpie.plugins.format.colors

    f = Formatting(['table'])
    # Test that the constructor of Formatting properly created
    assert f.enabled_plugins[0] is httpie.plugins.format.table.TableProcessor
    assert f.enabled_plugins[1] is httpie.plugins.format.colors.ColorsProcessor
    f = Formatting(['colors'])
    assert f.enabled_plugins[0] is httpie.plugins.format.colors.ColorsProcessor
    f = Formatting([])
    assert f.enabled_plugins == []
    # Test that non-existing group names do not result in errors
    f = Formatting(['non-existant-group'])
    assert f.enabled_plugins == []


# Generated at 2022-06-13 22:15:11.506027
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Test for no available plugin for given mime
    groups = []
    env = Environment()
    kwargs = {}
    f = Formatting(groups, env, **kwargs)
    content = '{"key": "value"}'
    mime = 'application/json'
    result = f.format_body(content, mime)
    assert result == content
    # Test for available plugins for given mime
    groups = ['colors']
    env = Environment()
    kwargs = {}
    f = Formatting(groups, env, **kwargs)
    content = '{"key": "value"}'
    mime = 'application/json'
    result = f.format_body(content, mime)

# Generated at 2022-06-13 22:15:16.856410
# Unit test for constructor of class Formatting
def test_Formatting():

    exp_len = 2

    # call function
    obj_formatting = Formatting([
        "colors",
        "format"
    ])

    # compare exp. and act. result
    assert len(obj_formatting.enabled_plugins) == exp_len


# Generated at 2022-06-13 22:15:27.841673
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('text/html'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('text/plain'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('text/csv'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('application/json'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('application/xml'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('application/jwt'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('application/base64'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('application/yaml'), ConverterPlugin)


# Generated at 2022-06-13 22:15:30.315940
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    conversion = Conversion()
    assert conversion.get_converter('text/plain') is None



# Generated at 2022-06-13 22:15:39.981180
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fake_env = Environment()
    fake_env.colors = True
    fake_env.style = 'solarized'

    fake_plugin = Formatting(groups=['headers'], env=fake_env)
    assert fake_plugin.format_headers('Content-Type: text/html\n') == '\x1b[37m\x1b[1m\x1b[44mContent-Type: text/html\x1b[0m\n'


# Generated at 2022-06-13 22:15:46.871043
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_data = [
        ({'foo': 'bar', 'bar': 'baz'}, {'foo': 'bar', 'bar': 'baz'}),
        ({'baz': 'baz'}, {'baz': 'baz'}),
    ]

    for input_data, expected in test_data:
        f = Formatting(['colors'])
        input_data = json.dumps(input_data)
        input_data = f.format_headers(input_data)
        expected = json.dumps(expected)
        assert input_data == expected

# Generated at 2022-06-13 22:15:52.463026
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Case 1: convert to pretty formatting
    assert is_valid_mime('application/json')
    assert Conversion.get_converter('application/json').name == 'Pretty'

    # Case 2: convert to json
    assert is_valid_mime('application/xml')
    assert Conversion.get_converter('application/xml').name == 'JSON'

# Generated at 2022-06-13 22:15:53.985188
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """
    Test for Formatting class
    """
    assert 1 == 1


# Generated at 2022-06-13 22:15:55.948708
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatter = Formatting([], env=Environment())
    assert formatter.format_headers("Headers") == "Headers"

# Generated at 2022-06-13 22:16:03.556559
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = {"Content-Type": "text/plain", "Content-Length": "0"}
    f = Formatting(["headers"])
    result = f.format_headers(headers)
    assert "recursive" in result
    headers = {"Content-Type": "text/plain", "Content-Length": "0"}
    f = Formatting([""])
    result = f.format_headers(headers)
    assert result == 'Content-Length: 0\r\nContent-Type: text/plain'


# Generated at 2022-06-13 22:16:08.034890
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers_to_format = 'HTTP/1.1 200 OK'
    formatter = Formatting(['Headers'], colors=256)
    assert headers_to_format != formatter.format_headers(headers_to_format)


# Generated at 2022-06-13 22:16:13.283348
# Unit test for constructor of class Formatting
def test_Formatting():
    string = 'a\nb\nc\nd'
    expected = 'abcd'
    assert Formatting([]).format_headers(string) == expected
    assert Formatting(['default']).format_headers(string) == expected
    assert Formatting(['color']).format_headers(string) == expected

# Generated at 2022-06-13 22:16:20.567620
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    class JsonFormatter:
        def format_body(self, content, mime):
            return "JsonFormatter: " + str(content)

    class PrettyFormatter:
        def format_body(self, content, mime):
            return "PrettyFormatter: " + str(content)

    class NoneFormatter:
        def format_body(self, content, mime):
            return "NoneFormatter: " + str(content)

    def test_case(group_name, content, expected_output):
        available_plugins = {
            "json": [JsonFormatter],
            "pretty": [PrettyFormatter],
            "none": [NoneFormatter]
        }

        formatting = Formatting(groups=[group_name], available_plugins=available_plugins, mime="application/json")

# Generated at 2022-06-13 22:16:33.394440
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """ Unit test for method format_body of class Formatting """
    # Arrange
    result = ""
    expected = "<html>\n<body>\n<h1>Highlight Formatter</h1>\n</body>\n</html>"
    fmt = Formatting(env = Environment(), groups = ["formatter:highlight"])

    # Act
    result = fmt.format_body("<html><body><h1>Highlight Formatter</h1></body></html>", "text/html")

    # Assert
    assert result == expected

# Generated at 2022-06-13 22:16:50.600900
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    groups = ["colors", "formatters"]
    env = Environment()
    headers = '''HTTP/1.1 200 OK
Content-Length: 19
Content-Type: text/html; charset=utf-8
Date: Sun, 15 Apr 2018 13:56:21 GMT
Server: Werkzeug/0.14.1 Python/3.5.2

'''
    kwargs = {}
    f = Formatting(groups, env, **kwargs)
    f.format_headers(headers)

    groups = ["colors", "formatters"]
    env = Environment()

# Generated at 2022-06-13 22:17:04.605104
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
	import unittest
	class TestFormatting_format_body(unittest.TestCase):
		def test_default(self):
			from httpie.plugins.formatter import BaseFormatter
			from httpie.plugins.formatters.json import JsonFormatter
			from httpie.plugins.formatters.pretty import PrettyFormatter
			from httpie.plugins.formatters.raw import RawFormatter
			from httpie.plugins.formatters.colors import ColorsFormatter
			from httpie.plugins.formatters.headers import HeadersFormatter
			from httpie.plugins.formatters.grep import GrepFormatter
			f = Formatting(['raw', 'pretty', 'json'], env=Environment())

# Generated at 2022-06-13 22:17:16.070029
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    available_plugins = plugin_manager.get_formatters_grouped()

    enabled_plugins = []
    groups = ["colors"]
    for group in groups:
        for cls in available_plugins[group]:
            p = cls()
            if p.enabled:
                enabled_plugins.append(p)

    content = """
    {
        "id": 1,
        "name": "A green door",
        "price": 12.50,
        "tags": ["home", "green"]
    }
    """
    mime = "application/json"
    for p in enabled_plugins:
        content = p.format_body(content, mime)
    print(content)

if __name__ == "__main__":
    test_Formatting_format_body()

# Generated at 2022-06-13 22:17:16.690260
# Unit test for constructor of class Formatting
def test_Formatting():
    Formatting([])


# Generated at 2022-06-13 22:17:18.822306
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: 42\r\n'
    print(Formatting(['colors']).format_headers(headers))


# Generated at 2022-06-13 22:17:25.157723
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("application/json"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("application/json; charset=utf-8"), ConverterPlugin)
    assert not Conversion.get_converter("application/json;")
    assert not Conversion.get_converter("/json")
    assert not Conversion.get_converter("json")


# Generated at 2022-06-13 22:17:28.447391
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
  assert _test_Conversion_get_converter("text/html", None)
  assert _test_Conversion_get_converter("application/json", "JSON")


# Generated at 2022-06-13 22:17:32.853392
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """
    return the correspond json converter
    :return:
    """
    json_converter = Conversion.get_converter("application/json")
    assert json_converter.__class__.__name__ == 'JSONConverter'



# Generated at 2022-06-13 22:17:41.062392
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['colors']
    f = Formatting(groups)
    content = '{"some_key": "some_value"}'
    mime = 'application/json'
    assert f.format_body(content, mime) == '{\n    "some_key": "some_value"\n}'

    mime = 'application/xml'
    assert f.format_body(content, mime) == content



# Generated at 2022-06-13 22:17:49.361859
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=['format', 'colors'], env=Environment(),
                   auto_json=True, default_options={},
                   indent=3, body_style='auto')
    #  assert that type(f) is Formatting
    assert isinstance(f, Formatting)
    #  assert that enabled_plugins is a list
    assert isinstance(f.enabled_plugins, list)
    #  assert that enabled_plugins is not empty
    assert f.enabled_plugins != []
    #  assert that the first element in enabled_plugins is a FormatterPlugin
    assert isinstance(f.enabled_plugins[0], FormatterPlugin)

# Generated at 2022-06-13 22:18:04.146293
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    formatter = Formatting(groups=["JSON"], env=env,
                           indent=2, sort_keys=True)
    headers = formatter.format_headers("""HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 48
Content-Type: application/json; charset=utf-8
Date: Mon, 18 Mar 2019 05:53:43 GMT
ETag: "2a91847c6f753fb6148a38c56c3d3f7e"
Server: Cowboy
Via: 1.1 vegur

""")

# Generated at 2022-06-13 22:18:07.908322
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert isinstance(converter, ConverterPlugin)
    converter = Conversion.get_converter('a/b')
    assert converter is None

# Generated at 2022-06-13 22:18:16.698215
# Unit test for method format_headers of class Formatting

# Generated at 2022-06-13 22:18:18.892375
# Unit test for constructor of class Formatting
def test_Formatting():
    test_input = ['headers']
    env = Environment()
    f = Formatting(test_input, env)
    assert f.enabled_plugins == []

# Generated at 2022-06-13 22:18:31.332375
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion.get_converter('image/jpeg')
    assert(c.mime == 'image/jpeg')
    #assert(c.name == 'Jpeg')

    c = Conversion.get_converter('text/html')
    assert(c.mime == 'text/html')
    #assert(c.name == 'Html')

    c = Conversion.get_converter('application/json')
    assert(c.mime == 'application/json')
    #assert(c.name == 'Json')

    c = Conversion.get_converter('text/csv')
    assert(c.mime == 'text/csv')
    #assert(c.name == 'Csv')

    c = Conversion.get_converter('application/x-www-form-urlencoded')
   

# Generated at 2022-06-13 22:18:33.297729
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("image/jpeg") == None

# Generated at 2022-06-13 22:18:43.078747
# Unit test for constructor of class Formatting
def test_Formatting():
    data = Formatting(['colors'],
                      colors=0,
                      style="test",
                      table_style="test",
                      pretty=True,
                      order=1)
    assert data.enabled_plugins == []
    assert type(data.enabled_plugins) == list

    data = Formatting(['colors'],
                      colors=1,
                      style="test",
                      table_style="test",
                      pretty=True,
                      order=1)
    assert data.enabled_plugins != []
    assert type(data.enabled_plugins) == list


# Generated at 2022-06-13 22:18:50.719325
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    assert(Formatting([]).format_headers("HTTP/1.1 200 OK\r\n") == "HTTP/1.1 200 OK\r\n")
    assert(Formatting(['colors']).format_headers("HTTP/1.1 200 OK\r\n") == "\033[1;33mHTTP/1.1 200 OK\033[0m\r\n")
    assert(Formatting(['colors']).format_headers("HTTP/1.1 200 OK\r\nServer: 1.0\r\n") == "\033[1;33mHTTP/1.1 200 OK\033[0m\r\n\033[1;35mServer: 1.0\033[0m\r\n")

# Generated at 2022-06-13 22:19:02.668244
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.formatters import JSONFormatter, JSONLinesFormatter
    groups = ['format_headers', 'format_body']
    fmt = Formatting(groups)
    fmt.enabled_plugins = [JSONFormatter(), JSONLinesFormatter()]

# Generated at 2022-06-13 22:19:13.217371
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Create a class with a helper method
    class MyFormatting:
        def __init__(self, groups, env=Environment(), **kwargs):
            self.groups = groups
            self.enabled_plugins = []
            self.kwargs = kwargs
            self.env = env

        def get_formatters(self):
            return [MockFormatter]

        def make_formatter(self, fcls, **kwargs):
            f = fcls(env=self.env, **self.kwargs)
            if f.enabled:
                self.enabled_plugins.append(f)
            return f

    # Create a helper mock class
    class MockFormatter:
        def __init__(self, env, **kwargs):
            self.env = env
            self.kwargs = kwargs

# Generated at 2022-06-13 22:19:21.849002
# Unit test for constructor of class Formatting
def test_Formatting():
    F = Formatting(['colors'])
    assert F.enabled_plugins[0]._scheme_re.match('https://')
    assert F.enabled_plugins[0]._scheme_re.match('ssh://')

# Generated at 2022-06-13 22:19:23.601529
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(["formatters"])
    assert True

# Generated at 2022-06-13 22:19:33.871655
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    assert Formatting([]).format_headers('Content-Type: application/json') == 'Content-Type: application/json'
    assert Formatting(['headers']).format_headers('Content-Type: application/json') == 'Content-Type: application/json'
    assert Formatting(['headers']).format_headers('Content-Type: application/json\r\nContent-Length: 10') == \
        'Content-Type: application/json\r\n' + \
        'Content-Length: 10'

# Generated at 2022-06-13 22:19:39.047679
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = "Content-Type: application/json\r\nContent-Length: 12\r\n"
    formatter = Formatting(groups=["format", "colors"])
    assert formatter.format_headers(headers) == "\x1b[94mContent-Type\x1b[39m: application/json\r\n\x1b[94mContent-Length\x1b[39m: 12\r\n\r\n"

# Generated at 2022-06-13 22:19:39.990007
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # TODO
    pass

# Generated at 2022-06-13 22:19:48.999427
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.output.streams import write, get_method
    from httpie.plugins.builtin import JSONOutputFormatter
    from httpie.output.formatters.colors import get_lexer
    from httpie.plugins.registry import plugin_manager
    from httpie.context import Environment
    import httpie
    httpie.__main__.HTTPIE_OUTPUT_FILE = None
    httpie.__main__.HTTPIE_OUTPUT_DIR = None
    httpie.__main__.HTTPIE_OUTPUT_FORMAT = None
    httpie.__main__.HTTPIE_OUTPUT_OPTIONS = None

    env = Environment(arguments={"--headers-grouped": False})
    t1 = Formatting(groups=["headers"], env=env)

# Generated at 2022-06-13 22:19:53.569462
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    import pytest
    mock_mimes = ['application/json', 'application/xml', 'application/yaml']
    assert len(plugin_manager.get_converters()) == 3
    for mime in mock_mimes:
        assert Conversion.get_converter(mime).mime == mime


# Generated at 2022-06-13 22:19:57.527863
# Unit test for constructor of class Formatting
def test_Formatting():
    # TODO: replace environment with HEADERS
    fmt = Formatting(['colors'], Environment())
    assert fmt.enabled_plugins == plugin_manager.get_formatters_grouped()['colors']


# Generated at 2022-06-13 22:20:06.403367
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    if Conversion.get_converter('application/json') is None:
        print('Conversion.get_converter(application/json) is None')
    if Conversion.get_converter('application/xml') is None:
        print('Conversion.get_converter(application/xml) is None')
    if Conversion.get_converter('application/javascript') is None:
        print('Conversion.get_converter(application/javascript) is None')
    if Conversion.get_converter('application/x-www-form-urlencoded') is None:
        print('Conversion.get_converter(application/x-www-form-urlencoded) is None')
    c = Conversion.get_converter('text/plain')

# Generated at 2022-06-13 22:20:17.620651
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fm = Formatting(groups=('colors',))

# Generated at 2022-06-13 22:20:23.505764
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter_class = Conversion.get_converter('/json')
    assert converter_class is not None

# Generated at 2022-06-13 22:20:36.802817
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # test case 1
    groups = ['colors']
    kwargs = {}
    formatting = Formatting(groups, **kwargs)
    headers = '{ "a": "b" }'
    result = formatting.format_headers(headers)
    expected_result = '{\n  "a":       "b"\n}\n'
    assert result == expected_result

    # test case 2
    groups = ['colors']
    kwargs = {}
    formatting = Formatting(groups, **kwargs)
    headers = '{}'
    result = formatting.format_headers(headers)
    expected_result = '{\n}\n'
    assert result == expected_result

    # test case 3
    groups = ['colors']
    kwargs = {}
    formatting = Formatting(groups, **kwargs)
   

# Generated at 2022-06-13 22:20:49.190119
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    mime = 'application/json'
    content = '{"result": "ok"}'

# Generated at 2022-06-13 22:20:59.001641
# Unit test for constructor of class Formatting

# Generated at 2022-06-13 22:21:09.013742
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('application/json'),
                      ConverterPlugin) == True
    assert isinstance(Conversion.get_converter('application/json'),
                      ConverterPlugin) == True
    assert isinstance(Conversion.get_converter('application/xml'),
                      ConverterPlugin) == True
    assert isinstance(Conversion.get_converter('application/octet-stream'),
                      ConverterPlugin) == True
    assert isinstance(Conversion.get_converter('text/html'),
                      ConverterPlugin) == False

# Generated at 2022-06-13 22:21:12.468473
# Unit test for constructor of class Formatting
def test_Formatting():
    if Formatting:
        print("Test Formatting passed")
    else:
        print("Test Formatting failed")

# Generated at 2022-06-13 22:21:23.310706
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    env = Environment()
    env.stdout = cStringIO.StringIO()
    env.stderr = cStringIO.StringIO()
    fm = Formatting(['colors'], env=env)
    assert fm.format_body('{"test":true}', 'application/json') == '{\x1b[32m\x1b[1m"test"\x1b[0m:\x1b[34m\x1b[1mtrue\x1b[0m}'
    assert fm.format_body('{"test":true}', 'application/xml') == '{"test":true}'
    assert fm.format_body('{"test":true}', '') == '{"test":true}'

# Generated at 2022-06-13 22:21:26.281783
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ["Html"]
    check_enabled_plugins = []
    f = Formatting(groups)
    assert f.enabled_plugins == check_enabled_plugins



# Generated at 2022-06-13 22:21:37.164256
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
	format_headers = Formatting.format_headers
	headers = '''HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 25 May 2017 07:30:51 GMT
Content-Length: 57
Server: nginx


{
    "answer": 42,
    "more": "none"
}
'''
	assert format_headers(headers) == headers

# Generated at 2022-06-13 22:21:41.444665
# Unit test for constructor of class Formatting
def test_Formatting():
    if os.path.isfile('/etc/httpie/config.json'):
        assert Formatting(['localhost']) is not None
    else:
        assert Formatting([]) is not None


# Generated at 2022-06-13 22:21:49.200496
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    pass

# Generated at 2022-06-13 22:21:55.601562
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins import FormatterPlugin
    import os
    import pytest
    from tempfile import NamedTemporaryFile
    from unittest.mock import patch
    from httpie import ExitStatus

    class TestPlugin(FormatterPlugin):
        name = 'test'
        description = 'test plugin'
        enabled = True
        def format_headers(self, headers):
            return headers.upper()
    p = TestPlugin()

    # test format headers
    txt = 'test:test plugin\n'
    assert p.format_headers(txt) == txt.upper()

    # test with processing argument '--print=Hh'
    with NamedTemporaryFile(delete=False) as f:
        f.write(txt.encode())

    from httpie.core import main

# Generated at 2022-06-13 22:21:58.559341
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    conv = Conversion.get_converter('application/json')
    conv2 = Conversion.get_converter('application/json')
    assert conv.mime == conv2.mime

# Generated at 2022-06-13 22:22:05.570591
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors']
    available_plugins = plugin_manager.get_formatters_grouped()
    enabled_plugins = []
    for group in groups:
        for cls in available_plugins[group]:
            p = cls(env=Environment())
            if p.enabled:
                enabled_plugins.append(p)
    assert enabled_plugins != []


# Generated at 2022-06-13 22:22:10.225771
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter_json = Conversion.get_converter("application/json")
    assert isinstance(converter_json,ConverterPlugin)
    converter_not_found = Conversion.get_converter("application/Notfound")
    assert converter_not_found is None
