# file: project/ansible/module_utils/facts/system/date_time.py:27-68
# asked: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}
# gained: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}

import builtins
import datetime as real_datetime
import time as real_time
import types

import ansible.module_utils.facts.system.date_time as dt_module
from ansible.module_utils.facts.system.date_time import DateTimeFactCollector


def test_collect_normal(monkeypatch):
    fixed = 1700000000.0
    monkeypatch.setattr(dt_module.time, "time", lambda: fixed)
    collector = DateTimeFactCollector()
    result = collector.collect(module=None, collected_facts=None)
    assert "date_time" in result
    dt = result["date_time"]
    expected_now = real_datetime.datetime.fromtimestamp(fixed)
    expected_utc = real_datetime.datetime.utcfromtimestamp(fixed)
    assert dt["year"] == expected_now.strftime("%Y")
    assert dt["month"] == expected_now.strftime("%m")
    assert dt["weekday"] == expected_now.strftime("%A")
    assert dt["weekday_number"] == expected_now.strftime("%w")
    assert dt["weeknumber"] == expected_now.strftime("%W")
    assert dt["day"] == expected_now.strftime("%d")
    assert dt["hour"] == expected_now.strftime("%H")
    assert dt["minute"] == expected_now.strftime("%M")
    assert dt["second"] == expected_now.strftime("%S")
    assert dt["epoch"] == expected_now.strftime("%s")
    assert dt["epoch"] != ""
    assert dt["epoch"][0] != "%"
    assert dt["epoch_int"] == str(int(expected_now.strftime("%s")))
    assert dt["date"] == expected_now.strftime("%Y-%m-%d")
    assert dt["time"] == expected_now.strftime("%H:%M:%S")
    assert dt["iso8601_micro"] == expected_utc.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert dt["iso8601"] == expected_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert dt["iso8601_basic"] == expected_now.strftime("%Y%m%dT%H%M%S%f")
    assert dt["iso8601_basic_short"] == expected_now.strftime("%Y%m%dT%H%M%S")
    assert dt["tz"] == real_time.strftime("%Z")
    assert dt["tz_dst"] == real_time.tzname[1]
    assert dt["tz_offset"] == real_time.strftime("%z")


def _make_fakedatetime_first_s_returns(fake_value):
    class _FakeNow:
        def __init__(self, real):
            self._real = real
            self._count = 0

        def strftime(self, fmt):
            if fmt == "%s":
                self._count += 1
                if self._count == 1:
                    return fake_value
                return self._real.strftime(fmt)
            return self._real.strftime(fmt)

    class _FakeDateTime:
        @classmethod
        def fromtimestamp(cls, ts, tz=None):
            real = real_datetime.datetime.fromtimestamp(ts)
            return _FakeNow(real)

        @classmethod
        def utcfromtimestamp(cls, ts):
            real = real_datetime.datetime.utcfromtimestamp(ts)
            return _FakeNow(real)

    return types.SimpleNamespace(datetime=_FakeDateTime)


def test_collect_epoch_empty_fallback(monkeypatch):
    fixed = 1234567890.0
    monkeypatch.setattr(dt_module.time, "time", lambda: fixed)
    monkeypatch.setattr(dt_module, "datetime", _make_fakedatetime_first_s_returns(""))
    collector = DateTimeFactCollector()
    result = collector.collect()
    assert "date_time" in result
    dt = result["date_time"]
    expected_now = real_datetime.datetime.fromtimestamp(fixed)
    expected_utc = real_datetime.datetime.utcfromtimestamp(fixed)
    assert dt["epoch"] == str(int(fixed))
    assert dt["epoch_int"] == str(int(expected_now.strftime("%s")))
    assert dt["year"] == expected_now.strftime("%Y")
    assert dt["date"] == expected_now.strftime("%Y-%m-%d")
    assert dt["time"] == expected_now.strftime("%H:%M:%S")
    assert dt["iso8601"] == expected_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert dt["iso8601_micro"] == expected_utc.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert dt["tz"] == real_time.strftime("%Z")
    assert dt["tz_dst"] == real_time.tzname[1]
    assert dt["tz_offset"] == real_time.strftime("%z")


def test_collect_epoch_percent_fallback(monkeypatch):
    fixed = 1700000000.123
    monkeypatch.setattr(dt_module.time, "time", lambda: fixed)
    monkeypatch.setattr(dt_module, "datetime", _make_fakedatetime_first_s_returns("%s"))
    collector = DateTimeFactCollector()
    result = collector.collect(module=None, collected_facts=None)
    assert "date_time" in result
    dt = result["date_time"]
    expected_now = real_datetime.datetime.fromtimestamp(fixed)
    expected_utc = real_datetime.datetime.utcfromtimestamp(fixed)
    assert dt["epoch"] == str(int(fixed))
    assert dt["epoch_int"] == str(int(expected_now.strftime("%s")))
    assert dt["year"] == expected_now.strftime("%Y")
    assert dt["weekday"] == expected_now.strftime("%A")
    assert dt["date"] == expected_now.strftime("%Y-%m-%d")
    assert dt["iso8601"] == expected_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert dt["tz"] == real_time.strftime("%Z")
    assert dt["tz_dst"] == real_time.tzname[1]


def test_collect_epoch_int_empty_fallback(monkeypatch):
    fixed = 1234567890.5
    monkeypatch.setattr(dt_module.time, "time", lambda: fixed)
    real_str = builtins.str
    real_int = builtins.int
    state = {"n": 0}

    def fake_str(o=None, *a, **k):
        state["n"] += 1
        if state["n"] == 1:
            return ""
        if o is None and not a and not k:
            return real_str()
        if a or k:
            return real_str(o, *a, **k) if o is not None else real_str(*a, **k)
        return real_str(o)

    def fake_int(o=None, *a, **k):
        if o is None and not a and not k:
            return real_int()
        return real_int(o, *a, **k)

    monkeypatch.setattr(dt_module, "str", fake_str, raising=False)
    monkeypatch.setattr(dt_module, "int", fake_int, raising=False)
    collector = DateTimeFactCollector()
    result = collector.collect()
    assert "date_time" in result
    dt = result["date_time"]
    expected_now = real_datetime.datetime.fromtimestamp(fixed)
    assert dt["epoch"] == expected_now.strftime("%s")
    assert dt["epoch_int"] == real_str(real_int(fixed))
    assert dt["epoch_int"] == real_str(real_int(float(fixed)))
    assert dt["date"] == expected_now.strftime("%Y-%m-%d")


def test_collect_epoch_int_percent_fallback(monkeypatch):
    fixed = 1700000000.789
    monkeypatch.setattr(dt_module.time, "time", lambda: fixed)
    real_str = builtins.str
    real_int = builtins.int
    state = {"n": 0}

    def fake_str(o=None, *a, **k):
        state["n"] += 1
        if state["n"] == 1:
            return "%s"
        if o is None and not a and not k:
            return real_str()
        if a or k:
            return real_str(o, *a, **k) if o is not None else real_str(*a, **k)
        return real_str(o)

    def fake_int(o=None, *a, **k):
        if o is None and not a and not k:
            return real_int()
        return real_int(o, *a, **k)

    monkeypatch.setattr(dt_module, "str", fake_str, raising=False)
    monkeypatch.setattr(dt_module, "int", fake_int, raising=False)
    collector = DateTimeFactCollector()
    result = collector.collect(module=None, collected_facts=None)
    assert "date_time" in result
    dt = result["date_time"]
    expected_now = real_datetime.datetime.fromtimestamp(fixed)
    expected_utc = real_datetime.datetime.utcfromtimestamp(fixed)
    assert dt["epoch"] == expected_now.strftime("%s")
    assert dt["epoch_int"] == real_str(real_int(fixed))
    assert dt["iso8601"] == expected_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert dt["iso8601_micro"] == expected_utc.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
