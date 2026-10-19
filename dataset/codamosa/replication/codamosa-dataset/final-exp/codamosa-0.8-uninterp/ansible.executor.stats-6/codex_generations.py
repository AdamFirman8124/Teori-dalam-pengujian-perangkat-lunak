

# Generated at 2022-06-12 21:51:13.169385
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    agg_stats = AggregateStats()
    agg_stats.ok['host1'] = 1
    agg_stats.decrement('ok', 'host1')
    agg_stats.decrement('ok', 'host1')

    assert agg_stats.ok['host1'] == 0, "ok was not decremented by 2"

# Generated at 2022-06-12 21:51:17.206210
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    stats = AggregateStats()

    stats.increment('a', 'b')
    assert stats.a['b'] == 1
    assert stats.a['b'] == 1

    stats.increment('a', 'b')
    assert stats.a['b'] == 2

    stats.increment('a', 'c')
    assert stats.a['b'] == 2
    assert stats.a['c'] == 1


# Generated at 2022-06-12 21:51:25.862267
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()

    stats.processed = {
        'localhost': 1,
        'fakehost': 1
    }

    stats.failures = {
        'localhost': 1,
        'fakehost': 1
    }

    for host in stats.processed:
        for _ in range(stats.failures[host]):
            stats.decrement('failures', host)
        assert(stats.failures[host] == 0)

    stats.failures = {
        'localhost': 1,
        'fakehost': 0
    }

    for host in stats.processed:
        for _ in range(stats.failures[host]):
            stats.decrement('failures', host)
        assert(stats.failures[host] == 0)

test_AggregateStats_decrement()

# Generated at 2022-06-12 21:51:35.416241
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    host='test_host'
    what='rescued'
    ags = AggregateStats()
    # Testing negative values
    ags.processed[host] = 1
    ags.rescued[host] = 0
    ags.decrement(what, host)

    assert ags.rescued[host] == 0

    ags.rescued[host] = 0
    ags.decrement(what, host)

    assert ags.rescued[host] == 0
    ags.rescued[host] = 2
    ags.decrement(what, host)

    assert ags.rescued[host] == 1

    # Testing negative values
    ags.processed[host] = 1
    ags.ignored[host] = 0
    ags.decre

# Generated at 2022-06-12 21:51:43.638613
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('changed', 'host1')
    stats.increment('changed', 'host1')
    stats.increment('changed', 'host1')
    stats.decrement('changed', 'host1')
    assert stats.changed['host1'] == 2
    stats.decrement('changed', 'host1')
    stats.decrement('changed', 'host1')
    assert stats.changed['host1'] == 0
    stats.decrement('changed', 'host1')
    assert stats.changed['host1'] == 0
    stats.decrement('changed', 'host2')
    assert 0 not in stats.changed.values()

# Generated at 2022-06-12 21:51:50.110237
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'localhost')
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0
    assert 'localhost' not in stats.failures
    assert 'localhost' not in stats.dark
    assert 'localhost' not in stats.changed
    assert 'localhost' not in stats.skipped
    assert 'localhost' not in stats.ignored
    assert 'localhost' not in stats.rescued



# Generated at 2022-06-12 21:51:52.730795
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'localhost')
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0


# Generated at 2022-06-12 21:51:55.422631
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('failures', 'localhost')
    stats.decrement('failures', 'localhost')
    assert stats.failures.get('localhost', 0) == 0


# Generated at 2022-06-12 21:51:58.283443
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement("ok","localhost")
    stats.decrement("ok","localhost")
    assert stats.ok["localhost"] == 0
    stats.decrement("ok","localhost")
    assert stats.ok["localhost"] == 0


# Generated at 2022-06-12 21:52:01.942420
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():

    stats = AggregateStats()
    stats.increment("skipped", "host1")
    assert stats.skipped["host1"] > 0
    stats.decrement("skipped", "host1")
    assert stats.skipped["host1"] == 0


# Generated at 2022-06-12 21:52:13.268700
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    from ansible.utils.vars import combine_vars

    stats = AggregateStats()
    stats.update_custom_stats('foo', 123)
    assert stats.custom['_run']['foo'] == 123

    # test combine_vars with custom stats
    stats.update_custom_stats('dict', {'a': 1, 'b': 2}, host='example.org')
    stats.update_custom_stats('dict', {'a': 2, 'c': 3}, host='example.org')
    stats.update_custom_stats('dict', {'d': 4}, host='foo.org')
    stats.update_custom_stats('dict', {'a': 3, 'b': 2}, host='bar.org')


# Generated at 2022-06-12 21:52:16.379337
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('skipped', 'myhost')
    assert stats.skipped['myhost'] == 0
    stats.skipped['myhost'] = 4
    stats.decrement('skipped', 'myhost')
    assert stats.skipped['myhost'] == 3

# Generated at 2022-06-12 21:52:24.062934
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    a_stats = AggregateStats()
    a_stats.update_custom_stats("fizz", "buzz", "127.0.0.1")
    a_stats.update_custom_stats("fizz", "chatter", "127.0.0.1")
    a_stats.update_custom_stats("fizz", "chatter", "127.0.0.2")
    a_stats.update_custom_stats("foo", "bar", "127.0.0.1")
    a_stats.update_custom_stats("foo", "bar", "127.0.0.2")
    a_stats.update_custom_stats("foo", "bizzy", "127.0.0.2")

# Generated at 2022-06-12 21:52:32.175211
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    agg_stats = AggregateStats()
    agg_stats.update_custom_stats('a', {'aa': '11'}, 'zzz')
    assert agg_stats.custom['zzz']['a'] == {'aa': '11'}
    agg_stats.update_custom_stats('a', {'bb': '22'}, 'zzz')
    assert agg_stats.custom['zzz']['a'] == {'aa': '11', 'bb': '22'}
    agg_stats.update_custom_stats('b', 33, 'zzz')
    assert agg_stats.custom['zzz']['b'] == 33
    agg_stats.update_custom_stats('b', 44, 'zzz')
    assert agg_stats.custom['zzz']['b'] == 77

# Generated at 2022-06-12 21:52:41.246517
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    import tempfile

    # Fail early if statistics.py is out of sync with module_utils/statistics.py
    # Ideally we would move statistics.py there, but the code is still used by
    # the internal callback
    try:
        tmp_file = tempfile.NamedTemporaryFile(delete=True)
        tmp_file.write("%s/%s" % ('ansible/module_utils', __file__))
        tmp_file.flush()
        result = __salt__['cmd.run_stdout'](['sh', '-c', 'diff -q $1 ansible/module_utils/statistics.py', tmp_file.name])
        assert len(result) == 0
    finally:
        tmp_file.close()

    stats = AggregateStats()

# Generated at 2022-06-12 21:52:50.350688
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    from ansible.vars.unsafe_proxy import wrap_var

    def test_func(what, host='_run'):
        a = AggregateStats()
        a.update_custom_stats('test', what, host)
        return a.custom

    assert test_func(None) == {'_run': {'test': None}}
    assert test_func(True) == {'_run': {'test': True}}
    assert test_func(False) == {'_run': {'test': False}}
    assert test_func(42) == {'_run': {'test': 42}}
    assert test_func(42.42) == {'_run': {'test': 42.42}}
    assert test_func('test') == {'_run': {'test': 'test'}}
    assert test_func

# Generated at 2022-06-12 21:52:59.104803
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    # pylint: disable=missing-docstring
    stats = AggregateStats()
    stats.update_custom_stats("_run", {"failed": 0, "ok": 0, "skipped": 0, "changed": 0})
    assert stats.custom == {"_run": {"failed": 0, "ok": 0, "skipped": 0, "changed": 0}}
    stats.increment("ok", "localhost")
    stats.increment("ok", "localhost")
    stats.increment("changed", "localhost")
    stats.increment("rescued", "localhost")
    assert stats.custom == {"_run": {"failed": 0, "ok": 0, "skipped": 0, "changed": 0}, "localhost": {"failed": 0, "ok": 0, "skipped": 0, "changed": 0}}
    stats.set_custom

# Generated at 2022-06-12 21:53:03.869082
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    a = AggregateStats()
    a.update_custom_stats('foo', 1)
    assert a.custom['_run']['foo'] == 1
    a.update_custom_stats('foo', 1)
    assert a.custom['_run']['foo'] == 2
    a.update_custom_stats('bar', 1, 'host')
    assert a.custom['host']['bar'] == 1
    a.update_custom_stats('bar', 1, 'host')
    assert a.custom['host']['bar'] == 2
    a.update_custom_stats('bar', 1, 'host')
    assert a.custom['host']['bar'] == 3
    a.update_custom_stats('bar', 'a', 'host2')

# Generated at 2022-06-12 21:53:09.554883
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    stats.update_custom_stats('add', {'a': 1})
    assert stats.custom['_run']['add'] == {'a': 1}
    stats.update_custom_stats('add', {'a': 2})
    assert stats.custom['_run']['add'] == {'a': 3}
    stats.update_custom_stats('add', {'a': {}}, host='localhost')
    assert stats.custom['localhost']['add'] == {'a': {}}
    stats.update_custom_stats('add', {'a': 2}, host='localhost')
    assert stats.custom['localhost']['add'] == 2

# Generated at 2022-06-12 21:53:16.460144
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    stats.update_custom_stats('test_count', {'success': 1, 'fail': 2})
    assert stats.custom['_run']['test_count']['success'] == 1
    assert stats.custom['_run']['test_count']['fail'] == 2

    stats.update_custom_stats('test_count', {'success': 3, 'fail': 4})
    assert stats.custom['_run']['test_count']['success'] == 4
    assert stats.custom['_run']['test_count']['fail'] == 6

    stats.update_custom_stats('test_count', 1)
    assert stats.custom['_run']['test_count'] == 1

    stats.update_custom_stats('test_count', 'foobar')
   

# Generated at 2022-06-12 21:53:23.777367
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    failed = False
    aggregate_stats = AggregateStats()
    aggregate_stats.ok['host'] = 1
    aggregate_stats.decrement('ok', 'host')
    if aggregate_stats.ok != dict(host=0):
        failed = True
    if not failed:
        print("OK")
    else:
        print("FAILED")

if __name__ == '__main__':
    test_AggregateStats_decrement()

# Generated at 2022-06-12 21:53:28.844899
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    s = AggregateStats()
    s.increment('ok', 'host1')
    s.decrement('ok', 'host1')
    assert s.ok.get('host1') == 0
    # This should pass
    s.decrement('ok', 'host1')
    # This should never happen, but let's be safe
    s.decrement('ok', 'host2')
    assert s.ok.get('host2') == 0

# Generated at 2022-06-12 21:53:31.366893
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggr = AggregateStats()
    aggr.dark["myhost"] = 4
    aggr.decrement("dark", "myhost")
    assert aggr.dark["myhost"] == 3

# Generated at 2022-06-12 21:53:34.007293
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    as_ = AggregateStats()
    as_.increment('ok', 'test')
    as_.increment('ok', 'test')
    as_.increment('ok', 'test')
    as_.decrement('ok', 'test')
    assert as_.ok['test'] == 2

# Generated at 2022-06-12 21:53:39.818503
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():

    ag = AggregateStats()
    ag.ok = {'host1': 1, 'host2': 1}
    ag.decrement('ok', 'host1')
    assert ag.ok['host1'] == 0
    assert ag.ok['host2'] == 1

    ag = AggregateStats()
    ag.ok = {'host1': 0, 'host2': 1}
    ag.decrement('ok', 'host1')
    assert ag.ok['host1'] == 0
    assert ag.ok['host2'] == 1

    ag = AggregateStats()
    ag.ok = {'host1': 1, 'host2': 1}
    ag.decrement('ok', 'host3')
    assert ag.ok['host1'] == 1
    assert ag.ok['host2'] == 1

# Generated at 2022-06-12 21:53:46.511371
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    test_obj = AggregateStats()

    # test decrementing an unset key
    test_obj.decrement('ignored', 'host')
    assert test_obj.ignored.get('host', 0) == 0

    # test decrementing key set to 1
    test_obj.ignored['host'] = 1
    test_obj.decrement('ignored', 'host')
    assert test_obj.ignored['host'] == 0

    # test decrementing key set to 0
    test_obj.decrement('ignored', 'host')
    assert test_obj.ignored['host'] == 0

# Generated at 2022-06-12 21:53:54.943134
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    import os
    import sys
    import unittest

    try:
        from unittest import mock
    except ImportError:
        import mock

    ansible_module_utils = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if ansible_module_utils not in sys.path:
        sys.path.insert(0, ansible_module_utils)
    from ansible.module_utils.common.collections import MutableMapping
    from ansible.module_utils._text import to_bytes

    def _mock_empty_value(self, key):
        return None

    def _mock_get_value(self, key):
        return 1


# Generated at 2022-06-12 21:53:57.484403
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    agg = AggregateStats()
    agg.decrement('ok', 'hostname')
    agg.decrement('ok', 'hostname')
    assert agg.ok['hostname'] == 0

# Generated at 2022-06-12 21:54:05.450479
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    assert stats.ok == {}

    # Decrement an empty field
    stats.decrement('ok', 'host')
    assert stats.ok == {'host': 0}

    # Decrement a non-empty field
    stats.increment('ok', 'host')
    stats.decrement('ok', 'host')
    assert stats.ok == {'host': 0}

    # Decrement a non-empty field twice
    stats.increment('ok', 'host')
    stats.increment('ok', 'host')
    stats.decrement('ok', 'host')
    stats.decrement('ok', 'host')
    assert stats.ok == {'host': 0}


# Generated at 2022-06-12 21:54:07.398902
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    from ansible.utils.vars import merge_hash
    agg = AggregateStats()
    agg.increment("failures", host="foo")
    agg.decrement("failures", host="foo")
    assert agg.failures["foo"] == 0