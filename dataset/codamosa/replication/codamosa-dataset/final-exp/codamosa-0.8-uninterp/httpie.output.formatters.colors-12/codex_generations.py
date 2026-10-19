

# Generated at 2022-06-13 21:51:34.626974
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from httpie.formatters import ColorFormatter

    # Test for incorrect style name
    style = ColorFormatter.get_style_class("incorrect")
    assert style == Solarized256Style

    # Test for pygments default style
    style = ColorFormatter.get_style_class("default")
    assert style == pygments.styles.get_style_by_name("default")

    # Test for style name solarized256
    style = ColorFormatter.get_style_class("solarized256")
    assert style == Solarized256Style

# Generated at 2022-06-13 21:51:40.234639
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    e = Environment(colors=256)
    with pytest.raises(TypeError):
        ColorFormatter(e, color_scheme='wrong')
    with pytest.raises(TypeError):
        ColorFormatter(e)
    ColorFormatter(e, color_scheme=SOLARIZED_STYLE)
    ColorFormatter(e, color_scheme=AUTO_STYLE)

# Generated at 2022-06-13 21:51:42.850579
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert SimplifiedHTTPLexer().get_tokens('GET / HTTP/1.1\nHost: example.com\n') == []

# Generated at 2022-06-13 21:51:49.152952
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # type: () -> None
    class Env:
        colors = 256
        _colors = 256
    formatter = ColorFormatter(Env())
    assert formatter.formatter.__class__.__name__ == "Terminal256Formatter"
    assert formatter.http_lexer.__class__.__name__ == "SimplifiedHTTPLexer"
    assert pygments.styles.get_style_by_name(SOLARIZED_STYLE).__name__ == "Solarized256Style"

# Generated at 2022-06-13 21:51:51.124678
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == "HTTP"
    assert lexer.aliases == ['http']

# Generated at 2022-06-13 21:52:00.074427
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    for line in (
        b'GET /index.html HTTP/1.0',
        b'POST / HTTP/1.1',
        b'Connection: keep-alive',
        b'Content-Length: 1234',
        b'Content-Type: application/x-www-form-urlencoded',
        b'',
        b'HTTP/1.1 200 OK',
        b'Connection: keep-alive',
        b'Content-Length: 1234',
        b'Content-Type: application/x-www-form-urlencoded'
    ):
        assert list(SimplifiedHTTPLexer().get_tokens(line))

# Generated at 2022-06-13 21:52:09.130094
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class ColorFormatterTest(ColorFormatter):
        def get_lexer_for_body(
            self, mime: str,
            body: str
        ) -> Optional[Type[Lexer]]:
            return self.parent.get_lexer_for_body(mime, body)

    ColorFormatterTest.parent = ColorFormatter
    ColorFormatterTest.explicit_json = False
    ColorFormatterTest.formatter = Terminal256Formatter(
        style=Solarized256Style
    )
    ColorFormatterTest.http_lexer = SimplifiedHTTPLexer()
    ColorFormatterTest.enabled = True

    formatter = ColorFormatterTest(Environment(colors=256))
    body = '''{"name": "value"}'''

# Generated at 2022-06-13 21:52:13.570732
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    ColorFormatter(
        color_scheme='solarized',
        env=Environment(colors=256, print_body=False),
        explicit_json=False,
        stdout=None,
    )

# Generated at 2022-06-13 21:52:15.005172
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    print('success')


# Generated at 2022-06-13 21:52:26.358970
# Unit test for function get_lexer

# Generated at 2022-06-13 21:52:34.886914
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    _ = SimplifiedHTTPLexer
    assert True

# Generated at 2022-06-13 21:52:48.269240
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():

    class MockEnvironment:
        def __init__(self):
            self.colors = 256

    class MockColorFormatter(ColorFormatter):
        def __init__(self):
            super(MockColorFormatter, self).__init__(MockEnvironment())

        def format_body(self, body, mime):
            pass

    formatter = MockColorFormatter()
    headers_text = "HTTP/1.1 200 OK\r\nAccept: application/json\r\n" \
                   "Content-Type: text/plain"

# Generated at 2022-06-13 21:53:01.121575
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # Setup
    formatter = ColorFormatter(Environment())

    # Test cases

# Generated at 2022-06-13 21:53:07.508678
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from unittest import mock
    import pygments.styles
    mocked_class = mock.MagicMock(return_value='test_class')
    with mock.patch.object(pygments.styles, 'get_style_by_name', mocked_class):
        assert ColorFormatter.get_style_class('test') == 'test_class'
        assert mocked_class.call_count == 1

# Generated at 2022-06-13 21:53:18.798411
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import os
    import httpie
    import config
    import http_session

    env = httpie.Environment(config_dir=os.path.expanduser("~/.httpie"), colors=True)
    # Instantiate an http session
    session = http_session.HTTPSession(env)

    explicit_json = True

    # No path for GET or DELETE / admin
    url = "http://127.0.0.1:8080/restconf/operational/ietf-interfaces:interfaces"
    room = "admin"
    # GET
    args = httpie.core.parse_args([], env)
    args.url = url
    args.method = "GET"
    args.json = explicit_json

    # Instantiate the HTTPie formatter with our attributes

# Generated at 2022-06-13 21:53:32.618478
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()

# Generated at 2022-06-13 21:53:47.494951
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    color_formatter = ColorFormatter(None)
    color_formatter.get_lexer_for_body("", "")
    color_formatter.format_body("", "")

    # test unicode
    test_data = u'\u3042'
    assert color_formatter.format_body(test_data, "text/plain") == test_data

    # test lexer
    code = "#!/bin/bash\necho hoge"
    assert color_formatter.format_body(code, "text/plain") != code

    if not hasattr(StringIO, "getvalue"):
        # python 2.x
        class StringIO(StringIO):
            def getvalue(self):
                return self

# Generated at 2022-06-13 21:53:52.415971
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.context import Environment
    from httpie.config import Config
    from httpie.plugins import FormatterPlugin
    env = Environment()
    config = Config(colors=True)
    formatter = ColorFormatter(env = env, config = config)
    assert isinstance(formatter,FormatterPlugin)

# Generated at 2022-06-13 21:53:55.825787
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert SimplifiedHTTPLexer.__name__ == 'SimplifiedHTTPLexer'
    assert SimplifiedHTTPLexer.aliases == ['http']
    assert SimplifiedHTTPLexer.filenames == ['*.http']
    assert SimplifiedHTTPLexer.name == 'HTTP'



# Generated at 2022-06-13 21:53:59.012605
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    """Test for the constructor of SimplifiedHTTPLexer."""
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP', "The lexer name should be 'HTTP'"

# Generated at 2022-06-13 21:54:05.644359
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    color_formatter_object = ColorFormatter(environment, False, 'solarized')
    assert isinstance(color_formatter_object, ColorFormatter)

# Generated at 2022-06-13 21:54:18.154337
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # Style is default for incorrect or empty style
    assert ColorFormatter.get_style_class('') == pygments.styles.get_style_by_name(DEFAULT_STYLE)
    assert ColorFormatter.get_style_class('non-existing') == pygments.styles.get_style_by_name(DEFAULT_STYLE)

    if is_windows and DEFAULT_STYLE == 'fruity':
        # Windows gets fruity style as default
        assert ColorFormatter.get_style_class('auto') == pygments.styles.get_style_by_name('fruity')
    else:
        # Linux, MacOs and Cygwin get common style as default
        assert ColorFormatter.get_style_class('auto') == pygments.styles.get_style_by_name('common')

   

# Generated at 2022-06-13 21:54:31.469893
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    import json
    import requests
    import requests.packages.urllib3 as urllib3
    #from httpie.compat import getfqdn
    #from httpie.core import Environment, main_http
    #from httpie.output.streams import b64_encode
    #from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE

    from httpie.plugins import FormatterPlugin
    from httpie.plugins import PluginContainer
    from httpie.plugins import plugin_manager

    from httpie.compat import is_windows
    from httpie import ExitStatus
    from httpie.context import Environment
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE, write
    import os

# Generated at 2022-06-13 21:54:39.236240
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    http_lexer = SimplifiedHTTPLexer()
    formatter = TerminalFormatter()
    # HTTP request
    code = "GET / HTTP/1.1\n" \
           "Host: httpbin.org\n" \
           "Accept-Encoding: gzip, deflate\n" \
           "Connection: keep-alive\n" \
           "User-Agent: HTTPie/0.9.2\n" \
           "\n"
    assert pygments.highlight(code, http_lexer, formatter).strip() == code

# Generated at 2022-06-13 21:54:44.066956
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    color_formatter = ColorFormatter(Environment())
    body = "This is a sample body"
    mime = 'text/plain'
    lexer = color_formatter.get_lexer_for_body(mime, body)
    assert lexer == pygments.lexers.get_lexer_by_name('text')

# Generated at 2022-06-13 21:54:47.217817
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style
    assert ColorFormatter.get_style_class('solarized256') == Solarized256Style

# Generated at 2022-06-13 21:55:02.422075
# Unit test for method format_headers of class ColorFormatter

# Generated at 2022-06-13 21:55:09.090009
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style
    assert ColorFormatter.get_style_class('solarized256') == Solarized256Style
    assert ColorFormatter.get_style_class('solarized16') == \
        pygments.styles.get_style_by_name('solarized')
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:55:22.900518
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.output.streams import STDOUT_ENCODING
    from httpie.output.base import OutputOptions
    from httpie.output.formatters.colors import ColorFormatter
    from httpie.context import Environment
    env = Environment(colors=256)
    env.stdout_isatty = True
    env.stdout_encoding = STDOUT_ENCODING
    output_options = OutputOptions(
        verbose=True,
        json=False,
        styles=False,
        stream=None,
        color=True,
        print_body_only_if_stdin=False,
        output_options=()
    )

# Generated at 2022-06-13 21:55:36.487534
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from tests import http
    import json

# Generated at 2022-06-13 21:55:53.098047
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # FIXME:
    pass

# Generated at 2022-06-13 21:56:01.394081
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class DummyEnv(object):
        def __init__(self):
            self.colors = True

    class DummyConfig(object):
        def __init__(self):
            self.style = 'solarized'

    env = DummyEnv()
    config = DummyConfig()
    color_formatter = ColorFormatter(env=env, config=config)

    assert color_formatter.format_body(body='[{"a":"b"}]', mime='text/plain') == '[{\n  "a": "b"\n}]'
    assert color_formatter.format_body(body='[{"a":"b"}]', mime='application/json') == '[{\n  "a": "b"\n}]'

# Generated at 2022-06-13 21:56:17.005352
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.cli import styled_path
    from httpie import ExitStatus
    from collections import namedtuple
    from httpie.plugins import FormatterPlugin
    from httpie.main import main

    Status = namedtuple(
        'Status',
        ['ok', 'exit_status', 'http_status', 'reason']
    )

    headers = """HTTP/1.1 200 OK
Content-Length: 279196
Connection: keep-alive
Content-Encoding: gzip
Content-Type: application/json; charset=utf-8
Date: Fri, 01 Dec 2017 00:00:44 GMT
Server: nginx
Vary: Accept-Encoding
X-Powered-By: Express\n"""

    def run(*args, **kwargs):
        main(args, **kwargs)

    # terminal colors on

# Generated at 2022-06-13 21:56:18.048686
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    ColorFormatter(Environment(colors=256))

# Generated at 2022-06-13 21:56:30.558330
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import requests
    import base64
    s = requests.Session()
    # python=2
    username = '666888'
    passwd = '654321'
    # python=3
    # username = b'666888'
    # passwd = b'654321'
    s.auth = (username, passwd)
    print(s.auth)
    s.headers.update({
        'content-type': 'application/json'
    })

    r = s.get(
        'http://httpbin.org/get'
    )
    print(r.content)

    r = s.post(
        'http://httpbin.org/post',
        json={
            'name': 'test',
            'age': 16
        }
    )
    print(r.content)

    r

# Generated at 2022-06-13 21:56:44.487174
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    """Check if the SimplifiedHTTPLexer works as expected, we are expecting a working
    SimplifiedHTTPLexer for the test"""
    formatter = Terminal256Formatter(style=Solarized256Style)

    # Check if the request works
    test_request = '''GET / HTTP/1.1
Host: localhost
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive'''

# Generated at 2022-06-13 21:56:58.328343
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # import requests
    import urllib3
    #from httpie.plugins import FormatterPlugin
    #from httpie.compat import is_windows
    from httpie.context import Environment
    env = Environment(colors=True, stdout_isatty=True)
    explicit_json = False
    color_scheme = DEFAULT_STYLE

    formatter = ColorFormatter(env,
                               explicit_json,
                               color_scheme)

    r = urllib3.PoolManager().request('GET', 'https://baidu.com/',retries=False)
    #r = requests.get('https://baidu.com/')
    #print(r.text)
    print(formatter.format_headers(r.headers))


if __name__ == '__main__':
    test

# Generated at 2022-06-13 21:57:08.011984
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.plugins.builtin import HTTPHeadersProcessor

    # Test parameters
    env = Environment(
        auto_help=False,
        auto_version=False,
        auto_env=False,
        auto_color=False,
        output_options=None,
        colors=True,
        min_options=False,
        default_options=None,
        config_dir=None,
        config_path=None,
        plugins=None,
        proxy=None,
        traceback=False,
        debug=False,
        silent=False,
        verbose=False,
        quiet=False,
    )

    color_formatter = ColorFormatter(env)

    # Test 1 - Process headers

# Generated at 2022-06-13 21:57:14.653044
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.formatter import get_preferred
    from httpie.context import Environment

    env = Environment()
    env.stdout_isatty = True
    env.colors = 256

    formatter = get_preferred(env=env, color_scheme=AUTO_STYLE)

    body_text_plain = formatter.format_body('something', 'application/json')
    assert body_text_plain == 'something'

    body_json = formatter.format_body(
        '{"foo": "bar", "array": [1,2,3,4]}',
        'application/json'
    )

# Generated at 2022-06-13 21:57:19.419016
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    """ColorFormatter.format_headers()
    """
    env = Environment(colors=256)
    #method = ColorFormatter(env, color_scheme=SOLARIZED_STYLE).format_headers
    method = ColorFormatter(env, color_scheme=SOLARIZED_STYLE).format_headers
    output = method(
        'GET / HTTP/1.1\n'
        'Host: localhost:5000\n'
        'Accept-Encoding: gzip, deflate\n'
        'Accept: */*\n'
        'Connection: keep-alive\n'
        'User-Agent: HTTPie/0.9.3\n'
    )

# Generated at 2022-06-13 21:58:15.923820
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.compat import str
    from httpie.core import main
    from httpie.plugins import SeleniumFormatterPlugin
    from httpie.plugins import ResponseProcessorPlugin
    from httpie.plugins import ViewerPlugin

    color_formatter = ColorFormatter(
        env=None, explicit_json=False, color_scheme='solarized'
    )

    class Viewer(ViewerPlugin):
        name = 'viewer'

        def get_attributes(self) -> dict:
            return {
                'set_viewer_for_type': {
                    'text/plain': 'view'
                }
            }

        def view(self, context, **kwargs):
            color_formatter.format_body(body=context.content, mime=context.content_type)


# Generated at 2022-06-13 21:58:19.109860
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    class FakeEnv:
        def __init__(self, colors=True):
            self.colors = colors
    
    assert ColorFormatter(FakeEnv(colors=True)).formatter

# Generated at 2022-06-13 21:58:31.401423
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import httpie
    f = httpie.plugins.builtin.colors.ColorFormatter(
        Environment(colors=256), color_scheme="nord",
    )

# Generated at 2022-06-13 21:58:42.664773
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.output import get_library
    formatter = ColorFormatter(get_library().env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert formatter.format_body("{'foo':'bar'}", 'application/json') == "\x1b[33m{\x1b[39;49;00m\x1b[33m'foo'\x1b[39;49;00m\x1b[33m:\x1b[39;49;00m\x1b[33m'bar'\x1b[39;49;00m\x1b[33m}\x1b[39;49;00m\x1b[39;49;00m\n"

# Generated at 2022-06-13 21:58:50.330515
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import tempfile
    import os
    import sys
    import os.path
    import subprocess
    import shutil

    basedir = os.path.dirname(os.path.abspath(__file__))
    prefix = 'test_ColorFormatter_'
    dirpath = tempfile.mkdtemp(prefix=prefix, dir=basedir)

    # Diagnostics
    if len(os.listdir(dirpath)) != 0:
        raise Exception('Created dir {} is not empty'.format(dirpath))


# Generated at 2022-06-13 21:58:51.064120
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    return ColorFormatter

# Generated at 2022-06-13 21:59:02.203383
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    text = '{"url": "https://www.amazon.com/dp/B07JLNNTHR"}'
    env = Environment(
        colors=256,
        headers=False,
        output_file=None,
        stdin=None,
        verbose=False,
    )
    formatter = ColorFormatter(env, color_scheme='solarized')
    lexer = formatter.get_lexer_for_body('application/json', text)
    assert lexer
    res = pygments.highlight(code=text, lexer=lexer, formatter=formatter.formatter)
    assert res

# Generated at 2022-06-13 21:59:10.167306
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    env = Environment(
        colors=True,
        style='solarized'
    )
    formatter = ColorFormatter(env=env)

    def _run(mime, body):
        actual = formatter.format_body(body, mime)
        return actual

    # Test colorization
    json_body = '{"key": "value"}'
    expected = u'%c(yellow)%s%c(reset)' % (u'\u001b', json_body, u'\u001b')
    actual = _run('application/json', json_body)
    assert actual == expected

    html_body = '<h1>Header</h1>'

# Generated at 2022-06-13 21:59:20.343120
# Unit test for method format_body of class ColorFormatter

# Generated at 2022-06-13 21:59:24.198911
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    body = "var_dump(\"OK\");"
    c = ColorFormatter(Environment())
    assert c.format_body(body=body, mime='text/plain') == 'var_dump(\"OK\");'

# Generated at 2022-06-13 21:59:57.525134
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('text/plain') == TextLexer
    assert get_lexer('application/json') == PygmentsHttpLexer
    assert get_lexer('application/json', explicit_json=True) == \
           pygments.lexers.JsonLexer
    assert get_lexer('application/json', explicit_json=True,
                     body='{"key": "value"}') == pygments.lexers.JsonLexer
    assert get_lexer('application/json', explicit_json=True,
                     body='Invalid JSON') == PygmentsHttpLexer
    assert get_lexer('text/html') == pygments.lexers.HtmlLexer
    assert get_lexer('text/x-python') == pygments.lexers.PythonLexer
    assert get_lexer('text/x-python-script')

# Generated at 2022-06-13 22:00:08.325564
# Unit test for function get_lexer
def test_get_lexer():
    from pygments.lexers import get_lexer_by_name, guess_lexer
    # Test for mime type application/json
    # with no body
    assert get_lexer_by_name('json') == get_lexer('application/json')
    # Test for mime type application/json
    # with body
    assert get_lexer_by_name('json') == get_lexer('application/json',
                                                  body='{"key":"value"}')
    # Test for mime type application/json
    # with body
    assert get_lexer_by_name('json') == get_lexer('application/json',
                                                  body='{"key":"value"}',
                                                  explicit_json=True)
    # Test for mime type application/json-home
    # with body
    assert get_

# Generated at 2022-06-13 22:00:14.808650
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    #fake environment
    env = Environment()
    #default arguments
    explicit_json = False
    color_scheme = DEFAULT_STYLE
    kwargs = {}
    
    cf = ColorFormatter(env, explicit_json, color_scheme, **kwargs)
    assert(cf.group_name == 'colors')
    assert(cf.enabled)
    assert(cf.explicit_json == explicit_json)
    assert(cf.color_scheme == color_scheme)
    assert(cf.kwargs == kwargs)

# Generated at 2022-06-13 22:00:28.137476
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    class SUT(ColorFormatter):
        def format_headers(self, headers: str) -> str:
            return headers
        def get_lexer_for_body(self, mime: str, body: str) -> Optional[Type[Lexer]]:
            return None
    env = Environment()
    env.colors = True
    sut = SUT(env, explicit_json=False, color_scheme=DEFAULT_STYLE)


# Generated at 2022-06-13 22:00:36.522679
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.plugins import FormatterPluginManager
    from httpie.environment import Environment

    class TestPlugin(FormatterPlugin):
        group_name = 'test'

        def format_headers(self, headers):
            return headers

        def format_body(self, body, mime):
            return body

    class TestPlugin2(FormatterPlugin):
        group_name = 'test2'
        enabled = False

    with open('tests/fixtures/color_formatter_test.json', 'rb') as f:
        json_string = f.read()

    # Format json with explicit_json=False and as_form=True
    env = Environment(colors=False)
    cf = ColorFormatter(env, explicit_json=False, as_form=True)

# Generated at 2022-06-13 22:00:44.413726
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    import httpie.plugins
    plugins = [p for p in httpie.plugins.plugins if 'colors' in p.group_name]
    for p in plugins:
        if p.__name__ == "ColorFormatter":
            assert p(None, color_scheme=DEFAULT_STYLE).enabled == True
    #test for get_available_styles()
    assert DEFAULT_STYLE in p.get_available_styles()
    

# Generated at 2022-06-13 22:00:46.629927
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    f = ColorFormatter(env, color_scheme='solarized', explicit_json=False)

# Generated at 2022-06-13 22:00:56.814221
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from httpie.context import Environment
    # Mock environment
    env = Environment()
    env.colors = 256
    # Init formatter plugin
    f = ColorFormatter(env, color_scheme=SOLARIZED_STYLE)
    # Run formatter method on mock data
    mime = 'application/json'
    body = '[{"id": 1, "name": "first", "value": 443523},'\
            ' {"id": 2, "name": "second", "value": 11}, '\
            '{"id": 3, "name": "third", "value": 9.81}]'
    result = f.format_body(body, mime)
    # Check if the method returns right colorized result

# Generated at 2022-06-13 22:01:07.475306
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # arrange
    mime = "application/json"
    body = '{"key":"value"}'
    formatter = ColorFormatter(Environment(colors=True), explicit_json=False)

    # action
    result = formatter.format_body(body, mime)

    # assert
    assert result == '<span style="color:#708"><span style="font-weight:bold">{</span><span style="color:#708">"<span style="color:#07a">key</span>"<span style="color:#708">:</span>"<span style="color:#07a">value</span>"<span style="color:#708">}</span></span>'