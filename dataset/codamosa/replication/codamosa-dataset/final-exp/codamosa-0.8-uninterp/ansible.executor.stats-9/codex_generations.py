

# Generated at 2022-06-12 21:51:03.556633
# Unit test for method decrement of class AggregateStats

# Generated at 2022-06-12 21:51:08.092810
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # create a AggregateStats object
    astats = AggregateStats()
    astats.decrement("ok", "localhost")
    #ok of localhost  should be 0 as decremented
    assert astats.ok["localhost"] == 0
    # creating a dict for ok
    dict_ok = {"localhost": 1}
    # creating an object of AggregateStats
    astats = AggregateStats()
    # creating a dict for ok "localhost": 1
    astats.ok = dict_ok
    # decrementing ok for localhost
    astats.decrement("ok", "localhost")
    #ok of localhost  should be 0 as decremented
    assert astats.ok["localhost"] == 0

# Generated at 2022-06-12 21:51:16.364494
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', '127.0.0.1')
    assert stats.ok == {'127.0.0.1': 0}
    stats.decrement('dark', '127.0.0.1')
    assert stats.dark == {'127.0.0.1': 0}
    stats.decrement('rescued', '127.0.0.1')
    assert stats.rescued == {'127.0.0.1': 0}
    stats.dark['127.0.0.1'] = 1
    stats.decrement('dark', '127.0.0.1')
    assert stats.dark == {'127.0.0.1': 0}


# Generated at 2022-06-12 21:51:25.158541
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    import pytest

    stats = AggregateStats()
    stats.increment('ignored', 'host1')
    stats.increment('ignored', 'host1')
    assert stats.ignored['host1'] == 2

    stats.increment('ignored', 'host2')
    assert stats.ignored['host2'] == 1

    # Check that processing count is incremented
    assert stats.processed['host1'] == 1
    assert stats.processed['host2'] == 1

    with pytest.raises(AttributeError):
        stats.increment('something', 'host2')

    # Check that numbers are coerced to int even if original value is float
    stats.ignored['host1'] = 0.0
    stats.increment('ignored', 'host1')
    assert stats.ignored['host1'] == 1



# Generated at 2022-06-12 21:51:30.135213
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.ok['test_host'] = 0
    stats.ok['test_host'] = stats.ok['test_host'] + 1
    assert stats.ok['test_host'] == 1
    stats.decrement('ok', 'test_host')
    assert stats.ok['test_host'] == 0
    stats.decrement('ok', 'test_host')
    assert stats.ok['test_host'] == 0

# Generated at 2022-06-12 21:51:41.181327
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate = AggregateStats()

    # Host did not change, already successful
    aggregate.ok['testhost'] = 1
    aggregate.decrement('ok', 'testhost')
    assert aggregate.ok == { 'testhost': 0 }

    # Host changed, now failure
    aggregate.changed['testhost'] = 1
    aggregate.decrement('changed', 'testhost')
    assert aggregate.changed == { 'testhost': 0 }
    assert aggregate.failures == { 'testhost': 1 }

    # Host was ok, now ignored
    aggregate.ok['testhost'] = 1
    aggregate.decrement('ok', 'testhost')
    assert aggregate.ok == { 'testhost': 0 }
    assert aggregate.ignored == { 'testhost': 1 }

    # Host was skipped, now ok

# Generated at 2022-06-12 21:51:50.625609
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    host = 'localhost'
    which = 'failures'
    what = 2
    stats.update_custom_stats(which, what, host)
    assert stats.custom[host][which] == what

    what = 1
    stats.update_custom_stats(which, what, host)
    assert stats.custom[host][which] == (what + what)

    what = {'k1': 'v1'}
    stats.update_custom_stats(which, what, host)
    assert stats.custom[host][which] == (what + what)

    what = {'k1': 'v2'}
    stats.update_custom_stats(which, what, host)
    assert stats.custom[host][which] == {'k1': 'v2'}

# Generated at 2022-06-12 21:51:58.594744
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggr = AggregateStats()
    
    assert aggr.decrement('failures', 'test_host') == dict(failures=0)
    assert aggr.decrement('failures', 'test_host') == dict(failures=0)
    assert aggr.decrement('failures', 'test_host') == dict(failures=0)
    assert aggr.decrement('failures', 'test_host') == dict(failures=0)
    aggr.increment('failures', 'test_host')
    assert aggr.decrement('failures', 'test_host') == dict(failures=0)
    aggr.increment('failures', 'test_host')
    aggr.increment('failures', 'test_host')

# Generated at 2022-06-12 21:52:01.223868
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    agg_stats = AggregateStats()

    agg_stats.increment('ok', 'host1')
    agg_stats.increment('ok', 'host1')
    agg_stats.increment('ok', 'host2')

    expected_ok = {'host1':2, 'host2':1}

    assert agg_stats.ok == expected_ok

# Generated at 2022-06-12 21:52:10.755936
# Unit test for method decrement of class AggregateStats

# Generated at 2022-06-12 21:52:19.540204
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    aggregateStats = AggregateStats()
    assert dict() == aggregateStats.custom
    # Test for adding an entry to custom stats
    aggregateStats.update_custom_stats("key1", "value1")
    assert dict(_run=dict(key1="value1")) == aggregateStats.custom
    # Test for adding another entry to custom stats
    aggregateStats.update_custom_stats("key2", "value2")
    assert dict(_run=dict(key1="value1", key2="value2")) == aggregateStats.custom
    # Test for adding another entry to custom stats
    aggregateStats.update_custom_stats("key1", "value3")
    assert dict(_run=dict(key1="value3", key2="value2")) == aggregateStats.custom
    # Test for adding an entry to custom stats for a specific host
    aggregateStats.update_

# Generated at 2022-06-12 21:52:27.805437
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    aggregate = AggregateStats()

    # test appending to stats
    aggregate.update_custom_stats('my_stats', 'test')
    aggregate.update_custom_stats('my_stats', 'test')
    aggregate.update_custom_stats('my_stats', 'test')
    assert aggregate.custom['_run']['my_stats'] == 'testtesttest'

    # test merging of dicts
    aggregate.set_custom_stats('my_stats', {'a': 'b', 'c': 'd'})
    aggregate.set_custom_stats('my_stats', {'a': 'b', 'c': 'e'})
    assert aggregate.custom['_run']['my_stats']['a'] == 'b'

# Generated at 2022-06-12 21:52:34.176906
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    # instantiate class
    aggr_stats = AggregateStats()

    # test set_custom_stats method
    aggr_stats.set_custom_stats('foo', 'bar')
    assert aggr_stats.custom['_run']['foo'] == 'bar'

    # test update_custom_stats method without key 'foo'
    aggr_stats = AggregateStats()
    aggr_stats.update_custom_stats('foo', 'bar')
    assert aggr_stats.custom['_run']['foo'] == 'bar'

    # test update_custom_stats method with key 'foo'
    aggr_stats.update_custom_stats('foo', 'bar')
    assert aggr_stats.custom['_run']['foo'] == 'barbar'

    # test update_custom_stats method with key 'foo

# Generated at 2022-06-12 21:52:42.910037
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():

    agg = AggregateStats()

    agg.update_custom_stats('custom', {"key": "value"}, "host")
    assert agg.custom['host']['custom']['key'] == 'value'

    agg.update_custom_stats('custom', {"key": "value"}, "host")
    assert agg.custom['host']['custom']['key'] == 'value'

    agg.update_custom_stats('custom', {"key": "value2"}, "host")
    assert agg.custom['host']['custom']['key'] == 'value2'

    agg.update_custom_stats('dont_overwrite', {"key": "value"})
    assert agg.custom['_run']['dont_overwrite'] == {"key": "value"}


# Generated at 2022-06-12 21:52:51.875257
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():

    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'a': 2, 'b': 0, 'd': 4}
    dict3 = {'host1': dict1, 'host2': dict2}
    dict4 = {'host2': dict2}

    stats = AggregateStats()

    stats.update_custom_stats('test', dict1)
    assert stats.custom['_run']['test'] == dict1
    stats.set_custom_stats('test', dict2)
    assert stats.custom['_run']['test'] == dict2
    stats.set_custom_stats('test', dict2, 'host')
    assert stats.custom['host']['test'] == dict2
    stats.update_custom_stats('test', dict1, 'host')


# Generated at 2022-06-12 21:53:00.619316
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    aggregate_stats = AggregateStats()
    stats_run = {'a': 'x', 'b': 'y'}
    aggregate_stats.update_custom_stats('test', stats_run)
    assert {'test': stats_run} == aggregate_stats.custom

    stats = {'c': 'z', 'd': 'u'}
    aggregate_stats.update_custom_stats('test', stats, host='host1')
    assert {'test': stats_run, 'host1': {'test': stats}} == aggregate_stats.custom

    # test merging of two dictionaries using update_custom_stats
    stats = {'b': 'y2', 'c': 'z2', 'e': 'v'}
    aggregate_stats.update_custom_stats('test', stats, host='host1')

# Generated at 2022-06-12 21:53:07.620359
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():

    stats = AggregateStats()
    # test for int
    stats.update_custom_stats('foo', 1, 'host0')
    assert stats.custom['host0']['foo'] == 1
    stats.update_custom_stats('foo', 1, 'host0')
    assert stats.custom['host0']['foo'] == 2
    # test for str
    stats.update_custom_stats('foo', 'bar', 'host0')
    assert stats.custom['host0']['foo'] == 'bar'
    # test for merging of dict
    stats.update_custom_stats('foo', {'bar': 1}, 'host0')
    assert stats.custom['host0']['foo'] == {'bar': 1}
    stats.update_custom_stats('foo', {'baz': 2}, 'host0')


# Generated at 2022-06-12 21:53:11.970106
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    result_dict = {}
    test_obj = AggregateStats()
    test_obj.set_custom_stats('test_key','test_value','test_host')
    result_dict['test_key'] = 'test_value'
    assert test_obj.custom['test_host'] == result_dict

    test_obj.set_custom_stats('test_key_2','test_value_2','test_host')
    result_dict['test_key_2'] = 'test_value_2'
    assert test_obj.custom['test_host'] == result_dict

    test_obj.set_custom_stats('test_key_3','test_value_3','test_host_2')
    result_dict_2 = {}
    result_dict_2['test_key_3'] = 'test_value_3'

# Generated at 2022-06-12 21:53:17.395694
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    import json
    import sys
    import os

    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'lib')))
    from ansible.module_utils._text import to_text

    stats = AggregateStats()

    # When the host is None or '_run' and there is no custom item with the given name, add the new item
    assert to_text(json.dumps(stats.custom)) == to_text(json.dumps({}))
    stats.update_custom_stats('test', 'test')
    assert to_text(json.dumps(stats.custom)) == to_text(json.dumps({'_run': {'test': 'test'}}))

    # When the host is None or '

# Generated at 2022-06-12 21:53:26.981444
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    ag = AggregateStats()
    ag.update_custom_stats('foo', 'bar')
    assert ag.custom.get('_run', {}).get('foo') == 'bar'
    ag.update_custom_stats('foo', 'baz')
    assert ag.custom.get('_run', {}).get('foo') == 'baz'
    ag.update_custom_stats('foo', 'bar', 'bob')
    assert ag.custom.get('bob', {}).get('foo') == 'bar'
    ag.update_custom_stats('foo', 'baz', 'bob')
    assert ag.custom.get('bob', {}).get('foo') == 'baz'
    ag.update_custom_stats('foo', 'bar', 'bob')