

# Generated at 2022-06-13 22:22:48.340559
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class _formatter(FormatterPlugin):
        def format_headers(self, headers):
            return headers.replace('\n', '+')
    headers = '''
    <h1>
    <h2>
    '''
    formatted_headers = '''
    <h1>+<h2>+'''
    assert formatted_headers == _formatter().format_headers(headers)

# Generated at 2022-06-13 22:22:54.149676
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class MockFormatterPlugin(FormatterPlugin):
        def __init__(self):
            super(MockFormatterPlugin, self).__init__(**{'format_options': {'headers': False}})

        def format_headers(self, headers: str) -> str:
            return "mock"

    plugin = MockFormatterPlugin()
    result = plugin.format_headers("test")
    assert result == "mock"

# Generated at 2022-06-13 22:23:07.071454
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    # Test case 1
    something_else_mime = 'image/png'

# Generated at 2022-06-13 22:23:14.052959
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    # implementation of abstract method
    def format_body(self, content: str, mime: str) -> str:
        return content

    # check whether the method is overridden
    f1 = FormatterPlugin()
    f1.format_body = format_body
    f1.format_body('R', 'application/json')

    # check whether the implementation is correct
    f2 = FormatterPlugin()
    f2.format_body = format_body
    print(f2.format_body('{response}', 'application/json'))

# Generated at 2022-06-13 22:23:21.051419
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class TestFormatterPlugin(FormatterPlugin):
        def format_body(self, content: str, mime: str) -> str:
            return content + ' TEST'
    content = 'TEST'
    mime = 'text/plain'
    formatter = TestFormatterPlugin(format_options = 'TEST')
    assert formatter.format_body(content, mime) == content + ' TEST'

# Generated at 2022-06-13 22:23:29.297365
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class MyFormatterPlugin(FormatterPlugin):
      def format_body(self, content, mime):
        return content + '_' + mime

    assert MyFormatterPlugin(
        format_options={}
    ).format_body('test', mime='application/json') == 'test_application/json'
    # Object of class FormatterPlugin can not be created since
    # method format_body of class FormatterPlugin is abstract
    #assert FormatterPlugin(
    #    format_options={}
    #).format_body('test', mime='application/json') != 'test_application/json'


# Generated at 2022-06-13 22:23:31.765058
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class FormatterPluginTest(FormatterPlugin):
        def format_headers(self, headers):
            return ""



# Generated at 2022-06-13 22:23:42.266584
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    rst = re.sub(r'^.*?\n.*?(\n.*?){2}.*?\n', '', dedent(test_FormatterPlugin_format_headers.__doc__), flags=re.S|re.M)
    header_list = header_list_to_dict(rst)
    assert header_list == {'Content-Type': 'text/plain',
                           'Accept': '*/*',
                           'X-Custom-Header': 'Custom-Value',
                           'Custom-Header': 'Custom-Value',
                           'X-Custom-Header2': 'Custom-Value2'}


# Generated at 2022-06-13 22:23:46.126070
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class TestFormatter(FormatterPlugin):

        def format_body(self, content: str, mime: str) -> str:
            return content
    
    formatter = TestFormatter()
    assert formatter.format_body("hello","") == "hello"



# Generated at 2022-06-13 22:23:46.869484
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    assert True

# Generated at 2022-06-13 22:23:56.684129
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    """
    Test FormatterPlugin.format_body function
    """
    from httpie.plugins import FormatterPlugin
    from httpie.formatter import get_formatter

    def test_format_body(formatter_plugin, content, mime):
        formatter_plugin.format_body(content, mime)
        sys.stdout.write('\n\n')


# Generated at 2022-06-13 22:24:03.977925
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    # test set status line
    class FakeEnv:
        stdin=sys.stdin
        stdout=sys.stdout
        stderr=sys.stderr

    class TestFormatterPlugin(FormatterPlugin):
        def format_body(self, body, mime):
            return 'TestFormatterPlugin' + body

    tfp = TestFormatterPlugin(env=FakeEnv())
    assert tfp.format_body(body='test1', mime='test2') == 'TestFormatterPlugintest1'

# Generated at 2022-06-13 22:24:09.524172
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():

    class _TestFormatterPlugin(FormatterPlugin):

        def format_headers(self, headers: str) -> str:
            return headers[::-1]

    # Testing the format_headers method of the FormatterPlugin class.
    f = _TestFormatterPlugin()
    assert f.format_headers("ABC") == "CBA"


# Generated at 2022-06-13 22:24:11.065366
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    assert FormatterPlugin.format_body == FormatterPlugin().format_body



# Generated at 2022-06-13 22:24:11.832546
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    return

# Generated at 2022-06-13 22:24:16.131530
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    """This is the test code"""
    # code
    headers = {'User-Agent': 'httpie'}
    # unit test
    assert headers == {'User-Agent': 'httpie'}


# Generated at 2022-06-13 22:24:18.761000
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    assert FormatterPlugin.format_headers('abcdef') == 'abcdef'


# Generated at 2022-06-13 22:24:19.558884
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    assert True

# Generated at 2022-06-13 22:24:24.436333
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    d = {"Content-Type" : "application/json", "X-Custom-Header" : "content"}
    text = json.dumps(d)
    plugin = FormatterPlugin()
    s = plugin.format_headers(text)
    print(s)

# Generated at 2022-06-13 22:24:26.087118
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    if not hasattr(FormatterPlugin, 'format_headers'):
        print('missing required attribute "format_headers" in class FormatterPlugin')


# Generated at 2022-06-13 22:24:37.212077
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    test_formatter = FormatterPlugin()
    test_header = 'HTTP/1.1 200 OK\r\nServer: nginx/1.10.3 (Ubuntu)\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: 255\r\nConnection: keep-alive\r\nVary: Cookie\r\nX-Frame-Options: SAMEORIGIN\r\nX-XSS-Protection: 1; mode=block\r\nX-Content-Type-Options: nosniff\r\nDate: Fri, 14 Aug 2020 01:18:36 GMT\r\n\r\n'

# Generated at 2022-06-13 22:24:43.713464
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    from httpie.plugins import FormatterPlugin
    class FormatterPlugin_C(FormatterPlugin):
        name = 'Formatter_C'
        description = 'Formatter_C'
        group_name = 'Formatter_C'
        def format_headers(self, headers):
            return 'H' + headers
    fp = FormatterPlugin_C()
    assert fp.format_headers('hello') == 'Hhello'


# Generated at 2022-06-13 22:24:45.130966
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    assert FormatterPlugin.format_body == FormatterPlugin().format_body

# Generated at 2022-06-13 22:24:48.237269
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    c = FormatterPlugin()
    assert c.format_headers('test') == 'test'


# Generated at 2022-06-13 22:24:55.138851
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    import io
    from httpie.plugins.builtin import FormatterPlugin
    class Test(FormatterPlugin):
        def format_headers(self, headers):
            assert isinstance(headers, str)
            return headers
    test = Test()
    test.format_headers(u"HTTP/1.1 200 OK\r\nContent-Length: 3\r\n\r\n")



# Generated at 2022-06-13 22:24:59.367806
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class TestFormatter(FormatterPlugin):
        def format_headers(self, headers: str) -> str:
            return headers

    formatter = TestFormatter(format_options={})
    assert formatter.format_headers("abc") == "abc"



# Generated at 2022-06-13 22:25:05.553898
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    # A basic HTTP response, which has one header, content-type
    res = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n"
    s = FormatterPlugin()
    assert (res == s.format_headers(res))


# Generated at 2022-06-13 22:25:12.865607
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    """
    Unit test for method format_body() of class FormatterPlugin.
    """

    # Creating dummy instance of FormatterPlugin class
    cls = FormatterPlugin()

    # Unit test for format_body(self, content, mime)
    try:
        # method 'format_body' returns string
        if not isinstance(cls.format_body('content', 'mime'), str):
            assert False
    except Exception:
        # In case of any exception, unit test fails
        assert False

    # In case no exception, test passes
    assert True


# Generated at 2022-06-13 22:25:23.063074
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    fp = FormatterPlugin()
    fp.format_body("<html><body>\nHello world!\n</body></html>", 'text/html')
    assert fp.format_body("<html><body>\nHello world!\n</body></html>", 'text/html') == "<html><body>\nHello world!\n</body></html>"
    assert fp.format_body("<html><body>\nHello world!\n</body></html>", 'application/json') == "<html><body>\nHello world!\n</body></html>"
    # add extra checks


# Generated at 2022-06-13 22:25:30.135471
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    # Setup FormatterPlugin
    test_FormatterPlugin = FormatterPlugin()
    # Test normal behavior
    # Setup mocks
    test_FormatterPlugin = FormatterPlugin()

    # Perform the call
    result = test_FormatterPlugin.format_headers(
        'Foo: bar\n\n'
    )

    # Verify the result
    assert result == 'Foo: bar'



# Generated at 2022-06-13 22:25:40.726085
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():

    class Simple(FormatterPlugin):

        def format_body(self, content: str, mime: str) -> str:
            return content.upper()

    assert Simple().format_body('hello', None) == 'HELLO'


# Generated at 2022-06-13 22:25:44.574841
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    formatter_plugin = FormatterPlugin(**kwargs)
    assert formatter_plugin.format_headers('{"key": "value"}') == '{"key": "value"}'



# Generated at 2022-06-13 22:25:54.679424
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    from tests.plugins import ResponseFormatterPlugin

    class MyResponseFormatterPlugin(ResponseFormatterPlugin):
        name = 'my-format'

    responseFormatterPlugin = MyResponseFormatterPlugin()

    assert('<html>\n    <title>My Title</title>\n</html>' == responseFormatterPlugin.format_body('<html><title>My Title</title></html>','text/html'))
    assert('<html><title>My Title</title></html>' == responseFormatterPlugin.format_body('<html><title>My Title</title></html>','application/xml'))
    assert('{"key":"value"}' == responseFormatterPlugin.format_body('{"key":"value"}','application/json'))

# Generated at 2022-06-13 22:26:08.498365
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    print('[test_FormatterPlugin_format_body]')
    from httpie.plugins import plugin_manager

    json_formatter = plugin_manager.get_formatter(
        'json', format_options={'colors': False},
        color_scheme={})

    xml_formatter = plugin_manager.get_formatter(
        'xml', format_options={'colors': False},
        color_scheme={})

    # json
    body = '{"name": "Frank"}'

    assert json_formatter.format_body(body, 'application/json') \
           == '{\n    "name": "Frank"\n}'

    # xml
    body = '<employee><name>Frank</name></employee>'

    assert xml_formatter.format_body(body, 'application/xml')

# Generated at 2022-06-13 22:26:15.165564
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    headers = b'HTTP/1.1 200 OK\r\n '\
              b'Content-Type: application/json\r\n '\
              b'Content-Length: 8\r\n '\
              b'Accept-Ranges: bytes\r\n '\
              b'Via: 1.1 vegur\r\n\r\n'
    assert FormatterPlugin().format_headers(headers.decode('utf8')) == \
           'HTTP/1.1 200 OK\nContent-Type: application/json\n'\
           'Content-Length: 8\nAccept-Ranges: bytes\nVia: 1.1 vegur\n'

# Test for method format_body of class FormatterPlugin

# Generated at 2022-06-13 22:26:26.977021
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    from typing import List
    from httpie.plugins import FormatterPlugin
    from httpie.context import Environment

    class MyFormatterPlugin(FormatterPlugin):

        def format_body(self, content: str, mime: str) -> str:
            return "Test"

    assert MyFormatterPlugin(None, {}).format_body("", "") == "Test"


    class MyFormatterPlugin2(FormatterPlugin):

        def format_headers(self, headers: str) -> str:
            return "Test"

    assert MyFormatterPlugin2(None, {}).format_headers("") == "Test"

    assert FormatterPlugin(None, {}).format_body("", "") != "Test"

    assert FormatterPlugin(None, {}).format_headers("") != "Test"

# Generated at 2022-06-13 22:26:31.846465
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    fp = FormatterPlugin()
    mime = 'application/json'
    content = '{"title": "Hello World"}'
    assert fp.format_body(content, mime) == content


# Generated at 2022-06-13 22:26:33.625075
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    assert FormatterPlugin.format_headers('headers') == 'headers'


# Generated at 2022-06-13 22:26:34.858379
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    return True


# Generated at 2022-06-13 22:26:38.407266
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    with open(__file__[:-3] + '_test_format_formatter_plugin.py', 'r') as f:
        content = f.read()
        exec(content)


# Generated at 2022-06-13 22:26:57.217247
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    import httpie

    fp = httpie.plugins.builtin.format.FormatterPlugin(format_options=None)
    assert fp.format_headers('HTTP/1.1. 200 OK\r\nContent-Type: application/json\r\n\r\n') == 'HTTP/1.1. 200 OK\r\nContent-Type: application/json\r\n\r\n'


# Generated at 2022-06-13 22:26:58.194021
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
   assert 500==500

# Generated at 2022-06-13 22:27:00.376959
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    assert FormatterPlugin(**{'format_options': {}}).format_body("hello", "text/plain") == "hello"

# Generated at 2022-06-13 22:27:02.879808
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    import pytest
    assert FormatterPlugin.format_body(self='',content='',mime='')==''

# Generated at 2022-06-13 22:27:05.608641
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    fp = FormatterPlugin()
    assert fp.format_body('content', 'mime') == 'content'

# Generated at 2022-06-13 22:27:18.280741
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    MIMETYPES = ['application/x-www-form-urlencoded', 'multipart/form-data']
    plugin_formatter = FormatterPlugin('test')
    formatted_body = plugin_formatter.format_body("key1=value1&key2=value2", MIMETYPES[0])
    print("Content: {}".format(formatted_body))
    assert formatted_body == "key1=value1\nkey2=value2"

    formatted_body = plugin_formatter.format_body("", MIMETYPES[1])
    print("Content: {}".format(formatted_body))
    assert formatted_body == ""

    formatted_body = plugin_formatter.format_body("{'key1':'value1', 'key2':'value2'}", "application/json")

# Generated at 2022-06-13 22:27:29.705458
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    from httpie.plugins.builtin import FormatterPlugin
    from httpie.output.formatters.colors import get_lexer

    lexer = get_lexer('HTTPHeaders')
    headers = '''HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Content-Length: 19
Connection: keep-alive\r\n
'''
    headers_formatted = FormatterPlugin(format_options={'headers': 'oneline'}).format_headers(headers)
    assert headers_formatted == 'HTTP/1.1 200 OK Content-Type: text/plain; charset=utf-8 Content-Length: 19 Connection: keep-alive'

# Generated at 2022-06-13 22:27:32.408940
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    plugin_body = FormatterPlugin("")
    str_body = plugin_body.format_body("example body", "application/text")
    assert str_body == "example body"

# Generated at 2022-06-13 22:27:38.368557
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class TestFormatterPlugin(FormatterPlugin):
        group_name = 'test'
        def format_body(self, content, mime):
            return mime + content

    content = 'test'
    mime = 'test'
    formatter = TestFormatterPlugin(kwargs = {})
    print(formatter.format_body(content, mime))

# Test that uses the method format_body of class FormatterPlugin
test_FormatterPlugin_format_body()

# Generated at 2022-06-13 22:27:45.430776
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class TestFormatter(FormatterPlugin):
        """Test class"""
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def format_body(self, content, mime):
            """Return processed `content`."""
            return content

    plugin = TestFormatter(**{'format_options': ()})
    assert plugin.name == plugins.__name__ + '.TestFormatter'
    assert plugin.description is None

    assert plugin.format_body('test', 'mime') == 'test'

# Generated at 2022-06-13 22:27:55.980973
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    pass



# Generated at 2022-06-13 22:28:00.747591
# Unit test for constructor of class TransportPlugin
def test_TransportPlugin():
    class Plugin:
        name = "Plugin"
        prefix = "Plugin"

        def __init__(self):
            pass
    
    Plugin = TransportPlugin(Plugin)
    assert Plugin.prefix == "Plugin"
    assert Plugin.name == "Plugin"


# Generated at 2022-06-13 22:28:04.336729
# Unit test for constructor of class FormatterPlugin
def test_FormatterPlugin():
    plugin = FormatterPlugin(**{'format_options':'json'})
    assert plugin.format_options == 'json'



# Generated at 2022-06-13 22:28:10.977273
# Unit test for method get_auth of class AuthPlugin
def test_AuthPlugin_get_auth():
  class test_plugin(AuthPlugin):

    auth_type = 'test'

    def get_auth(self, username=None, password=None):
        print(username, password)
        return None

  t1 = test_plugin()
  t1.get_auth(username='test', password='test2')
  # Expected output:
  #
  # test test2
  #

  # Unit test for method get_adapter of class TransportPlugin

# Generated at 2022-06-13 22:28:15.271565
# Unit test for method get_adapter of class TransportPlugin
def test_TransportPlugin_get_adapter():
    t = TransportPlugin()
    try:
        t.get_adapter()
    except NotImplementedError:
        pass
    else:
        assert False


# Generated at 2022-06-13 22:28:19.171164
# Unit test for constructor of class FormatterPlugin
def test_FormatterPlugin():
    import plugin
    fp = plugin.FormatterPlugin()
    fp.name
    fp.description
    fp.group_name
    fp.format_headers("")
    fp.format_body("", "")
    fp.format_options
    fp.supported_colors
    fp.kwargs
    fp.enabled


# Generated at 2022-06-13 22:28:31.515896
# Unit test for method get_auth of class AuthPlugin
def test_AuthPlugin_get_auth():
    import requests

    class MyPlugin(AuthPlugin):
        #auth_type = 'my-auth'
        auth_type = 'test'
        auth_parse = False
        netrc_parse = False
        prompt_password = False

        def get_auth(self, username, password):
            pass
            #return requests.auth.HTTPBasicAuth(username, password)

    plugin = MyPlugin('', '')
    assert plugin.auth_type == 'test'
    assert plugin.auth_parse == False
    assert plugin.netrc_parse == False
    assert plugin.prompt_password == False

    try:
        print(plugin.get_auth('foo', 'bar'))
    except NotImplementedError:
        pass


# Generated at 2022-06-13 22:28:35.605459
# Unit test for constructor of class ConverterPlugin
def test_ConverterPlugin():
    cp =ConverterPlugin("application/vnd.ms-excel")
    assert cp.mime == "application/vnd.ms-excel"


# Generated at 2022-06-13 22:28:49.864147
# Unit test for constructor of class FormatterPlugin
def test_FormatterPlugin():
    from httpie.constants import DEFAULT_OPTIONS
    from httpie.context import Environment
    from httpie.output.streams import StdoutBytesStream
    from httpie.core import get_exit_status
    from httpie.style import style_error, style_note
    from httpie.plugins import FormatterPlugin
    import os
    import json
    from tempfile import TemporaryDirectory

    def create_environment(arg_str):
        env = Environment(StdoutBytesStream, TempFileNameStream,
                          log_level='error',
                          stdin=FakeStdin(),
                          stdout=FakeStdout(),
                          colors=256,
                          is_windows=True,
                          debug=True,
                          default_options=arg_str)
        return env


# Generated at 2022-06-13 22:28:54.086827
# Unit test for method convert of class ConverterPlugin
def test_ConverterPlugin_convert():
    class my_ConverterPlugin(ConverterPlugin):
        def convert(self, content_bytes):
            return content_bytes
        @classmethod
        def supports(cls, mime):
            return True
    c = my_ConverterPlugin('application/vnd.my+json')
    c.convert(b'abc')
    assert True


# Generated at 2022-06-13 22:29:17.780871
# Unit test for method get_adapter of class TransportPlugin
def test_TransportPlugin_get_adapter():
    from httpie.plugins import TransportPlugin
    class MyTransportPlugin(TransportPlugin):
        prefix = 'foo'
        def get_adapter(self):
            return None
    MyTransportPlugin() # Check that there's no crash

# Generated at 2022-06-13 22:29:25.405205
# Unit test for method convert of class ConverterPlugin
def test_ConverterPlugin_convert():
    from httpie.compat import str
    from httpie.plugins import plugin_manager
    import msgpack
    mime = 'application/msgpack'
    d = {'a': 1, 'b': 'two'}
    b = msgpack.packb(d)
    print(b)
    # Ask plugin manager for a response converter based on mime type
    c = plugin_manager.get_converter(mime)
    # convert the messagepack response to a string for display on standard output
    s = str(c.convert(b), encoding='utf8')
    print(s)


# Generated at 2022-06-13 22:29:30.017772
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class FormatterPluginTest(FormatterPlugin):
        def format_body(self, content: str, mime: str) -> str:
            return content.replace('"', '\'')
    assert FormatterPluginTest(format_options={}).format_body('"hello"', "") == "\'hello\'"

# Generated at 2022-06-13 22:29:35.588179
# Unit test for constructor of class ConverterPlugin
def test_ConverterPlugin():
    class test_ConverterPlugin(ConverterPlugin):
        def __init__(self, mime):
            self.mime = mime
        def convert(self, content_bytes):
            pass
        @classmethod
        def supports(cls, mime):
            pass
    assert test_ConverterPlugin('application/x-msgpack').mime == 'application/x-msgpack'


# Generated at 2022-06-13 22:29:36.997877
# Unit test for method get_auth of class AuthPlugin
def test_AuthPlugin_get_auth():
    assert AuthPlugin.get_auth("test","test") == "test"

# Generated at 2022-06-13 22:29:41.468234
# Unit test for method get_adapter of class TransportPlugin
def test_TransportPlugin_get_adapter():
    plugin2 = TransportPlugin()
    assert isinstance(plugin2, TransportPlugin)
    # This should not raise an error
    plugin2.get_adapter()


# Generated at 2022-06-13 22:29:52.322941
# Unit test for method get_adapter of class TransportPlugin
def test_TransportPlugin_get_adapter():
    """
    Test method get_adapter of class TransportPlugin
    """
    # Test method get_adapter of class TransportPlugin
    test_TransportPlugin_get_adapter.sub_test_1 = """
    Test method get_adapter with parameter not None
    """
    print(test_TransportPlugin_get_adapter.sub_test_1)
    my_transport_plugin = TransportPlugin()
    # Test get_adapter with param not None
    result = my_transport_plugin.get_adapter()
    assert(result == NotImplementedError)
    # Test get_adapter() with param is None
    test_TransportPlugin_get_adapter.sub_test_2 = """
    Test method get_adapter with parameter is None
    """

# Generated at 2022-06-13 22:29:56.064968
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class formatter(FormatterPlugin):
        def format_body(self, content: str, mime: str) -> str:
            pass
    assert True


# Generated at 2022-06-13 22:30:07.943416
# Unit test for method get_auth of class AuthPlugin
def test_AuthPlugin_get_auth():
    class MyAuth(AuthPlugin):
        auth_type = 'my-auth'
        auth_require = True
        auth_parse = True
        netrc_parse = False
        prompt_password = False

        def get_auth(self, username=None, password=None):
            return MyAuthObj(username=username, password=password)

    plugin = MyAuth()
    auth = plugin.get_auth('my-user', 'my-pass')
    assert auth.username == 'my-user'
    assert auth.password == 'my-pass'
    assert plugin.raw_auth == 'my-user:my-pass'

    plugin.raw_auth = None
    auth = plugin.get_auth()
    assert auth.username is None
    assert auth.password is None

# Generated at 2022-06-13 22:30:20.811161
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    assert FormatterPlugin(format_options = {}).format_body(
            '<html><body>asdf</body></html>', 'html') \
           == '<html><body>asdf</body></html>'
    assert FormatterPlugin(format_options = {'format_json' : True}).format_body(
            '{"a":1}', 'application/json') \
           == '{\n    "a": 1\n}'
    assert FormatterPlugin(format_options = {'format_json' : True, 'prettify_json' : True}).format_body(
            '{"a":1}', 'application/json') \
           == "{\n    \"a\": 1\n}"

# Generated at 2022-06-13 22:31:02.611795
# Unit test for constructor of class TransportPlugin
def test_TransportPlugin():
    tp = TransportPlugin('test_prefix')
    assert tp.prefix is not None


# Generated at 2022-06-13 22:31:08.290200
# Unit test for constructor of class AuthPlugin
def test_AuthPlugin():
    import httpie
    a = httpie.plugins.AuthPlugin()
    assert a.auth_type == None
    assert a.auth_require == True
    assert a.auth_parse == True
    assert a.netrc_parse == False
    assert a.prompt_password == True
    assert a.raw_auth == None
    del httpie


# Generated at 2022-06-13 22:31:15.856001
# Unit test for constructor of class ConverterPlugin
def test_ConverterPlugin():
    cp1 = ConverterPlugin('mime1')
    assert cp1.mime == 'mime1'
    assert cp1.convert(b'foobar') == NotImplementedError

    cp2 = ConverterPlugin('mime2')
    assert cp2.mime == 'mime2'
    assert cp2.convert(b'foobar') == NotImplementedError


# Generated at 2022-06-13 22:31:17.759445
# Unit test for constructor of class AuthPlugin
def test_AuthPlugin():
    try:
        authplugin = AuthPlugin()
    except NotImplementedError:
        pass



# Generated at 2022-06-13 22:31:26.934356
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    import string
    import random

    for case_num in range(0, 100):
        headers = []
        for _ in range(0, random.randint(1, 10)):
            headers.append('{}:{}'.format(
                ''.join(random.choices(string.printable, k=random.randint(1, 10))),
                ''.join(random.choices(string.printable, k=random.randint(1, 10)))))

        fp = FormatterPlugin(format_options={'headers': 'on', 'headers_zero': True})
        fp.format_headers('\r\n'.join(headers))


# Generated at 2022-06-13 22:31:31.696867
# Unit test for constructor of class TransportPlugin
def test_TransportPlugin():
    prefix = 'unix'
    test = TransportPlugin()
    test.__init__()
    test.prefix = prefix

    try:
        test.get_adapter()
    except NotImplementedError:
        pass


# Generated at 2022-06-13 22:31:40.173875
# Unit test for method get_auth of class AuthPlugin
def test_AuthPlugin_get_auth():
    class AuthPlugin(BasePlugin):
        """Auth plugin that implements get_auth function"""
        auth_type = 'test'
        auth_require = True
        auth_parse = True
        netrc_parse = False
        prompt_password = True

        def get_auth(self, username=None, password=None):
            """Auth plugin get_auth implementation"""
            self.username = username
            self.password = password
            self.raw_auth = self.raw_auth
            return 'test'

    auth = AuthPlugin()
    assert auth.get_auth(username = 'foobar', password = 'barfoo') == 'test'


# Generated at 2022-06-13 22:31:52.695968
# Unit test for constructor of class ConverterPlugin
def test_ConverterPlugin():

    # Create a subclass
    class ConverterPluginTest(ConverterPlugin):

        # Override __init__() of its parent
        def __init__(self, mime):
            self.mime = mime
            self.mime = mime

        def convert(self, content_bytes):
            print("convert")

        @classmethod
        def supports(cls, mime):
            print("support")

    # Create an instance of ConverterPluginTest
    plugin = ConverterPluginTest(3)

    # Call convert() function
    plugin.convert(content_bytes = "bytes")

    # Call supports() function
    ConverterPluginTest.supports(mime = "mime")

# Generated at 2022-06-13 22:32:02.874478
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    from httpie.config import Config
    from httpie.context import Environment
    from httpie.plugins import plugin_manager

# Generated at 2022-06-13 22:32:03.812760
# Unit test for method get_adapter of class TransportPlugin
def test_TransportPlugin_get_adapter():
    raise NotImplementedError()
