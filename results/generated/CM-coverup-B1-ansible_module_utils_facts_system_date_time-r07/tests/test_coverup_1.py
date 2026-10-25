# file: project/ansible/module_utils/facts/system/date_time.py:27-68
# asked: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}
# gained: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}

import datetime as real_datetime
import time as real_time

import ansible.module_utils.facts.system.date_time as dt_module
from ansible.module_utils.facts.system.date_time import DateTimeFactCollector


def _install_fixed_time(monkeypatch, fixed_ts):
    fake_time = type("FakeTime", (), {})()
    fake_time.tzname = real_time.tzname
    fake_time.time = lambda: fixed_ts
    fake_time.strftime = real_time.strftime
    monkeypatch.setattr(dt_module, "time", fake_time)


def _install_fake_datetime(monkeypatch, s_values):
    real_dt = real_datetime.datetime
    state = {"idx": 0}

    class _FakeNow:
        def __init__(self, real):
            self._real = real

        def strftime(self, fmt):
            if fmt == "%s":
                if state["idx"] < len(s_values):
                    v = s_values[state["idx"]]
                    state["idx"] += 1
                    return v
            return self._real.strftime(fmt)

    class _FakeDateTime:
        @classmethod
        def fromtimestamp(cls, ts, tz=None):
            if tz is None:
                real = real_dt.fromtimestamp(ts)
            else:
                real = real_dt.fromtimestamp(ts, tz)
            return _FakeNow(real)

        @classmethod
        def utcfromtimestamp(cls, ts):
            return real_dt.utcfromtimestamp(ts)

    class _FakeDatetimeModule:
        datetime = _FakeDateTime

    monkeypatch.setattr(dt_module, "datetime", _FakeDatetimeModule())


def _install_fake_module_str(monkeypatch, first_value):
    real_str = str
    calls = {"n": 0}

    def fake_str(*args, **kwargs):
        calls["n"] += 1
        if calls["n"] == 1:
            return first_value
        return real_str(*args, **kwargs)

    monkeypatch.setattr(dt_module, "str", fake_str, raising=False)


def test_collect_normal_path(monkeypatch):
    fixed_ts = 1234567890.0
    normal = str(int(fixed_ts))
    _install_fixed_time(monkeypatch, fixed_ts)
    _install_fake_datetime(monkeypatch, [normal, normal])
    c = DateTimeFactCollector()
    result = c.collect()
    assert "date_time" in result
    d = result["date_time"]
    real_now = real_datetime.datetime.fromtimestamp(fixed_ts)
    real_utc = real_datetime.datetime.utcfromtimestamp(fixed_ts)
    assert d["epoch"] == normal
    assert d["epoch_int"] == normal
    assert d["year"] == real_now.strftime("%Y")
    assert d["month"] == real_now.strftime("%m")
    assert d["weekday"] == real_now.strftime("%A")
    assert d["weekday_number"] == real_now.strftime("%w")
    assert d["weeknumber"] == real_now.strftime("%W")
    assert d["day"] == real_now.strftime("%d")
    assert d["hour"] == real_now.strftime("%H")
    assert d["minute"] == real_now.strftime("%M")
    assert d["second"] == real_now.strftime("%S")
    assert d["date"] == real_now.strftime("%Y-%m-%d")
    assert d["time"] == real_now.strftime("%H:%M:%S")
    assert d["iso8601_micro"] == real_utc.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert d["iso8601"] == real_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert d["iso8601_basic"] == real_now.strftime("%Y%m%dT%H%M%S%f")
    assert d["iso8601_basic_short"] == real_now.strftime("%Y%m%dT%H%M%S")
    assert d["tz"] == real_time.strftime("%Z")
    assert d["tz_dst"] == real_time.tzname[1]
    assert d["tz_offset"] == real_time.strftime("%z")


def test_collect_epoch_empty_fallback(monkeypatch):
    fixed_ts = 1234567890.0
    normal = str(int(fixed_ts))
    _install_fixed_time(monkeypatch, fixed_ts)
    _install_fake_datetime(monkeypatch, ["", normal])
    c = DateTimeFactCollector()
    result = c.collect()
    d = result["date_time"]
    assert d["epoch"] == normal
    assert d["epoch"] != ""
    assert d["epoch_int"] == normal
    real_now = real_datetime.datetime.fromtimestamp(fixed_ts)
    assert d["year"] == real_now.strftime("%Y")
    assert d["date"] == real_now.strftime("%Y-%m-%d")


def test_collect_epoch_percent_fallback(monkeypatch):
    fixed_ts = 1234567890.0
    normal = str(int(fixed_ts))
    _install_fixed_time(monkeypatch, fixed_ts)
    _install_fake_datetime(monkeypatch, ["%s", normal])
    c = DateTimeFactCollector()
    result = c.collect()
    d = result["date_time"]
    assert d["epoch"] == normal
    assert d["epoch"][0] != "%"
    assert d["epoch_int"] == normal
    real_now = real_datetime.datetime.fromtimestamp(fixed_ts)
    real_utc = real_datetime.datetime.utcfromtimestamp(fixed_ts)
    assert d["month"] == real_now.strftime("%m")
    assert d["iso8601_micro"] == real_utc.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def test_collect_epoch_int_empty_fallback(monkeypatch):
    fixed_ts = 1234567890.0
    normal = str(int(fixed_ts))
    _install_fixed_time(monkeypatch, fixed_ts)
    _install_fake_datetime(monkeypatch, [normal, normal])
    _install_fake_module_str(monkeypatch, "")
    c = DateTimeFactCollector()
    result = c.collect()
    d = result["date_time"]
    assert d["epoch"] == normal
    assert d["epoch_int"] == normal
    assert d["epoch_int"] != ""
    real_now = real_datetime.datetime.fromtimestamp(fixed_ts)
    assert d["day"] == real_now.strftime("%d")
    assert d["iso8601_basic"] == real_now.strftime("%Y%m%dT%H%M%S%f")


def test_collect_epoch_int_percent_fallback(monkeypatch):
    fixed_ts = 1234567890.0
    normal = str(int(fixed_ts))
    _install_fixed_time(monkeypatch, fixed_ts)
    _install_fake_datetime(monkeypatch, [normal, normal])
    _install_fake_module_str(monkeypatch, "%s")
    c = DateTimeFactCollector()
    result = c.collect()
    d = result["date_time"]
    assert d["epoch"] == normal
    assert d["epoch_int"] == normal
    assert d["epoch_int"][0] != "%"
    real_now = real_datetime.datetime.fromtimestamp(fixed_ts)
    assert d["hour"] == real_now.strftime("%H")
    assert d["iso8601_basic_short"] == real_now.strftime("%Y%m%dT%H%M%S")
    assert d["tz"] == real_time.strftime("%Z")
    assert d["tz_dst"] == real_time.tzname[1]
    assert d["tz_offset"] == real_time.strftime("%z")
