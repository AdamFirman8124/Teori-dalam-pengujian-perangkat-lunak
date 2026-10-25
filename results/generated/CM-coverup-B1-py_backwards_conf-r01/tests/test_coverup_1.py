# file: project/py_backwards/conf.py:12-14
# asked: {"lines": [13, 14], "branches": [[13, 0], [13, 14]]}
# gained: {"lines": [13, 14], "branches": [[13, 0], [13, 14]]}

from argparse import Namespace

from py_backwards.conf import init_settings, settings


def test_init_settings_debug_true(monkeypatch):
    monkeypatch.setattr(settings, "debug", False)
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True


def test_init_settings_debug_false(monkeypatch):
    monkeypatch.setattr(settings, "debug", False)
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False
