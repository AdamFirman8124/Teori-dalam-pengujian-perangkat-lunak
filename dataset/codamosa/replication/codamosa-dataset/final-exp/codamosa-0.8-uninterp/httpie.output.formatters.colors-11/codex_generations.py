

# Generated at 2022-06-13 21:51:40.153816
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import os
    import sys
    import tempfile
    import httpie.cli
    sys.stderr = tempfile.TemporaryFile("w")
    env = httpie.cli.Environment()
    env.session = httpie.Session(env)
    env.colors = 256

# Generated at 2022-06-13 21:51:45.652539
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from .http import HttpRequest
    from httpie.output.streams import StdoutStream
    from httpie.config import Config
    from httpie.context import Environment
    environment = Environment(config=Config(), stdout=StdoutStream(), stderr=None)
    request = HttpRequest(
        method='GET',
        url='https://github.com/jakubroztocil/httpie',
        headers={'Accept': 'application/json'},
        body=None,
        environment=environment
    )
    formatter = ColorFormatter(env=environment, explicit_json=False, color_scheme='solarized')
    request.format_http(formatter=formatter)
    assert formatter is not None

# Generated at 2022-06-13 21:51:51.472209
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class("manni") == pygments.styles.get_style_by_name("manni")
    assert ColorFormatter.get_style_class("monokai") == pygments.styles.get_style_by_name("monokai")
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style
    assert ColorFormatter.get_style_class("dark") == pygments.styles.get_style_by_name("dark")

# Generated at 2022-06-13 21:51:54.252945
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter = ColorFormatter(Environment(vars={"httpie.colors":True}))
    assert color_formatter.formatter.__class__ == Terminal256Formatter


# Generated at 2022-06-13 21:51:57.636164
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    headers = '''label: mongodb://localhost:27017/
label2: mongodb: //localhost:27017/
label3: mongodb://localhost:27017/
'''
    # print(ColorFormatter().format_headers(headers))



# Generated at 2022-06-13 21:52:05.851456
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.output.streams import UnsupportedEnvironment
    import httpie.compat
    import io
    import sys
    import httpie.context
    import httpie.core
    import httpie.plugins
    env = httpie.context.Environment()
    env.stdout = io.StringIO()

    httpie.plugins.load_internal_plugins()
    httpie.plugins.load_external_plugins()

    env.colors = 256
    color_formatter = httpie.plugins.lookup_plugin('color_formatter', env)

    request = httpie.core.Request(
        1234,
        'GET',
        'https://httpbin.org/get',
        '',
        {},
        [],
        {}
    )

# Generated at 2022-06-13 21:52:20.830802
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2022-06-13 21:52:32.600653
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    # type: () -> None
    """
    Ensure that the format_headers method of the ColorFormatter can
    format HTTP headers.
    """

    formatter = ColorFormatter(env=Environment())
    assert formatter.formatter

    # simple case
    headers = '''\
HTTP/1.1 200 OK
Content-Type: application/json
Server: example.org

'''

    # normal case

# Generated at 2022-06-13 21:52:39.480145
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    """
    Test ColorFormatter.__init__()
    """
    import httpie.cli
    env = httpie.cli.Environment()
    # Test environment variable HTTPIE_COLORS == 0
    env.colors = 0
    cf = ColorFormatter(env)
    assert not cf.enabled
    # Test environment variable HTTPIE_COLORS == 1 and terminal support colors
    env.colors = 1
    cf = ColorFormatter(env)
    assert cf.enabled
    # Test environment variable HTTPIE_COLORS == 256 and terminal 256 colors is not supported
    env.colors = 256
    cf = ColorFormatter(env)
    assert cf.enabled
    # Test environment variable HTTPIE_COLORS == 1 and terminal does not support colors
    env.colors = 1
    cf = ColorFormatter(env)
    assert not cf

# Generated at 2022-06-13 21:52:46.663609
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    """
    Unit test for SimplifiedHTTPLexer.
    """

    headers_txt = '''GET /foo HTTP/1.1\r
Host: localhost:8080\r
User-Agent: httpie/0.9.4\r
Accept-Encoding: gzip, deflate, compress\r
Accept: */*\r
Connection: keep-alive\r
\r
'''
    t = SimplifiedHTTPLexer()
    tokens = t.get_tokens(headers_txt)

# Generated at 2022-06-13 21:52:55.449845
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    cf = ColorFormatter(None, False, 'default', None)
    style_class = cf.get_style_class('solarized')
    assert issubclass(style_class, pygments.style.Style)

# Generated at 2022-06-13 21:53:06.708268
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.compat import is_windows
    from httpie.context import Environment
    if is_windows:
        return
    env = Environment(colors=256)
    formatter = ColorFormatter(env,color_scheme='solarized')

# Generated at 2022-06-13 21:53:18.549257
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    """
    Tests :class:`httpie.plugins.colors.ColorFormatter.format_headers` using
    pygments' mock formatter..
    """
    from .mocks import MockFormatter
    from .mocks import MockFormatterBuffer
    from .mocks import MockLexer
    from .mocks import MockLexerBuffer
    from .mocks import MockToken
    from .mocks import MockTokenSource

    cf = ColorFormatter(Environment())

    # Prepare formatter and lexer mocks
    formatter = MockFormatter(MockFormatterBuffer())
    formatter.get_style_defs = lambda: ''
    formatter.wrap = lambda x, *args, **kwargs: x
    formatter.__class__.name = 'mockformatter'

    lxb = MockLexerBuffer()
    lxb

# Generated at 2022-06-13 21:53:19.218264
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert True

# Generated at 2022-06-13 21:53:24.513466
# Unit test for function get_lexer
def test_get_lexer():
    lexer = get_lexer(
        mime='application/json',
        explicit_json=True,
        body=''
    )
    assert lexer == pygments.lexers.get_lexer_by_name('json')

# Generated at 2022-06-13 21:53:34.719952
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    class testEnv:
        colors = 256
    env = testEnv()
    test_subject = ColorFormatter(
        env=env,
        format='none',
        explicit_json=False,
        color_scheme=AUTO_STYLE
    )

    input = {
        'Content-Type': ['"application/json; charset=utf-8"'],
        'Date': ['"Sat, 21 Sep 2019 12:07:33 GMT"'],
        'Transfer-Encoding': ['"chunked"']
    }


# Generated at 2022-06-13 21:53:48.889532
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    config = {'color_scheme': 'auto'}
    color_formatter = ColorFormatter(config)
    assert color_formatter.color_scheme == 'auto'
    assert color_formatter.formatter == TerminalFormatter()

    config = {'color_scheme': 'solarized'}
    color_formatter = ColorFormatter(config)
    assert color_formatter.color_scheme == 'solarized'
    assert color_formatter.formatter == TerminalFormatter()

    config = {'color_scheme': 'fruity'}
    color_formatter = ColorFormatter(config)
    assert color_formatter.color_scheme == 'fruity'
    assert color_formatter.formatter == TerminalFormatter()


# Generated at 2022-06-13 21:53:57.097419
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # Test 1
    mime = 'text/html'
    body = ''
    explicit_json = False
    
    result = ColorFormatter.get_lexer_for_body(mime, explicit_json, body) 
    assert result is None
    
    # Test 2
    mime = 'text/html'
    body = '<html></html>'
    explicit_json = False
    
    result = ColorFormatter.get_lexer_for_body(mime, explicit_json, body) 
    assert result is None
    
    # Test 3
    mime = 'application/json'
    body = ''
    explicit_json = True
    
    result = ColorFormatter.get_lexer_for_body(mime, explicit_json, body) 
    assert result is None
    
   

# Generated at 2022-06-13 21:54:02.120014
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    lexer = ColorFormatter(None).get_lexer_for_body(
        mime='application/json',
        body='',
    )
    assert lexer == pygments.lexers.get_lexer_by_name('json')

    lexer = ColorFormatter(None).get_lexer_for_body(
        mime='application/vnd.api+json',
        body='',
    )
    assert lexer == pygments.lexers.get_lexer_by_name('json')

    lexer = ColorFormatter(None).get_lexer_for_body(
        mime='text/plain',
        body='',
    )
    assert lexer.name == 'Text only'
    assert isinstance(lexer, pygments.lexers.special.TextLexer)


# Generated at 2022-06-13 21:54:08.930265
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    env = Environment(colors=256)
    color_formatter = ColorFormatter(env, color_scheme='solarized')
    response_headers = '''HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 5742
Content-Type: application/json
Date: Sun, 07 Oct 2018 15:47:56 GMT
Vary: Accept, Accept-Encoding
X-Powered-By: Express
'''

# Generated at 2022-06-13 21:54:22.286476
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # System (travis) does not have Pygments lexer for GV
    lexer = ColorFormatter.get_lexer_for_body('image/vnd.graphviz', '{}')
    assert lexer is None

    lexer = ColorFormatter.get_lexer_for_body('image/png', '{}')
    assert lexer is None

    lexer = ColorFormatter.get_lexer_for_body('image/svg+xml', '{}')
    assert lexer is None

    lexer = ColorFormatter.get_lexer_for_body('text/plain', '{}')
    assert lexer is None

# Generated at 2022-06-13 21:54:26.075603
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter = ColorFormatter(Environment(), False, None)
    assert color_formatter.formatter.__class__.__name__ == "TerminalFormatter"

# Generated at 2022-06-13 21:54:39.929916
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment
    from httpie import input
    from httpie.plugins import plugin_manager

    class FakeResponse:
        headers = {'content-type': 'text/html'}
        status_code = 200

    plugin_manager.load_installed_plugins()
    env = Environment()
    env.parser = input.FileMemoryInputParser()
    env.stdin = 'http/1.1'
    formatter = ColorFormatter(env)
    response = FakeResponse()
    result = formatter.format_body('', response)
    assert 200 == response.status_code
    assert '\x1b[38;5;246m' == result[0:10]
    assert '\x1b[0m' == result[-4:]

# Generated at 2022-06-13 21:54:49.204329
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import pytest

    env = Environment()
    env.colors = 256

    colorFormatter = ColorFormatter(env)


# Generated at 2022-06-13 21:54:50.807280
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    pass



# Generated at 2022-06-13 21:55:03.039112
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import httpie.core
    import httpie.plugins.formatter.colors
    import httpie.plugins.formatter.json
    argv = ['/httpie.py', 'http://example.com']
    env = httpie.core.Environment(argv)
    cf = httpie.plugins.formatter.colors.ColorFormatter(env)
    jf = httpie.plugins.formatter.json.JSONFormatter(env)
    headers = 'Accept:application/json\nContent-Type:application/json\n'
    print("{0}\n{1}\n{2}\n{3}".format(argv, env, cf, headers))
    print(cf.format_headers(headers))

# Generated at 2022-06-13 21:55:05.722755
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('default') == pygments.styles.get_style_by_name('default')
    assert ColorFormatter.get_style_class('SOLARIZED_STYLE') == Solarized256Style

# Generated at 2022-06-13 21:55:13.120685
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.output.streams import get_response_stream
    from httpie.core import Environment
    env = Environment()
    env.colors = 256
    color_formatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert isinstance(color_formatter.formatter, Terminal256Formatter)
    assert isinstance(color_formatter.http_lexer, SimplifiedHTTPLexer)
    assert not isinstance(color_formatter.http_lexer, PygmentsHttpLexer)
    assert color_formatter.enabled
    assert color_formatter.formatter.style == Solarized256Style

# Generated at 2022-06-13 21:55:17.680485
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # Mock a response and the formatter
    response = {
        'content': {
            'mime': 'application/json',
            'content': '{"key": "value"}'
        }
    }
    formatter = ColorFormatter(Environment())

    assert formatter.format_body(response['content']['content'], response['content']['mime']) == '{\n  "key": "value"\n}\n'

# Generated at 2022-06-13 21:55:19.096817
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    f = ColorFormatter({})

# Generated at 2022-06-13 21:55:41.580701
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import os
    from httpie.context import Environment
    env = Environment()
    color_scheme = 'auto'
    explicit_json = False
    cf = ColorFormatter(env, explicit_json, color_scheme)
    assert cf.explicit_json == False
    assert cf.http_lexer is not None
    assert cf.formatter is not None
    color_scheme = 'fruity'
    cf = ColorFormatter(env, explicit_json, color_scheme)
    assert cf.explicit_json == False
    assert cf.http_lexer is not None
    assert cf.formatter is not None
    color_scheme = 'solarized'
    cf = ColorFormatter(env, explicit_json, color_scheme)
    assert cf.explicit_json == False
    assert cf.http

# Generated at 2022-06-13 21:55:55.587154
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    # Request-Line
    text = 'GET /foo HTTP/1.1\n'
    tokens = [
        (pygments.token.Name.Function, 'GET'),
        (pygments.token.Text, ' '),
        (pygments.token.Name.Namespace, '/foo'),
        (pygments.token.Text, ' '),
        (pygments.token.Keyword.Reserved, 'HTTP'),
        (pygments.token.Operator, '/'),
        (pygments.token.Number, '1.1'),
        (pygments.token.Text, '\n'),
    ]
    assert SimplifiedHTTPLexer().get_tokens(text) == tokens

    # Response Status-Line
    text = 'HTTP/1.1 200 OK\n'

# Generated at 2022-06-13 21:56:02.644923
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    import io
    import sys

    if sys.version_info >= (3, 0):
        stdout = io.StringIO()
    else:
        stdout = io.BytesIO()

    lexer = SimplifiedHTTPLexer()
    formatter = Terminal256Formatter(style=Solarized256Style)
    pygments.highlight(code="""
HTTP/1.1 200 OK
Transfer-Encoding: chunked
Response headers; are key-value pairs
""", lexer=lexer, formatter=formatter, outfile=stdout)
    content = stdout.getvalue()
    assert content.strip() == "\x1b[38;5;141mHTTP/1.1 200 OK"



# Generated at 2022-06-13 21:56:18.556868
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.core import http_status_codes
    from httpie.context import Environment
    env = Environment()
    colorformatter = ColorFormatter(env, True, 'solarized')
    # A response with the default colorformatter colors

# Generated at 2022-06-13 21:56:21.955294
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('monokai') == pygments.styles.get_style_by_name('monokai')

# Generated at 2022-06-13 21:56:31.974927
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    """
    class httpie.plugins.formatter.colors.ColorFormatter
    def get_lexer_for_body(self, mime: str, body: str) -> Optional[Type[Lexer]]:
    """
    c = ColorFormatter(Environment(), explicit_json=False, color_scheme=DEFAULT_STYLE, **{})
    assert c.get_lexer_for_body('application/json', '{"message":"hello world"}') == pygments.lexers.get_lexer_by_name('json')
    assert c.get_lexer_for_body('application/json', '{"message":"hello world"}') != pygments.lexers.get_lexer_by_name('text')
    assert c.get_lexer_for_body('application/json', '{"message":"hello world"}')

# Generated at 2022-06-13 21:56:38.758056
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Depends on pygments
    from httpie.context import Environment
    environment = Environment(colors=256,
                              style=SOLARIZED_STYLE,
                              )
    formatter = ColorFormatter(env=environment)
    assert formatter.formatter is not None
    assert formatter.http_lexer is not None
    assert formatter.explicit_json is False

# Generated at 2022-06-13 21:56:47.733067
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    headers = """
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 28
    """
    body = """
{
    "key": "value"
}
    """
    env = Environment()
    env.colors = 256
    formatter = ColorFormatter(env)
    result = formatter.format_body(body, "application/json")
    # Check that the body is not colored
    assert result == body

# Generated at 2022-06-13 21:56:54.881976
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(AUTO_STYLE) is None
    assert ColorFormatter.get_style_class('fruity') == pygments.styles.get_style_by_name('fruity')
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style

# Generated at 2022-06-13 21:57:01.412635
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    ColorFormatter(env=Environment(colors=True, is_terminal=True))
    ColorFormatter(env=Environment(colors=256, is_terminal=True))
    ColorFormatter(env=Environment(colors=False, is_terminal=True))



# Generated at 2022-06-13 21:57:22.639453
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter
    assert ColorFormatter()

# Generated at 2022-06-13 21:57:34.921125
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.compat import is_windows
    from httpie.context import Environment
    from httpie.plugins.builtin import HTTPieJSONLexer, HTTPieResponseLexer
    from httpie.plugins.colors import ColorFormatter

    env = Environment()
    env.colors = True
    env.style = 'solarized'

    # Use the plugin
    colors = ColorFormatter(env=env)

    # Format text bodies
    assert colors.format_body(body='abc', mime='text/plain') == 'abc'
    assert colors.format_body(body='abc', mime='text/html') == 'abc'
    assert colors.format_body(body='{"foo":"bar"}', mime='text/plain') == '{\n  "foo": "bar"\n}'

    # If there is no

# Generated at 2022-06-13 21:57:47.510719
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from .config import Config, ConfigParser
    from .utils import OSEnv
    from .context import Environment
    from .streams.writers import BaseWriter
    from httpie.input import ParseError
    from io import StringIO

    import sys

    config = Config()

    # Use constructors with default parameters
    config_parser = ConfigParser(env=OSEnv(),
                                 config=config)

    input_stream = StringIO()
    output_stream = StringIO()
    error_stream = StringIO()


# Generated at 2022-06-13 21:58:01.872823
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.plugins.colors import ColorFormatter
    import pygments.styles
    import pygments.styles.solarized
    color_formatter = ColorFormatter(None)
    style_class = color_formatter.get_style_class("solarized")
    assert style_class == pygments.styles.solarized.Solarized256Style
    style_class = color_formatter.get_style_class("solarized256")
    assert style_class == pygments.styles.solarized256.Solarized256Style
    style_class = color_formatter.get_style_class("solarized")
    assert style_class == pygments.styles.solarized.Solarized256Style
    style_class = color_formatter.get_style_class("solarized256")
    assert style_class == py

# Generated at 2022-06-13 21:58:14.337067
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.plugins.colors import ColorFormatter
    colorFormatter = ColorFormatter(None, False)

    input_data = "HTTP/1.1 200 OK\r\nContent-Length: 14\r\nContent-Type: application/json\r\n\r\n"
    expected_data = "\x1b[36mHTTP/1.1 200 OK\x1b[0m\r\nContent-Length: \x1b[33m14\x1b[0m\r\nContent-Type: \x1b[33mapplication/json\x1b[0m\r\n\r\n"
    actual_data = colorFormatter.format_headers(input_data)
    assert actual_data == expected_data

# Generated at 2022-06-13 21:58:24.450022
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import unittest.mock
    env = unittest.mock.MagicMock()
    env.colors = False
    env.colors = True
    c = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert c.format_body('', 'text/html') == ''
    assert c.format_body('\n', 'text/html') == ''
    assert c.format_body('\r\n', 'text/html') == ''
    assert c.format_body('bla', 'text/html') == 'bla'
    assert c.format_body('bla', 'bla') == 'bla'
    assert c.format_body('bla', 'application/javascript') == 'bla'

# Generated at 2022-06-13 21:58:36.406040
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.plugins.colors import ColorFormatter
    assert ColorFormatter.get_style_class('solarized256') == Solarized256Style
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style
    assert ColorFormatter.get_style_class('fruity') == pygments.styles.get_style_by_name('fruity')
    assert ColorFormatter.get_style_class('default') == AutoStyle
    assert ColorFormatter.get_style_class('auto') == AutoStyle
    from httpie.compat import is_windows
    if not is_windows:
        assert ColorFormatter.get_style_class('monokai') == pygments.styles.get_style_by_name('monokai')

# Generated at 2022-06-13 21:58:42.894403
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    cf = ColorFormatter(Environment())
    assert "HTTP" == cf.get_lexer_for_body('text/plain', 'Foo: bar')
    assert "JSON" == cf.get_lexer_for_body('application/json', '{}')
    assert "JSON" == cf.get_lexer_for_body('text/html', '{}')
    assert "JSON" == cf.get_lexer_for_body('foo/bar', '{}')

# Generated at 2022-06-13 21:58:50.178409
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    env = Environment()
    env.colors = False
    formatter = ColorFormatter(env)
    assert(formatter.get_style_class('fruity') is pygments.styles.get_style_by_name('fruity'))

    env.colors = 256
    formatter = ColorFormatter(env)
    assert(formatter.get_style_class('solarized') is Solarized256Style)


# Generated at 2022-06-13 21:59:03.580196
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    def get_tokens(string):
        lexer = SimplifiedHTTPLexer()
        return lexer.get_tokens(string)

    def assert_tokens(string, expected):
        actual = list(get_tokens(string))
        assert actual == expected

    # General format
    assert_tokens(
        "FOO: bar",
        [
            (pygments.token.Name.Attribute, 'FOO'),
            (pygments.token.Text, ' ' * 3),
            (pygments.token.Operator, ':'),
            (pygments.token.Text, ' ' * 3),
            (pygments.token.String, 'bar'),
            (pygments.token.Text, '\n')
        ]
    )

    # Request-Line
    assert_tok

# Generated at 2022-06-13 21:59:31.162355
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.plugins.builtin import HTTPHeadersFormat

    env = Environment(colors=256)

    cf = ColorFormatter(env=env)

    lines = [
            b'GET /get HTTP/1.1',
            b'Accept: */*',
            b'Accept-Encoding: gzip, deflate',
            b'Connection: keep-alive',
    ]

    hf = HTTPHeadersFormat()

    headers = hf.format(lines)

    print (cf.format_headers(headers))



# Generated at 2022-06-13 21:59:42.886523
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    def assert_formatting(body, mime, lexer_class=None, explicit_json=False):
        body_bytes = body.encode('utf8')
        try:
            json.loads(body)
        except (ValueError, TypeError):
            json_lexer = False
        else:
            json_lexer = True
        formatter = ColorFormatter(Environment())
        assert formatter.format_body(body_bytes, mime) == (
            body_bytes if lexer_class is None else body_bytes.decode('utf8')
        )
        assert formatter.format_body(body_bytes, mime, explicit_json=True) == (
            body_bytes if (lexer_class is None or not json_lexer) else body_bytes.decode('utf8')
        )


# Generated at 2022-06-13 21:59:49.684452
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=8)
    cf = ColorFormatter(env)
    headers = """
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Vary: X-Origin
Vary: Referer
Content-Encoding: gzip
Date: Fri, 23 Mar 2018 20:39:27 GMT
Server: ESF
Cache-Control: private
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Alt-Svc: quic=":443"; ma=2592000; v="44,43,39,35"
Accept-Ranges: none
Vary: Origin,Accept-Encoding
Transfer-Encoding: chunked

"""

# Generated at 2022-06-13 21:59:52.141828
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style

# Generated at 2022-06-13 22:00:00.342242
# Unit test for function get_lexer
def test_get_lexer():
    # Check that we can get the right lexer for HTTP headers.
    assert get_lexer('text/plain') == SimplifiedHTTPLexer
    assert get_lexer('text/x-http') == SimplifiedHTTPLexer
    assert get_lexer('message/http') == SimplifiedHTTPLexer
    assert get_lexer('message/x-http') == SimplifiedHTTPLexer

    # Make sure we get the right lexer for a text body.
    assert get_lexer('text/plain', '') == SimplifiedHTTPLexer

    # Check that we get the right lexer for a JSON body.
    assert get_lexer('text/plain', '{}') is not None
    assert get_lexer('text/plain', '{}') != SimplifiedHTTPLexer

    #

# Generated at 2022-06-13 22:00:09.317794
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(Environment(colors=256))

# Generated at 2022-06-13 22:00:11.149307
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style

# Generated at 2022-06-13 22:00:16.934947
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env=Environment(colors=256, styles=False)
    explicit_json=False
    color_scheme=DEFAULT_STYLE
    formatter = ColorFormatter(env=env,explicit_json=explicit_json,color_scheme=color_scheme)
    assert formatter.enabled==True
    assert formatter.explicit_json == False
    assert formatter.group_name == 'colors'
    assert type(formatter.http_lexer) is SimplifiedHTTPLexer
    assert type(formatter.formatter) is Terminal256Formatter

# Generated at 2022-06-13 22:00:19.096663
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    test_color_formatter = ColorFormatter(httpie.context.Environment())

# Generated at 2022-06-13 22:00:30.594265
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # Make sure the results for get_lexer_for_body are in sync with get_lexer
    from httpie.plugins.builtin import JSONStreams

    c = ColorFormatter(Environment())

    assert c.get_lexer_for_body("xyz/unknown") is None
    assert c.get_lexer_for_body("application/json") == pygments.lexers.get_lexer_by_name("json")
    assert c.get_lexer_for_body("application/json+json") == pygments.lexers.get_lexer_by_name("json")

    # --json flag should make sure JSON lexer is used
    lexer = c.get_lexer_for_body("application/unknown", explicit_json=True, body="{}")