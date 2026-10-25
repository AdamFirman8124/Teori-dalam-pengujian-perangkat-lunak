# file: project/ansible/module_utils/facts/system/date_time.py:27-68
# asked: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}
# gained: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}

import builtins
import types

import pytest

from ansible.module_utils.facts.system import date_time


EPOCH_TS = 1704164645.75

LOCAL_FORMATS = {
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

UTC_FORMATS = {
    "%Y-%m-%dT%H:%M:%S.%fZ": "2024-01-02T08:04:05.654321Z",
    "%Y-%m-%dT%H:%M:%SZ": "2024-01-02T08:04:05Z",
}


def _install_fake_clock(monkeypatch, epoch_formats):
    epoch_formats = iter(epoch_formats)

    class FakeLocalDateTime:
        def strftime(self, format_string):
            if format_string == "%s":
                return next(epoch_formats)
            return LOCAL_FORMATS[format_string]

    class FakeUTCDateTime:
        def strftime(self, format_string):
            return UTC_FORMATS[format_string]

    class FakeDateTime:
        @staticmethod
        def fromtimestamp(timestamp):
            assert timestamp == EPOCH_TS
            return FakeLocalDateTime()

        @staticmethod
        def utcfromtimestamp(timestamp):
            assert timestamp == EPOCH_TS
            return FakeUTCDateTime()

    fake_datetime_module = types.SimpleNamespace(datetime=FakeDateTime)
    fake_time_module = types.SimpleNamespace(
        time=lambda: EPOCH_TS,
        strftime=lambda format_string: {
            "%Z": "TEST",
            "%z": "+0530",
        }[format_string],
        tzname=("TEST_STANDARD", "TEST_DAYLIGHT"),
    )

    monkeypatch.setattr(date_time, "datetime", fake_datetime_module)
    monkeypatch.setattr(date_time, "time", fake_time_module)


def _expected_facts(epoch, epoch_int):
    return {
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
            "epoch": epoch,
            "epoch_int": epoch_int,
            "date": "2024-01-02",
            "time": "03:04:05",
            "iso8601_micro": "2024-01-02T08:04:05.654321Z",
            "iso8601": "2024-01-02T08:04:05Z",
            "iso8601_basic": "20240102T030405123456",
            "iso8601_basic_short": "20240102T030405",
            "tz": "TEST",
            "tz_dst": "TEST_DAYLIGHT",
            "tz_offset": "+0530",
        }
    }


def test_collect_returns_all_date_time_facts(monkeypatch):
    _install_fake_clock(monkeypatch, ["1704164645", "1704164645"])
    collected_facts = {"existing": "unchanged"}

    result = date_time.DateTimeFactCollector().collect(
        module=object(),
        collected_facts=collected_facts,
    )

    assert result == _expected_facts("1704164645", "1704164645")
    assert collected_facts == {"existing": "unchanged"}


@pytest.mark.parametrize("unsupported_epoch", ["", "%s"])
def test_collect_falls_back_when_epoch_format_is_unsupported(
    monkeypatch, unsupported_epoch
):
    _install_fake_clock(monkeypatch, [unsupported_epoch, "222"])

    result = date_time.DateTimeFactCollector().collect()

    assert result == _expected_facts(str(int(EPOCH_TS)), "222")


@pytest.mark.parametrize("unsupported_epoch_int", ["", "%s"])
def test_collect_falls_back_when_epoch_int_format_is_unsupported(
    monkeypatch, unsupported_epoch_int
):
    _install_fake_clock(monkeypatch, ["111", "222"])

    def fake_str(value):
        if value == 222:
            return unsupported_epoch_int
        return builtins.str(value)

    monkeypatch.setattr(date_time, "str", fake_str, raising=False)

    result = date_time.DateTimeFactCollector().collect()

    assert result == _expected_facts("111", builtins.str(int(EPOCH_TS)))
