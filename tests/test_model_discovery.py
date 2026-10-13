"""Model discovery/probe must be robust and never crash the experiment."""
from __future__ import annotations

import json
import sys
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import model_discovery as md  # noqa: E402


def test_render_markdown_lists_available_and_unavailable():
    rep = md.DiscoveryReport(
        timestamp_utc="2026-10-13T02:00:00Z",
        base_url="https://router.octalabs.id/v1",
        models_endpoint="https://router.octalabs.id/v1/models",
        listed_models=["a", "b"],
        available_models=["a"],
        unavailable_models=["b"],
        probes=[
            {"name": "a", "status": "OK", "detail": "responded"},
            {"name": "b", "status": "UNAVAILABLE", "detail": "HTTP 400: bad"},
        ],
        list_ok=True,
    )
    md_text = md.render_markdown(rep)
    assert "Available now:** 1" in md_text
    assert "`a`" in md_text
    assert "HTTP 400: bad" in md_text


def test_write_report_creates_file(tmp_path):
    rep = md.DiscoveryReport(timestamp_utc="t", available_models=["x"])
    out = tmp_path / "nested" / "models.json"
    md.write_report(rep, out)
    data = json.loads(out.read_text())
    assert data["available_models"] == ["x"]
    assert data["timestamp_utc"] == "t"


def test_discover_without_key_is_safe():
    rep = md.discover_and_probe("https://x/v1", "", probe=True)
    assert rep.list_ok is False
    assert "no API key" in rep.list_error
    assert rep.available_models == []


def test_list_models_handles_connection_error(monkeypatch):
    def boom(*a, **k):
        raise urllib.error.URLError("no route")

    monkeypatch.setattr(md.urllib.request, "urlopen", boom)
    ids, err = md.list_models("https://x/v1", "k")
    assert ids == []
    assert "URLError" in err


def test_probe_model_reports_http_error(monkeypatch):
    class FakeHTTPError(urllib.error.HTTPError):
        def read(self_inner):
            return b'{"error":"unavailable"}'

    def boom(req, timeout=None):
        raise FakeHTTPError("u", 400, "bad", {}, None)

    monkeypatch.setattr(md.urllib.request, "urlopen", boom)
    p = md.probe_model("https://x/v1", "k", "m")
    assert p.available is False
    assert p.http_status == 400
    assert "unavailable" in p.detail


def test_probe_model_ok(monkeypatch):
    class FakeResp:
        status = 200
        def read(self_inner):
            return b'{"ok":true}'
        def __enter__(self_inner):
            return self_inner
        def __exit__(self_inner, *a):
            return False

    monkeypatch.setattr(md.urllib.request, "urlopen", lambda req, timeout=None: FakeResp())
    p = md.probe_model("https://x/v1", "k", "m")
    assert p.available is True
    assert p.status == "OK"
