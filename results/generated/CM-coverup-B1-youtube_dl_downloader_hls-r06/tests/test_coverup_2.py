# file: project/youtube_dl/downloader/hls.py:30-58
# asked: {"lines": [32, 53, 54, 55, 56, 57, 58], "branches": []}
# gained: {"lines": [32, 53, 54, 55, 56, 57, 58], "branches": []}

import youtube_dl.downloader.hls as hls_module
from youtube_dl.downloader.hls import HlsFD


SIMPLE_MANIFEST = (
    "#EXTM3U\n"
    "#EXT-X-VERSION:3\n"
    "#EXT-X-TARGETDURATION:10\n"
    "#EXTINF:10.0,\n"
    "segment0.ts\n"
    "#EXTINF:10.0,\n"
    "segment1.ts\n"
    "#EXT-X-ENDLIST\n"
)


def test_can_download_plain_vod_allowed():
    assert HlsFD.can_download(SIMPLE_MANIFEST, {}) is True
    assert HlsFD.can_download(SIMPLE_MANIFEST, {"is_live": False}) is True
    assert HlsFD.can_download(SIMPLE_MANIFEST, {"is_live": None}) is True


def test_can_download_none_key_allowed(monkeypatch):
    monkeypatch.setattr(hls_module, "can_decrypt_frag", True)
    manifest = SIMPLE_MANIFEST + "#EXT-X-KEY:METHOD=NONE\n"
    assert HlsFD.can_download(manifest, {}) is True


def test_can_download_unsupported_key_method_rejected():
    manifest = (
        "#EXTM3U\n"
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="skd://key"\n'
        "#EXTINF:10.0,\n"
        "segment0.ts\n"
    )
    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_unsupported_map_rejected():
    manifest = (
        "#EXTM3U\n"
        '#EXT-X-MAP:URI="init.mp4"\n'
        "#EXTINF:10.0,\n"
        "segment0.ts\n"
    )
    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_aes128_allowed_when_can_decrypt(monkeypatch):
    monkeypatch.setattr(hls_module, "can_decrypt_frag", True)
    manifest = (
        "#EXTM3U\n"
        '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/key.key"\n'
        "#EXTINF:10.0,\n"
        "segment0.ts\n"
    )
    assert HlsFD.can_download(manifest, {}) is True


def test_can_download_aes128_rejected_when_cannot_decrypt(monkeypatch):
    monkeypatch.setattr(hls_module, "can_decrypt_frag", False)
    manifest = (
        "#EXTM3U\n"
        '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/key.key"\n'
        "#EXTINF:10.0,\n"
        "segment0.ts\n"
    )
    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_no_aes_allowed_when_cannot_decrypt(monkeypatch):
    monkeypatch.setattr(hls_module, "can_decrypt_frag", False)
    assert HlsFD.can_download(SIMPLE_MANIFEST, {}) is True


def test_can_download_aes128_byterange_rejected(monkeypatch):
    monkeypatch.setattr(hls_module, "can_decrypt_frag", True)
    manifest = (
        "#EXTM3U\n"
        '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/key.key"\n'
        "#EXT-X-BYTERANGE:1000@0\n"
        "#EXTINF:10.0,\n"
        "segment0.ts\n"
    )
    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_byterange_without_aes_allowed(monkeypatch):
    monkeypatch.setattr(hls_module, "can_decrypt_frag", True)
    manifest = SIMPLE_MANIFEST + "#EXT-X-BYTERANGE:1000@0\n"
    assert HlsFD.can_download(manifest, {}) is True


def test_can_download_aes128_byterange_rejected_even_without_decrypt(monkeypatch):
    monkeypatch.setattr(hls_module, "can_decrypt_frag", False)
    manifest = (
        "#EXTM3U\n"
        '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/key.key"\n'
        "#EXT-X-BYTERANGE:1000@0\n"
        "#EXTINF:10.0,\n"
        "segment0.ts\n"
    )
    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_live_rejected():
    assert HlsFD.can_download(SIMPLE_MANIFEST, {"is_live": True}) is False


def test_can_download_not_live_allowed():
    assert HlsFD.can_download(SIMPLE_MANIFEST, {"is_live": False}) is True
    assert HlsFD.can_download(SIMPLE_MANIFEST, {}) is True
