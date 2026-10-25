

# Generated at 2026-10-24 10:49:55.622848
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:49:58.041333
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:50:00.458476
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:50:02.880640
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:50:05.300141
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:50:07.716278
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:50:10.133442
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:50:12.548551
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:50:14.966054
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:50:17.383071
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-24 10:50:19.797819
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-24 10:50:22.214212
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-24 10:50:24.631640
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:50:27.047118
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:50:29.476509
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:50:31.893719
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:50:34.310398
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:50:36.728077
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:50:39.145994
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:50:41.562571
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:50:43.981821
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:50:46.400232
# Unit test for function get_lexer

# Generated at 2026-10-24 10:50:48.816997
# Unit test for function get_lexer

# Generated at 2026-10-24 10:50:51.234447
# Unit test for function get_lexer

# Generated at 2026-10-24 10:51:05.487513
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('default') is pygments.styles.get_style_by_name('default')
    assert ColorFormatter.get_style_class('monokai') is pygments.styles.get_style_by_name('monokai')
    assert ColorFormatter.get_style_class('fruity') is pygments.styles.get_style_by_name('fruity')
    assert issubclass(ColorFormatter.get_style_class('default'), pygments.style.Style)
    assert ColorFormatter.get_style_class('no-such-style-xyz123') is Solarized256Style
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style
    assert ColorFormatter.get_style_class('') is Solarized256Style

# Generated at 2026-10-24 10:51:35.287365
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    import pygments.style
    import pygments.styles

    # 1. Known Pygments style: returns that style class.
    assert (
        ColorFormatter.get_style_class("default")
        is pygments.styles.get_style_by_name("default")
    )
    assert (
        ColorFormatter.get_style_class("fruity")
        is pygments.styles.get_style_by_name("fruity")
    )
    assert issubclass(
        ColorFormatter.get_style_class("monokai"),
        pygments.style.Style
    )

    # 2. Bundled/custom style name: falls back to Solarized256Style.
    assert ColorFormatter.get_style_class("solarized") is Solarized256Style
    assert ColorFormatter.get_style_class("auto") is Solarized256Style

    # 3. Unknown style: falls back to Solarized256Style.
    assert (
        ColorFormatter.get_style_class("no-such-style-xyz123")
        is Solarized256Style
    )

# Generated at 2026-10-24 10:51:37.710263
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:51:40.129673
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:51:42.549835
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:51:44.969334
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:51:47.388183
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:51:49.808985
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:51:52.225670
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:51:54.644872
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:51:57.063053
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:51:59.482165
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:52:01.898376
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:52:04.313800
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:52:06.731091
# Unit test for function get_lexer

# Generated at 2026-10-24 10:52:09.147628
# Unit test for function get_lexer

# Generated at 2026-10-24 10:52:11.564314
# Unit test for function get_lexer

# Generated at 2026-10-24 10:52:13.983336
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:52:16.398330
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:52:18.814553
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:52:21.233272
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:52:23.650005
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:52:26.067459
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:52:28.486896
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:52:30.902766
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:52:33.321245
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:52:35.739765
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:52:38.156758
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:52:40.573069
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:52:43.237891
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    assert ColorFormatter.get_style_class('default') is pygments.styles.get_style_by_name('default')
    assert ColorFormatter.get_style_class('monokai') is pygments.styles.get_style_by_name('monokai')
    assert ColorFormatter.get_style_class('fruity') is pygments.styles.get_style_by_name('fruity')
    assert issubclass(ColorFormatter.get_style_class('default'), pygments.style.Style)
    assert ColorFormatter.get_style_class('no-such-style-xyz123') is Solarized256Style
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style
    assert ColorFormatter.get_style_class('') is Solarized256Style

# Generated at 2026-10-24 10:52:44.616794
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:52:47.334121
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from httpie.context import Environment

# Generated at 2026-10-24 10:52:48.714379
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

# Generated at 2026-10-24 10:53:05.420097
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

# Generated at 2026-10-24 10:53:06.742849
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

# Generated at 2026-10-24 10:53:08.070609
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

# Generated at 2026-10-24 10:53:11.139242
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:53:12.475082
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment


# Generated at 2026-10-24 10:53:28.964297
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:53:31.571540
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:53:33.994150
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:53:36.414186
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:53:38.833831
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:53:41.393327
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:53:43.815343
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:53:46.234020
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:53:48.655847
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:53:51.076218
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 10:53:53.497260
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 10:53:55.912317
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 10:53:58.333682
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:54:00.755341
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:54:03.172469
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:54:05.593562
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:54:08.012815
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:54:10.434767
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:54:12.849603
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:54:15.272273
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:54:17.691765
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:54:20.109341
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:54:22.531413
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:54:24.952819
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:54:27.370965
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:54:29.794718
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:54:32.212897
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:54:34.632790
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:54:37.061449
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:54:39.467629
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:54:41.889300
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 10:54:44.552888
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():env = type('E', (), {'colors': 256})()

# Generated at 2026-10-24 10:55:01.014760
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:55:02.534101
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():assert ColorFormatter.get_style_class("default").__name__ == "DefaultStyle"

# Generated at 2026-10-24 10:55:20.364210
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:55:22.792467
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:55:25.314666
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:55:27.734040
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:55:30.153660
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:55:32.570995
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:55:35.158497
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:55:37.579072
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:55:39.991284
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:55:42.410046
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:55:44.833963
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:55:47.251152
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:55:49.673612
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:55:52.094380
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:55:54.510923
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:55:56.931470
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:55:59.353376
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:56:01.799424
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:56:04.190413
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 10:56:06.606194
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 10:56:09.025659
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 10:56:11.449795
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:56:13.873070
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:56:34.707081
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:56:37.879682
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:56:39.206745
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment


# Generated at 2026-10-24 10:56:55.973853
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

# Generated at 2026-10-24 10:56:59.046418
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 10:57:01.943878
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():env = type('E', (), {'colors': 256})()

# Generated at 2026-10-24 10:57:04.699933
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 10:57:07.577201
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():env = type('E', (), {'colors': 256})()

# Generated at 2026-10-24 10:57:08.910948
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:57:11.604373
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from httpie.context import Environment

# Generated at 2026-10-24 10:57:29.592178
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:57:31.511650
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment


# Generated at 2026-10-24 10:57:33.231423
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

# Generated at 2026-10-24 10:57:50.979268
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:57:53.394450
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:57:55.990957
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:57:58.776425
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:58:00.108031
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.context import Environment


# Generated at 2026-10-24 10:58:03.076114
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:58:04.404056
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.context import Environment


# Generated at 2026-10-24 10:58:07.116104
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:58:08.463467
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment


# Generated at 2026-10-24 10:58:11.294752
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:58:12.622909
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.context import Environment


# Generated at 2026-10-24 10:58:15.386613
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:58:21.176080
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-24 10:58:37.560763
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.context import Environment


# Generated at 2026-10-24 10:58:40.082269
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:58:42.504072
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:58:44.924846
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:58:47.340976
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:58:49.898093
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:58:52.315207
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:58:54.735642
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:58:57.157645
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:58:59.590250
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:59:13.734671
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # --json not passed; body highlighted based on its Content-Type.
    env = mock.Mock()
    env.colors = 256

    formatter = ColorFormatter(env=env, explicit_json=False, color_scheme='solarized')

    # JSON body with a JSON content type -> gets syntax-highlighted.
    body = json.dumps({'foo': 'bar', 'n': 1})
    result = formatter.format_body(body, 'application/json')
    assert 'foo' in result
    assert 'bar' in result
    assert '\x1b[' in result  # contains ANSI color escape sequences

    # A lexer is found for JSON, so it must not be the plain TextLexer.
    lexer = formatter.get_lexer_for_body('application/json', body)
    assert lexer is not None
    assert not issubclass(lexer, TextLexer)

    # Unknown content type falls back to TextLexer, body still echoed.
    plain = 'just some text'
    result_plain = formatter.format_body(plain, 'application/octet-stream')
    assert 'just some text' in result_plain

    # explicit_json=True with a wrong Content-Type but valid JSON body
    # forces the JSON lexer and highlights it.
    json_formatter = ColorFormatter(env=env, explicit_json=True, color_scheme='solarized')
    result_forced = json_formatter.format_body(body, 'text/plain')
    assert '\x1b[' in result_forced
    assert 'foo' in result_forced

    # explicit_json=True but the body is not valid JSON -> left unhighlighted.
    not_json = 'this is { not json'
    result_invalid = json_formatter.format_body(not_json, 'text/plain')
    assert 'this is { not json' in result_invalid

# Generated at 2026-10-24 10:59:15.167649
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

# Generated at 2026-10-24 10:59:16.604522
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:59:18.064233
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():assert ColorFormatter.get_style_class("default").__name__ == "DefaultStyle"

# Generated at 2026-10-24 10:59:20.165491
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:59:21.538892
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():assert ColorFormatter.get_style_class("default").__name__ == "DefaultStyle"

# Generated at 2026-10-24 10:59:22.875139
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:59:43.822205
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:59:46.238982
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:59:48.787287
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:59:51.204027
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:59:53.620244
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:59:56.040076
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 10:59:58.470514
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 11:00:00.887157
# Unit test for method get_lexer_for_body of class ColorFormatter