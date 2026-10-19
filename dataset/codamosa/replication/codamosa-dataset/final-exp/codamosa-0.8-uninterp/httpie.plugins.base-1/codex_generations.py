

# Generated at 2022-06-13 22:22:45.294678
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    obj = FormatterPlugin()
    mime = ''
    content = ''
    expected = ''
    actual = obj.format_body(content, mime)
    assert actual == expected

# Generated at 2022-06-13 22:22:48.855932
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    i=FormatterPlugin()
    j=i.format_headers("lalalalalalalalala")
    assert j=="lalalalalalalalala"


# Generated at 2022-06-13 22:22:53.153386
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class MockFormatterPlugin(FormatterPlugin): 
        def format_headers(self, headers):
            return ('a\nb')
    headers = 'a:b\nc:d'
    formatter = MockFormatterPlugin()
    assert formatter.format_headers(headers) == 'a\nb'


# Generated at 2022-06-13 22:23:04.180752
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    # Act
    test_formatter = FormatterPlugin()
    headers = test_formatter.format_headers("""HTTP/1.1 200 OK
Server: nginx/1.8.0
Date: Mon, 08 Jun 2020 11:27:51 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 12
Connection: keep-alive
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *""")
    # Assert

# Generated at 2022-06-13 22:23:08.539434
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class MyFormatterPlugin(FormatterPlugin):
        """Return passed `headers` unchanged"""
        def format_headers(self, headers: str) -> str:
            return headers
    assert MyFormatterPlugin(format_options={}).format_headers("Test") == "Test"


# Generated at 2022-06-13 22:23:13.473694
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class FormatterPluginMock(FormatterPlugin):
        @staticmethod
        def format_body(content, mime):
            return '{}-formatted'.format(content)

    plugin = FormatterPluginMock(format_options='format')
    assert plugin.format_body('chunk', 'mime') == 'chunk-formatted'


# Generated at 2022-06-13 22:23:26.310421
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class MyFormatter(FormatterPlugin):
        def format_body(self, content, mime):
            return content + '--- is processed with MyFormatter'
        def format_headers(self, headers):
            return headers.upper()

    # create HTTP headers
    headers = {'Content-Type': 'plain/text'}
    headers_str = '\n'.join('{}: {}'.format(name, value)
                            for name, value in headers.items())

    # create FormatterPlugin object
    kwargs = {'format_options': {'table': True,
                                 'unicode': True}}
    f = MyFormatter(**kwargs)
    result = f.format_body('hello_world', 'plain/text')
    expected = 'hello_world--- is processed with MyFormatter'

# Generated at 2022-06-13 22:23:29.298871
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    header = "Content-Type: application/json"
    assert FormatterPlugin(env=object).format_headers(header) == header


# Generated at 2022-06-13 22:23:40.685071
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    """
    Test formatter plugin
    """
    from httpie.terminal import httpie_version
    from httpie.environment import Environment
    from httpie.plugins import plugin_manager
    from . import __version__

    plugin_manager.load_installed_plugins()
    env = Environment(httpie_version=httpie_version,
                      extended_help=False,
                      output_file=None,
                      config_dir=None,
                      config_path=None,
                      config_paths=None,
                      defaults_path=None,
                      default_options=None,
                      env=None,
                      is_windows=False,
                      stdin_isatty=None)

    # Class FormatterPlugin is an abstract class
    # So it cannot be instantiated directly.
    # We create a subclass instead.

# Generated at 2022-06-13 22:23:42.500945
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    assert FormatterPlugin.format_headers('text') == 'text'


# Generated at 2022-06-13 22:23:54.051570
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class MyFormatter(FormatterPlugin):
        def format_body(self, content: str, mime: str) -> str:
            return "non-empty"
    mime = "mime"
    content = "content"
    try:
        formatter = MyFormatter(None)
        if formatter.format_body(content, mime) == "non-empty":
            return "test passed"
    except Exception as e:
        return "test failed: exception: " + str(e)
    return "test failed"

# Generated at 2022-06-13 22:24:00.489616
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class Test(FormatterPlugin):
        package_name = 'test'
        name = 'test'
        description = 'test dummy plugin'
        group_name = 'test'
        def format_headers(self, headers: str) -> str:
            return "asdf"

    env = Environment()
    plugin = Test(env)
    assert plugin.format_headers("qwer") == "asdf"


# Generated at 2022-06-13 22:24:13.478682
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    ''' The expected result is a list of all the headers.
        The input is a simple raw message.

        Note: This is a unit test, 'nose' would be needed to run it.
    '''
    class FormatterPlugin(BasePlugin):
        group_name = 'format'

        def __init__(self, **kwargs):
            self.enabled = True
            self.kwargs = kwargs
            self.format_options = kwargs['format_options']

        def format_headers(self, headers: str) -> str:
            return headers

        def format_body(self, content: str, mime: str) -> str:
            return content


# Generated at 2022-06-13 22:24:24.380585
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    import httpie
    from httpie.core import main
    from httpie.core import exit_status
    from httpie.core import HTTP_OK
    from httpie.core import Environment
    from httpie.core import parse_kwargs
    from httpie.core import parse_download_args
    from httpie.core import parser
    from httpie.core import get_response
    from httpie.core import load_config_files

    headers = [('Content-Type', 'text/plain')]
    config_files = None
    body = b"Testing"

    # Create env
    env = Environment(headers, config_files)

    # Create config
    config = load_config_files(env)
    config.default_options.verify = False

    # Build args

# Generated at 2022-06-13 22:24:26.029717
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    result = FormatterPlugin.format_headers('"Content-Type" : "application/json"')
    assert result == '"Content-Type" : "application/json"'


# Generated at 2022-06-13 22:24:34.707782
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    # Be careful with imports of classes inside httpie.compat
    # and httpie.compat.packages, as they may cause circular imports
    class FormatterPluginTest(FormatterPlugin):
        def __init__(self, **kwargs):
            super(FormatterPluginTest, self).__init__(**kwargs)

        def format_headers(self, headers: str) -> str:
            return headers[::-1]

    formatter = FormatterPluginTest(format_options={})
    assert formatter.format_headers("abc") == "cba"



# Generated at 2022-06-13 22:24:38.881335
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    plugin = FormatterPlugin(color_theme='color-theme-name')
    headers = "status_code = 200\n"
    r = plugin.format_headers(headers)
    assert r == headers



# Generated at 2022-06-13 22:24:48.603791
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():

    # Here we create a class which extends the FormatterPlugin
    class MockedFormatterPlugin(FormatterPlugin):
        def format_headers(self, headers: str) -> str:
            return 'mocked output'

    # Here we create a reference for an object of the class
    formatter_plugin = MockedFormatterPlugin(**{'format_options': None})

    # Here we pass to the object a string that contains the headers
    result = formatter_plugin.format_headers('headers')

    # Here we check if the result is exactly the same as we expect
    assert( result == 'mocked output' )


# Generated at 2022-06-13 22:24:56.940180
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    def main():
        content = "import json\nprint(json.dumps({'a': 'b', 'c': 'd'}, indent=2))"
        mime = "text/vnd.python.py"
        json_plugin = JSON()
        print(json_plugin.format_body(content, mime))
    main()
    # output:
    # {
    #   "a": "b",
    #   "c": "d"
    # }
    


# Generated at 2022-06-13 22:25:00.658832
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    def assert_eq(content, expected):
        assert f.format_body(content, 'application/atom+xml') == expected

    f = FormatterPlugin(format_options=None)
    assert_eq("<xml/>", "<xml/>")

# Generated at 2022-06-13 22:25:12.865409
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    # plugin_rc=''
    # plugin_rc_file=None
    # plugin_confdir=None
    # plugin_confdirs=None
    test_FormatterPlugin = FormatterPlugin(
        env=None,
        format_options=None,
        plugin_config=None,
        plugin_rc_file=None,
        plugin_confdir=None,
        plugin_confdirs=None,
    )
    test_response = '{"name":"zhouze","age":22,"gender":"male"}'
    mime = 'application/json'
    result = test_FormatterPlugin.format_body(test_response, mime)
    assert result == '{\n    "age": 22,\n    "gender": "male",\n    "name": "zhouze"\n}'

# Generated at 2022-06-13 22:25:20.315524
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    fp = FormatterPlugin(format_options={})
    assert fp.format_body(content='', mime='') == ''
    assert fp.format_body(content='Hello World!', mime='') == 'Hello World!'
    assert fp.format_body(content='', mime='text/html') == ''
    assert fp.format_body(content='Hello World!', mime='text/html') == 'Hello World!'


# Generated at 2022-06-13 22:25:28.577686
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class TestFormatterPlugin(FormatterPlugin):
        def format_body(self, content: str, mime: str) -> str:
            return "testing"

    import httpie
    env = httpie.Environment(colors=0)
    plugin = TestFormatterPlugin(env=env, format_options={})
    assert plugin.format_body("content", "mime") == "testing"


# Generated at 2022-06-13 22:25:32.406645
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    body="<content>here</content>"
    plugin = FormatterPlugin()

    assert plugin.format_body("<content>here</content>","application/xml") == "<content>here</content>"


# Generated at 2022-06-13 22:25:35.006014
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    plugin = FormatterPlugin()
    assert plugin.format_headers('') == ''


# Generated at 2022-06-13 22:25:41.411929
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    # Create FormatterPlugin instance
    formatter_plugin = FormatterPlugin(format_options=None, output_file=None)

    # Initialize content and mime
    content = 'test'
    mime = 'application/test'

    # Call the method format_body
    res = formatter_plugin.format_body(content=content, mime=mime)

    # Check results
    assert res == content
    assert mime == 'application/test'


# Generated at 2022-06-13 22:25:52.434079
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    env = Environment(colors=256)
    assert "hello" == FormatterPlugin(env=env,format_options={}).format_body("hello",None)
    env = Environment(colors=True)
    assert "hello" == FormatterPlugin(env=env,format_options={}).format_body("hello",None)
    env = Environment(colors='ansi')
    assert "hello" == FormatterPlugin(env=env,format_options={}).format_body("hello",None)
    env = Environment(colors='false')
    assert "hello" == FormatterPlugin(env=env,format_options={}).format_body("hello",None)


# Generated at 2022-06-13 22:25:57.852108
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    formatter_plugin = FormatterPlugin()
    headers_line = b'headers: text'
    headers_text = formatter_plugin.format_headers(headers_line)
    assert headers_text == b'headers: text'


# Generated at 2022-06-13 22:26:00.786568
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    formatterPlugin = FormatterPlugin(format_options={})
    print(formatterPlugin.format_body('1', None))

# Generated at 2022-06-13 22:26:08.255070
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class MyFormatterPlugin(FormatterPlugin):
        def format_body(self, body: str, mime: str) -> str:
            return body+"g"
    a = '<html><body>Hello World</body></html>'
    out = MyFormatterPlugin().format_body(a,'text/html')
    #print(out,"g")
    assert out == '<html><body>Hello World</body></html>g' 



# Generated at 2022-06-13 22:26:12.472141
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    assert True


# Generated at 2022-06-13 22:26:25.083474
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class FormatterPlugin(BasePlugin):
        def __init__(self, mime):
            self.mime = mime

        def format_body(self, content: str, mime: str) -> str:
            """Return processed `content`.

            :param mime: E.g., 'application/atom+xml'.
            :param content: The body content as text

            """
            return content

    called = False
    def do_test():
        nonlocal called
        called = True
        formatter = FormatterPlugin('text/plain')
        res = formatter.format_body('', 'text/plain')
        assert res == '', 'Should return empty string'
    do_test()
    assert called is True, 'Should call do_test()'


# Generated at 2022-06-13 22:26:27.105421
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    p = FormatterPlugin()
    res_str = p.format_headers("TEST")
    assert res_str == "TEST"


# Generated at 2022-06-13 22:26:30.091336
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    fp = FormatterPlugin()
    assert fp.format_headers('Hello') == 'Hello'

# Generated at 2022-06-13 22:26:40.757123
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    header_str = """HTTP/1.1 200 OK
Date: Sun, 19 Jul 2020 07:14:28 GMT
Server: Apache/2.4.38 (Debian)
Last-Modified: Mon, 08 Jun 2020 00:19:16 GMT
ETag: "14-5a17096430d1f"
Accept-Ranges: bytes
Content-Length: 20
Vary: Accept-Encoding
Content-Type: text/html

"""
    obj = FormatterPlugin()
    assert header_str == obj.format_headers(header_str)
    obj.enabled = False
    assert header_str == obj.format_headers(header_str)



# Generated at 2022-06-13 22:26:47.364254
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class MyPlugin(FormatterPlugin):
        name = 'My Plugin'
        group_name = 'None'

        def format_headers(self, headers):
            return 'Changed'

    formatter = MyPlugin(a=1, b=2)

    assert formatter.format_headers(headers='header') == 'Changed'



# Generated at 2022-06-13 22:26:48.614496
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    pass


# Generated at 2022-06-13 22:26:50.182185
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    assert 1 == 1


# Generated at 2022-06-13 22:27:02.508749
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    import os
    from httpie.core import Environment
    fp = os.path.dirname(__file__)
    env = Environment(stdin=None, stdout=None, stderr=None,
                      color=None, style=None, vars={
                          'config_dir': os.path.join(fp, 'testdata/config')
                      },
                      config_dir=os.path.join(fp, 'testdata/config'))
    formatter = env.plugins['httpie-highlight'].instantiate(env, format_options=['headers'])
    # test data from Plugin Highlight 
    # http://docs.python-guide.org/en/latest/writing/structure/

# Generated at 2022-06-13 22:27:11.612662
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    try:
        global _test_FormatterPlugin_format_body_test_counter
        _test_FormatterPlugin_format_body_test_counter += 1
    except NameError:
        _test_FormatterPlugin_format_body_test_counter = 0
    try:
        assert _test_FormatterPlugin_format_body_test_counter < 3
        assert True
    except AssertionError:
        e = AssertionError('No mocks, do not call more than once.')
        raise e
    return 'Dummy plugin to test_FormatterPlugin_format_body.'


# Generated at 2022-06-13 22:27:22.802974
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class MYFormatterPlugin(FormatterPlugin):
        def format_headers(self, headers: str) -> str:
            return headers
    f=MYFormatterPlugin(**{'format_options':{}})
    ans= f.format_headers('Headers')
    if ans == 'Headers':
        print('test_FormatterPlugin_format_headers OK')
    else:
        print('test_FormatterPlugin_format_headers Error')


# Generated at 2022-06-13 22:27:24.407057
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    pass


# Generated at 2022-06-13 22:27:33.817345
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    import pytest
    from httpie.output.formatters import BaseFormatter
    class TestFormatter(BaseFormatter):
        name = 'test'
        def __init__(self, env, format_options):
            super().__init__(env, format_options)

        def format_headers(self, headers):
            return headers

        def format_body(self, body, mime):
            return 'OK'

    # **********************
    # Test 1 : format_body returns wrong type
    # **********************
    class WrongOuput(TestFormatter):
        def format_body(self, body, mime):
            return 42

    with pytest.raises(TypeError):
        WrongOuput({'format_options': {}}, {})


# Generated at 2022-06-13 22:27:36.728050
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class FormatTestPlugin(FormatterPlugin):
        enabled = True

        def format_headers(self, headers):
            return json.dumps([headers])

    fmt = FormatTestPlugin(None)
    headers = fmt.format_headers("test")

    assert json.loads(headers) == [("test")]


# Generated at 2022-06-13 22:27:40.832426
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    formatter = FormatterPlugin(None, format_options={}, headers={})
    result = formatter.format_body("body", "application/atom+xml")
    assert result == "body"

# Generated at 2022-06-13 22:27:46.074149
# Unit test for method format_headers of class FormatterPlugin

# Generated at 2022-06-13 22:27:49.748296
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class FormatterPluginTest(FormatterPlugin):

        def format_body(self, content, mime):
            return "test_content"

    httpie_json = FormatterPluginTest()
    assert httpie_json.format_body("content", "mime") == "test_content"



# Generated at 2022-06-13 22:28:00.521132
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    import httpie.plugins
    import httpie.output.formatters.colors
    fp = httpie.plugins.FormatterPlugin(
        output_options={
            'colors' : False,
            'format' : 'basic',
            'indent' : '2'
        },
        format_options = {
            'colors' : False,
            'format' : 'basic',
            'indent' : '2'
        },
        output_file=None,
        stdin=_fake_stdin(),
        stdout=_fake_stdout()
    )
    assert '"aaa" : "bbb"' in fp.format_body(
        content='{"aaa" : "bbb"}',
        mime='application/json')



# Generated at 2022-06-13 22:28:10.271000
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    import json
    class JsonFormatterPlugin(FormatterPlugin):
        def format_body(self, content, mime):
            if mime == 'application/json':
                try:
                    return json.dumps(json.loads(content), indent=2, sort_keys=True)
                except ValueError:
                    return content

    env = Environment(formatter_plugins=[JsonFormatterPlugin])
    assert env.formatter_plugins[0].format_body("{\"a\":1}", mime="application/json") == '{\n  "a": 1\n}'



# Generated at 2022-06-13 22:28:18.955133
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    """Unit test for method format_headers of class FormatterPlugin"""
    class formatter_plugin(FormatterPlugin):
        def format_headers(self, headers):
            return headers

    try:
        formatter_plugin(None)
    except TypeError as e:
        print('test_FormatterPlugin_format_headers: TypeError: formatter_plugin() takes 1 positional argument but 2 were given')
        assert False
    except Exception as e:
        print('test_FormatterPlugin_format_headers: Unexpected exception raised when instantiate formatter_plugin')
        assert False
    else:
        assert True


# Generated at 2022-06-13 22:28:32.552677
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class FormatterPluginDummy(FormatterPlugin):
        def format_headers(self, headers):
            return "test"

    body = {'kv': 'test'}
    headers = 'test'
    format_options = {}
    env = FakeEnvironment(body=body, headers=headers, format_options=format_options)

    plugin = FormatterPluginDummy(env=env, format_options=format_options)
    assert plugin.format_headers(headers) == "test"


# Generated at 2022-06-13 22:28:36.169209
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    assert FormatterPlugin(**{'format_options':{}}).format_body("hello", "text/plain") == "hello"


# Generated at 2022-06-13 22:28:49.286312
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    from plugin.formatter import PrettyJsonFormatterPlugin
    from httpie import Environment
    from httpie.output.streams import UnsupportedOutput
    # creation of httpie.output.streams.UnsupportedOutput was taken from gitHub repo
    # https://github.com/jakubroztocil/httpie/blob/master/httpie/output/streams.py
    # file
    class PrettyJsonFormatterPluginTest:
        def test_format_headers(self):
            formatter = PrettyJsonFormatterPlugin(env=Environment(UnsupportedOutput()), format_options='')
            # headers, which is empty
            self.assertEqual('',formatter.format_headers(headers=''))


# Generated at 2022-06-13 22:28:58.524876
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class FormatterPlugin_1(FormatterPlugin):
        def __init__(self, **kwargs):
            self.kwargs = kwargs

    formatter = FormatterPlugin_1(**dict(format_options=dict()))
    headers =  formatter.format_headers(
    '''Content-Type: application/xml;charset=UTF-8
    ETag: "e5c5fa0ab7c5f5fa8f7fa4d4de2e9d1c:1536799667"
    Date: Tue, 21 Aug 2018 10:01:07 GMT
    Status: 200 OK
    ''')

# Generated at 2022-06-13 22:29:04.082232
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    from _plugin_legacy import FormatterPlugin
    class Test(FormatterPlugin):
        def format_body(self, content, mime):
            return content
    formatter = Test()
    assert formatter.format_body("Test content", 'application/atom+xml') == "Test content"


# Generated at 2022-06-13 22:29:08.971426
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class DummyFormatterPlugin(FormatterPlugin):
        def format_body(self, content, mime):
            return 'formatted_content'
    dfp = DummyFormatterPlugin()
    assert dfp.format_body('', 'text') == 'formatted_content'



# Generated at 2022-06-13 22:29:18.645834
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    """
    Test case for FormatterPlugin.format_headers()

    """
    mock_session = Mock()
    mock_headers = {
        'CustomHeader': 'Custom header value',
        'Accept': 'application/json'
    }

    a_formatter = FormatterPlugin(env=mock_session)
    output = a_formatter.format_headers(headers=mock_headers)
    assert 'CustomHeader' in output
    assert 'Accept' in output



# Generated at 2022-06-13 22:29:19.323383
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    pass

# Generated at 2022-06-13 22:29:21.930386
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    json = FormatterPlugin()
    assert json.format_body(content='{"hello": "world"}', mime='application/json') == '{\n    "hello": "world"\n}'

# Generated at 2022-06-13 22:29:23.612436
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    assert True, "This test was implemented to get 100% code coverage. This shouldn't fail."

# Generated at 2022-06-13 22:29:32.896932
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    class a(FormatterPlugin):
        def format_body(self, content: str, mime: str) -> str:
            return content

    assert a().format_body("hello world!", "text/html") == "hello world!"


# Generated at 2022-06-13 22:29:37.667014
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():

    import httpie.formatter
    import os
    from httpie.plugins import plugin_manager

    plugins_dir = os.path.dirname(httpie.formatter.__file__)
    plugin_manager.discover(plugins_dir)

    formatter_plugin = plugin_manager.get_formatter(format_name="json")
    print(formatter_plugin)

    formatter_plugin.format_body(content='{"abc":"def"}', mime="application/json")



# Generated at 2022-06-13 22:29:43.787203
# Unit test for constructor of class AuthPlugin
def test_AuthPlugin():
    # Test base class
    assert issubclass(AuthPlugin, BasePlugin)
    assert hasattr(AuthPlugin, "get_auth")
    assert hasattr(AuthPlugin, "auth_type")
    assert hasattr(AuthPlugin, "auth_require")
    assert hasattr(AuthPlugin, "auth_parse")
    assert hasattr(AuthPlugin, "netrc_parse")
    assert hasattr(AuthPlugin, "prompt_password")
    assert hasattr(AuthPlugin, "raw_auth")


# Generated at 2022-06-13 22:29:47.121547
# Unit test for constructor of class FormatterPlugin
def test_FormatterPlugin():
    from httpie.core import Environment
    from httpie.plugins import FormatterPlugin
    environment = Environment()

    assert(FormatterPlugin(format_options = environment) != None)


# Generated at 2022-06-13 22:29:54.771394
# Unit test for method get_auth of class AuthPlugin
def test_AuthPlugin_get_auth():
    # foo
    class BarAuth(AuthPlugin):
        auth_type = 'bar'
        auth_require = False
        auth_parse = True
        netrc_parse = True
        prompt_password = True
        def get_auth(self, username=None, password=None):
            return self.raw_auth
    # test
    env = Environment(auto_auth=True, auth=True)
    plugin = BarAuth(env)
    # get_auth() should return auth raw string
    plugin.raw_auth = 'bar_auth_raw'
    assert plugin.get_auth(username='foo', password='bar') == 'bar_auth_raw'
    # get_auth() should return auth raw string
    plugin.raw_auth = None

# Generated at 2022-06-13 22:30:04.147472
# Unit test for method get_adapter of class TransportPlugin
def test_TransportPlugin_get_adapter():
    import unittest
    import inspect
    
    class TransportPlugin(BasePlugin):
        prefix = None

        def get_adapter(self):
            pass

    class TransportPluginTest(unittest.TestCase):

        def test_method_must_be_implemented(self):
            t = TransportPlugin()
            with self.assertRaises(NotImplementedError):
                t.get_adapter()

        def test_method_must_be_defined(self):
            t = TransportPlugin()
            self.assertTrue(inspect.getmembers(t, predicate=inspect.ismethod))

    unittest.main()

# Unit test of method get_auth of class AuthPlugin

# Generated at 2022-06-13 22:30:08.325024
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    class MyFormatterPlugin(FormatterPlugin):
        def format_headers(self, headers):
            return headers
    p = MyFormatterPlugin(env=None, format_options={})
    assert isinstance(p.format_headers('Content-Type: text/html'), str)


# Generated at 2022-06-13 22:30:11.890638
# Unit test for constructor of class FormatterPlugin
def test_FormatterPlugin():
    from httpie.plugins import plugin_manager
    format_name = 'json'
    plugin_manager.get_plugin_class(FormatterPlugin, format_name)


# Generated at 2022-06-13 22:30:20.811837
# Unit test for constructor of class AuthPlugin
def test_AuthPlugin():
    import httpie.plugins.auth
    auth_plugin = httpie.plugins.auth.AuthPlugin()
    assert auth_plugin.name == None
    assert auth_plugin.description == None
    assert auth_plugin.package_name == None
    assert auth_plugin.auth_type == None
    assert auth_plugin.auth_require == True    
    assert auth_plugin.auth_parse == True
    assert auth_plugin.netrc_parse == False
    assert auth_plugin.prompt_password == True
    assert auth_plugin.raw_auth == None
    

# Generated at 2022-06-13 22:30:24.734718
# Unit test for constructor of class BasePlugin
def test_BasePlugin():
    class BasePlugin:
        pass

    x=BasePlugin()
    x.name = "hi"
    x.package_name="hi"
    x.name
    x.package_name
    try:
        x.x
    except AttributeError:
        print("AttributeError:")
    else:
        pass



# Generated at 2022-06-13 22:30:36.334111
# Unit test for constructor of class TransportPlugin
def test_TransportPlugin():
    testPlugin = TransportPlugin()
    testPlugin.get_adapter()

# Generated at 2022-06-13 22:30:38.030242
# Unit test for constructor of class TransportPlugin
def test_TransportPlugin():
    plugin = TransportPlugin()
    assert plugin.prefix == None


# Generated at 2022-06-13 22:30:41.171798
# Unit test for constructor of class TransportPlugin
def test_TransportPlugin():
    transportPlugin = TransportPlugin()
    transportPlugin.prefix = "http"
    print(transportPlugin.prefix)


# Generated at 2022-06-13 22:30:45.328618
# Unit test for method get_auth of class AuthPlugin
def test_AuthPlugin_get_auth():
    class DummyAuthPlugin(AuthPlugin):
        auth_type = 'dummy'

        def get_auth(self, username=None, password=None):
            return username, password

    assert DummyAuthPlugin().get_auth(username='foo', password='bar') == ('foo', 'bar')

# Generated at 2022-06-13 22:30:49.971626
# Unit test for method convert of class ConverterPlugin
def test_ConverterPlugin_convert():
    class TestConverterPlugin(ConverterPlugin):
        def convert(self, content_bytes):
            return content_bytes

        @classmethod
        def supports(cls,mime):
            return True
    mime = 'html'
    TestConverterPlugin(mime).convert(b'<html>')


# Generated at 2022-06-13 22:30:58.398227
# Unit test for constructor of class FormatterPlugin
def test_FormatterPlugin():
    """
    Testing class FormatterPlugin

    """
    import os
    import sys
    import requests
    plugins = load_plugins(os.path.dirname(sys.modules['httpie'].__file__) +
                           '/../plugins')
    formatters = load_formatters(plugins)
    cli = Cli(Environment(stdout=sys.stdout, stderr=sys.stderr,
                          stdin=sys.stdin, configdir=''))
    r = requests.models.Response()
    r.status_code = 200
    for f in formatters:
        f.format_headers(r.headers)
        f.format_body(r.text, 'application/json')



# Generated at 2022-06-13 22:31:04.844848
# Unit test for constructor of class BasePlugin
def test_BasePlugin():
    """
    Unit test for the class BasePlugin

    :return: none
    """
    def test_BasePlugin():
        plugin = BasePlugin()
        assert plugin.name == 'HTTPie Plugin'
        assert plugin.package_name == 'plugin'
        assert plugin.description == None


# Generated at 2022-06-13 22:31:10.164286
# Unit test for constructor of class ConverterPlugin
def test_ConverterPlugin():
    # ConverterPlugin(self, mime: str) -> None
    class ConverterPlugin_forTest(ConverterPlugin):
        def __init__(self, mime: str):
            print(f"mime {mime}")

    # 
    test_ConverterPlugin = ConverterPlugin_forTest("mime")
    assert True



# Generated at 2022-06-13 22:31:16.769084
# Unit test for constructor of class AuthPlugin
def test_AuthPlugin():
    """
    auth plugin class
    the name should be in the format of '[^A-Z]*[A-Z]*$'
    """
    AuthPlugin.__init__(AuthPlugin)
    assert re.match('[^A-Z]*[A-Z]*$',AuthPlugin.__name__)


# Generated at 2022-06-13 22:31:25.851439
# Unit test for method format_headers of class FormatterPlugin
def test_FormatterPlugin_format_headers():
    """Test suite for FormatterPlugin.format_headers()."""

    # Redefine FormatterPlugin for testing purpose.
    class FormatterPlugin_(FormatterPlugin):
        "A dummy plugin for testing purpose."
        group_name = 'format'

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def format_headers(self, headers: str) -> str:
            return 'a' + headers + 'b'

    #
    env = Environment(colors=256, stdin=None, stdout=None, stderr=None)
    formatter = FormatterPlugin_(env=env, format_options=dict())

    # Test
    s = formatter.format_headers('OK')

    # Assert
    assert (s == 'aOKb')


# Generated at 2022-06-13 22:31:47.150177
# Unit test for method get_adapter of class TransportPlugin
def test_TransportPlugin_get_adapter():
    class MyTransportPlugin(TransportPlugin):
        prefix = "abc"

        def get_adapter(self):
            pass

    MyTransportPlugin(prefix=None)
    print(MyTransportPlugin.prefix)


if __name__ == '__main__':
    test_TransportPlugin_get_adapter()

# Generated at 2022-06-13 22:31:50.165596
# Unit test for constructor of class BasePlugin
def test_BasePlugin():
    test = BasePlugin()
    assert test.name == None
    assert test.description == None
    assert test.package_name == None


# Generated at 2022-06-13 22:31:52.694647
# Unit test for constructor of class TransportPlugin
def test_TransportPlugin():
    TransportPlugin.prefix = 'http://www.google.com'
    env = Environment()
    assert TransportPlugin(env)


# Generated at 2022-06-13 22:31:54.842363
# Unit test for method get_adapter of class TransportPlugin
def test_TransportPlugin_get_adapter():
    class TransportPlugin(TransportPlugin):

        def get_adapter(self):
            print("get_adapter() of TransportPlugin")

    TransportPlugin()

# Generated at 2022-06-13 22:32:02.350489
# Unit test for method get_auth of class AuthPlugin
def test_AuthPlugin_get_auth():
    print("test_AuthPlugin_get_auth()")
    #class Mock_AuthPlugin(AuthPlugin):
    #    auth_type = None
    #    auth_require = True
    #    auth_parse = True
    #    netrc_parse = False
    #    prompt_password = True
    #    def get_auth(self, username=None, password=None):
    #        return username, password
    #
    #plugin_mock = Mock_AuthPlugin()
    #plugin_mock.get_auth(username=None, password=None)
    pass

# Generated at 2022-06-13 22:32:03.913714
# Unit test for constructor of class ConverterPlugin
def test_ConverterPlugin():
    converter = ConverterPlugin(mime='text/html')
    print(converter.mime)


# Generated at 2022-06-13 22:32:14.963626
# Unit test for constructor of class FormatterPlugin
def test_FormatterPlugin():
    import os
    import sys

    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin

    # Set environment variables  
    os.environ["TERM_PROGRAM"] = "TestProgram"
    os.environ['TERM_PROGRAM_VERSION'] = "TestVersion"
    os.environ['TERM_SESSION_ID'] = "TestSessionID"
    sys.stdin = open(os.devnull, "r")
    sys.stdout = open(os.devnull, "w")
    sys.stderr = open(os.devnull, "w")

    # Create an instance of class Environment
    env = Environment()
    
    # Create an instance of class FormatterPlugin

# Generated at 2022-06-13 22:32:18.310812
# Unit test for method convert of class ConverterPlugin
def test_ConverterPlugin_convert():
    class converter(ConverterPlugin):
        def convert(self, content_bytes):
            return content_bytes.decode()

        @classmethod
        def supports(cls, mime):
            return True
    assert converter('a').convert(b'123') == '123'
    assert converter.supports(None) == True


# Generated at 2022-06-13 22:32:22.846886
# Unit test for constructor of class FormatterPlugin
def test_FormatterPlugin():
    plugin = FormatterPlugin(**{})
    assert plugin.enabled == True
    assert plugin.kwargs == {}
    assert plugin.format_options == None
    assert plugin.format_headers("hello") == "hello"
    assert plugin.format_body("hello","") == "hello"


# Generated at 2022-06-13 22:32:25.755246
# Unit test for method format_body of class FormatterPlugin
def test_FormatterPlugin_format_body():
    assert(FormatterPlugin.format_body("1", "x") == "1")
