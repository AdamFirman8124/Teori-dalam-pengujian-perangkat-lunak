

# Generated at 2022-06-13 21:51:38.704680
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment()
    formatter = ColorFormatter(env)
    headers = ('GET / HTTP/1.1\r\n'
               'Content-Type: application/json\r\n'
               'Host: www.example.org\r\n'
               'User-Agent: HTTPie Example\r\n'
               '\r\n')

# Generated at 2022-06-13 21:51:44.761943
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter = ColorFormatter(
        env=Environment(colors=256),
        color_scheme=SOLARIZED_STYLE
    )
    assert formatter.formatter.__class__.__name__ == 'Terminal256Formatter'
    assert formatter.formatter.style.__class__.__name__ == 'Solarized256Style'

# Generated at 2022-06-13 21:51:48.122627
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) is Solarized256Style
    assert ColorFormatter.get_style_class('emacs') is pygments.styles.EmacsStyle



# Generated at 2022-06-13 21:51:51.438452
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    formatter = ColorFormatter(env=env)
    assert formatter.enabled
    assert formatter.explicit_json == False
    assert formatter.color_scheme == DEFAULT_STYLE

# Generated at 2022-06-13 21:51:52.019793
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    pass

# Generated at 2022-06-13 21:52:01.228443
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class MockEnvironment:
        def __init__(self, color_val):
            self.colors = color_val

    formatter = ColorFormatter(env=MockEnvironment(256))
    assert formatter.format_body(body='{"foo": 1}', mime="application/json") == "\x1b[38;5;22m{\x1b[39m\x1b[38;5;28m\"foo\"\x1b[39m\x1b[38;5;28m:\x1b[39m \x1b[38;5;81m1\x1b[39m\x1b[38;5;22m}\x1b[39m"

# Generated at 2022-06-13 21:52:05.866209
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    """Check if method get_style_class of class ColorFormatter is working as
    expected."""

    instance = ColorFormatter(None, foo='bar')

    assert instance.get_style_class('solarized') == Solarized256Style
    assert instance.get_style_class('fruity') == pygments.styles.fruity.FruityStyle

# Generated at 2022-06-13 21:52:20.830715
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import httpie.cli.style
    from httpie.output.streams import RAW_STDOUT
    from httpie.plugins.colors import ColorFormatter
    from httpie.compat import is_windows
    from httpie.context import Environment
    import sys
    import os
    import contextlib
    import io
    import unittest

    @contextlib.contextmanager
    def captured_output():
        new_out, new_err = io.StringIO(), io.StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err


# Generated at 2022-06-13 21:52:32.599788
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    color_formatter = ColorFormatter(None)
    # test null
    assert color_formatter.format_body('', '') == ''
    # test json format
    assert color_formatter.format_body('{"name": "Yohan"}', 'application/json') == '\x1b[90m{\x1b[39m\x1b[32m"name"\x1b[39m\x1b[90m:\x1b[39m \x1b[33m"Yohan"\x1b[39m\x1b[90m}\x1b[39m'

# Generated at 2022-06-13 21:52:39.454747
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('image/jpg') is None
    assert get_lexer('image/svg+xml') is not None
    assert get_lexer('text/html') is not None
    assert get_lexer('text/x-python') is not None

    assert get_lexer('text/html+xml', explicit_json=True) is not None
    assert get_lexer('text/html+xml', body='<html></html>',
                     explicit_json=True) is not None
    assert get_lexer('text/html+xml', body='{}', explicit_json=True) is not None
    assert get_lexer('text/html+xml', body='{', explicit_json=True) is None

    assert get_lexer('application/json', explicit_json=True) is not None
    assert get_

# Generated at 2022-06-13 21:52:59.317219
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    import pygments.lexer

    lexer = SimplifiedHTTPLexer()
    assert isinstance(lexer, pygments.lexer.RegexLexer)

    # POST /hello/world HTTP/1.1
    # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    # Host: example.com

    tokens = lexer.get_tokens(
        'POST /hello/world HTTP/1.1\r\n'
        'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
        'Host: example.com'
    )

# Generated at 2022-06-13 21:53:04.123303
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    content = '{"response":"OK"}'
    mime = 'application/json'
    formatter = ColorFormatter()
    formatted_body = formatter.format_body(body=content, mime=mime)
    assert formatted_body is not None

# Generated at 2022-06-13 21:53:08.623755
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('native') is pygments.styles.native
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style



# Generated at 2022-06-13 21:53:20.429107
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.client import Response

    def _format_headers_test(response: Response, expected_result: str):
        assert ColorFormatter.format_headers(response) == expected_result

    CRLF = '\r\n'

    _format_headers_test(
        Response(
            'HTTP/1.1 101 Switching Protocols',
            'Connection: upgrade',
            'Upgrade: websocket',
        ),
        '\x1b[38;5;8mHTTP/1.1 101 Switching Protocols\x1b[0m\r\n'
        'Connection: upgrade\r\n'
        '\x1b[38;5;8mUpgrade: websocket\x1b[0m\r\n'
    )


# Generated at 2022-06-13 21:53:33.291602
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.core import main
    from httpie.plugins import builtin
    from colorama import Fore, Style
    import requests

    color = builtin.get_plugin_manager().instantiate(main.Environment(), 'color')

# Generated at 2022-06-13 21:53:45.406206
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.compat import is_windows
    if not is_windows:
        body = ColorFormatter.format_body(body = '{ "a" : "b" }', mime = 'application/json')
        assert body == '\x1b[0;36m{ "a" : "b" }\x1b[0m'
        body = ColorFormatter.format_body(body='<html><body>Hello world.</body></html>', mime='text/html')
        assert body == '\x1b[0;96m<html><body>Hello world.</body></html>\x1b[0m'


# Generated at 2022-06-13 21:53:56.507751
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():

    # WARNING: test only pass on linux
    # On other systems, not tested

    # Create an instance of ColorFormatter
    env = Environment()
    formatter = ColorFormatter(env)

    # Test any text without encoding
    # Should return a lexer
    lexer = formatter.get_lexer_for_body(
        mime='text',
        body='text'
    )
    assert lexer != None

    # Test any JSON without encoding
    # Should return a lexer
    lexer = formatter.get_lexer_for_body(
        mime='application/json',
        body='json'
    )
    assert lexer != None

    # Test any text with encoding='UTF-8'
    # Should return a lexer

# Generated at 2022-06-13 21:54:05.141598
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.context import Environment
    env = Environment()
    from httpie.output.streams import BinaryBytesOutputStream
    output_stream = BinaryBytesOutputStream(env)
    from httpie.plugins.builtin import HTTPHeadersProcessor, HTTPBodyProcessor
    from httpie.output.streams import UnsupportedOutputStream
    headers_processor = HTTPHeadersProcessor()
    body_processor = HTTPBodyProcessor()
    color_formatter = ColorFormatter(env)
    body = "This is the body"
    mime = "text/html"

# Generated at 2022-06-13 21:54:11.425416
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    class TestFormatter(FormatterPlugin):
        def format_headers(self, headers: str) -> str:
            return super().format_headers(headers)

    formatter = TestFormatter()
    assert formatter.format_headers('Headers: Value\n') == 'Headers: Value\n'

# Generated at 2022-06-13 21:54:20.778542
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    f = ColorFormatter(env=Environment())
    assert f.format_body("<html>Hi</html>", "text/html") == "<html>Hi</html>"
    assert f.format_body("<html>Hi</html>", "application/json") is None
    assert f.format_body('""', "application/json") is '""'

    f = ColorFormatter(env=Environment(), explicit_json=True)
    assert f.format_body("<html>Hi</html>", "text/html") == "<html>Hi</html>"
    assert f.format_body("<html>Hi</html>", "application/json") is None
    assert f.format_body('""', "application/json") is '""'

# Generated at 2022-06-13 21:54:38.224618
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.plugins.colors import ColorFormatter
    from pygments.styles import get_style_by_name
    import platform
    import sys

    # Check if operating system is Windows
    if platform.system() == 'Windows':
        assert ColorFormatter.get_style_class('fruity') == get_style_by_name('fruity')
    else:
        assert ColorFormatter.get_style_class('monokai') == get_style_by_name('monokai')

# Generated at 2022-06-13 21:54:42.077283
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    source = "regular"
    mime = 'text/plain'
    assert ColorFormatter.format_body(source, mime) == source
    mime = 'application/json'
    assert ColorFormatter.format_body(source, mime) != source

# Generated at 2022-06-13 21:54:43.819252
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    SimplifiedHTTPLexer("HTTP")

# Generated at 2022-06-13 21:54:49.300719
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.core import main

    color_formatter = ColorFormatter(Environment())
    assert color_formatter.format_headers('') == '\n'

    color_formatter = ColorFormatter(Environment(colors=True))
    assert color_formatter.format_headers('') == '\n'



# Generated at 2022-06-13 21:55:00.643309
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(Environment(colors=256))
    lexer = formatter.get_lexer_for_body(
        mime='text/html',
        body="""<!DOCTYPE html>
        <html>
        <body>
        <h1>My First Heading</h1>
        <p>My first paragraph.</p>
        </body>
        </html>"""
    )
    assert 'Html' in str(lexer)



# Generated at 2022-06-13 21:55:08.724868
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from httpie.plugins import FormatterPlugin
    from httpie.colors import ColorFormatter
    import pygments.formatters
    import pygments.lexers.javascript
    import pygments.lexers.html
    import pygments.lexers.css
    env = Environment(colors=256)
    formatter = ColorFormatter(env)
    lexer = pygments.lexers.javascript.JavascriptLexer()
    assert(formatter.format_body(body='test', mime='application/json') == 'test')
    assert(formatter.format_body(body='test', mime='application/javascript') != 'test')

# Generated at 2022-06-13 21:55:15.350878
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    terminal_formater = TerminalFormatter()
    http_lexer = PygmentsHttpLexer()
    assert ColorFormatter().formatter == terminal_formater
    assert ColorFormatter().http_lexer == http_lexer
    assert ColorFormatter(explicit_json=False).explicit_json == False

# Generated at 2022-06-13 21:55:27.813498
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment

    class TestColorFormatter(ColorFormatter):
        def get_lexer_for_body(self, mime, body):
            return self.http_lexer  # Use HTTP lexer as a fallback

    # For each test case, the first item is a mock content type, and the
    # second item is a mock response body.
    test_cases = [
        ('application/json', '{"test": "example"}'),
        ('application/xml', '<?xml version="1.0" encoding="UTF-8"?>'),
        ('text/html', '<!DOCTYPE html>'),
        ('text/plain', 'some plain text'),
    ]

    env = Environment(
        colors=True,
        stdout_isatty=True,
    )

    # Test on a regular

# Generated at 2022-06-13 21:55:41.073998
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    import pytest

    from httpie.plugins import FormatterPlugin

    class TestColorFormatter(ColorFormatter):
        def __init__(self):
            super().__init__(env=Environment(), output_file=None)

    c = TestColorFormatter()
    assert (
        c.get_lexer_for_body(
            mime='text/html', body='<html></html>'
        ) == pygments.lexers.get_lexer_by_name('html')
    )

    assert (
        c.get_lexer_for_body(
            mime='foo/bar', body='<html></html>'
        ) == pygments.lexers.get_lexer_by_name('html')
    )


# Generated at 2022-06-13 21:55:55.220766
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class MockEnvironment:
        colors = True

    # Force the environment to report 256 colors
    # and use the same color scheme on all platforms
    formatter = ColorFormatter(env=MockEnvironment())
    assert formatter.formatter.__class__.__name__ == 'Terminal256Formatter'
    assert formatter.formatter.style.__class__.__name__ == 'Terminal256Style'
    assert formatter.formatter.style.background_color == '#000000'
    assert formatter.formatter.style.styles[pygments.token.String] == '#d70000'

    # Without 256 colors, the Solarized256Style is not used
    formatter = ColorFormatter(env=MockEnvironment(), color_scheme='solarized')

# Generated at 2022-06-13 21:56:23.952929
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.input import ParseError
    from .utils import TestEnvironment, http

    env = TestEnvironment(colors=256)
    http('--print=HB', env=env)
    http('--print=HB', '--json', env=env)

    # Correct mime type, and it's JSON:
    response = http('--print=HB', 'GET', '/', env=env)
    assert 'HTTP/1.1 200 OK' in response
    assert 'Content-Type: application/json' in response
    assert '\x1b[38;5;245m{\x1b[39m' not in response  # not colorized
    assert '{\n    "headers": {\n' in response  # JSON lexer

    # Wrong mime type, but it's actually JSON.
    # If this is text/plain, will

# Generated at 2022-06-13 21:56:30.313352
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from .helpers import http
    from . import __file__ as httpie_path
    env = Environment()
    env.color = True
    formatter = ColorFormatter(env=env)
    with open(httpie_path, 'r') as fd:
        body = fd.read()
        rst = formatter.format_body(body=body, mime='text/x-python')
    assert rst



# Generated at 2022-06-13 21:56:33.240132
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert isinstance(ColorFormatter.get_style_class(SOLARIZED_STYLE),Solarized256Style)

# Generated at 2022-06-13 21:56:44.281108
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style = ColorFormatter.get_style_class('tango')
    assert style.__name__ == 'TangoStyle', 'class TangoStyle not found'
    style = ColorFormatter.get_style_class('solarized')
    assert style.__name__ == 'SolarizedStyle', 'class SolarizedStyle not found'
    style = ColorFormatter.get_style_class('solarized256')
    assert style.__name__ == 'Solarized256Style', 'class Solarized256Style not found'
    try:
        ColorFormatter.get_style_class('invalid')
        assert False
    except ClassNotFound:
        assert True

# Generated at 2022-06-13 21:56:55.578265
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class get_style_calls(ColorFormatter):
        def __init__(self, *args):
            super().__init__(*args)
            self.called_with = []
        def get_style_class(self, *args):
            self.called_with.append(args)
            return super().get_style_class(*args)

    gsc = get_style_calls(Environment())
    assert gsc.called_with == []

    gsc.get_style_class("solarized")
    assert gsc.called_with == [("solarized",)]

# Generated at 2022-06-13 21:56:58.029845
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter = ColorFormatter(Environment(colors=256))
    assert color_formatter.formatter is not None

# Generated at 2022-06-13 21:57:07.773994
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import pygments as py
    style = "solarized"
    c = ColorFormatter(None, color_scheme=style)
    assert style in c.get_style_class(style).__name__
    assert c.formatter.__class__.__name__ in ['Terminal256Formatter', 'TerminalFormatter']
    assert isinstance(c.formatter.style, py.styles.get_style_by_name(style))
    style = "monokai"
    c = ColorFormatter(None, color_scheme=style)
    assert style in c.get_style_class(style).__name__
    assert c.formatter.__class__.__name__ in ['Terminal256Formatter', 'TerminalFormatter']

# Generated at 2022-06-13 21:57:14.504083
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from pygments import highlight
    from pygments.lexers import HttpLexer
    from pygments.lexers import HttpRequestLexer
    from pygments.lexers import HttpResponseLexer
    from pygments.lexers import HttpLexer as PygmentsHttpLexer
    from pygments.lexers import JsonLexer
    from pygments.lexers import JavascriptLexer
    from pygments.lexers import XmlLexer
    from pygments.lexers import XmlDjangoLexer
    from pygments.lexers import XmlHtmlLexer
    from pygments.lexers import XmlRssLexer
    from pygments.lexers import XmlRstLexer
    from pygments.formatters import Terminal256Formatter
    
    env = Environment(colors=256)
    formatter = ColorFormatter

# Generated at 2022-06-13 21:57:15.244366
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    pass

# Generated at 2022-06-13 21:57:19.995769
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # pylint: disable=unused-variable
    env = None
    explicit_json = False
    color_scheme = None
    formatter = ColorFormatter(env, explicit_json, color_scheme)
    pass

# Generated at 2022-06-13 21:58:12.179482
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    from httpie.compat import is_windows
    import json
    try:
        json.loads('{foo: bar')
    except ValueError as e:
        assert e.args == ('Expecting property name enclosed in double quotes: '
                   'line 1 column 2 (char 1)',)
    c = ColorFormatter(Environment(colors=256, debug=True), explicit_json=False, color_scheme=DEFAULT_STYLE)
    lexer = c.get_lexer_for_body('application/json', '{foo: bar')
    assert lexer == None
    lexer = c.get_lexer_for_body('application/json', '{foo: bar', explicit_json=True)

# Generated at 2022-06-13 21:58:21.165824
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    from httpie.utils import MimeType

    import requests
    r = requests.get("https://api.github.com/users/weeb-test")

    formatter_plugin = FormatterPlugin()
    c = ColorFormatter(Environment, explicit_json=False, formatter=formatter_plugin)
    c.format_body(r.text, MimeType.get_type(r.text, r.headers['Content-Type']))
    assert (r.text is not None)

# Generated at 2022-06-13 21:58:25.581623
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter('test')
    assert formatter.get_lexer_for_body('application/json', '{}') is not None
    assert formatter.get_lexer_for_body('application/json', '{}') is not None



# Generated at 2022-06-13 21:58:37.475517
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.output.colors import ColorFormatter
    for target_mime in (
        'application/json', 'application/problem+json', 'application/hal+json',
        'application/vnd.api+json'
    ):
        assert ColorFormatter.get_lexer_for_body(target_mime, '{}') is not None
    for target_mime in (
        'application/xml', 'application/hal+xml', 'application/vnd.api+xml',
        'application/gpx+xml'
    ):
        assert ColorFormatter.get_lexer_for_body(target_mime, '<test/>') is not None
    for target_mime in (
        'application/x-yaml', 'application/vnd.api+yaml'
    ):
        assert ColorForm

# Generated at 2022-06-13 21:58:45.081129
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.plugins.colors.utils import ColorFormatter
    color_formatter = ColorFormatter(env=None,color_scheme=AUTO_STYLE)
    assert color_formatter.get_style_class(color_scheme=AUTO_STYLE) == None
    assert color_formatter.get_style_class(color_scheme=SOLARIZED_STYLE) == Solarized256Style
    assert color_formatter.get_style_class(color_scheme=DEFAULT_STYLE) == Solarized256Style


# Generated at 2022-06-13 21:58:51.730009
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class Dummy_Environment:
        def __init__(self):
            self.colors = None
    class Dummy_ColorFormatter(ColorFormatter):
        def __init__(self, environment):
            super().__init__(environment)
            self.explicit_json = False
            self.formatter = None

    fmt = Dummy_ColorFormatter(Dummy_Environment())
    fmt.get_lexer_for_body = lambda mime, body: TextLexer()
    fmt.formatter = TerminalFormatter()
    body = 'hello world'
    assert fmt.format_body(body, 'application/json') == body
    assert fmt.format_body(body, 'text/plain') == body
    assert fmt.format_body(body, 'text/html') == body

# Generated at 2022-06-13 21:59:04.697643
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env)
    headers = """GET / HTTP/1.1
Host: www.google.com
Accept: text/html
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.5
Connection: keep-alive"""

# Generated at 2022-06-13 21:59:14.675341
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    env = Environment(colors=256)
    color_formatter_256 = ColorFormatter(env=env, color_scheme="solarized")

    body = """{
    "readme": "This is a test."
}"""
    # The json lexer will be selected because the body is a valid json object
    assert color_formatter_256.get_lexer_for_body("application/json", body) == pygments.lexers.get_lexer_by_name("json")


if __name__ == '__main__':
    test_ColorFormatter_get_lexer_for_body()

# Generated at 2022-06-13 21:59:31.250275
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    # arrange
    headers_str = '''GET /api/v1/users HTTP/1.1
Host: 127.0.0.1:8000
User-Agent: python-requests/2.24.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Authorization: Token ea476aabeaebd0ddf9ffa9c195e2b1dae0c02b37
'''

    import platform
    import os
    import sys

    sys.platform = 'linux'


# Generated at 2022-06-13 21:59:36.676138
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    with open("testcase.txt", "r", encoding='utf-8') as f:
        data = f.read()
    ans = lexer.get_tokens(data)
    for i in ans:
        print(i)


# Generated at 2022-06-13 22:01:09.454293
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.input import ParseException
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.builtin import HTTPProxyAuth
    from httpie.plugins.builtin import HTTPDigestAuth
    from httpie.plugins.builtin import HTTPAuthPlugin
    from httpie.plugins.builtin import session
    from httpie.plugins.builtin import AuthPlugin
    from httpie.plugins.builtin import JSONStreamFormatter
    from httpie.plugins.builtin import stream
    from httpie.plugins.builtin import IgnoreStdinPlugin
    from httpie.plugins.builtin import HTTPHeaders
    from httpie.plugins.builtin import HTTPOptions
    from httpie.plugins.builtin import HTTPMethod
    from httpie.plugins.builtin import HTTPiePlugin