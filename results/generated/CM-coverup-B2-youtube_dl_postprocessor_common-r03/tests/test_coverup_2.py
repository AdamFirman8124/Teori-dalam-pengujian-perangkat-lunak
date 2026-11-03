# file: project/youtube_dl/postprocessor/common.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import youtube_dl.postprocessor.common as common


class _FakeDownloader(object):
    """Minimal stand-in for a downloader object."""


def test_postprocessor_init_default_downloader_is_none():
    # Covers line 35: __init__ must run and assign the default (None).
    pp = common.PostProcessor()
    assert pp._downloader is None


def test_postprocessor_init_with_downloader():
    # Covers line 35 again, with an explicit downloader argument,
    # verifying the assignment actually stores the given object.
    downloader = _FakeDownloader()
    pp = common.PostProcessor(downloader)
    assert pp._downloader is downloader


def test_postprocessor_init_downloader_shadows_class_attribute():
    # The instance attribute set in __init__ must shadow the class-level
    # _downloader = None default.
    downloader = _FakeDownloader()
    pp = common.PostProcessor(downloader=downloader)
    assert common.PostProcessor._downloader is None  # class attr untouched
    assert pp._downloader is downloader              # instance attr set
