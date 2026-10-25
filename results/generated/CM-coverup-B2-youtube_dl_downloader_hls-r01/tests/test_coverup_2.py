# file: project/youtube_dl/downloader/hls.py:30-58
# asked: {"lines": [32, 53, 54, 55, 56, 57, 58], "branches": []}
# gained: {"lines": [32, 53, 54, 55, 56, 57, 58], "branches": []}

import pytest

import youtube_dl.downloader.hls as hls
from youtube_dl.downloader.hls import HlsFD


@pytest.mark.parametrize(
    "manifest",
    [
        "#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts\n#EXT-X-ENDLIST",
        "#EXTM3U\nsegment.ts\n#EXT-X-ENDLIST",
    ],
)
def test_can_download_supported_unencrypted_manifest(monkeypatch, manifest):
    monkeypatch.setattr(hls, "can_decrypt_frag", False)

    assert HlsFD.can_download(manifest, {}) is True


def test_can_download_aes128_when_decryption_is_available(monkeypatch):
    monkeypatch.setattr(hls, "can_decrypt_frag", True)
    manifest = "#EXTM3U\n#EXT-X-KEY:METHOD=AES-128,URI=\"key.bin\"\nsegment.ts"

    assert HlsFD.can_download(manifest, {}) is True


@pytest.mark.parametrize(
    "manifest",
    [
        "#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES,URI=\"key.bin\"\nsegment.ts",
        "#EXTM3U\n#EXT-X-MAP:URI=\"init.mp4\"\nsegment.m4s",
    ],
)
def test_can_download_rejects_unsupported_manifest_features(monkeypatch, manifest):
    monkeypatch.setattr(hls, "can_decrypt_frag", True)

    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_rejects_aes128_without_decryption_support(monkeypatch):
    monkeypatch.setattr(hls, "can_decrypt_frag", False)
    manifest = "#EXTM3U\n#EXT-X-KEY:METHOD=AES-128,URI=\"key.bin\"\nsegment.ts"

    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_rejects_aes128_with_byte_ranges(monkeypatch):
    monkeypatch.setattr(hls, "can_decrypt_frag", True)
    manifest = (
        "#EXTM3U\n"
        "#EXT-X-KEY:METHOD=AES-128,URI=\"key.bin\"\n"
        "#EXT-X-BYTERANGE:1024@0\n"
        "segment.ts"
    )

    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_rejects_live_stream(monkeypatch):
    monkeypatch.setattr(hls, "can_decrypt_frag", True)
    manifest = "#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:1\nsegment.ts"

    assert HlsFD.can_download(manifest, {"is_live": True}) is False
