

# Generated at 2022-06-12 21:51:03.797577
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'host1')
    assert stats.ok.get('host1') == 0

# Generated at 2022-06-12 21:51:07.188824
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    ags = AggregateStats()
    ags.increment('failures', 'host')
    ags.increment('ok', 'host')
    ags.increment('ok', 'host')
    ags.increment('ok', 'host')
    ags.increment('failures', 'host')
    ags.increment('failures', 'host')
    print(ags.failures)
    print(ags.ok)


# Generated at 2022-06-12 21:51:16.392260
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    """AggregateStats.decrement should handle edge cases and not decrement below 0"""
    stats = AggregateStats()
    stats.decrement('ok', 'localhost');
    assert stats.ok['localhost'] == 0

    stats.ok['localhost'] = 3
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 2
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 1
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0

    stats.ok['localhost'] = -1
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0


# Generated at 2022-06-12 21:51:25.188971
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    sut = AggregateStats()
    for what in ('ok', 'failures', 'dark', 'changed', 'skipped', 'rescued', 'ignored'):
        sut.increment(what, 'testhost')
        sut.decrement(what, 'testhost')
        assert sut.__getattribute__(what)['testhost'] == 0
        assert 'testhost' in sut.processed
        assert sut.processed['testhost'] == 1
    assert sut.summarize('testhost')['ok'] == 0
    assert sut.summarize('testhost')['failures'] == 0
    assert sut.summarize('testhost')['unreachable'] == 0
    assert sut.summarize('testhost')['changed'] == 0
    assert sut.summarize

# Generated at 2022-06-12 21:51:32.009334
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    stats.update_custom_stats('blah', 3)
    assert stats.custom['_run']['blah'] == 3
    stats.update_custom_stats('blah', 2)
    assert stats.custom['_run']['blah'] == 5
    stats.update_custom_stats('blah', {'a': 1, 'b': 2})
    assert stats.custom['_run']['blah'] == {'a': 1, 'b': 2, 'a': 1, 'b': 2}


# Generated at 2022-06-12 21:51:38.274829
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    a = AggregateStats()

    a.decrement('ok', 'myhost')
    assert a.ok['myhost'] == 0

    a.ok['myhost'] = 1
    a.decrement('ok', 'myhost')
    assert a.ok['myhost'] == 0

    a.ok['myhost'] = 0
    a.decrement('ok', 'myhost')
    assert a.ok['myhost'] == 0

# Generated at 2022-06-12 21:51:39.226172
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    pass



# Generated at 2022-06-12 21:51:43.369346
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggstats = AggregateStats()
    aggstats.increment('ok', 'foo')
    aggstats.decrement('ok', 'foo')
    assert aggstats.ok['foo'] == 0
    # This should never happen, but let's be safe
    aggstats.decrement('ok', 'foo')
    assert aggstats.ok['foo'] == 0

# Generated at 2022-06-12 21:51:52.882711
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    import sys

    # Initialize the class and call update_custom_stats
    stats = AggregateStats()
    stats.update_custom_stats("variable", {'k1': 'v1', 'k2': 'v2'})
    assert stats.custom == {'_run': {'variable': {'k1': 'v1', 'k2': 'v2'}}}, "update_custom_stats method of AggregateStats class failed"

    stats.update_custom_stats("variable", {'k3': 'v3', 'k4': 'v4'})

# Generated at 2022-06-12 21:51:57.394749
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    ag = AggregateStats()
    ag.increment('ok', 'h1')
    ag.decrement('ok', 'h1')
    assert ag.ok == {'h1': 0}
    ag.decrement('ok', 'h1')
    assert ag.ok == {'h1': 0}
    ag.decrement('failures', 'h1')
    assert ag.ok == {'h1': 0}


# Generated at 2022-06-12 21:52:02.867708
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stat = AggregateStats()
    stat.failures['host1'] = 1
    stat.decrement('failures', 'host1')
    assert stat.failures['host1'] == 0
    stat.decrement('failures', 'host1')
    assert stat.failures['host1'] == 0

# Generated at 2022-06-12 21:52:08.138601
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    agg_stats = AggregateStats()
    agg_stats.decrement('ok', 'host1')
    assert agg_stats.ok == {'host1': 0}
    agg_stats.ok['host1'] = 5
    agg_stats.decrement('ok', 'host1')
    assert agg_stats.ok == {'host1': 4}


# Generated at 2022-06-12 21:52:09.952728
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'host')

    assert stats.ok['host'] == 0

# Generated at 2022-06-12 21:52:14.429914
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    host = 'localhost'
    stats.decrement('changed', host)
    assert stats.changed is not None
    assert host in stats.changed
    assert stats.changed[host] == 0
    stats.changed[host] = 1
    stats.decrement('changed', host)
    assert stats.changed[host] == 0


# Generated at 2022-06-12 21:52:23.043008
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():

    stats = AggregateStats()
    stats.decrement('changes', 'example1')
    stats.decrement('changes', 'example2')

    # Decrement of stats['changes']['example1']
    assert stats.changed['example1'] == 0
    assert stats.changed['example2'] == 0

    stats.decrement('ignored', 'example1')
    stats.decrement('ignored', 'example2')

    # Decrement of stats['ignored']['example1']
    assert stats.ignored['example1'] == 0
    assert stats.ignored['example2'] == 0

    stats.decrement('ok', 'example1')
    stats.decrement('ok', 'example2')

    # Decrement of stats['ok']['example1']
    assert stats.ok['example1']

# Generated at 2022-06-12 21:52:27.453042
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate_stats = AggregateStats()
    aggregate_stats.ok['host1'] = 1
    aggregate_stats.decrement('ok','host1')
    assert aggregate_stats.ok['host1'] == 0
    aggregate_stats.ok['host1'] = 0
    aggregate_stats.decrement('ok','host1')
    assert aggregate_stats.ok['host1'] == 0

# Generated at 2022-06-12 21:52:33.961507
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    ag = AggregateStats()
    ag.increment('ok', '127.0.0.1')
    ag.increment('ok', '127.0.0.2')
    ag.increment('ok', '127.0.0.3')
    assert ag.ok['127.0.0.1'] == 1
    assert ag.ok['127.0.0.2'] == 1
    assert ag.ok['127.0.0.3'] == 1
    assert ag.summarize('127.0.0.1') == {'ok': 1, 'unreachable': 0, 'rescued': 0, 'failures': 0, 'changed': 0, 'ignored': 0, 'skipped': 0}

# Generated at 2022-06-12 21:52:38.423732
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stat = AggregateStats()
    stat.decrement("rescued", "foo")
    assert stat.rescued["foo"] == 0
    stat.increment("rescued", "foo")
    stat.decrement("rescued", "foo")
    assert stat.rescued["foo"] == 0

# Generated at 2022-06-12 21:52:42.910227
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    a = AggregateStats()

    # one successful run
    a.increment('ok', 'localhost')
    assert a.ok['localhost'] == 1

    # decrement for positive values should work
    a.decrement('ok', 'localhost')
    assert a.ok['localhost'] == 0

    # decrement for 0 should just set the value to 0
    a.decrement('ok', 'localhost')
    assert a.ok['localhost'] == 0


# Generated at 2022-06-12 21:52:48.245251
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # test when _what[host] exist
    a = AggregateStats()
    a.ok['host'] = 1
    a.decrement('ok', 'host')
    assert a.ok['host'] == 0
    # test when _what[host] doesn't exist
    a.decrement('ok', 'host')
    assert a.ok['host'] == 0
    # test when _what[host] is a negative number
    a.ok['host'] = 0
    a.decrement('ok', 'host')
    assert a.ok['host'] == 0
    # test when _what[host] is a positive number
    a.ok['host'] = 1
    a.decrement('ok', 'host')
    assert a.ok['host'] == 0