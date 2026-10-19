

# Generated at 2022-06-13 21:51:34.781810
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.compat import urlopen
    from httpie.core import main

    responses = main(
        args=['--style=solarized', '--body-on-error', 'GET', 'http://httpbin.org/get'],
        env=Environment(),
        stdin=urlopen(''),
        stdin_isatty=True,
        stdout=None,
        stdout_isatty=True,
    )

    assert '\x1b[7m\x1b[32mHTTP/1.1\x1b[0m \x1b[32m200\x1b[0m' in responses[0].rendered_output

# Generated at 2022-06-13 21:51:43.495533
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import io
    from httpie.output.colors import ColorFormatter
    from httpie.plugins import FormatterPlugin
    import pygments.formatters
    import sys
    args = io.StringIO()
    sys.stdout = args
    env = FormatterPlugin.Config(colors=True)

# Generated at 2022-06-13 21:51:53.001053
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    headers = '''GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/0.9.2'''

# Generated at 2022-06-13 21:52:03.334618
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    request_line = 'GET / HTTP/1.1'
    status_line = 'HTTP/1.1 200 OK'
    headers = 'Content-Type: text/html'

    tokens = SimplifiedHTTPLexer().get_tokens_unprocessed(request_line)
    assert tuple(tokens) == (
        (pygments.token.Name.Function, 'GET'),
        (pygments.token.Text, ' '),
        (pygments.token.Name.Namespace, '/'),
        (pygments.token.Text, ' '),
        (pygments.token.Keyword.Reserved, 'HTTP'),
        (pygments.token.Operator, '/'),
        (pygments.token.Number, '1.1'),
    )

    tokens = SimplifiedHTTPLexer().get_tok

# Generated at 2022-06-13 21:52:09.098519
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('text/html') == pygments.lexers.get_lexer_by_name('html')
    assert get_lexer('application/json') == pygments.lexers.get_lexer_by_name(
        'json')
    assert get_lexer('application/vnd.github+json') == \
           pygments.lexers.get_lexer_by_name('json')
    assert get_lexer('application/vnd.github.v3+json') == \
           get_lexer('application/vnd.github+json')

# Generated at 2022-06-13 21:52:22.471691
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.plugins import FormatterPluginManager
    from httpie.context import Environment
    env = Environment()
    env.stdout = io.StringIO()
    env.stderr = io.StringIO()
    plugin_manager = FormatterPluginManager(env=env)
    color_formatter = ColorFormatter(env=env)
    plugin_manager.add_plugin(plugin=color_formatter, name=color_formatter.name)
    plugin_manager.enable(name=color_formatter.name)

    color_formatter.format_headers(headers="test")
    assert env.stdout.getvalue() == '\x1b[38;5;33mtest\x1b[0m\n'


# Generated at 2022-06-13 21:52:32.919816
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    env = Environment()
    color = ColorFormatter(env, explicit_json=False, color_scheme='monokai')
    lexer = color.get_lexer_for_body("application/json", "")
    assert lexer.__name__ == "JSONLexer"

    lexer = color.get_lexer_for_body("application/json", '{"name": "httpie"}')
    assert lexer.__name__ == "JSONLexer"

    lexer = color.get_lexer_for_body("application/json", '{}')
    assert lexer.__name__ == "JSONLexer"

    lexer = color.get_lexer_for_body("application/json", '{asdf}')
    assert lexer.__name__ == "TextLexer"

# Generated at 2022-06-13 21:52:43.829476
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    file = open("../../data/sample_response.json","r") 
    data = file.read()
    response_color = ColorFormatter(Environment, False, "solarized")
    response_color.http_lexer.name = 'HTTP'
    response_color.formatter.style_name = 'solarized256'
    lexer = response_color.get_lexer_for_body("application/json", data)
    body_colored = response_color.format_body(body=data, mime="application/json")
    print(body_colored)

test_ColorFormatter_format_body()

# Generated at 2022-06-13 21:52:45.087873
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    print(ColorFormatter(Environment()))

# Generated at 2022-06-13 21:52:49.302950
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import httpie.core
    c = ColorFormatter(None)
    body = c.format_body(
        body='"value"',
        mime='application/json'
    )
    assert isinstance(body, str), body



# Generated at 2022-06-13 21:53:02.892246
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.context import Environment

    env = Environment()
    env.stdout_isatty = True
    color_formatter = ColorFormatter(env=env)

    assert color_formatter.formatter.__class__.__name__ == 'Terminal256Formatter'
    assert color_formatter.http_lexer.__class__.__name__ == 'SimplifiedHTTPLexer'



# Generated at 2022-06-13 21:53:16.577427
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from .helpers import TestEnvironment
    env = TestEnvironment()
    env.stdout_isatty = True
    env.colors = True
    env.color_scheme = AUTO_STYLE
    formatter = ColorFormatter(env)
    assert formatter.get_style_class('fruity') == pygments.styles.get_style_by_name('fruity')
    assert formatter.get_style_class(AUTO_STYLE) == Solarized256Style
    assert formatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style

    env.stdout_isatty = True
    env.colors = 256
    env.color_scheme = AUTO_STYLE
    formatter = ColorFormatter(env)
    assert formatter.get

# Generated at 2022-06-13 21:53:24.873265
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    import pytest
    from httpie.context import Environment
    env = Environment()

    def test(mime, expected):
        cf = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
        lexer = cf.get_lexer_for_body(mime, "")

        # lexer may be None
        if lexer:
            assert lexer.name == expected

    test('application/json', 'json')
    test('text/plain', 'text')
    # TODO: add more tests

# Generated at 2022-06-13 21:53:34.832702
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    http_lexer = SimplifiedHTTPLexer()

    assert http_lexer.name == 'HTTP'
    assert http_lexer.aliases == ['http']
    assert http_lexer.filenames == ['*.http']

# Generated at 2022-06-13 21:53:40.752207
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    color_formatter = ColorFormatter(color_scheme="fruity", env=Environment(colors=True))
    body = '<html></html>'
    mime = 'application/xml'
    result = color_formatter.format_body(body, mime)
    assert result != body

# Generated at 2022-06-13 21:53:54.153346
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    class NullEnvironment:
        colors = 256

# Generated at 2022-06-13 21:54:02.320167
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(None)
    # test case:
    #   mime = application/json; charset=UTF-8
    assert formatter.get_lexer_for_body('application/json; charset=UTF-8','') == pygments.lexers.get_lexer_by_name('json')

    # test case:
    #   mime = text/html; charset=UTF-8
    assert formatter.get_lexer_for_body('text/html; charset=UTF-8','') == pygments.lexers.get_lexer_by_name('html')

    # test case:
    #   mime = text/plain
    assert formatter.get_lexer_for_body('text/plain','') is None

# Generated at 2022-06-13 21:54:09.071669
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    def test(body, mime, lexer_name):
        lexer = ColorFormatter(None).get_lexer_for_body(body, mime)
        assert lexer.name == lexer_name

    test('{}', 'application/json', 'JSON')
    test('{}', 'application/json; charset=utf-8', 'JSON')
    test('{}', 'application/json; indent=4', 'JSON')
    test('foo()', 'application/javascript', 'JavaScript')
    test('foo()', 'application/javascript; indent=4', 'JavaScript')
    test('bar()', 'application/ecmascript', 'JavaScript')
    test('<html></html>', 'application/xml', 'XML')
    test('<html></html>', 'text/xml', 'XML')

# Generated at 2022-06-13 21:54:19.772907
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter({})

    # First test json
    lexer = formatter.get_lexer_for_body("application/json", '{"key": "value"}')
    assert lexer is not None #if the body is json, a lexer is returned
    assert lexer.name == 'JSON' #lexer name should be JSON

    # Then test non-json
    lexer = formatter.get_lexer_for_body("text/html", '<html>')
    assert lexer.name == 'HTML' #lexer name should be HTML

    # Then test xml
    lexer = formatter.get_lexer_for_body("application/xml", '<xml>')
    assert lexer.name == 'XML' #lexer name should be XML

    # Then test non-recognized content-type
   

# Generated at 2022-06-13 21:54:32.400992
# Unit test for function get_lexer
def test_get_lexer():
    get_lexer = ColorFormatter.get_lexer_for_body
    # Regular lexer
    assert get_lexer('text/plain', '') == pygments.lexers.get_lexer_by_name('text')

    # Content type with charset
    assert get_lexer('text/plain; charset=UTF-8', '') == pygments.lexers.get_lexer_by_name('text')

    # Special case for JSON
    assert get_lexer('application/json', '{}') == pygments.lexers.get_lexer_by_name('json')

    # Special case for JSON and explicit --json flag
    assert get_lexer('application/javascript', '{}', True) == pygments.lexers.get_lexer_by_name('json')

    # Weird mimetype

# Generated at 2022-06-13 21:54:44.717673
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter(Environment())
    body = "this is a test body"
    mime = 'text/html'
    expected = body
    assert expected == formatter.format_body(body, mime)

# Generated at 2022-06-13 21:54:51.823114
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import unittest as ut


    class TestCase(ut.TestCase):
        def test_format_body(self):
            import json


            formatter = ColorFormatter(
                env=Environment(),
                explicit_json=False,
                color_scheme='auto',
                enable_format=True,
            )
            mime = 'application/json'
            target_str = "null"
            body = json.dumps(json.loads(target_str))
            res = formatter.format_body(body, mime)
            self.assertEqual(target_str, res)


    ut.main()

# Generated at 2022-06-13 21:55:02.935547
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    # RFC 2616 (HTTP/1.1)
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']

# Generated at 2022-06-13 21:55:08.415380
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=256)
    color_formatter_plugin = ColorFormatter(env=env)
    headers='''GET / HTTP/1.1
Host: www.google.com
User-Agent: httpie

'''
    color_formatter_plugin.format_headers(headers)



# Generated at 2022-06-13 21:55:22.627217
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    from pygments.token import Token
    from pygments import highlight
    example = b"GET / HTTP/1.1\n\n"
    assert (highlight(example, SimplifiedHTTPLexer(), Terminal256Formatter()) ==
            "[38;5;40m[38;5;222mGET[38;5;228m [38;5;40m/[38;5;222m HTTP[38;5;228m/[38;5;40m1.1[38;5;228m\n\n")
    example = b"HTTP/1.1 200 OK\nContent-Length: 10\n\n"

# Generated at 2022-06-13 21:55:34.060443
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import pygments.lexers
    import pygments.formatters

    cf = ColorFormatter(Environment())
    lexer = pygments.lexers.get_lexer_by_name('json')
    formatter = pygments.formatters.TerminalFormatter()
    result = pygments.highlight(code="{}", lexer=lexer, formatter=formatter)
    assert cf.format_body(body="{}", mime="application/json") == result
    assert cf.format_body(body="<html><body>Hello</body></html>", mime="text/html") == "<html><body>Hello</body></html>"


# Generated at 2022-06-13 21:55:43.468661
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2022-06-13 21:55:57.073424
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    class Dummy(ColorFormatter):
        def __init__(self):
            super().__init__(None, explicit_json=False, color_scheme='auto')
        def format_headers(self, headers: str) -> str:
            return headers
        def format_body(self, body: str, mime: str) -> str:
            return body
    color_formatter = Dummy()

    # We use the simplified Lexer because it is easier to debug and
    # it is sufficient for our testing purposes.
    assert color_formatter.get_lexer_for_body(mime='text/html; charset=utf-8', body='') == pygments.lexers.get_lexer_for_mimetype('text/html')

# Generated at 2022-06-13 21:56:04.744910
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    env.colors = 256
    color_formatter = ColorFormatter(env=env, color_scheme='solarized')
    assert color_formatter.formatter == Terminal256Formatter(
        style=Solarized256Style)

    env.colors = 256
    color_formatter = ColorFormatter(env=env, color_scheme='auto')
    assert color_formatter.formatter == TerminalFormatter()

    env.colors = 8
    color_formatter = ColorFormatter(env=env, color_scheme='auto')
    assert color_formatter.formatter == TerminalFormatter()

    env.colors = 8
    color_formatter = ColorFormatter(env=env, color_scheme='solarized')
    assert color_formatter.formatter == TerminalFormatter()

# Generated at 2022-06-13 21:56:15.909121
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=256)
    ColorFormatter(env)
    raw_headers = '''\
GET / HTTP/1.1
Host: localhost:8080
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: JSESSIONID=23091489B4D4AD4F5581B8AFF7350544'''

# Generated at 2022-06-13 21:56:43.880240
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    import pygments.formatters.terminal
    from pygments.lexers.special import TextLexer
    from pygments.lexers.text import HttpLexer as PygmentsHttpLexer

    env = Environment(colors=256)
    assert isinstance(env, Environment)
    assert env.colors == 256

    explicit_json = False
    color_scheme = DEFAULT_STYLE
    formatter = ColorFormatter(env, explicit_json, color_scheme)
    assert isinstance(formatter, ColorFormatter)
    assert isinstance(formatter.formatter, pygments.formatters.terminal256.Terminal256Formatter)
    assert isinstance(formatter.formatter.style, Solarized256Style)

# Generated at 2022-06-13 21:56:46.440710
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:56:48.603721
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter = ColorFormatter(Environment())
    assert formatter

# Generated at 2022-06-13 21:56:55.210428
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.output.formatters.colors import ColorFormatter
    formatter = ColorFormatter(None, False)
    assert '\x1b[' in ColorFormatter.format_body('{"x": 1}', 'application/json')
    assert '\x1b[' not in ColorFormatter.format_body('abc', 'text/plain')


# Generated at 2022-06-13 21:57:00.624068
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    formatter = ColorFormatter(Environment())
    input_str = 'HTTP/1.1 200 OK\r\nHost: example.com\r\nAccept: text/html\r\n'
    output_str = formatter.format_headers(input_str)
    print(output_str)
    assert output_str is not None

# Generated at 2022-06-13 21:57:05.273072
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    from pygments.lexers.text import HttpLexer
    http_lexer = HttpLexer()
    simplified_http_lexer = SimplifiedHTTPLexer()
    assert http_lexer != simplified_http_lexer
    assert len(http_lexer.tokens) > len(simplified_http_lexer.tokens)

# Generated at 2022-06-13 21:57:12.977935
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.utils import JSON_SORT_KEYS
    from httpie.plugins.builtin import JSONFormatter

    def get_ColorFormatter(explicit_json: bool):
        return ColorFormatter(
            env=Environment(colors=True),
            explicit_json=explicit_json,
            json_sort_keys=JSON_SORT_KEYS,
            indent=2,
        )

    color_formatter = get_ColorFormatter(explicit_json=False)
    json_formatter = JSONFormatter(
        json_sort_keys=JSON_SORT_KEYS,
        indent=2,
    )


# Generated at 2022-06-13 21:57:25.149457
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    """ ColorFormatter.format_headers()
    """
    from httpie.compat import str
    from httpie import ExitStatus
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from httpie.cli import parser
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    from httpie.models import HTTPRequest
    from httpie import __version__

    http_request = HTTPRequest(
        method='GET',
        url='http://httpie.org',
        headers={'Accept-Encoding': 'utf8'},
        auth=None,
        timeout=None,
    )

    args = parser.parse_args([
        '--ignore-stdin',
        '--print=H',
        '--verbose',
    ])


# Generated at 2022-06-13 21:57:37.737001
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from io import StringIO
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    env = Environment()
    class mock:
        pass
    formatter_plugin = FormatterPlugin(mock())
    color_formatter = ColorFormatter(env, None)

    def get_style_class(name):
        color_formatter.get_style_class(name)

    get_style_class(SOLARIZED_STYLE)
    get_style_class(AUTO_STYLE)
    get_style_class(DEFAULT_STYLE)
    try:
        get_style_class(DEFAULT_STYLE + '_')
    except:
        assert True
    try:
        get_style_class('')
    except:
        assert True

# Generated at 2022-06-13 21:57:48.095499
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():

    # MIME type 'text/plain'
    assert get_lexer('text/plain') == pygments.lexers.get_lexer_by_name('text')

    # MIME type 'application/javascript'
    assert get_lexer('application/javascript') == pygments.lexers.get_lexer_by_name('js')

    # MIME type 'application/x-javascript'
    assert get_lexer('application/x-javascript') == pygments.lexers.get_lexer_by_name('js')

    # MIME type 'application/json; charset=utf-8'
    assert get_lexer('application/json; charset=utf-8') == pygments.lexers.get_lexer_by_name('json')

# Generated at 2022-06-13 21:58:12.359639
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import main
    from httpie.core import parse_args
    from httpie.plugins import FormatterPluginManager
    from httpie.context import Environment
    from pygments.formatters.terminal import TerminalFormatter
    from pygments.formatters.terminal256 import Terminal256Formatter
    from pygments.lexers.text import HttpLexer as PygmentsHttpLexer
    from pygments.lexer import Lexer
    from pygments.lexers.special import TextLexer
    from pygments.lexers.html import HtmlLexer
    from httpie.output.formatters.colors import ColorFormatter
    import pygments.styles
    from pygments.util import ClassNotFound


# Generated at 2022-06-13 21:58:23.359864
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(
        Environment(colors=256)
    )


# Generated at 2022-06-13 21:58:35.534748
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    import pygments.lexers
    colorFormatter = ColorFormatter("")
    tests = [
        ('application/json', '{}', pygments.lexers.get_lexer_by_name('json')),
        ('application/json+foo', '{}', pygments.lexers.get_lexer_by_name('json')),
        ('application/json; charset=utf-8', '{}', pygments.lexers.get_lexer_by_name('json')),
        ('application/foobar', '{}', None),
        ('application/foobar+json', '{}', None),
        ('application/foobar; charset=utf-8+json', '{}', None),
        ('application/foobar; charset=utf-8', '{}', None),
    ]

# Generated at 2022-06-13 21:58:45.656147
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    try:
        from pygments.lexers.data import JsonLexer as PygmentsJsonLexer
    except ImportError:
        try:
            from pygments.lexers.agile import JsonLexer as PygmentsJsonLexer
        except ImportError:
            PygmentsJsonLexer = None

    env = Environment(colors=256, stdout_isatty=True)
    request = 'GET /'
    headers = ['Accept: application/json', 'Content-Type: application/json']
    headers_str = '\n'.join([request, *headers])

    # mock http_lexer, in order to test response header
    http_lexer = SimplifiedHTTPLexer()
    formatter = Terminal256Formatter(style=Solarized256Style)


# Generated at 2022-06-13 21:58:52.023890
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from pygments.token import Token
    from pygments.lexers import JsonLexer

    class MockFormatter:
        def __init__(self):
            self.levels = []
            self.text = []
            self.tokens = []

        def get_style_defs(self, *args, **kwargs):
            pass

        def format(self, tokensource, outfile):
            self.levels.append(tokensource.level)
            self.text.append(tokensource.text)
            self.tokens.append(tokensource.tokens)

    cf = ColorFormatter(None, False, 'fruity')
    cf.formatter = MockFormatter()

    lexer = JsonLexer()

# Generated at 2022-06-13 21:59:04.995047
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    test_string = 'GET / HTTP/1.1\r\n' + 'Content-Type: application/json\r\n'
    expected_tokens = [
        (2, pygments.token.Name.Namespace),
        (6, pygments.token.Keyword.Reserved),
        (6, pygments.token.Operator),
        (5, pygments.token.Number),
        (1, pygments.token.Text),
        (1, pygments.token.Name.Attribute),
        (14, pygments.token.Text),
        (1, pygments.token.Operator),
        (1, pygments.token.Text),
        (19, pygments.token.String)
    ]
    # Since we are comparing the actual tokens,

# Generated at 2022-06-13 21:59:16.864715
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie import ExitStatus
    from httpie.client import HTTP_ERROR_EXIT_STATUS
    from httpie.core import main
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPCookieAuth, HTTPHeader
    from httpie.compat import is_windows
    import logging
    import threading
    import time

    class ThreadWithReturnValue(threading.Thread):
        def __init__(self, group=None, target=None, name=None,
                     args=(), kwargs={}, Verbose=None):
            threading.Thread.__init__(self, group, target, name, args, kwargs)
            self._return = None

# Generated at 2022-06-13 21:59:21.650638
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    color_formatter = ColorFormatter(Environment())
    body, mime = '{"hello": "world"}', 'application/json'
    assert color_formatter.format_body(body, mime)

# Generated at 2022-06-13 21:59:26.570016
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter()
    assert formatter.format_body('body', 'text/html') == 'body'
    assert formatter.format_body('body', 'application/json') == 'body'

# Generated at 2022-06-13 21:59:38.672749
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # available_lexers = pygments.lexers.get_all_lexers()
    class testEnv(object):
        def __init__(self):
            self.colors = 256
    from httpie.plugins import plugin_manager
    from httpie.main import get_client, Environment, parse_json
    from httpie.plugins import FormatterPlugin

    class JSONPrettyFormatter(FormatterPlugin):
        help = ''

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def format_body(self, body, mime):
            return self.json_indent(body)

    plugin_manager.register(JSONPrettyFormatter, 'json_pp', 'json_pretty')

    # print_json = JSONPrettyFormatter()

    # resp = get_client(Environment(

# Generated at 2022-06-13 21:59:59.194166
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment()
    colorFormatter = ColorFormatter(env, False, None)
    headers = colorFormatter.format_headers("GET /api/v1/products HTTP/1.1\n"
                                            "Accept: application/json\n"
                                            "Content-Type: application/json")

# Generated at 2022-06-13 22:00:06.397313
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style
    assert ColorFormatter.get_style_class('monokai') == pygments.styles.Monokai
    assert ColorFormatter.get_style_class('nonexistent') == Solarized256Style
    assert ColorFormatter.get_style_class(None) == Solarized256Style
    assert ColorFormatter.get_style_class('') == Solarized256Style
    assert ColorFormatter.get_style_class(object) == Solarized256Style

# Generated at 2022-06-13 22:00:08.359411
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    processor = ColorFormatter(env)

# Generated at 2022-06-13 22:00:10.884126
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style = ColorFormatter.get_style_class('solarized256')
    assert style == Solarized256Style
    assert style.styles[pygments.token.Name.Builtin.Pseudo] == '#d75f00'

# Generated at 2022-06-13 22:00:18.413846
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import httpie.formatter

    from unittest import mock

    class MockColorFormatter(httpie.formatter.ColorFormatter):
        def get_style_class(self, color_scheme: str) -> Type[pygments.style.Style]:
            return pygments.styles.get_style_by_name('monokai')

    headers = """\
HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Sun, 25 Feb 2018 16:30:46 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 3
Connection: keep-alive
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
X-DNS-Prefetch-Control: off

"""


# Generated at 2022-06-13 22:00:22.100434
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # type: () -> None
    color_format = ColorFormatter(Environment(), False, 'solarized')
    assert color_format.__class__.__name__ == 'ColorFormatter'
    assert color_format.enabled

# Generated at 2022-06-13 22:00:24.226784
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env= Environment(colors=True)
    formatter= ColorFormatter(env)
    pass

# Generated at 2022-06-13 22:00:32.461011
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    color_formatter = ColorFormatter(
        env=env,
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )
    assert color_formatter.color_scheme_name == DEFAULT_STYLE
    assert color_formatter.enabled
    assert color_formatter.explicit_json
    assert isinstance(color_formatter.formatter, TerminalFormatter)
    assert isinstance(color_formatter.http_lexer, PygmentsHttpLexer)



# Generated at 2022-06-13 22:00:39.085479
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style = ColorFormatter.get_style_class('solarized256')
    assert issubclass(style, pygments.style.Style)
    assert style == Solarized256Style
    style = ColorFormatter.get_style_class('solarized')
    assert issubclass(style, pygments.style.Style)
    assert style == Solarized256Style

# Generated at 2022-06-13 22:00:41.650541
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('native') == pygments.styles.get_style_by_name('native')

# Generated at 2022-06-13 22:01:12.446957
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert 'HTTP' == SimplifiedHTTPLexer.name

