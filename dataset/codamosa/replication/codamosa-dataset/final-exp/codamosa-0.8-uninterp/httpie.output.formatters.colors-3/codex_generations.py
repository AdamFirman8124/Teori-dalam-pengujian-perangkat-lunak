

# Generated at 2022-06-13 21:51:32.527471
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    data = {
        'mime': 'application/json',
        'body': '{}',
        'expected': '\x1b[01;33m{\x1b[0m\n\x1b[01;33m}\x1b[0m\n'
    }

    env = Environment(True, 256)
    cf = ColorFormatter(env, color_scheme='solarized')

    assert cf.format_body(data['body'], data['mime']) == data['expected']

# Generated at 2022-06-13 21:51:40.356378
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    code = '''\
POST /post HTTP/1.1
Host: httpbin.org
Accept-Encoding: gzip, deflate, compress
Accept: */*
User-Agent: HTTPie/0.9.2
Content-Length: 12
Content-Type: application/json

{"hello": "world"}
'''.encode('utf-8')
    lexer = SimplifiedHTTPLexer()
    formatter = Terminal256Formatter(style=Solarized256Style)
    result = pygments.highlight(
        code=code,
        lexer=lexer,
        formatter=formatter,
    )

# Generated at 2022-06-13 21:51:43.624999
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    """Unit test for constructor of class SimplifiedHTTPLexer.
    """
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']
    assert lexer.tokens



# Generated at 2022-06-13 21:51:53.290484
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    class TestPlugin(ColorFormatter):
        def format_headers(self, headers: str) -> str:
            return "".join([
                "headers are:\n",
                super().format_headers(headers)
            ])

    x = TestPlugin(env=None)

# Generated at 2022-06-13 21:51:57.694468
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter(Environment(colors=256, is_terminal=True))
    body = 'body'
    mime = 'text/html'
    assert formatter.format_body(body, mime) == body

# Generated at 2022-06-13 21:52:05.870812
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    lexer_short_description = lexer.short_description()
    assert lexer_short_description == 'HTTP'

    lexer_aliases = lexer.aliases
    assert lexer_aliases == ['http']

    lexer_filenames = lexer.filenames
    assert lexer_filenames == ['*.http']

    lexer_tokens = lexer.tokens
    assert 'root' in lexer_tokens

# Generated at 2022-06-13 21:52:10.043522
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('default') is pygments.styles.get_style_by_name('default')

# Generated at 2022-06-13 21:52:18.096266
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment()
    env.colors = True
    color_formatter = ColorFormatter(env)
    headers = "GET /files/test.txt HTTP/1.1\nHeader: value\nAnother-Header: another value    "
    assert "GET /files/test.txt HTTP/1.1\nHeader: value\nAnother-Header: another value" == color_formatter.format_headers(headers)

# Generated at 2022-06-13 21:52:21.532213
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style_class = ColorFormatter.get_style_class(
        DEFAULT_STYLE
    )
    assert style_class.__name__ == 'Solarized256Style'

# Generated at 2022-06-13 21:52:28.818431
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    import re

# Generated at 2022-06-13 21:52:47.101889
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.plugins.builtin import JSONFormatterPlugin

    class MockEnvironment:

        class MockConfig:
            def __init__(self):
                self.colors = 16
                self.style = DEFAULT_STYLE
                self.unicode_output = True

        def __init__(self):
            self.config = self.MockConfig()

    environment = MockEnvironment()
    color_formatter = ColorFormatter(env=environment)
    body = '{"key":"value"}'

    # Run some test cases and see if the result is as expected.
    assert color_formatter.format_body(body, 'application/json') == body
    assert color_formatter.format_body(body, 'text/html') == body

# Generated at 2022-06-13 21:52:59.956470
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(colors=256)
    colorFormatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    # Assert the use of Terminal256Formatter()
    assert(isinstance(colorFormatter.formatter, Terminal256Formatter))
    # Assert the use of SimplifiedHTTPLexer()
    assert(isinstance(colorFormatter.http_lexer, SimplifiedHTTPLexer))
    # Assert that the get_lexer_for_body() function returns correct value for the 
    # mime type 'application/json' and json body.
    assert(isinstance(colorFormatter.get_lexer_for_body('application/json', '{"a":"b"}'), pygments.lexers.jvm.JavascriptLexer))
    # Ass

# Generated at 2022-06-13 21:53:10.425553
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    import pathlib
    import os

    formatter = ColorFormatter(Environment(colors=256, is_windows=False,
                                           stdout_isatty=True))
    path = pathlib.Path(os.path.dirname(__file__))
    css_path = path / 'resources/style.css'
    css_file = css_path.open("r").read()
    assert str(get_lexer("text/css", False, css_file)) == "<class 'pygments.lexers.css.CssLexer'>"
    html_path = path / 'resources/index.html'
    html_file = html_path.open("r").read()

# Generated at 2022-06-13 21:53:18.428020
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class ColorsFormatter(ColorFormatter):
        def get_lexer_for_body(mime, body):
            return None

    result = ColorsFormatter().format_body("[{\"a\":\"b\"}]", 'application/json')
    assert result.strip() == "[{\"a\":\"b\"}]"

    result = ColorsFormatter().format_body("<html><body>1</body></html>", 'text/html')
    assert result.strip() == "<html><body>1</body></html>"

    result = ColorsFormatter().format_body("", 'text/plain')
    assert result.strip() == ""

# Generated at 2022-06-13 21:53:20.255783
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert True


# Generated at 2022-06-13 21:53:33.230367
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import pytest
    from httpie import ExitStatus
    from utils import http, HTTP_OK
    
    env = Environment()

    r = http('GET', HTTP_OK, env=env, color_scheme=SOLARIZED_STYLE)
    assert HTTP_OK in r
    assert r.exit_status == ExitStatus.OK
    assert 'HTTP/1.1 200 OK' in r

    r = http('POST', HTTP_OK, 'test', 'test', env=env)
    assert HTTP_OK in r
    assert r.exit_status == ExitStatus.OK
    assert 'Content-Length: 4' in r
    assert 'Content-Type: text/plain' in r

    r = http('GET', HTTP_OK, 'test', 'test', env=env)
    assert HTTP_OK in r

# Generated at 2022-06-13 21:53:48.033395
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.compat import urlparse

    env = Environment(colors=256)
    formatter = ColorFormatter(env)

    # HTML
    assert formatter.get_lexer_for_body(
        'text/html',
        '<html><head><title>Test</title></head><body>Test</body></html>'
    ) == pygments.lexers.get_lexer_by_name('html')

    # JSON
    assert formatter.get_lexer_for_body(
        'application/json',
        '{"k1": "v1"}'
    ) == pygments.lexers.get_lexer_by_name('json')

    # JSON with incorrect Content-Type

# Generated at 2022-06-13 21:53:51.203758
# Unit test for function get_lexer
def test_get_lexer():
    lexer = get_lexer('text/html')
    assert lexer is not None
    lexer = get_lexer('image/png')
    assert lexer is None

# Generated at 2022-06-13 21:53:58.040937
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment
    env = Environment(colors=256)
    formatter = ColorFormatter(env, color_scheme='solarized')

    json_data = '{"name": "John Doe", "age": 26}'
    assert formatter.format_body(json_data, 'application/json') == json_data
    assert formatter.format_body(json_data, 'application/json; charset=UTF-8') == json_data

# Generated at 2022-06-13 21:54:02.320641
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    env = Environment()
    blacklist = ['/Users/gwang/httpie/tests', '/Users/gwang/httpie/httpie']
    env.config['colors.format'] = '256'
    env.config['colors.style'] = 'solarized'
    color_formatter = ColorFormatter(env, False)
    print(color_formatter.format_body('{"name": "gwang"}', 'application/json'))

# Generated at 2022-06-13 21:54:14.464463
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(colors=256)
    formatter = ColorFormatter(env, color_scheme=SOLARIZED_STYLE)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.formatter.style == Solarized256Style
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)

# Generated at 2022-06-13 21:54:18.791061
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    class SimplifiedHttpLexer(pygments.lexer.RegexLexer):
        name = 'SimplifiedHTTPLexer'
        tokens = {}

    assert SimplifiedHttpLexer.name == 'SimplifiedHTTPLexer'
    assert SimplifiedHttpLexer.tokens == {}



# Generated at 2022-06-13 21:54:29.699917
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    tokens = SimplifiedHTTPLexer().get_tokens_unprocessed(u'X-API-Token: abc')
    assert tokens.__next__() == (pygments.token.Name.Attribute, u'X-API-Token')
    assert tokens.__next__() == (pygments.token.Text, u'')
    assert tokens.__next__() == (pygments.token.Operator, u':')
    assert tokens.__next__() == (pygments.token.Text, u' ')
    assert tokens.__next__() == (pygments.token.String, u'abc')

# Generated at 2022-06-13 21:54:41.225568
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.compat import is_windows
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    import pygments.lexers
    import pygments.styles


# Generated at 2022-06-13 21:54:56.779540
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=256)

# Generated at 2022-06-13 21:55:04.403786
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import io

    headers = """\
HTTP/1.1 404 Not Found
Date: Sun, 18 Oct 2015 00:50:01 GMT
Server: Apache
Vary: Accept-Encoding
Content-Length: 301
Connection: close
Content-Type: text/html; charset=iso-8859-1
"""
    env = Environment(
        stdin=io.StringIO(),
        stdout=io.StringIO(),
        stderr=io.StringIO(),
        colors=256
    )
    formatter = ColorFormatter(env, arg_parser=None)
    # result = formatter.format_headers(headers)
    assert len(headers) > 10

# Generated at 2022-06-13 21:55:13.449375
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    clr = ColorFormatter(Environment()) 
    
    # default case
    headers = "GET / HTTP/1.1\r\nHost: localhost:3000\r\nUser-Agent: httpie/0.9.9\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nConnection: keep-alive"
    headers_highlighted = clr.format_headers(headers)
    assert headers_highlighted == "\x1b[38;5;244mGET / HTTP/1.1\x1b[0m\r\nHost: localhost:3000\r\nUser-Agent: httpie/0.9.9\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nConnection: keep-alive"

# Generated at 2022-06-13 21:55:17.217957
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.colors import ColorFormatter
    assert ColorFormatter.get_style_class('fruity').__name__ == 'FruityStyle', (
        'Unexpected style class name')

# Generated at 2022-06-13 21:55:18.007122
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert True

# Generated at 2022-06-13 21:55:21.443300
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = {'colors': True}
    cf = ColorFormatter(env)
    assert cf.formatter.style._styles["Name.Attribute"] == "#b58900", "Solarized256Style output should be #b58900"

# Generated at 2022-06-13 21:55:34.404255
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.output.colors import ColorFormatter
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:55:42.202723
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class FauxEnvironment(object):
        def __init__(self, colors):
            self.colors = colors

    env = FauxEnvironment(256)
    formatter = ColorFormatter(env, color_scheme=SOLARIZED_STYLE)
    assert formatter.get_style_class(SOLARIZED_STYLE) is Solarized256Style

    env = FauxEnvironment(8)
    formatter = ColorFormatter(env, color_scheme=SOLARIZED_STYLE)
    assert formatter.get_style_class(SOLARIZED_STYLE) is not Solarized256Style

# Generated at 2022-06-13 21:55:44.745947
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE)\
           is Solarized256Style

# Generated at 2022-06-13 21:55:48.638252
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class("solarized256") == Solarized256Style
    assert ColorFormatter.get_style_class("solarized256") != Terminal256Formatter

# Generated at 2022-06-13 21:55:59.598042
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import io
    import httpie.input as input
    import httpie.core as core
    import httpie.output as output
    import httpie.cli.argtypes as argtypes
    from httpie.output.streams import StdoutBytesIO

    args = input.ParseResult()
    args.method = 'GET'
    args.headers = []
    args.headers = [
        'Accept: text/html',
        'Content-Type: application/json',
        'User-Agent: HTTPie'
    ]
    args.auth = None
    args.auth_type = 'basic'
    args.username = None
    args.password = None
    args.verify = True
    args.verify_all = argtypes.verify_true
    args.ssl = None
    args.style = None

# Generated at 2022-06-13 21:56:01.206918
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter = ColorFormatter(Environment(), False, DEFAULT_STYLE)

# Generated at 2022-06-13 21:56:11.848462
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class_solarized = ColorFormatter.get_style_class(SOLARIZED_STYLE)
    class_solarized256 = ColorFormatter.get_style_class('solarized256')
    assert class_solarized == class_solarized256

    class_monokai256 = ColorFormatter.get_style_class('monokai256')
    class_monokai = pygments.styles.get_style_by_name('monokai')
    assert class_monokai256 == class_monokai

# Generated at 2022-06-13 21:56:12.515732
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    pass

# Generated at 2022-06-13 21:56:20.041204
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style
    assert ColorFormatter.get_style_class('solarized256') == Solarized256Style
    assert ColorFormatter.get_style_class('Auto') == Solarized256Style
    assert ColorFormatter.get_style_class('auto') == Solarized256Style
    assert ColorFormatter.get_style_class('fruity') == pygments.styles.get_style_by_name('fruity')

# Generated at 2022-06-13 21:56:31.337994
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    # Arrange
    from httpie import ExitStatus
    from httpie.compat import StringIO
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from tests.data import (
        BIN_FILE_PATH,
        BIN_FILE_CONTENT,
        BIN_FILE_PATH_ARG,
        FILE_PATH_ARG,
        FILE_PATH,
        JSON_FILE_PATH_ARG,
        JSON_FILE_PATH,
        JSON_FILE_CONTENT,
        JSON_FILE_LINES
    )

    environment = Environment()
    stdout = StringIO()
    stderr = StringIO()
    color_formatter = ColorFormatter(env=environment)


# Generated at 2022-06-13 21:57:01.496520
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    def get_lexer_for_body(self, mime: str, body: str) -> Optional[Type[Lexer]]:
        return get_lexer(
            mime=mime,
            explicit_json=self.explicit_json,
            body=body,
        )
    ColorFormatter.get_lexer_for_body = get_lexer_for_body

    def format_body(self, body: str, mime: str) -> str:
        lexer = self.get_lexer_for_body(mime, body)
        if lexer:
            body = pygments.highlight(
                code=body,
                lexer=lexer,
                formatter=self.formatter,
            )
        return body
    ColorFormatter.format_body = format_body

    # Body with

# Generated at 2022-06-13 21:57:10.358784
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    env = Environment(application_name=None, colors=False)
    cf = ColorFormatter(env=env)

    # Test different mime/web extensions
    mime = 'text/plain'
    assert type(cf.get_lexer_for_body(mime, '')) == pygments.lexers.TextLexer

    mime = 'application/json'
    assert type(cf.get_lexer_for_body(mime, '')) == pygments.lexers.JsonLexer

    mime = 'audio/flac'
    assert type(cf.get_lexer_for_body(mime, '')) == pygments.lexers.AudioLexer

    mime = 'video/mpeg'
    assert type(cf.get_lexer_for_body(mime, '')) == pygments.lexers

# Generated at 2022-06-13 21:57:23.218909
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie import ExitStatus
    from httpie.compat import str
    from httpie.core import main
    from httpie.context import Environment
    import httpie.plugins
    env = Environment()
    stdin_isatty = True
    stdout_isatty = True
    style = 'solarized'
    color_formatter = ColorFormatter(env, stdin_isatty,
                                     stdout_isatty, style)

    def http(*args, **kwargs):
        """
        http(method, url, data=None, stdin_isatty=stdin_isatty,
             stdout_isatty=stdout_isatty, style=style, env=env)
        """
        kwargs.setdefault('stdin_isatty', stdin_isatty)

# Generated at 2022-06-13 21:57:25.945002
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    print(lexer)


test_SimplifiedHTTPLexer()

# Generated at 2022-06-13 21:57:37.989807
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.input import ParseError

    # Test with content type text/plain
    text = "This is a plain text"
    assert ColorFormatter(Environment()).format_body(text, "text/plain") == text

    # Test with content type application/json
    json_text = '{"key": "value"}'
    assert ColorFormatter(Environment(), explicit_json=True).format_body(json_text, "application/json") == json_text
    assert ColorFormatter(Environment(), explicit_json=False).format_body(json_text, "application/json") == json_text

    # Test with content type text/html
    html_text = 'HTML'
    assert ColorFormatter(Environment()).format_body(html_text, "text/html") == html_text

    # Test with content type application/x-

# Generated at 2022-06-13 21:57:45.035798
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    class SampleEnvironment(Environment):
        def __init__(self, colors: int=0, **kwargs):
            super().__init__(**kwargs)
            self.colors = colors

    env = SampleEnvironment()
    formatter = ColorFormatter(env)
    if not formatter.enabled:
        return
    formatter.format_headers(
        """
        POST /api/status HTTP/1.1
        Content-Type: application/json
        Content-Length: 10
        """
    )

# Generated at 2022-06-13 21:57:52.579332
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import httpie
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    from httpie.compat import is_windows, isatty
    from httpie.plugins.colors import ColorFormatter

    class MockArgs(object):
        traceback = False
        verbose = False
        debug = False
        color = 'auto'
        style = 'auto'
        pretty = True
        formatter = 'colors'
        headers = True
        body = True

    env = Environment()
    args = MockArgs()

    formatter = ColorFormatter(env, args)
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: texte/test'
    body = '{"attribute": "value"}'
    mime = 'application/json'

    # Check if body has been changed

# Generated at 2022-06-13 21:57:54.756625
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:58:01.748865
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(DEFAULT_STYLE) == Solarized256Style
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style
    assert ColorFormatter.get_style_class(AUTO_STYLE) == Solarized256Style
    assert ColorFormatter.get_style_class('none') == None


# Generated at 2022-06-13 21:58:14.686401
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.input import ParseError

    class DummyLexer(pygments.lexer.RegexLexer):
        pass

    class DummyFormatter(pygments.formatter.Formatter):
        def format(self, tokensource, outfile):
            outfile.write('formatted')

    class DummyTerminal(object):
        def __init__(self, *args):
            pass

        def write(self, *args):
            pass

        def read(self, *args):
            pass

    formatter = ColorFormatter(
        env=Environment(colors=256),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE
    )
    assert formatter.get_lexer_for_body(
        mime='text/html',
        body=''
    )

# Generated at 2022-06-13 21:58:42.894555
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.compat import is_windows
    from httpie.output import BINARY_SUPPRESSED_NOTICE

    cr = '\r\n'
    env = Environment(colors=256, stdin_isatty=True, stdout_isatty=True)

    # Binary output should not be formatted even with --print==B or --stream
    formatter = ColorFormatter(env=env,
                               explicit_json=True,
                               color_scheme='auto')

    c = formatter.format_headers(
        ('HTTP/1.1 200 OK' + cr +
         'Content-Type: application/octet-stream' + cr + cr +
         BINARY_SUPPRESSED_NOTICE))

# Generated at 2022-06-13 21:58:53.410951
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.compat import is_windows
    if is_windows:
        return

    from httpie.context import Environment
    e = Environment()
    e.colors = False
    e.options.color_scheme = 'fruity'
    p = ColorFormatter(e)
    headers = '`Content-Type: application/json\nServer: nginx\n' \
              'Connection: keep-alive\n\n`'
    expected = '\x1b[35m`\x1b[35m`Content-Type\x1b[0m: \x1b[36m`\x1b[36m' \
               '`application/json\x1b[35m`\x1b[35m`\n\x1b[35m`\x1b[35m`'

# Generated at 2022-06-13 21:59:05.816347
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # create formatter
    formatter = ColorFormatter(Environment(), False, "solarized")
    # test http response body
    response_body = """
<html>
  <head>
    <title>Example Domain</title>
    <link rel="stylesheet" href="/stylesheets/style.css" />
  </head>
  <body>
    <div class="page">
      <h1>Example Domain</h1>
      <p>This domain is established to be used for illustrative examples in documents. You may use this
      domain in examples without prior coordination or asking for permission.</p>
      <p><a href="http://www.iana.org/domains/example">More information...</a></p>
    </div>
  </body>
</html>
"""
    # test get_lexer_for

# Generated at 2022-06-13 21:59:17.479827
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env_args = {'format': None, 'colors': 256, 'style': 'solarized'}

    cf = ColorFormatter(Environment(**env_args), explicit_json=False, color_scheme='solarized')

    assert cf.enabled == True
    assert cf.formatter.__class__.__name__ == 'Terminal256Formatter'
    assert cf.http_lexer.__class__.__name__ == 'SimplifiedHTTPLexer'
    assert cf.explicit_json == False
    assert cf.group_name == 'colors'

    assert pygments.formatters.terminal.TerminalFormatter is not Terminal256Formatter
    assert pygments.lexers.special.TextLexer is not SimplifiedHTTPLexer
    assert pygments.styles.get_style_by_name

# Generated at 2022-06-13 21:59:19.081462
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer is not None



# Generated at 2022-06-13 21:59:21.809131
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    formatter = ColorFormatter(None, color_scheme="solarized")
    assert formatter.get_style_class("solarized") == Solarized256Style

# Generated at 2022-06-13 21:59:29.182669
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    import unittest
    import sys

    class TestSimplifiedHTTPLexer(unittest.TestCase):
        def test_request_line(self):
            correct = '<Keyword.Reserved>HTTP<Operator>/<Number>1.1<Text>'\
                      '<Name.Function>GET<Text><Name.Namespace>'\
                      '/<Text><Keyword.Reserved>HTTP<Operator>/<Number>1.1'
            lexer = SimplifiedHTTPLexer()
            tokens = list(lexer.get_tokens('GET / HTTP/1.1'))
            self.assertEquals(len(tokens), 7)
            self.assertEquals(str(tokens[0]), correct)


# Generated at 2022-06-13 21:59:41.473545
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import sys
    env = Environment(colors=256, stdout=sys.stdout)

    # Test with color scheme set to auto, but coloring is not enabled
    cf = ColorFormatter(env, color_scheme='auto')
    cf.enabled = False
    headers = '''GET / HTTP/1.1
Host: localhost:8000
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
User-Agent: HTTPie/0.9.2

'''
    expected_result = '''GET / HTTP/1.1
Host: localhost:8000
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
User-Agent: HTTPie/0.9.2

'''
    assert cf.format_headers(headers) == expected_result

# Generated at 2022-06-13 21:59:57.748436
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    env = Environment()
    env.stdout_isatty = True
    env.colors = 256

    class FakeResponse:
        def __init__(self, content_type='', body=''):
            self.content_type = content_type
            self.body = body

    format = ColorFormatter(env)
    assert format is not None

    # Test content_type is text/html
    response = FakeResponse(content_type='text/html', body='<html></html>')
    ret = format.format_body(response.body, response.content_type)
    assert ret == '\x1b[38;5;31m<html></html>\x1b[0m'

    # Test content_type is text/html with body is <html>, the formatter should format <html>
    response = FakeResponse

# Generated at 2022-06-13 22:00:08.357514
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    '''
    测试 ColorFormatter.format_headers 方法
    :return:
    '''
    headers = "HTTP/1.1 200 OK\n" \
              "Accept: */*\n" \
              "Connection: keep-alive\n" \
              "Content-Length: 555\n" \
              "Content-Type: application/json; charset=utf-8\n" \
              "Date: Thu, 09 Jan 2020 06:54:41 GMT\n" \
              "Vary: Accept-Encoding\n" \
              "X-Powered-By: Express\n\n"
    # 验证颜色设置
    env = Environment(colors=256, style='')
    color_formatter = ColorFormatter

# Generated at 2022-06-13 22:00:48.171588
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    color_formatter = ColorFormatter(None, explicit_json=False, color_scheme=SOLARIZED_STYLE)
    style = color_formatter.get_style_class(SOLARIZED_STYLE)
    assert style == Solarized256Style

# Generated at 2022-06-13 22:00:54.355113
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    env = Environment()
    env.colors = 256
    formatter = ColorFormatter(env)
    assert formatter.get_lexer_for_body('application/json','{"a":1}')

    formatter.explicit_json = True
    assert formatter.get_lexer_for_body('application/json','{"a":1}')

    assert not formatter.get_lexer_for_body('application/json','')

    assert formatter.get_lexer_for_body('application/json','not a json')

# Generated at 2022-06-13 22:01:07.868848
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=256)
    f = ColorFormatter(env)
    out = f.format_headers('GET / HTTP/1.1\r\nHost: example.com')