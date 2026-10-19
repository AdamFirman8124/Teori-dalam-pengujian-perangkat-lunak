

# Generated at 2022-06-13 21:51:36.279001
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.utils import MimeType
    from httpie.compat import is_windows

    env = Environment(colors=True)
    color_formatter = ColorFormatter(env)
    color_formatter.http_lexer = SimplifiedHTTPLexer()


# Generated at 2022-06-13 21:51:44.213789
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.plugins import FormatterPluginManager

    test_formatter = FormatterPluginManager.find_plugin_by_group_name(
        group_name='colors',
        prefix='formatter_'
    )(env=Environment(colors=True), color_scheme=DEFAULT_STYLE)

    mime = 'text/plain'
    body = 'Hello, World!'
    body_with_pygments = test_formatter.format_body(body, mime)
    assert body_with_pygments == body, (
        "When content type is 'text/plain' then do not apply syntax "
        "highlighting to the body."
    )

    mime = 'application/json'
    body = r'{"key": "value"}'
    body_with_pygments = test_formatter.format_

# Generated at 2022-06-13 21:51:53.434127
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # Use method get_lexer_for_body of class ColorFormatter to get lexer for body

    body = """
{
  "alphabet": {
    "a": "abcdefghijklmnopqrstuvwxyz",
    "b": {
      "c": "cba"
    }
  }
}"""

    assert ColorFormatter.get_lexer_for_body(
        'text/html', body) is None

    assert ColorFormatter.get_lexer_for_body(
        'application/json', body) == pygments.lexers.JsonLexer

    assert ColorFormatter.get_lexer_for_body(
        'application/javascript', body) == pygments.lexers.JavaScriptLexer

# Generated at 2022-06-13 21:51:59.933796
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from environment import MockEnvironment
    env = MockEnvironment(
        styles=True,
        colors=256
    )
    assert issubclass(ColorFormatter(env).get_style_class('solarized'),
                      Solarized256Style)
    assert issubclass(ColorFormatter(env).get_style_class('fruity'),
                      pygments.styles.get_style_by_name('fruity'))

# Generated at 2022-06-13 21:52:05.456907
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie import Environment
    from httpie.output.streams import get_binary_stream
    env = Environment()
    color_fmter = ColorFormatter(env=env, explicit_json=True, color_scheme='solarized')
    style_class = color_fmter.get_style_class('solarized')
    assert style_class == Solarized256Style

# Generated at 2022-06-13 21:52:13.378509
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('application/json', True, '{}')
    assert not get_lexer('text/html', False, '{}')
    assert get_lexer('application/javascript', False, '{}')
    assert get_lexer('text/plain', False, '{}')
    assert not get_lexer('text/html', True, '1')

# Generated at 2022-06-13 21:52:25.725741
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    class MockEnv:
        colors = True

    class MockColorFormatter(ColorFormatter):
        def __init__(self, env, **kwargs):
            pass

    cf = MockColorFormatter(MockEnv())
    example_header = b"HTTP/1.1 200 OK\r\nContent-Type: application/json; utf-8\r\n" \
                     b"Server: Windows Server 2008 R2 X64\r\nX-Powered-By: ASP.NET\r\n" \
                     b"Date: Thu, 22 Nov 2018 01:39:22 GMT\r\nContent-Length: 0\r\n"

# Generated at 2022-06-13 21:52:34.931164
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    cli_args = {
        'color': 'auto',
        'colors': 256,
        'colors256': True,
        'json': False,
        'style': 'default',
        'style_default': True,
        'style_override': True,
    }
    env = Environment()

    color_formatter_instance = ColorFormatter(cli_args, env)

    assert getattr(color_formatter_instance, 'group_name') == 'colors'
    assert getattr(color_formatter_instance, 'enabled') == True
    assert getattr(color_formatter_instance, 'explicit_json') == False
    assert isinstance(getattr(color_formatter_instance, 'formatter'), Terminal256Formatter)

# Generated at 2022-06-13 21:52:48.325829
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
   import sys
   import os
   import httpie
   from httpie.plugins import FormatterPlugin
   from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
   
   class RequestFormatter(FormatterPlugin):
     """Request formatter."""

     name = 'Request'
     order = -2

   class ResponceFormatter(FormatterPlugin):
     """Responce formatter."""

     name = 'Responce'
     order = -1

   class ColorFormatter(FormatterPlugin):
     """Color Formatter."""

     name = 'Color'
     order = 0

   class PrettyFormatter(FormatterPlugin):
     """Pretty JSON formatter."""

     name = 'Pretty'
     order = 1

   class RequestBodyFormatter(FormatterPlugin):
     """Request body formatter."""

    

# Generated at 2022-06-13 21:52:54.088774
# Unit test for function get_lexer
def test_get_lexer():
    # `get_lexer` should return a TextLexer instance when no other
    # lexer is available
    l = get_lexer('application/pdf')
    assert issubclass(l, pygments.lexers.TextLexer)

# Generated at 2022-06-13 21:53:18.251692
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    headers = """HTTP/1.1 200 OK
Content-Type: text/plain

"""
    body = "badger\n"
    mime = 'text/plain' 
    #passing ColorFormatter object as f to format_body() directly
    f = ColorFormatter()
    assert f.format_body(body, mime) == "\x1b[38;5;33mbadger\n\x1b[0m"

# Generated at 2022-06-13 21:53:29.766993
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    class DummyEnviron:
        json = False
        colors = True

    dummy_environ = DummyEnviron()

    color_formatter = ColorFormatter(env=dummy_environ)

    from requests import get
    from pprint import pprint

    # Present
    mime = 'text/html'
    r = get('https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol')
    pprint(r.headers)
    pprint(r.text)
    body = r.text
    print(color_formatter.format_body(body=body, mime=mime))

    # Missing
    mime = 'application/json'
    r = get('https://api.github.com/users/HTTPie/repos')
    pprint(r.json())

# Generated at 2022-06-13 21:53:36.233388
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    headers = (
        'GET / HTTP/1.1\n'
        'Accept: */*\n'
        'Accept-Encoding: gzip, deflate\n'
        'Connection: keep-alive\n'
        'Host: httpbin.org\n'
        'User-Agent: HTTPie/1.0.2\n'
        'X-Foo: Baz\n'
    )

# Generated at 2022-06-13 21:53:46.349693
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    assert ColorFormatter.get_lexer_for_body(";charset=utf-8", "notJSON") is None
    assert ColorFormatter.get_lexer_for_body("application/json", "notJSON") is None
    assert ColorFormatter.get_lexer_for_body("application/json", "JSON") is pygments.lexers.get_lexer_by_name("json")
    assert ColorFormatter.get_lexer_for_body("text/html", "notJSON") is pygments.lexers.get_lexer_by_name("html")

# Generated at 2022-06-13 21:53:56.320841
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    assert get_lexer(mime='text/plain').__name__ == 'TextLexer'
    assert get_lexer(mime='text/plain; charset=utf-8').__name__ == 'TextLexer'

    assert get_lexer(mime='application/json').__name__ == 'JsonLexer'
    assert get_lexer(mime='application/vnd.api+json').__name__ == 'JsonLexer'

    assert get_lexer(mime='application/javascript',
                     body=b'{"foo": "bar"}').__name__ == 'JsonLexer'
    assert get_lexer(mime='text/javascript', body=b'{"foo": "bar"}').__name__ == 'JsonLexer'

# Generated at 2022-06-13 21:54:00.065848
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(Environment(), False, 'solarized')
    assert formatter.get_lexer_for_body('application/json', '') is None
    assert formatter.get_lexer_for_body('application/json', '{') is None

# Generated at 2022-06-13 21:54:01.169651
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style

# Generated at 2022-06-13 21:54:02.216339
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    formatter = ColorFormatter()
    assert formatter is not None

# Generated at 2022-06-13 21:54:09.000214
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import os
    import sys
    import pytest
    from httpie import ExitStatus
    from utils import http, HTTP_OK


    env = Environment()
    env.config['style'] = 'default'
    env.config['colors'] = 256

    r = http('GET', HTTP_OK)
    assert r.exit_status == ExitStatus.OK
    assert r.json == {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'HTTPie/1.0.3'}, 'origin': '183.196.58.217', 'url': 'http://httpbin.org/get'}
    r = http('-v', 'GET', HTTP_OK)

# Generated at 2022-06-13 21:54:19.732710
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(None)
    lexer = formatter.get_lexer_for_body('application/json', '{}')
    assert lexer.name == 'JSON'
    lexer = formatter.get_lexer_for_body('application/vnd.api+json', '{}')
    assert lexer.name == 'JSON'
    lexer = formatter.get_lexer_for_body('application/ld+json', '{}')
    assert lexer.name == 'JSON'
    lexer = formatter.get_lexer_for_body('application/foo+json', '{}')
    assert lexer.name == 'JSON'
    lexer = formatter.get_lexer_for_body('application/json', '{}')
    assert lexer.name == 'JSON'

# Generated at 2022-06-13 21:54:33.422264
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie import ExitStatus
    from tests.utils import HTTP_OK, MockEnvironment
    env = MockEnvironment(colors=256, stdin_isatty=True, stdout_isatty=True)
    r = ColorFormatter(env, color_scheme='solarized').format_headers(HTTP_OK)
    assert ExitStatus.OK == 0
    assert r.startswith('\x1b[38;5;131mHTTP')
    assert r.endswith('\x1b[m\r\n\r\n')


# Generated at 2022-06-13 21:54:36.016201
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    try:
        c = ColorFormatter(None) 
    except Exception:
        assert False
    else:
        assert True

# Generated at 2022-06-13 21:54:45.730571
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.analyse_text("GET")
    assert lexer.analyse_text("POST")
    assert lexer.analyse_text("DELETE")
    assert lexer.analyse_text("PUT")
    assert not lexer.analyse_text("Invalid")
    assert not lexer.analyse_text("Invalid/")
    assert not lexer.analyse_text("GET Invalid/")
    assert lexer.analyse_text("GET /")
    assert lexer.analyse_text("GET /some/path")
    assert lexer.analyse_text("GET /some/path HTTP/1.1")
    assert lexer.analyse_text("HTTP/1.1")
    assert lexer.analyse_text("HTTP/1.1 200")

# Generated at 2022-06-13 21:54:49.762100
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_scheme = 'solarized'
    http_lexer = SimplifiedHTTPLexer()
    formatter = Terminal256Formatter(
        style=Solarized256Style)
    assert ColorFormatter(
        None,
        explicit_json=None,
        color_scheme=color_scheme,
        **{}
    ).formatter == formatter

# Generated at 2022-06-13 21:55:03.336351
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    from pygments.formatters.terminal import TerminalFormatter
    from pygments.token import Keyword, Text, Name, Number, Name, Operator
    color_formatter = ColorFormatter(None, None)
    headers = '''\
POST / HTTP/1.1
Host: localhost:8080
User-Agent: HTTPie/0.7.0
Accept-Encoding: gzip, deflate
Accept: */*
Content-Length: 11
Content-Type: application/x-www-form-urlencoded
'''
    body = 'a=1&b=2'
    response_headers = color_formatter.format_headers(headers)
    response_body = color_formatter.format_body(body, 'application/x-www-form-urlencoded')

    print(response_headers)

# Generated at 2022-06-13 21:55:12.970914
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.context import Environment
    class DummyResponse(object):
        def __init__(self, headers, content_type):
            self.headers = headers
            self.content_type = content_type
    def _create_env(colors=True):
        return Environment(colors=colors)
    # Inputs to the method and expected output string
    headers = '''\
HTTP/1.1 200 OK
Date: Sun, 09 Jul 2017 17:28:09 GMT
Server: Apache/2.4.10 (Debian)
Last-Modified: Mon, 24 Mar 2014 18:54:28 GMT
ETag: "17c7-4f6dcf4507ee4"
Accept-Ranges: bytes
Content-Length: 5991
Vary: Accept-Encoding
Content-Type: text/html
'''

# Generated at 2022-06-13 21:55:25.570691
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=256, stdout_isatty=True)
    color_formatter = ColorFormatter(env)

    headers = color_formatter.format_headers(
        'GET /foo HTTP/1.1\n'
        'Host: example.org\n'
        'User-Agent: httpie/0.9.8\n'
        'Accept-Encoding: gzip, deflate\n'
        'Accept: application/json\n'
        'Connection: keep-alive\n\n'
    )

# Generated at 2022-06-13 21:55:39.383954
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    color_formatter = ColorFormatter(
        Environment(),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )
    headers = color_formatter.format_headers("HTTP/1.1 200 OK\n"
                                    "Server: nginx\n"
                                    "Date: Sun, 06 Oct 2019 06:10:01 GMT\n"
                                    "Content-Type: text/html;charset=utf-8\n"
                                    "Content-Length: 0\n"
                                    "Connection: keep-alive\n"
                                    "Set-Cookie:JSESSIONID=C7483B79F1B4A4E4126E9C40F9C11396")

# Generated at 2022-06-13 21:55:45.376254
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    color_formatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert color_formatter.http_lexer is not None
    assert color_formatter.formatter is not None
    assert color_formatter.explicit_json is False
    assert color_formatter.enabled is True


# Generated at 2022-06-13 21:55:52.350172
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter(None)
    mime = 'application/json'
    body = '{"foo":"bar"}'
    lexer = formatter.get_lexer_for_body(mime, body)
    assert lexer.__name__ == 'JSON'


if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-13 21:56:11.365350
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.plugins import PluginManager
    from httpie import output

    class MockEnvironment:
        colors = 256
        stdin_isatty = False
        stdout_isatty = False
        is_windows = False
        is_mac = False
        colors_force = False
        plugins = PluginManager()

    env = MockEnvironment()

    formatter = output.ColorFormatter(env)

    # When the server specifies an Accept header that contains the "*"
    # wildcard, it indicates that it will accept any MIME type. Therefore
    # the formatter will not highlight the text of the response.
    #
    # See: https://stackoverflow.com/a/11877316

# Generated at 2022-06-13 21:56:22.112247
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class MockedColorFormatter(ColorFormatter):
        def get_lexer_for_body(
            self, mime: str,
            body: str
        ) -> Optional[Type[Lexer]]:
            return pygments.lexers.get_lexer_by_name('json')
    from io import StringIO
    body = '{"a":1,"b":2}'
    out = StringIO()
    f = MockedColorFormatter(env={}, out=out)
    f.format_body(body, 'text/plain')

# Generated at 2022-06-13 21:56:32.017845
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.plugins.builtin import JSONTransform

    def _assert_lexer_matches_mime(
        mime_type,
        body='',
        body_lexer=None,
        explicit_json=False,
    ):
        c = ColorFormatter(
            env=Environment(),
            explicit_json=explicit_json,
            color_scheme=DEFAULT_STYLE,
        )
        actual_lexer = c.get_lexer_for_body(mime_type, body)
        assert actual_lexer == body_lexer, \
            '%s: %s != %s' % (mime_type, actual_lexer, body_lexer)

    def _assert_lexer_matches_json(body, lexer):
        return _assert_lexer_matches

# Generated at 2022-06-13 21:56:42.761120
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment
    colorFormatter = ColorFormatter(Environment(color=True, stdout_isatty=True))
    body = '{"key": 3}\n\n'
    mime_type = 'application/json'
    output = colorFormatter.format_body(body, mime_type)

# Generated at 2022-06-13 21:56:53.316654
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()

    assert lexer.analyse_text('') == 0
    assert lexer.analyse_text('Foo: Bar') == 1
    assert lexer.analyse_text('GET /index.html HTTP/1.1') == 1
    assert lexer.analyse_text('HTTP/1.1 404 Not Found') == 1

    formatter = Terminal256Formatter(style=Solarized256Style)
    result = pygments.highlight(code='Foo: Bar', lexer=lexer, formatter=formatter)

# Generated at 2022-06-13 21:57:02.898724
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.cli import Environment
    env = Environment()
    env.colors = True
    color_formatter = ColorFormatter(env, color_scheme='solarized')
    print(color_formatter.get_lexer_for_body('image/jpeg', "JFIF"))
    print(color_formatter.get_lexer_for_body('text/html', "<html></html>"))
    print(color_formatter.get_lexer_for_body('application/json', '{"a":"b"}'))
    print(color_formatter.get_lexer_for_body('text/plain', 'just a text'))
    # print(color_formatter.get_lexer_for_body('text/plain', '{"a":"b"}'))

# Generated at 2022-06-13 21:57:06.903994
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('monokai') is pygments.styles.get_style_by_name('monokai')
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style
    assert ColorFormatter.get_style_class('auto') is Solarized256Style

# Generated at 2022-06-13 21:57:13.965202
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from io import StringIO
    environment = Environment()

    # Test if a plain text is unchanged
    color_formatter = ColorFormatter(env=environment)
    input_text = 'Plain text.'
    output_text = color_formatter.format_body(input_text, mime='text/plain')
    assert input_text == output_text
    # Test if a plain text is unchanged even if an extension of the file is
    # parsed by pygments
    input_text = 'Plain text.\n'
    output_text = color_formatter.format_body(input_text, mime='text/plain')
    assert input_text == output_text

    # Test if a json string is unchanged
    input_text = '{"json":"json"}'

# Generated at 2022-06-13 21:57:25.899048
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=True)
    formatter = ColorFormatter(env)
    headers = """GET / HTTP/1.1
Host: httpbin.org
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: HTTPie/0.9.9
"""

# Generated at 2022-06-13 21:57:34.649241
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    import httpie.plugins

    class ColorFormatterTest(ColorFormatter):
        def __init__(self, enable_colors=True):
            kwargs = dict()
            super().__init__(
                env=Environment(color=enable_colors),
                **kwargs
            )

        def format_body(self, body: str, mime: str) -> str:
            return body

        def get_lexer_for_body(
            self, mime: str,
            body: str
        ) -> Optional[Type[Lexer]]:
            return None

    httpie.plugins.formatter.FormatterPlugin.key_value_formatter = lambda x, y, z: str(x) + ': ' + str(y)

    # Testing a standard header line

# Generated at 2022-06-13 21:57:49.671595
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.core import get_response
    from httpie.output.streams import BUFSIZE
    from httpie.plugins import plugin_manager
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from httpie.output.streams import is_bytes
    from httpie.plugins import FormatterPlugin
    import httpie.plugins.builtin
    import pygments.lexer
    import pygments.lexers
    import pygments.style
    import pygments.styles
    import pygments.token
    from pygments.formatters.terminal import TerminalFormatter
    from pygments.formatters.terminal256 import Terminal256Formatter
    from pygments.lexer import Lexer
    from pygments.util import ClassNotFound

    import requests

#     body = requests.get('http://localhost

# Generated at 2022-06-13 21:57:51.329769
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    SimplifiedHTTPLexer



# Generated at 2022-06-13 21:57:53.760585
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    h_lexer = SimplifiedHTTPLexer()
    assert(h_lexer.name == 'HTTP')

# Generated at 2022-06-13 21:58:06.474076
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # https://jsonplaceholder.typicode.com/posts/1
    response_body = """
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
"""

# Generated at 2022-06-13 21:58:11.537547
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class Temp(object):
        def __init__(self):
            self.color_scheme = 'solarized'
    args = Temp()
    result = ColorFormatter.get_style_class(args.color_scheme)
    assert result is Solarized256Style

# Generated at 2022-06-13 21:58:22.896278
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.compat import is_windows
    from .config import Config
    from .output.streams import DEFAULT_STREAM
    from .style import build_style_processor

    style_plugin = build_style_processor(
        color_scheme=DEFAULT_STYLE,
        explicit_json=False,
        env=Environment(colors=256),
        stream=DEFAULT_STREAM,
        config=Config(colors=256),
    )
    assert isinstance(style_plugin, ColorFormatter)
    assert style_plugin.enabled

    def test(mime, body, expected):
        lexer = style_plugin.get_lexer_for_body(mime, body)
        result = style_plugin.format_body(body, mime)
        assert result == expected

# Generated at 2022-06-13 21:58:30.152349
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    env = {'colors': True}
    formatter = ColorFormatter(env)
    mime = 'text/plain'
    assert isinstance(formatter.get_lexer_for_body(mime, ''), pygments.lexers.TextLexer)
    mime = 'application/json'
    assert isinstance(formatter.get_lexer_for_body(mime, ''), pygments.lexers.JsonLexer)

# Generated at 2022-06-13 21:58:34.526390
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from pygments.styles import get_style_by_name
    style1 = ColorFormatter.get_style_class('solarized')
    style2 = get_style_by_name('solarized')
    assert style1 == style2

# Generated at 2022-06-13 21:58:44.478336
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie import environment

    class IO(object):
        def __init__(self):
            self.output_data = []

        def write(self, data):
            self.output_data.append(data)

    class Input(object):
        def __init__(self, input_data):
            self.input_queue = input_data

        def readline(self, limit=-1):
            return self.input_queue.pop(0)

    class Output(object):
        def __init__(self):
            self.output_data = []

        def write(self, data):
            self.output_data.append(data)

    class Environment(object):
        colors = True
        colors256 = True
        is_terminal = True
        stdout = IO()
        stdin = Input([])
        stdin

# Generated at 2022-06-13 21:58:52.611987
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    assert get_lexer(mime = 'text/html')
    assert get_lexer(mime = 'application/xml')
    assert get_lexer(mime = 'application/javascript')
    assert get_lexer(mime = 'application/octet-stream', body='')
    assert get_lexer(mime = 'application/octet-stream', body='hello')
    assert not get_lexer(mime = 'application/octet-stream', body='<html></html>')
    assert get_lexer(mime = 'application/octet-stream', body='<html></html>', explicit_json=True)

# Generated at 2022-06-13 21:59:16.630805
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    assert ColorFormatter.format_headers("") == ""
    assert ColorFormatter.format_headers("some string") == "some string"
    assert ColorFormatter.format_headers("string\n") == "string\n"
    assert ColorFormatter.format_headers("some string\n") == "some string\n"
    assert ColorFormatter.format_headers("some string\nanother string") == "some string\nanother string"
    assert ColorFormatter.format_headers("HTTP/1.1 some string\nanother string") == "HTTP/1.1 some string\nanother string"
    assert ColorFormatter.format_headers("HTTP/1.1 200 some string\nanother string") == "HTTP/1.1 200 some string\nanother string"

# Generated at 2022-06-13 21:59:17.444689
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert (0)

# Generated at 2022-06-13 21:59:19.378846
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    style_class = Solarized256Style
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) is style_class

# Generated at 2022-06-13 21:59:27.905556
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter(Environment(colors=256))
    formatter.http_lexer = SimplifiedHTTPLexer()
    formatter.formatter = Terminal256Formatter(style=Solarized256Style)

    #without body
    body = "\n\n"
    mime = "text/html"
    expected = "\n\n"

    assert formatter.format_body(body, mime) == expected

    #with body
    mime = "text/html"
    body = "<html></html>"
    expected = "\x1b[38;5;37m<html></html>\x1b[39m\x1b[49m\n"
    assert formatter.format_body(body, mime) == expected

    #simulate request json
    mime = "text/html"


# Generated at 2022-06-13 21:59:40.582365
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class MyFormatter(ColorFormatter):
        def __init__(self, *args, **kwargs):
            try:
                self.enabled = True
            except EnvironmentError:
                self.enabled = False
            self.env = None

    # Default
    formatter = MyFormatter(None, None)
    assert formatter.get_style_class('fruity') is pygments.styles.get_style_by_name('fruity')
    assert formatter.get_style_class('auto') is Solarized256Style
    assert formatter.get_style_class('solarized256') is Solarized256Style

    # No color support
    formatter = MyFormatter(None, None)
    formatter.enabled = False
    assert formatter.get_style_class('fruity') is pygments.styles.get

# Generated at 2022-06-13 21:59:42.208158
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    c=ColorFormatter({})
    print(c)

# Generated at 2022-06-13 21:59:57.524127
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.core import Program
    from httpie.context import Environment
    from httpie.output.streams import STDOUT_STREAM
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.cli.parser import parse_args
    from httpie.plugins.builtin import HTTPHeaders
    env = Environment(stdin=None, stdout=STDOUT_STREAM,
                      stderr=STDOUT_STREAM, vars={}, compare_key_values_order=KeyValueArgType.CASE_INSENSITIVE)
    http = Program(env=env,
                   config=parse_args([]),
                   processors=[],
                   plugins=[ColorFormatter(env), HTTPHeaders()])
    assert http is not None

# Generated at 2022-06-13 22:00:01.626228
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():

    c = ColorFormatter(None)
    # print c
    body = '{"a":"b"}'

    print(c.format_body(body, 'application/json'))

# Generated at 2022-06-13 22:00:09.753508
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import os, sys

    # Normally httpie imports itself in its environment.py, but here we need to import the whole functionality
    sys.path.append(os.path.abspath('./httpie'))
    sys.path.append(os.path.abspath('./httpie/plugins'))
    sys.path.append(os.path.abspath('./httpie/runners'))

    from httpie.compat import is_windows
    from httpie.plugins import FormatterPlugin
    from httpie.context import Environment
    from httpie.plugins.color import ColorFormatter

    body = '''
    {
        "key": "value",
        "key2" : [1,2,3]
    }
    '''

    # On Windows, force auto style to fruity

# Generated at 2022-06-13 22:00:17.525581
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class DummyEnv:
        def __init__(self):
            self.colors = 256

    class DummyStyle:
        pass

    class DummyClass:
        def __init__(self, env, color_scheme=None):
            self.env = env
            self.color_scheme = color_scheme
            self.get_style_class = ColorFormatter.get_style_class

    dummy_class = DummyClass(DummyEnv())

    assert dummy_class.get_style_class(AUTO_STYLE) == Solarized256Style
    assert dummy_class.get_style_class(SOLARIZED_STYLE) == Solarized256Style
    assert dummy_class.get_style_class('dummy') == DummyStyle

# Generated at 2022-06-13 22:00:52.451461
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.compat import urlopen
    from httpie.plugins import builtin
    from httpie.context import Environment
    from httpie.utils import get_binary_stream

    import json
    import os
    import sys
    import tempfile

    if is_windows:
        # Skip this test on Windows
        return

    class Environment:
        def __init__(self):
            self.colors = 256

    env = Environment()
    color_formatter = builtin.ColorFormatter(env)

    # Try an XML body with Content-Type: text/xml
    textXMLFile = os.path.join(os.path.dirname(__file__), "../../fixtures/textXML.xml")
    with open(textXMLFile) as f:
        xml = f.read()

# Generated at 2022-06-13 22:01:06.116473
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    x = ColorFormatter(
        env = Environment(
            colors = 256,
            style = "fruity",
        ),
        explicit_json = False,
        color_scheme = "solarized",
    )
    assert x.group_name == 'colors'
    assert x.enabled
    assert x.explicit_json == False
    assert x.formatter.__class__.__name__ == 'Terminal256Formatter'
    assert x.http_lexer.__class__.__name__ == 'SimplifiedHTTPLexer'
    assert x.get_lexer_for_body("application/json", "json").__class__.__name__ == 'JsonLexer'

# Generated at 2022-06-13 22:01:13.728604
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('monokai') == pygments.styles.get_style_by_name('monokai')
    assert ColorFormatter.get_style_class('mOnOkAi') == pygments.styles.get_style_by_name('mOnOkAi')
    assert ColorFormatter.get_style_class(AUTO_STYLE) == pygments.styles.get_style_by_name(AUTO_STYLE)
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) == Solarized256Style