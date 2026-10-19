

# Generated at 2022-06-13 21:51:37.551490
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    """
    Verify that the output of SimplifiedHTTPLexer will be the same as the
    expected result.

    """
    simplified_lexer = SimplifiedHTTPLexer()
    content = """GET / HTTP/1.1

Host: httpbin.org
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.18.4


HTTP/1.1 200 OK
Connection: keep-alive
Server: gunicorn/19.7.1
Date: Wed, 11 Apr 2018 14:58:08 GMT
Content-Type: application/json
Content-Length: 15763
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Via: 1.1 vegur


"""

    # The order of

# Generated at 2022-06-13 21:51:49.048548
# Unit test for method format_headers of class ColorFormatter

# Generated at 2022-06-13 21:52:00.113532
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    import pygments.lexers
    import re

    class TestColorFormatter(ColorFormatter):
        def perform_format(self, body_bytes, mime):
            return self.format_body(body_bytes.decode('utf-8'), mime)

    def check_response(mime, body, lexer):
        assert TestColorFormatter(None).get_lexer_for_body(mime, body) == lexer

    def get_lexer_class_name(lexer):
        return re.sub('^<class \'pygments.lexers.\w+\.', '', str(lexer))

    # JSON with incorrect Content-Type => JSON Lexer
    check_response('text/plain', '{"foo": "bar"}', pygments.lexers.JsonLexer)

# Generated at 2022-06-13 21:52:02.467550
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color = ColorFormatter(Environment(), None)
    assert isinstance(color, ColorFormatter)

# Generated at 2022-06-13 21:52:10.128669
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    args = [
        'http',
        '--body-format=colors',
        'httpbin.org/post',
        'a=b'
    ]
    cfg = {
       'color_scheme': 'solarized',
    }

# Generated at 2022-06-13 21:52:24.351685
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.cli.argtypes import MIME_TYPES


# Generated at 2022-06-13 21:52:25.308911
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter is not None

# Generated at 2022-06-13 21:52:34.814789
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import main
    import textwrap
    r = main(['--json', '--headers', 'https://httpbin.org/post'], '''\
    POST /post HTTP/1.1
    Accept: application/json
    Accept-Encoding: identity

    {
        "json": true
    }
    ''')

# Generated at 2022-06-13 21:52:43.700775
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import main
    arguments = {'--headers': False, '--json': False, '--pretty': False, '--style': 'solarized', '--verbose': False, '--version': False, '<url>': 'http://httpbin.org/json'}
    test_env = {'color': True, 'explicit_json': False}
    response = main(arguments=arguments, env=test_env)
    assert response.exit_code == 0

# Generated at 2022-06-13 21:52:52.406459
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import sys

    def detect_colors() -> int:
        if sys.platform == 'win32':
            return 0
        if 'COLORTERM' in os.environ:
            return 256
        if sys.stdout.isatty():
            try:
                import curses
                curses.setupterm()
                return curses.tigetnum('colors')
            except Exception:
                return 0
        return 0

    env = Environment(
        colors=detect_colors(),
    )
    formatter = ColorFormatter(env=env)
    assert formatter.formatter
    assert formatter.http_lexer

# Generated at 2022-06-13 21:53:09.171061
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    c = ColorFormatter(
        env=Environment(colors=256, is_windows=True),
        color_scheme=SOLARIZED_STYLE
    )
    print(c.formatter.__class__.__name__)
    assert c.formatter.__class__.__name__ == 'Terminal256Formatter'

    c = ColorFormatter(
        env=Environment(colors=256, is_windows=False),
        color_scheme=SOLARIZED_STYLE
    )
    print(c.formatter.__class__.__name__)
    assert c.formatter.__class__.__name__ == 'Terminal256Formatter'


# Generated at 2022-06-13 21:53:16.957069
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('text/plain') is None
    assert type(get_lexer('application/json')) is pygments.lexers.JsonLexer
    assert type(get_lexer('application/javascript')) is pygments.lexers.JavascriptLexer
    assert type(get_lexer('text/html')) is pygments.lexers.HtmlLexer


if __name__ == '__main__':
    import sys
    import doctest
    doctest.testmod(sys.modules[__name__])

# Generated at 2022-06-13 21:53:32.085192
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    """
    This lexer can handle the case where a HTTP message body
    looks like a header.
    """
    from pygments.token import Token
    from pygments.formatters import TerminalFormatter
    from pygments import highlight
    import io


# Generated at 2022-06-13 21:53:38.144375
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    simplifier = SimplifiedHTTPLexer()
    print(pygments.highlight('GET / HTTP/1.1\nHost: localhost', simplifier, pygments.formatters.TerminalFormatter()))


test_SimplifiedHTTPLexer()

# Generated at 2022-06-13 21:53:47.020448
# Unit test for function get_lexer
def test_get_lexer():
    lexer = get_lexer(mime='text/foo')
    assert isinstance(lexer, TextLexer)
    assert lexer.name == 'Text only'
    assert lexer.aliases == ['text']

    lexer = get_lexer(mime='text/foo', explicit_json=True, body='{"foo":"bar"}')
    assert lexer.name == 'JSON'
    assert lexer.aliases == ['json']

# Generated at 2022-06-13 21:53:58.493351
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    for debuglevel in range(0,40):
            class DummyRequest(object):
                def __init__(self, method, path):
                    self.method = method
                    self.path = path
            env = Environment(colors=True, stdout=None, stderr=None, stdin=None, debug=debuglevel)
            colorFormatter = ColorFormatter(env=env)
            headers = 'Content-Type: text/html\nHost: localhost'
            result = colorFormatter.format_headers(headers)
            assert(result == '\x1b[38;5;245mContent-Type\x1b[39m: text/html\n\x1b[38;5;245mHost\x1b[39m: localhost')
            if debuglevel>=10:
                colorFormatter.format

# Generated at 2022-06-13 21:54:06.131206
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.cli import parser
    args = parser.parse_args(args=[])
    headers = "HTTP/1.1 200 OK\nDate: Mon, 27 Jul 2009 12:28:53 GMT\nServer: Apache Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT ETag: \"34aa387-d-1568eb00\" Accept-Ranges: bytes Content-Length: 51 Vary: Accept-Encoding Content-Type: text/plain\nX-Pad: avoid browser bug"
    color_formatter = ColorFormatter(env=args.__dict__)
    color_formatter.http_lexer = SimplifiedHTTPLexer()
    color_formatter.formatter = Terminal256Formatter(
        style=Solarized256Style
    )

# Generated at 2022-06-13 21:54:18.303182
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('application/json') == pygments.lexers.get_lexer_by_name('json')
    assert get_lexer('application/json',  explicit_json=True) == pygments.lexers.get_lexer_by_name('json')
    assert get_lexer('application/json',  explicit_json=True,
                     body='{"test": true}') == pygments.lexers.get_lexer_by_name('json')
    assert get_lexer('application/json',  explicit_json=True,
                     body='{"test": true') == pygments.lexers.get_lexer_by_name('json')
    assert get_lexer('application/notjson',  explicit_json=True,
                     body='{"test": true') == None

# Generated at 2022-06-13 21:54:26.969197
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    c = ColorFormatter
    assert c.get_style_class(AUTO_STYLE) == c.get_style_class('monokai')
    assert c.get_style_class(SOLARIZED_STYLE) == Solarized256Style
    assert c.get_style_class('not_existed_style') == Solarized256Style
    assert c.get_style_class(SOLARIZED_STYLE) == Solarized256Style



# Generated at 2022-06-13 21:54:29.253941
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(AUTO_STYLE) != Solarized256Style

# Generated at 2022-06-13 21:54:46.023203
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import pytest
    from httpie.plugins import plugin_manager
    from httpie.context import Environment
    from httpie.plugins.colors import ColorFormatter

# Generated at 2022-06-13 21:54:56.278941
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.plugins import builtin
    builtin.load_plugins()
    env = Environment(colors=True)
    formatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert "https://example.com" \
           in formatter.format_body('{"url": "https://example.com"}', "application/json")
    assert "" \
           in formatter.format_body('{"nested": {"key": "value"}}', "application/json")
    assert "" \
           in formatter.format_body('{"url": "https://example.com"}', "text/plain")
    assert "" \
           in formatter.format_body('abc123', "text/plain")

# Generated at 2022-06-13 21:54:58.736777
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    ColorFormatter(
        Environment(),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )


if __name__ == '__main__':
    test_ColorFormatter()

# Generated at 2022-06-13 21:55:03.090539
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    original = pygments.lexers.text.HttpLexer
    temp = SimplifiedHTTPLexer()
    pygments.lexers.text.HttpLexer = SimplifiedHTTPLexer
    ColorFormatter(Environment(), color_scheme='solarized-dark')
    pygments.lexers.text.HttpLexer = original

# Generated at 2022-06-13 21:55:12.350229
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import pytest
    from httpie.compat import urlopen
    from httpie.plugins import FormatterPluginManager
    formatters = FormatterPluginManager.get_available_formatters()
    formatter_plugin = formatters["colors"](None)
    html = urlopen('https://httpie.org/').read()
    assert formatter_plugin.format_body(html, 'text/html') == \
        pygments.highlight(
                code=html,
                lexer=pygments.lexers.HtmlLexer(),
                formatter=pygments.formatters.Terminal256Formatter(),
            )
    with pytest.raises(ValueError):
        formatter_plugin.format_body('', 'not exist')

# Generated at 2022-06-13 21:55:25.188862
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    vars = {'colors': True, 'style': 'solarized'}
    e = Environment(**{k: vars[k] for k in ('colors', 'style')})
    c = ColorFormatter(e)

    # GET /tasks/api HTTP/1.1
    # Accept: application/json; indent=4
    # Content-Type: application/json
    text = r'GET /tasks/api HTTP/1.1\nAccept: application/json; indent=4\nContent-Type: application/json'

# Generated at 2022-06-13 21:55:36.221652
# Unit test for method format_headers of class ColorFormatter

# Generated at 2022-06-13 21:55:37.645046
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style

# Generated at 2022-06-13 21:55:47.212609
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.builtin import HTTPDigestAuth
    from httpie.plugins.builtin import HTTPBearerAuth
    from httpie.plugins.builtin import HTTPNtlmAuth
    from httpie.plugins.builtin import HTTPProxyAuth
    from httpie.plugins.builtin import FormatterPlugin
    from httpie.plugins.builtin import JSONOptionsPlugin
    from httpie.plugins.builtin import RawOptionsPlugin
    from httpie.plugins.builtin import PrettyOptionsPlugin
    import httpie.plugins.builtin

    plugins = [
        HTTPBasicAuth, HTTPDigestAuth, HTTPProxyAuth, HTTPBearerAuth, HTTPNtlmAuth, FormatterPlugin,
        JSONOptionsPlugin, RawOptionsPlugin, PrettyOptionsPlugin
    ]

# Generated at 2022-06-13 21:55:55.220448
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    """
    Unit test for method format_body of class ColorFormatter
    """
    color_formatter = ColorFormatter(None)
    assert "".join(color_formatter.format_body("{\"bar\\n\",\"a\":\"b\"}", 'application/json')) == "{\"bar\\n\",\"a\":\"b\"}", \
        "color_formatter.format_body returns the same string if it doesn't know the mimetype"



# Generated at 2022-06-13 21:56:06.258342
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter = ColorFormatter(None)
    assert color_formatter != None

# Generated at 2022-06-13 21:56:18.800617
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    http_lexer = SimplifiedHTTPLexer()
    assert http_lexer.name == 'HTTP'
    assert http_lexer.aliases == ['http']
    assert http_lexer.filenames == ['*.http']

# Generated at 2022-06-13 21:56:30.992800
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.core import main

    class NoArgs(object):
        """No args passed to main, simulates --body='none'"""
        def __init__(self):
            self.follow = False
            self.prettify = True
            self.style = None
            self.colors = 256
            self.body = 'none'
            self.headers = False
            self.verbose = False
            self.debug = False
            self.output_file = None
            self.request_body = None
            self.timeout = None
            self.check_status = False
            self.stream = False
            self.download = False
            self.print_body = True
            self.help = False
            self.version = False
            self.implicit_content_type = None
            self.ignore_stdin = False
           

# Generated at 2022-06-13 21:56:32.935475
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:56:45.227891
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.compat import is_windows
    from httpie.plugins import FormatterPlugin
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin

    class TestFormatter(FormatterPlugin):
        def format_headers(self, headers):
            return headers

        def format_body(self, body, mime):
            return body

    color_formatter = ColorFormatter(Environment(), False)

    assert '<h1>' in color_formatter.format_body("<h1>hello world</h1>", "text/html")
    assert '<h1>' in color_formatter.format_body("<h1>hello world</h1>", "application/html")

# Generated at 2022-06-13 21:56:55.870257
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    print(ColorFormatter.format_body('string', 'text/string'))
    print(ColorFormatter.format_body('json', 'text/json'))
    print(ColorFormatter.format_body('{}', 'application/json'))
    print(ColorFormatter.format_body('{}', 'application/json; charset=utf-8'))
    print(ColorFormatter.format_body('{}', 'application/json; charset=utf-8;'))
    print(ColorFormatter.format_body('{}', 'application/json;'))

# Generated at 2022-06-13 21:57:05.870755
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter(None, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert formatter.format_body('{}', 'text/json') == '{}'
    assert formatter.format_body('{}', 'text/pown') == '{}'
    assert formatter.format_body('{}', 'text/json;charset=utf-8') == '{}'
    assert formatter.format_body('{}', 'application/json') == '{}'
    assert formatter.format_body('{}', 'application/pown') == '{}'
    assert formatter.format_body('{}', 'application/json;charset=utf-8') == '{}'

# Generated at 2022-06-13 21:57:18.487847
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import io
    from httpie.plugins.builtin import JSONStreamLexer

    env = Environment()
    color_formatter = ColorFormatter(env=env, verbose=True)

    # test case 1:
    # application/json
    mime = "application/json"
    body = '{"name":"yeku","age":18}'
    lexer = color_formatter.get_lexer_for_body(mime, body)
    assert lexer == JSONStreamLexer

    # test case 2:
    # text/html
    mime = "text/html"
    body = "12323232"
    lexer = color_formatter.get_lexer_for_body(mime, body)
    assert lexer is None

    # test case 3:
    # text/html; charset=utf

# Generated at 2022-06-13 21:57:30.701089
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from pygments.lexers.html import HtmlLexer
    myFormatter = ColorFormatter(None)
    assert myFormatter.format_body(body="", mime="text/html") == ""
    assert myFormatter.format_body(body="<html><head><title>My title</title></head></html>", mime="text/html") == "<html><head><title>My title</title></head></html>"
    assert myFormatter.format_body(body="<html><head><title>My title</title></head></html>", mime="text/plain") == "<html><head><title>My title</title></head></html>"

# Generated at 2022-06-13 21:57:32.317273
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:58:01.318196
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    fake_body = 'fake-body'
    assert ColorFormatter.get_lexer_for_body('application/xml', fake_body) is None
    assert isinstance(
        ColorFormatter.get_lexer_for_body('application/json', fake_body),
        pygments.lexers.JsonLexer
    )
    assert ColorFormatter.get_lexer_for_body('application/json', None) is None
    assert ColorFormatter.get_lexer_for_body('text/html', fake_body) is False

# Generated at 2022-06-13 21:58:13.501281
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import io
    import unittest
    import unittest.mock

    request_headers = """\
GET /api HTTP/1.1
Host: www.example.com
Accept: */*
Connection: keep-alive
Content-Length: 15
Content-Type: application/x-www-form-urlencoded

"""


# Generated at 2022-06-13 21:58:23.986720
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    # Request-Line
    #
    # This takes only a single line as input, so make sure we're getting
    # output as expected.
    lexer_output = pygments.highlight(
        'GET / HTTP/2.0\r\n',
        lexer=SimplifiedHTTPLexer(),
        formatter=Terminal256Formatter(style=Solarized256Style),
    )

# Generated at 2022-06-13 21:58:34.342151
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # Given
    formatter = ColorFormatter(Environment())

# Generated at 2022-06-13 21:58:44.201730
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.plugins import FormatterPlugin, _redact_auth, _redact_headers
    from httpie.compat import is_windows
    from httpie.context import Environment
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPDigestAuth
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE


# Generated at 2022-06-13 21:58:53.956500
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    from pygments.token import Token
    from pygments import highlight
    from pygments.lexers import HttpLexer
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']

# Generated at 2022-06-13 21:59:05.855855
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    headers = ''
    mime = 'text/html'
    body = ''
    color_formatter = ColorFormatter(Environment(), explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert color_formatter.format_body(body=body, mime=mime) == ''

    headers = ''
    mime = 'text/html'
    body = '<html></html>\n'
    color_formatter = ColorFormatter(Environment(), explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert color_formatter.format_body(body=body, mime=mime) == '<html></html>\n'

    headers = ''
    mime = 'text/html'

# Generated at 2022-06-13 21:59:12.523431
# Unit test for function get_lexer

# Generated at 2022-06-13 21:59:21.124574
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter = ColorFormatter(env=None)
    # Test public class attributes.
    print(formatter.group_name)
    print(formatter.help)
    print(formatter.is_enabled)
    print(formatter._help_group)
    # Test public instance attributes.
    print(formatter.explicit_json)
    print(formatter.formatter)
    print(formatter.http_lexer)
    # Test public instance methods.
    print(formatter.format_body('',''))
    print(formatter.format_headers(''))
    print(formatter.get_style_class('solarized'))
    print(formatter.get_lexer_for_body('',''))


# Generated at 2022-06-13 21:59:34.839194
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    c = ColorFormatter(None)
    assert c.get_lexer_for_body('application/json', None) == get_lexer('application/json')
    assert c.get_lexer_for_body('application/json', '') == get_lexer('application/json')
    assert c.get_lexer_for_body('application/json', '{}') == get_lexer('application/json')
    assert c.get_lexer_for_body('application/json+json', '{}') == get_lexer('application/json+json')
    assert c.get_lexer_for_body('application/json+a', '{}') == get_lexer('application/json+a')
    assert c.get_lexer_for_body('application/json+a+json', '{}')