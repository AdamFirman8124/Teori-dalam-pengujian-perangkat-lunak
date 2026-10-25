# file: project/youtube_dl/downloader/hls.py:30-58
# asked: {"lines": [32, 53, 54, 55, 56, 57, 58], "branches": []}
# gained: {"lines": [32, 53, 54, 55, 56, 57, 58], "branches": []}

import pytest

import youtube_dl.downloader.hls as hls


@pytest.mark.parametrize(
    "manifest",
    [
        "#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts",
        "#EXTM3U\n#EXT-X-KEY:METHOD=AES-128,URI=key.bin\nsegment.ts",
    ],
)
def test_can_download_supported_manifests(monkeypatch, manifest):
    original = hls.can_decrypt_frag

    with monkeypatch.context() as patch:
        patch.setattr(hls, "can_decrypt_frag", True)
        assert hls.HlsFD.can_download(manifest, {}) is True

    assert hls.can_decrypt_frag is original


@pytest.mark.parametrize(
    "manifest",
    [
        "#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES\nsegment.ts",
        "#EXTM3U\n#EXT-X-MAP:URI=init.mp4\nsegment.m4s",
    ],
)
def test_can_download_rejects_unsupported_features(monkeypatch, manifest):
    original = hls.can_decrypt_frag

    with monkeypatch.context() as patch:
        patch.setattr(hls, "can_decrypt_frag", True)
        assert hls.HlsFD.can_download(manifest, {}) is False

    assert hls.can_decrypt_frag is original


def test_can_download_rejects_aes128_without_decryption_support(monkeypatch):
    original = hls.can_decrypt_frag
    manifest = "#EXTM3U\n#EXT-X-KEY:METHOD=AES-128,URI=key.bin\nsegment.ts"

    with monkeypatch.context() as patch:
        patch.setattr(hls, "can_decrypt_frag", False)
        assert hls.HlsFD.can_download(manifest, {}) is False

    assert hls.can_decrypt_frag is original


def test_can_download_rejects_aes128_with_byte_ranges(monkeypatch):
    original = hls.can_decrypt_frag
    manifest = (
        "#EXTM3U\n"
        "#EXT-X-KEY:METHOD=AES-128,URI=key.bin\n"
        "#EXT-X-BYTERANGE:1024@0\n"
        "segment.ts"
    )

    with monkeypatch.context() as patch:
        patch.setattr(hls, "can_decrypt_frag", True)
        assert hls.HlsFD.can_download(manifest, {}) is False

    assert hls.can_decrypt_frag is original


def test_can_download_rejects_live_stream(monkeypatch):
    original = hls.can_decrypt_frag
    manifest = "#EXTM3U\nsegment.ts"

    with monkeypatch.context() as patch:
        patch.setattr(hls, "can_decrypt_frag", True)
        assert hls.HlsFD.can_download(manifest, {"is_live": True}) is False
        assert hls.HlsFD.can_download(manifest, {"is_live": False}) is True

    assert hls.can_decrypt_frag is original
