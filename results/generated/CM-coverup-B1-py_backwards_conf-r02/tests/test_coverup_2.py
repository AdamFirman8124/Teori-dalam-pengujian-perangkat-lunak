# file: project/py_backwards/conf.py:12-14
# asked: {"lines": [13, 14], "branches": [[13, 0], [13, 14]]}
# gained: {"lines": [13, 14], "branches": [[13, 0], [13, 14]]}

from argparse import Namespace

from py_backwards.conf import init_settings, settings


def test_init_settings_debug_true_sets_settings_debug(monkeypatch):
    monkeypatch.setattr(settings, "debug", False)

    init_settings(Namespace(debug=True))

    assert settings.debug is True


def test_init_settings_debug_false_leaves_settings_debug(monkeypatch):
    monkeypatch.setattr(settings, "debug", False)

    init_settings(Namespace(debug=False))

    assert settings.debug is False
