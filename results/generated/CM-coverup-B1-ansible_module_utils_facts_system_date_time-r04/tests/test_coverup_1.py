# file: project/ansible/module_utils/facts/system/date_time.py:27-68
# asked: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}
# gained: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}

import builtins
from types import SimpleNamespace

import pytest

from ansible.module_utils.facts.system import date_time


def _install_fixed_clock(monkeypatch, epoch_values=None):
    epoch_values = iter(epoch_values or ["1704164645", "1704164645"])

    local_values = {
        "%Y": "2024",
        "%m": "01",
        "%A": "Tuesday",
        "%w": "2",
        "%W": "01",
        "%d": "02",
        "%H": "03",
        "%M": "04",
        "%S": "05",
        "%Y-%m-%d": "2024-01-02",
        "%H:%M:%S": "03:04:05",
        "%Y%m%dT%H%M%S%f": "20240102T030405678901",
        "%Y%m%dT%H%M%S": "20240102T030405",
    }
    utc_values = {
        "%Y-%m-%dT%H:%M:%S.%fZ": "2024-01-02T03:04:05.678901Z",
        "%Y-%m-%dT%H:%M:%SZ": "2024-01-02T03:04:05Z",
    }

    class FakeDate:
        def __init__(self, values, is_local=False):
            self._values = values
            self._is_local = is_local

        def strftime(self, format_string):
            if self._is_local and format_string == "%s":
                return next(epoch_values)
            return self._values[format_string]

    class FakeDateTime:
        @classmethod
        def fromtimestamp(cls, timestamp):
            assert timestamp == 1704164645.75
            return FakeDate(local_values, is_local=True)

        @classmethod
        def utcfromtimestamp(cls, timestamp):
            assert timestamp == 1704164645.75
            return FakeDate(utc_values)

    fake_datetime = SimpleNamespace(datetime=FakeDateTime)
    fake_time = SimpleNamespace(
        time=lambda: 1704164645.75,
        strftime=lambda format_string: {
            "%Z": "UTC",
            "%z": "+0000",
        }[format_string],
        tzname=("UTC", "UTC"),
    )

    monkeypatch.setattr(date_time, "datetime", fake_datetime)
    monkeypatch.setattr(date_time, "time", fake_time)


def test_collect_returns_all_date_time_facts(monkeypatch):
    _install_fixed_clock(monkeypatch)

    result = date_time.DateTimeFactCollector().collect(
        module=object(),
        collected_facts={"existing": "value"},
    )

    assert result == {
        "date_time": {
            "year": "2024",
            "month": "01",
            "weekday": "Tuesday",
            "weekday_number": "2",
            "weeknumber": "01",
            "day": "02",
            "hour": "03",
            "minute": "04",
            "second": "05",
            "epoch": "1704164645",
            "epoch_int": "1704164645",
            "date": "2024-01-02",
            "time": "03:04:05",
            "iso8601_micro": "2024-01-02T03:04:05.678901Z",
            "iso8601": "2024-01-02T03:04:05Z",
            "iso8601_basic": "20240102T030405678901",
            "iso8601_basic_short": "20240102T030405",
            "tz": "UTC",
            "tz_dst": "UTC",
            "tz_offset": "+0000",
        }
    }


@pytest.mark.parametrize("unsupported_epoch", ["", "%s"])
def test_collect_falls_back_for_unsupported_epoch_format(
    monkeypatch, unsupported_epoch
):
    _install_fixed_clock(
        monkeypatch,
        epoch_values=[unsupported_epoch, "1704164645"],
    )

    result = date_time.DateTimeFactCollector().collect()
    facts = result["date_time"]

    assert facts["epoch"] == "1704164645"
    assert facts["epoch_int"] == "1704164645"
    assert facts["date"] == "2024-01-02"
    assert facts["iso8601"] == "2024-01-02T03:04:05Z"


@pytest.mark.parametrize("unsupported_epoch_int", ["", "%s"])
def test_collect_falls_back_for_unsupported_epoch_int_string(
    monkeypatch, unsupported_epoch_int
):
    _install_fixed_clock(monkeypatch)
    str_calls = []

    def fake_str(value):
        str_calls.append(value)
        if len(str_calls) == 1:
            return unsupported_epoch_int
        return builtins.str(value)

    monkeypatch.setattr(date_time, "str", fake_str, raising=False)

    result = date_time.DateTimeFactCollector().collect()
    facts = result["date_time"]

    assert facts["epoch"] == "1704164645"
    assert facts["epoch_int"] == "1704164645"
    assert str_calls == [1704164645, 1704164645]
    assert facts["time"] == "03:04:05"
    assert facts["tz"] == "UTC"
