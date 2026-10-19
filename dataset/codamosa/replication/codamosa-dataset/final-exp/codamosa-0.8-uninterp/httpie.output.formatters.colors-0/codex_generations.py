

# Generated at 2022-06-13 21:51:34.675763
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    http_lexer = SimplifiedHTTPLexer()
    code = 'GET /'
    tokens = [
        (pygments.token.Name.Function, 'GET '),
        (pygments.token.Name.Namespace, '/'),
    ]
    assert list(http_lexer.get_tokens(code)) == tokens

# Generated at 2022-06-13 21:51:43.437911
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.context import Environment
    from httpie.plugins import BuiltinPluginManager
    from httpie.plugins.builtin import HTTPHeadersPlugin
    from httpie.plugins.colors import ColorFormatter

    env = Environment()
    plugin_manager = BuiltinPluginManager()
    plugin_manager.load_builtin_plugins()
    output_options = plugin_manager.instantiate(
        plugin_name='http-headers',
        env=env
    )


# Generated at 2022-06-13 21:51:45.399808
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert isinstance(SimplifiedHTTPLexer(), pygments.lexer.RegexLexer)

# Generated at 2022-06-13 21:51:54.377230
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']
    assert len(lexer.tokens) == 1
    assert len(lexer.tokens['root']) == 3
    assert lexer.tokens['root'][0][0] == r'([A-Z]+)( +)([^ ]+)( +)(HTTP)(/)(\d+\.\d+)'
    assert lexer.tokens['root'][1][0] == r'(HTTP)(/)(\d+\.\d+)( +)(\d{3})( +)(.+)'

# Generated at 2022-06-13 21:52:00.374293
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    lexer.analyze("POST /foo/bar HTTP/1.1")
    lexer.analyze("Accept: */*")
    lexer.analyze("Accept-Encoding: gzip, deflate, br")
    result = lexer.analyze("Content-Length: 2")
    assert isinstance(result, pygments.token._TokenType)


# Generated at 2022-06-13 21:52:09.159457
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import io
    import httpie.colors as colors
    import httpie.output.formatter as formatter
    from httpie.output.streams import get_output_stream

    env = Environment(colors=256)
    output_stream = get_output_stream(is_terminal=True, is_colors=True)
    formatterCls = formatter.get(
        env,
        output_stream=output_stream,
        color_scheme='solarized'
    )
    formatterCls.get_style_class = ColorFormatter.get_style_class
    formatterCls.format_headers = ColorFormatter.format_headers


# Generated at 2022-06-13 21:52:14.105603
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # Simple call
    assert ColorFormatter.get_style_class(DEFAULT_STYLE) == Solarized256Style
    # Call with invalid color_scheme
    assert ColorFormatter.get_style_class('invalid') is None

# Generated at 2022-06-13 21:52:24.973446
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    cf = ColorFormatter(
        env=Environment('false', '256', False),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )
    assert cf.enabled is False
    cf = ColorFormatter(
        env=Environment('true', '256', False),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )
    assert cf.enabled is True
    assert cf.formatter == Terminal256Formatter(
        style=pygments.styles.get_style_by_name(DEFAULT_STYLE)
    )
    cf = ColorFormatter(
        env=Environment('true', '16', False),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )
    assert cf.enabled

# Generated at 2022-06-13 21:52:34.540821
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import copy
    env = Environment()
    options = copy.deepcopy(env.config)
    options.group_name = 'colors'
    options.explicit_json = True
    options.color_scheme = DEFAULT_STYLE
    formatter = ColorFormatter(env, **options)
    formatter.enabled = True

    headers = """
HTTP/1.1 200 OK
Etag: "626096cd824ccef6daf57cde7d87b9aa"
Content-Type: application/json
Date: Wed, 23 Aug 2017 01:42:44 GMT
"""

# Generated at 2022-06-13 21:52:47.902344
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    # colored in italic
    headers = "GET / HTTP/1.1\r\n" \
              "Host: www.baidu.com\r\n" \
              "Connection: keep-alive\r\n" \
              "Upgrade-Insecure-Requests: 1\r\n" \
              "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)\
              \ AppleWebKit/537.36 (KHTML, like Gecko) " \
              "Chrome/68.0.3440.106 Safari/537.36\r\n" \
              "Accept: text/html,application/xhtml+xml,application/xml;" \
              "q=0.9,image/webp,image/apng,*/*;q=0.8\r\n"

# Generated at 2022-06-13 21:53:00.923803
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert type(lexer) == SimplifiedHTTPLexer
    assert type(lexer.name) == str
    assert type(lexer.aliases) == list
    assert type(lexer.filenames) == list
    assert type(lexer.tokens) == dict

# Generated at 2022-06-13 21:53:13.248453
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import io, sys
    from httpie import ExitStatus, main
    from httpie.compat import is_windows
    from httpie.context import Environment
    from httpie.output import BINARY_SUPPRESSED_NOTICE
    from utils import http, HTTP_OK, MOCK_HTTP_RESPONSE, MOCK_HTTP_REQUEST
    from utils import TestEnvironment, mock
    args = httpie.cli.parser.parse_args(args=[
        '--print', 'hB', '--headers', 'GET', MOCK_HTTP_RESPONSE.url
    ], env=Environment())

# Generated at 2022-06-13 21:53:16.957890
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.context import Environment
    env = Environment()
    formatter = ColorFormatter(env, explicit_json=False, color_scheme='auto')
    assert formatter.name == 'colors'
    assert formatter.enabled == False

# Generated at 2022-06-13 21:53:28.847270
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import main  # Avoid circular import
    from httpie.input import ParseError

    import mock
    from pytest import raises

    class MockEnv(object):
        colors = 256

    class MockExitStatus(object):
        def __init__(self):
            self.value = 0

    class MockStdout(object):
        def getvalue(self):
            return self.value

        def write(self, value):
            self.value = value

    class MockStderr(object):
        def getvalue(self):
            return self.value

        def write(self, value):
            self.value = value

    def test_cases():
        yield 'text/plain', 'plain'
        yield 'text/html', 'html'
        yield 'application/javascript', 'javascript'

# Generated at 2022-06-13 21:53:29.600315
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    SystemExit()

# Generated at 2022-06-13 21:53:42.296202
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.formatter.colors import ColorFormatter
    from requests import Response
    env = Environment(colors=256)
    color_formatter = ColorFormatter(env)
    content_type = 'application/json'
    response = Response()
    response.headers['content-type'] = content_type
    mime = color_formatter.get_lexer_for_body(content_type, response.content)
    assert 'json' in mime.aliases
    content_type = 'text/html'
    response = Response()
    response.headers['content-type'] = content_type
    mime = color_formatter.get_lexer_for_body(content_type, response.content)
    assert 'html' in mime.aliases

# Generated at 2022-06-13 21:53:43.103605
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter

# Generated at 2022-06-13 21:53:55.522444
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    '''testing headers and status lines'''
    header_text='GET / HTTP/1.1\nHost: www.baidu.com\nUser-Agent: httpie/0.8.3\nAccept-Encoding: gzip, deflate\nAccept: */*\nConnection: keep-alive\n\n'
    s=SimplifiedHTTPLexer()
    assert s.get_tokens(header_text)[-1][0] in [pygments.token.Text,pygments.token.Token]


# Generated at 2022-06-13 21:53:57.025954
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style = ColorFormatter.get_style_class('solarized')
    assert style == Solarized256Style

# Generated at 2022-06-13 21:53:57.939859
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:54:04.832479
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class TestStyle(pygments.style.Style):
        pass
    assert ColorFormatter.get_style_class('test') == TestStyle

# Generated at 2022-06-13 21:54:10.268240
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer(mime='application/json') is not None
    assert get_lexer(mime='application/problem+json') is not None
    assert get_lexer(mime='application/something.json') is not None

# Generated at 2022-06-13 21:54:20.627393
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.output.streams import get_log_stream, get_output_stream
    from httpie.input import ParseError

    env = Environment()
    formatter = ColorFormatter(
        env,
        explicit_json=True,
        color_scheme=DEFAULT_STYLE,
        log_stream=get_log_stream(env, is_terminal=True),
        stdout=get_output_stream(env, is_terminal=True),
        stderr=get_output_stream(env, is_terminal=True),
    )

# Generated at 2022-06-13 21:54:30.500597
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie import ExitStatus
    from httpie.compat import urlopen
    from httpie.context import Environment
    from httpie.plugins import FormatterPluginManager

    class FakeEnvironment(Environment):
        colors = 256

    fpm = FormatterPluginManager()
    cf = ColorFormatter(FakeEnvironment, fpm)
    response = urlopen("http://httpbin.org/get")
    mime = response.info().get_content_type()
    body = response.read().decode()
    assert body is not None
    assert cf.get_lexer_for_body(mime, body) is not None

# Generated at 2022-06-13 21:54:38.667883
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    colorFormatter = ColorFormatter(Environment({'colors': True}))
    assert(isinstance(colorFormatter.formatter, TerminalFormatter) or isinstance(colorFormatter.formatter, Terminal256Formatter))
    assert(isinstance(colorFormatter.http_lexer, SimplifiedHTTPLexer) or isinstance(colorFormatter.http_lexer, PygmentsHttpLexer))

# Generated at 2022-06-13 21:54:42.510183
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    styles = AVAILABLE_STYLES
    for color_scheme in styles:
        formatter = ColorFormatter(None, None, color_scheme)
        style = formatter.get_style_class(color_scheme)
        assert style

# Generated at 2022-06-13 21:54:53.770334
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.context import Environment
    e = Environment()
    assert ColorFormatter(env=e,explicit_json=False,color_scheme=DEFAULT_STYLE).__dict__['explicit_json']==False
    assert ColorFormatter(env=e,explicit_json=False,color_scheme=DEFAULT_STYLE).__dict__['color_scheme']==DEFAULT_STYLE
    assert ColorFormatter(env=e, explicit_json=False, color_scheme=DEFAULT_STYLE).__dict__['enabled']==True
    e.colors = False
    assert ColorFormatter(env=e, explicit_json=False, color_scheme=DEFAULT_STYLE).__dict__['enabled'] == False


# Generated at 2022-06-13 21:55:02.664435
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class ColorFormatterMock(ColorFormatter):
        def get_lexer_for_body(
            self, mime: str,
            body: str
        ) -> Optional[Type[Lexer]]:
            return get_lexer(
                mime=mime,
                explicit_json=self.explicit_json,
                body=body,
            )

    mime = 'application/json'
    body = '{"name":"value"}'
    env = Environment()
    env.colors = True
    formatter = ColorFormatterMock(env)
    assert formatter.format_body(body, mime)

# Generated at 2022-06-13 21:55:07.569552
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer
    assert lexer.tokens
    assert lexer.tokens['root']

if __name__ == '__main__':
    test_SimplifiedHTTPLexer()

# Generated at 2022-06-13 21:55:16.232921
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import textwrap

    formatter = ColorFormatter(
        env=Environment(colors=256),
        color_scheme='solarized'
    )
    assert formatter.formatter
    assert formatter.http_lexer
    headers = textwrap.dedent("""\
        GET / HTTP/1.1
        Host: localhost:8080
        User-Agent: HTTPie/0.9.9
        Accept: */*
    """)

# Generated at 2022-06-13 21:55:24.561439
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(DEFAULT_STYLE)
    assert ColorFormatter.get_style_class(DEFAULT_STYLE) == pygments.styles.get_style_by_name(DEFAULT_STYLE)
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:55:26.969737
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == \
        Solarized256Style

# Generated at 2022-06-13 21:55:30.365127
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # Assert that the solarized 256 style can also be retrieved by its name
    assert ColorFormatter.get_style_class('solarized256') == Solarized256Style

# Generated at 2022-06-13 21:55:42.207977
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie import ExitStatus
    from httpie.config import Environment
    from httpie.plugins import BuiltinPluginManager

    env = Environment(colors=256)
    pm = BuiltinPluginManager()
    pm.load_builtin_plugins()
    headers_processor = pm.instantiate(
        name='color',
        klass=ColorFormatter,
        env=env
    )

    headers = '''\
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 15
Server: Werkzeug/0.11.11 Python/2.7.13'''
    headers_colored = headers_processor.format_headers(headers)
    assert '\x1b[1;30;43m' in headers_colored  # Header name

# Generated at 2022-06-13 21:55:55.932620
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment
    from httpie.plugins import plugin_manager
    from httpie.output.streams import FileStream

    env = Environment(stdin=None, stdout=FileStream('stdout'),
                      stderr=FileStream('stderr'),
                      style=DEFAULT_STYLE, colors=256,
                      extensions=[], output_options=[])

    formatter = plugin_manager.get_formatter('colors', env)
    assert formatter.format_body(
        '    <html><body>Hello</body></html>',
        'text/html'
    ) == '    <html><body>Hello</body></html>'

# Generated at 2022-06-13 21:56:03.771017
# Unit test for function get_lexer
def test_get_lexer():
    # type: () -> None
    from httpie.input import Parser
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.builtin import HTTPHeadersPlugin

    p = Parser()
    p.env.stdout.isatty = lambda: True
    p.env.colors = True
    p.env.colors_force = True
    p.env.prettifier_enabled.append('colors')
    p.env.prettifier_enabled.append(
        'prettifier'
    )  # to ensure that colors isn't disabled by the prettifier

    f = FormatterPlugin(env=p.env)
    f.enabled = True

    h = HTTPHeadersPlugin(parser=p)
    h.enabled = True


# Generated at 2022-06-13 21:56:14.473392
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    color_formatter = ColorFormatter(
        env=Environment(),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
        **{}
    )
    # 1st case: no json in mime
    #   1.1 no json in subtype
    mime = "application/xml"
    body = '{"widget": {"debug": "on", "window": {"title": "Sample Konfabulator Widget", "name": "main_window", "width": 500, "height": 500}, "text": {"data": "Click Here", "size": 36, "style": "bold", "name": "text1", "hOffset": 250, "vOffset": 100, "alignment": "center", "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"}}}'

# Generated at 2022-06-13 21:56:18.271059
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    _ = ColorFormatter(
        env=Environment(colors=True, stream=None),
        explicit_json=False,
        color_scheme='solarized',
    )

# Generated at 2022-06-13 21:56:30.650179
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class TestColorFormatter(ColorFormatter):
        def get_lexer_for_body(self, mime: str, body: str) -> Optional[Type[Lexer]]:
            return get_lexer(
                mime=mime,
                explicit_json=self.explicit_json,
                body=body,
            )

    # Test good case format body
    cf = TestColorFormatter(Environment(), color_scheme=DEFAULT_STYLE)
    assert "\x1b[38;5;45m{\x1b[39m\x1b[38;5;45m" in cf.format_body('{"test": true}', 'application/json')

    # Test bad case
    cf = TestColorFormatter(Environment(), color_scheme=DEFAULT_STYLE)

# Generated at 2022-06-13 21:56:32.235265
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color = ColorFormatter(None)

# Generated at 2022-06-13 21:56:52.250209
# Unit test for method format_headers of class ColorFormatter

# Generated at 2022-06-13 21:56:53.625845
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    expected = Solarized256Style
    result = ColorFormatter.get_style_class('solarized')
    assert (result == expected)

# Generated at 2022-06-13 21:57:04.321261
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    from pygments.token import Token
    from tests.compat import unittest
    from tests.constants import (
        UNICODE_GREEK_REQUEST_HEADER_JSON,
        UNICODE_GREEK_REQUEST_HEADER_FORM,
        UNICODE_GREEK_REQUEST_HEADER_URLENCODED,
        UNICODE_GREEK_RESPONSE_HEADER_JSON,
        UNICODE_GREEK_RESPONSE_HEADER_HTML,
        UNICODE_GREEK_RESPONSE_HEADER_XML,
        UNICODE_GREEK_RESPONSE_HEADER_URLENCODED,
        UNICODE_GREEK_HEADER_VALUE_BASIC_AUTH_URL,
    )


# Generated at 2022-06-13 21:57:19.581674
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import re
    import pytest
    env = Environment()
    formatter = ColorFormatter(env)
    assert formatter.is_enabled() == True
    text = formatter.format_headers('GET / HTTP/1.1\nHost: example.com\n')
    assert text == '\x1b[34;1mGET \x1b[0m/\x1b[33;1m \x1b[0m\x1b[1mHTTP/1.1\x1b[0m\n\x1b[34;1mHost\x1b[0m: \x1b[36;1mexample.com\x1b[0m\n'

# Generated at 2022-06-13 21:57:27.693877
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']
    tokens = lexer.get_tokens('GET /users/1 HTTP/1.1')
    assert tokens[0][0] == pygments.token.Name.Function
    assert tokens[0][1] == 'GET'
    assert tokens[1][0] == pygments.token.Text
    assert tokens[1][1] == ' '
    assert tokens[2][0] == pygments.token.Name.Namespace
    assert tokens[2][1] == '/users/1'
    assert tokens[3][0] == pygments.token.Text
    assert tokens[3][1] == ' '

# Generated at 2022-06-13 21:57:28.824680
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert(ColorFormatter)

# Generated at 2022-06-13 21:57:40.468947
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.output.pretty import FormattedResponse
    from httpie.plugins import FormatterPlugin
    from httpie.plugins import color

    class MyColorFormatter(ColorFormatter):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.json = False
            self.explicit_json = False

        def format_body(self, body: str, mime: str) -> str:
            return body

    def print_get_lexer_for_body(mime: str, body: str) -> None:
        print('-' * 80)
        print('mime:', mime)
        print('body:', body)
        # httpie.plugins.color.ColorFormatter.get_lexer_for_body
        lexer = formatter

# Generated at 2022-06-13 21:57:47.934495
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    """
    Test method format_headers, it must return a string.
    """

    def inner_test(env_colors):
        """
        Test method format_headers in different cases by creating an
        :class:`httpie.context.Environment` for each case.
        """
        color_formatter = ColorFormatter(
            Environment(colors=env_colors, stdout_isatty=True, stdin_isatty=True)
        )
        assert isinstance(color_formatter.format_headers("foo: bar"), str)

    inner_test(False)
    inner_test(True)

# Generated at 2022-06-13 21:57:58.814116
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    env = Environment()
    env.colors = True
    color_formatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    body = """{
    "id": 1,
    "name": "A green door",
    "price": 12.50,
    "tags": ["home", "green"]
}"""
    assert color_formatter.format_body(body, 'application/json')
    # Error case
    assert color_formatter.format_body(body, 'text/plain')

# Generated at 2022-06-13 21:58:01.005454
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter = ColorFormatter(Environment())
    assert formatter.formatter.__class__ == TerminalFormatter

# Generated at 2022-06-13 21:58:32.781904
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.clients.http import _parse_mime_type
    from responses import Response

    assert _parse_mime_type('text/html') == ('text', 'html', {})

    def _test_mime_and_body(mime, body, lexer=None):
        formatter = ColorFormatter(None)
        expected_lexer = get_lexer(mime, body=body)
        if not expected_lexer:
            expected_lexer = SimplifiedHTTPLexer
        actual_lexer = get_lexer(mime, body=body, explicit_json=True)
        if not actual_lexer:
            actual_lexer = SimplifiedHTTPLexer
        assert formatter.get_lexer_for_body(mime, body) == lexer or expected_lexer

# Generated at 2022-06-13 21:58:35.384178
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    print("Testing SimplifiedHTTPLexer")
    _ = SimplifiedHTTPLexer()
    print("Using SimplifiedHTTPLexer")

# Generated at 2022-06-13 21:58:39.254970
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('fruity') == pygments.styles.get_style_by_name('fruity')
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:58:49.178261
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.compat import is_windows
    from httpie.output.streams import ColorizedStdout
    from httpie.output.streams import UncolorizedStdout

    # this part is about testing a static class.

    # class ColorFormatter(FormatterPlugin):
    #     """
    #     Colorize using Pygments
    #
    #     This processor that applies syntax highlighting to the headers,
    #     and also to the body if its content type is recognized.
    #
    #     """
    #     group_name = 'colors'
    #
    #     def __init__(
    #         self,
    #         env: Environment,
    #         explicit_json=False,
    #         color_scheme=DEFAULT_STYLE,
    #         **kwargs
    #     ):

# Generated at 2022-06-13 21:58:55.342799
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # ColorFormatter.get_style_class(solarized) -> Solarized256Style
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style

    # ColorFormatter.get_style_class(auto) -> Solarized256Style
    assert ColorFormatter.get_style_class(AUTO_STYLE) == Solarized256Style

    # ColorFormatter.get_style_class(invalid) -> Solarized256Style
    try:
        ColorFormatter.get_style_class('')
        assert False
    except ClassNotFound:
        assert True

# Generated at 2022-06-13 21:59:06.554025
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    formatter = ColorFormatter(
        Environment(colors=256),
        color_scheme="solarized256",
        **{}
    )
    c_formatter = ColorFormatter(
        Environment(colors=True),
        color_scheme="solarized256",
        **{}
    )

# Generated at 2022-06-13 21:59:18.003516
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # Given
    color_formatter = ColorFormatter

    # When
    lexer_1 = color_formatter.get_lexer_for_body(color_formatter, 'text/xml', '<test/>')
    lexer_2 = color_formatter.get_lexer_for_body(color_formatter, 'text/plain', 'test')
    lexer_3 = color_formatter.get_lexer_for_body(color_formatter, 'text/plain', '{"test"}')
    lexer_4 = color_formatter.get_lexer_for_body(color_formatter, 'text/plain', '{"test": ')
    lexer_5 = color_formatter.get_lexer_for_body(color_formatter, 'application/json', '{"test": ')

   

# Generated at 2022-06-13 21:59:29.634621
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.context import Environment
    # * 0 *
    formatter = ColorFormatter(Environment(colors=False))
    assert formatter.get_lexer_for_body('text/plain', '') is None
    # * 1 *
    formatter = ColorFormatter(Environment(colors=True))
    assert formatter.get_lexer_for_body('text/plain', '') is TextLexer
    # * 2 *
    formatter = ColorFormatter(Environment(colors=True))
    assert formatter.get_lexer_for_body('application/xml', '<html>') is None
    # * 3 *
    formatter = ColorFormatter(Environment(colors=True), explicit_json=True)

# Generated at 2022-06-13 21:59:41.932248
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    assert ColorFormatter.get_lexer_for_body(
        'application/json', ''
    ) == pygments.lexers.get_lexer_by_name('JSON')

    assert ColorFormatter.get_lexer_for_body(
        'application/octet-stream', ''
    ) is None

    assert ColorFormatter.get_lexer_for_body(
        'application/xml', ''
    ) == pygments.lexers.get_lexer_by_name('XML')

    assert ColorFormatter.get_lexer_for_body(
        'text/html', ''
    ) == pygments.lexers.get_lexer_by_name('HTML')


# Generated at 2022-06-13 21:59:44.298052
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert 'FormatterPlugin' in str(SimplifiedHTTPLexer)

# Generated at 2022-06-13 22:00:30.170032
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.compat import is_windows
    from httpie.context import Environment
    from httpie.plugins.colors import ColorFormatter

    env = Environment(is_windows=is_windows)
    cf = ColorFormatter(env)

    assert cf.get_lexer_for_body('text/plain') is None
    assert isinstance(cf.get_lexer_for_body('application/json'), pygments.lexers.JsonLexer)
    assert isinstance(cf.get_lexer_for_body('application/javascript'), pygments.lexers.JavascriptLexer)
    assert isinstance(cf.get_lexer_for_body('text/html; charset=utf-8'), pygments.lexers.HtmlLexer)

# Generated at 2022-06-13 22:00:35.031057
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    color_formatter = ColorFormatter()
    css_lexer = pygments.lexers.get_lexer_by_name('css')

    assert color_formatter.format_body('h1 {color: blue', 'text/css') == pygments.highlight(
                code='h1 {color: blue',
                lexer=css_lexer,
                formatter=color_formatter.formatter
            )

# Generated at 2022-06-13 22:00:48.253541
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.core import main

    env = main.Environment(colors=256)
    color_formatter = ColorFormatter(env, color_scheme=SOLARIZED_STYLE)
    color_formatter.reset()

    headers = '''\
HTTP/1.1 200 OK
Server: nginx
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive
Vary: Origin
Vary: X-HTTP-Method-Override
Access-Control-Allow-Origin: *
Cache-Control: no-cache
Date: Mon, 10 Aug 2015 21:40:56 GMT
X-Frame-Options: SAMEORIGIN

'''

    colorized = color_formatter.format_headers(headers)


# Generated at 2022-06-13 22:00:59.545192
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    class NullEnvironment:
        colors = True
    color_formatter = ColorFormatter(env=NullEnvironment())

# Generated at 2022-06-13 22:01:01.726323
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(color_scheme='solarized') == Solarized256Style

# Generated at 2022-06-13 22:01:09.613175
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    formatter_class = ColorFormatter.get_style_class('solarized')
    assert formatter_class._name == 'Solarized256Style'
    formatter_class = ColorFormatter.get_style_class('fruity')
    assert formatter_class._name == 'Fruity'
    formatter_class = ColorFormatter.get_style_class(AUTO_STYLE)
    assert formatter_class._name == 'Fruity'


# Generated at 2022-06-13 22:01:17.182283
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.input import ParseError
    from requests.compat import str
    class Lexer:
        def __init__(self, source):
            self._source = source
        def get_tokens_unprocessed(self, source):
            return [(source, None)]
    input_json_str = """\
[
  {
    "field1": "value1"
  }
]
"""
    input_non_json_str = ''.join([str(i) for i in range(10)])
    class MockEnvironment:
        def __init__(self, colors):
            self.colors = colors
    class MockFormatter:
        def __init__(self, enabled, formatter):
            self.enabled = enabled
            self.formatter = formatter