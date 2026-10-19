

# Generated at 2022-06-12 21:51:15.271371
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    host = "myhost"
    ag = AggregateStats()
    ag.ok[host] = 1
    ag.decrement('ok', host)
    assert ag.ok[host] == 0

# Generated at 2022-06-12 21:51:24.025747
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    ags = AggregateStats()
    ags.update_custom_stats('a', 1, None)
    assert (ags.custom == {'_run': {'a': 1}})
    assert (ags.custom['_run']['a'] == 1)
    ags.update_custom_stats('a', 2, None)
    assert (ags.custom == {'_run': {'a': 3}})
    assert (ags.custom['_run']['a'] == 3)
    ags.update_custom_stats('a', '2', None)
    assert (ags.custom == {'_run': {'a': '32'}})
    assert (ags.custom['_run']['a'] == '32')

# Generated at 2022-06-12 21:51:29.473465
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    aggregate = AggregateStats()
    aggregate.update_custom_stats("uptime", "1 day")
    assert aggregate.custom["_run"]["uptime"] == "1 day"
    aggregate.update_custom_stats("uptime", "1 day", "127.0.0.1")
    assert aggregate.custom["127.0.0.1"]["uptime"] == "1 day"
    aggregate.update_custom_stats("cpu_info", {"cpu_count": 2, "cpu_arch": "x86_64"})
    assert aggregate.custom["_run"]["cpu_info"] == {"cpu_count": 2, "cpu_arch": "x86_64"}
    aggregate.update_custom_stats("cpu_info", {"cpu_count": 1, "cpu_arch": "i386"})

# Generated at 2022-06-12 21:51:34.271906
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    aggregateStats = AggregateStats()
    aggregateStats.increment("ok", "host1")
    aggregateStats.increment("processed", "host2")
    aggregateStats.increment("rescued", "host3")
    aggregateStats.increment("ignored", "host4")
    aggregateStats.increment("dark", "host5")
    aggregateStats.increment("ok", "host3")
    assert aggregateStats.processed == {"host2": 1}
    assert aggregateStats.failures == {}
    assert aggregateStats.ok == {"host1": 1, "host3": 1}
    assert aggregateStats.dark == {"host5": 1}
    assert aggregateStats.changed == {}
    assert aggregateStats.skipped == {}
    assert aggregateStats.rescued == {"host3": 1}

# Generated at 2022-06-12 21:51:41.410863
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'test')
    stats.increment('ok', 'test')
    stats.decrement('ok', 'test')
    if stats.summarize('test')['ok'] != 1:
        raise AssertionError('ok should be 1')

    stats.decrement('ok', 'test')
    if stats.summarize('test')['ok'] != 0:
        raise AssertionError('ok should be 0')


# Generated at 2022-06-12 21:51:46.354480
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    stats = AggregateStats()
    host = 'testhost.example.com'
    stats.increment('ok', host)
    assert stats.ok[host] == 1
    stats.increment('failures', host)
    stats.increment('failures', host)
    assert stats.failures[host] == 2
    assert stats.ok[host] == 1


# Generated at 2022-06-12 21:51:54.911326
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggStat = AggregateStats()
    aggStat.decrement("changed", "testHost")
    assert(aggStat.changed["testHost"] == 0)
    aggStat.increment("changed", "testHost")
    aggStat.increment("changed", "testHost")
    aggStat.increment("changed", "testHost")
    aggStat.decrement("changed", "testHost")
    assert(aggStat.changed["testHost"] == 2)
    aggStat.decrement("changed", "testHost")
    assert(aggStat.changed["testHost"] == 1)
    aggStat.decrement("changed", "testHost")
    assert(aggStat.changed["testHost"] == 0)
    aggStat.decrement("changed", "testHost")

# Generated at 2022-06-12 21:52:01.352958
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():

    agg_stats = AggregateStats()

    agg_stats.update_custom_stats('counter', 1)
    assert agg_stats.custom['_run']['counter'] == 1

    agg_stats.update_custom_stats('counter', 1)
    assert agg_stats.custom['_run']['counter'] == 2

    agg_stats.update_custom_stats('counter', 1, host='host1')
    assert agg_stats.custom['host1']['counter'] == 1

    agg_stats.update_custom_stats('counter', -1, host='host1')
    assert agg_stats.custom['host1']['counter'] == 0

    agg_stats.update_custom_stats('counter', -1, host='host1')
    assert agg_stats.custom['host1']['counter'] == 0

    agg

# Generated at 2022-06-12 21:52:07.639408
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'host')
    assert stats.ok == {'host': 0}

    stats = AggregateStats()
    stats.ok = {'host': 2}
    stats.decrement('ok', 'host')
    assert stats.ok == {'host': 1}

    stats = AggregateStats()
    stats.decrement('ok', 'host')
    assert stats.ok == {'host': 0}

# Generated at 2022-06-12 21:52:15.157805
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.processed = { "foo": 1 }
    stats.failures = { "foo": 0, "bar": 1 }
    stats.ok = { "bar": 2, "baz": 4 }

    assert stats.processed == { "foo": 1 }
    assert stats.failures == { "foo": 0, "bar": 1 }
    assert stats.ok == { "bar": 2, "baz": 4 }

    stats.decrement("failures", "bar")
    stats.decrement("ok", "bar")

    assert stats.failures == { "foo": 0, "bar": 0 }
    assert stats.ok == { "bar": 1, "baz": 4 }