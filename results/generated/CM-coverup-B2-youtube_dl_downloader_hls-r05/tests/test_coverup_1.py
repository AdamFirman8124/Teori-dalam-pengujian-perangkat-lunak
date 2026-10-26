# file: project/youtube_dl/downloader/hls.py:30-58
# asked: {"lines": [32, 53, 54, 55, 56, 57, 58], "branches": []}
# gained: {"lines": [32, 53, 54, 55, 56, 57, 58], "branches": []}

import pytest

from youtube_dl.downloader import hls
from youtube_dl.downloader.hls import HlsFD


PLAIN_MANIFEST = (
    '#EXTM3U\n'
    '#EXT-X-VERSION:3\n'
    '#EXT-X-TARGETDURATION:10\n'
    '#EXTINF:10,\n'
    'segment0.ts\n'
    '#EXT-X-ENDLIST\n'
)


def test_can_download_plain_manifest():
    assert HlsFD.can_download(PLAIN_MANIFEST, {}) is True


def test_can_download_plain_manifest_not_live():
    assert HlsFD.can_download(PLAIN_MANIFEST, {'is_live': False}) is True


def test_can_download_rejects_live_stream():
    assert HlsFD.can_download(PLAIN_MANIFEST, {'is_live': True}) is False


def test_can_download_rejects_ext_x_map():
    manifest = PLAIN_MANIFEST + '#EXT-X-MAP:URI="init.mp4"\n'
    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_rejects_unsupported_key_method():
    manifest = PLAIN_MANIFEST + '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_accepts_key_method_none():
    manifest = PLAIN_MANIFEST + '#EXT-X-KEY:METHOD=NONE\n'
    assert HlsFD.can_download(manifest, {}) is True


def test_can_download_accepts_aes128_when_decryption_available(monkeypatch):
    monkeypatch.setattr(hls, 'can_decrypt_frag', True)
    manifest = PLAIN_MANIFEST + '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
    assert HlsFD.can_download(manifest, {}) is True


def test_can_download_rejects_aes128_when_decryption_unavailable(monkeypatch):
    monkeypatch.setattr(hls, 'can_decrypt_frag', False)
    manifest = PLAIN_MANIFEST + '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_rejects_aes128_with_byterange(monkeypatch):
    monkeypatch.setattr(hls, 'can_decrypt_frag', True)
    manifest = (
        PLAIN_MANIFEST
        + '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        + '#EXT-X-BYTERANGE:1000@0\n'
    )
    assert HlsFD.can_download(manifest, {}) is False


def test_can_download_accepts_byterange_without_aes128(monkeypatch):
    monkeypatch.setattr(hls, 'can_decrypt_frag', False)
    manifest = PLAIN_MANIFEST + '#EXT-X-BYTERANGE:1000@0\n'
    assert HlsFD.can_download(manifest, {}) is True


def test_can_download_does_not_mutate_manifest_or_info_dict():
    manifest = PLAIN_MANIFEST + '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
    info_dict = {'is_live': False}
    manifest_before = manifest
    info_before = dict(info_dict)

    HlsFD.can_download(manifest, info_dict)

    assert manifest == manifest_before
    assert info_dict == info_before


def test_can_decrypt_frag_global_restored_after_monkeypatch(monkeypatch):
    original = hls.can_decrypt_frag
    monkeypatch.setattr(hls, 'can_decrypt_frag', False)
    assert hls.can_decrypt_frag is False
    monkeypatch.undo()
    assert hls.can_decrypt_frag is original
