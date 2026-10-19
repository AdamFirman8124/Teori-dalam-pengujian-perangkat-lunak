

# Generated at 2022-06-12 21:51:05.550571
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    import pytest
    from ansible.module_utils.common._collections_compat import MutableMapping
    stats = AggregateStats()
    stats.update_custom_stats('foo', {'bar': 2}, 'localhost')
    assert stats.custom['localhost']['foo']['bar'] == 2
    stats.update_custom_stats('foo', {'bar': 6})
    assert stats.custom['_run']['foo']['bar'] == 6
    with pytest.raises(TypeError):
        stats.update_custom_stats('foo', 'bar', 'localhost')
    with pytest.raises(TypeError):
        stats.update_custom_stats('foo', 1, 'localhost')

# Generated at 2022-06-12 21:51:16.280053
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    ags = AggregateStats()
    ags.update_custom_stats("play", "play_1")
    ags.update_custom_stats("task", "task_1", "host1")
    print (ags.custom)
    print ("*" * 40)
    # test add dictionaries
    ags.update_custom_stats("play", {"play_2": "play_2"}, "host1")
    ags.update_custom_stats("task", {"task_2": "task_2"}, "host1")
    print (ags.custom)
    print ("*" * 40)
    # test add int
    ags.update_custom_stats("play", 1)
    ags.update_custom_stats("task", 1, "host1")
    print (ags.custom)

# Generated at 2022-06-12 21:51:25.094409
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():

    X = AggregateStats()

    # test when no entry for host exists
    X.update_custom_stats('which', 'what', 'host')
    assert X.custom == {'host': {'which': 'what'}}

    # test when no entry for which exists
    X.custom = {'host': {'other': 'other'}}
    X.update_custom_stats('which', 'what', 'host')
    assert X.custom == {'host': {'which': 'what', 'other': 'other'}}

    # test when matching types
    X.custom = {'host': {'which': 'other'}}
    X.update_custom_stats('which', 'what', 'host')
    assert X.custom == {'host': {'which': 'whatother'}}

    # test when mismatching types
    X

# Generated at 2022-06-12 21:51:34.409113
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate_stats = AggregateStats()
    aggregate_stats.increment('ok', 'localhost')
    assert aggregate_stats.decrement('ok', 'localhost') is None
    assert aggregate_stats.ok == {'localhost': 0}
    assert aggregate_stats.ignored == {'localhost': 0}
    assert aggregate_stats.decrement('ignored', 'localhost') is None
    # Decrementing again should not give an error
    assert aggregate_stats.decrement('ignored', 'localhost') is None
    assert aggregate_stats.ok == {'localhost': 0}
    assert aggregate_stats.ignored == {'localhost': 0}
    # Decrementing without incrementing should not give an error
    assert aggregate_stats.decrement('ok', 'localhost') is None

# Generated at 2022-06-12 21:51:42.447551
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('failures', 'host1')
    stats.increment('ignored', 'host1')
    assert stats.failures['host1'] == 1
    assert stats.ignored['host1'] == 1
    stats.decrement('failures', 'host1')
    stats.decrement('ignored', 'host1')
    assert stats.failures['host1'] == 0
    assert stats.ignored['host1'] == 0
    stats.decrement('ignored', 'host1')
    assert stats.ignored['host1'] == 0

# Generated at 2022-06-12 21:51:48.627165
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'host1')
    stats.increment('ok', 'host2')
    stats.decrement('ok', 'host1')
    stats.decrement('ok', 'host2')
    assert stats.ok.get('host1') == 0
    assert stats.ok.get('host2') == 0
    stats.decrement('ok', 'host2')
    assert stats.ok.get('host2') == 0

# Generated at 2022-06-12 21:51:56.885765
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    stats = AggregateStats()
    stats.increment('ok', '127.0.0.1')
    assert stats.ok['127.0.0.1'] == 1 and stats.processed['127.0.0.1'] == 1
    stats.increment('ok', '127.0.0.1')
    assert stats.ok['127.0.0.1'] == 2 and stats.processed['127.0.0.1'] == 1
    stats.increment('failures', '127.0.0.1')
    assert stats.failures['127.0.0.1'] == 1 and stats.processed['127.0.0.1'] == 1
    stats.increment('ok', '127.0.0.1')
    assert stats.ok['127.0.0.1'] == 3 and stats

# Generated at 2022-06-12 21:52:02.440863
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    stats = AggregateStats()
    stats.increment('ok', 'host1')
    stats.increment('ok', 'host2')
    stats.increment('failures', 'host3')
    stats.increment('dark', 'host4')

    assert stats.processed['host1'] == 1
    assert stats.ok['host1'] == 1
    assert stats.ok['host2'] == 1
    assert stats.failures['host3'] == 1
    assert stats.dark['host4'] == 1


# Generated at 2022-06-12 21:52:12.436039
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    stats.update_custom_stats('counter', 1, 'host1')
    assert stats.custom['host1']['counter'] == 1

    # Adding a different type than the existing type should not update
    # the custom stats.
    stats.update_custom_stats('counter', '1', 'host2')
    assert stats.custom['host1']['counter'] == 1
    assert stats.custom['host2']['counter'] is None

    # Add one to the existing value
    stats.update_custom_stats('counter', 1, 'host1')
    assert stats.custom['host1']['counter'] == 2

    # Attempting to add to a non-existing value should not affect the
    # existing stats
    stats.update_custom_stats('not_counter', 3, 'host1')


# Generated at 2022-06-12 21:52:15.157845
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    a = AggregateStats()
    a.ok["b"] = 1
    a.decrement("ok", "b")
    assert a.ok["b"] == 0
    a.decrement("ok", "c")
    assert a.ok["c"] == 0


# Generated at 2022-06-12 21:52:18.352375
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():

    stats = AggregateStats()
    stats.increment("ok", "host1")
    stats.decrement("ok", "host1")
    assert stats.ok["host1"] == 0


# Generated at 2022-06-12 21:52:24.784023
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()

    # test for simple values
    stats.update_custom_stats("attribute_name", 1)
    assert stats.get_custom_stats("attribute_name") == 1
    stats.update_custom_stats("attribute_name", 1)
    assert stats.get_custom_stats("attribute_name") == 2
    stats.update_custom_stats("attribute_name", -1)
    assert stats.get_custom_stats("attribute_name") == 1

    # test for a hash
    stats.update_custom_stats("key_a", {"key_b": 1, "key_c": 2})
    stats.update_custom_stats("key_a", {"key_b": 1, "key_c": 2})

# Generated at 2022-06-12 21:52:32.838999
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    import pytest
    from inspect import cleandoc

    # both dicts, merge
    h_stats = AggregateStats()
    h_stats.update_custom_stats('foo', {'a': 1}, 'bar')
    h_stats.update_custom_stats('foo', {'b': 2}, 'bar')
    assert h_stats.custom['bar']['foo'] == {'a': 1, 'b': 2}

    # numeric, numeric, add
    h_stats = AggregateStats()
    h_stats.update_custom_stats('foo', 1, 'bar')
    h_stats.update_custom_stats('foo', 1, 'bar')
    assert h_stats.custom['bar']['foo'] == 2

    # string, string, add
    h_stats = AggregateStats()
    h_stats

# Generated at 2022-06-12 21:52:37.776408
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # Setup:
    agg_stats_obj = AggregateStats()
    agg_stats_obj.ok['some host'] = 1

    # Run:
    agg_stats_obj.decrement('ok', 'some host')

    # Verify:
    assert agg_stats_obj.ok == {'some host': 0}


# Generated at 2022-06-12 21:52:44.309498
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    '''decrement does not allow a variable to go below 0'''
    stats = AggregateStats()
    stats.ok["host1"] = 1
    stats.ok["host2"] = 1
    stats.decrement("ok", "host1")

    assert stats.ok["host1"] == 0, "Should have decremented host1's ok stats to 0"
    stats.decrement("ok", "host2")
    assert stats.ok["host2"] == 0, "Should have decremented host2's ok stats to 0"

    try:
        stats.decrement("ok", "host1")
    except Exception as e:
        assert str(e) == "Don't be so negative", "Should have failed to decrement below 0"

# Generated at 2022-06-12 21:52:53.917243
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    from nose2.tools import params
    from collections import defaultdict

    # These params are used to test update_custom_stats:
    # (input params what, expected result)
    test_params_for_what = params(
        # Testing int type
        (10, 10),
        # Testing string type
        ('test', 'test'),
        # Testing class MutableMapping
        (defaultdict(int), defaultdict(int)),
        # Testing list
        ([1,2,3], [1,2,3]),
        # Testing tuple
        ((1,2,3), (1,2,3)),
        # Testing str and list
        (['test', 1, [2, 3], '4'], ['test', 1, [2, 3], '4'])
    )

    # These params are used to test update_custom_stats

# Generated at 2022-06-12 21:53:02.335936
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    stats.update_custom_stats('foo', {'bar': 1})
    assert stats.custom['_run']['foo'] == {'bar': 1}
    stats.update_custom_stats('foo', {'baz': 2})
    assert stats.custom['_run']['foo'] == {'bar': 1, 'baz': 2}
    stats.update_custom_stats('foo', {'bar': 2})
    assert stats.custom['_run']['foo'] == {'bar': 3, 'baz': 2}
    stats.update_custom_stats('foo', {'qux': 4}, host='localhost')
    assert stats.custom['localhost']['foo'] == {'qux': 4}

# Generated at 2022-06-12 21:53:06.068562
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate_stats = AggregateStats()
    aggregate_stats.decrement('ok', 'test_host')
    assert aggregate_stats.ok['test_host'] == 0
    assert len(aggregate_stats.ok) == 1
    aggregate_stats.ok['test_host'] = 2
    aggregate_stats.decrement('ok', 'test_host')
    assert aggregate_stats.ok['test_host'] == 1
    aggregate_stats.decrement('ok', 'test_host')
    assert aggregate_stats.ok['test_host'] == 0
    try:
        aggregate_stats.ok['test_host'] = -1
        aggregate_stats.decrement('ok', 'test_host')
    except KeyError:
        assert True
    assert aggregate_stats.ok['test_host'] == 0

# Generated at 2022-06-12 21:53:13.722031
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():

    import unittest

    # A test class for ansible.utils.AggregateStats
    class AggregateStatsTest(unittest.TestCase):

        # test for update_custom_stats method of class AggregateStats
        def test_update_custom_stats(self):

            stat = AggregateStats()
            stat.update_custom_stats('foo', 'bar')
            self.assertEqual(stat.custom['_run']['foo'], 'bar')

            stat.update_custom_stats('foo', 'bar')
            self.assertEqual(stat.custom['_run']['foo'], 'bar')

            stat.update_custom_stats('foo', 1)
            self.assertEqual(stat.custom['_run']['foo'], 1)

            stat.update_custom_stats('foo', 1)


# Generated at 2022-06-12 21:53:25.156421
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    stats.update_custom_stats('test_1', {'test_1': 1, 'test_2': 2, 'test_3': {'test_3': 3}})
    assert stats.custom['_run']['test_1'] == {'test_1': 1, 'test_2': 2, 'test_3': {'test_3': 3}}, 'Test failed: initial aggregation'
    stats.update_custom_stats('test_1', {'test_2': 3, 'test_3': {'test_3': 4}, 'test_4': {'test_4_1': 41}, 'test_5': 5})

# Generated at 2022-06-12 21:53:34.447174
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    test_stats = AggregateStats()
    test_stats.processed["host1"] = 1
    test_stats.failures["host1"] = 1
    test_stats.ok["host1"] = 2
    test_stats.dark["host1"] = 0
    test_stats.changed["host1"] = 0
    test_stats.skipped["host1"] = 0
    test_stats.rescued["host1"] = 0
    test_stats.ignored["host1"] = 0
    test_stats.custom["host1"] = {}
    test_stats.decrement("ok","host1")
    test_stats.decrement("ok","host1")
    assert test_stats.ok["host1"] == 0
    assert test_stats.custom["host1"] == {}


# Generated at 2022-06-12 21:53:37.445243
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.ok = { 'host1': 1 }

    # reduction is not possible
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 0

    # ok is not set
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 0


# Generated at 2022-06-12 21:53:40.924482
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 0
    stats.increment('ok', 'host1')
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 0
    stats.increment('ok', 'host1')
    stats.increment('ok', 'host2')
    assert stats.ok['host1'] == 1
    assert stats.ok['host2'] == 1

# Generated at 2022-06-12 21:53:42.872425
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate = AggregateStats()
    aggregate.decrement('dark', '127.0.0.1')
    assert aggregate.dark['127.0.0.1'] == 0

# Generated at 2022-06-12 21:53:45.802932
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'host1')
    assert stats.ok == {'host1': 0}

# Generated at 2022-06-12 21:53:49.795083
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # Nothing to decrement on empty object
    empty_stats = AggregateStats()
    empty_stats.decrement('ok', 'localhost')

    # Just test that nothing crashes
    stats = AggregateStats()
    stats.increment('failures', 'localhost')
    stats.decrement('failures', 'localhost')
    assert stats.failures['localhost'] == 0

# Generated at 2022-06-12 21:53:56.025391
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # Test with decrementing a key that exists in the statistics
    stats = AggregateStats()
    stats.ok['localhost'] = 2
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 1

    # Test with decrementing a key with a value of 1
    stats = AggregateStats()
    stats.ok['localhost'] = 1
    stats.decrement('ok', 'localhost')
    assert 'localhost' not in stats.ok

    # Test with decrementing a key with a value of 0
    stats = AggregateStats()
    stats.ok['localhost'] = 0
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0

# Generated at 2022-06-12 21:54:01.777201
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    from ansible.module_utils.six import iteritems

    ag = AggregateStats()
    ag.increment('ok', 'server1')
    ag.increment('ok', 'server1')
    ag.increment('ok', 'server1')
    assert ag.ok.get('server1', 0) == 3
    ag.decrement('ok', 'server1')
    assert ag.ok.get('server1', 0) == 2

# Generated at 2022-06-12 21:54:08.054440
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    s = AggregateStats()

    s.increment("dark", "host1")
    assert(s.dark["host1"] == 1)

    s.decrement("dark", "host1")
    assert(s.dark["host1"] == 0)

    s.increment("dark", "host1")
    s.increment("dark", "host2")
    assert(s.dark["host1"] == 1)
    assert(s.dark["host2"] == 1)

    s.decrement("dark", "host1")
    s.decrement("dark", "host2")
    assert(s.dark["host1"] == 0)
    assert(s.dark["host2"] == 0)

    s.dark["host3"] = 0
    s.decrement("dark", "host3")
   

# Generated at 2022-06-12 21:54:12.627117
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    testStats = AggregateStats()
    # decrement value from 0 to -1
    testStats.decrement('rescued', 'localhost')
    assert testStats.rescued['localhost'] == 0
    # decrement value from 1 to 0
    testStats.rescued['localhost'] = 1
    testStats.decrement('rescued', 'localhost')
    assert testStats.rescued['localhost'] == 0
