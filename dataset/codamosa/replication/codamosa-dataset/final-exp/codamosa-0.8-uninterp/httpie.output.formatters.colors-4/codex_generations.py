

# Generated at 2022-06-13 21:51:33.692100
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized256') is Solarized256Style
    assert ColorFormatter.get_style_class(DEFAULT_STYLE) is not Solarized256Style

# Generated at 2022-06-13 21:51:40.897480
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    class MockReport:
        def __init__(self):
            self.errors = []
            self.count = 0

        def error(self, message, type_):
            self.errors.append(message)
            self.count += 1

    report = MockReport()
    lexer = SimplifiedHTTPLexer(report)
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']
    assert 'root' in lexer.tokens
    assert report.count == 0

# Generated at 2022-06-13 21:51:43.047067
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter({})
    body = '{"key":"value"}'
    mime = 'application/json'
    assert formatter.format_body(body, mime) == body

# Generated at 2022-06-13 21:51:44.973197
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style

# Generated at 2022-06-13 21:51:54.135135
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    environment: Environment = Environment(colors=256, style=SOLARIZED_STYLE)
    ColorFormatter.__init__(environment)
    assert environment.style == SOLARIZED_STYLE
    assert environment.colors
    assert environment.formatter
    assert environment.http_lexer
    assert environment.explicit_json
    environment.style = 'fruity'
    assert environment.style != SOLARIZED_STYLE
    assert environment.style == 'fruity'
    environment.style = SOLARIZED_STYLE
    assert environment.style == SOLARIZED_STYLE
    environment.colors = 0
    assert environment.colors == 0
    environment.colors = 256
    assert environment.colors == 256
    environment.explicit_json = True

# Generated at 2022-06-13 21:51:59.029406
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('default') == pygments.styles.get_style_by_name('default')
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style
    assert ColorFormatter.get_style_class('auto') == pygments.style.Style

# Generated at 2022-06-13 21:52:06.821712
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import jsonschema
    formatter = ColorFormatter(
        env=None,
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )
    body = jsonschema.Draft7Validator.META_SCHEMA
    mime = 'application/json'
    assert(formatter.format_body(body=body, mime=mime) == body)
    mime = 'application/text'
    assert(formatter.format_body(body=body, mime=mime) == body)



# Generated at 2022-06-13 21:52:21.528648
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    assert ColorFormatter.get_lexer_for_body('application/json', '[]') == pygments.lexers.get_lexer_by_name('json')
    assert ColorFormatter.get_lexer_for_body('text/html', '') == pygments.lexers.get_lexer_by_name('html')
    assert ColorFormatter.get_lexer_for_body('application/javascript', '') == pygments.lexers.get_lexer_by_name('javascript')
    assert ColorFormatter.get_lexer_for_body('text/css', '') == pygments.lexers.get_lexer_by_name('css')

# Generated at 2022-06-13 21:52:22.278485
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    assert True

# Generated at 2022-06-13 21:52:23.867092
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    assert ColorFormatter is not None

# Generated at 2022-06-13 21:52:32.284079
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == "HTTP"
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']

# Generated at 2022-06-13 21:52:36.714051
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    print("Starting test_ColorFormatter")
    env = Environment()
    explicit_json = False
    color_scheme = DEFAULT_STYLE
    formatter = ColorFormatter(env, explicit_json, color_scheme)
    assert formatter.explicit_json == explicit_json
    assert formatter.formatter is not None
    assert formatter.http_lexer is not None
    print("Finished test_ColorFormatter")


# Generated at 2022-06-13 21:52:41.321743
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    print(ColorFormatter(None).format_headers(
        headers='''Content-Type: application/json
Content-Length: 4'''))

# Generated at 2022-06-13 21:52:42.076565
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    SimplifiedHTTPLexer()

# Generated at 2022-06-13 21:52:53.242661
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.plugins import as_pygments_lines
    from httpie.context import Environment

    env = Environment(colors=256, stdout_isatty=True)
    color_formatter = ColorFormatter(env)
    headers = ''
    mime_type = ''
    color_lines = as_pygments_lines(color_formatter, headers, mime_type)
    assert color_lines == ['']

    env = Environment()
    color_formatter = ColorFormatter(env)
    headers = 'content-type: application/json\n' \
              'content-type: application/json; charset=utf-8'
    mime_type = ''
    color_lines = as_pygments_lines(color_formatter, headers, mime_type)

# Generated at 2022-06-13 21:52:57.332851
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    class Test:
        pass

    color_format = ColorFormatter(Test())

    color_format.get_style_class('solarized')
    color_format.get_style_class('fruity')
    color_format.get_style_class('monokai')

# Generated at 2022-06-13 21:53:00.454241
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    color_formatter = ColorFormatter(None)
    assert color_formatter.get_style_class(None) == Solarized256Style

# Generated at 2022-06-13 21:53:10.663324
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # In order to test ColorFormatter.format_body, we need to create an instance
    from httpie.context import Environment
    env = Environment(colors=True)
    c = ColorFormatter(env=env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    # Test with a JSON body
    mime = 'application/json'
    body = '{"id": 123}'
    lexer = 'json'
    result = c.format_body(body, mime)
    assert lexer in result, '%s not in %s' % (lexer, result)
    # Test with a HTML body
    mime = 'text/html'
    body = '<html><body></body></html>'
    lexer = 'html'

# Generated at 2022-06-13 21:53:19.496776
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import os
    env = Environment()
    env.stdout_isatty = True
    env.colors = 256
    formatter = ColorFormatter(env, color_scheme = "vs")
    file_path = os.path.dirname(__file__)
    with open(file_path+"/test.txt", "r") as myfile:
        data = myfile.read()
    mime = "text/html"
    lexer = formatter.get_lexer_for_body(mime, data)
    assert lexer.name == 'HTML'
    res = formatter.format_body(data, mime)
    file_path = os.path.dirname(__file__)

# Generated at 2022-06-13 21:53:27.373977
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.plugins import FormatterPlugin
    import pygments.lexers.web as web
    from httpie.context import Environment
    env = Environment(colors=True)
    formatter = ColorFormatter(env)
    assert isinstance(formatter, FormatterPlugin)
    assert formatter.get_lexer_for_body('application/json', '{}') == web.JsonLexer
    asser

# Generated at 2022-06-13 21:53:39.324053
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('solarized') == Solarized256Style
    assert ColorFormatter.get_style_class('fruity') == pygments.styles.Fruity

# Generated at 2022-06-13 21:53:53.115197
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    body = '''
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getLatestVersionResponse xmlns="http://webservices.colegiocontic.com.br/">
      <getLatestVersionResult>string</getLatestVersionResult>
    </getLatestVersionResponse>
  </soap:Body>
</soap:Envelope>
'''
    from httpie.output.formatters.colors import ColorFormatter


# Generated at 2022-06-13 21:54:01.885770
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():

    # Test if, given a Content-Type, it formats json body in json format
    class TestEnvironment:
        colors = 256

    color_formatter = ColorFormatter(env=TestEnvironment())
    json_mime = "application/json"
    html_mime = "text/html"
    json_body = '{"name":"Chuck","company":"Dev"}'
    html_body = '<html><head><title>Test</title></head></html>'
    lexer = pygments.lexers.get_lexer_by_name("json")
    json_body_formatted = pygments.highlight(
                code=json_body,
                lexer=lexer,
                formatter=color_formatter.formatter,)
    assert color_formatter.format_body(json_body, json_mime) == json_

# Generated at 2022-06-13 21:54:03.711934
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.__class__.__name__ == "SimplifiedHTTPlexer"

# Generated at 2022-06-13 21:54:09.741595
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie import input
    from httpie.plugins import plugin_manager
    from httpie.context import Environment

    f = plugin_manager.instantiate_plugin(
        name='colors',
        env=Environment(),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )
    #        HTTP/1.1 101 Switching Protocols\r\n
    #        Upgrade: WebSocket\r\n
    #        Connection: Upgrade\r\n
    #        \r\n
    raw_headers = input.QueryData('Upgrade: WebSocket\r\n').raw
    raw_headers+= input.QueryData('Connection: Upgrade\r\n').raw
    raw_headers+= input.QueryData('\r\n').raw


# Generated at 2022-06-13 21:54:20.268578
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    class FakeEnvironment():
        def __init__(self, colors):
            self.colors = colors

    class FakeFormatter(ColorFormatter):
        """
        This class is a copy of the ColorFormatter class but without
        the init method to avoid having to mock the environment.
        """
        def __init__(self):
            pass

    def test(body, mime, lexer):
        formatter = FakeFormatter()
        assert formatter.get_lexer_for_body(mime, body) == lexer

    formatter = ColorFormatter(FakeEnvironment(8))
    test('{"foo":"bar"}', 'text/plain', None)
    test('{"foo":"bar"}', 'application/json', None)
    formatter.explicit_json = True

# Generated at 2022-06-13 21:54:32.608472
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    input_http = """POST / HTTP/1.1
Host: localhost:4444
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 5
"""

# Generated at 2022-06-13 21:54:35.428657
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment()
    ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)

# Generated at 2022-06-13 21:54:45.336346
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from httpie.plugins import Helpers
    from contextlib import contextmanager
    from httpie.utils import StdoutBytesIO
    import io


    class FakeUnicodeBody:
        def __init__(self, body):
            self.body = body

        def __unicode__(self):
            return self.body


    @contextmanager
    def fake_stdout(stdout):
        real_stdout = sys.stdout
        sys.stdout = io.TextIOWrapper(stdout)
        yield
        sys.stdout = real_stdout


    class TestHelpers(Helpers):
        def __init__(self, *args, **kwargs):
            super(TestHelpers, self).__init__(*args, **kwargs)
            assert 'BINARY' not in self.BODY

# Generated at 2022-06-13 21:54:54.988832
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from httpie.compat import isatty

    class FakeEnv:
        colors = 256
        stdout_isatty = False
        stdin_isatty = False

    env = FakeEnv()
    env.stdout_isatty = isatty(env.stdout)
    env.stdin_isatty = isatty(env.stdin)

    color_formatter = ColorFormatter(env, color_scheme='solarized')
    mime = 'application/json'
    json_body = '[{"id": 1}, {"id": 2, "name": "HTTPie"}]'
    assert color_formatter.get_lexer_for_body(mime, json_body) is not None
    mime = 'application/json+wrong'
    assert color_formatter.get_lexer

# Generated at 2022-06-13 21:55:23.627665
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(colors=256)
    color_formatter = ColorFormatter(env=env)
    headers = """Accept: */*
Accept-Encoding: gzip, deflate, compress
Accept-Language: en-us
Content-Length: 26
Content-Type: application/x-www-form-urlencoded
Host: www.baidu.com
User-Agent: HTTPie/0.9.3"""

# Generated at 2022-06-13 21:55:37.449597
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(colors=256)
    color_formatter = ColorFormatter(env, explicit_json=False, color_scheme='solarized')
    assert color_formatter.enabled
    assert color_formatter.explicit_json == False
    assert color_formatter.formatter.__class__.__name__ == 'Terminal256Formatter'
    assert color_formatter.http_lexer.__class__.__name__ == 'SimplifiedHTTPLexer'
    color_formatter = ColorFormatter(env, explicit_json=False, color_scheme=None)
    assert color_formatter.enabled
    assert color_formatter.explicit_json == False
    assert color_formatter.formatter.__class__.__name__ == 'TerminalFormatter'
    assert color_formatter

# Generated at 2022-06-13 21:55:45.556666
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # Case 1: no lexer found
    formatter = ColorFormatter(Environment(
        stdin=None,
        stdout=None,
        stderr=None,
        colors=256
    ))
    assert formatter.format_body(mime='unknown/type', body='some content') == 'some content'
    # Case 2: lexer found
    formatter = ColorFormatter(Environment(
        stdin=None,
        stdout=None,
        stderr=None,
        colors=256
    ))
    assert formatter.format_body(mime='text/html', body='<html></html>') == '<html></html>'

# Generated at 2022-06-13 21:55:58.382202
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    env = Environment(color=256)
    formatter = ColorFormatter(env, color_scheme='solarized', explicit_json=False)
    # body = '''
    # <!DOCTYPE html>
    # <html>
    # <head>
    # <title>Upload file</title>
    # </head>
    # <body>
    # <h1>Upload file</h1>
    # <form action="" method="post" enctype="multipart/form-data">
    # <input type="file" name="filename" />
    # <input type="submit" value="Upload" />
    # </form>
    # </body>
    # </html>
    # '''
    # mime = 'text/html'
    # lexer = formatter.get_lexer

# Generated at 2022-06-13 21:56:03.113651
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Tests if color formatter is initiated without errors

    colorFormatter = ColorFormatter(Environment(colors = 256), explicit_json=True, color_scheme='day')
    # Check if the color formatter is initiated
    assert colorFormatter

# Generated at 2022-06-13 21:56:19.003785
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    import pytest
    from httpie.formatters.colors import ColorFormatter
    from httpie.plugins import FormatterPlugin
    import httpie.plugins.builtin.colors
    from click.testing import CliRunner

    httpie.plugins.builtin.colors.patch_pygments()


# Generated at 2022-06-13 21:56:26.595598
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    import json
    import httpie.plugins
    httpie.plugins.CLIENT_OUTPUT_OPTIONS_MAP['json'] = 'explicit-json'
    color_formatter = ColorFormatter(Environment(
        colors=256,
        is_windows=False,
        stdin=None,
        stdout=None,
        stdin_isatty=False,
        stdout_isatty=False,
    ), explicit_json=True, color_scheme=Solarized256Style)

    # If there is no content-type header or no body, return None
    assert color_formatter.get_lexer_for_body(
        mime=None,
        body=''
    ) is None

    # If content-type is not recognized, return None
    assert color_formatter.get_lexer_for

# Generated at 2022-06-13 21:56:38.926288
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(
        env=Environment(),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
        force_color=True,
    )

    assert formatter
    assert formatter.get_lexer_for_body(
        mime="text/html",
        body="<html></html>"
    ) == pygments.lexers.get_lexer_for_mimetype("text/html")


    assert formatter.get_lexer_for_body(
        mime="application/xml",
        body="<xml></xml>"
    ) == pygments.lexers.get_lexer_for_mimetype("application/xml")

    assert formatter.explicit_json == False

# Generated at 2022-06-13 21:56:44.990454
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(stdout_isatty=True, colors=256)
    formatter = ColorFormatter(env, color_scheme='solarized')
    assert '\x1b[31mGET\x1b[39m' in formatter.format_headers('GET /')

# Generated at 2022-06-13 21:56:58.443224
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Environment(
        stdout_isatty=True,
        colors=256,
        stdin_isatty=False,
       
        output_options={"pretty": False, "colors": True, "style": "solarized", "format": "colors", "print_body": "all"}
    )
    headers = "Accept: application/json\r\nContent-Type: application/json"
    cf = ColorFormatter(env, color_scheme="solarized")
    assert cf.format_headers(headers) == "\x1b[38;5;37mAccept\x1b[0m: application/json\r\n\x1b[38;5;37mContent-Type\x1b[0m: application/json"

# Generated at 2022-06-13 21:57:38.984025
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('monokai') == pygments.styles.get_style_by_name('monokai')
    assert ColorFormatter.get_style_class('solarized256') == Solarized256Style
    assert ColorFormatter.get_style_class('auto') is None

# Generated at 2022-06-13 21:57:40.206865
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    print(SimplifiedHTTPLexer)

# Generated at 2022-06-13 21:57:43.017280
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    test_env = Environment()
    test_formatter = ColorFormatter(env=test_env)
    assert test_formatter.formatter == TerminalFormatter()

# Generated at 2022-06-13 21:57:45.569492
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    cf = ColorFormatter(
        env=Environment(),
        explicit_json=False,
        color_scheme=DEFAULT_STYLE,
    )
    pass

# Generated at 2022-06-13 21:57:52.897368
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    http_lexer = PygmentsHttpLexer()
    cf = ColorFormatter(None)
    assert cf.get_lexer_for_body("application/json") == \
           cf.get_lexer_for_body("application/json", body="1")
    assert cf.get_lexer_for_body("application/json", body="{\"test\" : 1}") == \
           pygments.lexers.get_lexer_by_name(name="json")

    assert cf.get_lexer_for_body("application/javascript") == \
           cf.get_lexer_for_body("application/javascript", body="alert(\"Test Alert\")")

# Generated at 2022-06-13 21:57:58.349619
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    a = ColorFormatter(ColorFormatter.group_name, True, False)
    assert isinstance(a, ColorFormatter)
    b = ColorFormatter(ColorFormatter.group_name, True, True)
    assert isinstance(b, ColorFormatter)

# Generated at 2022-06-13 21:58:01.745909
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    c = ColorFormatter(
        explicit_json=False,
        color_scheme='solarized',
        env=Environment()
    )
    assert c.group_name == 'colors'

# Generated at 2022-06-13 21:58:02.955796
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    assert SimplifiedHTTPLexer()

# Generated at 2022-06-13 21:58:07.555778
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # ColorFormatter(env, explicit_json=, color_scheme=)
    env = Environment()
    explicit_json = False
    color_scheme = 'solarized'
    ColorFormatter(env, explicit_json, color_scheme)

# Generated at 2022-06-13 21:58:11.419964
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = pygments.lexers.get_lexer_by_name("http")
    assert issubclass(type(lexer), SimplifiedHTTPLexer)



# Generated at 2022-06-13 21:59:23.447242
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.context import Environment
    from httpie.output.colors import ColorFormatter
    env = Environment()
    env.colors = 256
    c = ColorFormatter(env, explicit_json=False, color_scheme='solarized')
    assert c.enabled

# Generated at 2022-06-13 21:59:37.725221
# Unit test for function get_lexer
def test_get_lexer():
    assert not get_lexer('application/xml')
    assert get_lexer('application/xml', explicit_json=True, body='<foo/>')
    assert get_lexer('text/xml', explicit_json=True, body='<foo/>')

    assert get_lexer('application/json+jq')
    assert get_lexer('application/json')

    # css-derived lexers
    assert pygments.lexers.get_lexer_for_mimetype('text/scss')
    assert get_lexer('text/scss')
    assert pygments.lexers.get_lexer_for_mimetype('text/less')
    assert get_lexer('text/less')
    assert pygments.lexers.get_lexer_for_mimetype('text/stylus')

# Generated at 2022-06-13 21:59:39.411290
# Unit test for function get_lexer
def test_get_lexer():
    assert not get_lexer('text/plain', explicit_json=False)

# Generated at 2022-06-13 21:59:49.365965
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    env = Environment(colors=True)
    formatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert formatter.formatter == TerminalFormatter()
    env.colors = 256
    formatter = ColorFormatter(env, explicit_json=False, color_scheme=DEFAULT_STYLE)
    assert formatter.formatter == Terminal256Formatter()

# Generated at 2022-06-13 21:59:58.236978
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('text/plain') is None
    assert get_lexer('text/html') is pygments.lexers.HtmlLexer
    assert get_lexer('text/html; charset=utf-8') is pygments.lexers.HtmlLexer
    assert get_lexer('text/html', explicit_json=True) is pygments.lexers.HtmlLexer
    assert get_lexer('text/html', body='<html></html>') is pygments.lexers.HtmlLexer
    assert get_lexer('text/html', body='{}') is pygments.lexers.HtmlLexer
    assert get_lexer('application/json') is pygments.lexers.JsonLexer
    assert get_lexer('application/json', body='<html></html>') is py

# Generated at 2022-06-13 21:59:59.154459
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    pass

# Generated at 2022-06-13 22:00:01.626304
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # type: () -> None

    c = ColorFormatter(None)
    assert c.explicit_json == False

# Generated at 2022-06-13 22:00:03.898366
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    c = ColorFormatter(explicit_json=False, color_scheme=DEFAULT_STYLE)

# Generated at 2022-06-13 22:00:11.704898
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.compat import isatty

    orig = isatty(1)
    try:
        isatty(1, lambda: True)
        assert ColorFormatter({'colors': 256}).formatter.__repr__() != ''
        isatty(1, lambda: False)
        assert ColorFormatter({'colors': 256}).formatter.__repr__() != ''
    finally:
        isatty(1, orig)


# Generated at 2022-06-13 22:00:18.898924
# Unit test for function get_lexer
def test_get_lexer():
    assert get_lexer('text/html',
                     '<html></html>') == pygments.lexers.get_lexer_by_name('html')
    assert get_lexer('text/plain',
                     '<html></html>') == pygments.lexers.get_lexer_by_name('text')
    assert get_lexer('application/json',
                     '{}') == pygments.lexers.get_lexer_by_name('json')
    assert get_lexer('application/json',
                     '<html></html>') is None
    assert get_lexer('application/x-javascript',
                     '{}') == pygments.lexers.get_lexer_by_name('javascript')