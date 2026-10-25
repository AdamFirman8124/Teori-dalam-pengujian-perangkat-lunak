

# Generated at 2026-10-25 01:57:38.900840
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():
    collector = DateTimeFactCollector()
    assert collector.name == 'date_time'
    assert collector._fact_ids == set()

    before = int(time.time())
    facts_dict = collector.collect()
    after = int(time.time())

    assert list(facts_dict) == ['date_time']
    dt = facts_dict['date_time']

    # every key present, nothing extra, all values are str
    assert set(dt) == EXPECTED_KEYS
    for key, value in dt.items():
        assert isinstance(value, str), '%s is %r, not str' % (key, type(value))

    # epoch/epoch_int are integers within the window the collect() call spanned
    assert dt['epoch'].lstrip('-').isdigit()
    assert dt['epoch_int'].lstrip('-').isdigit()
    epoch = int(dt['epoch_int'])
    assert before - 1 <= epoch <= after + 1
    assert int(dt['epoch']) == epoch

    # local-time fields are derived from that same epoch (no second-boundary flake)
    local = datetime.datetime.fromtimestamp(epoch)
    assert dt['year'] == local.strftime('%Y')
    assert dt['month'] == local.strftime('%m')
    assert dt['day'] == local.strftime('%d')

# Generated at 2026-10-25 01:57:41.316575
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-25 01:57:43.947851
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-25 01:57:46.363222
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-25 01:58:02.645171
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch


# Generated at 2026-10-25 01:58:41.353105
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():real_datetime_module = datetime

# Generated at 2026-10-25 01:58:43.773171
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 01:58:46.188307
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 01:58:48.756030
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-25 01:58:51.172018
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-25 01:58:53.585756
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-25 01:59:24.853224
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 01:59:47.710933
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():import importlib

# Generated at 2026-10-25 02:00:12.382105
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():import sys

# Generated at 2026-10-25 02:00:29.169817
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest import mock


# Generated at 2026-10-25 02:00:54.370294
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch


# Generated at 2026-10-25 02:02:19.162954
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():import sys

# Generated at 2026-10-25 02:02:43.108759
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch


# Generated at 2026-10-25 02:02:45.526037
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:02:48.092804
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:02:50.507876
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:02:52.922011
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:02:55.337346
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:02:57.763368
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:03:00.179056
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:03:02.594113
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:03:31.363843
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():import datetime as real_datetime

# Generated at 2026-10-25 02:03:55.825564
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch


# Generated at 2026-10-25 02:03:58.415547
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:04:00.830332
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:04:03.246258
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:04:05.660261
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:04:25.337155
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():import importlib

# Generated at 2026-10-25 02:04:53.591933
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:04:56.008903
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:04:58.423593
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:05:01.055742
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:05:03.470779
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:05:05.885202
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:05:08.299891
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:05:22.354222
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():import sys

# Generated at 2026-10-25 02:05:49.082558
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch


# Generated at 2026-10-25 02:06:17.080217
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 02:06:35.669459
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from types import SimpleNamespace

# Generated at 2026-10-25 02:06:59.335974
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from types import SimpleNamespace
