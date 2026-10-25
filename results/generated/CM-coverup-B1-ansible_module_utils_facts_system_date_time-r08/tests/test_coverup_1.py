# file: project/ansible/module_utils/facts/system/date_time.py:27-68
# asked: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}
# gained: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}

import datetime as std_datetime
import time as std_time
import types

import ansible.module_utils.facts.system.date_time as dt_module
from ansible.module_utils.facts.system.date_time import DateTimeFactCollector


def test_collect_normal(monkeypatch):
    fixed = 1700000000.789
    fake_s = str(int(fixed))
    real_now = std_datetime.datetime.fromtimestamp(fixed)
    real_utcnow = std_datetime.datetime.utcfromtimestamp(fixed)

    class _FakeNow:
        def __init__(self, real):
            self._real = real

        def strftime(self, fmt):
            if fmt == "%s":
                return fake_s
            return self._real.strftime(fmt)

    class _FakeDateTime:
        @classmethod
        def fromtimestamp(cls, ts, tz=None):
            return _FakeNow(std_datetime.datetime.fromtimestamp(ts))

        @classmethod
        def utcfromtimestamp(cls, ts):
            return _FakeNow(std_datetime.datetime.utcfromtimestamp(ts))

    monkeypatch.setattr(dt_module, "datetime", types.SimpleNamespace(datetime=_FakeDateTime))
    monkeypatch.setattr(dt_module.time, "time", lambda: fixed)
    monkeypatch.setattr(dt_module.time, "tzname", ("STD", "DST"))
    orig_strftime = std_time.strftime

    def _fake_strftime(fmt, *args, **kwargs):
        if fmt == "%Z":
            return "STD"
        if fmt == "%z":
            return "+0000"
        return orig_strftime(fmt, *args, **kwargs)

    monkeypatch.setattr(dt_module.time, "strftime", _fake_strftime)

    result = DateTimeFactCollector().collect(module=None, collected_facts=None)

    assert "date_time" in result
    dt = result["date_time"]
    assert dt["year"] == real_now.strftime("%Y")
    assert dt["month"] == real_now.strftime("%m")
    assert dt["weekday"] == real_now.strftime("%A")
    assert dt["weekday_number"] == real_now.strftime("%w")
    assert dt["weeknumber"] == real_now.strftime("%W")
    assert dt["day"] == real_now.strftime("%d")
    assert dt["hour"] == real_now.strftime("%H")
    assert dt["minute"] == real_now.strftime("%M")
    assert dt["second"] == real_now.strftime("%S")
    assert dt["epoch"] == fake_s
    assert dt["epoch"] != ""
    assert dt["epoch"][0] != "%"
    assert dt["epoch_int"] == str(int(fake_s))
    assert dt["epoch_int"] != ""
    assert dt["epoch_int"][0] != "%"
    assert dt["date"] == real_now.strftime("%Y-%m-%d")
    assert dt["time"] == real_now.strftime("%H:%M:%S")
    assert dt["iso8601_micro"] == real_utcnow.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert dt["iso8601"] == real_utcnow.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert dt["iso8601_basic"] == real_now.strftime("%Y%m%dT%H%M%S%f")
    assert dt["iso8601_basic_short"] == real_now.strftime("%Y%m%dT%H%M%S")
    assert dt["tz"] == "STD"
    assert dt["tz_dst"] == "DST"
    assert dt["tz_offset"] == "+0000"


def test_collect_epoch_empty_fallback(monkeypatch):
    fixed = 1234567890.0
    expected = str(int(fixed))
    fake_s = ""
    fake_int_str = ""
    real_int = int

    class _StrWrapper:
        def __init__(self, s):
            self._s = s

        def __str__(self):
            return self._s

        def __repr__(self):
            return self._s

    def _fake_int(x, *args, **kwargs):
        if isinstance(x, str) and (x == "" or x.startswith("%")):
            return _StrWrapper(fake_int_str)
        return real_int(x, *args, **kwargs)

    class _FakeNow:
        def __init__(self, real):
            self._real = real

        def strftime(self, fmt):
            if fmt == "%s":
                return fake_s
            return self._real.strftime(fmt)

    class _FakeDateTime:
        @classmethod
        def fromtimestamp(cls, ts, tz=None):
            return _FakeNow(std_datetime.datetime.fromtimestamp(ts))

        @classmethod
        def utcfromtimestamp(cls, ts):
            return _FakeNow(std_datetime.datetime.utcfromtimestamp(ts))

    monkeypatch.setattr(dt_module, "datetime", types.SimpleNamespace(datetime=_FakeDateTime))
    monkeypatch.setattr(dt_module, "int", _fake_int, raising=False)
    monkeypatch.setattr(dt_module.time, "time", lambda: fixed)
    monkeypatch.setattr(dt_module.time, "tzname", ("STD", "DST"))
    orig_strftime = std_time.strftime

    def _fake_strftime(fmt, *args, **kwargs):
        if fmt == "%Z":
            return "STD"
        if fmt == "%z":
            return "+0000"
        return orig_strftime(fmt, *args, **kwargs)

    monkeypatch.setattr(dt_module.time, "strftime", _fake_strftime)

    result = DateTimeFactCollector().collect()
    assert "date_time" in result
    dt = result["date_time"]
    real_now = std_datetime.datetime.fromtimestamp(fixed)
    real_utcnow = std_datetime.datetime.utcfromtimestamp(fixed)
    assert dt["epoch"] == expected
    assert dt["epoch_int"] == expected
    assert dt["year"] == real_now.strftime("%Y")
    assert dt["month"] == real_now.strftime("%m")
    assert dt["weekday"] == real_now.strftime("%A")
    assert dt["day"] == real_now.strftime("%d")
    assert dt["date"] == real_now.strftime("%Y-%m-%d")
    assert dt["time"] == real_now.strftime("%H:%M:%S")
    assert dt["iso8601"] == real_utcnow.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert dt["iso8601_micro"] == real_utcnow.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert dt["tz"] == "STD"
    assert dt["tz_dst"] == "DST"
    assert dt["tz_offset"] == "+0000"


def test_collect_epoch_percent_fallback(monkeypatch):
    fixed = 1700000000.123
    expected = str(int(fixed))
    fake_s = "%s"
    fake_int_str = "%s"
    real_int = int

    class _StrWrapper:
        def __init__(self, s):
            self._s = s

        def __str__(self):
            return self._s

        def __repr__(self):
            return self._s

    def _fake_int(x, *args, **kwargs):
        if isinstance(x, str) and (x == "" or x.startswith("%")):
            return _StrWrapper(fake_int_str)
        return real_int(x, *args, **kwargs)

    class _FakeNow:
        def __init__(self, real):
            self._real = real

        def strftime(self, fmt):
            if fmt == "%s":
                return fake_s
            return self._real.strftime(fmt)

    class _FakeDateTime:
        @classmethod
        def fromtimestamp(cls, ts, tz=None):
            return _FakeNow(std_datetime.datetime.fromtimestamp(ts))

        @classmethod
        def utcfromtimestamp(cls, ts):
            return _FakeNow(std_datetime.datetime.utcfromtimestamp(ts))

    monkeypatch.setattr(dt_module, "datetime", types.SimpleNamespace(datetime=_FakeDateTime))
    monkeypatch.setattr(dt_module, "int", _fake_int, raising=False)
    monkeypatch.setattr(dt_module.time, "time", lambda: fixed)
    monkeypatch.setattr(dt_module.time, "tzname", ("STD", "DST"))
    orig_strftime = std_time.strftime

    def _fake_strftime(fmt, *args, **kwargs):
        if fmt == "%Z":
            return "STD"
        if fmt == "%z":
            return "+0000"
        return orig_strftime(fmt, *args, **kwargs)

    monkeypatch.setattr(dt_module.time, "strftime", _fake_strftime)

    result = DateTimeFactCollector().collect(module=None, collected_facts=None)
    assert "date_time" in result
    dt = result["date_time"]
    real_now = std_datetime.datetime.fromtimestamp(fixed)
    real_utcnow = std_datetime.datetime.utcfromtimestamp(fixed)
    assert dt["epoch"] == expected
    assert dt["epoch_int"] == expected
    assert dt["year"] == real_now.strftime("%Y")
    assert dt["weekday_number"] == real_now.strftime("%w")
    assert dt["weeknumber"] == real_now.strftime("%W")
    assert dt["hour"] == real_now.strftime("%H")
    assert dt["minute"] == real_now.strftime("%M")
    assert dt["second"] == real_now.strftime("%S")
    assert dt["date"] == real_now.strftime("%Y-%m-%d")
    assert dt["time"] == real_now.strftime("%H:%M:%S")
    assert dt["iso8601_micro"] == real_utcnow.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert dt["iso8601"] == real_utcnow.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert dt["iso8601_basic"] == real_now.strftime("%Y%m%dT%H%M%S%f")
    assert dt["iso8601_basic_short"] == real_now.strftime("%Y%m%dT%H%M%S")
    assert dt["tz"] == "STD"
    assert dt["tz_dst"] == "DST"
    assert dt["tz_offset"] == "+0000"
