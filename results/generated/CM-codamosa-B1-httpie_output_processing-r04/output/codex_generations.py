

# Generated at 2026-10-25 08:27:35.847992
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    first_plugin = Mock()
    first_plugin.format_body.return_value = "formatted once"

    second_plugin = Mock()
    second_plugin.format_body.return_value = "formatted twice"

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_plugin, second_plugin]

    result = formatting.format_body("original content", "application/json")

    assert result == "formatted twice"
    assert first_plugin.format_body.call_args_list == [
        call("original content", "application/json")
    ]
    assert second_plugin.format_body.call_args_list == [
        call("formatted once", "application/json")
    ]

# Generated at 2026-10-25 08:27:38.392314
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:27:40.935262
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:27:43.355731
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:27:45.775710
# Unit test for constructor of class Conversion

# Generated at 2026-10-25 08:27:48.189383
# Unit test for constructor of class Conversion

# Generated at 2026-10-25 08:27:50.611370
# Unit test for constructor of class Conversion

# Generated at 2026-10-25 08:27:53.026669
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:27:55.443752
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:27:57.862280
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:28:00.302233
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:28:02.723411
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:28:05.138217
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:28:07.559092
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:28:09.974690
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:28:12.391206
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:28:14.814705
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:28:17.230185
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:28:19.647843
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:28:22.064427
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:28:24.480915
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:28:26.898577
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:28:29.317153
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:28:31.733469
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:28:34.152082
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:28:36.572887
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:28:38.990816
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:28:41.409866
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:28:43.824949
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:28:46.241793
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:28:48.658129
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:28:51.077074
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:28:53.493568
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:28:55.913209
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:28:58.328137
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:29:03.318675
# Unit test for constructor of class Formatting
def test_Formatting():formatting = Formatting(groups=[])

# Generated at 2026-10-25 08:29:09.874045
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    first_plugin = Mock()
    first_plugin.format_headers.return_value = "formatted by first"

    second_plugin = Mock()
    second_plugin.format_headers.return_value = "formatted by second"

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_plugin, second_plugin]

    result = formatting.format_headers("original headers")

    first_plugin.format_headers.assert_called_once_with("original headers")
    second_plugin.format_headers.assert_called_once_with("formatted by first")
    assert result == "formatted by second"

# Generated at 2026-10-25 08:29:24.313224
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Mock()

    first_plugin = Mock()
    first_plugin.enabled = True
    first_plugin.format_headers.return_value = "First: formatted"

    disabled_plugin = Mock()
    disabled_plugin.enabled = False

    second_plugin = Mock()
    second_plugin.enabled = True
    second_plugin.format_headers.return_value = "Second: formatted"

    first_plugin_class = Mock(return_value=first_plugin)
    disabled_plugin_class = Mock(return_value=disabled_plugin)
    second_plugin_class = Mock(return_value=second_plugin)

    available_plugins = {
        "test-group": [
            first_plugin_class,
            disabled_plugin_class,
            second_plugin_class,
        ]
    }

    with patch.object(
        plugin_manager,
        "get_formatters_grouped",
        return_value=available_plugins,
    ):
        formatting = Formatting(
            groups=["test-group"],
            env=env,
            option="value",
        )

        result = formatting.format_headers("Original: header")

    assert result == "Second: formatted"

    first_plugin_class.assert_called_once_with(env=env, option="value")
    disabled_plugin_class.assert_called_once_with(env=env, option="value")
    second_plugin_class.assert_called_once_with(env=env, option="value")

    first_plugin.format_headers.assert_called_once_with("Original: header")
    disabled_plugin.format_headers.assert_not_called()
    second_plugin.format_headers.assert_called_once_with("First: formatted")

# Generated at 2026-10-25 08:29:26.732467
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:29:29.316875
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:29:31.733059
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:29:34.308217
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:29:36.725535
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:29:39.146057
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:29:41.563022
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:29:43.978469
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:29:46.393687
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:29:48.810346
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:29:51.261785
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:29:53.678451
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:29:56.092281
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:29:58.510382
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:30:00.928979
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:30:03.347029
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:30:05.762232
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:30:08.417242
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:30:25.239147
# Unit test for constructor of class Formatting
def test_Formatting():
    """Unit test for Formatting.__init__."""
    from unittest.mock import MagicMock, patch

    mock_env = MagicMock()

    def make_cls(enabled=True):
        instance = MagicMock()
        instance.enabled = enabled
        cls = MagicMock(return_value=instance)
        return cls, instance

    # 1. empty groups -> no plugins instantiated
    with patch.object(plugin_manager, "get_formatters_grouped",
                      return_value={"a": [make_cls(True)[0]]}):
        f = Formatting(groups=[], env=mock_env)
        assert f.enabled_plugins == []

    # 2. filters out disabled plugins, keeps enabled ones in order
    cls_a, inst_a = make_cls(enabled=True)
    cls_b, inst_b = make_cls(enabled=False)
    cls

# Generated at 2026-10-25 08:30:41.710669
# Unit test for constructor of class Formatting
def test_Formatting():
    """Unit test for Formatting.__init__."""
    from unittest.mock import MagicMock, patch

    mock_env = MagicMock()

    def make_cls(enabled=True):
        instance = MagicMock()
        instance.enabled = enabled
        cls = MagicMock(return_value=instance)
        return cls, instance

    # 1. empty groups -> no plugins instantiated
    with patch.object(plugin_manager, "get_formatters_grouped",
                      return_value={"a": [make_cls(True)[0]]}):
        f = Formatting(groups=[], env=mock_env)
        assert f.enabled_plugins == []

    # 2. filters out disabled plugins, keeps enabled ones in order
    cls_a, inst_a = make_cls(enabled=True)
    cls_b, inst_b = make_cls(enabled=False)
    cls

# Generated at 2026-10-25 08:30:44.132632
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:30:46.549173
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:30:49.001029
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:30:51.538826
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:30:53.955640
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:30:56.569739
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:30:59.011674
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:31:01.405856
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:31:03.825697
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:31:06.241016
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:31:08.657388
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:31:11.077124
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:31:13.814135
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:31:15.149856
# Unit test for constructor of class Formatting
def test_Formatting():formatter = Formatting(groups=[])
assert formatter.enabled_plugins == []
assert formatter.format_headers("Content-Type: text/plain") == "Content-Type: text/plain"
assert formatter.format_body("hello", "text/plain") == "hello"
assert formatter.format_body("hello", "not-a-mime") == "hello"

# Generated at 2026-10-25 08:31:33.651224
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:31:35.288456
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from httpie.plugins.base import BaseFormatter


# Generated at 2026-10-25 08:31:53.713057
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:31:56.132857
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:31:58.705120
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:32:01.120528
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:32:03.694099
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:32:06.112978
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:32:08.537125
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:32:10.954207
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:32:13.371367
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:32:15.928523
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:32:18.325465
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:32:20.735562
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:32:23.153473
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:32:25.572505
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:32:27.995233
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:32:30.408887
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:32:32.823092
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:32:35.243845
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:32:37.710712
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:32:40.129746
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:32:42.543898
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:32:58.727814
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:33:00.270236
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from httpie.plugins.base import BaseFormatter


# Generated at 2026-10-25 08:33:03.347332
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:33:04.810809
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch

# Generated at 2026-10-25 08:33:20.042135
# Unit test for constructor of class Formatting
def test_Formatting():import pytest

# Replace `your_module` with the module containing Formatting
from your_module import Formatting


def test_formatting_constructor_loads_only_enabled_plugins(monkeypatch):
    created = []

    class EnabledFormatter:
        def __init__(self, env, **kwargs):
            created.append(("enabled", env, kwargs))
            self.enabled = True

    class DisabledFormatter:
        def __init__(self, env, **kwargs):
            created.append(("disabled", env, kwargs))
            self.enabled = False

    monkeypatch.setattr(
        "your_module.plugin_manager.get_formatters_grouped",
        lambda: {
            "response": [
                EnabledFormatter,
                DisabledFormatter,
            ]
        },
    )

    env = object()
    formatting = Formatting(
        groups=["response"],
        env=env,
        color=True,
    )

    # Both formatter classes are instantiated.
    assert created == [
        ("enabled", env, {"color": True}),
        ("disabled", env, {"color": True}),
    ]

    # Only enabled formatters are retained.
    assert len(formatting.enabled_plugins) == 1
    assert isinstance(formatting.enabled_plugins[0], EnabledFormatter)

# Generated at 2026-10-25 08:33:22.728237
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:33:25.148648
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:33:27.566206
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:33:30.144765
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:33:32.581502
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:33:34.980492
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:33:37.396147
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:33:39.821031
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:33:42.234856
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:33:44.649773
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:33:46.068815
# Unit test for constructor of class Formatting
def test_Formatting():formatter = Formatting(groups=[])
assert formatter.enabled_plugins == []
assert formatter.format_headers("Content-Type: text/plain") == "Content-Type: text/plain"
assert formatter.format_body("hello", "text/plain") == "hello"
assert formatter.format_body("hello", "not-a-mime") == "hello"

# Generated at 2026-10-25 08:34:02.844787
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():import pytest
from unittest.mock import patch, MagicMock

from httpie.plugins import ConverterPlugin
from httpie.context import Environment
import sys
sys.path.insert(0, '/path/to/your/project')  # adjust as needed
from your_module import Formatting  # module containing the code above


class DummyFormatter:
    """Minimal formatter plugin for testing."""
    enabled = True

    def __init__(self, env=None, **kwargs):
        self.env = env
        self.kwargs = kwargs

    def format_headers(self, headers: str) -> str:
        return headers

    def module_0.format_body(self, content: str, mime: str) -> str:
        return content.upper()


class DisabledFormatter(DummyFormatter):
    enabled = False


def test_format_body_applies_enabled_formatters():
    fmt = Formatting(groups=['group1'], env=Environment())

    # Inject a mock grouped-plugins dict
    with patch.object(fmt, 'enabled_plugins', [DummyFormatter()]):
        result = fmt.format_body('hello', 'application/json')
    assert result == 'HELLO'


def test_format_body_skips_invalid_mime():
    fmt = Formatting(groups=['group1'], env=Environment())

    called = []
    class RecordingFormatter(DummyFormatter):
        def module_0.format_body(self, content, mime):
            called.append(mime)
            return content

    with patch.object(fmt, 'enabled_plugins', [RecordingFormatter()]):
        result = fmt.format_body('hello', 'not-a-mime')  # no slash -> invalid

    assert result == 'hello'
    assert called == []  # formatter never invoked


def test_format_body_chains_multiple_formatters():
    fmt = Formatting(groups=['group1'], env=Environment())

    class SuffixFormatter(DummyFormatter):
        def module_0.format_body(self, content, mime):
            return content + '-A'

    class PrefixFormatter(DummyFormatter):
        def module_0.format_body(self, content, mime):
            return 'B-' + content

    with patch.object(fmt, 'enabled_plugins', [SuffixFormatter(), PrefixFormatter()]):
        result = fmt.format_body('x', 'text/plain')

    assert result == 'B-x-A'  # applied in registration order


def test_format_body_with_no_plugins_returns_content_unchanged():
    fmt = Formatting(groups=['group1'], env=Environment())
    with patch.object(fmt, 'enabled_plugins', []):
        assert fmt.format_body('raw', 'application/json') == 'raw'

# Generated at 2026-10-25 08:34:04.504881
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:34:07.053352
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:34:09.750933
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:34:13.791027
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:34:16.201915
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:34:18.617734
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:34:21.182519
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:34:23.603498
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:34:26.021759
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:34:28.438752
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:34:30.857523
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:34:33.273503
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:34:35.691788
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:34:38.111061
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:34:40.526019
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:34:42.941710
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:34:45.358934
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:34:47.779837
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:34:50.191575
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:34:52.607332
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:34:55.024278
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:34:57.441828
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:34:59.863116
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:35:02.278385
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:35:04.695455
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:35:07.115858
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:35:09.545768
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:35:12.667189
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:35:14.200940
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch

# Generated at 2026-10-25 08:35:15.575646
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:35:17.030451
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from httpie.plugins.base import BaseFormatter


# Generated at 2026-10-25 08:35:24.525685
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:35:27.058093
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:35:29.475833
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:35:31.896381
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:35:34.311703
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:35:36.896988
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:35:39.316372
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:35:41.782987
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:35:44.206881
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:35:46.625227
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:35:49.038898
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:35:51.457231
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:35:53.872949
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:35:56.286765
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:35:58.703790
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:36:01.119875
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:36:03.540449
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:36:05.954966
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:36:08.373738
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:36:10.793588
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:36:13.288535
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:36:15.704179
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:36:18.123293
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:36:20.541275
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:36:22.957814
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:36:25.373069
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:36:27.791725
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:36:30.207482
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:36:32.677277
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:36:35.088208
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:36:44.946906
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:36:47.361726
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:36:49.779688
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:36:52.198330
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:36:54.701422
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:37:12.299059
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:37:13.715914
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:37:16.137553
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:37:18.554106
# Unit test for method format_headers of class Formatting