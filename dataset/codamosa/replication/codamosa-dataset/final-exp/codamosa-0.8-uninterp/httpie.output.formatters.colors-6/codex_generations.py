

# Generated at 2022-06-13 21:51:32.804445
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # Arrange
    # Instantiate ColorFormatter to test it
    color_formatter = ColorFormatter(Environment())
    # Act
    # Assert
    assert color_formatter.format_body('{"key":"a string value"}', 'application/json') == '{\x1b[34m"key"\x1b[39;49;00m:\x1b[33m"a string value"\x1b[39;49;00m}'

# Generated at 2022-06-13 21:51:42.403599
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from collections import OrderedDict
    cformatter = ColorFormatter(Environment(colors=256))
    assert issubclass(type(cformatter.get_lexer_for_body("application/json", "")), pygments.lexers.data.JsonLexer)
    assert issubclass(type(cformatter.get_lexer_for_body("application/json", '{"a":1}')), pygments.lexers.data.JsonLexer)
    assert issubclass(type(cformatter.get_lexer_for_body("application/json", '{"a":')), pygments.lexers.text.TextLexer)

# Generated at 2022-06-13 21:51:44.301244
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(DEFAULT_STYLE) is Solarized256Style

# Generated at 2022-06-13 21:51:53.753713
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    t = ColorFormatter(None)

    # Test for text response
    body = t.format_body('<html>Hello World</html>', 'text/html')
    assert body == '\x1b[39;49;00m<html>Hello World</html>\x1b[39;49;00m'

    # Test for xml response
    body = t.format_body('<html>Hello World</html>', 'application/xml')
    assert body == '\x1b[39;49;00m<html>Hello World</html>\x1b[39;49;00m'

    # Test for json response
    body = t.format_body('{"abc": "def"}', 'text/json')

# Generated at 2022-06-13 21:52:03.753582
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import os
    import sys

    class FakeEnv:
        colors = True

    fake_env = FakeEnv()
    headers = '''HTTP/1.1 200 OK\r
Date: Sun, 05 Apr 2020 09:56:39 GMT\r
Server: Apache\r
Last-Modified: Wed, 28 Nov 2007 01:43:45 GMT\r
ETag: "7f3c3-2a1-90d9b400"\r
Accept-Ranges: bytes\r
Content-Length: 681\r
Connection: close\r
Content-Type: text/html; charset=UTF-8\r
\r'''

    formatter = ColorFormatter(env=fake_env, explicit_json=False, color_scheme='solarized')
    fd = sys.stdout.fileno()
   

# Generated at 2022-06-13 21:52:06.075086
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style_class = ColorFormatter.get_style_class('default')
    assert style_class == pygments.styles.default
    style_class = ColorFormatter.get_style_class('solarized')
    assert style_class == Solarized256Style

# Generated at 2022-06-13 21:52:20.893683
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import sys
    import os
    import json

    # Directory where script is located.
    test_dir = os.path.dirname(os.path.realpath(__file__))

    # Directory where unit tests are located.
    test_case_dir = test_dir + "\\unit_test_case"

    # Setup the environment for testing.
    environment = Environment(colors=256)
    environment.config['style'] = "solarized"
    environment.is_windows = False
    test_cases = os.listdir(test_case_dir)

    # Run unit tests.
    for test_case in test_cases:
        if test_case.endswith(".test_case"):
            sys.stdout.flush()


# Generated at 2022-06-13 21:52:24.171992
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class("solarized") == Solarized256Style

# Generated at 2022-06-13 21:52:29.494245
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style_class = ColorFormatter.get_style_class(SOLARIZED_STYLE)
    assert style_class == Solarized256Style
    style_class = ColorFormatter.get_style_class(DEFAULT_STYLE)
    assert style_class != Solarized256Style
    assert style_class in pygments.styles.get_all_styles()

# Generated at 2022-06-13 21:52:37.357093
# Unit test for method format_headers of class ColorFormatter

# Generated at 2022-06-13 21:52:53.916240
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import httpie.context as c
    env = c.Environment(colors=256, stdout_isatty=True, stdin_isatty=True,
                        output_options=c.DEFAULT_OUTPUT_OPTIONS)
    class FakeOpts(object):
        def __init__(self, explicit_json=False, color_scheme=DEFAULT_STYLE, **kwargs):
            self.explicit_json = explicit_json  # --json
            self.color_scheme = color_scheme
    callargs = {'env': env, 'opts': FakeOpts}
    thing = ColorFormatter(**callargs)
    assert thing.explicit_json == False
    assert thing.formatter.style == pygments.styles.get_style_by_name('default')

# Generated at 2022-06-13 21:53:05.255164
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    raw_headers = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: application/json; charset=utf-8\r\n'
        'Date: Fri, 24 Nov 2017 13:10:30 GMT\r\n'
        'Server: WSGIServer/0.2 CPython/3.6.2\r\n'
        'X-Frame-Options: SAMEORIGIN\r\n'
    )

# Generated at 2022-06-13 21:53:11.015734
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.plugins.colors import ColorFormatter
    from pygments.formatters.terminal256 import Terminal256Formatter
    assert ColorFormatter.get_style_class(AUTO_STYLE) == Terminal256Formatter
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style

# Generated at 2022-06-13 21:53:22.367272
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.core import main as httpie
    from httpie.plugins import builtin

    # An HTTPie command invocation is like a unittest.
    # There are several approaches.

    # Low-level approach:
    #   1. Create an Environment object,
    #   2. Load the plugins,
    #   3. Construct the Arguments and the Command instance.
    #   4. Construct the HTTPie Core Application and invoke it.

    env = Environment()
    plugins = builtin.load(env)
    args = ['-h']
    cmd = httpie.Command(args=args, env=env, plugins=plugins)
    app = httpie.Application(cmd=cmd, env=env, plugins=plugins)
    try:
        app.run()
    except SystemExit as e:
        assert e.code == 0

# Generated at 2022-06-13 21:53:31.646828
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    env = Environment()
    color_formatter = ColorFormatter(env)
    color_formatter.format_headers('GET / HTTP/1.1\r\nHost: www.example.org\r\n\r\n')
    color_formatter.format_headers('HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n')
    color_formatter.format_headers('Content-Type: text/plain\r\n\r\n')

# Generated at 2022-06-13 21:53:39.850794
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']
    assert len(lexer.tokens['root']) == 3
    # Request-Line
    pattern, token_groups = lexer.tokens['root'][0]
    assert pattern == (r'([A-Z]+)( +)([^ ]+)( +)(HTTP)(/)(\d+\.\d+)')
    assert len(token_groups) == 7
    assert pygments.token.Name.Function == token_groups[0]
    assert pygments.token.Text == token_groups[1]
    assert pygments.token.Name.Namespace == token_groups[2]

# Generated at 2022-06-13 21:53:51.237313
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('foo/bar', explicit_json=False) is None
    assert get_lexer('foo/bar+json') == pygments.lexers.get_lexer_by_name('json')
    assert get_lexer('foo/bar+json') == pygments.lexers.get_lexer_by_name('json')
    assert get_lexer('application/json') == pygments.lexers.get_lexer_by_name('json')
    assert get_lexer('application/json', body="{}") == pygments.lexers.get_lexer_by_name('json')
    assert get_lexer('text/plain', body="{}", explicit_json=True) == pygments.lexers.get_lexer_by_name('json')

# Generated at 2022-06-13 21:53:52.142302
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    ColorFormatter()

# Generated at 2022-06-13 21:53:59.375106
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    c = ColorFormatter(None, None, None)
    assert c.format_body("{\"test\":\"ok\"}", "application/json") == (
    "\x1b[38;5;36m{\x1b[39m\x1b[38;5;33m\"test\"\x1b[39m\x1b[38;5;40m:\x1b[39m\x1b[38;5;33m\"ok\"\x1b[39m\x1b[38;5;36m}\x1b[39m")

# Generated at 2022-06-13 21:54:01.063004
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():

    assert ColorFormatter.get_style_class('tango') == pygments.styles.get_style_by_name('tango')



# Generated at 2022-06-13 21:54:20.250672
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import sys
    import logging
    import httpie
    from httpie.config import Config
    from httpie import plugins
    from httpie.main import main
    from httpie.context import Environment
    config = Config(env=Environment.from_env())
    args = httpie.cli.parser.parse_args([])
    log = logging.getLogger()
    env = Environment(
        stdin=sys.stdin,
        stdout=sys.stdout,
        stderr=sys.stderr,
        stdin_isatty=config.isatty,
        output_isatty=config.isatty,
        colors=256,
        config=config,
        args=args,
        log_level=logging.WARNING
    )
    formatter = ColorFormatter(env)

# Generated at 2022-06-13 21:54:31.466775
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.plugins import FormatterPlugin
    from httpie.output.streams import NoOpProgressIndicator

    plugin = ColorFormatter(
        env=Environment(),
        explicit_json=True,
        color_scheme='solarized',
        progress_indicator=NoOpProgressIndicator(),
    )

    headers = "Greeting: hello\r\n\r\n"

    assert plugin.format_headers(headers) == \
        "\x1b[34mGreeting\x1b[39;49m\x1b[37m: \x1b[39;49m\x1b[93mhello" \
        "\x1b[39;49m"



# Generated at 2022-06-13 21:54:35.012371
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class("solarized") == Solarized256Style
    assert ColorFormatter.get_style_class("solarized256") == Solarized256Style

# Generated at 2022-06-13 21:54:38.347295
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class("monokai") == pygments.styles.get_style_by_name("monokai")
    assert ColorFormatter.get_style_class("solarized256") == Solarized256Style

# Generated at 2022-06-13 21:54:43.303612
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter = ColorFormatter(None)
    assert color_formatter.formatter.style_class == Solarized256Style
    assert color_formatter.http_lexer.__class__ == SimplifiedHTTPLexer
    assert color_formatter.enabled is True
    assert color_formatter.explicit_json is False



# Generated at 2022-06-13 21:54:52.020092
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # sample mime-type and body values
    mime = 'text/plain (text/html)'
    body = '<html><body><h1>Hello World!</h1></body></html>'

    # check text/plain mime-type
    lexer = get_lexer(mime='text/plain', body=body)
    assert lexer == None

    # check text/html mime-type
    lexer = get_lexer(mime='text/html', body=body)
    assert lexer == pygments.lexers.get_lexer_by_name('html')

    # check application/json mime-type
    lexer = get_lexer(mime='application/json', body=body)
    assert lexer == None

    # check application/json mime-type with json body
    body

# Generated at 2022-06-13 21:54:54.022218
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style

# Generated at 2022-06-13 21:54:56.976921
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter = ColorFormatter(
        env=Environment(),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )
    assert formatter

# Generated at 2022-06-13 21:55:02.136993
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    # Test for different color schemes
    for color_scheme in [DEFAULT_STYLE, 'pygments', 'fruity']:
        formatter = ColorFormatter('env', color_scheme=color_scheme)
        assert formatter.format_headers('some') == 'some'

# Generated at 2022-06-13 21:55:12.393912
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.utils import get_mime_type, is_json
    import pygments.lexers
    def get_lexer_aliases(lexer):
        if lexer: return sorted(lexer.aliases)
        else: return []
    fakeBody = '''
<html>
<head>
<title>Hello World</title>
</head>
<body>
<h1>Hello World</h1>
</body>
</html>
    '''
    env = Environment(stdout=None, colors=256, style='Solarized')
    formatter = ColorFormatter(env)

    # valid html
    mime = get_mime_type(fakeBody)
    lexer = formatter.get_lexer_for_body(mime, fakeBody)
    assert get_lexer_aliases

# Generated at 2022-06-13 21:55:39.885735
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    lexer = SimplifiedHTTPLexer()
    formatter = Terminal256Formatter(style=Solarized256Style)
    headers = '''GET / HTTP/1.1\r\nHost: httpbin.org\r\nUser-Agent: HTTPie/1.0.2\r\nAccept-Encoding: gzip, deflate\r\nAccept: application/json'''
    headers = pygments.highlight(
        code=headers,
        lexer=lexer,
        formatter=formatter,
    ).strip()


# Generated at 2022-06-13 21:55:48.822039
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.compat import str
    from httpie.output.streams import ColorizedBytesOutputStream
    from httpie.compat import is_py26

    class TestEnv(object):
        def __init__(self):
            self.colors = 256 if is_windows else True
            self.stream = ColorizedBytesOutputStream(b"", is_tty=True)

    env = TestEnv()
    ColorFormatter(env, color_scheme=AUTO_STYLE)


# Generated at 2022-06-13 21:55:59.687084
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()

    request = """GET / HTTP/1.1
Host: www.github.com
User-Agent: HTTPie/0.9.9"""

# Generated at 2022-06-13 21:56:05.581303
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter(Environment(), color_scheme='solarized')
    mime = 'text/css'
    body = '#content { color: #333; }'
    lexer = formatter.get_lexer_for_body(mime, body)
    assert lexer == pygments.lexers.get_lexer_by_name('css')

# Generated at 2022-06-13 21:56:13.219120
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(colors=True)
    http_lexer = SimplifiedHTTPLexer()
    formatter = Terminal256Formatter(
        style=Solarized256Style
    )
    color_formatter = ColorFormatter(env=env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert (http_lexer == color_formatter.http_lexer and
            formatter == color_formatter.formatter)

# Generated at 2022-06-13 21:56:19.900143
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style_class = ColorFormatter.get_style_class('stata-dark')
    assert style_class == pygments.styles.get_style_by_name('stata-dark')
    style_class = ColorFormatter.get_style_class('solarized')
    assert style_class == Solarized256Style
    style_class = ColorFormatter.get_style_class('solarized256')
    assert style_class == Solarized256Style

# Generated at 2022-06-13 21:56:31.288221
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie import Environment
    from httpie.plugins.formatter.colors import ColorFormatter
    from httpie.plugins.formatter import JSONFormatter
    import unittest

    # Build an Environment and Instantiate the ColorFormatter class
    env = Environment()
    formatter = ColorFormatter(env=env, explicit_json=False)

    # Test over different MIMETYPES

# Generated at 2022-06-13 21:56:44.732495
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    ColorFormatter.group_name = 'colors'

# Generated at 2022-06-13 21:56:58.602201
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import pytest
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from httpie.compat import is_windows
    from httpie.plugins import FormatterPlugin
    from httpie.context import Environment
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from httpie.compat import is_windows
    from httpie.plugins import FormatterPlugin
    from httpie.context import Environment
    from httpie.plugins.colors import ColorFormatter, SimplifiedHTTPLexer, Solarized256Style
    class SimplifiedHTTPLexer(pygments.lexer.RegexLexer):
        name = 'HTTP'
        aliases = ['http']
        filenames = ['*.http']

# Generated at 2022-06-13 21:57:08.262695
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    color_formatter = ColorFormatter(
        env=None,
    )
    # test no lexers
    assert color_formatter.get_lexer_for_body(mime='', body='') is None
    # test text/html
    assert isinstance(color_formatter.get_lexer_for_body(mime='text/html', body=''),
                       pygments.lexers.html.HtmlLexer)
    # test application/json
    assert isinstance(color_formatter.get_lexer_for_body(mime='application/json', body=''),
                       pygments.lexers.data.JsonLexer)
    # test application/json+json

# Generated at 2022-06-13 21:57:48.152062
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import main
    from httpie.compat import is_windows

    env = Environment(colors=256, stdin=None, stdout=None, stderr=None)
    args = main.parser.parse_args(args=[], env=env)
    args.colors = DEFAULT_STYLE
    formatter = ColorFormatter(env, args)

    # When color scheme is auto
    if formatter.enabled:
        assert formatter.formatter == Terminal256Formatter(
            style=Solarized256Style
        )

    # When color scheme is solarized256
    args.colors = SOLARIZED_STYLE
    formatter = ColorFormatter(env, args)

# Generated at 2022-06-13 21:58:02.360118
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2022-06-13 21:58:14.856854
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(build_environment(edebug=True))

    mime = 'application/json'
    body = ''
    lexer = formatter.get_lexer_for_body(mime, body)
    assert lexer == pygments.lexers.get_lexer_by_name('json')

    mime = 'application/xml'
    body = ''
    lexer = formatter.get_lexer_for_body(mime, body)
    assert lexer == pygments.lexers.get_lexer_by_name('xml')

    mime = 'text/plain'
    body = '{"foo": "bar"}'
    lexer = formatter.get_lexer_for_body(mime, body)
    assert lexer == pygments.lexers.get_lexer_

# Generated at 2022-06-13 21:58:24.472898
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    tokens_gen = lexer.get_tokens_unprocessed('GET / HTTP/1.1')
    tokens = list(tokens)
    assert len(tokens_gen) == 7
    assert tokens[0][0] == pygments.token.Name.Function
    assert tokens[0][1] == 'GET'
    assert tokens[1][0] == pygments.token.Text
    assert tokens[1][1] == ' '
    assert tokens[2][0] == pygments.token.Name.Namespace
    assert tokens[2][1] == '/'
    assert tokens[3][0] == pygments.token.Text
    assert tokens[3][1] == ' '
    assert tokens[4][0] == pygments.token.Keyword.Res

# Generated at 2022-06-13 21:58:27.181249
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter = ColorFormatter(None)
    assert formatter.formatter is not None
    assert formatter.http_lexer is not None

# Generated at 2022-06-13 21:58:31.536721
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import sys
    from httpie.context import Environment
    env = Environment(stdout=sys.stdout)
    colorFormatter = ColorFormatter(env)
    colorFormatter.format_body("<h1>Hello</h1><p>name</p>", "text/html")

# Generated at 2022-06-13 21:58:39.008172
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.formatters.terminal import TerminalFormatter
    formatter = TerminalFormatter()
    import pygments.lexers
    import pygments.formatters
    import pygments.token
    import pygments
    lexer = pygments.lexers.get_lexer_for_mimetype('text/html')
    response_body = pygments.highlight(
        code='Hi this is html',
        lexer=lexer,
        formatter=formatter,
    )
    print(response_body)

# Generated at 2022-06-13 21:58:50.138008
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=256)
    cf = ColorFormatter(env)

    headers = '''\
Content-Length: 11
Content-Type: text/html; charset=utf-8
Server: Whatever/1.2.3
Set-Cookie: foo=bar
Set-Cookie: baz=qux

'''
    headers_colored = '''\
Content-Length: 11
Content-Type: text/html; charset=utf-8
Server: Whatever/1.2.3
Set-Cookie: foo=bar
Set-Cookie: baz=qux

'''
    assert cf.format_headers(headers) == headers_colored



# Generated at 2022-06-13 21:58:59.325878
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import pygments
    input_data = '''GET / HTTP/1.1\r\n
XIAO-MING: HAPPY\r\n\r\n
'''
    formatter = pygments.formatters.terminal.TerminalFormatter()
    lexer = SimplifiedHTTPLexer()
    result = pygments.highlight(
        code=input_data,
        lexer=lexer,
        formatter=formatter,
    )
    print(result)

# Generated at 2022-06-13 21:59:07.678171
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class MockEnvironment():
        def __init__(self):
            self.colors = 256

    class MockFormatter():
        def __init__(self):
            self.env = MockEnvironment()

    formatter = MockFormatter()
    formatter_with_style = ColorFormatter(formatter.env,
                                          color_scheme='solarized')
    assert formatter_with_style.get_style_class('solarized') == Solarized256Style
    formatter_with_default_style = ColorFormatter(formatter.env)
    assert formatter_with_default_style.get_style_class(DEFAULT_STYLE) == Solarized256Style



# Generated at 2022-06-13 21:59:40.220837
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class ColorFormatterTest(ColorFormatter):
        def get_lexer_for_body(
            self, mime: str,
            body: str
        ) -> Optional[Type[Lexer]]:
            return get_lexer(
                mime=mime,
                explicit_json=self.explicit_json,
                body=body,
            )

    color_formatter_test = ColorFormatterTest(None, False, None)
    assert color_formatter_test.format_body("", "application/json") == ""
    assert color_formatter_test.format_body("", "text/dummy") == ""
    assert color_formatter_test.format_body("", "none/none") == ""

# Generated at 2022-06-13 21:59:46.689042
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter = ColorFormatter(Environment(), False)
    assert (color_formatter.enabled == True)
    assert (color_formatter.formatter is not None)
    assert (color_formatter.http_lexer is not None)



# Generated at 2022-06-13 21:59:50.787797
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter({'colors':True})
    lexer = formatter.get_lexer_for_body(
        mime='application/json',
        body='{}'
    )
    assert lexer == pygments.lexers.get_lexer_by_name('json')

# Generated at 2022-06-13 21:59:52.387490
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class("solarized256") == Solarized256Style

# Generated at 2022-06-13 21:59:56.086501
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    expected = ColorFormatter()
    assert expected.formatter.__class__ == Terminal256Formatter
    assert expected.explicit_json == False

# Generated at 2022-06-13 22:00:07.838551
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    env.colors = True
    cf = ColorFormatter(env, explicit_json=False, color_scheme="default")
    assert isinstance(cf.formatter, TerminalFormatter)
    assert isinstance(cf.http_lexer, pygments.lexers.text.HttpLexer)
    cf = ColorFormatter(env, explicit_json=False, color_scheme="solarized")
    assert isinstance(cf.formatter, Terminal256Formatter)
    assert isinstance(cf.formatter.style, Solarized256Style)
    cf = ColorFormatter(env, explicit_json=False, color_scheme="foo")
    assert isinstance(cf.formatter, Terminal256Formatter)
    assert isinstance(cf.formatter.style, Solarized256Style)

# Generated at 2022-06-13 22:00:10.327553
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']

# Generated at 2022-06-13 22:00:12.653806
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    color_formatter_instance = ColorFormatter(None)
    assert color_formatter_instance.format_headers == '<method ColorFormatter.format_headers>'

# Generated at 2022-06-13 22:00:20.800020
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # Arrange
    color_formatter = ColorFormatter(
        env=None
    )

    # Act
    style_solarized = color_formatter.get_style_class('solarized')
    style_256 = color_formatter.get_style_class('256')

    # Assert
    assert style_solarized == Solarized256Style


# Generated at 2022-06-13 22:00:24.499684
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter = ColorFormatter(None, explicit_json=True, color_scheme='solarized')
    assert formatter.explicit_json == True
    assert formatter.formatter.style == Solarized256Style

# Generated at 2022-06-13 22:00:53.386017
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    env.colors = 256
    color_scheme = 'solarized'
    explicit_json = False
    formatter = ColorFormatter(env=env, explicit_json=explicit_json, color_scheme=color_scheme)
    assert formatter.enabled

    env.colors = False
    formatter = ColorFormatter(env=env, explicit_json=explicit_json, color_scheme=color_scheme)
    assert not formatter.enabled


# Generated at 2022-06-13 22:01:06.980988
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    tokens = lexer.get_tokens("GET / HTTP/1.1")
    assert next(tokens) == (pygments.token.Name.Function, "GET")
    assert next(tokens) == (pygments.token.Text, " ")
    assert next(tokens) == (pygments.token.Name.Namespace, "/")
    assert next(tokens) == (pygments.token.Text, " ")
    assert next(tokens) == (pygments.token.Keyword.Reserved, "HTTP")
    assert next(tokens) == (pygments.token.Operator, "/")
    assert next(tokens) == (pygments.token.Number, "1.1")
    assert next(tokens)

# Generated at 2022-06-13 22:01:16.286350
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    formatter = ColorFormatter(env=None)
    headers = '''\
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Mon, 27 Nov 2017 12:38:42 GMT
Content-Type: text/html
Content-Length: 162
Last-Modified: Sat, 04 Nov 2017 19:48:22 GMT
Connection: keep-alive
ETag: "5a0674ae-a2"
Accept-Ranges: bytes
'''