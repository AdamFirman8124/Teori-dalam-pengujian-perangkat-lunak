

# Generated at 2022-06-13 21:51:33.490515
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(
        colors=256,
        stdin=True,
        stdout=True,
        isatty=True
    )
    formatter = ColorFormatter(env=env, color_scheme=DEFAULT_STYLE)

# Generated at 2022-06-13 21:51:45.710044
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # Arrange
    def get_lexer(mime, body):
        cf = ColorFormatter(Environment(), 'auto')
        lexer = cf.get_lexer_for_body(mime, body)
        return lexer

    # Act
    response = get_lexer('application/json', '{"hello":"world"}')
    assert repr(response) == '<Lexer for "JSON" at 0x7f4c4d5f5ea0>'

    response = get_lexer('application/hal+json', '{"hello":"world"}')
    assert repr(response) == '<Lexer for "JSON" at 0x7f4c4d5f5ea0>'

    response = get_lexer('application/vnd.example+json', '{"hello":"world"}')

# Generated at 2022-06-13 21:51:47.851886
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    try:
        SimplifiedHTTPLexer()
    except:
        raise AssertionError("SimplifiedHTTPLexer constructor is broken")

# Generated at 2022-06-13 21:51:49.708352
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter('--ignore-stdin', '--stream')

# Generated at 2022-06-13 21:51:59.793920
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.output import BINARY_SUPPRESSED_NOTICE
    from httpie.plugins import builtin

    env = Environment()
    env.stdout = env.stderr = six.StringIO()
    color_scheme = DEFAULT_STYLE
    explicit_json = False

    formatter = ColorFormatter(env=env, explicit_json=explicit_json,
                               color_scheme=color_scheme)

    formatter.env.colors = 256
    headers = 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
    assert not formatter.format_headers(headers).startswith(BINARY_SUPPRESSED_NOTICE)



# Generated at 2022-06-13 21:52:08.976005
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.plugins import DEFAULT_PLUGINS
    from httpie.output.streams import StdoutBytesIO
    colorFormatter = ColorFormatter(
        env=Environment(
            colors=256,
            config_dir=None,
            output_format='colors',
            output_options=None,
            stdin_isatty=False,
            stdout_isatty=True,
            plugins=DEFAULT_PLUGINS,
        ),
        explicit_json=False,
        color_scheme='solarized',
        stdout=StdoutBytesIO(),
    )
    assert isinstance(colorFormatter.get_style_class('solarized'), Solarized256Style)

# Generated at 2022-06-13 21:52:22.141558
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    c = ColorFormatter(environment=None)
    c.enabled = True
    input_ = 'GET / HTTP/1.1\r\nHost: www.httpbin.org\r\nAccept: */*\r\nUser-Agent: HTTPie/1.0.2\r\n'

# Generated at 2022-06-13 21:52:29.058568
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    try:
        import pygments.lexers.special
        pygments.lexers.special.HttpLexer = SimplifiedHTTPLexer
        import pygments.lexers.compiled
        pygments.lexers.compiled.HttpLexer = SimplifiedHTTPLexer
    except ImportError:
        pass
    http_lexer = SimplifiedHTTPLexer()
    example_request = """\
GET /api/user HTTP/1.1
Host: example.com
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8
User-Agent: HTTPie/0.9.2
"""

# Generated at 2022-06-13 21:52:37.056152
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    color_formatter = ColorFormatter(Environment(), False, 'solarized')
    result = color_formatter.format_headers(
        'GET / HTTP/1.1\r\nHost: localhost:8080\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nUser-Agent: HTTPie/0.9.8\r\n\r\n'
    )

# Generated at 2022-06-13 21:52:41.855548
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    """
    make sure we can init a ColorFormatter without errors.
    """
    environment = Environment()
    formatter = ColorFormatter(env=environment)
    assert isinstance(formatter, ColorFormatter)

# Generated at 2022-06-13 21:53:00.883791
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import pytest
    from httpie.context import Environment
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    env = Environment()
    formatter = ColorFormatter(env)

    def get_formatted_body(mime: str, body: str, explicit_json=False):
        return formatter.format_body(
            body=body,
            mime=mime,
            explicit_json=explicit_json,
        )

    with pytest.raises(Exception):
        get_formatted_body('text/html', '<html><body>Hello!</body></html>')

    assert get_formatted_body('text/html+jinja', '<html><body>Hello!</body></html>') is None


# Generated at 2022-06-13 21:53:10.861186
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class MockResponse(object):
        body = ''
        headers = {'Content-Type': ''}
    class MockEnvironment(object):
        colors = 256
    env = MockEnvironment()
    color = ColorFormatter(env)
    body = color.format_body('', 'text/html')
    assert body == ''
    body = color.format_body('<html>', 'text/html')
    assert body != '<html>'
    body = color.format_body('{}', 'application/json')
    assert body != '{}'
    body = color.format_body('{}', 'application/json')
    assert body != '{}'
    body = color.format_body('{}', 'application/json')
    assert body != '{}'

# Generated at 2022-06-13 21:53:17.370415
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    f = ColorFormatter(
        env="env",
        explicit_json=True,
        color_scheme="color_scheme",
        **{"kwargs": "kwargs"}
    )
    assert f.group_name == 'colors'
    assert f.explicit_json is True
    assert f.formatter is not None
    assert f.http_lexer is not None

# Generated at 2022-06-13 21:53:29.580235
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.colors import ColorFormatter
    from httpie.context import Environment
    import os
    env = Environment(colors=256)
    f = ColorFormatter(env=env, color_scheme='solarized')
    # headers
    headers = '''Content-Length: 628
Content-Type: application/json
Date: Wed, 02 Aug 2017 17:05:46 GMT
Server: WSGIServer/0.1 Python/2.7.12
X-Powered-By: Flask
'''

# Generated at 2022-06-13 21:53:37.600124
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    text = '''
POST /post HTTP/1.1
Host: example.com
Accept: application/json
User-Agent: HTTPie/0.9.2
Content-Type: application/json; charset=utf-8
Content-Length: 15

{"foo": "bar"}
    '''
    m = 'application/json'
    for t, content in lexer.get_tokens(text.strip()):
        print("%s%s" % (content, t), end='\n' if t in pygments.token.Text else '')

# Generated at 2022-06-13 21:53:50.532864
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    text = '''
GET / HTTP/1.1\r
Content-Type: application/json\r
X-Foo: Bar\r
\r
{"hello": "world"}
'''

# Generated at 2022-06-13 21:53:58.829583
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    request_line = 'GET / HTTP/1.1'
    status_line = 'HTTP/1.1 200 OK'
    headers = [
        'User-Agent: HTTPie/1.0.0',
        'Accept: application/json',
        'Content-Length: 29'
    ]

    for line in [request_line, status_line] + headers:
        print(pygments.highlight(
            code=line,
            lexer=SimplifiedHTTPLexer(),
            formatter=Terminal256Formatter(
                style=Solarized256Style
            )
        ))

# Generated at 2022-06-13 21:54:00.785487
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    l = SimplifiedHTTPLexer()
    l.get_tokens_unprocessed("""GET / HTTP/2
Content-Type: text/plain

hello""")

# Generated at 2022-06-13 21:54:07.979206
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    class TestEnvironment(Environment):
        def __init__(self):
            self.colors = True

    env = TestEnvironment()
    formatter = ColorFormatter(env=env)
    assert formatter.get_lexer_for_body('application/json', b'') is not None
    assert formatter.get_lexer_for_body('application/json', b'{}') is not None
    assert formatter.get_lexer_for_body('application/json', b'{') is not None
    assert formatter.get_lexer_for_body('application/json', b'test') is not None
    assert formatter.get_lexer_for_body('application/json', b'{}') is not None

# Generated at 2022-06-13 21:54:19.143174
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    tokens = [
        (t, v) for t, v in SimplifiedHTTPLexer().get_tokens_unprocessed(
            'GET /api/user/123 HTTP/1.1\n'
            'Content-Type: application/json\n'
            '\n'
            '{ "username" : "user1" }\n'
        )
    ]

# Generated at 2022-06-13 21:54:32.649821
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter = ColorFormatter(None)
    assert color_formatter.enabled

# Generated at 2022-06-13 21:54:43.588058
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    color_formatter = ColorFormatter(Environment())
    body_text = 'Lorem ipsum dolor sit amet'
    formated_body_text = color_formatter.format_body(body_text, 'text/plain')
    assert body_text == formated_body_text
    formated_body_json = color_formatter.format_body(
        '{"foo": "bar"}', 'application/json'
    )
    assert formated_body_json.startswith(
        '\x1b[38;5;%sm{\x1b[39m\x1b[38;5;%sm"'%(
            255, 34)
    )

# Generated at 2022-06-13 21:54:54.721650
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import sys
    import os
    sys.path.append('..')
    from core import main
    env = main.Environment(colors=True)
    headers = 'Cache-Control: private\r\nContent-Type: text/html; charset=utf-8\r\nServer: Microsoft-IIS/7.5\r\nX-AspNet-Version: 4.0.30319\r\nX-Powered-By: ASP.NET\r\nDate: Tue, 20 Jun 2017 13:28:27 GMT\r\nContent-Length: 83718'
    formatter = ColorFormatter(env)

# Generated at 2022-06-13 21:55:00.602703
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    color_formatter = ColorFormatter(Environment(None, None, None), False, DEFAULT_STYLE, None)

    # return False when lexer is not found
    assert color_formatter.format_body('body', 'text/plain') == 'body'
    # return True when lexer is found
    assert color_formatter.format_body('body', 'text/html') != 'body'

# Generated at 2022-06-13 21:55:08.706920
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    """
        Test the constructor of class SimplifiedHTTPLexer.
    """
    from httpie.output.formatters.colors import SimplifiedHTTPLexer

    # Test case 1: Check token names.
    simplifiedHTTPLexer = SimplifiedHTTPLexer()
    tokens = simplifiedHTTPLexer.tokens['root']
    # Check the first three tokens.
    requestLineTokens = ['Keyword.Function', 'Text', 'Name.Namespace', 'Text', 'Keyword.Reserved', 'Operator', 'Number']
    responseStatusLineTokens = ['Keyword.Reserved', 'Operator', 'Number', 'Text', 'Number', 'Text', 'Name.Exception']
    headerToken = ['Name.Attribute', 'Text', 'Operator', 'Text', 'String']

# Generated at 2022-06-13 21:55:20.062433
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # Initialize variables
    env = Environment()
    mime = 'text/plain'
    body = '' # Expected lexer: TextLexer

    # Lexer to be used
    lexer = pygments.lexers.get_lexer_by_name('text')

    # Initialize formatter
    formatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)

    # Actual lexer and expected lexer
    actual = formatter.get_lexer_for_body(mime, body)
    expected = lexer
    assert actual == expected

# Generated at 2022-06-13 21:55:26.186078
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment({'HTTPIE_COLORS': '256'})
    color_formatter = ColorFormatter(env=env)
    formatter = color_formatter.formatter
    assert isinstance(formatter, Terminal256Formatter)
    assert formatter.style == Solarized256Style
    style_class = color_formatter.get_style_class('solarized256')
    assert style_class == Solarized256Style
    assert color_formatter.get_lexer_for_body('application/json', '{"key":"value"}') is not None

# Generated at 2022-06-13 21:55:39.942514
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from .color import ColorFormatter
    from . import utils
    from .output import JsonFormat
    f = ColorFormatter(utils.Environment(colors=256))
    assert f.get_lexer_for_body('application/json', '{"a":1}') == pygments.lexers.get_lexer_by_name('json')
    assert f.get_lexer_for_body('application/json', 'x') == None
    assert f.get_lexer_for_body('application/json; foo=bar; baz=foo', '{"a":1}') == pygments.lexers.get_lexer_by_name('json')
    assert f.get_lexer_for_body('application/json', '{"a":1}', True) == pygments.lexers.get_lexer_by

# Generated at 2022-06-13 21:55:48.892831
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    test_cases = (
        # Expected lexer, content type, body
        (None, '', 'x'),
        (None, 'x', 'x'),
        (None, 'text/x', 'x'),
        (None, 'text/c+x', 'x'),
        (None, 'text/css', 'x'),
        (None, 'text/json', 'x'),
        (None, 'text/json', '{x:"x"}'),
        (pygments.lexers.JSONLexer, 'text/json', '{"x":"x"}'),
        (pygments.lexers.JSONLexer, 'application/json', 'x'),
        (pygments.lexers.JSONLexer, 'application/json', '{"x":"x"}')
    )

# Generated at 2022-06-13 21:55:49.405603
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter

# Generated at 2022-06-13 21:56:09.588950
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import main
    class MyEnvironment(Environment):
        def __init__(self):
            super().__init__()
            self.colors = 256

    environment = MyEnvironment()
    environment.stdout_isatty = True
    color_formatter = ColorFormatter(env=environment)
    body = "test body"
    mime = "application/json"

    result = color_formatter.format_body(body, mime)
    assert result == "test body"

# Generated at 2022-06-13 21:56:12.218433
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    formatter = ColorFormatter(env, explicit_json=False, color_scheme="solarized")

# Generated at 2022-06-13 21:56:20.402462
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    assert get_lexer("foo/bar") == None
    assert get_lexer("text/foo") == None
    assert get_lexer("application/json") == pygments.lexers.get_lexer_by_name('json')
    assert get_lexer("application/json", explicit_json=True) == pygments.lexers.get_lexer_by_name('json')
    assert get_lexer("application/json", explicit_json=True, body="{'x': 1}") == pygments.lexers.get_lexer_by_name('json')

# Generated at 2022-06-13 21:56:27.400459
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import httpie.output.formatters.colors
    env = Environment(colors=True)
    formatter = httpie.output.formatters.colors.ColorFormatter(env)
    headers = "HTTP/1.1 200 OK\n" \
              "Content-Type: text/html; charset=UTF-8\n" \
              "Server: ExampleServer\n" \
              "X-XSS-Protection: 1; mode=block\n" \
              "Date: Sat, 25 Nov 2017 22:41:17 GMT\n" \
              "Content-Length: 14\n" \
              "\n" \
              "Hello World."

# Generated at 2022-06-13 21:56:37.126844
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    assert get_lexer('application/json', explicit_json=False, body='{}')
    assert get_lexer('text/plain', explicit_json=False, body='{}')
    assert get_lexer('text/plain', explicit_json=False, body='')
    assert get_lexer('application/json', explicit_json=True, body='{}')
    assert get_lexer('text/plain', explicit_json=True, body='{}')
    assert not get_lexer('text/plain', explicit_json=True, body='')

# Generated at 2022-06-13 21:56:44.390785
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    from pygments.token import Token
    assert SimplifiedHTTPLexer.tokens['root'][0][1] == pygments.lexer.bygroups(
        pygments.token.Name.Function,
        pygments.token.Text,
        pygments.token.Name.Namespace,
        pygments.token.Text,
        pygments.token.Keyword.Reserved,
        pygments.token.Operator,
        pygments.token.Number
    )

# Generated at 2022-06-13 21:57:00.225120
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(None)
    assert formatter.get_lexer_for_body('application/json', '')
    assert formatter.get_lexer_for_body('application/json', '{}')
    assert formatter.get_lexer_for_body(
        'application/json', '{"a":"b"}'
    ) is pygments.lexers.get_lexer_by_name('json')

    assert not formatter.get_lexer_for_body('application/xml', '')
    assert not formatter.get_lexer_for_body('application/xml', '<a>')

# Generated at 2022-06-13 21:57:09.400321
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(Environment(colors=256))
    assert formatter.get_lexer_for_body('text/plain', 'some text') is None

    lexer = formatter.get_lexer_for_body('text/html', '')
    assert lexer.__name__ == 'HtmlLexer'

    lexer = formatter.get_lexer_for_body('text/xml', '')
    assert lexer.__name__ == 'XmlLexer'

    lexer = formatter.get_lexer_for_body('application/json', '')
    assert lexer.__name__ == 'JsonLexer'

    # This is tricky.
    lexer = formatter.get_lexer_for_body('application/x-bogus', '')
    assert lexer is None



# Generated at 2022-06-13 21:57:17.155386
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # Given
    http_formatter_mock = ColorFormatter(
        Environment(colors=1, stdout_isatty=False),
    )

    # When
    lexer = http_formatter_mock.get_lexer_for_body(
        'application/json',
        '{"key":"value"}',
    )

    # Then
    assert lexer is not None
    assert lexer.name == 'JSON'

# Generated at 2022-06-13 21:57:22.793434
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('fruity') != None
    assert ColorFormatter.get_style_class('monokai') != None
    assert ColorFormatter.get_style_class('solarized') != None
    assert ColorFormatter.get_style_class('auto') == None
    assert ColorFormatter.get_style_class('notexisted') == None

# Generated at 2022-06-13 21:57:46.645622
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.compat import is_windows, is_py34
    from httpie.context import Environment

    # Python 3.4 in Windows has issues with ANSI color output.
    # https://github.com/jakubroztocil/httpie/issues/258
    if is_windows and is_py34:
        return

    env = Environment(colors=256)

    # Default case
    body = "text"
    color_formatter = ColorFormatter(env)
    assert color_formatter.format_body(body=body, mime="text/plain") == body

    # JSON case
    body = "{\"text\":\"value\"}"
    color_formatter = ColorFormatter(env)
    assert color_formatter.format_body(body=body, mime="application/json") == body

    #

# Generated at 2022-06-13 21:57:53.146682
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie import ExitStatus

    # Setup
    exit_status = ExitStatus()
    headers = '\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: JSON',
        'Content: text/HTML',
        '',
        ''
    ])
    body = '{"foo":true}'
    # Run
    result = ColorFormatter(exit_status, color_scheme=AUTO_STYLE)
    result = result.format_body(body=body, mime="JSON")
    # Assert
    assert result == '{\n  "\x1b[0;32mfoo\x1b[0m": \x1b[0;33mtrue\x1b[0m'

# Generated at 2022-06-13 21:58:06.061679
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment()
    formatter = ColorFormatter(env)
    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Date: Mon, 24 Nov 2014 16:18:32 GMT\r\n"
        "Server: Apache\r\n"
        "Last-Modified: Tue, 04 Nov 2014 08:09:51 GMT\r\n"
        "ETag: \"f000f4-4e4-5044f44c4cec0\"\r\n"
        "Accept-Ranges: bytes\r\n"
        "Content-Length: 1268\r\n"
        "Content-Type: application/octet-stream\r\n"
        "\r\n"
        "1234567890"
    )
    fmt_headers = formatter.format_headers

# Generated at 2022-06-13 21:58:19.130358
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.output.formatters import get_formatter
    from httpie import ExitStatus

    output_file = None
    env = Environment(colors=256, stdout=output_file, stderr=output_file)
    formatter = get_formatter(env=env)
    assert isinstance(formatter, ColorFormatter)


# Generated at 2022-06-13 21:58:25.985569
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    color_formatter = ColorFormatter({})
    print(color_formatter.format_headers('GET / HTTP/1.1\r\nAccept: text/html'))
    print(color_formatter.format_body('body', 'text/html'))


if __name__ == '__main__':
    test_ColorFormatter_format_body()

# Generated at 2022-06-13 21:58:33.645846
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.plugins.colors import ColorFormatter
    from pygments.styles.default import DefaultStyle
    assert ColorFormatter.get_style_class('default') == DefaultStyle
    assert ColorFormatter.get_style_class('') == DefaultStyle
    assert ColorFormatter.get_style_class('DoesntExist') == DefaultStyle
    assert ColorFormatter.get_style_class('auto') == DefaultStyle

# Generated at 2022-06-13 21:58:35.686885
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    formatter = ColorFormatter(env=env)
    assert formatter != None

# Generated at 2022-06-13 21:58:45.778464
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2022-06-13 21:58:48.640980
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class("manni") is pygments.styles.get_style_by_name("manni")
    assert ColorFormatter.get_style_class("solarized") is Solarized256Style

# Generated at 2022-06-13 21:58:54.846842
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.plugins import FormatterPlugin
    from httpie.output.streams import get_response_stream

    class MyColorFormatter(FormatterPlugin):

        def format_body(self, body:str, mime:str) -> str:
            return "***" + body + "***"

    cf = MyColorFormatter(None)
    env = Environment(colors=256)
    out_stream = get_response_stream(env)
    cf.format_body("hello","")

    assert cf.format_body("hello","") == "***hello***"

# Generated at 2022-06-13 21:59:17.393869
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    c = SimplifiedHTTPLexer()

# Generated at 2022-06-13 21:59:21.295442
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']



# Generated at 2022-06-13 21:59:27.550694
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    assert ColorFormatter.get_lexer_for_body('application/json', 'json')
    assert not ColorFormatter.get_lexer_for_body('application/xml', 'xml')

    assert (ColorFormatter.get_lexer_for_body('application/x-yaml', 'yaml')
            is pygments.lexers.get_lexer_for_filename('h.yaml'))
    assert (ColorFormatter.get_lexer_for_body('application/x-yml', 'yml')
            is pygments.lexers.get_lexer_for_filename('h.yml'))

# Generated at 2022-06-13 21:59:39.230896
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.cli import parser
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin

    class TestFormatter(FormatterPlugin):
        def get_lexer_for_body(self, mime, body):
            return TextLexer()

    args = parser.parse_args([])
    args.colors = True
    args.prettify = True
    env = Environment(args)

    body = '''{
        "a": "1",
        "b": "2",
        "c": "3"
    }'''

    text = TestFormatter(env).format_body(body, None)

    assert text == '\x1b[37m' + body + '\x1b[39m'

# Generated at 2022-06-13 21:59:48.394558
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():

    from httpie.plugins import FormatterPlugin
    from httpie.context import Environment
    
    # Test for class ColorFormatter 
    def test_ColorFormatter():
        """Test for class ColorFormatter"""
        test_formatter = ColorFormatter(
            env=Environment(),
            explicit_json=False,
            color_scheme=SOLARIZED_STYLE,
            **{
                'multiple_lines': False,
                'requires_content_type_header': False,
                'is_streaming_handler': False
            }
        )
        assert test_formatter.formatter.__class__.__name__ == 'Terminal256Formatter', 'method get_style_class of class ColorFormatter returns incorrect style when "color_scheme" parameter is set to "solarized256"'
        assert test_form

# Generated at 2022-06-13 21:59:57.079711
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import unittest

    def verify(self,
               body: str,
               mime: str,
               should_colorize: bool,
               explicit_json: bool = False,
               color_scheme: str = 'auto'):
        env = Environment()
        formatter = ColorFormatter(
            env,
            explicit_json=explicit_json,
            color_scheme=color_scheme,
        )
        result = formatter.format_body(body, mime)
        self.assertEqual(
            result != body,
            should_colorize
        )

    class ColorFormatterTest(unittest.TestCase):
        def test_color_formatter(self):
            verify(self, '{}', 'application/json', True)

# Generated at 2022-06-13 22:00:01.823699
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    fmt = ColorFormatter(
        env=Environment(colors=256),
        color_scheme='solarized',
    )
    assert fmt.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 22:00:11.625270
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    """Test ColorFormatter.format_body
    """
    environment = Environment()
    formatter = ColorFormatter(env=environment)
    output = "Hello"
    mime = "text/plain"
    # Should return the same with no body or mime
    assert(formatter.format_body(None, None) is None)
    assert(formatter.format_body(output, None) == output)
    assert(formatter.format_body(None, mime) is None)
    # Should return a formated body
    assert(formatter.format_body(output, mime) != output)

# Generated at 2022-06-13 22:00:18.866330
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('text/plain') == pygments.lexers.TextLexer
    assert get_lexer('text/html') == pygments.lexers.HtmlLexer
    assert get_lexer('application/json') == pygments.lexers.JsonLexer
    assert get_lexer('application/ebook+epub') == pygments.lexers.EpubLexer
    assert get_lexer('application/x-tar') == pygments.lexers.TarLexer
    assert get_lexer('application/x-gtar') == pygments.lexers.TarLexer
    assert get_lexer('application/tar+gzip') == pygments.lexers.TarGzipLexer
    # Try to resolve a non-lexer-supported MIME type
    assert not get_lexer('application/foo')


# Generated at 2022-06-13 22:00:30.403003
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    class MockEnv(object):
        def __init__(self):
            self.colors = True

    env = MockEnv()
    color = ColorFormatter(env)
    request = 'GET /foo HTTP/1.1\r\nHost: localhost\r\nContent-Type: application/json\r\n'\
              'Accept: application/json\r\nAccept-Encoding: gzip, deflate\r\n\r\n'
    result = color.format_headers(request)