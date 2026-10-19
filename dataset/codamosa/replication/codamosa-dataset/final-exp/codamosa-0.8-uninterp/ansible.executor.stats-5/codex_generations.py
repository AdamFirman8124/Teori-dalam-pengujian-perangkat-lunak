

# Generated at 2022-06-12 21:51:01.999154
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # GIVEN
    stats = AggregateStats()

    # WHEN
    for i in range(10):
        stats.increment('ok', 'foo')

    for i in range(10):
        stats.decrement('ok', 'foo')

    # THEN
    assert stats.ok['foo'] == 0

# Generated at 2022-06-12 21:51:07.492140
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    # Success Case
    def _update_custom_stats_success_case():
        a = AggregateStats()
        a.update_custom_stats('key', 1)
        assert a.custom['_run']['key'] == 1
        a.update_custom_stats('key', 2)
        assert a.custom['_run']['key'] == 3

    # Mismatch type Case
    def _update_custom_stats_mismatch_type():
        a = AggregateStats()
        a.update_custom_stats('key', 1)
        assert a.custom['_run']['key'] == 1
        a.update_custom_stats('key', 'string')
        assert a.custom['_run']['key'] == 1

    # Success Case: Dictionary object

# Generated at 2022-06-12 21:51:10.498283
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
  import unittest
  agg = AggregateStats()
  agg.decrement('ok', 'host1')
  assert agg.ok['host1'] == 0

# Generated at 2022-06-12 21:51:12.559143
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    as1 = AggregateStats()
    as1.decrement('skipped', 'test-host')
    assert as1.skipped['test-host'] == 0

# Generated at 2022-06-12 21:51:15.202015
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()

    stats.skipped = {
        "testhost": 1
    }

    stats.decrement("skipped", "testhost")

    assert stats.skipped["testhost"] == 0


# Generated at 2022-06-12 21:51:23.954379
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    a = AggregateStats()
    a.update_custom_stats('b', 1, 'host1')
    assert a.custom['host1']['b'] == 1

    a.update_custom_stats('b', 42, 'host2')
    assert a.custom['host2']['b'] == 42
    assert a.custom['host1']['b'] == 1

    a.update_custom_stats('b', {'c': 1}, 'host1')
    assert a.custom['host1']['b'] == {'c': 1}

    a.update_custom_stats('b', {'c': 2}, 'host1')
    assert a.custom['host1']['b'] == {'c': 2}

    a.update_custom_stats('b', ['c', 1], 'host1')


# Generated at 2022-06-12 21:51:30.482524
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    stats = AggregateStats()
    host = '127.0.0.1'

    assert stats.processed == {}
    assert stats.failures == {}
    assert stats.ok == {}
    assert stats.dark == {}
    assert stats.changed == {}
    assert stats.skipped == {}
    assert stats.rescued == {}
    assert stats.ignored == {}

    stats.increment('failures', host)

    assert stats.failures.get(host) == 1



# Generated at 2022-06-12 21:51:41.373571
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    stats = AggregateStats()
    stats.increment('ok', 'test-host')
    assert stats.processed['test-host'] == 1
    assert stats.ok['test-host'] == 1

    # test incrementing failed items
    stats.increment('failures', 'test-host')
    stats.increment('failures', 'test-host')
    stats.increment('failures', 'test-host')

    assert stats.failures['test-host'] == 3

    # test incrementing dark items
    stats.increment('dark', 'test-host')
    stats.increment('dark', 'test-host')

    assert stats.dark['test-host'] == 2
    assert stats.ok['test-host'] == 1

# Generated at 2022-06-12 21:51:43.213517
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'localhost')
    assert stats.ok == {'localhost': 0}

# Generated at 2022-06-12 21:51:52.730248
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    # Create stats instance
    stats = AggregateStats()

    # Set the custom stats
    stats.set_custom_stats("test_set", 33)
    stats.update_custom_stats("test_agg", 77)

    # Retrieve the custom stats
    cust_stats = stats.custom['_run']
    assert cust_stats["test_set"] == 33
    assert cust_stats["test_agg"] == 77

    # Test aggregation of a dictionary
    # Set a different custom stats
    another_dict = {'fruit': 'orange', 'count': 7}
    stats.update_custom_stats("test_agg", another_dict)

    # Retrieve the custom stats
    cust_stats = stats.custom['_run']
    assert cust_stats["test_set"] == 33
    assert cust_stats["test_agg"] == another_

# Generated at 2022-06-12 21:51:57.898881
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.ok = {'host': 1}
    stats.decrement('ok', 'host')
    assert stats.ok == {'host': 0}
    stats.decrement('ok', 'host')
    assert stats.ok == {'host': 0}


# Generated at 2022-06-12 21:52:02.903924
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats =  AggregateStats()
    assert stats.processed == {}
    assert stats.failures == {}
    assert stats.ok == {}
    assert stats.dark == {}
    assert stats.changed == {}
    assert stats.skipped == {}
    assert stats.rescued == {}
    assert stats.ignored == {}
    assert stats.custom == {}

    stats.increment("ok", "fakehost")
    assert stats.processed == {"fakehost": 1}
    assert stats.ok == {"fakehost": 1}

    stats.increment("ok", "fakehost")
    assert stats.processed == {"fakehost": 1}
    assert stats.ok == {"fakehost": 2}

    # this should not change anything
    stats.decrement("ok", "fakehost")

# Generated at 2022-06-12 21:52:12.921701
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # constructor
    instance = AggregateStats()
    # set some values
    instance.increment('changed', 'myserver')
    instance.increment('rescued', 'myserver')
    instance.increment('ok', 'myserver')
    instance.increment('ok', 'myserver2')
    # decrement
    instance.decrement('changed', 'myserver')
    instance.decrement('rescued', 'myserver')
    instance.decrement('ok', 'myserver')
    instance.decrement('ok', 'myserver2')
    # test
    assert instance.changed['myserver'] == 0
    assert instance.rescued['myserver'] == 0
    assert instance.ok['myserver'] == 0
    assert instance.ok['myserver2'] == 0

# Generated at 2022-06-12 21:52:20.385464
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    instance = AggregateStats()
    possible_what_to_decrement_1 = ['ok', 'failures', 'dark', 'changed',
        'skipped', 'rescued', 'ignored']
    possible_what_to_decrement_2 = 'what'
    # Test with host in the particular statistic
    for what in possible_what_to_decrement_1:
        host = 'test_host'
        setattr(instance, what, {host: 1})
        instance.decrement(what, host)
        assert getattr(instance, what).get(host, 0) == 0
    # Test with host not in the particular statistic
    for what in possible_what_to_decrement_1:
        host = 'other_host'
        setattr(instance, what, {})
        instance.dec

# Generated at 2022-06-12 21:52:23.365761
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate_stats = AggregateStats()
    aggregate_stats.ok['localhost'] = 1
    aggregate_stats.decrement('ok', 'localhost')
    assert 0 == aggregate_stats.ok['localhost']
    aggregate_stats.decrement('ok', 'localhost')
    assert 0 == aggregate_stats.ok['localhost']

# Generated at 2022-06-12 21:52:27.348734
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.processed = {'test': 1}
    stats.ignored = {'test': 1}
    stats.decrement('ignored', 'test')
    assert stats.ignored['test'] == 0
    assert stats.processed == {'test': 1}


# Generated at 2022-06-12 21:52:33.895582
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    host = 'test'
    stats.increment('ok', host)
    stats.increment('ok', host)
    assert (len(stats.ok) == 1 and stats.ok[host] == 2)
    stats.increment('ok', host)
    assert (len(stats.ok) == 1 and stats.ok[host] == 3)
    stats.decrement('ok', host)
    assert (len(stats.ok) == 1 and stats.ok[host] == 2)
    stats.decrement('ok', host)
    assert (len(stats.ok) == 1 and stats.ok[host] == 1)
    stats.decrement('ok', host)
    assert (len(stats.ok) == 1 and stats.ok[host] == 0)
    stats.decre

# Generated at 2022-06-12 21:52:39.031346
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('dark', 'mytesthost')
    assert stats.dark.get('mytesthost', 0) == 0

    stats.dark['mytesthost'] = 2
    stats.decrement('dark', 'mytesthost')
    assert stats.dark.get('mytesthost', 0) == 1



# Generated at 2022-06-12 21:52:43.342198
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'host1')
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 0

    stats.increment('ok', 'host1')
    stats.decrement('ok', 'host1')
    stats.decrement('ok', 'host1')
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 0

# Generated at 2022-06-12 21:52:50.463992
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    __valid_stats = ['ok', 'failures', 'dark', 'changed', 'skipped', 'rescued', 'ignored']

    for stat in __valid_stats:
        test_stats = AggregateStats()
        # _run is the default host for global stats
        test_stats._run_start = True
        test_stats.decrement(stat, '_run')
        assert test_stats.__dict__[stat]['_run'] == 0
        test_stats.decrement(stat, '_run')
        assert test_stats.__dict__[stat]['_run'] == 0
