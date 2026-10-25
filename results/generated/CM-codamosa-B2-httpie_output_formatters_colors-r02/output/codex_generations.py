

# Generated at 2026-10-24 14:38:56.574635
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()

    # Ensure the lexer was constructed successfully
    assert lexer is not None
    assert isinstance(lexer, pygments.lexer.RegexLexer)

    # Ensure the lexer metadata is defined as expected
    assert lexer.name == 'HTTP'
    assert 'http' in lexer.aliases
    assert '*.http' in lexer.filenames

    # Ensure the token rules are defined
    assert 'root' in lexer.tokens
    assert len(lexer.tokens['root']) == 3

# Generated at 2026-10-24 14:38:59.438364
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:39:28.217145
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():import re


# Generated at 2026-10-24 14:39:47.361509
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():style = Solarized256Style()

# Generated at 2026-10-24 14:39:48.798957
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    style = Solarized256Style()

    # Constructor returns an instance of the style class
    assert isinstance(style, Solarized256Style)
    assert isinstance(style, pygments.style.Style)

    # Core style attributes are set
    assert style.background_color == Solarized256Style.BASE03
    assert isinstance(style.styles, dict)
    assert len(style.styles) > 0

    # Every mapped token resolves to a non-empty style string
    for token, value in style.styles.items():
        assert isinstance(token, pygments.token._Token)
        assert isinstance(value, str)
        assert value.strip() != ''

    # A few spot checks against the palette
    assert style.styles[pygments.token.Keyword] == Solarized256Style.GREEN
    assert style.styles[pygments.token.String] == Solarized256Style.CYAN
    assert style.styles[pygments.token.Name.Exception] == Solarized256Style.YELLOW


def test_Solarized256Style_via_pygments():
    # Pygments can look it up and instantiate it by class
    from pygments.formatters.terminal256 import Terminal256Formatter
    formatter = Terminal256Formatter(style=Solarized256Style)
    assert formatter.style is not None

    # It also round-trips through highlight() without error
    out = pygments.highlight('{"a": 1}',
                             pygments.lexers.get_lexer_by_name('json'),
                             formatter)
    assert out  # non-empty, contains ANSI escapes
    assert '\x1b[' in out


def test_get_style_class_fallback():
    # Known style resolves via pygments; unknown name falls back to Solarized256
    assert ColorFormatter.get_style_class('monokai') is not None
    assert ColorFormatter.get_style_class('no-such-style') is Solarized256Style
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style

# Generated at 2026-10-24 14:39:50.229085
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

# Generated at 2026-10-24 14:40:13.678537
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # 1. A real Pygments style resolves to that style's class.
    assert (
        ColorFormatter.get_style_class('fruity')
        is pygments.styles.get_style_by_name('fruity')
    )

    # 2. The bundled 'solarized' name is not a Pygments style -> fallback.
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) is Solarized256Style

    # 3. Unknown style names must not raise; they fall back too.
    assert (
        ColorFormatter.get_style_class('definitely-not-a-style')
        is Solarized256Style
    )

    # 4. Whatever comes back is a usable Pygments style class.
    assert issubclass(
        ColorFormatter.get_style_class('monokai'), pygments.style.Style
    )

# Generated at 2026-10-24 14:40:16.096860
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:40:18.510572
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:40:20.922633
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:40:23.335877
# Unit test for function get_lexer

# Generated at 2026-10-24 14:40:25.750620
# Unit test for function get_lexer

# Generated at 2026-10-24 14:40:28.166508
# Unit test for function get_lexer

# Generated at 2026-10-24 14:40:30.579412
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:40:32.998420
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:40:35.408350
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:40:37.821635
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:40:40.235412
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:40:41.943784
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment


# Generated at 2026-10-24 14:41:12.200583
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from unittest.mock import MagicMock

    # Disabled when the environment has no color support.

# Generated at 2026-10-24 14:41:28.841987
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # 1. A real Pygments style resolves to that style's class.
    assert (
        ColorFormatter.get_style_class('fruity')
        is pygments.styles.get_style_by_name('fruity')
    )

    # 2. The bundled 'solarized' name is not a Pygments style -> fallback.
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) is Solarized256Style

    # 3. Unknown style names must not raise; they fall back too.
    assert (
        ColorFormatter.get_style_class('definitely-not-a-style')
        is Solarized256Style
    )

    # 4. Whatever comes back is a usable Pygments style class.
    assert issubclass(
        ColorFormatter.get_style_class('monokai'), pygments.style.Style
    )

# Generated at 2026-10-24 14:41:45.430695
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

# Generated at 2026-10-24 14:42:01.903221
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # 1. A real Pygments style resolves to that style's class.
    assert (
        ColorFormatter.get_style_class('fruity')
        is pygments.styles.get_style_by_name('fruity')
    )

    # 2. The bundled 'solarized' name is not a Pygments style -> fallback.
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) is Solarized256Style

    # 3. Unknown style names must not raise; they fall back too.
    assert (
        ColorFormatter.get_style_class('definitely-not-a-style')
        is Solarized256Style
    )

    # 4. Whatever comes back is a usable Pygments style class.
    assert issubclass(
        ColorFormatter.get_style_class('monokai'), pygments.style.Style
    )

# Generated at 2026-10-24 14:42:04.546729
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

# Generated at 2026-10-24 14:42:20.963178
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # 1. A real Pygments style resolves to that style's class.
    assert (
        ColorFormatter.get_style_class('fruity')
        is pygments.styles.get_style_by_name('fruity')
    )

    # 2. The bundled 'solarized' name is not a Pygments style -> fallback.
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) is Solarized256Style

    # 3. Unknown style names must not raise; they fall back too.
    assert (
        ColorFormatter.get_style_class('definitely-not-a-style')
        is Solarized256Style
    )

    # 4. Whatever comes back is a usable Pygments style class.
    assert issubclass(
        ColorFormatter.get_style_class('monokai'), pygments.style.Style
    )

# Generated at 2026-10-24 14:42:23.379158
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:42:25.794885
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:42:28.207048
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:42:30.624706
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:42:33.034873
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:42:35.447834
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:42:37.862766
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 14:42:40.275483
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 14:42:42.690928
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 14:42:45.100346
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:42:47.514197
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:42:48.900863
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment


# Generated at 2026-10-24 14:43:24.143879
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:43:26.560098
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:43:28.974161
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:43:31.388307
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:43:33.802471
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:43:36.216044
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:43:38.627429
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:43:41.040023
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:43:43.452588
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:43:45.865790
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:43:48.281948
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:43:52.755285
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():from pygments.styles import get_style_by_name

    # A style that exists in Pygments is returned as-is.

# Generated at 2026-10-24 14:43:55.681883
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:44:22.923014
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:44:25.456461
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:44:29.343457
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:44:31.755300
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:44:34.168295
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:44:36.581950
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 14:44:38.996154
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 14:44:41.412852
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 14:44:43.824220
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:44:46.238595
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:44:48.651450
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:45:33.867256
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:45:36.454816
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:45:38.867338
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:45:41.285815
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:45:43.698799
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:45:46.113279
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:45:48.527518
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 14:45:50.942881
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 14:45:53.353392
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 14:45:55.764941
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:45:58.176352
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:46:00.587403
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:46:02.999798
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:46:05.414405
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:46:07.827718
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:46:10.247341
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:46:12.660013
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:46:15.076081
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:46:17.774351
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:46:20.502455
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:46:21.916113
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():import re


# Generated at 2026-10-24 14:46:27.031098
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 14:46:41.674366
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-24 14:46:43.107433
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-24 14:46:59.696825
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

# Generated at 2026-10-24 14:47:02.110754
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:47:04.621490
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:47:07.034777
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:47:09.709692
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:47:12.128864
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:47:14.656797
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:47:17.072868
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:47:19.484743
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:47:21.900119
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:47:24.314700
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:47:26.729369
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:47:29.158480
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:47:31.579869
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:47:33.993309
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:47:36.407462
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:47:38.821241
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:47:41.240385
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:47:43.655719
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 14:47:46.593539
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from unittest.mock import MagicMock

    # Disabled when the environment has no color support.

# Generated at 2026-10-24 14:47:49.399923
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 14:48:05.848992
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():import re


# Generated at 2026-10-24 14:48:25.125419
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # 1. A real Pygments style resolves to that style's class.
    assert (
        ColorFormatter.get_style_class('fruity')
        is pygments.styles.get_style_by_name('fruity')
    )

    # 2. The bundled 'solarized' name is not a Pygments style -> fallback.
    assert ColorFormatter.get_style_class(SOLARIZED_STYLE) is Solarized256Style

    # 3. Unknown style names must not raise; they fall back too.
    assert (
        ColorFormatter.get_style_class('definitely-not-a-style')
        is Solarized256Style
    )

    # 4. Whatever comes back is a usable Pygments style class.
    assert issubclass(
        ColorFormatter.get_style_class('monokai'), pygments.style.Style
    )

# Generated at 2026-10-24 14:48:27.657253
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 14:48:30.069046
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 14:48:32.485463
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 14:48:34.898127
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:48:37.310380
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:48:39.723436
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 14:48:42.136093
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:48:44.549474
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:48:46.962494
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 14:48:49.376500
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 14:48:51.797122
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 14:48:54.204858
# Unit test for method get_lexer_for_body of class ColorFormatter