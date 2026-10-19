

# Generated at 2022-06-13 21:51:37.541320
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    def check(mime, body, expected_lexer):
        actual_lexer = ColorFormatter.get_lexer_for_body(mime, body)
        assert actual_lexer.name == expected_lexer.name

    check('text/plain', '', pygments.lexers.get_lexer_by_name('text'))
    check('application/json', '{}', pygments.lexers.get_lexer_by_name('json'))
    check('application/unknown-json', '{}', None)
    check('application/json', '{"foo": 123}', pygments.lexers.get_lexer_by_name('json'))
    check('application/unknown-json', '{"foo": 123}', pygments.lexers.get_lexer_by_name('json'))
   

# Generated at 2022-06-13 21:51:45.023933
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # pylint: disable=protected-access
    assert ColorFormatter._get_style_class(None) == TerminalFormatter().style
    assert ColorFormatter._get_style_class('fruity') == TerminalFormatter().style
    assert ColorFormatter._get_style_class('256') == Terminal256Formatter().style
    assert ColorFormatter._get_style_class('auto') == TerminalFormatter().style



# Generated at 2022-06-13 21:51:47.250317
# Unit test for function get_lexer
def test_get_lexer():
    lexer = get_lexer(mime='text/javascript')
    assert lexer.__name__ == 'JavaScript'



# Generated at 2022-06-13 21:51:56.327781
# Unit test for function get_lexer
def test_get_lexer():
    for mimetype in ["text/html", "text/html; charset=utf-8"]:
        assert get_lexer(mimetype, body="")
    assert get_lexer("application/x-yaml", body="")
    assert get_lexer("application/javascript", body="")
    assert get_lexer("text/x-sh", body="")
    assert get_lexer("foo/bar", body="")
    assert get_lexer("foo/bar", body="", explicit_json=True) == get_lexer("application/json", body="")



# Generated at 2022-06-13 21:52:05.306227
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2022-06-13 21:52:09.494329
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import httpie
    env = httpie.Environment(colors=True, styled=True)
    formatter = ColorFormatter(env)
    assert formatter is not None

# Generated at 2022-06-13 21:52:19.784901
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class DummyEnv():
        colors = 256

    # Assert format_body works for unicode string.
    formatter = ColorFormatter(DummyEnv())
    body = formatter.format_body(
        u'\xa3 59.9',
        'application/json'
    )
    assert body == body

    # Assert format_body works for ASCII string.
    body = formatter.format_body(
        '{"key": "value"}',
        'application/json'
    )
    assert body == body

# Generated at 2022-06-13 21:52:29.746681
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import main
    from httpie.formatter import JSONFormatter
    from httpie import ExitStatus

    env = Environment()
    env.stdin = open("test_data/test_comet.json", 'rb')
    exit_status, output, _ = main(
        env=env,
        args=[
            "--json",
            "https://httpbin.org/post"
        ]
    )

    assert exit_status == ExitStatus.OK
    assert output == JSONFormatter().format_body('{"key": "value"}', 'application/json')

# Generated at 2022-06-13 21:52:37.535085
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    from httpie.compat import is_windows

    env = Environment(color=256)
    formatter = ColorFormatter(env)

# Generated at 2022-06-13 21:52:50.638304
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.plugins import ColorFormatter
    # Test case 1
    obj = ColorFormatter(None, False)
    assert obj.format_body("abc", "text/plain") == "abc"
    # Test case 2

# Generated at 2022-06-13 21:53:02.222819
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    color_formatter = ColorFormatter(Environment(colors=256))
    for style in AVAILABLE_STYLES:
        try:
            color_formatter.get_style_class(style)
        except Exception as ex:
            assert False, f"Pygments style {style} caused exception: {ex}"

# Generated at 2022-06-13 21:53:11.854642
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    env = Environment(colors=256)
    formatter = ColorFormatter(env, color_scheme=SOLARIZED_STYLE, style=None)
    assert formatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style
    assert formatter.get_style_class(DEFAULT_STYLE) == Solarized256Style
    assert formatter.get_style_class(AUTO_STYLE) == Solarized256Style
    assert formatter.get_style_class('default') == pygments.styles.get_style_by_name('default')

# Generated at 2022-06-13 21:53:17.993723
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # First, test that a default value is given.
    if is_windows:
        assert ColorFormatter.get_style_class(None) == pygments.styles.get_style_by_name(
            'fruity')
    else:
        assert ColorFormatter.get_style_class(None) == pygments.styles.get_style_by_name(
            'auto')

    # Then, test that all available styles are valid.
    for style in AVAILABLE_STYLES:
        ColorFormatter.get_style_class(style)

# Generated at 2022-06-13 21:53:20.751427
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lx = SimplifiedHTTPLexer()


# Generated at 2022-06-13 21:53:28.636240
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():

    class Dummy(dict):
        pass

    class DummyEnv(Dummy):
        def __init__(self):
            self.colors = 256

    env = DummyEnv()
    __ = ColorFormatter(env, explicit_json=False, color_scheme='monokai',
                        **Dummy(explicit_json=False, color_scheme='monokai'))

# Generated at 2022-06-13 21:53:33.154745
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    try:
        ColorFormatter(None).format_body("", "text/html")
        ColorFormatter(None).format_body("", "application/json")
    except Exception as e:
        pytest.fail("Exception not expected:", e)

# Generated at 2022-06-13 21:53:42.958904
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import main
    args = ['--format=colors', '--style=solarized', 'GET', 'http://httpbin.org/get']
    env = main.parse_args(args=args, env=Environment())
    processor = ColorFormatter(env=env)
    assert processor.format_body('hello world', 'text/html') == '\x1b[7m\x1b[38;5;33m'"hello world" + "\x1b[0m"

# Generated at 2022-06-13 21:53:55.450300
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.output.streams import DEFAULT_STDOUT_ENCODING
    from httpie import Environment
    from httpie.main import get_default_headers
    from httpie.plugins import FormatterPlugin
    class TestColorFormatter(FormatterPlugin):
        group_name = 'colors'
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
        def format_headers(self, headers: str) -> str:
            return "plain" + headers
    class TestEnvironment(Environment):
        colors = None
    env = TestEnvironment(
        default_options=get_default_headers(),
        colors=None,
        stdout_encoding=DEFAULT_STDOUT_ENCODING,
    )

# Generated at 2022-06-13 21:53:56.867359
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style

# Generated at 2022-06-13 21:53:59.338413
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style



# Generated at 2022-06-13 21:54:20.227172
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    env = Environment(colors=256)
    body = "PREFIX\n{\"field1\": [{\"field2\": \"value2\"}]}\nSUFFIX"
    mime = "application/json"
    formatter = ColorFormatter(env)
    result = formatter.format_body(body=body, mime=mime)
    assert result == "PREFIX\n\x1b[38;5;118m{\"field1\": [{\"field2\": \"value2\"}]}\nSUFFIX\x1b[0m"

# Generated at 2022-06-13 21:54:21.692109
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    assert get_lexer('application/json')

# Generated at 2022-06-13 21:54:24.023394
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter(Environment()).enabled is True
    assert ColorFormatter(Environment(colors=False)).enabled is False

# Generated at 2022-06-13 21:54:26.816897
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE)  is Solarized256Style

# Generated at 2022-06-13 21:54:36.414916
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import http
    env = Environment()

    # If environment variable HTTPIE_COLORS = 0, method format_body should
    # return the body as it is, without any highlighting.
    env.colors = 0
    cf = ColorFormatter(env)

    body_json = '{"key": "value"}'
    body_plaintext = "Hello World"
    body_html = '<div>Hello World</div>'
    body_xml = '<key>value</key>'

    json_http_status, json_header, json_body = http(
        env,
        '--json',
        'GET',
        'http://httpbin.org/anything',
        body=body_json
    )

# Generated at 2022-06-13 21:54:43.836281
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from . import main

    class Env:
        colors = 256

    env = Env()
    cf = ColorFormatter(env=env)
    # assert True is True
    # assert cf.get_lexer_for_body('application/json', '{}') is not None
    # assert cf.get_lexer_for_body('application/json', '') is not None
    # assert cf.get_lexer_for_body('application/jsonx', '{}') is None
    # assert cf.get_lexer_for_body('', '') is None
    # assert cf.get_lexer_for_body('text/plain', '') is None
    # assert cf.get_lexer_for_body('text/javascript', '') is None
    # assert cf.get_lexer_for_body('

# Generated at 2022-06-13 21:54:45.007376
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:54:54.488456
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie import ExitStatus
    from httpie.client import Environment
    from httpie.compat import is_windows
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin

    if is_windows:
        color_scheme = 'fruity'
    else:
        color_scheme = 'auto'

    env = Environment(colors=256, color_scheme=color_scheme)
    f = ColorFormatter(env=env)
    assert f.formatter.__class__.__name__ == 'Terminal256Formatter'

    env2 = Environment(colors=True, color_scheme=color_scheme)
    f2 = ColorFormatter(env=env2)
    assert f2.formatter.__class__.__name__ == 'TerminalFormatter'

    headers

# Generated at 2022-06-13 21:54:57.437131
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    for style in AVAILABLE_STYLES:
        assert issubclass(ColorFormatter.get_style_class(style),
                          pygments.style.Style)

# Generated at 2022-06-13 21:55:07.284073
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from .util import get_plugin_manager
    formatter = ColorFormatter(
        env=Environment(),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE
    )
    body = """{
        "id": 1,
        "name": "Foo",
        "price": 123,
        "tags": [
            "Bar",
            "Eek"
        ],
        "stock": {
            "warehouse": 300,
            "retail": 20
        }
    }
    """

# Generated at 2022-06-13 21:55:20.246407
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    """
    The SimplifiedHTTPLexer checks the input and separate them into the right tokens
    """
    assert SimplifiedHTTPLexer().get_tokens(
        'GET http://www.google.com HTTP/1.1') == \
           [(3, 'http://www.google.com'), (0, ' '), (5, 'HTTP'), (0, '/'), (2, '1.1')]


# Generated at 2022-06-13 21:55:21.599328
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    c = ColorFormatter(None)
    assert c.enabled == False

# Generated at 2022-06-13 21:55:29.036197
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.compat import pygments_version_info
    from httpie.plugins import BuiltinPluginManager
    from httpie.output import get_style_class
    from pygments.styles import get_style_by_name

    assert get_style_by_name('default') == get_style_class('default')

    # In order to see if it can find the new style created in this
    # file, we need to actually create it:
    assert get_style_by_name('solarized256') == get_style_class('solarized256')

    # If the version of pygments is older than 2.0.2, the
    # "solarized256" cannot be found, as it is not included in its
    # list of styles:

# Generated at 2022-06-13 21:55:41.643919
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    """
    Create a simplified HTTP lexer.
    Then assert if it matches the input given.

    """
    http_lexer = SimplifiedHTTPLexer()
    input_s = """HTTP/1.1 404 Not Found\n"""
    t = http_lexer.get_tokens(input_s)
    for i in t:
        if i[0] == pygments.token.Keyword.Reserved:
            assert i[1] == "HTTP", "Failed test for token Keyword.Reserved"
        elif i[0] == pygments.token.Operator:
            assert i[1] == "/", "Failed test for token Operator"
        elif i[0] == pygments.token.Number:
            assert i[1] == "1.1", "Failed test for token Number"


# Generated at 2022-06-13 21:55:55.158059
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.cli import parser
    from httpie.context import Environment
    env = Environment(colors=256)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args(['-p','colors','http://httpbin.org/headers','--json','--force-colors','--style','solarized'])
    cf = ColorFormatter(
        env,
        explicit_json=args.json,
        color_scheme=args.style,
    )
    assert cf.formatter.__class__.__name__ == 'Terminal256Formatter', "Proper color formatter not selected"
    assert cf.formatter.style.__class__.__name__ == 'Solarized256Style', "Proper color scheme not selected"

# Generated at 2022-06-13 21:55:57.673054
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    assert ColorFormatter(env).enabled

    env.colors = False
    assert not ColorFormatter(env).enabled

    env.colors = 256
    assert ColorFormatter(env).enabled

# Generated at 2022-06-13 21:56:03.673051
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    """
    Test to check that get_style_class returns the right style
    if parameter is not AUTO_STYLE, else Solarized256Style
    """
    import requests
    env = Environment(colors=256)
    color_formatter = ColorFormatter(env, explicit_json=False, color_scheme='fruity')
    assert color_formatter.get_style_class('fruity') == pygments.styles.get_style_by_name('fruity')
    assert color_formatter.get_style_class(AUTO_STYLE) == Solarized256Style

# Generated at 2022-06-13 21:56:14.044359
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class NewStyle(pygments.style.Style):
        pass

    assert ColorFormatter.get_style_class('newstyle') is NewStyle
    assert ColorFormatter.get_style_class('fruity') is pygments.styles.get_style_by_name('fruity')
    assert ColorFormatter.get_style_class(None) is pygments.styles.get_style_by_name(None)
    assert ColorFormatter.get_style_class('') is pygments.styles.get_style_by_name('')
    assert ColorFormatter.get_style_class('auto') is pygments.styles.get_style_by_name('default')
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style


# Generated at 2022-06-13 21:56:23.782532
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie import ExitStatus
    def get_lexer_for_body(mime, body, explicit_json=False):
        env = Environment(
            stdin=None,
            stdout=None,
            stderr=None,
            stdin_isatty=None,
            stdout_isatty=None,
            color=256,
            extensions=[],
            config_dir=None,
            config_file=None,
            env=None,
            version=ExitStatus.OK,
            children=None,
            output_options=None,
            stdout_is_redirected=None,
            run_once=False,
        )
        formatter = ColorFormatter(env = env)
        return formatter.get_lexer_for_body(mime, body)




# Generated at 2022-06-13 21:56:29.501389
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from os.path import dirname, join
    from httpie.context import Environment

    from httpie import ExitStatus
    from httpie.client import HTTPieRequest
    from httpie.plugins import FormatterPlugin
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from httpie.compat import is_windows
    from httpie.core import main
    from httpie.downloads import (parse_content_range, filename_from_content_disposition, filename_from_url)
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from httpie.plugins import FormatterPlugin
    from httpie.utils import cached_property, get_mime_type, jdk_download_link, is_file_url, is_valid_url

# Generated at 2022-06-13 21:56:38.089828
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('monokai') \
        == pygments.styles.get_style_by_name('monokai')

# Generated at 2022-06-13 21:56:51.904079
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():

    from httpie.cli.constants import COLOR, COLOR_STYLES
    from httpie.context import Environment
    from httpie.plugins.core import Formatter
    from httpie.plugins import builtin_plugins

    env = Environment(colors=COLOR, color_scheme=COLOR_STYLES[0])
    formatter = Formatter(env)
    for plugin in builtin_plugins.get_installed():
        formatter.add_parser(plugin)

    # Test 1
    color_formatter = formatter.resolve('colors')
    assert color_formatter.__class__.__name__ == 'ColorFormatter'
    assert color_formatter.get_style_class(COLOR_STYLES[0]) == Solarized256Style

    # Test 2

# Generated at 2022-06-13 21:57:05.140133
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import pytest
    from httpie import Environment
    from httpie.utils import get_local_http_bin_url

    env = Environment(
        colors=True,
        simple_output=True,
        stdin_isatty=True,
        stdout_isatty=True,
        style=SOLARIZED_STYLE,
        verbose=True,
    )


# Generated at 2022-06-13 21:57:12.891205
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from datetime import datetime
    from httpie.core import Environment
    from httpie.compat import is_windows
    from httpie.context import Environment

    env = Environment()
    color_formatter = ColorFormatter(env=env)

    formatter = color_formatter.formatter

    if is_windows:
        assert isinstance(formatter, TerminalFormatter)
        assert color_formatter.http_lexer is PygmentsHttpLexer
    else:
        assert isinstance(formatter, Terminal256Formatter)
        assert color_formatter.http_lexer is SimplifiedHTTPLexer

        style_class = Solarized256Style
        if color_formatter.color_scheme is DEFAULT_STYLE:
            style_class = Solarized256Style

        assert formatter.style is style_class

   

# Generated at 2022-06-13 21:57:14.790131
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    formatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert formatter.get_style_class(color_scheme=DEFAULT_STYLE)

# Generated at 2022-06-13 21:57:23.379310
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.plugins.colors import ColorFormatter
    assert ColorFormatter.get_style_class(AUTO_STYLE).__name__ == 'NoStyle'
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE).__name__ == 'Solarized256Style'
    assert ColorFormatter.get_style_class('manni').__name__ == 'ManniStyle'
    assert ColorFormatter.get_style_class('default').__name__ == 'DefaultStyle'


# Generated at 2022-06-13 21:57:35.664053
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    color_scheme = 'solarized'
    explicit_json = False
    # under any circumstances, will use 256color mode
    formatter = ColorFormatter(env, explicit_json, color_scheme)
    assert formatter.is_enabled() == True
    assert isinstance(formatter.formatter, Terminal256Formatter)
    # test available styles
    env.colors = 256
    env.style = None
    formatter = ColorFormatter(env, explicit_json, color_scheme)
    assert formatter.is_enabled() == True
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.formatter.style == Solarized256Style
    assert formatter.formatter.style.background_color == "#1c1c1c"

# Generated at 2022-06-13 21:57:48.011213
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    """
    https://github.com/jkbrzt/httpie/issues/1527
    """
    from httpie.plugins import FormatterPlugin
    from httpie.compat import is_windows

    use_auto_style = DEFAULT_STYLE == AUTO_STYLE
    has_256_colors = not is_windows
    if use_auto_style or not has_256_colors:
        http_lexer = PygmentsHttpLexer()
        formatter = TerminalFormatter()
    else:
        http_lexer = SimplifiedHTTPLexer()
        formatter = Terminal256Formatter(
            style=Solarized256Style
        )

    formatter_plugin = FormatterPlugin(formatter=formatter)

# Generated at 2022-06-13 21:57:58.280825
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import httpie.compat
    import httpie.cli
    import httpie.compat
    import httpie.plugins
    env = httpie.cli.Environment(
        colors=256,
        stdin=httpie.compat.mock.MagicMock(),
        stdout=httpie.compat.mock.MagicMock(),
        stderr=httpie.compat.mock.MagicMock(),
    )
    plugin = ColorFormatter(env=env, explicit_json=False)



# Generated at 2022-06-13 21:58:02.982742
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    env.args = []
    env.args.json = False
    env.args.style = 'monokai'
    env.args.force_colors = True
    env.args.colors = 256
    ColorFormatter(env)

# Generated at 2022-06-13 21:58:13.929279
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    li = SimplifiedHTTPLexer()


# Generated at 2022-06-13 21:58:24.228161
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import main

    # Test with a JSON body
    args = [
        '--headers',
        '--verbose',
        '--print=B',
        'POST',
        'http://httpbin.org/post',
        'foo=bar',
        'baz=bar'
    ]
    with main(args=args):
        env = Environment()
        color_formatter = ColorFormatter(env)

# Generated at 2022-06-13 21:58:36.188107
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    from pygments.formatters import HtmlFormatter
    from pygments.util import ClassNotFound
    import os
    import random
    import string

    formatter = HtmlFormatter(style=Solarized256Style)
    http_lexer = SimplifiedHTTPLexer()
    # generate a random http header
    header = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))+':'+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    html = pygments.highlight(code=header, lexer=http_lexer, formatter=formatter).strip()

# Generated at 2022-06-13 21:58:43.885555
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Constructor should not raise
    try:
        env = Environment(auto_colors=False)
        ColorFormatter(env)
        env = Environment(auto_colors=True)
        ColorFormatter(env, color_scheme='default')
        ColorFormatter(env, color_scheme='solarized')
        ColorFormatter(env, color_scheme='solarized256')
        ColorFormatter(env, color_scheme='auto')
        ColorFormatter(env, color_scheme='none')
    except AssertionError:
        assert False

# Generated at 2022-06-13 21:58:52.612035
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    c = ColorFormatter(None)
    # if mime is None and body is None, return None
    assert c.get_lexer_for_body(None, None) is None
    # if mime is None, return None
    assert c.get_lexer_for_body(None, '{"name": "value"}') is None
    # if body is None, return None
    assert c.get_lexer_for_body('application/json', None) is None
    # if mime and body are not None, return correct Lexer
    assert c.get_lexer_for_body('application/json', '{"name": "value"}') == pygments.lexers.JsonLexer

# Generated at 2022-06-13 21:58:55.241998
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    s = SimplifiedHTTPLexer()
    print(s.name)

# Generated at 2022-06-13 21:58:59.834417
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    env = Environment(colors=True)
    text = "one"
    mime = "text/plain"
    formatter = ColorFormatter(env)

    assert formatter.format_body(text, mime) == text

# Generated at 2022-06-13 21:59:03.672924
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter = ColorFormatter(False)
    assert color_formatter.enabled == False
    color_formatter = ColorFormatter(True)
    assert color_formatter.enabled == True
    assert color_formatter.formatter == None

# Generated at 2022-06-13 21:59:06.131673
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    fmt = ColorFormatter(Environment())

# Generated at 2022-06-13 21:59:11.040064
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    _ = ColorFormatter(None)
    assert ColorFormatter.get_style_class('fruity') == pygments.styles.get_style_by_name('fruity')
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:59:42.392216
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from io import StringIO

    from httpie.compat import pyver
    from httpie.plugins import plugin_manager
    from tests.compat import mock

    plugin_manager.load_internal_plugins()

    plugin = ColorFormatter(
        Environment(),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )



# Generated at 2022-06-13 21:59:49.632070
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    from httpie.compat import is_windows
    from pygments.formatters import Terminal256Formatter
    from pygments.styles import get_style_by_name
    from pygments.lexers import get_lexer_for_mimetype
    from pygments.styles.monokai import MonokaiStyle
    from pygments.lexers import HttpLexer

    # example of data
    data = b'GET / HTTP/1.1\r\nContent-Length: 100\r\n'

    # test plugin
    def plugin():
        return ColorFormatter(
            env,
            color_scheme='monokai'
        )

    #create env
    env = Environment(colors=256)

    # plugin with formatter

# Generated at 2022-06-13 21:59:55.582021
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import os
    test_env = Environment()
    test_env.colors = 256
    cap = lambda x: os.system('./autopep.sh | ./test.sh "%s:%s"' % (x,x))
    from httpie.output.formatters.colors import ColorFormatter
    test_env.colors = 256
    formatter = ColorFormatter(test_env)
    cap('headers')

# Generated at 2022-06-13 22:00:07.801169
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import httpie

    env = httpie.Environment()
    formatter = ColorFormatter(env)
    headers = '''GET / HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.5
Host: httpbin.org'''.split('\n')
    result = formatter.format_headers("\n".join(headers))

# Generated at 2022-06-13 22:00:10.424609
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter(None).get_style_class('monokai') == pygments.styles.get_style_by_name('monokai')

# Generated at 2022-06-13 22:00:18.115950
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment()
    env.colors = True
    kwargs = {}
    cf = ColorFormatter(env, **kwargs)
    headers = """GET / HTTP/1.1
Host: localhost:8080
User-Agent: Go-http-client/1.1
"""

# Generated at 2022-06-13 22:00:29.827457
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    class FakeEnvironment():
        def __init__(self):
            self.colors = 256
    class FakeResponse():
        def __init__(self, headers, body):
            self.headers = headers
            self.body = body
    
    # mime type text/html
    headers = {'content-type': 'text/html'}
    body = """<?xml version="1.0" encoding="iso-8859-1"?>
        <!-- 
        #####################################################
        ################### -Welcome- #######################
        #####################################################

        """
    expected_lexer = pygments.lexers.get_lexer_by_name('html')
    actual_lexer = ColorFormatter(FakeEnvironment()).get_lexer_for_body(headers['content-type'], body)
    assert expected_lex

# Generated at 2022-06-13 22:00:33.088499
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    lexer.get_tokens_unprocessed('some test')
    lexer = SimplifiedHTTPLexer()
    lexer.get_tokens_unprocessed('200 OK')

# Generated at 2022-06-13 22:00:35.043481
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    SimplifiedHTTPLexer()

# Generated at 2022-06-13 22:00:48.259915
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.input import ParseError
    from httpie.plugins.builtin import HTTPBasicAuth

    env = Environment(colors=256, stdin=None)
    color_formatter = ColorFormatter(env, explicit_json=False)
    basic_auth = HTTPBasicAuth()

    class MockResponse:
        def __init__(self, headers, body, json=None):
            self.headers = headers
            self.body = body
            self.json = json
        @property
        def status_code(self):
            return 200

    # 1. No Content-Type, no json => text
    headers = {'Content-Length': '1001'}
    response = MockResponse(headers, 'just a plain body')