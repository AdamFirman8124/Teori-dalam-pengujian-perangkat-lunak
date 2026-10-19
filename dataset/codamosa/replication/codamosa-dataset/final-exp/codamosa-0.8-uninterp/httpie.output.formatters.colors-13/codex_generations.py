

# Generated at 2022-06-13 21:51:39.342820
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.output.streams import ResponseStream
    from httpie.plugins import FormatterPluginManager

    headers = """\
HTTP/1.1 200 OK
Server: Apache
Content-Length: 60
Content-Type: text/plain
Date: Fri, 04 May 2012 16:07:07 GMT
X-Miku: Hatsune Miku

"""

    response_stream = ResponseStream()
    f = ColorFormatter(env={'colors': 256})
    f.stream = response_stream
    f.manager = FormatterPluginManager()
    f.format_headers(headers)

    from pygments.formatters import Terminal256Formatter
    from pygments.styles import get_style_by_name
    c = f.formatter.get_style_defs(get_style_by_name('solarized256'))

# Generated at 2022-06-13 21:51:50.041169
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    env = Environment(colors=256)
    formatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)


# Generated at 2022-06-13 21:51:54.977849
# Unit test for function get_lexer
def test_get_lexer():
    json_lexer = pygments.lexers.get_lexer_by_name('json')
    assert get_lexer('application/json') is json_lexer
    assert get_lexer('application/notjson') is None
    assert get_lexer('application/json', True, '{"a": 1}') is json_lexer

# Generated at 2022-06-13 21:52:04.206223
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    test_http_string = """GET /test/test_test HTTP/1.1
Host: httpbin.org
Connection: keep-alive
Cache-Control: max-age=0
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip,deflate,sdch
Accept-Language: en-US,en;q=0.8,sl;q=0.6,bs;q=0.4"""
    lexer = SimplifiedHTTPLexer()

# Generated at 2022-06-13 21:52:09.153360
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    """
    The SimplifiedHTTPLexer makes a few assumptions about the structure of HTTP
    messages.  This test checks a few of them.  These situations are really
    corner cases and shouldn't arise in the wild, but we don't want our
    assumptions to cause problems for users.
    """
    l = SimplifiedHTTPLexer()
    def check(code, tokens):
        tokens = [
            (pygments.token.Token.__dict__[type], value)
            for type, value in tokens
        ]
        assert list(l.get_tokens(code)) == tokens

    # Longlines

# Generated at 2022-06-13 21:52:15.491952
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # given
    sut = ColorFormatter(None)
    # when
    actual = sut.format_body('abc', 'text/html')
    # then
    assert '<div' in actual
    assert '\x1b[0m</span>' in actual


# Generated at 2022-06-13 21:52:24.380679
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    # Unit test for method format_headers of class ColorFormatter
    headers_str  = '''HTTP/1.1 200 OK
Server: nginx
Date: Sat, 09 Apr 2016 05:40:35 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Vary: Accept-Encoding
X-RateLimit-Limit: 5000
X-RateLimit-Remaining: 4999
ETag: "a20b6af0ec2e950a8be27e7aa53e28c85a3c91d8"
Cache-Control: max-age=0, private, must-revalidate
X-XSS-Protection: 1'''
    color_formatter = ColorFormatter(None)

# Generated at 2022-06-13 21:52:29.911370
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    string = '''\
HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 01 May 2014 02:06:46 GMT
Content-Length: 2

{}
'''

    lexer = SimplifiedHTTPLexer()
    tokens = list(lexer.get_tokens(string))
    assert tokens[0][0] == pygments.token.Keyword.Reserved
    assert tokens[0][1] == 'HTTP'
    assert tokens[1][0] == pygments.token.Operator
    assert tokens[1][1] == '/'
    assert tokens[2][0] == pygments.token.Number
    assert tokens[2][1] == '1.1'
    assert tokens[3][0] == pygments.token.Text

# Generated at 2022-06-13 21:52:37.649118
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    """Test constructor of class ColorFormatter."""
    # Test 1
    env = Environment(colors=True)
    color_formatter = ColorFormatter(env)
    assert(isinstance(color_formatter.formatter, TerminalFormatter))
    assert(color_formatter.http_lexer is PygmentsHttpLexer)

    # Test 2
    color_formatter = ColorFormatter(env, color_scheme='fruity')
    assert(isinstance(color_formatter.formatter, TerminalFormatter))
    assert(color_formatter.http_lexer is PygmentsHttpLexer)

    # Test 3
    color_formatter = ColorFormatter(env, color_scheme='solarized')
    assert(isinstance(color_formatter.formatter, Terminal256Formatter))

# Generated at 2022-06-13 21:52:41.897901
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    test_env = Environment(colors=256)
    formatter = ColorFormatter(env=test_env)
    style = formatter.get_style_class(SOLARIZED_STYLE)
    assert style == Solarized256Style

# Generated at 2022-06-13 21:53:01.498911
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.formatting import get_formatter_class
    from httpie.context import Environment, EnvironmentRequest

    data = '''HTTP/1.1 200 OK
Content-Length: 15
Content-Type: application/json
Date: Sat, 23 Jun 2018 13:53:53 GMT
Server: Werkzeug/0.14.1 Python/2.7.5

{"key1": "value1"}'''

    formatter_class = get_formatter_class({})
    formatter = formatter_class(
        env=Environment(colors=256, request=EnvironmentRequest(method='GET')),
        color_scheme='solarized'
    )
    color_formatter = formatter.processor_class.group_processor_classes['colors']

    headers = data[:data.index('\n\n')]

# Generated at 2022-06-13 21:53:11.142726
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.plugins import FormatterPlugin
    from httpie import ExitStatus
    from httpie import ExitStatus
    from httpie.output.formatters.colors import ColorFormatter
    from httpie.plugins import PluginManager, get_plugin_manager

    f = ColorFormatter(
        env=Environment(),
        explicit_json=False,
        color_scheme='solarized',
    )

    headers = "ABC: DEF\nDDA:EE\n"
    http_lexer = SimplifiedHTTPLexer()

    formatter = Terminal256Formatter(
        style=Solarized256Style
    )

    pygments.highlight(
        code=headers,
        lexer=http_lexer,
        formatter=formatter,
    ).strip

# Generated at 2022-06-13 21:53:15.802405
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    color_formatter = ColorFormatter(
        env=None,
        color_scheme='none',
    )
    style_class = color_formatter.get_style_class(DEFAULT_STYLE)
    assert style_class == Solarized256Style



# Generated at 2022-06-13 21:53:30.866703
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class Env:
        def __init__(self, colors):
            self.colors = colors

    class ColorFormatter2(ColorFormatter):
       def get_style_class(self, color_scheme):
           if color_scheme != AUTO_STYLE:
               raise ValueError('unexpected color scheme: {}'.format(color_scheme))
           return super().get_style_class(color_scheme)

    env = Env('8')
    color_formatter = ColorFormatter2(env, color_scheme=AUTO_STYLE)
    assert color_formatter.formatter.__class__.__name__ == 'TerminalFormatter'

    env.colors = '256'
    color_formatter = ColorFormatter2(env, color_scheme=AUTO_STYLE)

# Generated at 2022-06-13 21:53:33.935788
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    styles = ['solarized', 'dark']
    for style in styles:
        assert isinstance(ColorFormatter.get_style_class(style),
                          pygments.style.Style)

# Generated at 2022-06-13 21:53:48.689179
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    # call `ColorFormatter` with:
    #  - `env` argument with a value of `Environment` instance that has the
    #    following attributes:
    #      - `colors` set to `256`
    #  - `explicit_json` argument set to `False`
    #  - `color_scheme` argument set to `solarized`
    c = ColorFormatter(
        env=Environment(colors=256),
        explicit_json=False,
        color_scheme="solarized"
    )

    # call `format_headers` of `c` with argument `headers` set to
    # "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n"

# Generated at 2022-06-13 21:53:56.987387
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    """Test method format_body of class ColorFormatter"""
    import httpie
    import tempfile
    import json

    tf = tempfile.NamedTemporaryFile()

    # use the same color_scheme as in ColorFormatter.__init__()
    color_scheme = DEFAULT_STYLE

    # Add mock arguments to Environment() https://stackoverflow.com/a/13499397
    args = '--verbose --pretty=all --stream --download --output=' + tf.name
    env = httpie.Environment({}, args)

    cf = ColorFormatter(
        env=env,
        explicit_json=False,
        color_scheme=color_scheme,
    )
    # JSON
    body = json.dumps({'key': 'value'}, indent=4)

# Generated at 2022-06-13 21:54:05.501090
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment
    from httpie.core import Response
    from httpie.plugins import FormatterPluginManager
    from httpie.output.streams import NO_PIPE
    stdout = NO_PIPE
    cformatter = ColorFormatter(Environment())
    cformatter.enabled = True
    response = Response(
        ff=FormatterPluginManager([cformatter]),
        stdout=stdout,
        color_scheme=DEFAULT_STYLE,
        ctx=Environment(),
        request=None,
        content=True,
        headers=True,
        quiet=False,
        verbose=False,
    )
    result = cformatter.format_body(
        body="<html><body>Hello</body></html>",
        mime="text/html"
    )


# Generated at 2022-06-13 21:54:18.010707
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    import httpie.json
    json_body = "[1,2,3]"
    line_counter = 0

# Generated at 2022-06-13 21:54:26.135555
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    # Request line:
    tok = lexer.get_tokens('GET /foo HTTP/1.1')
    assert isinstance(tok, list)
    assert tok[0][0] == pygments.token.Name.Function
    assert tok[1][1] == ' '
    assert tok[2][0] == pygments.token.Name.Namespace
    assert tok[3][1] == ' '
    assert tok[4][0] == pygments.token.Keyword.Reserved
    assert tok[5][0] == pygments.token.Operator
    assert tok[6][0] == pygments.token.Number
    # Response status-line:

# Generated at 2022-06-13 21:54:35.481299
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    print(ColorFormatter.format_body('{"name":"value"}', "application/json"))  # noqa


if __name__ == "__main__":
    test_ColorFormatter_format_body()

# Generated at 2022-06-13 21:54:45.371354
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    """
    Test that format_headers() returns the expected output.
    """
    import os
    import pathlib
    import re
    import pypandoc

    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

    # load list of HTTP Headers from http.md
    markdown_file = pathlib.Path(base_path, "doc", "http.md")
    markdown_string = markdown_file.read_text()

    # extract list of HTTP Headers
    pattern = re.compile(r'^- (.+)$', re.MULTILINE)
    http_headers = pattern.findall(markdown_string)

    # generated html output
    html_string = pypandoc.convert_text

# Generated at 2022-06-13 21:54:55.102788
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    text = 'User-Agent: Mozilla/5.0\r\n'
    tokens = list(lexer.get_tokens(text))

    assert tokens[0] == (
        pygments.token.Name.Attribute,
        'User-Agent',
        1,
        0,
        'User-Agent',
    )
    assert tokens[1] == (
        pygments.token.Text,
        ' ',
        1,
        11,
        ' ',
    )
    assert tokens[2] == (
        pygments.token.Operator,
        ':',
        1,
        12,
        ':',
    )

# Generated at 2022-06-13 21:54:56.235030
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter


# Generated at 2022-06-13 21:55:00.350189
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    colorFormatter = ColorFormatter(Environment({'colors': True}))
    assert colorFormatter.format_headers('httpie') == '\x1b[30m\x1b[47m\x1b[49m\x1b[39m'

# Generated at 2022-06-13 21:55:04.283027
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    """Test ColorFormatter get_style_class function"""

    for style in AVAILABLE_STYLES:
        style_class = ColorFormatter.get_style_class(style)
        assert isinstance(style_class, type(pygments.style.Style))

# Generated at 2022-06-13 21:55:05.000448
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert True

# Generated at 2022-06-13 21:55:13.844311
# Unit test for function get_lexer
def test_get_lexer():
    http_lexer = SimplifiedHTTPLexer()
    lexer = get_lexer('text/html')
    assert lexer is not None
    assert lexer.name == 'HTML'
    assert pygments.highlight(code='<html><head><title>Hi</title></head></html>',
                              lexer=lexer, formatter=pygments.formatters.TerminalFormatter())
    lexer = get_lexer('text/html', body='An invalid html')
    assert lexer is not None
    assert lexer.name == 'Text only'
    assert pygments.highlight(code='An invalid html',
                              lexer=lexer, formatter=pygments.formatters.TerminalFormatter())
    lexer = get_lexer('application/json')
    assert lexer is not None
   

# Generated at 2022-06-13 21:55:23.113580
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env)
    input_ = "GET /search?q=httpie HTTP/1.1\r\nHost: google.com\r\n\r\n"
    output = formatter.format_headers(input_)
    assert output == "\x1b[38;5;245mGET /search?q=httpie HTTP/1.1\r\nHost:\x1b[39m \x1b[38;5;244mgoogle.com\r\n\r\n"

# Generated at 2022-06-13 21:55:26.849360
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():

    class FakeEnvironment(object):
        colors = True

    color_formatter = ColorFormatter(FakeEnvironment())
    lexer = color_formatter.get_lexer_for_body(mime="application/json", body="test")
    assert lexer == pygments.lexers.get_lexer_by_name('json')

# Generated at 2022-06-13 21:55:35.141599
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter = ColorFormatter(Environment(), False, 'solarized')
    assert formatter.formatter._style == Solarized256Style
    assert formatter.http_lexer == SimplifiedHTTPLexer

# Generated at 2022-06-13 21:55:44.411026
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    http_lexer = SimplifiedHTTPLexer()
    assert http_lexer.name == 'HTTP', "Expected http_lexer.name == 'HTTP'"
    assert http_lexer.aliases == ['http'], "Expected http_lexer.aliases == ['http']"
    assert http_lexer.filenames == ['*.http'], "Expected http_lexer.filenames == ['*.http']"
    assert http_lexer.tokens, "Expected http_lexer.tokens to be truthy"
    assert http_lexer.tokens['root'], "Expected http_lexer.tokens['root'] to be truthy"

# Generated at 2022-06-13 21:55:46.352729
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized256') is Solarized256Style

# Generated at 2022-06-13 21:55:58.701650
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    env = Environment.parse([])
    color_formatter = ColorFormatter(env, color_scheme='fruity')
    style_class = color_formatter.get_style_class(color_scheme='fruity')
    assert isinstance(style_class, pygments.style.Style)
    assert style_class.__name__ == 'FruityStyle'
    assert color_formatter.formatter.style.__name__ == 'FruityStyle'

    color_formatter = ColorFormatter(env, color_scheme=DEFAULT_STYLE)
    style_class = color_formatter.get_style_class(color_scheme=DEFAULT_STYLE)
    assert isinstance(style_class, pygments.style.Style)
    assert color_formatter.formatter.style.__name

# Generated at 2022-06-13 21:56:06.220464
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Arrange
    env = Environment()

    # Act
    colorFormatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    # Assert
    assert colorFormatter.explicit_json == False
    assert colorFormatter.formatter != None
    assert colorFormatter.http_lexer != None

if __name__ == "__main__":
    test_ColorFormatter()

# Generated at 2022-06-13 21:56:18.747826
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    env = Environment(colors=256)
    cf = ColorFormatter(env, explicit_json=False, color_scheme=AUTO_STYLE, **{})
    assert cf.format_body('{ "foo" : "bar" }', mime='application/json') == '{ "foo" : "bar" }'
    assert cf.format_body('Så skedde det något', mime='text/plain') == 'Så skedde det något'
    assert cf.format_body('<!DOCTYPE html>', mime='text/html') == '<!DOCTYPE html>'
    assert cf.format_body("""<?xml version="1.0"?>""", mime='application/xml') == """<?xml version="1.0"?>"""
    assert cf.format

# Generated at 2022-06-13 21:56:30.935519
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter(Environment())
    body = '{"name":"jack", "age":19}'
    lexer = formatter.get_lexer_for_body('application/json', body)
    assert lexer.name == 'JSON'

    color_body = formatter.format_body(body, 'application/json')
    color_lines = color_body.split('\n')
    assert len(color_lines) == 3
    assert '{' in color_lines[0]
    assert '"name":' in color_lines[1]
    assert '}' in color_lines[2]

    body = 'name=jack&age=19'
    lexer = formatter.get_lexer_for_body('application/x-www-form-urlencoded', body)
    color_body = formatter

# Generated at 2022-06-13 21:56:44.629587
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.core import main
    from httpie.core import request
    from httpie.core import response
    from httpie.core import parser
    from httpie.core import main
    from httpie.core import entrypoint
    from httpie.core import args
    from httpie.core import AuthCredentials
    from httpie.core import auth
    from httpie.core import helpers
    from httpie.core import plugins
    from httpie.core import __version__ as version
    from httpie.core import exit

    # Generate a test response object

# Generated at 2022-06-13 21:56:47.168123
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:56:52.350552
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter = ColorFormatter(Environment(colors=256, output_stream=None))
    assert isinstance(color_formatter.formatter, Terminal256Formatter)
    assert isinstance(color_formatter.http_lexer, SimplifiedHTTPLexer)

# Generated at 2022-06-13 21:57:10.935192
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # prepare
    from httpie.plugins.colors import ColorFormatter
    from httpie.plugins.json import JSONFormatter
    import pygments.lexers
    from httpie.context import Environment
    from httpie.plugins.builtin import HTTPHeadersProcessor
    import pygments.token
    lexer = None
    # execute
    env = Environment()
    headers = HTTPHeadersProcessor(env=env)
    formatter = ColorFormatter(
        env=env,
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )
    body1 = 'HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n'

# Generated at 2022-06-13 21:57:23.412070
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    def assert_lexer(mime, body, lexer_name):
        lexer = ColorFormatter(Environment()).get_lexer_for_body(mime, body)
        assert lexer is not None
        assert lexer.name == lexer_name

    assert_lexer('application/json', '{}', 'JSON')
    assert_lexer('application/foo+json', '{}', 'JSON')
    assert_lexer('application/foo+bar+json', '{}', 'JSON')
    assert_lexer('application/json+foo+bar', '{}', 'JSON')
    assert_lexer('application/json+foo', '{}', 'JSON')

    assert_lexer('application/x-json', '{}', 'JSON')

# Generated at 2022-06-13 21:57:28.038634
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color = ColorFormatter("")
    assert(color.formatter.__class__.__name__ == 'Terminal256Formatter')
    assert(color.http_lexer.__class__.__name__ == 'SimplifiedHTTPLexer')

# Generated at 2022-06-13 21:57:39.692879
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from tests.utils import http

    env = Environment()
    env.stdout = env.stderr = open('/dev/null', 'w')
    env.colors = 256
    color_formatter = ColorFormatter(env, color_scheme="monokai")
    r = http('GET', '--print=Hhb', 'https://httpbin.org/headers',
             env=env)
    assert BINARY_SUPPRESSED_NOTICE.decode() in r
    assert r.exit_status == http.ExitStatus.OK
    assert r.stderr == ''


# Generated at 2022-06-13 21:57:49.194748
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import datetime
    import json
    import platform
    import sys

# Generated at 2022-06-13 21:57:50.546478
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    pass



# Generated at 2022-06-13 21:57:53.829136
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert 'json' in get_lexer('application/json').aliases
    assert 'json' in get_lexer('text/plain').aliases

# Generated at 2022-06-13 21:58:05.288691
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class FakeEnvironment:
        def __init__(self, colors=None):
            self.colors = colors
    formatter = ColorFormatter(FakeEnvironment(), explicit_json=False, color_scheme=DEFAULT_STYLE, **{})
    mime = "application/json"
    body = '{"key":"value"}'
    assert isinstance(formatter.get_lexer_for_body(mime, body), pygments.lexers.JsonLexer)
    mime = "text/plain"
    body = "Hello World"
    assert isinstance(formatter.get_lexer_for_body(mime, body), pygments.lexers.TextLexer)

# Generated at 2022-06-13 21:58:08.093255
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('monokai')
    assert ColorFormatter.get_style_class('xxx') == Solarized256Style

# Generated at 2022-06-13 21:58:12.446180
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    print(ColorFormatter.format_headers('Content-Type: text/html; charset=utf-8'))


if __name__ == "__main__":
    test_ColorFormatter_format_headers()

# Generated at 2022-06-13 21:58:42.165675
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    """
    Checks that the right lexer is chosen depending on the two parameters.
    """
    color_formatter = ColorFormatter(None)

    mime1 = 'application/json'
    body1 = '{"a": 1}'
    assert(color_formatter.get_lexer_for_body(mime1, body1) == pygments.lexers.get_lexer_by_name('json'))

    mime2 = 'application/json;charset=utf-8'
    body2 = '{"a": 1}'
    assert(color_formatter.get_lexer_for_body(mime2, body2) == pygments.lexers.get_lexer_by_name('json'))

    mime3 = 'application/json'
    body3 = ''

# Generated at 2022-06-13 21:58:42.813411
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter

# Generated at 2022-06-13 21:58:50.408720
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import pygments
    from httpie.colors import ColorFormatter
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin

    env = Environment(colors=True)
    headers = """\
HTTP/1.1 200 OK
Date: Sun, 16 Jun 2019 20:27:22 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Wed, 15 May 2019 17:42:27 GMT
ETag: "28d-5891bcaa0a8ec"
Accept-Ranges: bytes
Content-Length: 3496
Content-Type: text/html
"""

    # Expected result
    lexer = pygments.lexers.get_lexer_by_name('http')

# Generated at 2022-06-13 21:58:54.722365
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert SimplifiedHTTPLexer.name == 'HTTP' and SimplifiedHTTPLexer.aliases == ['http'] and SimplifiedHTTPLexer.filenames == ['*.http']

# Generated at 2022-06-13 21:59:06.205773
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    pygments.token.Token.HTTP_HEADER = 101
    pygments.token.Token.HTTP_HEADER_KEY = 102
    pygments.token.Token.HTTP_HEADER_VALUE = 103
    lexer = SimplifiedHTTPLexer()
    out = lexer.get_tokens_unprocessed(
        "GET /sample_page.html HTTP/1.1\r\n"
        "Host: example.com\r\n"
        "Connection: close\r\n"
        "X-My-Header: MyValue\r\n"
        "\r\n"
    )
    out = list(out)
    assert out[2][1] == pygments.token.HTTP_HEADER_KEY
    assert out[3][1] == pygments.token.HTTP_HEADER_VALUE

# Generated at 2022-06-13 21:59:17.742151
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # Arrange
    cf = ColorFormatter(explicit_json=False)

    # Assert
    assert cf.get_lexer_for_body("text/html") == pygments.lexers.get_lexer_by_name("html")
    assert cf.get_lexer_for_body("text/javascript") == pygments.lexers.get_lexer_by_name("javascript")
    assert cf.get_lexer_for_body("text/plain") == pygments.lexers.get_lexer_by_name("text")
    assert cf.get_lexer_for_body("text/xml") == pygments.lexers.get_lexer_by_name("xml")
    assert cf.get_lexer_for_body("application/json") == pygments.lexers.get_lexer_by

# Generated at 2022-06-13 21:59:20.639471
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(Environment(), 'test')
    assert formatter.get_lexer_for_body('application/json', 'test') is not None

# Generated at 2022-06-13 21:59:26.223938
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    environment = Environment(colors=16)
    colorFormatter = ColorFormatter(
        env=environment,
        explicit_json=False,
        color_scheme='default'
    )
    assert colorFormatter.enabled == True
    assert colorFormatter.explicit_json == False
    assert type(colorFormatter.http_lexer) == SimplifiedHTTPLexer
    assert type(colorFormatter.formatter) == TerminalFormatter
    # TODO: Check more variables


# Generated at 2022-06-13 21:59:38.596517
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie import input

    class MockEnvironment:

        def __init__(self):
            self.colors = 1

        def stdout_isatty(self):
            return True

    c = ColorFormatter(MockEnvironment())
    s = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n'

# Generated at 2022-06-13 21:59:45.857212
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style
    assert ColorFormatter.get_style_class('solarized256') == Solarized256Style
    assert ColorFormatter.get_style_class('some-style') == Solarized256Style



# Generated at 2022-06-13 22:00:25.044347
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    SimplifiedHTTPLexer()

# Generated at 2022-06-13 22:00:35.636376
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    import os
    import pygments.lexers.text as mock
    from httpie.plugins.colors.utils import SimplifiedHTTPLexer
    from httpie.plugins.colors.utils import PygmentsHttpLexer
    lexer = SimplifiedHTTPLexer()
    lexer.name = 'HTTP'
    lexer.aliases = ['http']
    lexer.filenames = ['*.http']
    lexer.tokens = { 'root': [(r'(.*?)( *)(:)( *)(.+)',pygments.lexer.bygroups(pygments.token.Name.Attribute, pygments.token.Text, pygments.token.Operator, pygments.token.Text, pygments.token.String))]}

# Generated at 2022-06-13 22:00:48.788360
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.output.streams import STDOUT_BYTES_WRITER
    from httpie import ExitStatus
    from httpie.plugins import plugin_manager
    from httpie.context import Environment

    env = Environment(stdout=STDOUT_BYTES_WRITER)
    plugin_manager.load_internal_plugins()
    plugin_manager.load_plugins(env)
    plugin_manager.instantiate_plugins(env)

    color_formatter = ColorFormatter(env=env)

    assert color_formatter.format_headers(headers='') == ''

# Generated at 2022-06-13 22:00:49.565813
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    pass

# Generated at 2022-06-13 22:01:00.668851
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    json_key = 'application/json'
    xml_key = 'application/xml'
    form_urlencoded = 'application/x-www-form-urlencoded'
    json_body = '{"persons":[{"hoi":1,"lala":2}]}'
    xml_body = '<xml><persons><person><hoi>1</hoi><lala>2</lala></person></persons></xml>'
    form_urlencoded_body = 'persons%5B%5D%5Bhoi%5D=1&persons%5B%5D%5Blala%5D=2'

# Generated at 2022-06-13 22:01:12.221610
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.plugins import FormatterPlugin
    import httpie.plugins.builtin
    import tempfile
    import os.path
    import os

    testdir = tempfile.mkdtemp()

    # Create a temp file with some content
    content = "This is a test for the test case."
    file_name = "text.txt"
    try:
        f = open(os.path.join(testdir, file_name), "w+")
        f.write(content)
        f.close()
    except IOError:
        print("Error: Creating file with content failed.")

    # Create an environment