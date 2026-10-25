# file: project/ansible/module_utils/facts/system/date_time.py:27-68
# asked: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}
# gained: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}

import datetime as real_datetime
import time as real_time

from ansible.module_utils.facts.system import date_time as dt_module
from ansible.module_utils.facts.system.date_time import DateTimeFactCollector

FIXED_TS = 1234567890.0
FIXED_DT = real_datetime.datetime(2009, 2, 13, 23, 31, 30, 123456)
FIXED_UTC = real_datetime.datetime(2009, 2, 13, 23, 31, 30, 123456)
FIXED_EPOCH_STR = str(int(FIXED_TS))

EXPECTED_KEYS = {
    'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
    'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time',
    'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
    'tz', 'tz_dst', 'tz_offset',
}


class _FakeNow:
    def __init__(self, base, s_effects, counter):
        self._base = base
        self._s_effects = s_effects
        self._counter = counter

    def strftime(self, fmt):
        if fmt == '%s':
            idx = self._counter['i']
            if idx < len(self._s_effects):
                self._counter['i'] += 1
                value = self._s_effects[idx]
                return value() if callable(value) else value
            return FIXED_EPOCH_STR
        return self._base.strftime(fmt)


class _FakeDatetime:
    def __init__(self, s_effects, counter):
        self._s_effects = s_effects
        self._counter = counter

    def fromtimestamp(self, ts):
        assert ts == FIXED_TS
        return _FakeNow(FIXED_DT, self._s_effects, self._counter)

    def utcfromtimestamp(self, ts):
        assert ts == FIXED_TS
        return _FakeNow(FIXED_UTC, self._s_effects, self._counter)


class _FakeTime:
    tzname = ('UTC', 'UTC')

    @staticmethod
    def time():
        return FIXED_TS

    @staticmethod
    def strftime(fmt):
        return {'%Z': 'UTC', '%z': '+0000'}[fmt]


def _patch_fixed_clock(monkeypatch, s_effects):
    counter = {'i': 0}
    monkeypatch.setattr(dt_module, 'time', _FakeTime)
    fake_datetime_cls = _FakeDatetime(s_effects, counter)
    fake_datetime_mod = type(
        'FakeDatetimeModule', (), {'datetime': fake_datetime_cls}
    )
    monkeypatch.setattr(dt_module, 'datetime', fake_datetime_mod)


def test_collect_normal_fixed_clock(monkeypatch):
    _patch_fixed_clock(monkeypatch, [FIXED_EPOCH_STR, FIXED_EPOCH_STR])

    facts = DateTimeFactCollector().collect()['date_time']

    assert set(facts) == EXPECTED_KEYS
    assert facts['year'] == '2009'
    assert facts['month'] == '02'
    assert facts['day'] == '13'
    assert facts['hour'] == '23'
    assert facts['minute'] == '31'
    assert facts['second'] == '30'
    assert facts['weekday'] == 'Friday'
    assert facts['weekday_number'] == '5'
    assert facts['weeknumber'] == FIXED_DT.strftime('%W')
    assert facts['epoch'] == FIXED_EPOCH_STR
    assert facts['epoch_int'] == FIXED_EPOCH_STR
    assert facts['date'] == '2009-02-13'
    assert facts['time'] == '23:31:30'
    assert facts['iso8601_micro'] == '2009-02-13T23:31:30.123456Z'
    assert facts['iso8601'] == '2009-02-13T23:31:30Z'
    assert facts['iso8601_basic'] == '20090213T233130123456'
    assert facts['iso8601_basic_short'] == '20090213T233130'
    assert facts['tz'] == 'UTC'
    assert facts['tz_dst'] == 'UTC'
    assert facts['tz_offset'] == '+0000'


def test_collect_real_clock_covers_no_fallback_branches():
    facts = DateTimeFactCollector().collect(module=None, collected_facts={})['date_time']

    assert set(facts) == EXPECTED_KEYS
    assert facts['epoch'].isdigit()
    assert facts['epoch_int'].isdigit()
    assert facts['date'] == '%s-%s-%s' % (facts['year'], facts['month'], facts['day'])
    assert facts['tz_dst'] == real_time.tzname[1]


def test_collect_epoch_empty_fallback(monkeypatch):
    _patch_fixed_clock(monkeypatch, ['', FIXED_EPOCH_STR])

    facts = DateTimeFactCollector().collect()['date_time']

    assert facts['epoch'] == FIXED_EPOCH_STR
    assert facts['epoch_int'] == FIXED_EPOCH_STR
    assert facts['date'] == '2009-02-13'
    assert facts['time'] == '23:31:30'


def test_collect_epoch_percent_fallback(monkeypatch):
    _patch_fixed_clock(monkeypatch, ['%s', FIXED_EPOCH_STR])

    facts = DateTimeFactCollector().collect()['date_time']

    assert facts['epoch'] == FIXED_EPOCH_STR
    assert facts['epoch_int'] == FIXED_EPOCH_STR
    assert facts['year'] == '2009'
    assert facts['iso8601'] == '2009-02-13T23:31:30Z'


def test_collect_epoch_int_empty_fallback(monkeypatch):
    _patch_fixed_clock(monkeypatch, [FIXED_EPOCH_STR, FIXED_EPOCH_STR])
    orig_str = str
    calls = {'n': 0}

    def fake_str(obj=None, *args, **kwargs):
        if isinstance(obj, int) and not args and not kwargs:
            calls['n'] += 1
            if calls['n'] == 1:
                return ''
            return orig_str(obj)
        if obj is None and not args and not kwargs:
            return orig_str()
        return orig_str(obj, *args, **kwargs)

    monkeypatch.setattr(dt_module, 'str', fake_str, raising=False)

    facts = DateTimeFactCollector().collect()['date_time']

    assert calls['n'] == 2
    assert facts['epoch'] == FIXED_EPOCH_STR
    assert facts['epoch_int'] == FIXED_EPOCH_STR
    assert facts['date'] == '2009-02-13'


def test_collect_epoch_int_percent_fallback(monkeypatch):
    _patch_fixed_clock(monkeypatch, [FIXED_EPOCH_STR, FIXED_EPOCH_STR])
    orig_str = str
    calls = {'n': 0}

    def fake_str(obj=None, *args, **kwargs):
        if isinstance(obj, int) and not args and not kwargs:
            calls['n'] += 1
            if calls['n'] == 1:
                return '%s'
            return orig_str(obj)
        if obj is None and not args and not kwargs:
            return orig_str()
        return orig_str(obj, *args, **kwargs)

    monkeypatch.setattr(dt_module, 'str', fake_str, raising=False)

    facts = DateTimeFactCollector().collect()['date_time']

    assert calls['n'] == 2
    assert facts['epoch'] == FIXED_EPOCH_STR
    assert facts['epoch_int'] == FIXED_EPOCH_STR
    assert facts['iso8601_micro'] == '2009-02-13T23:31:30.123456Z'
