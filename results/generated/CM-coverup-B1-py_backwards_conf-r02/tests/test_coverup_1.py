# file: project/py_backwards/conf.py:12-14
# asked: {"lines": [13, 14], "branches": [[13, 0], [13, 14]]}
# gained: {"lines": [13, 14], "branches": [[13, 0], [13, 14]]}

from argparse import Namespace

from py_backwards import conf


def test_init_settings_enables_debug(monkeypatch):
    monkeypatch.setattr(conf.settings, "debug", False)

    conf.init_settings(Namespace(debug=True))

    assert conf.settings.debug is True


def test_init_settings_leaves_debug_unchanged_when_disabled(monkeypatch):
    monkeypatch.setattr(conf.settings, "debug", True)

    conf.init_settings(Namespace(debug=False))

    assert conf.settings.debug is True
