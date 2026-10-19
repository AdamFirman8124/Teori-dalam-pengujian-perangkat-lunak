

# Generated at 2022-06-12 21:51:23.262529
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    plays = [
        Play().load({
            'name': 'test play 1',
            'hosts': 'all',
            'gather_facts': 'no',
            'tasks': [
                Task().load({
                    'name': 'test task 1',
                    'unreachable': True
                })
            ]
        })
    ]

    stats = AggregateStats()
    stats.increment('dark', 'test_host_1')
    stats.increment('dark', 'test_host_2')
    stats.increment('ok', 'test_host_1')
    stats.increment('ok', 'test_host_2')
    stats.increment('ok', 'test_host_1')

# Generated at 2022-06-12 21:51:28.536917
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    stats = AggregateStats()
    assert 'host1' not in stats.processed
    assert 'host1' not in stats.failures
    stats.increment('failures', 'host1')
    assert 'host1' in stats.processed
    assert 'host1' in stats.failures
    assert stats.processed['host1'] == 1
    assert stats.failures['host1'] == 1
    stats.increment('failures', 'host1')
    assert stats.processed['host1'] == 1
    assert stats.failures['host1'] == 2
    stats.increment('processed', 'host2')
    assert 'host2' in stats.processed
    assert stats.processed['host2'] == 1


# Generated at 2022-06-12 21:51:29.691893
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    stats = AggregateStats()
    stats.increment(stats, "dark", "localhost")
    assert stats.dark["localhost"] == 1


# Generated at 2022-06-12 21:51:33.322090
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'test')
    assert stats.ok['test'] == 1
    stats.decrement('ok', 'test')
    assert stats.ok['test'] == 0


# Generated at 2022-06-12 21:51:43.903331
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregatestats = AggregateStats()
    aggregatestats.ignored = {'test': 5}
    aggregatestats.decrement('ignored', 'test')
    assert aggregatestats.ignored == {'test': 4}
    aggregatestats.decrement('ignored', 'test')
    assert aggregatestats.ignored == {'test': 3}
    aggregatestats.decrement('ignored', 'test')
    assert aggregatestats.ignored == {'test': 2}
    aggregatestats.decrement('ignored', 'test')
    assert aggregatestats.ignored == {'test': 1}
    aggregatestats.decrement('ignored', 'test')
    assert aggregatestats.ignored == {'test': 0}
    aggreg

# Generated at 2022-06-12 21:51:50.071387
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    stats = AggregateStats()
    assert stats.ok == {}
    stats.increment('ok', '127.0.0.1')
    assert stats.ok == {'127.0.0.1': 1}
    stats.increment('ok', '127.0.0.1')
    assert stats.ok == {'127.0.0.1': 2}
    assert stats.processed == {'127.0.0.1': 1}


# Generated at 2022-06-12 21:51:53.621356
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    ''' test_AggregateStats_decrement '''
    agg = AggregateStats()
    agg.ok['host1'] = 1
    agg.decrement('ok', 'host1')
    if agg.ok['host1'] != 0:
        raise AssertionError("Bug in decrement")

# Generated at 2022-06-12 21:51:59.815530
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 0
    stats.increment('ok', 'host1')
    assert stats.ok['host1'] == 1
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 0

    stats.increment('ok', 'host2')
    assert stats.ok['host2'] == 1
    stats.decrement('ok', 'host2')
    assert stats.ok['host2'] == 0
    stats.decrement('ok', 'host2')
    assert stats.ok['host2'] == 0

# Generated at 2022-06-12 21:52:04.169522
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    ag = AggregateStats()
    ag.decrement('ok', 'host1')
    assert ag.ok['host1'] == 0
    ag.ok['host1'] = 1
    ag.decrement('ok', 'host1')
    assert ag.ok['host1'] == 0


# Generated at 2022-06-12 21:52:13.365407
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate = AggregateStats()
    stats = {
        'changed': 3,
        'failures': 0,
        'ignored': 0,
        'ok': 2,
        'processed': 1,
        'rescued': 0,
        'skipped': 0,
        'dark': 0
    }
    host = 'test_host'
    for key, value in stats.items():
        setattr(aggregate, key, {host: value})
    assert aggregate.ok[host] == stats['ok']
    aggregate.decrement('ok', host)
    assert aggregate.ok[host] == stats['ok'] - 1

    # test decrementing too much
    aggregate.decrement('failures', host)
  

# Generated at 2022-06-12 21:52:23.266153
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    aggregateStats = AggregateStats()
    aggregateStats.update_custom_stats('foo', 'bar')
    aggregateStats.update_custom_stats('foo2', 'bar2')
    aggregateStats.update_custom_stats('foo.bar', 1)
    aggregateStats.update_custom_stats('foo.bar', [1,2], host='_run')
    aggregateStats.update_custom_stats('foo.bar', [3,4], host='_run')
    aggregateStats.update_custom_stats('foo.bar', {'a':4})
    aggregateStats.update_custom_stats('foo.bar', {'b':6}, host='_run')
    aggregateStats.update_custom_stats('foo.bar', {'a':4, 'b':5, 'c':6})

# Generated at 2022-06-12 21:52:25.015900
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    result = AggregateStats()
    result.skipped['all'] = 5

    result.decrement('skipped', 'all')

    assert result.skipped['all'] == 4

# Generated at 2022-06-12 21:52:30.390728
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    aggregate_stats = AggregateStats()

    assert '_run' not in aggregate_stats.custom

    aggregate_stats.update_custom_stats('what', 'what')
    assert '_run' in aggregate_stats.custom
    assert aggregate_stats.custom['_run'] == {'what': 'what'}

    aggregate_stats.update_custom_stats('what', 'what')
    assert aggregate_stats.custom['_run'] == {'what': 'what'}

    aggregate_stats.update_custom_stats('what', {'what': 'what'})
    assert aggregate_stats.custom['_run'] == {'what': {'what': 'what'}}

    aggregate_stats.update_custom_stats('what', [1, 2, 3])

# Generated at 2022-06-12 21:52:35.546826
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    aggregate = AggregateStats()
    aggregate.set_custom_stats('foo', {'a': 1, 'c': 2}, 'host')
    aggregate.update_custom_stats('foo', {'a': 2, 'b': 1}, 'host')
    assert aggregate.custom.get('host').get('foo') == {'a': 3, 'b': 1, 'c': 2}


# Generated at 2022-06-12 21:52:43.932971
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    stats.update_custom_stats('custom_stats', 1)
    assert stats.custom['_run']['custom_stats'] == 1
    stats.update_custom_stats('custom_stats', 2)
    assert stats.custom['_run']['custom_stats'] == 3
    # Pass a host to make sure we don't crash with a key error
    stats.update_custom_stats('custom_stats', 3, 'localhost')
    assert stats.custom['localhost']['custom_stats'] == 3
    # Verify we can add multiple custom stats if we pass a host
    stats.update_custom_stats('custom_stats2', 1, 'localhost')
    assert stats.custom['localhost']['custom_stats2'] == 1

# Generated at 2022-06-12 21:52:52.649325
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate = AggregateStats()
    aggregate.ok = {'host1': 1, 'host2': 2}
    aggregate.processed = {'host1': 1, 'host2': 1}

    assert aggregate.ok['host1'] == 1
    assert aggregate.ok['host2'] == 2

    aggregate.decrement('ok', 'host1')

    assert aggregate.ok['host1'] == 0
    assert aggregate.processed['host1'] == 0
    assert aggregate.ok['host2'] == 2

    try:
        aggregate.decrement('ok', 'host1')
    except KeyError:
        assert True

    try:
        aggregate.decrement('ok', 'host_unknown')
    except KeyError:
        assert True

# Generated at 2022-06-12 21:52:55.245252
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregateStats = AggregateStats()
    aggregateStats.ignored = {'test': 5}
    aggregateStats.decrement('ignored', 'test')
    assert aggregateStats.ignored['test'] == 4

# Generated at 2022-06-12 21:53:03.511335
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    aggregate = AggregateStats()
    aggregate.update_custom_stats(
        'test_string',
        'aa'
    )
    aggregate.update_custom_stats(
        'test_string',
        'bb'
    )
    assert aggregate.custom['_run']['test_string'] == 'aabb'

    aggregate.update_custom_stats(
        'test_list',
        ['aa', 'bb']
    )
    aggregate.update_custom_stats(
        'test_list',
        ['cc', 'dd']
    )
    assert aggregate.custom['_run']['test_list'] == ['aa', 'bb', 'cc', 'dd']

    aggregate.update_custom_stats(
        'test_dict',
        {'aa': 'bb'}
    )
    aggregate.update_

# Generated at 2022-06-12 21:53:10.325657
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # Failures: test_AggregateStats_decrement: testcases.test_stats.test_AggregateStats_decrement.<locals>.decr_fixture
    # Failures: test_AggregateStats_decrement: testcases.test_stats.test_AggregateStats_decrement.<locals>.decr_fixture2
    import pytest
    # Initialize `what` and `host`
    what_init = None
    host_init = None
    as_decrement = AggregateStats()
    # Initialize `what` and `host`
    as_decrement.failures = {'foo': 0}
    what_init = 'failures'
    host_init = 'foo'
    if not what_init == 'failures':
        return False

# Generated at 2022-06-12 21:53:15.992090
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', '127.0.0.1')
    stats.decrement('ok', '127.0.0.1')
    stats.decrement('changed', '127.0.0.1')
    stats.decrement('ok', '127.0.0.2')
    assert stats.ok['127.0.0.1'] == 0
    assert stats.ok['127.0.0.2'] == 0
    assert stats.changed['127.0.0.1'] == 0
    assert '127.0.0.2' not in stats.changed
