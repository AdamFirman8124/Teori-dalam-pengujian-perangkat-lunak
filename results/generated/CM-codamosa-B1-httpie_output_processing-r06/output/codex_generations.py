

# Generated at 2026-10-25 07:58:49.501554
# Unit test for constructor of class Conversion
def test_Conversion():
    conversion = Conversion()

    assert isinstance(conversion, Conversion)
    assert conversion.__dict__ == {}

# Generated at 2026-10-25 07:59:06.268857
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 07:59:08.709483
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 07:59:11.172136
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 07:59:13.593463
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 07:59:16.003040
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 07:59:18.420010
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 07:59:20.942528
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 07:59:23.355587
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 07:59:25.770333
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 07:59:28.185069
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 07:59:30.598602
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 07:59:33.012556
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 07:59:35.453740
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 07:59:37.884775
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 07:59:40.298339
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 07:59:42.712161
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 07:59:45.129997
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 07:59:47.550165
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 07:59:49.965307
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 07:59:52.376840
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 07:59:54.796151
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 07:59:57.204703
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 07:59:59.620110
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:00:02.033779
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:00:04.448012
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:00:06.862208
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:00:09.276956
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:00:11.690682
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:00:14.106265
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:00:16.519908
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:00:18.933949
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:00:21.348443
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:00:23.763387
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:00:26.177416
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:00:37.944717
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():from httpie.plugins import FormatterPlugin


# Generated at 2026-10-25 08:00:48.884998
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Mock(spec=Environment)

    first_formatter = Mock()
    first_formatter.enabled = True
    first_formatter.format_headers.return_value = "formatted-once"

    disabled_formatter = Mock()
    disabled_formatter.enabled = False

    second_formatter = Mock()
    second_formatter.enabled = True
    second_formatter.format_headers.return_value = "formatted-twice"

    first_class = Mock(return_value=first_formatter)
    disabled_class = Mock(return_value=disabled_formatter)
    second_class = Mock(return_value=second_formatter)

    plugins = {
        "test-group": [first_class, disabled_class, second_class],
    }

    with patch.object(
        plugin_manager,
        "get_formatters_grouped",
        return_value=plugins,
    ):
        formatting = Formatting(
            groups=["test-group"],
            env=env,
            option="value",
        )

        result = formatting.format_headers("original headers")

    assert result == "formatted-twice"

    first_class.assert_called_once_with(env=env, option="value")
    disabled_class.assert_called_once_with(env=env, option="value")
    second_class.assert_called_once_with(env=env, option="value")

    first_formatter.format_headers.assert_called_once_with("original headers")
    second_formatter.format_headers.assert_called_once_with("formatted-once")
    disabled_formatter.format_headers.assert_not_called()

# Generated at 2026-10-25 08:00:58.712132
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-25 08:01:01.130324
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:01:03.543883
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:01:05.958088
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:01:08.372340
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:10.787446
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:13.200864
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:15.615748
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:18.028998
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:20.618559
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:23.031114
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:25.445313
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:27.861260
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:30.273927
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:01:32.686601
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:01:35.100302
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:01:37.518758
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:39.929120
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:42.346867
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:44.754967
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:47.169289
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:49.583313
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:01:51.997010
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:01:53.680794
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from httpie.plugins.base import BaseFormatter


# Generated at 2026-10-25 08:02:05.642028
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-25 08:02:16.763689
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock


def test_Formatting(monkeypatch):
    env = Mock(spec=Environment)

    enabled_formatter_1 = Mock(enabled=True)
    disabled_formatter = Mock(enabled=False)
    enabled_formatter_2 = Mock(enabled=True)

    formatter_class_1 = Mock(return_value=enabled_formatter_1)
    formatter_class_2 = Mock(return_value=disabled_formatter)
    formatter_class_3 = Mock(return_value=enabled_formatter_2)

    get_formatters_grouped = Mock(return_value={
        'group_1': [formatter_class_1, formatter_class_2],
        'group_2': [formatter_class_3],
    })
    monkeypatch.setattr(
        plugin_manager,
        'get_formatters_grouped',
        get_formatters_grouped,
    )

    formatting = Formatting(
        groups=['group_1', 'group_2'],
        env=env,
        option='value',
    )

    get_formatters_grouped.assert_called_once_with()
    formatter_class_1.assert_called_once_with(env=env, option='value')
    formatter_class_2.assert_called_once_with(env=env, option='value')
    formatter_class_3.assert_called_once_with(env=env, option='value')

    assert formatting.enabled_plugins == [
        enabled_formatter_1,
        enabled_formatter_2,
    ]

# Generated at 2026-10-25 08:02:23.207582
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from unittest.mock import Mock

    first_formatter = Mock()
    first_formatter.format_headers.return_value = "first formatted headers"

    second_formatter = Mock()
    second_formatter.format_headers.return_value = "final formatted headers"

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_formatter, second_formatter]

    result = formatting.format_headers("original headers")

    first_formatter.format_headers.assert_called_once_with("original headers")
    second_formatter.format_headers.assert_called_once_with(
        "first formatted headers"
    )
    assert result == "final formatted headers"

# Generated at 2026-10-25 08:02:25.675550
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:02:28.121453
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:02:30.534085
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:02:32.948030
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:02:35.363064
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:02:37.777863
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:02:40.366196
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:02:42.779852
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:02:45.193615
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:02:47.607286
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:02:50.020211
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:02:52.563224
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:02:54.991208
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:03:02.427549
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-25 08:03:13.117935
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Mock(spec=Environment)

    enabled_plugin = Mock()
    enabled_plugin.enabled = True

    disabled_plugin = Mock()
    disabled_plugin.enabled = False

    another_enabled_plugin = Mock()
    another_enabled_plugin.enabled = True

    enabled_cls = Mock(return_value=enabled_plugin)
    disabled_cls = Mock(return_value=disabled_plugin)
    another_enabled_cls = Mock(return_value=another_enabled_plugin)

    available_plugins = {
        'group1': [enabled_cls, disabled_cls],
        'group2': [another_enabled_cls],
    }

    with patch.object(
        plugin_manager,
        'get_formatters_grouped',
        return_value=available_plugins,
    ):
        formatting = Formatting(
            groups=['group1', 'group2'],
            env=env,
            option='value',
        )

    enabled_cls.assert_called_once_with(env=env, option='value')
    disabled_cls.assert_called_once_with(env=env, option='value')
    another_enabled_cls.assert_called_once_with(env=env, option='value')

    assert formatting.enabled_plugins == [
        enabled_plugin,
        another_enabled_plugin,
    ]

# Generated at 2026-10-25 08:03:25.263218
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:03:30.982502
# Unit test for constructor of class Formatting
def test_Formatting():formatter = Formatting(groups=[])
assert formatter.enabled_plugins == []
assert formatter.format_headers("Content-Type: text/plain") == "Content-Type: text/plain"
assert formatter.format_body("hello", "text/plain") == "hello"
assert formatter.format_body("hello", "not-a-mime") == "hello"

# Generated at 2026-10-25 08:03:48.692192
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:03:51.239429
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:03:53.654736
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:03:56.068504
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:04:02.026273
# Unit test for constructor of class Formatting
def test_Formatting():formatting = Formatting(groups=[])

# Generated at 2026-10-25 08:04:11.306196
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock


# Unit test for constructor of class Formatting
def test_Formatting(monkeypatch):
    env = Mock(spec=Environment)

    enabled_plugin = Mock()
    enabled_plugin.enabled = True

    disabled_plugin = Mock()
    disabled_plugin.enabled = False

    enabled_plugin_class = Mock(return_value=enabled_plugin)
    disabled_plugin_class = Mock(return_value=disabled_plugin)

    get_formatters_grouped = Mock(return_value={
        'format': [enabled_plugin_class, disabled_plugin_class],
    })
    monkeypatch.setattr(
        plugin_manager,
        'get_formatters_grouped',
        get_formatters_grouped,
    )

    formatting = Formatting(
        groups=['format'],
        env=env,
        option='value',
    )

    get_formatters_grouped.assert_called_once_with()
    enabled_plugin_class.assert_called_once_with(
        env=env,
        option='value',
    )
    disabled_plugin_class.assert_called_once_with(
        env=env,
        option='value',
    )

    assert formatting.enabled_plugins == [enabled_plugin]

# Generated at 2026-10-25 08:04:22.710268
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:04:25.128798
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:04:27.545757
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:04:29.958590
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:04:32.374470
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:04:34.788403
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:04:37.201824
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:04:39.617512
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:04:42.032078
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:04:44.447970
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:04:46.860320
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:04:49.275761
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:04:51.688499
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:04:54.107426
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:04:56.520064
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:04:58.938799
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:05:01.352875
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:05:03.875049
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:05:13.397733
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-25 08:05:19.966264
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    first_formatter = Mock()
    first_formatter.format_headers.return_value = "first formatted headers"

    second_formatter = Mock()
    second_formatter.format_headers.return_value = "final formatted headers"

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_formatter, second_formatter]

    result = formatting.format_headers("original headers")

    assert result == "final formatted headers"
    first_formatter.format_headers.assert_called_once_with("original headers")
    second_formatter.format_headers.assert_called_once_with(
        "first formatted headers"
    )

# Generated at 2026-10-25 08:05:31.728185
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = MagicMock(spec=Environment)

    first_formatter = MagicMock()
    first_formatter.enabled = True
    first_formatter.format_headers.return_value = "X-First: 1"

    disabled_formatter = MagicMock()
    disabled_formatter.enabled = False

    second_formatter = MagicMock()
    second_formatter.enabled = True
    second_formatter.format_headers.return_value = "X-First: 1\nX-Second: 2"

    first_class = MagicMock(return_value=first_formatter)
    disabled_class = MagicMock(return_value=disabled_formatter)
    second_class = MagicMock(return_value=second_formatter)

    available_plugins = {
        "headers": [first_class, disabled_class, second_class],
    }

    with patch.object(
        plugin_manager,
        "get_formatters_grouped",
        return_value=available_plugins,
    ):
        formatting = Formatting(groups=["headers"], env=env)
        result = formatting.format_headers("Original: value")

    assert result == "X-First: 1\nX-Second: 2"

    first_formatter.format_headers.assert_called_once_with("Original: value")
    second_formatter.format_headers.assert_called_once_with("X-First: 1")
    disabled_formatter.format_headers.assert_not_called()

    first_class.assert_called_once_with(env=env)
    disabled_class.assert_called_once_with(env=env)
    second_class.assert_called_once_with(env=env)

# Generated at 2026-10-25 08:05:43.808455
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import MagicMock, patch


# Generated at 2026-10-25 08:05:54.075320
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-25 08:05:56.489885
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:05:58.902496
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:06:01.316436
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:06:03.899558
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:06:06.392114
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:06:07.726933
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from httpie.plugins.base import BaseFormatter


# Generated at 2026-10-25 08:06:19.590906
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from unittest.mock import Mock

    first_processor = Mock()
    first_processor.format_headers.return_value = 'Content-Type: application/json'

    second_processor = Mock()
    second_processor.format_headers.return_value = 'CONTENT-TYPE: APPLICATION/JSON'

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_processor, second_processor]

    result = formatting.format_headers('content-type: application/json')

    assert result == 'CONTENT-TYPE: APPLICATION/JSON'
    first_processor.format_headers.assert_called_once_with(
        'content-type: application/json'
    )
    second_processor.format_headers.assert_called_once_with(
        'Content-Type: application/json'
    )

# Generated at 2026-10-25 08:06:30.404447
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = object()

    first_plugin = Mock()
    first_plugin.enabled = True
    first_plugin.format_headers.side_effect = lambda headers: (
        headers + "\nX-First: one"
    )

    disabled_plugin = Mock()
    disabled_plugin.enabled = False

    second_plugin = Mock()
    second_plugin.enabled = True
    second_plugin.format_headers.side_effect = lambda headers: (
        headers + "\nX-Second: two"
    )

    first_cls = Mock(return_value=first_plugin)
    disabled_cls = Mock(return_value=disabled_plugin)
    second_cls = Mock(return_value=second_plugin)

    grouped_plugins = {
        "test": [first_cls, disabled_cls, second_cls],
    }

    with patch.object(
        plugin_manager,
        "get_formatters_grouped",
        return_value=grouped_plugins,
    ):
        formatting = Formatting(groups=["test"], env=env)
        result = formatting.format_headers("Content-Type: text/plain")

    assert result == (
        "Content-Type: text/plain"
        "\nX-First: one"
        "\nX-Second: two"
    )

    first_cls.assert_called_once_with(env=env)
    disabled_cls.assert_called_once_with(env=env)
    second_cls.assert_called_once_with(env=env)

    first_plugin.format_headers.assert_called_once_with(
        "Content-Type: text/plain"
    )
    disabled_plugin.format_headers.assert_not_called()
    second_plugin.format_headers.assert_called_once_with(
        "Content-Type: text/plain\nX-First: one"
    )

# Generated at 2026-10-25 08:06:40.415436
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Mock()

    first_formatter = Mock()
    first_formatter.enabled = True
    first_formatter.format_headers.return_value = "first formatted"

    disabled_formatter = Mock()
    disabled_formatter.enabled = False

    second_formatter = Mock()
    second_formatter.enabled = True
    second_formatter.format_headers.return_value = "fully formatted"

    first_cls = Mock(return_value=first_formatter)
    disabled_cls = Mock(return_value=disabled_formatter)
    second_cls = Mock(return_value=second_formatter)

    available_plugins = {
        "test-group": [first_cls, disabled_cls, second_cls],
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

        result = formatting.format_headers("original headers")

    assert result == "fully formatted"

    first_cls.assert_called_once_with(env=env, option="value")
    disabled_cls.assert_called_once_with(env=env, option="value")
    second_cls.assert_called_once_with(env=env, option="value")

    first_formatter.format_headers.assert_called_once_with("original headers")
    disabled_formatter.format_headers.assert_not_called()
    second_formatter.format_headers.assert_called_once_with("first formatted")

# Generated at 2026-10-25 08:06:49.654269
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock


def test_Formatting(monkeypatch):
    env = Mock(spec=Environment)

    enabled_plugin = Mock()
    enabled_plugin.enabled = True

    disabled_plugin = Mock()
    disabled_plugin.enabled = False

    another_enabled_plugin = Mock()
    another_enabled_plugin.enabled = True

    enabled_cls = Mock(return_value=enabled_plugin)
    disabled_cls = Mock(return_value=disabled_plugin)
    another_enabled_cls = Mock(return_value=another_enabled_plugin)

    available_plugins = {
        'group1': [enabled_cls, disabled_cls],
        'group2': [another_enabled_cls],
    }

    monkeypatch.setattr(
        plugin_manager,
        'get_formatters_grouped',
        Mock(return_value=available_plugins),
    )

    formatting = Formatting(
        groups=['group1', 'group2'],
        env=env,
        option='value',
    )

    plugin_manager.get_formatters_grouped.assert_called_once_with()
    enabled_cls.assert_called_once_with(env=env, option='value')
    disabled_cls.assert_called_once_with(env=env, option='value')
    another_enabled_cls.assert_called_once_with(env=env, option='value')

    assert formatting.enabled_plugins == [
        enabled_plugin,
        another_enabled_plugin,
    ]

# Generated at 2026-10-25 08:06:52.069741
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:06:54.482435
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:06:56.894626
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:06:59.298088
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:07:01.712861
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:07:04.125099
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:07:14.834531
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-25 08:07:25.893770
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Mock()

    enabled_plugin_1 = Mock(enabled=True)
    disabled_plugin = Mock(enabled=False)
    enabled_plugin_2 = Mock(enabled=True)

    formatter_class_1 = Mock(return_value=enabled_plugin_1)
    formatter_class_2 = Mock(return_value=disabled_plugin)
    formatter_class_3 = Mock(return_value=enabled_plugin_2)

    available_plugins = {
        "group_1": [formatter_class_1, formatter_class_2],
        "group_2": [formatter_class_3],
    }

    with patch.object(
        plugin_manager,
        "get_formatters_grouped",
        return_value=available_plugins,
    ) as get_formatters_grouped:
        formatting = Formatting(
            groups=["group_1", "group_2"],
            env=env,
            option="value",
        )

    get_formatters_grouped.assert_called_once_with()

    formatter_class_1.assert_called_once_with(env=env, option="value")
    formatter_class_2.assert_called_once_with(env=env, option="value")
    formatter_class_3.assert_called_once_with(env=env, option="value")

    assert formatting.enabled_plugins == [
        enabled_plugin_1,
        enabled_plugin_2,
    ]

# Generated at 2026-10-25 08:07:48.841784
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    class FormatterPlugin:
        def __init__(self, suffix):
            self.suffix = suffix
            self.calls = []

        def module_0.format_body(self, content, mime):
            self.calls.append((content, mime))
            return content + self.suffix

    first_plugin = FormatterPlugin("-first")
    second_plugin = FormatterPlugin("-second")

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_plugin, second_plugin]

    result = formatting.format_body("content", "text/plain")

    assert result == "content-first-second"
    assert first_plugin.calls == [("content", "text/plain")]
    assert second_plugin.calls == [("content-first", "text/plain")]

    # Invalid MIME types must leave the content unchanged and skip plugins.
    result = formatting.format_body("unchanged", "invalid-mime")

    assert result == "unchanged"
    assert first_plugin.calls == [("content", "text/plain")]
    assert second_plugin.calls == [("content-first", "text/plain")]

# Generated at 2026-10-25 08:07:51.432172
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:07:53.951440
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:07:56.366606
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:07:58.780831
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:08:01.466259
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:08:03.957664
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:08:06.368711
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:08:08.782170
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:08:11.194315
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:08:13.608050
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:08:16.023923
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:08:18.441186
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:08:20.859213
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:23.270282
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:25.689698
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:28.101330
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:30.518051
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:32.936051
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:35.350135
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:37.799369
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:40.179905
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:42.594535
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:45.009810
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:47.426348
# Unit test for method format_headers of class Formatting