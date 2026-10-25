# file: project/ansible/module_utils/facts/system/date_time.py:27-68
# asked: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}
# gained: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}

from types import SimpleNamespace

import pytest

from ansible.module_utils.facts.system import date_time


def test_collect_returns_all_date_time_facts(monkeypatch):
    epoch_ts = 1700000000.75
    timestamps = []

    local_values = {
        "%Y": "2023",
        "%m": "11",
        "%A": "Tuesday",
        "%w": "2",
        "%W": "46",
        "%d": "14",
        "%H": "22",
        "%M": "13",
        "%S": "20",
        "%s": "1700000000",
        "%Y-%m-%d": "2023-11-14",
        "%H:%M:%S": "22:13:20",
        "%Y%m%dT%H%M%S%f": "20231114T221320123456",
        "%Y%m%dT%H%M%S": "20231114T221320",
    }
    utc_values = {
        "%Y-%m-%dT%H:%M:%S.%fZ": "2023-11-14T22:13:20.123456Z",
        "%Y-%m-%dT%H:%M:%SZ": "2023-11-14T22:13:20Z",
    }

    class FakeLocalDateTime:
        def strftime(self, date_format):
            return local_values[date_format]

    class FakeUtcDateTime:
        def strftime(self, date_format):
            return utc_values[date_format]

    class FakeDateTime:
        @classmethod
        def fromtimestamp(cls, timestamp):
            timestamps.append(("local", timestamp))
            return FakeLocalDateTime()

        @classmethod
        def utcfromtimestamp(cls, timestamp):
            timestamps.append(("utc", timestamp))
            return FakeUtcDateTime()

    fake_time = SimpleNamespace(
        time=lambda: epoch_ts,
        strftime=lambda date_format: {
            "%Z": "TEST_ZONE",
            "%z": "+0130",
        }[date_format],
        tzname=("TEST_STANDARD", "TEST_DAYLIGHT"),
    )

    monkeypatch.setattr(
        date_time, "datetime", SimpleNamespace(datetime=FakeDateTime)
    )
    monkeypatch.setattr(date_time, "time", fake_time)

    result = date_time.DateTimeFactCollector().collect(
        module=object(), collected_facts={"existing": "fact"}
    )

    assert timestamps == [("local", epoch_ts), ("utc", epoch_ts)]
    assert result == {
        "date_time": {
            "year": "2023",
            "month": "11",
            "weekday": "Tuesday",
            "weekday_number": "2",
            "weeknumber": "46",
            "day": "14",
            "hour": "22",
            "minute": "13",
            "second": "20",
            "epoch": "1700000000",
            "epoch_int": "1700000000",
            "date": "2023-11-14",
            "time": "22:13:20",
            "iso8601_micro": "2023-11-14T22:13:20.123456Z",
            "iso8601": "2023-11-14T22:13:20Z",
            "iso8601_basic": "20231114T221320123456",
            "iso8601_basic_short": "20231114T221320",
            "tz": "TEST_ZONE",
            "tz_dst": "TEST_DAYLIGHT",
            "tz_offset": "+0130",
        }
    }


@pytest.mark.parametrize("unsupported_epoch", ["", "%s"])
def test_collect_falls_back_when_percent_s_is_unsupported(
    monkeypatch, unsupported_epoch
):
    epoch_ts = 1700000000.75
    int_arguments = []

    local_values = {
        "%Y": "2023",
        "%m": "11",
        "%A": "Tuesday",
        "%w": "2",
        "%W": "46",
        "%d": "14",
        "%H": "22",
        "%M": "13",
        "%S": "20",
        "%s": unsupported_epoch,
        "%Y-%m-%d": "2023-11-14",
        "%H:%M:%S": "22:13:20",
        "%Y%m%dT%H%M%S%f": "20231114T221320123456",
        "%Y%m%dT%H%M%S": "20231114T221320",
    }
    utc_values = {
        "%Y-%m-%dT%H:%M:%S.%fZ": "2023-11-14T22:13:20.123456Z",
        "%Y-%m-%dT%H:%M:%SZ": "2023-11-14T22:13:20Z",
    }

    class StringValue:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

    def fake_int(value):
        int_arguments.append(value)
        if value == unsupported_epoch:
            return StringValue(unsupported_epoch)
        assert value == epoch_ts
        return StringValue("1700000000")

    class FakeLocalDateTime:
        def strftime(self, date_format):
            return local_values[date_format]

    class FakeUtcDateTime:
        def strftime(self, date_format):
            return utc_values[date_format]

    class FakeDateTime:
        @classmethod
        def fromtimestamp(cls, timestamp):
            assert timestamp == epoch_ts
            return FakeLocalDateTime()

        @classmethod
        def utcfromtimestamp(cls, timestamp):
            assert timestamp == epoch_ts
            return FakeUtcDateTime()

    fake_time = SimpleNamespace(
        time=lambda: epoch_ts,
        strftime=lambda date_format: {
            "%Z": "TEST_ZONE",
            "%z": "+0130",
        }[date_format],
        tzname=("TEST_STANDARD", "TEST_DAYLIGHT"),
    )

    monkeypatch.setattr(
        date_time, "datetime", SimpleNamespace(datetime=FakeDateTime)
    )
    monkeypatch.setattr(date_time, "time", fake_time)
    monkeypatch.setattr(date_time, "int", fake_int, raising=False)

    result = date_time.DateTimeFactCollector().collect()

    assert result["date_time"]["epoch"] == "1700000000"
    assert result["date_time"]["epoch_int"] == "1700000000"
    assert result["date_time"]["iso8601"] == "2023-11-14T22:13:20Z"
    assert result["date_time"]["tz"] == "TEST_ZONE"
    assert result["date_time"]["tz_dst"] == "TEST_DAYLIGHT"
    assert result["date_time"]["tz_offset"] == "+0130"
    assert int_arguments == [
        epoch_ts,
        unsupported_epoch,
        epoch_ts,
    ]
