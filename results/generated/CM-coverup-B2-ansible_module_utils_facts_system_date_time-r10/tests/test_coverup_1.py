# file: project/ansible/module_utils/facts/system/date_time.py:27-68
# asked: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}
# gained: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}

import builtins
from types import SimpleNamespace

import pytest

from ansible.module_utils.facts.system import date_time


EPOCH_TS = 1704164645.75
EPOCH_STRING = "1704164645"


def _patch_clock(monkeypatch, epoch_formats=None):
    epoch_formats = iter(epoch_formats or [EPOCH_STRING, EPOCH_STRING])

    class LocalDateTime:
        def strftime(self, fmt):
            values = {
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
                "%Y%m%dT%H%M%S%f": "20240102T030405123456",
                "%Y%m%dT%H%M%S": "20240102T030405",
            }
            if fmt == "%s":
                return next(epoch_formats)
            return values[fmt]

    class UTCDateTime:
        def strftime(self, fmt):
            return {
                "%Y-%m-%dT%H:%M:%S.%fZ": "2024-01-02T01:04:05.123456Z",
                "%Y-%m-%dT%H:%M:%SZ": "2024-01-02T01:04:05Z",
            }[fmt]

    class FakeDateTime:
        @staticmethod
        def fromtimestamp(timestamp):
            assert timestamp == EPOCH_TS
            return LocalDateTime()

        @staticmethod
        def utcfromtimestamp(timestamp):
            assert timestamp == EPOCH_TS
            return UTCDateTime()

    fake_datetime = SimpleNamespace(datetime=FakeDateTime)
    fake_time = SimpleNamespace(
        time=lambda: EPOCH_TS,
        strftime=lambda fmt: {"%Z": "TEST", "%z": "+0130"}[fmt],
        tzname=("TEST", "TEST-DST"),
    )
    monkeypatch.setattr(date_time, "datetime", fake_datetime)
    monkeypatch.setattr(date_time, "time", fake_time)


def test_collect_returns_all_date_time_facts(monkeypatch):
    _patch_clock(monkeypatch)
    collected_facts = {"existing": "unchanged"}

    result = date_time.DateTimeFactCollector().collect(
        module=object(),
        collected_facts=collected_facts,
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
            "epoch": EPOCH_STRING,
            "epoch_int": EPOCH_STRING,
            "date": "2024-01-02",
            "time": "03:04:05",
            "iso8601_micro": "2024-01-02T01:04:05.123456Z",
            "iso8601": "2024-01-02T01:04:05Z",
            "iso8601_basic": "20240102T030405123456",
            "iso8601_basic_short": "20240102T030405",
            "tz": "TEST",
            "tz_dst": "TEST-DST",
            "tz_offset": "+0130",
        }
    }
    assert collected_facts == {"existing": "unchanged"}


@pytest.mark.parametrize("unsupported_epoch", ["", "%s"])
def test_collect_falls_back_when_epoch_format_is_unsupported(
    monkeypatch, unsupported_epoch
):
    _patch_clock(monkeypatch, [unsupported_epoch, EPOCH_STRING])

    result = date_time.DateTimeFactCollector().collect()

    assert result["date_time"]["epoch"] == EPOCH_STRING
    assert result["date_time"]["epoch_int"] == EPOCH_STRING


@pytest.mark.parametrize("unsupported_epoch_int", ["", "%s"])
def test_collect_falls_back_when_epoch_int_format_is_unsupported(
    monkeypatch, unsupported_epoch_int
):
    _patch_clock(monkeypatch)
    calls = []

    class StringResult:
        def __str__(self):
            return unsupported_epoch_int

    def fake_int(value):
        calls.append(value)
        if len(calls) == 1:
            return StringResult()
        return builtins.int(value)

    monkeypatch.setattr(date_time, "int", fake_int, raising=False)

    result = date_time.DateTimeFactCollector().collect()

    assert result["date_time"]["epoch"] == EPOCH_STRING
    assert result["date_time"]["epoch_int"] == EPOCH_STRING
    assert calls == [EPOCH_STRING, EPOCH_TS]
