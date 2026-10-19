

# Generated at 2022-06-13 21:51:36.176755
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('text/html') == pygments.lexers.get_lexer_by_name('html')
    assert get_lexer('application/javascript') == pygments.lexers.get_lexer_by_name('javascript')
    assert get_lexer('text/less') == pygments.lexers.get_lexer_by_name('less')
    assert get_lexer('text/css') == pygments.lexers.get_lexer_by_name('css')
    assert get_lexer('text/x-markdown') == pygments.lexers.get_lexer_by_name('markdown')
    assert get_lexer('text/x-python') == pygments.lexers.get_lexer_by_name('python')

# Generated at 2022-06-13 21:51:48.212449
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(Environment(colors=True))
    assert formatter.get_lexer_for_body('application/json', '[]')
    assert formatter.get_lexer_for_body('application/json', '{"a": "b"}')
    assert formatter.get_lexer_for_body('application/json', '{"a": "b"') is None
    assert formatter.get_lexer_for_body('application/json', '"a": "b"}') is None
    assert formatter.get_lexer_for_body('application/javascript')
    assert formatter.get_lexer_for_body('application/js')
    assert formatter.get_lexer_for_body('application/typescript') is None

# Generated at 2022-06-13 21:51:49.553011
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    ColorFormatter();


# Generated at 2022-06-13 21:52:00.374375
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    mime_type = 'application/json'
    body = '{"key":"value"}'
    assert get_lexer(mime_type, body)
    assert pygments.lexers.get_lexer_by_name('json') == get_lexer(mime_type, body)

    mime_type = 'application/json'
    body = '{"key":"value"'
    assert get_lexer(mime_type, body)
    assert pygments.lexers.get_lexer_by_name('json') == get_lexer(mime_type, body)

    mime_type = 'unrecognizable'
    body = ''
    assert not get_lexer(mime_type, body)

    mime_type = 'application/javascript'
    body = '{"key":"value"}'

# Generated at 2022-06-13 21:52:07.077356
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    color_formatter = ColorFormatter(env, explicit_json=True, color_scheme="planet")
    assert color_formatter.explicit_json == True
    assert color_formatter.formatter == Terminal256Formatter(style='planet')
    color_formatter = ColorFormatter(env, explicit_json=True)
    assert color_formatter.explicit_json == True
    assert color_formatter.formatter == Terminal256Formatter(style=DEFAULT_STYLE)


# Generated at 2022-06-13 21:52:09.710111
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class(AUTO_STYLE) != Solarized256Style

# Generated at 2022-06-13 21:52:13.995401
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(colors=256)
    formatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert formatter is not None


# Generated at 2022-06-13 21:52:22.058187
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(colors=256)
    color_formatter = ColorFormatter(env)
    assert color_formatter.http_lexer.name == 'HTTP'
    assert color_formatter.http_lexer.aliases == ['http']
    assert color_formatter.formatter.name == 'Terminal256'

    color_formatter = ColorFormatter(env, color_scheme=SOLARIZED_STYLE)
    assert color_formatter.formatter.style == Solarized256Style



# Generated at 2022-06-13 21:52:32.223398
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.core import main

    env = main.build_environment()
    # env.colors = 256  # env.colors are None
    # assert not ColorFormatter(env, explicit_json=False, color_scheme='solarized').enabled

    # env.colors = 256
    # assert ColorFormatter(env, explicit_json=False, color_scheme='solarized').enabled
    # assert ColorFormatter(env, explicit_json=False, color_scheme='fruity').enabled
    # assert ColorFormatter(env, explicit_json=False, color_scheme='auto').enabled
    # assert not ColorFormatter(env, explicit_json=False, color_scheme='none').enabled


# Generated at 2022-06-13 21:52:36.649199
# Unit test for function get_lexer
def test_get_lexer():
    # An HTML body should resolve to the HTML lexer
    assert get_lexer('application/xhtml+xml', body='<html/>')

    # A JSON body should resolve to the JSON lexer
    assert get_lexer('application/x-www-form-urlencoded', body='{}')

    # A not-JSON body should resolve to no lexer
    assert not get_lexer('application/x-www-form-urlencoded', body='foo')

# Generated at 2022-06-13 21:52:53.732225
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    #Test a request
    result = pygments.lex(code="GET / HTTP/1.1", lexer=lexer)
    assert list(result) == [
        (pygments.token.Name.Function, 'GET'),
        (pygments.token.Text, ' '),
        (pygments.token.Name.Namespace, '/'),
        (pygments.token.Text, ' '),
        (pygments.token.Keyword.Reserved, 'HTTP'),
        (pygments.token.Operator, '/'),
        (pygments.token.Number, '1.1')
    ]
    #Test a request with a name/value header
    result = pygments.lex(code="GET / HTTP/1.1\nHost: localhost", lexer=lexer)

# Generated at 2022-06-13 21:53:05.106810
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import httpie
    from httpie.context import Environment
    from httpie.compat import is_windows
    from httpie import ExitStatus
    from httpie.output.streams import DEVNULL
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.colors import ColorFormatter
    from pytest import raises
    from pytest_httpie.test_mocks import HTTP_OK
    import requests

    # OS-specific settings, because the Solarized256Style is only available
    # on Windows.
    if is_windows:
        color_scheme = Solarized256Style
    else:
        color_scheme = DEFAULT_STYLE

    # Create a shortened ColorFormatter class that only tests the method
    # format_body.

# Generated at 2022-06-13 21:53:16.958209
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    # Request-Line
    assert(lexer.get_tokens_unprocessed(
        'GET / HTTP/1.1\r\n') ==
      [(6, pygments.token.Keyword.Reserved),
       (1, pygments.token.Operator),
       (1, pygments.token.Text),
       (3, pygments.token.Name.Namespace),
       (1, pygments.token.Text),
       (3, pygments.token.Number),
       (1, pygments.token.Text),
       (5, pygments.token.Name.Function),
       (1, pygments.token.Text)])
    # Response Status-Line

# Generated at 2022-06-13 21:53:29.630017
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment()
    env.colors = True
    formatter = ColorFormatter(env, color_scheme="dark")
    assert(formatter.format_headers('GET / HTTP/1.1\nHost: localhost\n\n') == "\x1b[32mGET\x1b[39m \x1b[0m/\x1b[39m \x1b[34mHTTP/1.1\x1b[39m\n\x1b[33mHost\x1b[39m: \x1b[1mlocalhost\x1b[22m\n")


# Generated at 2022-06-13 21:53:34.979794
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # GIVEN
    body= "{\n  \"id\": 1,\n  \"name\": \"A green door\",\n  \"price\": 12.50,\n  \"tags\": [\"home\", \"green\"]\n}"
    mime="application/json"
    explicit_json=False

    # WHEN
    lexer = get_lexer(mime, explicit_json, body)

    # THEN
    assert lexer == pygments.lexers.get_lexer_by_name('json')



# Generated at 2022-06-13 21:53:36.575457
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    http_lexer = SimplifiedHTTPLexer()

# Generated at 2022-06-13 21:53:39.457226
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    simplifier = SimplifiedHTTPLexer()
    print(simplifier.get_tokens_unprocessed("test"))

# Generated at 2022-06-13 21:53:53.214232
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    assert '' == ColorFormatter.format_headers('')
    assert '\x1B[1mGET / HTTP/1.1\x1B[0m' == ColorFormatter.format_headers('GET / HTTP/1.1\r\n')

# Generated at 2022-06-13 21:53:56.054571
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    lexer = get_lexer(
        mime='text/plain',
        explicit_json=False,
        body='[{"name":"James"}]'
    )
    assert isinstance(lexer, pygments.lexers.JsonLexer)

# Generated at 2022-06-13 21:53:59.830260
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert hasattr(lexer, 'name')
    assert hasattr(lexer, 'aliases')
    assert hasattr(lexer, 'filenames')
    assert hasattr(lexer, 'tokens')

# Generated at 2022-06-13 21:54:18.747482
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.context import Environment

    (env, _, _) = Environment().get_app_components()
    cf = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)

    lexer = cf.get_lexer_for_body(
        mime='application/json',
        body='{"foo": "bar"}'
    )
    assert lexer == pygments.lexers.get_lexer_by_name('json')

    lexer = cf.get_lexer_for_body(
        mime='application/vnd.example.v1+json',
        body='{"foo": "bar"}'
    )
    assert lexer == pygments.lexers.get_lexer_by_name('json')

    lexer = cf.get_lexer_

# Generated at 2022-06-13 21:54:26.564367
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import unittest
    import tempfile
    import os
    import json

    class ColorFormatterTest(unittest.TestCase):
        def test_format_body(self):
            json_string = '{"a": "b"}'
            #: has to create a tempfile because format_body only works on files
            with tempfile.NamedTemporaryFile(mode='w+') as tmpfile:
                tmpfile.write(json_string)
                tmpfile.seek(0)
                #: for some reason, the body doesn't actually get written to the file?
                #: The syntax highlight doesn't work, so we have to read from the tempfile
                #: to make sure that the file is written to
                #: Note that format_body doesn't return anything

# Generated at 2022-06-13 21:54:38.308150
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import main
    args = main.parser.parse_args(args=['--verbose'])

    formatter = ColorFormatter(args.env)

    body_color = formatter.format_body(
        body='{"a": 0}',
        mime='application/json'
    )
    assert len(body_color.split('\n')) == 1
    assert body_color.find('\x1b[0') == -1
    assert body_color.find('\x1b[1') != -1

    body_color = formatter.format_body(
        body='<html></html>',
        mime='text/html'
    )
    assert len(body_color.split('\n')) == 1
    assert body_color.find('\x1b[0')

# Generated at 2022-06-13 21:54:48.138056
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.compat import http_client
    from httpie.context import Environment
    from httpie.models import Response

    env = Environment(colors=256)
    headers = 'GET / HTTP/1.1\nContent-Type: application/json\n\n'
    body = '{}\n'
    response = Response(
        http_version=http_client.HTTP_1_1,
        status_code=http_client.OK,
        headers=headers,
        content=body,
    )

    formatter = ColorFormatter(env, color_scheme='solarized')

    assert formatter.format_body(body, 'application/json') == '{\n'

# Generated at 2022-06-13 21:55:02.790230
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    color_formatter = ColorFormatter(env=Environment())
    assert color_formatter.get_lexer_for_body(
        "application/json",
        body='{ "a": 1 }'
    ) is not None
    assert color_formatter.get_lexer_for_body(
        "application/json",
        body='{"a": 1}'
    ) is not None
    assert color_formatter.get_lexer_for_body(
        "application/json",
        body='{}'
    ) is not None
    assert color_formatter.get_lexer_for_body(
        "application/json",
        body='{ "a": 1, }'
    ) is not None

# Generated at 2022-06-13 21:55:13.499179
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2022-06-13 21:55:17.282033
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']

# Generated at 2022-06-13 21:55:26.567129
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    """
    Unit tests for class ColorFormatter.
    """
    env = Environment()
    formatter = ColorFormatter(env)

    json_str = ("[{\"name\":\"wuji\", \"age\":\"20\"},"
                "{\"name\":\"yihui\", \"age\":\"18\"}]")
    mime = "application/json"
    formatter_result = formatter.format_body(
        body=json_str,
        mime=mime
    )
    assert (formatter_result
            == ("[{\"name\":\"wuji\", \"age\":\"20\"},"
                "{\"name\":\"yihui\", \"age\":\"18\"}]")
            )

    html_str = ("<title>test</title>"
                "<h1>test</h1>")

# Generated at 2022-06-13 21:55:40.113504
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.cli.terminal import get_style, httpie_style
    from httpie.plugins import Plugin
    from httpie import cli

    class ColorFormatterMocked(ColorFormatter):
        _env = None
        _explicit_json = None
        _color_scheme = None

        def __init__(self, env_mock, explicit_json_mock, color_scheme_mock):
            super().__init__(env_mock, explicit_json_mock,
                             color_scheme_mock)
            self._env = env_mock
            self._explicit_json = explicit_json_mock
            self._color_scheme = color_scheme_mock

    class Env:
        stdout_isatty = True
        colors = 256

# Generated at 2022-06-13 21:55:43.466425
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter(Environment(colors=True))
    assert ColorFormatter(Environment(colors=256))
    assert ColorFormatter(Environment(colors=256), color_scheme=DEFAULT_STYLE)



# Generated at 2022-06-13 21:56:16.631119
# Unit test for function get_lexer
def test_get_lexer():
    ok_(get_lexer('application/json') is not None)  # JSON
    ok_(get_lexer('application/json', True, '{}') is not None)
    ok_(get_lexer('application/json', True, 'foo') is None)

    ok_(get_lexer('application/xml') == TextLexer)  # XML
    ok_(get_lexer('application/xml', True, '<foo/>') is not None)
    ok_(get_lexer('application/xml', True, 'foo') == TextLexer)

    ok_(get_lexer('application/yaml') == TextLexer)  # YAML
    ok_(get_lexer('application/yaml', True, '{}') is not None)

# Generated at 2022-06-13 21:56:29.355674
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie import cli
    from httpie.compat import is_windows
    from httpie.output.streams import RAW_STREAM_HEADER_FILTER, RAW_STREAM_BODY_WRITER
    from httpie.output.writers import RAW_WRITER
    env = cli.Environment(colors=256,
                          stdin=RAW_STREAM_HEADER_FILTER,
                          stdout=RAW_STREAM_BODY_WRITER,
                          stderr=RAW_WRITER)
    formatter = ColorFormatter(env,
        explicit_json=False,
        color_scheme='solarized')

    # Test format_headers

# Generated at 2022-06-13 21:56:43.628301
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    http_lexer = ColorFormatter(Environment(colors=0), explicit_json=0, color_scheme="fruity")
    assert http_lexer.enabled == False
    http_lexer = ColorFormatter(Environment(colors=256), explicit_json=0, color_scheme="fruity")
    assert http_lexer.http_lexer == SimplifiedHTTPLexer
    assert http_lexer.formatter == Terminal256Formatter
    http_lexer = ColorFormatter(Environment(colors=16), explicit_json=0, color_scheme="fruity")
    assert http_lexer.http_lexer == PygmentsHttpLexer
    assert http_lexer.formatter == TerminalFormatter


# Generated at 2022-06-13 21:56:48.218688
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    try:
        colorFormatter = ColorFormatter('httpie', explicit_json=False, color_scheme='fruity')
        assert isinstance(colorFormatter, ColorFormatter)
    except:
        print("Fail to create ColorFormatter")

# Generated at 2022-06-13 21:56:56.493812
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(True, 256)
    f = ColorFormatter(env, False, 'solarized')

    assert(delegate.enabled == True)
    assert(delegate.formatter.name == 'Terminal256Formatter')
    assert(delegate.http_lexer.name == 'SimplifiedHTTP')
    assert(delegate.explicit_json == False)



# Generated at 2022-06-13 21:57:06.126225
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    """
    Unit test for constructor of class ColorFormatter.
    """

    # Test cases
    environment = 'httpie-api-tests'
    explicit_json = True
    color_scheme = '256-colors'
    kwargs = {}

    # Constructor
    color_formatter = ColorFormatter(
        env=environment,
        explicit_json=explicit_json,
        color_scheme=color_scheme,
        **kwargs,
    )

    # Expected results
    expected_explicit_json = explicit_json
    expected_color_scheme = color_scheme

    # Assertions
    assert color_formatter.explicit_json == expected_explicit_json
    assert color_formatter.color_scheme == expected_color_scheme

# Generated at 2022-06-13 21:57:13.491138
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():

    def f1(x):
        return x

    def f2(x):
        return x

    res = ColorFormatter(0, f1, f2, explicit_json=False, color_scheme='auto')
    assert res.enabled
    assert res.group_name == 'colors'
    assert res.explicit_json == False
    assert str(type(res.formatter)) == "<class 'pygments.formatters.terminal.TerminalFormatter'>"
    assert str(type(res.http_lexer)) == "<class '__main__.SimplifiedHTTPLexer'>"

    res = ColorFormatter(256, f1, f2, explicit_json=False, color_scheme='solarized')
    assert res.enabled
    assert res.group_name == 'colors'
    assert res

# Generated at 2022-06-13 21:57:23.848216
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter = ColorFormatter(False, AUTO_STYLE)
    print(color_formatter.format_headers("Content-Type: application/json"))
    print(color_formatter.format_body("{\"a\": 1}", "application/json"))
    print(color_formatter.get_lexer_for_body("application/json", "{\"a\": 1}"))


if __name__ == '__main__':
    # Unit test
    test_ColorFormatter()

# Generated at 2022-06-13 21:57:27.078901
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(auto_env=False, colors=256,
                      style='solarized', vars={})
    ColorFormatter(env)

# Generated at 2022-06-13 21:57:35.942544
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie import __version__
    from httpie.config import DEFAULT_CONFIG_DIR

    env = Environment(
        colors=256,
        config_dir=DEFAULT_CONFIG_DIR,
        version=__version__,
    )
    color_formatter = ColorFormatter(env, explicit_json=False, color_scheme=AUTO_STYLE, **kwargs)
    assert color_formatter.formatter.style == Solarized256Style
    assert color_formatter.http_lexer == SimplifiedHTTPLexer
    assert color_formatter.explicit_json == False

# Generated at 2022-06-13 21:57:50.748473
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # test for default parameters
    c = ColorFormatter(env=Environment(), explicit_json=False, color_scheme='auto')
    assert c.explicit_json==False
    assert c.formatter.__class__.__name__=="TerminalFormatter"
    assert c.http_lexer.__class__.__name__=="SimplifiedHTTPLexer"
    # test for explicit_json=True
    c = ColorFormatter(env=Environment(), explicit_json=True, color_scheme='auto')
    assert c.explicit_json==True



# Generated at 2022-06-13 21:57:53.495855
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    try:
        formatter = ColorFormatter(Environment(), None)
        assert formatter
    except:
        assert False

# Generated at 2022-06-13 21:57:57.406635
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    env.colors = 256
    formatter = ColorFormatter(env=env, explicit_json=True)
    print(formatter.http_lexer)

# Generated at 2022-06-13 21:58:04.009505
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Create an environment
    env = Environment()
    env.colors = 256

    # Create a ColorFormatter
    color_scheme='monokai'
    color_formatter = ColorFormatter(env=env, color_scheme=color_scheme)
    assert(color_formatter.color_scheme == color_scheme)
    assert(color_formatter.formatter.style == 'monokai')

# Generated at 2022-06-13 21:58:06.690824
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter(None).enabled == False
    assert ColorFormatter(Environment(colors=256)).enabled == True

# Generated at 2022-06-13 21:58:14.273106
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    color_formatter = ColorFormatter(env=env)
    assert color_formatter.enabled == True
    assert color_formatter.explicit_json == False
    assert color_formatter.formatter.__class__.__name__ == \
        'TerminalFormatter'
    assert color_formatter.http_lexer.__class__.__name__ == \
        'SimplifiedHTTPLexer'
    assert color_formatter.group_name == 'colors'
    assert color_formatter.arg_name == 'colors'

# Generated at 2022-06-13 21:58:24.166791
# Unit test for function get_lexer
def test_get_lexer():
    def get_lexer_name(mime_type, data=''):
        return get_lexer(mime_type, body=data).name

    assert get_lexer_name('application/json') == 'JSON'
    assert get_lexer_name('application/javascript') == 'JavaScript'
    assert get_lexer_name('application/x-javascript') == 'JavaScript'
    assert get_lexer_name('text/javascript') == 'JavaScript'
    assert get_lexer_name('text/x-javascript') == 'JavaScript'
    assert get_lexer_name('text/x-python') == 'Python'
    assert get_lexer_name('application/vnd.google-earth.kml+xml') == 'XML'

# Generated at 2022-06-13 21:58:29.506062
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    f = ColorFormatter(Environment(colors=True, style='solarized'))
    assert isinstance(f, FormatterPlugin)
    assert f.enabled
    assert isinstance(f.formatter, Terminal256Formatter)
    assert f.formatter.style == Solarized256Style
    assert f.http_lexer == SimplifiedHTTPLexer
    assert f.explicit_json == False


# Generated at 2022-06-13 21:58:39.518737
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.context import Environment
    kwargs = {
        'env': Environment(),
        'explicit_json': True,
        'color_scheme': 'solarized',
        'force_colors': True,
        'style': 'solarized',
        'colors': 256,
        'stdout_isatty': True,
    }
    cf = ColorFormatter(**kwargs)
    assert cf.explicit_json == True
    assert cf.formatter.style == Solarized256Style
    assert cf.http_lexer == SimplifiedHTTPLexer
    assert cf.enabled == True

__all__ = (env, ColorFormatter, get_lexer)

# Generated at 2022-06-13 21:58:41.978818
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    c = ColorFormatter(Environment())

# Generated at 2022-06-13 21:59:01.527951
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('application/json')
    assert get_lexer('application/vnd.api+json')

# Generated at 2022-06-13 21:59:04.212680
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.client import Environment

    env = Environment()
    env.colors = True
    cf = ColorFormatter(env)
    assert cf.enabled == True

# Generated at 2022-06-13 21:59:06.322742
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter


# Generated at 2022-06-13 21:59:13.540101
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('application/json')
    assert get_lexer('application/json+whatever')
    assert get_lexer('application/whatever+json')
    assert get_lexer('application/whatever+json', explicit_json=True)
    assert get_lexer('application/json', explicit_json=True,
                     body='{"key": "value"}')
    assert not get_lexer('application/whatever', explicit_json=True)

# Generated at 2022-06-13 21:59:19.715250
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    env.colors = 256
    explicit_json = False
    color_scheme = DEFAULT_STYLE
    test_ColorFormatter = ColorFormatter(env, explicit_json, color_scheme)
    assert test_ColorFormatter.formatter == Terminal256Formatter(style=Solarized256Style)
    assert test_ColorFormatter.http_lexer == SimplifiedHTTPLexer
    assert test_ColorFormatter.explicit_json == False


# Generated at 2022-06-13 21:59:20.952662
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    ColorFormatter(Environment())

# Generated at 2022-06-13 21:59:27.550778
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import httpie.cli

    args = httpie.cli.parser.parse_args([])
    args.color = True

    env = httpie.cli.environment.Environment(args)

    color_formatter1 = ColorFormatter(env, explicit_json=False, color_scheme="auto")
    color_formatter2 = ColorFormatter(env, explicit_json=False, color_scheme="solarized")
    color_formatter3 = ColorFormatter(env, explicit_json=False, color_scheme="xcode")
    print(color_formatter1)
    print(color_formatter2)
    print(color_formatter3)

# Generated at 2022-06-13 21:59:40.255289
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import unittest, os
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    print(os.getcwd())
    env = Environment(
        colors=256,
        stdout_isatty=True,
        stdin_isatty=True,
        stdout=open(os.devnull, 'w'),
        stdin=open(os.devnull, 'r'),
    )
    colorformatter = ColorFormatter(env)
    class ColorFormatterTestCase(unittest.TestCase):
        def test_format_headers_should_return_type_str(self):
            formatted_headers = colorformatter.format_headers('headers')
            self.assertTrue(isinstance(formatted_headers, str))

# Generated at 2022-06-13 21:59:44.614845
# Unit test for function get_lexer
def test_get_lexer():
    assert isinstance(get_lexer('application/json'), PygmentsHttpLexer)
    assert isinstance(get_lexer('application/json', body='{}'), PygmentsHttpLexer)



# Generated at 2022-06-13 21:59:57.639259
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter=ColorFormatter(None,explicit_json=False,color_scheme=DEFAULT_STYLE)
    assert formatter.explicit_json==False
    assert formatter.formatter.color_scheme==DEFAULT_STYLE
    assert formatter.http_lexer.name=='HTTP'
    # assert formatter.formatter==TerminalFormatter() or formatter.formatter == Terminal256Formatter()
    # assert formatter.http_lexer==SimplifiedHTTPLexer() or formatter.http_lexer == PygmentsHttpLexer()
    assert formatter.enabled==True

# Generated at 2022-06-13 22:00:19.145080
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    env.colors = True
    formatter = ColorFormatter(env)
    assert formatter.enabled


# Generated at 2022-06-13 22:00:20.392188
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    c = ColorFormatter({})


# Generated at 2022-06-13 22:00:26.595914
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter = ColorFormatter(Environment(colors=True))
    assert formatter.enabled is True
    assert formatter.formatter is not None
    assert formatter.http_lexer is not None
    assert hasattr(formatter, 'format_body')
    assert hasattr(formatter, 'format_headers')
    assert hasattr(formatter, 'get_lexer_for_body')

# Generated at 2022-06-13 22:00:30.198055
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import httpie.output.streams  # noqa
    formatter = ColorFormatter(Environment(colors=256))
    assert formatter.formatter.__class__.__name__ == "Terminal256Formatter"

# Generated at 2022-06-13 22:00:34.981698
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
   from httpie.context import Environment
   test_env = Environment(color=True) 
   env = ColorFormatter(test_env)
   assert env.enabled == True

# Generated at 2022-06-13 22:00:36.154665
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    o = ColorFormatter()

# Generated at 2022-06-13 22:00:49.350694
# Unit test for function get_lexer
def test_get_lexer():
    # Existing mimetype
    assert(get_lexer('text/json') == pygments.lexers.JsonLexer)

    # Mime type with additional chars
    assert(get_lexer('text/json;encoding=utf-8') == pygments.lexers.JsonLexer)

    # Non-existing mimetype
    assert(get_lexer("text/totally-unknown") is None)

    # Empty mimetype
    assert(get_lexer("") is None)

    # None mimetype
    assert(get_lexer(None) is None)

    # Non-available lexer (lexers.json)
    assert(get_lexer("text/python-nonexisting") is None)

    # Non-available lexer (lexers/__init__.py)

# Generated at 2022-06-13 22:01:00.342400
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Initialize Environment
    from httpie import core
    from httpie.context import Environment
    from httpie.plugins import BuiltinPluginManager
    from httpie.config import Config
    from httpie.input import ParseError

    env = Environment(
        stdin=core.StdinBytesIO(b''),
        stdout=core.StdoutBytesIO(),
        config=Config(confdir=None, color=True, plugins=BuiltinPluginManager())
    )
    colorFormatter = ColorFormatter(env, explicit_json=False)
    assert colorFormatter.enabled
    assert colorFormatter.explicit_json == False

    colorFormatter = ColorFormatter(env, explicit_json=True)
    assert colorFormatter.enabled
    assert colorFormatter.explicit_json == True

# Generated at 2022-06-13 22:01:11.835333
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Without colors on.
    env = Environment()
    env.colors = False
    formatter = ColorFormatter(env)
    assert not formatter.enabled

    # With colors on.
    env.colors = True
    formatter = ColorFormatter(env)
    assert formatter.enabled

    # With non-default color scheme.
    env.colors = True
    formatter = ColorFormatter(env, color_scheme=SOLARIZED_STYLE)
    assert formatter.formatter.style == ColorFormatter.get_style_class(SOLARIZED_STYLE)

    # With non-default Content-Type.
    env.colors = True
    formatter = ColorFormatter(env, color_scheme=SOLARIZED_STYLE)
    body = 'hello'