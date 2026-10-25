# file: project/ansible/module_utils/facts/system/date_time.py:27-68
# asked: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}
# gained: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}

import calendar
import datetime as real_datetime
import time as real_time

from ansible.module_utils.facts.system import date_time as dt_module
from ansible.module_utils.facts.system.date_time import DateTimeFactCollector

FIXED_TS = 1234567890.0
FIXED_DT = real_datetime.datetime(2009, 2, 13, 23, 31, 30, 123456)
FIXED_UTC = real_datetime.datetime(2009, 2, 13, 23, 31, 30, 123456)

EXPECTED_KEYS = {
    'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
    'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time',
    'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
    'tz', 'tz_dst', 'tz_offset',
}


class _FakeNow:
    """Stand-in for a datetime instance with per-format strftime overrides."""

    def __init__(self, base, overrides):
        self._base = base
        self._overrides = overrides

    def strftime(self, fmt):
        if fmt in self._overrides:
            value = self._overrides[fmt]
            return value() if callable(value) else value
        return self._base.strftime(fmt)


class _FakeDatetime:
    """Stand-in for the datetime.datetime class."""

    def __init__(self, overrides):
        self._overrides = overrides

    def fromtimestamp(self, ts):
        assert ts == FIXED_TS
        return _FakeNow(FIXED_DT, self._overrides)

    def utcfromtimestamp(self, ts):
        assert ts == FIXED_TS
        return _FakeNow(FIXED_UTC, self._overrides)


class _FakeTime:
    """Stand-in for the time module with a frozen clock."""

    tzname = ('UTC', 'UTC')

    @staticmethod
    def time():
        return FIXED_TS

    @staticmethod
    def strftime(fmt):
        return {'%Z': 'UTC', '%z': '+0000'}[fmt]


class _SentinelInt(int):
    """int subclass used to signal 'this str() call must be faked'."""


def _patch_clock(monkeypatch, overrides=None):
    overrides = overrides or {}
    monkeypatch.setattr(dt_module, 'time', _FakeTime)
    monkeypatch.setattr(
        dt_module,
        'datetime',
        type('FakeDatetimeModule', (), {'datetime': _FakeDatetime(overrides)}),
    )


def _patch_epoch_int(monkeypatch, bad_value):
    """Make ``str(int(now.strftime('%s')))`` yield ``bad_value``.

    Line 54 converts the strftime result with int() before the guard on
    line 55 runs, so int('') / int('%s') would raise ValueError. Intercept
    int() in the module namespace: any str argument (only ever the
    '%s' strftime result, '' or '%s' in these tests) returns a sentinel,
    and str(sentinel) returns bad_value. int(float) for the fallback
    ``str(int(epoch_ts))`` still uses the real int/str.
    """
    real_int = int
    real_str = str
    sentinel = _SentinelInt(0)

    def fake_int(value, *args, **kwargs):
        if isinstance(value, str):
            return sentinel
        return real_int(value, *args, **kwargs)

    def fake_str(obj=''):
        if obj is sentinel:
            return bad_value
        return real_str(obj)

    monkeypatch.setitem(dt_module.__dict__, 'int', fake_int)
    monkeypatch.setitem(dt_module.__dict__, 'str', fake_str)


def test_collect_returns_all_date_time_facts():
    collector = DateTimeFactCollector()
    facts_dict = collector.collect(module=object(), collected_facts={})

    assert set(facts_dict) == {'date_time'}
    facts = facts_dict['date_time']
    assert set(facts) == EXPECTED_KEYS

    assert facts['date'] == '%s-%s-%s' % (facts['year'], facts['month'], facts['day'])
    assert facts['time'] == '%s:%s:%s' % (facts['hour'], facts['minute'], facts['second'])
    assert facts['weekday'] in calendar.day_name
    assert facts['weekday_number'] == str(
        real_datetime.date(
            int(facts['year']), int(facts['month']), int(facts['day'])
        ).strftime('%w')
    )

    assert facts['epoch_int'].isdigit()
    assert abs(int(facts['epoch_int']) - int(real_time.time())) <= 5
    assert facts['epoch'].isdigit()

    assert facts['iso8601'].endswith('Z') and len(facts['iso8601']) == 20
    assert facts['iso8601_micro'].endswith('Z') and len(facts['iso8601_micro']) == 27
    assert len(facts['iso8601_basic']) == 21
    assert len(facts['iso8601_basic_short']) == 15
    assert facts['iso8601_basic_short'] == facts['iso8601_basic'][:15]

    assert facts['tz_dst'] == real_time.tzname[1]
    assert facts['tz'] == real_time.strftime('%Z')
    assert facts['tz_offset'] == real_time.strftime('%z')

    assert collector.collect()['date_time'] is not facts


def test_collect_epoch_falls_back_when_strftime_returns_empty(monkeypatch):
    _patch_clock(monkeypatch, {'%s': ''})
    _patch_epoch_int(monkeypatch, '')

    facts = DateTimeFactCollector().collect()['date_time']

    assert facts['epoch'] == str(int(FIXED_TS))
    assert facts['epoch_int'] == str(int(FIXED_TS))
    assert facts['year'] == '2009'
    assert facts['month'] == '02'
    assert facts['day'] == '13'
    assert facts['hour'] == '23'
    assert facts['minute'] == '31'
    assert facts['second'] == '30'
    assert facts['weekday'] == 'Friday'
    assert facts['weekday_number'] == '5'
    assert facts['weeknumber'] == FIXED_DT.strftime('%W')
    assert facts['date'] == '2009-02-13'
    assert facts['time'] == '23:31:30'
    assert facts['iso8601_micro'] == '2009-02-13T23:31:30.123456Z'
    assert facts['iso8601'] == '2009-02-13T23:31:30Z'
    assert facts['iso8601_basic'] == '20090213T233130123456'
    assert facts['iso8601_basic_short'] == '20090213T233130'
    assert facts['tz'] == 'UTC'
    assert facts['tz_dst'] == 'UTC'
    assert facts['tz_offset'] == '+0000'


def test_collect_epoch_falls_back_when_strftime_returns_percent(monkeypatch):
    _patch_clock(monkeypatch, {'%s': '%s'})
    _patch_epoch_int(monkeypatch, '%s')

    facts = DateTimeFactCollector().collect()['date_time']

    assert facts['epoch'] == str(int(FIXED_TS))
    assert facts['epoch_int'] == str(int(FIXED_TS))
    assert facts['date'] == '2009-02-13'
    assert facts['time'] == '23:31:30'
    assert facts['iso8601'] == '2009-02-13T23:31:30Z'
