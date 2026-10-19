

# Generated at 2022-06-13 21:51:23.068558
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized256') == Solarized256Style

# Generated at 2022-06-13 21:51:30.077567
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class MockRequest:
        method = "GET"
        scheme = "http"
        host = "httpbin.org"
        path = "/"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json"
        }
    request = MockRequest()
    formatter = ColorFormatter()
    assert formatter.format_body(body='', mime='application/json') == '\n'



# Generated at 2022-06-13 21:51:33.489602
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class("solarized256") == Solarized256Style
    assert ColorFormatter.get_style_class("solarized") == Solarized256Style

# Generated at 2022-06-13 21:51:42.796948
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import pygments
    class MockLexer(pygments.lexer.RegexLexer):
        name = 'HTTP'
        aliases = ['http']
        filenames = ['*.http']

# Generated at 2022-06-13 21:51:45.557692
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('test') == 'test'
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style

# Generated at 2022-06-13 21:51:54.469582
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    assert ColorFormatter(None, None, None).format_body(
        '{',
        'application/json'
    ) == '\x1b[38;5;196m{\x1b[39m'

    assert ColorFormatter(None, None, None).format_body(
        '<!DOCTYPE html>',
        'text/html'
    ) == '<!DOCTYPE html>'

    assert ColorFormatter(None, None, None).format_body(
        '<!DOCTYPE html>',
        'text/html-html'
    ) == '\x1b[38;5;196m<!DOCTYPE html>\x1b[39m'


# Generated at 2022-06-13 21:52:04.157825
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # type: () -> None
    env = Environment(colors=256)
    color = ColorFormatter(env)

    # Test values from RFC2616
    mime = 'text/plain'
    body = ''
    assert isinstance(
        color.get_lexer_for_body(mime=mime, body=body),
        pygments.lexers.TextLexer
    )

    mime = 'text/plain; charset=ISO-8859-4'
    body = ''
    assert isinstance(
        color.get_lexer_for_body(mime=mime, body=body),
        pygments.lexers.TextLexer
    )

    mime = 'text/html'
    body = ''

# Generated at 2022-06-13 21:52:10.593357
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    response_status_line = 'HTTP/1.1 200 OK'
    response_status_line_parts = lexer.get_tokens(response_status_line)
    assert response_status_line_parts == [(pygments.token.Keyword.Reserved, 'HTTP'),
                                          (pygments.token.Operator, '/'),
                                          (pygments.token.Number, '1.1'),
                                          (pygments.token.Text, ' '),
                                          (pygments.token.Number, '200'),
                                          (pygments.token.Text, ' '),
                                          (pygments.token.Name.Exception, 'OK')]

# Generated at 2022-06-13 21:52:14.075131
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    """Unit test for method get_style_class of class ColorFormatter."""
    assert ColorFormatter.get_style_class("solarized")

# Generated at 2022-06-13 21:52:23.856218
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.compat import is_windows
    from httpie import __version__ as httpie_version
    from httpie.cli.color import ColorFormatter

    # Create formatter
    env = Environment(colors=True)
    formatter = ColorFormatter(env=env)
    # Set up environment
    if is_windows:
        # Colors on Windows via colorama don't look that
        # great and fruity seems to give the best result there.
        color_scheme = 'fruity'
    else:
        color_scheme = 'solarized'

    if httpie_version > '1.0.0':
        formatter.color_scheme = color_scheme
    else:
        formatter.color_scheme = color_scheme.replace('-', '_')
    formatter.init_

# Generated at 2022-06-13 21:52:30.607197
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    print("Testing class constructor of class ColorFormatter.\n")
    env = Environment()
    ColorFormatter(env, False, "solarized")

# Generated at 2022-06-13 21:52:35.082251
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    lexer.get_tokens('GET / HTTP/1.1')
    lexer.get_tokens('HTTP/1.1 200 OK')
    lexer.get_tokens('Cache-Control: no-cache')
    return

__all__ = (
    'ColorFormatter',
    'Solarized256Style',
)

# Generated at 2022-06-13 21:52:37.290998
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    ColorFormatter.get_lexer_for_body('application/json', '{}')

# Generated at 2022-06-13 21:52:46.257211
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():

    import pygments.lexers
    import pygments.token
    import unittest
    import pygments.lexers.text

    print(pygments.lexers.text)

    l = SimplifiedHTTPLexer(mimetypes=['text/html'])

# Generated at 2022-06-13 21:52:59.315500
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    def get_style_by_name(name):
        return pygments.styles.get_style_by_name(name)

    # OK
    assert ColorFormatter.get_style_class('fruity') is get_style_by_name('fruity')
    assert ColorFormatter.get_style_class('solarized') is get_style_by_name('solarized')
    assert ColorFormatter.get_style_class('fruity') is get_style_by_name('fruity')
    assert ColorFormatter.get_style_class('solarized') is get_style_by_name('solarized')
    # Does not exist
    assert ColorFormatter.get_style_class('nonexistent') is Solarized256Style
    # Invalid

# Generated at 2022-06-13 21:53:10.057701
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    obj = SimplifiedHTTPLexer()
    assert obj.name == 'HTTP'
    assert obj.aliases == ['http']
    assert obj.filenames == ['*.http']
    token_key = list(obj.tokens.keys())[0]
    assert token_key == 'root'
    token_value = obj.tokens.get(token_key)

# Generated at 2022-06-13 21:53:19.325294
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2022-06-13 21:53:26.192276
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('foo/bar') is None
    assert get_lexer('application/json') is not None
    assert get_lexer('application/json', body='{"foo": "bar"}') is not None
    assert get_lexer('application/json-rpc', body='{"foo": "bar"}') is not None

# Generated at 2022-06-13 21:53:28.232175
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) is Solarized256Style

# Generated at 2022-06-13 21:53:30.164834
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert len(SimplifiedHTTPLexer().tokens) > 0

# Generated at 2022-06-13 21:53:47.562150
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    color_formater = ColorFormatter(Environment(), False, 'auto', group_name='colors')
    if(color_formater.get_lexer_for_body('text/html', '<html>\n<body>\n<h1>\nHello world!\n</h1>\n</body>\n</html>\n') is None):
        assert False
    else:
        assert True

# Generated at 2022-06-13 21:53:48.887179
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter(Environment(), False, None)

# Generated at 2022-06-13 21:53:50.228733
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    colorformatter = ColorFormatter()
    assert colorformatter.enabled

# Generated at 2022-06-13 21:54:00.260531
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    cf = ColorFormatter()

# Generated at 2022-06-13 21:54:03.027217
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('mystyle') == None
    assert ColorFormatter.get_style_class('fruity') is not None
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) is not None

# Generated at 2022-06-13 21:54:09.511871
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    from pygments.formatters.terminal import TerminalFormatter
    from httpie.plugins.colors import Solarized256Style
    lexer = SimplifiedHTTPLexer()

# Generated at 2022-06-13 21:54:15.083029
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(color_scheme=AUTO_STYLE) is None
    assert ColorFormatter.get_style_class(color_scheme=SOLARIZED_STYLE) == Solarized256Style
    assert ColorFormatter.get_style_class(color_scheme='monokai') is pygments.styles.MonokaiStyle

# Generated at 2022-06-13 21:54:16.578220
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized256') == Solarized256Style

# Generated at 2022-06-13 21:54:25.199156
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    #
    # HTTP headers
    #
    formatter = ColorFormatter(None)  # type: ignore
    assert formatter.get_lexer_for_body('', '') is None

    #
    # HTML
    #
    assert (
        formatter.get_lexer_for_body('text/html', '') ==
        pygments.lexers.get_lexer_by_name('html')
    )
    assert (
        formatter.get_lexer_for_body('text/html', '<p>') ==
        pygments.lexers.get_lexer_by_name('html')
    )

# Generated at 2022-06-13 21:54:31.058162
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    class Env(object):
        colors = True

    fmt = ColorFormatter(env=Env(), explicit_json=False, color_scheme=AUTO_STYLE)
    assert fmt.explicit_json is False
    assert fmt.http_lexer is not None
    assert fmt.formatter is not None
    assert fmt.enabled



# Generated at 2022-06-13 21:54:38.927160
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    print("==> test_ColorFormatter()")
    try:
        formatter = ColorFormatter(Environment(colors=True))
    except Exception as err:
        print("ERROR: Exception: {}".format(err))
        assert False



# Generated at 2022-06-13 21:54:48.560971
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import httpie.formatter
    import httpie.output
    import httpie.utils
    import httpie.cli
    output_file = httpie.output.get_output_stream(
        redirect_stdout=True,
        stdout_isatty=True,
        output_file=None,
        force_stream=True,
        is_terminal=lambda: True
    )
    formatter = httpie.formatter.get_formatter(
        formatter_name='colors',
        output_options=httpie.cli.Environment(colors=256, versus=False)
    )()
    fmt_headers = formatter.format_headers
    httpie.utils.set_environ(HTTPIE_COLORS='256')

# Generated at 2022-06-13 21:55:02.956240
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import sys
    import unittest
    
    # Blame Python 3.5 for this
    # https://stackoverflow.com/questions/2267362/how-do-i-use-unittest-mock-to-patch-an-import
    sys.modules['termcolor'] = mock.MagicMock()
    class Environment():
        colors = True

    env = Environment()
    lexer = SimplifiedHTTPLexer()
    formatter = TerminalFormatter()
    color_formatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)

    class TestCase(unittest.TestCase):
        def test_jpeg_body(self):
            image_file = open("blah.jpg", "rb")
            image_data = image_file.read

# Generated at 2022-06-13 21:55:13.559067
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import httpie
    from httpie.core import main
    from httpie.compat import urlopen

    # TODO: for some reason the response is missing the Date header
    # when run from a unittest so we must omit it from the expected result
    # or the test will fail.
    r = urlopen('https://httpbin.org/headers')
    assert r.headers['date']

    class _FakeStdOut:
        def __init__(self):
            self.output = []

        def write(self, s):
            self.output.append(s)

        def __str__(self):
            return ''.join(self.output)

    args = ['-v', 'GET', 'https://httpbin.org/headers']
    env = httpie.Environment()
    stdout = _FakeStdOut()


# Generated at 2022-06-13 21:55:24.039311
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from requests_mock import Mocker
    from httpie.cli import parser

    Environment.colors = 256
    args = parser.parse_args(['--style', 'solarized'])
    filter_ = ColorFormatter(
        env=args.env,
        explicit_json=args.explicit_json,
        color_scheme=args.style,
    )
    mocker = Mocker()
    response = mocker.get('http://httpbin.org/headers')
    response.status_code = 200
    response.reason = 'OK'
    response.headers['Content-Type'] = 'application/json'

    filter_.format_headers(response.headers)

# Generated at 2022-06-13 21:55:34.312541
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.plugins.colors import ColorFormatter
    from pygments.styles.default import DefaultStyle
    from pygments.styles.solarized import SolarizedStyle
    from httpie.plugins.colors import Solarized256Style

    assert ColorFormatter.get_style_class("solarized") == SolarizedStyle
    assert ColorFormatter.get_style_class("solarized256") == Solarized256Style
    assert ColorFormatter.get_style_class("default") == DefaultStyle
    assert ColorFormatter.get_style_class("foo") == DefaultStyle

# Generated at 2022-06-13 21:55:40.394921
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class MockEnvironment:
        def __init__(self, colors):
            self.colors = colors
    env = MockEnvironment(256)
    formatter = ColorFormatter(env, True, "solarized")
    assert str(formatter.get_style_class("solarized")) == \
        "<class 'httpie.output.formatters.Solarized256Style'>"

# Generated at 2022-06-13 21:55:44.574012
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('default') == pygments.styles.get_style_by_name('default')
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style
    assert ColorFormatter.get_style_class('auto') == pygments.styles.get_style_by_name('default')

# Generated at 2022-06-13 21:55:51.594486
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    # Request-Line
    assert lexer.get_tokens('GET / HTTP/2.0')[0][0] == pygments.token.Name.Function
    assert lexer.get_tokens('GET / HTTP/2.0')[1][0] == pygments.token.Text
    assert lexer.get_tokens('GET / HTTP/2.0')[2][0] == pygments.token.Name.Namespace
    assert lexer.get_tokens('GET / HTTP/2.0')[3][0] == pygments.token.Text
    assert next(lexer.get_tokens('GET / HTTP/2.0'))[0] == pygments.token.Keyword.Reserved
    assert lexer.get_tokens

# Generated at 2022-06-13 21:56:00.833503
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import sys
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    headers = '''HTTP/1.1 200 OK
    Server: nginx/1.14.1
    Date: Sat, 27 Oct 2018 01:47:31 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 28
    Connection: keep-alive
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Credentials: true'''
    env = Environment()
    env.colors = 256
    color_scheme = 'solarized'
    plugin = ColorFormatter(env,color_scheme=color_scheme)
    color_headers = plugin.format_headers(headers)
    print(color_headers)

# Generated at 2022-06-13 21:56:23.565950
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import os
    os.environ['COLORTERM'] ='truecolor'
    os.environ['HUE_USE_256'] = 'true'
    os.environ['LS_COLORS'] = 'di=0;35:ln=0;36'
    os.environ['LSCOLORS'] = 'di=0;35:ln=0;36'
    os.environ['HUE_COLOR_SOLARIZED'] = 'false'
    os.environ['HUE_USE_XTERM256'] = 'false'
    os.environ['HUE_USE_SEPARATOR_256'] = 'true'
    os.environ['HUE_TERM_FORMAT'] = 'true'
    from httpie.context import Environment
    env = Environment()
    orig_colors = env.col

# Generated at 2022-06-13 21:56:26.305038
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    class MockLexer(SimplifiedHTTPLexer):
        pass
    lexer = MockLexer()
    assert lexer is not None

# Generated at 2022-06-13 21:56:27.573767
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter
    assert ColorFormatter(None)

# Generated at 2022-06-13 21:56:28.901943
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    ColorFormatter(env=env)

# Generated at 2022-06-13 21:56:44.005429
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(stdin=None, stdout=None,
                      stdout_isatty=None, stderr=None,
                      stderr_isatty=None)
    env.colors = 256
    assert ColorFormatter(env, color_scheme=AUTO_STYLE, explicit_json=True)
    assert ColorFormatter(env, color_scheme=SOLARIZED_STYLE, explicit_json=True)
    assert ColorFormatter(env, color_scheme=DEFAULT_STYLE, explicit_json=True)
    assert ColorFormatter(env, color_scheme=None, explicit_json=True)
    assert ColorFormatter(env, color_scheme='monokai', explicit_json=True)

# Generated at 2022-06-13 21:56:48.526414
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert isinstance(SimplifiedHTTPLexer(), pygments.lexer.RegexLexer)


__all__ = [
    'ColorFormatter',
    'SOLARIZED_STYLE',
]

# Generated at 2022-06-13 21:56:55.576077
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import pytest

    # Define color formatter with environment
    env = Environment(colors=True)
    color_formatter = ColorFormatter(env)
    # Run tests
    assert color_formatter.format_headers("Test") is None
    assert color_formatter.format_body("Test", "Test") is not None



# Generated at 2022-06-13 21:57:06.187065
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.output.streams import get_file_stream

    class FakeFormatter(ColorFormatter):
        """
        A subclass of ColorFormatter to override stream and environment members
        """

        def __init__(self):
            super(FakeFormatter, self).__init__(
                stream=get_file_stream('stderr'),
                env=Environment(),
            )

    formatter = FakeFormatter()

    def format_body_helper(body: str, mime: str) -> str:
        """
        Returns the formatted body
        """
        return formatter.format_body(body, mime)

    # test text format
    assert format_body_helper("Hello World", "text/plain") == "Hello World"

# Generated at 2022-06-13 21:57:09.361860
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer_1 = SimplifiedHTTPLexer()
    assert lexer_1.__class__.__name__ == 'SimplifiedHTTPLexer'
    assert lexer_1.__class__.__module__ == 'httpie.plugins.colors'

# Generated at 2022-06-13 21:57:15.507867
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import tempfile
    import os
    import re
    import subprocess

    test_string = "text only body"
    test_string_coloured = "\x1b[38;5;181mtext\x1b[39m\x1b[38;5;181m only\x1b[39m\x1b[38;5;181m body\x1b[39m"
    #create a dummy environment

# Generated at 2022-06-13 21:57:43.660653
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.main import parser

    # Sample null text
    null_body = '\x00' * 15

    # Test wrong content type
    class TestColorFormatter(ColorFormatter):
        def __init__(self, mime=None, explicit_json=False):
            self.mime = mime
            self.explicit_json = explicit_json

        def get_lexer_for_body(self, mime, body):
            return get_lexer(mime=self.mime, explicit_json=self.explicit_json, body=body)

    # Test that simple text returns no lexers
    f = TestColorFormatter(mime="text/plain")
    assert f.get_lexer_for_body("text/plain", null_body) is None
    # Test that json returns a json lexer

# Generated at 2022-06-13 21:57:47.172708
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style
    assert ColorFormatter.get_style_class(AUTO_STYLE) == pygments.styles.get_style_by_name('native')

# Generated at 2022-06-13 21:57:53.863605
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import json

    colorFormatter = ColorFormatter(None)
    result = colorFormatter.format_body('200', "application/json")
    assert result == '200'

    result = colorFormatter.format_body('{ "test": "200" }', "application/json")
    assert result == '{\n  \x1b[92m"test"\x1b[39;49;00m\x1b[0m: \x1b[33m"200"\x1b[39;49;00m\x1b[0m\n}\x1b[39;49;00m\x1b[0m'

    result = colorFormatter.format_body('{ "test": "200" }', "json")

# Generated at 2022-06-13 21:58:07.360523
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment()
    env.colors = 256  # force 256 color mode
    formatter = ColorFormatter(env=env)
    headers = '''\
X-header1: value1
X-header2: value2\n\n'''
    assert formatter.format_headers(headers) == '''\
{4}X-header1{0}: value1
{4}X-header2{0}: value2\n\n'''.format(*[Token.UUID[t] for t in [
    Token.LABEL_HEADER,
    Token.SEPARATOR_HEADER,
    Token.VALUE_HEADER,
    Token.NEWLINE,
    Token.EMPTY_LINE
]])

# Generated at 2022-06-13 21:58:08.811619
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    SimplifiedHTTPLexer('test')

# Generated at 2022-06-13 21:58:11.853100
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    print(ColorFormatter.format_body(ColorFormatter, "{\"test\":\"test\"}", "application/json"))



# Generated at 2022-06-13 21:58:14.287216
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    result = ColorFormatter.get_style_class('default')
    assert result == pygments.styles.get_style_by_name('default')

# Generated at 2022-06-13 21:58:24.392324
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    import logging
    import pygments.lexers
    import pygments.lexer
    import pygments.token
    import pygments.util
    import httpie
    import httpie.colors
    logging.basicConfig(level=logging.DEBUG)
    request_line = ("GET /echo?x=1 HTTP/1.1"
                    "Accept: application/json\n"
                    "\n")
    try:
        lexer = pygments.lexers.get_lexer_by_name('http')
        logging.debug("Original lexer for http: %s", lexer)
    except pygments.util.ClassNotFound:
        lexer = httpie.colors.SimplifiedHTTPLexer()
        logging.debug("Original lexer not found. Created %s", lexer)

# Generated at 2022-06-13 21:58:36.357966
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2022-06-13 21:58:44.990600
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    string = "POST /api/users/ HTTP/1.1\n" \
             "Content-Type: application/json\n" \
             "Authorization: Basic XXX\n" \
             "\n" \
             "{\"id\":2,\"name\":\"user2\",\"email\":\"user2@gmail.com\"}\n"
    tokens = list(pygments.lex(string, SimplifiedHTTPLexer()))
    assert len(tokens) == 10 and tokens[0][1] == 'POST' \
           and tokens[4][1] == 'Content-Type' \
           and tokens[7][1] == 'Authorization' and tokens[8][1] == '{'

# Generated at 2022-06-13 21:59:08.074479
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    color_formatter = ColorFormatter(Environment(), False)

    lexer = color_formatter.get_lexer_for_body('application/http-request', '')
    assert isinstance(lexer, SimplifiedHTTPLexer)

    lexer = color_formatter.get_lexer_for_body(
        'application/http-request',
        '{"key": "value"}'
    )
    assert isinstance(lexer, SimplifiedHTTPLexer)

    lexer = color_formatter.get_lexer_for_body(
        'application/http-request',
        '{"key": "value"}',
        explicit_json=True
    )
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    lexer = color_formatter.get_lexer_

# Generated at 2022-06-13 21:59:16.703396
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.cli import Formatter
    import json
    env = Environment()
    color_formatter = ColorFormatter(env)
    color_formatter.enabled = True
    headers = 'HTTP/1.1 200 OK\r\n'
    formatted_headers = color_formatter.format_headers(headers)
    assert formatted_headers == headers
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n'
    formatted_headers = color_formatter.format_headers(headers)
    assert formatted_headers == headers

# Generated at 2022-06-13 21:59:27.972018
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    def test_lexer_token(token, type, value):
        assert token[0] == type
        assert token[1] == value

    env = Environment(colors=256)
    color_formatter = ColorFormatter(env).format_body

    request_line = "GET /index.html HTTP/1.1"
    tokens = SimplifiedHTTPLexer().get_tokens(request_line)
    test_lexer_token(next(tokens), pygments.token.Name.Function, 'GET')
    test_lexer_token(next(tokens), pygments.token.Text, ' ')
    test_lexer_token(next(tokens), pygments.token.Name.Namespace, '/index.html')

# Generated at 2022-06-13 21:59:31.940819
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    assert ColorFormatter.format_body("[]", "application/json") == "\x1b[2J\x1b[H\x1b[36m[\x1b[39m\x1b[36m]\x1b[39m"

# Generated at 2022-06-13 21:59:43.300791
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=True)
    formatter = ColorFormatter(env=env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    headers = """Content-Type: text/html; charset=utf-8
Date: Tue, 04 Jun 2019 14:22:34 GMT
Server: Apache
X-Frame-Options: denied
Content-Length: 110
Connection: close

"""

# Generated at 2022-06-13 21:59:50.833647
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    ColorFormatter(Environment(), color_scheme=AUTO_STYLE)
    ColorFormatter(Environment(), color_scheme='solarized256')
    ColorFormatter(Environment(), color_scheme='solarized256')
    ColorFormatter(Environment(), color_scheme='solarized256')
    ColorFormatter(Environment(), color_scheme='solarized256')
    ColorFormatter(Environment(), color_scheme='solarized256')
    ColorFormatter(Environment(), color_scheme='solarized256')
    ColorFormatter(Environment(), color_scheme='solarized256')

# Generated at 2022-06-13 21:59:58.818582
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    c = ColorFormatter(None)
    assert c.format_headers("GET / HTTP/1.1\r\n") == "\x1b[38;5;28mGET\x1b[0m \x1b[38;5;25m/\x1b[0m \x1b[38;5;28mHTTP\x1b[0m\x1b[38;5;24m/\x1b[0m\x1b[38;5;31m1.1\x1b[0m\r\n"

# Generated at 2022-06-13 22:00:02.138199
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    """Test for method get_style_class of class ColorFormatter"""
    assert ColorFormatter._get_style_class('solarized256') is Solarized256Style

# Generated at 2022-06-13 22:00:13.928763
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2022-06-13 22:00:28.142938
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    # Test case for color formatter for httpie
    headers = ("'Connection': 'keep-alive'\n"
               "'Content-Length': '18'\n"
               "'Content-Type': 'application/json'\n"
               "'Date': 'Wed, 16 Aug 2017 15:30:45 GMT'\n"
               "'Server': 'gunicorn/19.7.1'\n"
               "'Vary': 'Accept, Cookie'\n"
               "'X-Frame-Options': 'SAMEORIGIN'\n"
               "'X-XSS-Protection': '1; mode=block'\n")
    f = ColorFormatter()
    formatted = f.format_headers(headers)
