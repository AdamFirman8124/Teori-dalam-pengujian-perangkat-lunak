

# Generated at 2022-06-12 21:51:15.858729
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    test_stats = AggregateStats()
    test_stats.increment("ok", "test_host")
    test_stats.increment("ok", "test_host")
    test_stats.increment("ok", "test_host")
    test_stats.increment("failed", "test_host")
    test_stats.decrement("failed", "test_host")
    assert test_stats.ok == {"test_host": 3}
    assert test_stats.failures == {"test_host": 0}

# Generated at 2022-06-12 21:51:24.685610
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # Test "failures"
    a = AggregateStats()
    a.decrement('failures', 'myhost')
    assert a.failures == {'myhost': 0}, "test_AggregateStats_decrement 1: failure"
    a.failures = {'myhost': 1}
    a.decrement('failures', 'myhost')
    assert a.failures == {'myhost': 0}, "test_AggregateStats_decrement 2: failure"
    # Test "ok"
    a = AggregateStats()
    a.decrement('ok', 'myhost')
    assert a.ok == {'myhost': 0}, "test_AggregateStats_decrement 3: failure"
    a.ok = {'myhost': 1}

# Generated at 2022-06-12 21:51:28.665716
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'abcd')
    stats.decrement('ok', 'no-host')
    stats.decrement('ok', 'abcd')
    assert stats.ok['abcd'] == 1
    assert stats.ok.get('no-host', None) == 0


# Generated at 2022-06-12 21:51:33.156095
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.dark = dict()
    stats.dark['ansible.com'] = 100
    stats.decrement('dark', 'ansible.com')
    assert stats.dark['ansible.com'] == 99
    stats.decrement('dark', 'ansible.com')
    assert stats.dark['ansible.com'] == 98
    stats.decrement('dark', 'ansible.com')
    assert stats.dark['ansible.com'] == 97
    stats.decrement('dark', 'ansible.com')
    assert stats.dark['ansible.com'] == 96
    stats.decrement('dark', 'ansible.com')
    assert stats.dark['ansible.com'] == 95

# Generated at 2022-06-12 21:51:43.804940
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()

    stats.update_custom_stats("a", dict())
    assert stats.custom["_run"]["a"] == dict()

    stats.update_custom_stats("a", dict())
    assert stats.custom["_run"]["a"] == dict()

    stats.update_custom_stats("a", dict(b=1))
    assert stats.custom["_run"]["a"] == dict(b=1)

    stats.update_custom_stats("a", dict(c=0.5))
    assert stats.custom["_run"]["a"] == dict(b=1, c=0.5)

    stats.update_custom_stats("a", dict(c=1))
    assert stats.custom["_run"]["a"] == dict(b=1, c=1)



# Generated at 2022-06-12 21:51:51.800473
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    AS = AggregateStats()
    AS.decrement("processed", "localhost")
    assert AS.processed["localhost"] == 0, "We should have 0 processed"
    AS.processed["localhost"] = 1
    AS.decrement("processed", "localhost")
    assert AS.processed["localhost"] == 0, "We should have 0 processed"
    # What happens when we decrement a non-existing key
    AS.increment("processed", "localhost")
    AS.decrement("processed", "remotehost")
    assert AS.processed["remotehost"] == 0, "We should have 0 processed"



# Generated at 2022-06-12 21:51:55.726488
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'localhost')
    assert stats.ok['localhost'] == 1
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0
    # There's no need to decrement a missing key
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0

# Generated at 2022-06-12 21:52:00.021317
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.custom['foo'] = {}
    stats.custom['foo']['bar'] = 4
    stats.decrement('custom', 'foo')
    assert stats.custom == {'foo': {'bar': 3}}
    # decrementing a key that does not exist should automatically set it to 0
    stats.decrement('custom', 'bar')
    assert stats.custom == {'foo': {'bar': 3}, 'bar': {}}

# Generated at 2022-06-12 21:52:02.674630
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0

# Generated at 2022-06-12 21:52:06.013938
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    asx = AggregateStats()
    asx.ok = {'localhost': 1}
    asx.decrement('ok', 'localhost')
    assert asx.ok == {'localhost': 0}
