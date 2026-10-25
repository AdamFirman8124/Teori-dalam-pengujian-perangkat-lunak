

# Generated at 2026-10-24 11:06:48.124573
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']

    # Constructor must accept the standard Pygments lexer options.
    lexer = SimplifiedHTTPLexer(stripnl=False, ensurenl=False, tabsize=2)
    assert lexer.stripnl is False
    assert lexer.ensurenl is False
    assert lexer.tabsize == 2

    # Sanity check: the lexer is usable and emits the expected header token.
    tokens = list(lexer.get_tokens('Content-Type: application/json'))
    assert tokens[0][0] is pygments.token.Name.Attribute

# Generated at 2026-10-24 11:07:17.318959
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()

    # Inherits Pygments constructor
    assert isinstance(lexer, pygments.lexer.RegexLexer)
    assert isinstance(lexer, Lexer)

    # Class configuration is preserved by constructor
    assert lexer.name == 'HTTP'
    assert 'http' in lexer.aliases
    assert '*.http' in lexer.filenames
    assert 'root' in lexer.tokens
    assert len(lexer.tokens['root']) == 3  # request-line, status-line, header

    # Default Lexer options
    assert lexer.stripnl is True
    assert lexer.stripall is False
    assert lexer.ensurenl is True
    assert lexer.tabsize == 8

    # Constructor accepts custom Lexer options
    custom = SimplifiedHTTPLexer(
        stripnl=False, stripall=True, ensurenl=False, tabsize=4
    )
    assert custom.stripnl is False
    assert custom.stripall is True
    assert custom.ensurenl is False
    assert custom.tabsize == 4

    # Instances are independent and usable
    assert lexer is not custom
    assert list(lexer.get_tokens('GET / HTTP/1.1'))

# Generated at 2026-10-24 11:07:19.740717
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:07:22.162554
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:07:24.736434
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:07:27.155187
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:07:29.573852
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:07:31.990035
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:07:34.411684
# Unit test for function get_lexer

# Generated at 2026-10-24 11:07:36.831459
# Unit test for function get_lexer

# Generated at 2026-10-24 11:07:39.255355
# Unit test for function get_lexer

# Generated at 2026-10-24 11:07:41.677452
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:07:44.102315
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:07:46.524289
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:07:48.954349
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 11:07:51.371343
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 11:07:53.788134
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 11:07:56.207708
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:07:58.625150
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:08:01.046307
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:08:03.458544
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:08:05.877294
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:08:08.296553
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:08:10.714315
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:08:13.135413
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:08:15.557520
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:08:17.976125
# Unit test for function get_lexer

# Generated at 2026-10-24 11:08:20.400518
# Unit test for function get_lexer

# Generated at 2026-10-24 11:08:22.822738
# Unit test for function get_lexer

# Generated at 2026-10-24 11:08:25.239838
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:08:40.749282
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():assert ColorFormatter.get_style_class('monokai') is pygments.styles.get_style_by_name('monokai')

# Generated at 2026-10-24 11:08:42.061990
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:08:59.965043
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:09:02.398038
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:09:05.012634
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:09:07.431978
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:09:09.855032
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:09:12.277051
# Unit test for function get_lexer

# Generated at 2026-10-24 11:09:14.692818
# Unit test for function get_lexer

# Generated at 2026-10-24 11:09:17.241728
# Unit test for function get_lexer

# Generated at 2026-10-24 11:09:19.754395
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:09:22.176949
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:09:24.594925
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:09:27.145227
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:09:29.561395
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:09:31.981378
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:09:34.410229
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:09:36.828664
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:09:39.248774
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:09:41.669971
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 11:09:44.090423
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 11:09:46.510319
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 11:09:48.928537
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:09:51.345707
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:09:53.761833
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:09:56.178622
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:09:58.598081
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:10:01.013481
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:10:03.428546
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:10:05.846753
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:10:08.261265
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:10:10.677072
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:10:13.092558
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:10:15.512076
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:10:17.928459
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:10:20.350434
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:10:22.771485
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:10:25.190075
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:10:27.610517
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:10:30.034229
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:10:46.580962
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()

    # Inherits Pygments constructor
    assert isinstance(lexer, pygments.lexer.RegexLexer)
    assert isinstance(lexer, Lexer)

    # Class configuration is preserved by constructor
    assert lexer.name == 'HTTP'
    assert 'http' in lexer.aliases
    assert '*.http' in lexer.filenames
    assert 'root' in lexer.tokens
    assert len(lexer.tokens['root']) == 3  # request-line, status-line, header

    # Default Lexer options
    assert lexer.stripnl is True
    assert lexer.stripall is False
    assert lexer.ensurenl is True
    assert lexer.tabsize == 8

    # Constructor accepts custom Lexer options
    custom = SimplifiedHTTPLexer(
        stripnl=False, stripall=True, ensurenl=False, tabsize=4
    )
    assert custom.stripnl is False
    assert custom.stripall is True
    assert custom.ensurenl is False
    assert custom.tabsize == 4

    # Instances are independent and usable
    assert lexer is not custom
    assert list(lexer.get_tokens('GET / HTTP/1.1'))

# Generated at 2026-10-24 11:11:04.636217
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:11:07.276145
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:11:09.694057
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:11:12.111995
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:11:14.533133
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:11:16.951005
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:11:19.484292
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:11:21.908795
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:11:24.333086
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:11:26.751571
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:11:29.173944
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:11:31.597381
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:11:34.015780
# Unit test for function get_lexer

# Generated at 2026-10-24 11:11:36.432989
# Unit test for function get_lexer

# Generated at 2026-10-24 11:11:38.854757
# Unit test for function get_lexer

# Generated at 2026-10-24 11:11:41.772127
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:11:58.567899
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.context import Environment


# Generated at 2026-10-24 11:12:01.397750
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:12:04.187144
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:12:05.573256
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.context import Environment


# Generated at 2026-10-24 11:12:08.296376
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:12:09.625321
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment


# Generated at 2026-10-24 11:12:10.975447
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:12:12.347839
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():assert ColorFormatter.get_style_class("default").__name__ == "DefaultStyle"

# Generated at 2026-10-24 11:12:14.867036
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:12:17.285419
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:12:19.706331
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:12:22.123418
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:12:24.543053
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:12:26.962819
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:12:29.382396
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:12:31.798659
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:12:34.215649
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:12:36.639389
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:12:39.059877
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:12:40.491826
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():assert ColorFormatter.get_style_class("default").__name__ == "DefaultStyle"

# Generated at 2026-10-24 11:12:41.867300
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from unittest.mock import Mock
    from httpie.context import Environment

    env = Mock(colors=True, **{'colors': 256})
    formatter = ColorFormatter(env=env, explicit_json=False, color_scheme='solarized')

    # JSON body via correct Content-Type
    lexer = formatter.get_lexer_for_body('application/json', '{"a": 1}')
    assert lexer is not None
    assert lexer.aliases and 'json' in lexer.aliases

    # JSON body via vendor subtype with +json suffix: application/vnd.api+json
    lexer = formatter.get_lexer_for_body('application/vnd.api+json', '{"a": 1}')
    assert lexer is not None
    assert lexer.aliases and 'json' in lexer.aliases

    # Non-JSON body with unknown mime type -> no lexer
    lexer = formatter.get_lexer_for_body('application/octet-stream', '\x00\x01')
    assert lexer is None

    # Plain text falls back to TextLexer
    lexer = formatter.get_lexer_for_body('text/plain', 'hello')
    assert lexer is not None
    assert issubclass(lexer, TextLexer)

    # explicit_json=True overrides a wrong Content-Type when body parses as JSON
    formatter_json = ColorFormatter(env=env, explicit_json=True, color_scheme='solarized')
    lexer = formatter_json.get_lexer_for_body('text/plain', '{"a": 1}')
    assert lexer is not None
    assert lexer.aliases and 'json' in lexer.aliases

    # explicit_json=True but body is NOT valid JSON -> stays non-JSON lexer
    lexer = formatter_json.get_lexer_for_body('text/plain', 'just text')
    assert lexer is not None
    assert issubclass(lexer, TextLexer)

# Generated at 2026-10-24 11:12:43.238750
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:12:45.980330
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from httpie.context import Environment

# Generated at 2026-10-24 11:12:47.302089
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:12:49.970386
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from httpie.context import Environment

# Generated at 2026-10-24 11:13:06.338839
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from unittest.mock import Mock
    from httpie.context import Environment

    env = Mock(colors=True, **{'colors': 256})
    formatter = ColorFormatter(env=env, explicit_json=False, color_scheme='solarized')

    # JSON body via correct Content-Type
    lexer = formatter.get_lexer_for_body('application/json', '{"a": 1}')
    assert lexer is not None
    assert lexer.aliases and 'json' in lexer.aliases

    # JSON body via vendor subtype with +json suffix: application/vnd.api+json
    lexer = formatter.get_lexer_for_body('application/vnd.api+json', '{"a": 1}')
    assert lexer is not None
    assert lexer.aliases and 'json' in lexer.aliases

    # Non-JSON body with unknown mime type -> no lexer
    lexer = formatter.get_lexer_for_body('application/octet-stream', '\x00\x01')
    assert lexer is None

    # Plain text falls back to TextLexer
    lexer = formatter.get_lexer_for_body('text/plain', 'hello')
    assert lexer is not None
    assert issubclass(lexer, TextLexer)

    # explicit_json=True overrides a wrong Content-Type when body parses as JSON
    formatter_json = ColorFormatter(env=env, explicit_json=True, color_scheme='solarized')
    lexer = formatter_json.get_lexer_for_body('text/plain', '{"a": 1}')
    assert lexer is not None
    assert lexer.aliases and 'json' in lexer.aliases

    # explicit_json=True but body is NOT valid JSON -> stays non-JSON lexer
    lexer = formatter_json.get_lexer_for_body('text/plain', 'just text')
    assert lexer is not None
    assert issubclass(lexer, TextLexer)

# Generated at 2026-10-24 11:13:08.859089
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:13:11.282347
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:13:13.787350
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:13:16.213374
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:13:18.633877
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:13:21.052415
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:13:23.614598
# Unit test for function get_lexer

# Generated at 2026-10-24 11:13:26.125563
# Unit test for function get_lexer

# Generated at 2026-10-24 11:13:28.550658
# Unit test for function get_lexer

# Generated at 2026-10-24 11:13:30.966494
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:13:33.384774
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:13:35.803741
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:13:38.221945
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:13:57.220867
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from httpie.context import Environment

# Generated at 2026-10-24 11:14:15.065526
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:14:16.382444
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment


# Generated at 2026-10-24 11:14:19.220749
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:14:36.966221
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:14:39.382354
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:14:41.999460
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:14:43.328883
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.context import Environment


# Generated at 2026-10-24 11:14:45.964191
# Unit test for function get_lexer
def test_get_lexer():
    import pygments.lexers
    from pygments.lexers.special import TextLexer

    lexer = module_0.get_lexer("application/json")
    assert type(lexer).__name__ == "JsonLexer"

    lexer = module_0.get_lexer("text/html")
    assert type(lexer).__name__ == "HtmlLexer"

    lexer = module_0.get_lexer("application/xml")
    assert type(lexer).__name__ == "XmlLexer"

    lexer = module_0.get_lexer("text/css")
    assert type(lexer).__name__ == "CssLexer"

    lexer = module_0.get_lexer("text/x-python")
    assert type(lexer).__name__ == "PythonLexer"

    lexer = module_0.get_lexer("text/plain")
    assert isinstance(lexer, TextLexer)

    lexer = module_0.get_lexer("application/vnd.example+json")
    assert type(lexer).__name__ == "JsonLexer"

    lexer = module_0.get_lexer("application/foo+json")
    assert type(lexer).__name__ == "JsonLexer"

    lexer = module_0.get_lexer("application/x-unknown-xyz")
    assert lexer is None

    lexer = module_0.get_lexer("image/png")
    assert lexer is None

    lexer = module_0.get_lexer("text/plain", explicit_json=True, body='{"a": 1}')
    assert type(lexer).__name__ == "JsonLexer"

    lexer = module_0.get_lexer("text/plain", explicit_json=True, body="[1, 2, 3]")
    assert type(lexer).__name__ == "JsonLexer"

    lexer = module_0.get_lexer("text/plain", explicit_json=True, body="not json")
    assert isinstance(lexer, TextLexer)

    lexer = module_0.get_lexer("text/plain", explicit_json=True, body="")
    assert isinstance(lexer, TextLexer)

    lexer = module_0.get_lexer("text/plain", explicit_json=False, body='{"a": 1}')
    assert isinstance(lexer, TextLexer)

    lexer = module_0.get_lexer("application/json", explicit_json=False, body="not json")
    assert type(lexer).__name__ == "JsonLexer"

# Generated at 2026-10-24 11:14:47.292130
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:15:21.696828
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:15:24.118347
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 11:15:26.541200
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:15:28.972932
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:15:31.390514
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:15:33.811430
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:15:36.236353
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:15:38.650373
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:15:42.031385
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:15:44.451104
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:15:46.869095
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:15:49.287012
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:15:51.706237
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:15:54.124284
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 11:15:56.540879
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:15:58.960950
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:16:01.380866
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:16:03.799157
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:16:06.219029
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:16:08.633347
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 11:16:11.052637
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:16:13.472567
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:16:15.890624
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:16:18.308068
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:16:20.728539
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:16:23.145815
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:16:25.564306
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:16:27.981806
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:16:30.402286
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:16:32.820584
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:16:35.239241
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 11:16:37.655015
# Unit test for method format_headers of class ColorFormatter