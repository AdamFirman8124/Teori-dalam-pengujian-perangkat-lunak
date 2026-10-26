

# Generated at 2026-10-25 08:06:31.429157
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import MagicMock, patch


# Generated at 2026-10-25 08:06:42.281669
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import Mock, patch


# Generated at 2026-10-25 08:06:49.860423
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    first_formatter = Mock()
    first_formatter.format_headers.return_value = "formatted-by-first"

    second_formatter = Mock()
    second_formatter.format_headers.return_value = "formatted-by-second"

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_formatter, second_formatter]

    result = formatting.format_headers("original-headers")

    assert result == "formatted-by-second"
    first_formatter.format_headers.assert_called_once_with("original-headers")
    second_formatter.format_headers.assert_called_once_with("formatted-by-first")

# Generated at 2026-10-25 08:06:52.502292
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:06:54.918560
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:06:57.329838
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:06:59.732434
# Unit test for function is_valid_mime

# Generated at 2026-10-25 08:07:02.145731
# Unit test for function is_valid_mime

# Generated at 2026-10-25 08:07:04.559868
# Unit test for function is_valid_mime

# Generated at 2026-10-25 08:07:13.401753
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import MagicMock, patch


# Generated at 2026-10-25 08:07:38.807465
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    formatting = Formatting.__new__(Formatting)

    first_plugin = Mock()
    first_plugin.format_body.return_value = "formatted by first"

    second_plugin = Mock()
    second_plugin.format_body.return_value = "formatted by second"

    formatting.enabled_plugins = [first_plugin, second_plugin]

    result = formatting.format_body("original content", "application/json")

    first_plugin.format_body.assert_called_once_with(
        "original content", "application/json"
    )
    second_plugin.format_body.assert_called_once_with(
        "formatted by first", "application/json"
    )
    assert result == "formatted by second"

    # An invalid MIME type must leave the content unchanged and skip plugins.
    first_plugin.reset_mock()
    second_plugin.reset_mock()

    result = formatting.format_body("original content", "invalid-mime")

    assert result == "original content"
    first_plugin.format_body.assert_not_called()
    second_plugin.format_body.assert_not_called()

# Generated at 2026-10-25 08:07:56.502683
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:07:58.914902
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:08:01.533370
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:08:03.966466
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:06.378177
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:08.791417
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:11.204300
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:08:13.617640
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:08:16.031941
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:08:18.445930
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:20.864523
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:23.275972
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:25.691771
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:28.106142
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:30.522799
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:32.939386
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:35.355837
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:37.862149
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:40.203319
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:42.611557
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:45.024843
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:08:47.439503
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:49.851533
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:52.268607
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:54.681392
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:57.095440
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:08:59.512874
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:09:01.929431
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:09:11.462699
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import patch


# Generated at 2026-10-25 08:09:25.201971
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-25 08:09:34.825768
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-25 08:09:37.241550
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:09:39.821235
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:09:42.239881
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:09:44.652539
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:09:47.066968
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:09:49.484288
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:09:51.896305
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:09:54.310307
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:09:56.727037
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:09:59.140285
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:10:01.555970
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:10:03.970553
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:10:06.387460
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:10:08.804396
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:10:11.218597
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:10:13.632876
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:10:16.050696
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:10:18.467817
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:10:20.926257
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:10:23.340770
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:10:25.752904
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:10:28.167380
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:10:30.581190
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:10:32.997508
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:10:35.414586
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:10:37.938256
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:10:40.264920
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:10:42.675886
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:10:48.640382
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():result = Conversion.get_converter("invalid")

# Generated at 2026-10-25 08:11:14.073055
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

# Generated at 2026-10-25 08:11:23.851014
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-25 08:11:26.482913
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:11:28.898601
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:11:31.312375
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:11:33.760908
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:11:36.148465
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:11:38.563733
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:11:40.977857
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:11:43.858296
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:11:46.332208
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:11:48.745425
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:11:51.158379
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:11:53.573507
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:11:55.986880
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:11:58.400387
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:12:00.816394
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:12:03.230930
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:12:05.643647
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:12:08.059413
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:12:10.475976
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:12:12.891581
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:12:15.309966
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:12:17.725978
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:12:20.141639
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:12:22.559898
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:12:24.975362
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:12:27.393058
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:12:29.808632
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:12:32.223258
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:12:34.638716
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:12:37.057078
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:12:39.473403
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:12:41.887334
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:12:44.304281
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:12:46.722285
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:12:49.183270
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:12:51.619516
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:12:54.035131
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:12:56.451188
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:12:58.864881
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:01.270221
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:13:03.689595
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:13:06.107868
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:13:08.520429
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:10.942058
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:13.356142
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:15.768957
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:18.183484
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:20.598917
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:23.016535
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:13:25.462569
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:13:27.847220
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:13:30.275625
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:32.692842
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:35.108461
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:37.524615
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:39.941330
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:42.357800
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:13:44.773182
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:13:47.186815
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:13:49.603816
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:13:52.024110
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:13:54.436494
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:13:56.851940
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:13:59.271455
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:14:01.687773
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:14:04.131344
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:14:06.582297
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:14:09.000203
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:14:11.413392
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:14:13.827975
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:14:16.244636
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:14:18.659712
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:14:21.081828
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:14:23.492698
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:14:25.995640
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:14:28.403874
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:14:30.823365
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:14:33.235958
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:14:35.650139
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:14:38.069025
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:14:40.487123
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:14:42.898379
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:14:45.317530
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:14:47.733017
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:14:50.246031
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:14:52.633656
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:14:55.048725
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:14:57.465791
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:14:59.880027
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:02.294433
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:04.710919
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:15:07.128416
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:15:09.541358
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:15:11.955130
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:15:14.374093
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:15:16.788410
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:15:19.203904
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:21.618522
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:24.035099
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:26.449514
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:15:28.863039
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:15:31.360240
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:15:33.812642
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:36.230193
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:38.642104
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:41.058067
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:15:43.469987
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:15:45.883607
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:15:48.299067
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:50.711757
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:53.126173
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:55.538132
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:15:57.950084
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:16:00.364929
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:16:02.779761
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:16:05.194023
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:16:07.607971
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 08:16:10.021812
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:16:12.434004
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:16:14.847045
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 08:16:17.262295
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:16:19.674785
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:16:22.087354
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 08:16:24.500247
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:16:26.914559
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 08:16:29.328980
# Unit test for method get_converter of class Conversion