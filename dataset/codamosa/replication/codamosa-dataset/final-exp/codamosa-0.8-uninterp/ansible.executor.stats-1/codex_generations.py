

# Generated at 2022-06-12 21:51:10.497796
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    my_variable = AggregateStats()
    my_variable.increment('failures', 'localhost')
    assert my_variable.failures['localhost'] == 1

# Generated at 2022-06-12 21:51:13.766859
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    stats = AggregateStats()
    stats.increment('dark', 'host1')
    stats.increment('dark', 'host2')
    stats.increment('dark', 'host1')

    assert stats.dark['host1'] == 2
    assert stats.dark['host2'] == 1

# Generated at 2022-06-12 21:51:19.106027
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.failures = {'a':1}

    # Call decrement with parameter what = 'failures' and host = 'a'
    stats.decrement('failures', 'a')
    assert stats.failures['a'] == 0

    # Call decrement with parameter what = 'failures' and host = 'b'
    stats.decrement('failures', 'b')
    assert stats.failures['b'] == 0


# Generated at 2022-06-12 21:51:25.699163
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    print('test start')
    stats = AggregateStats()
    stats.increment('ok', 'host1')
    stats.increment('ok', 'host1')
    stats.increment('ok', 'host1')
    stats.increment('ok', 'host2')
    stats.increment('ok', 'host2')
    stats.increment('ok', 'host2')
    assert stats.ok['host1'] == 3
    assert stats.ok['host2'] == 3
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 2
    assert stats.ok['host2'] == 3


# Generated at 2022-06-12 21:51:34.888456
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()

    # Setting what to some arbitrary value
    stats.changed= {"testhost": 10}
    # Calling the method
    stats.decrement("changed", "testhost")
    # Asserting that it has been decremented once
    assert stats.changed["testhost"] == 9

    # Calling the method again
    stats.decrement("changed", "testhost")
    # Asserting that it has been decremented once again
    assert stats.changed["testhost"] == 8

    # Trying to decrement from zero
    stats.changed = {"testhost": 0}
    # Calling the method
    stats.decrement("changed", "testhost")
    # Asserting that it has not been decremented
    assert stats.changed["testhost"] == 0

    # Trying to decrement from an unset counter


# Generated at 2022-06-12 21:51:45.739150
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    ag = AggregateStats()
    ag.update_custom_stats('custom', {'a':1})
    ag.update_custom_stats('custom', {'b':2})
    assert ag.custom['_run']['custom'] == {'a':1, 'b':2}

    ag.update_custom_stats('custom', {'a':2})
    assert ag.custom['_run']['custom'] == {'a':2, 'b':2}

    ag.update_custom_stats('custom', {'a':{'b':[1]}})
    assert ag.custom['_run']['custom'] == {'a': {'b': [1]}, 'b': 2}

    ag.update_custom_stats('custom', [1])
    assert ag.custom['_run']['custom']

# Generated at 2022-06-12 21:51:49.062951
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'testhost')
    stats.decrement('ok', 'testhost')

    assert stats.ok['testhost'] == 0
    assert stats.ok == {'testhost': 0}



# Generated at 2022-06-12 21:51:56.700261
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.ok = {'host1': 1, 'host2': 1}
    stats.decrement('ok', 'host2')
    assert stats.ok == {'host1': 1, 'host2': 0}, "Decrementing not working"
    assert stats.ok['host1'] == 1, "Decremented other wrong host"
    assert stats.ok['host2'] == 0, "Decremented wrong host"
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 0, "Decremented other wrong host"
    stats.decrement('ok', 'host2')
    assert stats.ok['host2'] == 0, "Decremented to negative"



# Generated at 2022-06-12 21:52:02.637411
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():

    obj = AggregateStats()
    host = 'localhost'
    # decrementing an item that does not exist
    obj.decrement('ok', host)
    assert obj.ok[host] == 0

    obj.increment('ok', host)
    assert obj.ok[host] == 1

    # decrementing an item that exist
    obj.decrement('ok', host)
    assert obj.ok[host] == 0

    # decrementing beyond 0
    obj.ok[host] = -5
    obj.decrement('ok', host)
    assert obj.ok[host] == 0

# Generated at 2022-06-12 21:52:10.431446
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggr = AggregateStats()

    # Check that decrement does not modify attributes that don't exist
    aggr.decrement('foo', 'bar')
    assert aggr.foo is None

    # Check that decrement decrease the attributes to 0
    aggr.ok['baz'] = 1
    aggr.decrement('ok', 'baz')
    assert aggr.ok['baz'] == 0

    # Check that decrement decrease the attributes less than 0
    aggr.ok['baz'] = -1
    aggr.decrement('ok', 'baz')
    assert aggr.ok['baz'] == 0

# Generated at 2022-06-12 21:52:15.645263
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    """Test method decrement of class AggregateStats
    """
    stats = AggregateStats()
    stats.processed['host'] = 1
    stats.ok['host'] = 42
    assert stats.ok['host'] == 42

    stats.decrement('ok', 'host')
    assert stats.ok['host'] == 41

    stats.decrement('ok', 'host')
    assert stats.ok['host'] == 40

# Generated at 2022-06-12 21:52:18.074322
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('failures', 'test-host')

    stat_before = stats.failures['test-host']
    stats.decrement('failures', 'test-host')
    stat_after = stats.failures['test-host']

    assert stat_before > stat_after

# Generated at 2022-06-12 21:52:20.496365
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats_obj = AggregateStats()
    stats_obj.increment("ok", "host1")
    stats_obj.decrement("ok", "host1")
    assert stats_obj.ok["host1"] == 0


# Generated at 2022-06-12 21:52:27.030518
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    test_cases = {
        "ok": {0: 1},
        "failures": {0: 0},
        "dark": {0: -1},
        "changed": {0: 0},
        "skipped": {0: 0},
        "rescued": {0: 0},
        "ignored": {0: 0},
    }
    for what, test_case in test_cases.items():
        for res in test_case:
            stats.increment(what, 0)
        for host, num in test_case.items():
            for _ in range(num):
                stats.decrement(what, host)
        assert stats.summarize(0)[what] == res
        for _ in range(res):
            stats.decrement(what, 0)


# Generated at 2022-06-12 21:52:33.710386
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'host1')

    # When value exists
    stats.decrement('ok', 'host1')
    # Check for reference equality as it's a dict
    assert getattr(stats, 'ok')['host1'] == 0

    # When value doesn't exist
    stats.decrement('ok', 'host2')
    # Check for reference equality as it's a dict
    assert getattr(stats, 'ok')['host2'] == 0

    # When value is 0
    stats.decrement('ok', 'host1')
    # Check for reference equality as it's a dict
    assert getattr(stats, 'ok')['host1'] == 0

    # When use a weird value that is below 0
    stats.ok['host1'] = -2
    stats.dec

# Generated at 2022-06-12 21:52:37.505644
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    import mock
    aggregate_stats = AggregateStats()
    aggregate_stats.skipped = {'host': 1}
    aggregate_stats.decrement('skipped', 'host')
    assert aggregate_stats.skipped == {'host': 0}

# Generated at 2022-06-12 21:52:40.799012
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():

    stats = AggregateStats()
    stats.decrement('failures', 'host')
    assert stats.failures['host'] == 0
    stats.failures['host'] = 1
    stats.decrement('failures', 'host')
    assert stats.failures['host'] == 0


# Generated at 2022-06-12 21:52:43.128734
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate_stats = AggregateStats()
    aggregate_stats.ok = {'test_host': 3}
    aggregate_stats.decrement('ok', 'test_host')
    assert aggregate_stats.ok['test_host'] == 2

# Generated at 2022-06-12 21:52:46.010442
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    s = AggregateStats()
    s.decrement('ok', 'host1')
    assert s.ok['host1'] == 0
    s.ok['host1'] = 1
    assert s.ok['host1'] == 1
    s.decrement('ok', 'host1')
    assert s.ok['host1'] == 0


# Generated at 2022-06-12 21:52:50.986207
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
        # Arrange
        aggStats = AggregateStats()
        aggStats.increment("ignored", "localhost")
        aggStats.increment("ignored", "localhost")
        aggStats.increment("dark", "localhost")
        aggStats.increment("dark", "localhost")
        aggStats.increment("dark", "localhost")
        aggStats.increment("dark", "localhost")
        aggStats.increment("ok", "localhost")

        # Act
        aggStats.decrement("ignored", "localhost")

        # Assert
        assert aggStats.ignored["localhost"] == 1

        # Act
        aggStats.decrement("dark", "localhost")

        # Assert
        assert aggStats.dark["localhost"] == 3

        # Act
        aggStats.decrement("ok", "localhost")

        #

# Generated at 2022-06-12 21:53:00.658227
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    agg = AggregateStats()
    # Test aginst starting value of 0
    agg.decrement('ok', 'localhost')
    assert agg.ok['localhost'] == 0
    # Test against starting value of 3
    agg.ok['localhost'] = 3
    agg.decrement('ok', 'localhost')
    assert agg.ok['localhost'] == 2
    # Don't let value go negative
    agg.decrement('ok', 'localhost')
    assert agg.ok['localhost'] == 1
    agg.decrement('ok', 'localhost')
    assert agg.ok['localhost'] == 0
    agg.decrement('ok', 'localhost')
    assert agg.ok['localhost'] == 0

# Generated at 2022-06-12 21:53:02.939664
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    o = AggregateStats()
    o.failures['host1'] = 1
    o.decrement('failures', 'host1')
    assert o.failures['host1'] == 0


# Generated at 2022-06-12 21:53:09.796090
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    def _do_test(what, exp_i, exp_v):
        stats = AggregateStats()
        stats.increment(what, 'myhost')
        stats.decrement(what, 'myhost')
        assert stats.processed == {'myhost': 1}
        _what = getattr(stats, what)
        assert _what == {'myhost': exp_i}
        assert _what[exp_v] == 0

    _do_test('ok', 1, 'myhost')
    _do_test('failures', 1, 'myhost')
    _do_test('dark', 1, 'myhost')
    _do_test('changed', 1, 'myhost')
    _do_test('skipped', 1, 'myhost')

# Generated at 2022-06-12 21:53:14.651785
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    res = AggregateStats()
    res.decrement("ok", "localhost")
    assert res.ok.get("localhost", 0) == 0
    res.ok["localhost"] = 1
    res.decrement("ok", "localhost")
    assert res.ok.get("localhost", 0) == 0
    res.ok["localhost"] = 2
    res.decrement("ok", "localhost")
    assert res.ok.get("localhost", 0) == 1


# Generated at 2022-06-12 21:53:19.379356
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    as_1 = AggregateStats()
    as_1.processed['localhost'] = 1
    as_1.rescued['localhost'] = 10
    as_1.decrement('rescued', 'localhost')
    assert as_1.rescued['localhost'] == 9


# Generated at 2022-06-12 21:53:28.179784
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    s = AggregateStats()
    assert s.ok == {}
    s.increment('ok', 'example.com')
    s.increment('ok', 'example.com')
    assert s.ok == {'example.com': 2}
    s.decrement('ok', 'example.com')
    assert s.ok == {'example.com': 1}
    s.decrement('ok', 'example.com')
    assert s.ok == {'example.com': 0}
    s.decrement('ok', 'example.com')
    assert s.ok == {'example.com': 0}
    s.increment('ok', 'example.com')
    assert s.ok == {'example.com': 1}

# Generated at 2022-06-12 21:53:31.709755
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
  aggregateStats=AggregateStats()
  assert aggregateStats.decrement("failures", "host1") == 0
  aggregateStats.increment("failures", "host1")
  assert aggregateStats.decrement("failures", "host1") == 0
  return True

# Generated at 2022-06-12 21:53:35.513364
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():

    success_stat = AggregateStats()
    error_stat = AggregateStats()
    success_stat.ok['host1'] = 1
    error_stat.ok['host1'] = 0
    success_stat.decrement('ok', 'host1')
    error_stat.decrement('ok', 'host1')
    assert success_stat.ok['host1'] == 0
    assert error_stat.ok['host1'] == 0


# Generated at 2022-06-12 21:53:37.429471
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'test')
    assert (stats.ok['test'] == -1)
    assert (stats.dark['test'] == 0)
    assert (stats.processed['test'] == 1)


# Generated at 2022-06-12 21:53:42.417653
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # Test zero value
    as_ = AggregateStats()

    as_.decrement('failures', 'hostA')
    assert as_.failures['hostA'] == 0

    # Test negative values
    as_.failures['hostA'] = -1
    as_.decrement('failures', 'hostA')
    assert as_.failures['hostA'] == 0

    as_.failures['hostA'] = 0
    as_.decrement('failures', 'hostA')
    assert as_.failures['hostA'] == 0

    # Test positive values
    as_.failures['hostA'] = 1
    as_.decrement('failures', 'hostA')
    assert as_.failures['hostA'] == 0

    as_.failures['hostA'] = 10