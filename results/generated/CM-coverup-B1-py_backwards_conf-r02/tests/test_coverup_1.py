# file: project/py_backwards/conf.py:12-14
# asked: {"lines": [13, 14], "branches": [[13, 0], [13, 14]]}
# gained: {"lines": [13, 14], "branches": [[13, 0], [13, 14]]}

from argparse import Namespace

import py_backwards.conf as conf


def test_init_settings_debug_true(monkeypatch):
    monkeypatch.setattr(conf.settings, "debug", False)
    args = Namespace(debug=True)
    conf.init_settings(args)
    assert conf.settings.debug is True


def test_init_settings_debug_false(monkeypatch):
    monkeypatch.setattr(conf.settings, "debug", True)
    args = Namespace(debug=False)
    conf.init_settings(args)
    assert conf.settings.debug is True
