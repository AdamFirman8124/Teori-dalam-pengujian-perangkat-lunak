

# Generated at 2022-06-13 22:12:20.355014
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():

    # Arrange
    expected = {
        "group1": "Method:\t\tGET",
        "group2": "Method:\t\tGET\nURL:\t\thttp://www.dummy.com",
        "group3": "Method:\t\tGET\nURL:\t\thttp://www.dummy.com\nProtocol:\tHTTP/0.9",
        "group4": "Method:\t\tGET\nURL:\t\thttp://www.dummy.com\nProtocol:\tHTTP/0.9\nHeaders:\tHost: www.dummy.com"
    }

    # Act
    group1 = Formatting(["group1"])
    group2 = Formatting(["group2"])
    group3 = Formatting(["group3"])
    group4 = Formatting

# Generated at 2022-06-13 22:12:25.688095
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime="application/json"
    # test for supported mime
    assert Conversion.get_converter(mime) != None
    # test for unsupported mime
    mime = "text/plain"
    assert Conversion.get_converter(mime) == None    


# Generated at 2022-06-13 22:12:34.928203
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # env is an object of class Environment
    env = Environment()
    # groups is a list of string.
    groups = ['colors']
    # invokes class Formatting to get object format
    format = Formatting(groups, env)
    # headers is a string.
    headers = 'Content-Type: text/plain\nServer: ngx_openresty\n'
    # invokes method format_headers of object format

# Generated at 2022-06-13 22:12:47.631735
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    class TestF(ConverterPlugin):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.enabled = True
            self.env = kwargs['env']
            self.use_colors = not self.env.colors
        def format_headers(self, headers: str) -> str:
            return headers + "testF"
    class TestG(ConverterPlugin):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.enabled = True
            self.env = kwargs['env']
            self.use_colors = not self.env.colors
        def format_headers(self, headers: str) -> str:
            return headers + "testG"
    plugin_manager.get_

# Generated at 2022-06-13 22:12:50.974484
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # This test will give a KeyError if it doesn't work.
    assert Formatting(['format']).format_headers('Content-Type: text/html\n') == 'Content-Type: text/html\n'

# Generated at 2022-06-13 22:12:59.791108
# Unit test for constructor of class Formatting
def test_Formatting():
    class EnvironmentTest(Environment):
        def __init__(self):
            super().__init__()
            self.colors = False
            self.styles = False
            self.stream = False
            self.default_options = None

    formatter = Formatting(['SyntaxHighlight', 'Pretty'], EnvironmentTest())
    print(formatter.format_headers('HTTP/1.1 200 OK\r\n'))
    print(formatter.format_body(open('response.json').read(), 'application/json'))



# Generated at 2022-06-13 22:13:04.851974
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    print("available_plugins: ", available_plugins)
    for group in available_plugins:
        print("group: ", group)
        for cls in available_plugins[group]:
            print("cls: ", cls)


# Generated at 2022-06-13 22:13:11.420662
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.output.formatters.colors import HumanizeColorsFormatter
    f = Formatting(['colors'], style = 'linux')
    h = HumanizeColorsFormatter(style = 'linux')
    assert f.format_headers('key: value') == h.format_headers('key: value')


# Generated at 2022-06-13 22:13:18.275856
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    my_formatting = Formatting(groups=['colored'], colors=256, style='client')

# Generated at 2022-06-13 22:13:22.334041
# Unit test for constructor of class Formatting
def test_Formatting():
    print("test case for constructor of class Formatting")
    #constructor of class Formatting
    fm = Formatting(['colors'])
    assert fm
    print("test case passed")


# Generated at 2022-06-13 22:13:31.681466
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    input_content = '[{"op": "test", "path": "/name", "value": "foo"}, ' \
                    '{"op": "remove", "path": "/name"}]'
    input_mime = 'application/json-patch+json'

    output = Formatting(groups=['json']).format_body(input_content, input_mime)
    print(output)

test_Formatting_format_body()

# Generated at 2022-06-13 22:13:41.094870
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nConnection: keep-alive\r\nServer: nginx/1.10.3 (Ubuntu)\r\nX-Powered-By: Express'
    headers_expected = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\nConnection: keep-alive\nServer: nginx/1.10.3 (Ubuntu)\nX-Powered-By: Express'
    env = Environment()
    groups = ["indent"]
    kwargs = {"indent": "2"}
    formatting = Formatting(groups, env, **kwargs)
    headers_result = formatting.format_headers(headers)
    assert headers_expected == headers_result

# Generated at 2022-06-13 22:13:51.678253
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    expect_mime_type = "application/json"
    expect_mime_type_invalid = "txt+json"
    expect_converter_class = "JsonConverter"

    mime_converter = Conversion.get_converter(expect_mime_type)
    assert mime_converter.MIME == expect_mime_type
    assert mime_converter.__class__.__name__ == expect_converter_class

    mime_converter = Conversion.get_converter(expect_mime_type_invalid)
    assert mime_converter == None


# Generated at 2022-06-13 22:13:55.872949
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert str(converter) == '<httpie.converter.JSONConverter object at 0x7f2c80797ac8>'

# Generated at 2022-06-13 22:14:05.785072
# Unit test for constructor of class Formatting
def test_Formatting():
    args_for_Formatting = [["basic", "colors"], Environment(),
                           False, False, False]
    f = Formatting(*args_for_Formatting)
    assert f.enabled_plugins[0].__class__.__name__ == "BasicFormatter"
    assert f.enabled_plugins[1].__class__.__name__ == "ColorsFormatter"
    assert f.enabled_plugins[0]._supports_headers
    assert not f.enabled_plugins[0]._supports_body
    assert not f.enabled_plugins[0]._supports_body_colors



# Generated at 2022-06-13 22:14:14.217248
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['colors']
    kwargs = {}
    env = Environment()
    content = 'Body to be formatted'
    mime = 'application/json'
    fmt = Formatting(groups, env, **kwargs)
    result = fmt.format_body(content, mime)
    expected = 'yamllint disable rule\n{\n    "Body": "to be formatted"\n}\n'
    assert result == expected

# Generated at 2022-06-13 22:14:18.784434
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
   assert Conversion.get_converter('application/json') == '<httpie.plugins.converter.JSONConverterPlugin object at 0x7fec0d0f9080>'



# Generated at 2022-06-13 22:14:21.945613
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert (isinstance(Conversion.get_converter("application/json"), ConverterPlugin))
    assert (Conversion.get_converter("text/html") == None)



# Generated at 2022-06-13 22:14:27.650478
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    format = Formatting(groups=['colors'])
    format.format_body(content="test,test,test", mime='plain/text')


# Generated at 2022-06-13 22:14:36.807381
# Unit test for method format_headers of class Formatting

# Generated at 2022-06-13 22:14:51.776227
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fmt = Formatting(groups=['colors', 'format'])
    # Test if format_headers of class Formatting can format headers normally

# Generated at 2022-06-13 22:15:04.755529
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    print('---- Unit test for method format_body of class Formatting starts ----')
    try:
        f = Formatting(groups=["format"], colors=False, indent=2, prefix="")
        content = '{"result":[{"id":"11","name":"DD"},{"id":"22","name":"CC"},{"id":"33","name":"BB"},{"id":"44","name":"AA"}]}'
        result = f.format_body(content, "application/json")
        print("result: {}".format(result))
    except Exception as ex:
        print("An exception happened when calling the function format_body of class Formatting: {}".format(str(ex)))
    print('---- Unit test for method format_body of class Formatting ends ----')


# Generated at 2022-06-13 22:15:14.026918
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    def test_1():
        mime = "application/json"
        c = Conversion.get_converter(mime)
        assert c.supports(mime)

    def test_2():
        mime = "application/x-www-form-urlencoded"
        c = Conversion.get_converter(mime)
        assert c.supports(mime)

    def test_3():
        mime = "image/jpeg"
        c = Conversion.get_converter(mime)
        assert c.supports(mime)

    def test_4():
        mime = "text/html"
        c = Conversion.get_converter(mime)
        assert not c.supports(mime)


# Generated at 2022-06-13 22:15:26.327543
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    class MockConverterPlugin(ConverterPlugin):
        def __init__(self, mime):
            self.mime = mime

        @classmethod
        def supports(cls, mime: str) -> bool:
            return mime == "application/json"

        def convert(self, content: str) -> str:
            return "This is the content [{}]".format(self.mime)

    supported_mime = "application/json"
    unsupported_mime = "image/png"
    plugin_manager.register_converter(MockConverterPlugin)

# Generated at 2022-06-13 22:15:28.140956
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("text/html") is not None

# Generated at 2022-06-13 22:15:31.492792
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    print(Conversion.get_converter('application/json'))
    print(Conversion.get_converter('xml'))

# Generated at 2022-06-13 22:15:41.820813
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not is_valid_mime('')
    assert is_valid_mime('text/plain')
    assert is_valid_mime('application/json')
    assert not is_valid_mime('application/json;charset=utf-8')
    assert not is_valid_mime('text')
    assert not is_valid_mime('/json')
    assert not is_valid_mime('text/')

    converter = Conversion.get_converter('text/plain')
    assert converter is None

    converter = Conversion.get_converter('application/json')
    assert converter is not None



# Generated at 2022-06-13 22:15:52.519722
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion.get_converter('application/json')
    assert c
    assert c.mime == 'application/json'
    assert c.supports('application/json')
    assert not c.supports('text/html')
    c = Conversion.get_converter('application/jso')
    assert not c
    c = Conversion.get_converter('')
    assert not c
    c = Conversion.get_converter('/')
    assert not c
    c = Conversion.get_converter('json')
    assert not c
    c = Conversion.get_converter(None)
    assert not c

# Generated at 2022-06-13 22:15:55.840585
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/xml'
    if is_valid_mime(mime):
        converter = Conversion.get_converter(mime)
        assert converter.mime == mime

# Generated at 2022-06-13 22:16:04.387676
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Case 1
    assert Formatting(['']).format_headers('header:value') == 'header: value'

    # Case 2
    assert Formatting(['colors']).format_headers('header:value') == \
           'header: \x1b[38;5;39mvalue\x1b[0m'

    # Case 3
    assert Formatting(['colors']).format_headers('header:\x1b[38;5;39mvalue\x1b[0m') == \
           'header: \x1b[38;5;39mvalue\x1b[0m'

# Generated at 2022-06-13 22:16:16.720934
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime_json = "application/json"
    mime_xml = "application/xml"
    yaml_exists = False
    #  Expected outputs
    out1 = "<class 'httpie.plugins.convert.converters.JSONConverter'>"
    out2 = "<class 'httpie.plugins.convert.converters.XMLConverter'>"
    out3 = "<class 'httpie.plugins.convert.converters.YAMLConverter'>"
    out4 = "None"

    #  Test outputs
    #  test1 and test2 should be equal since JSON Converter supports JSON and XML Converter supports XML
    test1 = str(Conversion.get_converter(mime_json)).replace(" ", "")

# Generated at 2022-06-13 22:16:36.795622
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # The method convert a string to json
    def test_get_converter_json():
        mime = 'application/json'
        converter = Conversion.get_converter(mime)
        assert hasattr(converter, 'to_json')

    # The method convert a string to xml
    def test_get_converter_xml():
        mime = 'application/xml'
        converter = Conversion.get_converter(mime)
        assert hasattr(converter, 'to_xml')

    # The method convert a string to csv
    def test_get_converter_csv():
        mime = 'text/csv'
        converter = Conversion.get_converter(mime)
        assert hasattr(converter, 'to_csv')

    # The method convert a string to t

# Generated at 2022-06-13 22:16:43.111220
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    # plugins = plugin_manager.get_formatters_grouped()
    # plugins2 = plugin_manager.get_all_enabled_formatters_grouped()
    groups = ['colors', 'formatters']
    env = Environment(colors=256)
    kwargs = {}
    f = Formatting(groups, env, **kwargs)
    assert f is not None

    # output_format="pretty"
    kwargs = {'output_format': 'pretty'}
    f = Formatting(groups, env, **kwargs)
    assert f is not None

    # output_format="json"
    kwargs = {'output_format': 'json'}
    f = Formatting(groups, env, **kwargs)
    assert f

# Generated at 2022-06-13 22:16:52.537788
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import warnings
    warnings.filterwarnings('ignore')

    assert Formatting([]).format_headers("Content-type: text/html") == "Content-type: text/html"
    assert Formatting([]).format_headers("Content-type: text/html\n") == "Content-type: text/html"
    assert Formatting(['colors']).format_headers("Content-type: text/html\n") == "\x1b[36mContent-type:\x1b[0m text/html"
    return True

# Generated at 2022-06-13 22:17:06.873205
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    print("\n======Test for method get_converter of class Conversion======")
    # Call get_converter() with parameter of mime HEX
    print("\n**********Test case 1**********")
    print("Parameter: mime = HEX")
    print("Expected: HexConverter('application/octet-stream')")
    converter = Conversion.get_converter('HEX')
    print("Actual  :", converter)
    if not isinstance(converter, HexConverter):
        print("Test failed: expected and actual values are different objects")
    elif converter.mime != 'application/octet-stream':
        print("Test failed: wrong mime value")
    else:
        print("Test passed")

    # Call get_converter() with parameter of mime JSON

# Generated at 2022-06-13 22:17:07.626862
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    pass

# Generated at 2022-06-13 22:17:12.412408
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    header = "hi: 123\nhello: 321\n"
    groups = ["colors", "format", "prettify"]
    test_Formatting = Formatting(groups)
    assert test_Formatting.format_headers(header) == "hi:     123\nhello: 321\n"


# Generated at 2022-06-13 22:17:15.838930
# Unit test for constructor of class Formatting
def test_Formatting():
    try:
        assert Formatting([]) == Formatting([])
    except AssertionError:
        print('two empty Formatting objects should be equal')

if __name__ == '__main__':
    test_Formatting()

# Generated at 2022-06-13 22:17:16.719873
# Unit test for constructor of class Formatting
def test_Formatting():
    Formatting(groups = ["syntax"], env = Environment())


# Generated at 2022-06-13 22:17:21.843015
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion().get_converter('text/xml') is not None
    assert Conversion().get_converter('text/html') is not None
    assert Conversion().get_converter('application/json') is None
    assert Conversion().get_converter('no valid') is None
    assert Conversion().get_converter('text/xml ') is None

# Generated at 2022-06-13 22:17:33.320231
# Unit test for method get_converter of class Conversion

# Generated at 2022-06-13 22:17:46.968169
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    actual_list = []
    expected_list = []
    class TestFormatter(object):
        def format_headers(self, headers):
            headers_list = headers.split('\n')
            for i in headers_list:
                actual_list.append(i)

    groups = ['test']
    test_output = Formatting(groups)
    test_output.enabled_plugins.append(TestFormatter())

    expected_list.append('HTTP/1.1 200 OK')
    expected_list.append('Transfer-Encoding: chunked')
    expected_list.append('Server: GitHub.com')
    expected_list.append('Status: 200 OK')
    expected_list.append('X-RateLimit-Remaining: 4999')
    expected_list.append('X-RateLimit-Limit: 5000')
    expected_list

# Generated at 2022-06-13 22:18:00.066118
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    class Pref:
        def __init__(self, pref):
            self.pref = pref
    
    @plugin_manager.register_converter('text/plain')
    class ConverterPluginMock(ConverterPlugin):
        def loads(self, args):
            return Pref('result')
        def dump(self, args):
            return Pref('result')
        def supports(self, mime):
            return True

    assert isinstance(Conversion.get_converter('text/plain').loads(None), Pref)
    assert isinstance(Conversion.get_converter('text/plain').dump(None), Pref)
    assert Conversion.get_converter('text/plain').dumps(None) is None
    assert Conversion.get_converter('text/plain').load(None) is None

# Generated at 2022-06-13 22:18:02.408896
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # pylint: disable=protected-access

    converter = Conversion.get_converter('application/json')
    assert isinstance(converter, ConverterPlugin)
    assert converter._mime == 'application/json'

    converter = Conversion.get_converter('application/xml')
    assert converter is None

# Generated at 2022-06-13 22:18:07.137701
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'text/html'
    assert is_valid_mime(mime)
    converter = Conversion.get_converter(mime)
    assert converter == 'text/html'


# Generated at 2022-06-13 22:18:15.159467
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(groups=['colors'])
    print(f.format_body("""{"name":"value", "a": "b"}""", mime="application/json"))
    print(f.format_body("""{"name":"value", "a": "b"}""", mime="foo/bar"))
    f = Formatting(groups=['colors'])
    print(f.format_body("""<html><h1>hello</h1></html>""", mime="text/html"))
    print(f.format_body("""<html><h1>hello</h1></html>""", mime="foo/bar"))

# Generated at 2022-06-13 22:18:19.247720
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    h = Formatting(groups=['colors-headers'])
    assert h.format_headers('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n') == (
          '\x1b[90mHTTP/1.1 200 OK\x1b[0m\r\n'
          '\x1b[94mContent-Type\x1b[0m: \x1b[36mapplication/json\x1b[0m\r\n'
          '\r\n')



# Generated at 2022-06-13 22:18:31.380166
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    json = '[{"age": 5, "name": "John"}, {"age": 7, "name": "May"}]'
    assert Formatting(["json"]).format_body(json, 'application/json') == '\n[\n    {\n        "age": 5,\n        "name": "John"\n    },\n    {\n        "age": 7,\n        "name": "May"\n    }\n]'
    xml = '<persons><person><age>5</age><name>John</name></person><person><age>7</age><name>May</name></person></persons>'

# Generated at 2022-06-13 22:18:36.080564
# Unit test for constructor of class Formatting
def test_Formatting():
    # Environment(colors=256, stream=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
    env = Environment()
    # Debug, Formatted
    groups = ['Debug', 'Formatted']
    f = Formatting(groups, env)
    assert f is not None


# Generated at 2022-06-13 22:18:47.865035
# Unit test for constructor of class Formatting
def test_Formatting():
    # check a normal case
    expected_groups = ['colors', 'colors']
    expected_kwargs = {'stdin': 'Testing'}
    expected_env = Environment()

    f = Formatting(groups=expected_groups, env=expected_env, **expected_kwargs)
    assert f.enabled_plugins == []
    assert f.groups == expected_groups
    assert f.kwargs == expected_kwargs
    assert f.env == expected_env

    # check corner cases

    # check with empty groups
    f = Formatting(groups=None)
    assert f.enabled_plugins == []
    assert f.groups == []

    # check with default kwargs
    f = Formatting(**expected_kwargs)
    assert f.kwargs == expected_kwargs

    # check with default env
    f = Format

# Generated at 2022-06-13 22:18:54.763712
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert converter is not None
    converter = Conversion.get_converter('application/xml')
    assert converter is not None

# Generated at 2022-06-13 22:19:04.796561
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_env = Environment()
    test_env.colors = True
    test_fmt = Formatting(['colors'], env=test_env)

# Generated at 2022-06-13 22:19:06.966954
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert converter is not None

# Generated at 2022-06-13 22:19:14.880431
# Unit test for constructor of class Formatting
def test_Formatting():

    groups = ['uglyjson', 'colors', 'format', 'colors']
    env = Environment()
    headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n"
    content = "{\"name\":\"test\", \"description\":\"test\"}"

    f = Formatting(groups, env)
    f.format_headers(headers)
    f.format_body(content, 'application/json')


# Generated at 2022-06-13 22:19:16.840093
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter(mime="application/json"), ConverterPlugin)



# Generated at 2022-06-13 22:19:23.782850
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/hcl")
    assert converter is not None
    assert str(converter) == "<ConverterPlugin application/hcl>"
    # The following cases should return None
    converter = Conversion.get_converter("application/invalid")
    assert converter is None
    converter = Conversion.get_converter("")
    assert converter is None

# Generated at 2022-06-13 22:19:30.350826
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    formatting_instance = Formatting(groups=['colors'], no_stream=True)
    assert formatting_instance.format_body('test_body', 'text/plain') == 'test_body'
    assert formatting_instance.format_body('test_body', 'application/json') == 'test_body'


# Generated at 2022-06-13 22:19:37.875935
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.cli.grouped import DEFAULT_FORMAT, DEFAULT_GROUP
    from httpie.context import Environment
    f = Formatting(DEFAULT_FORMAT, Environment(), stdout_isatty=True,
                   stderr_isatty=True)
    available_plugins = plugin_manager.get_formatters_grouped()
    assert len(available_plugins[DEFAULT_GROUP]) == len(f.enabled_plugins)
    f.format_headers("headers")
    f.format_body("content", "mime")



# Generated at 2022-06-13 22:19:45.368078
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    format_groups = ["colors", "format", "format-keys", "highlight", "pretty"]
    plugin_manager.load_plugins()
    formatting = Formatting(format_groups, debug=True, k=2, print_body=True, indented_json=False, line_max_width=80)
    mime = "application/json"
    assert formatting.format_body('{"key": "value"}', mime) == '{\n  "key": "value"\n}\n'

# Generated at 2022-06-13 22:19:55.475776
# Unit test for method format_body of class Formatting

# Generated at 2022-06-13 22:20:03.148370
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    expected_mime_type = "application/json"
    assert is_valid_mime(expected_mime_type)
    converter = Conversion.get_converter(expected_mime_type)
    assert converter.mime == expected_mime_type



# Generated at 2022-06-13 22:20:05.717442
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    #arrange
    mime = "image/png"
    #act
    conv = Conversion.get_converter(mime)
    #assert
    assert conv.supports(mime) == True


# Generated at 2022-06-13 22:20:12.127943
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    result1 = Conversion.get_converter('application/json')
    result2 = Conversion.get_converter('text/html')
    result3 = Conversion.get_converter('')
    assert result1.__class__.__name__ == 'JSONConverter'
    assert result2.__class__.__name__ == 'HTMLConverter'
    assert result3 is None


# Generated at 2022-06-13 22:20:16.970269
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.context import Environment
    # testing empty groups
    formatter = Formatting(env=Environment(), groups=[])
    assert formatter.enabled_plugins == []

    # testing non-empty groups
    formatter = Formatting(env=Environment(), groups=['input'])

# Generated at 2022-06-13 22:20:27.395702
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = Formatting(groups=['colors']).format_headers(headers='Content-Type: application/json\nStatus:200\nServer:nginx\nX-Powered-By:PHP/7.0.33')
    assert headers == '\x1b[38;5;244mContent-Type\x1b[0m: application/json\n\x1b[38;5;34mStatus\x1b[0m: 200\n\x1b[38;5;244mServer\x1b[0m: nginx\n\x1b[38;5;244mX-Powered-By\x1b[0m: PHP/7.0.33'


# Generated at 2022-06-13 22:20:39.633022
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_groups = ["colors", "json"]
    test_env = Environment()
    test_formatting = Formatting(test_groups, test_env)
    test_headers = '''HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 4
Content-Type: text/plain; charset=utf-8
Date: Sat, 05 Oct 2019 23:33:32 GMT
Server: Python/3.6 aiohttp/3.5.4'''
    test_headers = test_formatting.format_headers(test_headers)
    print(test_headers)

# Generated at 2022-06-13 22:20:49.466459
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # 1
    testcase = 'application/json; charset=utf8'
    assert is_valid_mime(testcase) is True
    assert Conversion.get_converter(testcase) is None

    # 2
    testcase = 'application/json'
    assert is_valid_mime(testcase) is True
    assert Conversion.get_converter(testcase).mime == 'application/json'

    # 3
    testcase = 'application/xml'
    assert is_valid_mime(testcase) is True
    assert Conversion.get_converter(testcase).mime == 'application/xml'

    # 4
    testcase = 'application/xml; charset=ascii'
    assert is_valid_mime(testcase) is True

# Generated at 2022-06-13 22:20:51.910008
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert (converter != None) and (converter != False)

# Generated at 2022-06-13 22:20:54.624443
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    json_mime = "application/json"
    assert Conversion.get_converter(json_mime).supports(json_mime) == True


# Generated at 2022-06-13 22:21:01.373073
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not Conversion.get_converter('')
    assert not Conversion.get_converter('a')
    assert not Conversion.get_converter('a/')
    assert not Conversion.get_converter('a/b/')
    assert not Conversion.get_converter('a//b')
    assert not Conversion.get_converter('//')
    assert not Conversion.get_converter('/')
    assert not Conversion.get_converter(';')

    assert not Conversion.get_converter('application/unknown')
    assert Conversion.get_converter('application/json')



# Generated at 2022-06-13 22:21:14.271217
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    f = Formatting(['colors'], style='solarized', colors=256)
    assert f.format_headers('Foo: bar\nBaz:'), 'Foo: bar\nBaz:'


# Generated at 2022-06-13 22:21:19.826961
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # test get_converter method with a valid input
    mime = "application/json"
    assert 'Convert JSON to formatted strings' == Conversion.get_converter(mime).__doc__

    # test get_converter method with a invalid input
    mime = "application/json/another"
    assert None == Conversion.get_converter(mime)

# Generated at 2022-06-13 22:21:26.686403
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    import json
    import yaml
    assert Conversion.get_converter('application/json') == json.JSONConverter('application/json')
    assert Conversion.get_converter('application/yaml') == yaml.YAMLConverter('application/yaml')
    assert Conversion.get_converter('') == None

# Generated at 2022-06-13 22:21:35.985405
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    res1 = Conversion.get_converter('application/json')
    res2 = Conversion.get_converter('application/xml')
    res3 = Conversion.get_converter('application/atom+xml')
    res4 = Conversion.get_converter('application/javascript')
    res5 = Conversion.get_converter('application/vnd.github.v3+json')
    assert isinstance(res1, ConverterPlugin)
    assert isinstance(res2, ConverterPlugin)
    assert isinstance(res3, ConverterPlugin)
    assert isinstance(res4, ConverterPlugin)
    assert isinstance(res5, ConverterPlugin)

# Generated at 2022-06-13 22:21:39.366684
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
	assert isinstance(Conversion.get_converter('application/json'),ConverterPlugin)



# Generated at 2022-06-13 22:21:43.819798
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter1 = Conversion.get_converter("image/png")
    converter2 = Conversion.get_converter("image/jpeg")
    converter3 = Conversion.get_converter("svg")
    converter4 = Conversion.g

# Generated at 2022-06-13 22:21:49.747179
# Unit test for constructor of class Formatting
def test_Formatting():
    ff = Formatting(['colors', 'colors-browser'])
    output = ff.format_headers("{'Content-Type': 'application/json'}")
    assert output == "{'Content-Type': 'application/json'}"
    output2 = ff.format_headers("{'Content-Type': 'text/html'}")
    if output2 != "{'Content-Type': 'text/html'}":
        raise Exception("Unexpected output")


# Generated at 2022-06-13 22:21:55.891492
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['colors', 'format']
    env = Environment()
    formatting = Formatting(groups, env)
    content = '{"key": "value"}'
    mime = 'application/json'
    ret = formatting.format_body(content, mime)
    print("Test case 1: ")
    print(ret)
    assert ret == '{\x1b[94m"key"\x1b[39;49;00m: \x1b[33m"value"\x1b[39;49;00m}'

    groups = ['colors', 'format']
    env = Environment()
    formatting = Formatting(groups, env)
    content = '{ "key": "value" }'
    mime = 'text/html'
    ret = formatting.format_body(content, mime)


# Generated at 2022-06-13 22:22:07.498916
# Unit test for constructor of class Formatting
def test_Formatting():
    test_env = Environment()
    test_env.colors = False
    test_env.format = 'prettyjson'
    test_env.output_options = {}
    test_env.stream = sys.stdout
    test_env.verbose = 0
    test_env.default_options = {}
    test_env.config = ConfigDict()
    test_env.config.config_dir = '/home/yifei/.config/httpie'
    test_env.config.config_path = '/home/yifei/.config/httpie/config.json'
    test_env.config.__dict__.update(
        {'__meta': {'HTTPie 1.0': 'JSON File'}, 'colors': {'style': 'monokai'}})
    test_env.config.__meta__ = {}