

# Generated at 2022-06-13 21:51:34.887555
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # defined styles
    assert ColorFormatter.get_style_class('monokai') \
        == pygments.styles.get_style_by_name('monokai')
    assert ColorFormatter.get_style_class('solarized') \
        == pygments.styles.get_style_by_name('solarized')

    # non-defined style
    assert ColorFormatter.get_style_class('asdf') \
        == pygments.styles.get_style_by_name('default')

# Generated at 2022-06-13 21:51:36.429551
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:51:41.340833
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie import config

    env = config.Environment()
    color_formatter = ColorFormatter(env=env)
    assert color_formatter.formatter is not None
    assert color_formatter.http_lexer is not None

# Generated at 2022-06-13 21:51:48.514437
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class MockEnv(object):
        colors = None
    class MockFormatterPlugin(object):
        implicit_body = True
        implicit_headers = True
        theme = None
    color_formatter = ColorFormatter(
        env=MockEnv(),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
        formatter=MockFormatterPlugin()
    )
    assert color_formatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style

# Generated at 2022-06-13 21:51:59.655449
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter(Environment(colors=256), explicit_json=False, color_scheme='solarized')
    # Test response with body without Content-Type
    body = '{"key": "value"}'
    body_highlight = formatter.format_body(body, '')
    assert body_highlight == "\x1b[38;5;4m{\x1b[39m\x1b[38;5;4m\"key\"\x1b[39m\x1b[38;5;4m:\x1b[39m \x1b[38;5;4m\"value\"\x1b[39m\x1b[38;5;4m}\x1b[39m"
    # Test response with body with Content-Type
    body = '{"key": "value"}'

# Generated at 2022-06-13 21:52:08.945345
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    assert ColorFormatter(Environment()).format_headers('GET /') == \
        "\x1b[1mGET\x1b[0m \x1b[1m/\x1b[0m\r\n"
    assert ColorFormatter(Environment(), color_scheme=SOLARIZED_STYLE).format_headers('GET /') == \
        "\x1b[32mGET\x1b[39m \x1b[32m/\x1b[39m\r\n"

# Generated at 2022-06-13 21:52:10.348915
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    cf = ColorFormatter()

# Generated at 2022-06-13 21:52:15.560643
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style = ColorFormatter.get_style_class(SOLARIZED_STYLE)
    assert style == Solarized256Style
    assert style.styles.get(pygments.token.Token, None) == Solarized256Style.BASE1

# Generated at 2022-06-13 21:52:20.241316
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    """
    Test the method get_style_class of class ColorFormatter
    """
    style_class = ColorFormatter(None).get_style_class(SOLARIZED_STYLE)
    assert style_class == Solarized256Style

# Generated at 2022-06-13 21:52:27.236971
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.input import ParseError
    from httpie.plugins import FormatterPlugin
    env = Environment()
    formatter = ColorFormatter(env)
    code = "GET / HTTP/1.1\r\nHeader: value\r\n\r\n"
    assert type(formatter.format_headers(code)) == str

# Generated at 2022-06-13 21:52:38.762840
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import re
    import subprocess
    import unittest

    class ColorFormatterTestCase(unittest.TestCase):
        def setUp(self):
            import os
            import httpie.core
            executable_path = httpie.core.sys.executable
            self.env = os.environ.copy()
            self.env["TERM"] = "xterm-256color"

        def test_headers_colorized(self):
            input_args = ['--debug', 'GET', 'https://httpie.org']
            input_result_string = subprocess.check_output(
                ['http', '--pretty=colors'] + input_args,
                env=self.env
            ).decode()


# Generated at 2022-06-13 21:52:45.187549
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # TODO: Figure out how to get this test running
    return
    from . import formatter

    # Returns False if formatter is not available
    if not formatter.ColorFormatter:
        return

    # Fixture to test
    class TestClass:
        def test_method(self):
            lexer = self.get_lexer_for_body('text/json', '{"id": 1}')
            assert hasattr(lexer, 'name') and lexer.name == 'JSON'

    # Operate on fixture
    test = TestClass()
    test.test_method()

# Generated at 2022-06-13 21:52:49.941763
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment()
    mp = ColorFormatter(env)
    headers = """GET / HTTP/1.1\r
Host: localhost:5000\r
Connection: keep-alive\r
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r
Upgrade-Insecure-Requests: 1\r
DNT: 1\r
Accept-Encoding: gzip, deflate, sdch\r
Accept-Language: en-US,en;q=0.8\r
\r
"""

# Generated at 2022-06-13 21:53:02.639238
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.utils import get_code_text

    env = Environment()
    env.stdout_isatty = True
    env.colors = True

    # When
    headers = ('Content-Length: 13\r\n'
               'Content-Type: text/html; charset=ISO-8859-4\r\n'
               'Set-Cookie: foo=bar; Domain=.example.com; Path=/; '
               'Expires=Wed, 13-Jan-2021 22:23:01 GMT; Secure; HttpOnly\r\n'
               'Date: Tue, 15 Nov 1994 08:12:31 GMT')
    fmt = ColorFormatter(env=env)
    headers = fmt.format_headers(headers)

    # Then

# Generated at 2022-06-13 21:53:11.569008
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.plugins.builtin import JSONFormatter
    from httpie.plugins.builtin import JSONPFormatter
    from httpie.plugins.builtin import XMLFormatter

    formatter = ColorFormatter(Environment(color=True))
    formatter.explicit_json = True
    json_formatter = JSONFormatter(Environment(color=True))
    jsonp_formatter = JSONPFormatter(Environment(color=True))
    xml_formatter = XMLFormatter(Environment(color=True))

    def check_lexer(mime: str, body: str):
        assert formatter.get_lexer_for_body(mime=mime, body=body)


# Generated at 2022-06-13 21:53:19.609812
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    # import pygments.formatters
    # (pygments.formatters.terminal.TerminalFormatter,
    #  pygments.formatters.terminal256.Terminal256Formatter)
    environment = Environment(colors=256)
    color_formatter_plugin = ColorFormatter(environment, explicit_json=False,
                                            color_scheme=DEFAULT_STYLE)
    assert color_formatter_plugin.format_body("hello: world", "text/html") == "hello: world"
    assert color_formatter_plugin.format_body("hello: world", "text/css") == "hello: world"

# Generated at 2022-06-13 21:53:22.671560
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.colors import ColorFormatter
    environment = Environment(colors=256)
    ColorFormatter(env=environment)

# Generated at 2022-06-13 21:53:34.210676
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import requests
    from httpie.compat import is_windows
    from httpie.plugins import FormatterPlugin
    from httpie.context import Environment
    env = Environment()
    env.colors = 256
    env.stdout_isatty = True
    env.stdin_isatty = True
    env.stderr_isatty = True
    env.stdout_encoding = 'utf-8'
    env.stdin_encoding = 'utf-8'
    env.stderr_encoding = 'utf-8'
    env.colors = True
    env.is_windows = is_windows
    env.stdout = requests.compat.StringIO()
    env.stderr = requests.compat.StringIO()
    env.stdin = requests.compat.StringIO()
   

# Generated at 2022-06-13 21:53:48.763063
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(Environment())
    assert 'JSON' == formatter.get_lexer_for_body(
        'application/json',
        '{"a": 100}'
    ).__class__.__name__
    assert 'Python' == formatter.get_lexer_for_body(
        'text/x-python',
        'print("hello world")'
    ).__class__.__name__
    assert 'XML' == formatter.get_lexer_for_body(
        'text/xml',
        '<a>100</a>'
    ).__class__.__name__
    assert 'Text only' == formatter.get_lexer_for_body(
        'text/plain',
        'hello world'
    ).__class__.__name__


# Generated at 2022-06-13 21:53:55.785169
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.compat import is_windows
    if is_windows:
        return
    formatter = ColorFormatter(None, {})
    assert formatter.format_body('{"a":1}', 'application/json') == "\x1b[38;5;22m{\x1b[39m\x1b[38;5;28m\"a\"\x1b[39m\x1b[38;5;64m:\x1b[39m\x1b[38;5;28m1\x1b[38;5;22m}\x1b[39m\n"

# Generated at 2022-06-13 21:54:04.076545
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    """
    >>> pygments.highlight('GET http://httpbin.org', SimplifiedHTTPLexer(), Terminal256Formatter(style=Solarized256Style))
    '\\x1b[38;5;37mGET\\x1b[39m \\x1b[38;5;19mhttp://httpbin.org\\x1b[39m\\n'
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 21:54:06.540393
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('fruity') is pygments.styles.get_style_by_name('fruity')
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style

# Generated at 2022-06-13 21:54:18.746463
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    class Env:
        colors = 256

    assert isinstance(
        ColorFormatter(
            Env(),
            color_scheme='solarized',
        ).get_lexer_for_body('application/json', '{}'),
        pygments.lexers.data.JsonLexer)

    assert isinstance(
        ColorFormatter(
            Env(),
        ).get_lexer_for_body('application/json', '{}'),
        pygments.lexers.data.JsonLexer)

    assert isinstance(
        ColorFormatter(
            Env(),
            color_scheme='solarized',
            explicit_json=True,
        ).get_lexer_for_body('application/x-javascript', '{}'),
        pygments.lexers.data.JsonLexer)



# Generated at 2022-06-13 21:54:25.863308
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style = ColorFormatter.get_style_class('anotherstyle')
    assert style is None

    style = ColorFormatter.get_style_class(SOLARIZED_STYLE)
    assert style is Solarized256Style

    style = ColorFormatter.get_style_class('emacs')
    assert isinstance(style, type)

# Generated at 2022-06-13 21:54:35.936440
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # Mocked-up HTTPie environment, passing True in the config.colors key to emulate a 256-color terminal
    class EnvironmentMock:
        def __init__(self, explained_json, color_scheme, explicit_json):
            self.config = {
                'colors': True,
                'explained_json': explained_json,
                'color_scheme': color_scheme,
                'explicit_json': explicit_json
            }

    # Example of a HTML body

# Generated at 2022-06-13 21:54:45.694054
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.plugins import plugin_manager
    from httpie.context import Environment
    from httpie.plugins.builtin import HTTP_PLUGIN_CLASS
    env = Environment()
    # default style is auto
    color_format = ColorFormatter(env)
    # style changes to fruity
    color_format_fruity = ColorFormatter(env,color_scheme='fruity')
    # style changes to solarized
    color_format_solarized = ColorFormatter(env,color_scheme='solarized')
    assert color_format.formatter != color_format_fruity.formatter\
           or color_format.formatter != color_format_solarized.formatter\
           or color_format_fruity.formatter != color_format_solarized.formatter
    plugin_manager

# Generated at 2022-06-13 21:54:48.532148
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(is_windows=False, colors=True)
    ColorFormatter(env=env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert True

# Generated at 2022-06-13 21:54:53.324280
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    class FakeEnv:
        def __init__(self):
            self.colors = None
    env = FakeEnv()
    httpie_color = ColorFormatter(env)
    assert httpie_color is not None

# Generated at 2022-06-13 21:55:04.331215
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.cli.terminal import Terminal

    try:
        import pygments
    except ImportError:
        return

    env = Environment(colors=256)
    formatter = ColorFormatter(env=env, color_scheme='solarized')
    fragment = formatter.format_headers('GET / HTTP/1.1\nHost: foo\n')
    assert IS_WIN and fragment.startswith('\x1b[38;5;251m') or \
        fragment.startswith('\x1b[38;5;148m')

    env = Environment(colors=256)
    formatter = ColorFormatter(env=env, color_scheme='solarized')
    fragment = formatter.format_headers('HTTP/1.1 200 OK\n\n')
    assert IS_WIN and fragment

# Generated at 2022-06-13 21:55:04.977057
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    pass

# Generated at 2022-06-13 21:55:18.314696
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    method = ColorFormatter.get_style_class
    assert issubclass(method(DEFAULT_STYLE), pygments.style.Style)
    assert issubclass(method('manni'), pygments.style.Style)
    assert issubclass(method(AUTO_STYLE), pygments.style.Style)
    assert issubclass(method(SOLARIZED_STYLE), Solarized256Style)

# Generated at 2022-06-13 21:55:31.053131
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    input = """
HTTP/1.1 200 OK
Date: Tue, 15 Nov 1994 08:12:31 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 138
Last-Modified: Tue, 15 Nov 1994 08:12:31 GMT
Server: EOS (vnywng/1DEC)

<title>Example</title>
<p>This is an example page.</p>
"""
    lexer = SimplifiedHTTPLexer()
    formatter = Terminal256Formatter(style=Solarized256Style)
    output = pygments.highlight(
        code=input,
        lexer=lexer,
        formatter=formatter,
    ).strip()

# Generated at 2022-06-13 21:55:42.421367
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('text/html')
    assert get_lexer('text/html; charset=utf-8')
    assert get_lexer('text/html', body='<!DOCTYPE html><html></html>')
    assert get_lexer('application/json')
    assert get_lexer('application/json', body='{}')
    assert get_lexer('application/x-yaml')
    assert get_lexer('application/x-yaml', body='{}')
    assert get_lexer('application/x-www-form-urlencoded')
    assert get_lexer('application/x-www-form-urlencoded', body='key=val')
    assert get_lexer('application/problem+json')

# Generated at 2022-06-13 21:55:46.106899
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style_class = ColorFormatter.get_style_class(color_scheme=SOLARIZED_STYLE)
    assert style_class is Solarized256Style

# Generated at 2022-06-13 21:55:55.876833
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Constructor
    formatter = ColorFormatter(Environment({'colors': None}))
    assert formatter.enabled is False
    formatter = ColorFormatter(Environment({'colors': True}))
    assert formatter.enabled is True
    formatter = ColorFormatter(Environment({'colors': False}))
    assert formatter.enabled is False
    formatter = ColorFormatter(Environment({'colors': 256}))
    assert formatter.enabled is True
    formatter = ColorFormatter(Environment({'colors': 16}))
    assert formatter.enabled is True

# Generated at 2022-06-13 21:56:03.739316
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.output.dotformatter import DotFormatter
    from httpie.output.formatters import get_formatter
    from httpie.output.streams import StdoutStream
    fmtr = get_formatter('table',
                         stdout=StdoutStream(),
                         env=Environment())
    fmtr.httpie = DotFormatter(env=Environment())
    #format_body(self, body: str, mime: str)
    fmtr.format_body('{"foo":"bar"}', 'application/json')
    fmtr.format_body('{"foo":"bar"}', 'application/json')
    fmtr.format_body('{"foo":"bar"}', 'application/json')
    fmtr.format_body('<html><body><body></html>', 'application/xml')
    f

# Generated at 2022-06-13 21:56:04.881969
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert isinstance(SimplifiedHTTPLexer(), pygments.lexer.RegexLexer)

# Generated at 2022-06-13 21:56:07.139042
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    from pygments.lexers import get_lexer_for_mimetype

    assert get_lexer_for_mimetype('text/http') == SimplifiedHTTPLexer

# Generated at 2022-06-13 21:56:22.061296
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('bw') is pygments.styles.get_style_by_name('bw')
    assert ColorFormatter.get_style_class('monokai') is pygments.styles.get_style_by_name('monokai')
    assert ColorFormatter.get_style_class('DEFualt') is pygments.styles.get_style_by_name('DEFAULT')
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style
    assert ColorFormatter.get_style_class('') is Solarized256Style
    assert ColorFormatter.get_style_class(None) is Solarized256Style


# Generated at 2022-06-13 21:56:32.016771
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class FakeEnvironment():
        def __init__(self, colors=True):
            self.colors = colors

    formatter = ColorFormatter(FakeEnvironment(), True, 'solarized256')

# Generated at 2022-06-13 21:56:52.793096
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import pytest
    from httpie.formatter import format_headers

    with pytest.raises(Exception, match='No such color scheme'):
        ColorFormatter(Environment(colors=256), 'nonexistent')

    # Test that the http lexer is used.
    headers = """GET / HTTP/1.1
Host: example.org
Accept: */*
"""
    # This would raise an exception if the lexer wasn't used.
    body = ColorFormatter(
        Environment(colors=256),
        color_scheme='murphy'
    ).format_headers(headers)
    assert body

    # Test the output of a colorized headers section

# Generated at 2022-06-13 21:56:56.492684
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    expected = 'httpie.plugins.builtin.colors.Solarized256Style'
    actual = ColorFormatter.get_style_class('solarized256').__name__
    assert actual == expected

# Generated at 2022-06-13 21:56:57.703719
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    ColorFormatter('env')

# Generated at 2022-06-13 21:57:07.534715
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    lexer = pygments.lexers.get_lexer_by_name('json')
    res_json = '''{
        "foo": "bar"
    }'''
    res_highlighted = '{'
    assert not ColorFormatter.format_body(res_json, '')
    assert 'bar' not in ColorFormatter.format_body(res_json, 'text')
    assert 'bar' not in ColorFormatter.format_body(res_json, 'json')
    assert 'bar' not in ColorFormatter.format_body(res_json, 'xml')
    assert 'bar' in ColorFormatter.format_body(res_json, 'application/json')
    assert 'bar' in ColorFormatter.format_body(res_json, 'application/json; charset=utf-8')

# Generated at 2022-06-13 21:57:12.587145
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class Dummy(object):
        def __init__(self, env):
            self.env = env

    formatter = ColorFormatter(env=Dummy(env=None))
    assert formatter.get_style_class('solarized') == Solarized256Style
    assert formatter.get_style_class('solarized256') == Solarized256Style
    assert formatter.get_style_class('solarized-light') == pygments.styles.get_style_by_name('solarized')



# Generated at 2022-06-13 21:57:14.654189
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    cf = ColorFormatter(env)
    assert cf.enabled is True
    assert cf.formatter is not None
    assert cf.http_lexer is not None
    assert cf.explicit_json is False

# Generated at 2022-06-13 21:57:27.399968
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.context import Environment
    from httpie.plugins import BuiltinPluginManager
    from httpie.plugins.manager import PresentPlugin
    from httpie.plugins.colors import ColorFormatter

    pm = BuiltinPluginManager()

    environment = Environment(stdin=None)
    environment.output_options = {
        'colors': '256'
    }

    for plugin in pm.get_plugins(PresentPlugin):
        plugin.update_environment(environment)

    color_formatter = ColorFormatter(env=environment)

    # POST /post HTTP/1.1
    # Accept: application/json
    # Content-Length: 11
    # Content-Type: application/x-www-form-urlencoded; charset=utf-8
    # Host: httpbin.org
    # User-Agent: HTTPie/2.

# Generated at 2022-06-13 21:57:39.071586
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    # Test with the default color scheme
    env = Environment(
        colors=256,
        style=ColorFormatter.AUTO_STYLE
    )
    formatter = ColorFormatter(env)

    actual = formatter.format_headers(headers = "HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: application/json\r\nDate: Wed, 04 Sep 2019 22:40:31 GMT\r\nTransfer-Encoding: chunked\r\n\r\n")

# Generated at 2022-06-13 21:57:45.611336
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    """
    Create an instance of ColorFormatter class.

    Call get_style_class method of this class.

    Make sure that the style object returned is of class
    Solarized256Style.
    """
    style = ColorFormatter(
        env=Environment(colors=256),
        color_scheme=SOLARIZED_STYLE
    ).get_style_class(color_scheme=SOLARIZED_STYLE)
    assert style is Solarized256Style

# Generated at 2022-06-13 21:57:53.636977
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import pygments
    from pygments.lexers.text import HttpLexer as PygmentsHttpLexer
    from pygments.formatters.terminal import TerminalFormatter


# Generated at 2022-06-13 21:58:19.777388
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment
    env = Environment()

    f = ColorFormatter(env)
    assert f.format_body("<html><head><title>Test</title></head></html>", "text/html") == "<html><head><title>Test</title></head></html>"


# Generated at 2022-06-13 21:58:31.450303
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment

    global_args = {'verify': False}

    def test_httpie(input, expected_output, expected_lexer, expected_color_formatter_enabled, fd=None, env=None):
        global_args.update(env or {})
        env = Environment(auto_env=False, **global_args)
        assert input.endswith('\n')
        input = input.encode('utf-8')
        output = ColorFormatter(env=env, explicit_json=False, color_scheme='auto',
                                stdin_isatty=True, stdout_isatty=True).format_body(
            body=input.decode('utf-8'), mime='application/json')

# Generated at 2022-06-13 21:58:32.744145
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    ColorFormatter.get_style_class('none')

# Generated at 2022-06-13 21:58:40.905611
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from .helpers import http

    r = http('--color=always', 'GET', httpbin.url + '/headers',
             'Foo:bar')
    assert r.exit_status == 0
    assert '\x1b[30m' in r  # Black.
    assert '\x1b[32m' in r  # Green.
    assert '\x1b[1m' in r  # Bold.
    assert '\x1b[39m' in r  # default.
    assert '\x1b[0m' in r  # Reset.

# Generated at 2022-06-13 21:58:44.480083
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style_class = ColorFormatter.get_style_class("solarized")
    assert style_class.__name__ == "Solarized256Style"

# Generated at 2022-06-13 21:58:49.749890
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']
    assert len(lexer.tokens) == 1
    assert len(lexer.tokens['root']) == 3

# Generated at 2022-06-13 21:58:51.271095
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter = ColorFormatter()
    pass

# Generated at 2022-06-13 21:59:04.345597
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    # Arrange
    class FakeEnv:
        def __init__(self):
            self.colors = 256

    color_formatter = ColorFormatter(FakeEnv())
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n'

    # Act
    result = color_formatter.format_headers(headers)

    # Assert

# Generated at 2022-06-13 21:59:08.819743
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    class FakeEnvironment:
        def __init__(self, colors, stdout_isatty):
            self.colors = colors
            self.stdout_isatty = stdout_isatty

    class FakeFormatterPlugin(ColorFormatter):
        pass

    env = FakeEnvironment(256, True)
    formatter = FakeFormatterPlugin(env)
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n'

# Generated at 2022-06-13 21:59:12.584474
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    print(get_lexer('application/json', body='{"a":1}'))
    print(get_lexer('application/json', body='{"a":1}', explicit_json=True))

# Generated at 2022-06-13 21:59:49.683323
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    try:
        env = Environment(colors=False)
        color_formatter = ColorFormatter(env)
        assert not color_formatter.enabled
    except Exception as e:
        assert False, e
    try:
        env = Environment()
        color_formatter = ColorFormatter(env)
        assert color_formatter.enabled
    except Exception as e:
        assert False, e
    try:
        env = Environment()
        color_formatter = ColorFormatter(env, color_scheme='solarized')
        assert color_formatter.enabled
    except Exception as e:
        assert False, e
    try:
        env = Environment(colors=256)
        color_formatter = ColorFormatter(env)
        assert color_formatter.enabled
    except Exception as e:
        assert False, e

# Generated at 2022-06-13 21:59:58.434725
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert SimplifiedHTTPLexer.name == 'HTTP'
    assert SimplifiedHTTPLexer.aliases == 'http'
    assert SimplifiedHTTPLexer.filenames == '*.http'
    assert SimplifiedHTTPLexer.tokens == 'root'
    assert SimplifiedHTTPLexer.BASE03 == "#1c1c1c"
    assert SimplifiedHTTPLexer.BASE02 == "#262626"
    assert SimplifiedHTTPLexer.BASE01 == "#4e4e4e"
    assert SimplifiedHTTPLexer.BASE00 == "#585858"
    assert SimplifiedHTTPLexer.BASE0 == "#808080"
    assert SimplifiedHTTPLexer.BASE1 == "#8a8a8a"


# Generated at 2022-06-13 21:59:59.852803
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    import pytest
    with pytest.raises(TypeError):
        lexer.get_tokens(text=None)

# Generated at 2022-06-13 22:00:09.112992
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # If MIME type is text/html, then get an html lexer
    color_formatter = ColorFormatter(Environment())
    lexer_for_body = color_formatter.get_lexer_for_body("text/html", "")
    assert lexer_for_body.__name__ == "XHtmlLexer"

    # If MIME type is text/javascript, then get an html lexer
    lexer_for_body = color_formatter.get_lexer_for_body("text/javascript", "")
    assert lexer_for_body.__name__ == "JavascriptLexer"

    # If MIME type is text/css, then get an html lexer
    lexer_for_body = color_formatter.get_lexer_for_body("text/css", "")
    assert lexer

# Generated at 2022-06-13 22:00:17.910462
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import unittest
    from unittest.mock import Mock
    from httpie.context import Environment
    from httpie.plugins import FormatterPluginManager

    class TestCase(unittest.TestCase):
        def test_format_headers(self):
            env = Environment(stdout=None, colors=256)
            formatter = ColorFormatter(env, explicit_json=False)
            color_string = formatter.format_headers("Content-Type: application/json\nAccept: application/json\n")


# Generated at 2022-06-13 22:00:29.779491
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    """
    Test ColorFormatter.format_body
    
    This method expects two strings as parameters.
    
    Parameters : 
    body: the body of the response of the server (the content)
    mime: the mime type of the content
    """
    try:
        import httpie.plugins as p
    except:
        assert False, 'Could not import module httpie.plugins'
        return
    
    import httpie.compat as c
    
    try:
        import httpie.context as con
    except:
        assert False, 'Could not import module httpie.context'
        return
    
    if (c.is_windows):
        color_scheme = 'fruity'
    else:
        color_scheme = 'auto'

# Generated at 2022-06-13 22:00:31.813939
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Test if can be constructed when feature not supported
    env = Environment()
    env.colors = False
    ColorFormatter(env=env)



# Generated at 2022-06-13 22:00:44.708411
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    from pygments.lexer import RegexLexer
    assert issubclass(SimplifiedHTTPLexer, RegexLexer)

    request = 'GET / HTTP/1.1'
    response = 'HTTP/1.1 200 OK'
    header = 'Foo: Bar'
    assert pygments.lexer.bygroups(
        pygments.token.Name.Function,
        pygments.token.Text,
        pygments.token.Name.Namespace,
        pygments.token.Text,
        pygments.token.Keyword.Reserved,
        pygments.token.Operator,
        pygments.token.Number
    ).__dict__ == pygments.lex(request, lexer=SimplifiedHTTPLexer()).__dict__

# Generated at 2022-06-13 22:00:48.022041
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    try:
        SimplifiedHTTPLexer()
    except:
        print("===Failed to construct SimplifiedHTTPLexer===")
        raise
    print("===Test SimplifiedHTTPLexer successful===")


# Generated at 2022-06-13 22:00:56.413133
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import pytest

    header_string = "Content-Type: text/html\r\nContent-Length: 17\r\n"
    obj_ColorFormatter = ColorFormatter(Environment())
    assert obj_ColorFormatter.format_headers(header_string) == "\x1b[38;5;241mContent-Type\x1b[0m: \x1b[38;5;37mtext/html\x1b[0m\r\n\x1b[38;5;241mContent-Length\x1b[0m: \x1b[38;5;37m17\x1b[0m\r\n"

