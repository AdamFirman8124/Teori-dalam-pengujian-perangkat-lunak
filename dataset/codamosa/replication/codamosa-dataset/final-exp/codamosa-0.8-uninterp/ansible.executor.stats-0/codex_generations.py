

# Generated at 2022-06-12 21:51:18.324920
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('dark', 'test_host')
    assert stats.dark['test_host'] == 0



# Generated at 2022-06-12 21:51:25.335988
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()

    stats.decrement("ok", "host1")
    assert stats.ok["host1"] == 0

    stats.ok["host1"] = 2
    stats.decrement("ok", "host1")
    assert stats.ok["host1"] == 1

    stats.ok["host1"] = -1
    stats.decrement("ok", "host1")
    assert stats.ok["host1"] == 0

    #with pytest.raises(KeyError):
    #    stats.ok["host1"] = -2
    #    stats.decrement("ok", "host1")


# Generated at 2022-06-12 21:51:32.631600
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    '''Tests for decrement method of class AggregateStats'''
    aggregate_stats = AggregateStats()
    host = "test_host"
    aggregate_stats.increment('ok', host)
    assert aggregate_stats.ok.get(host, 0) == 1
    aggregate_stats.decrement('ok', host)
    assert aggregate_stats.ok.get(host, 0) == 0
    aggregate_stats.decrement('ok', host)
    assert aggregate_stats.ok.get(host, 0) == 0
    # Nothing should have changed
    assert aggregate_stats.processed.get(host, 0) == 1

# Generated at 2022-06-12 21:51:37.524044
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    test = AggregateStats()
    test.increment('ok', '127.0.0.1')
    test.decrement('ok', '127.0.0.1')
    assert test.ok['127.0.0.1'] == 0
    assert test.ok['127.0.0.2'] == 0

# Generated at 2022-06-12 21:51:47.543619
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    import unittest

    class t_AggregateStats(unittest.TestCase):

        def test_AggregateStats_decrement_failures_host(self):
            a = AggregateStats()
            a.increment('failures', 'host1')
            a.increment('failures', 'host2')
            a.increment('failures', 'host1')

            a.decrement('failures', 'host1')
            self.assertEqual(a.failures, {'host1': 1, 'host2': 1})

        def test_AggregateStats_decrement_failures_host_none(self):
            a = AggregateStats()
            a.increment('failures', 'host1')
            a.increment('failures', 'host2')

# Generated at 2022-06-12 21:51:55.901969
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    sts = AggregateStats()
    sts.update_custom_stats('some_var', 1, 'host1')
    assert sts.custom['host1']['some_var'] == 1
    sts.update_custom_stats('some_var', {'key': 42}, 'host1')
    assert sts.custom['host1']['some_var']['key'] == 42
    sts.update_custom_stats('some_var', 10, 'host1')
    assert sts.custom['host1']['some_var'] == 52
    sts.update_custom_stats('some_var', 1)
    assert sts.custom['_run']['some_var'] == 1
    sts.update_custom_stats('some_var', 'abc')

# Generated at 2022-06-12 21:51:59.243352
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    foo = AggregateStats()

    # negative cases
    foo.decrement('ok', 'localhost')
    assert foo.ok['localhost'] == 0

    # positive case
    foo.ok['localhost'] = 5
    foo.decrement('ok', 'localhost')
    assert foo.ok['localhost'] == 4



# Generated at 2022-06-12 21:52:03.195631
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    """
    Verify decrement method of class AggregateStats
    """
    aggregate_stats = AggregateStats()
    aggregate_stats.decrement('failures', 'Task1')
    expected_results = {'Task1': 0}
    assert aggregate_stats.failures == expected_results

# Generated at 2022-06-12 21:52:08.421108
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment("test", "fake")
    assert stats.test["fake"] == 1
    stats.decrement("test", "fake")
    assert stats.test["fake"] == 0
    stats.decrement("test", "fake")
    assert stats.test["fake"] == 0
    assert stats.test.get("fake", 0) == 0

# Generated at 2022-06-12 21:52:16.461714
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    test_stats = AggregateStats()

    # Test decrement of empty dict
    test_stats.decrement('ok', 'host1')
    assert test_stats.ok['host1'] == 0

    # Test decrement of dict with 1 element
    test_stats.increment('ok', 'host1')
    test_stats.decrement('ok', 'host1')
    assert test_stats.ok['host1'] == 0

    # Test decrement of dict with 2 elements
    test_stats.increment('ok', 'host1')
    test_stats.increment('ok', 'host1')
    test_stats.decrement('ok', 'host1')
    assert test_stats.ok['host1'] == 1

    # Test decrement of dict with likely negative value

# Generated at 2022-06-12 21:52:20.190366
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.ok = {'localhost': 10}
    stats.decrement('ok', 'localhost')
    assert stats.ok == {'localhost': 9}


# Generated at 2022-06-12 21:52:24.751021
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    a = AggregateStats()
    a.set_custom_stats(3,4,5)
    assert a.custom == {'_run': {3: 4, 5: 1}}
    a.set_custom_stats(5,5,5)
    assert a.custom == {'_run': {3: 4, 5: 5}} # set_custom_stats will update
    a.set_custom_stats(3,6,5)
    assert a.custom == {'_run': {3: 6, 5: 5}}

# Generated at 2022-06-12 21:52:30.188609
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()

    stats.ok = {'host1': 1, 'host2': 1, 'host3': 0}
    stats.skipped = {'host1': 1, 'host2': 1, 'host3': 1}
    stats.dark = {'host1': 1, 'host2': 1}
    stats.ignored = {'host1': 1, 'host2': 1}

    for what in ('ok', 'skipped', 'dark', 'ignored'):
        for host in ('host1', 'host2', 'host3'):
            stats.decrement(what, host)

    assert stats.ok == {'host1': 0, 'host2': 0, 'host3': 0}

# Generated at 2022-06-12 21:52:34.358973
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment("ok", 'localhost')
    assert stats.ok['localhost'] == 1, 'ok is incremented by 1'
    stats.decrement("ok", 'localhost')
    assert stats.ok['localhost'] == 0, 'ok is decremented by 1'

# Generated at 2022-06-12 21:52:41.482455
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment("ok", "test_host")
    stats.increment("ok", "test_host")
    assert stats.ok["test_host"] == 2

    stats.decrement("ok", "test_host")
    assert stats.ok["test_host"] == 1
    stats.decrement("ok", "test_host")
    assert stats.ok["test_host"] == 0

    # When decremented below 0, set to 0
    stats.decrement("ok", "test_host")
    assert stats.ok["test_host"] == 0

# Generated at 2022-06-12 21:52:50.351261
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    import unittest

    class TestAggregateStats(unittest.TestCase):
        def test_decrement_host_ok(self):
            aggr = AggregateStats()
            aggr.ok['host1'] = 1
            aggr.decrement('ok', 'host1')
            self.assertEqual(0, aggr.ok['host1'])

        def test_decrement_host_failures(self):
            aggr = AggregateStats()
            aggr.failures['host1'] = 1
            aggr.decrement('failures', 'host1')
            self.assertEqual(0, aggr.failures['host1'])

        def test_decrement_host_dark(self):
            aggr = AggregateStats()

# Generated at 2022-06-12 21:52:59.103772
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'test')
    stats.increment('ok', 'test')
    stats.decrement('ok', 'test')
    if stats.ok['test'] != 1:
        raise AssertionError('decrement broken')
    # make sure decrementing 0 doesn't raise an error
    stats.decrement('ok', 'test')
    # make sure decrementing a value that doesn't exist doesn't raise an error
    stats.decrement('ok', 'not a host')
    stats.increment('ok', 'not a host')
    stats.decrement('ok', 'not a host')

    stats.increment('failures', 'test')
    stats.increment('failures', 'test')
    stats.decrement('failures', 'test')

# Generated at 2022-06-12 21:53:06.423670
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()

    stats.update_custom_stats('dict_key', {}, 'some_host')
    assert stats.custom['some_host']['dict_key'] == {}

    stats.update_custom_stats('dict_key', {'a': 'b'}, 'some_host')
    assert stats.custom['some_host']['dict_key']['a'] == 'b'

    stats.update_custom_stats('dict_key', {'c': 'd'}, 'some_host')
    assert stats.custom['some_host']['dict_key']['c'] == 'd'

    stats.update_custom_stats('int_key', int(100), 'some_host')
    assert stats.custom['some_host']['int_key'] == int(100)

    stats

# Generated at 2022-06-12 21:53:08.970495
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():

    aggregate = AggregateStats()

    # dictionary as what
    what = {"test_key": "test_value"}
    aggregate.update_custom_stats("test", what, "test_host")

# Generated at 2022-06-12 21:53:12.543953
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    s = AggregateStats()
    s.increment('ok', 'host1')
    assert(s.ok['host1'] == 1)
    s.decrement('ok','host1')
    assert(s.ok['host1'] == 0)


# Generated at 2022-06-12 21:53:19.661299
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aw = AggregateStats()
    aw.ok['host'] = 1

    # no error should be raised
    aw.decrement('ok', 'host')
    aw.decrement('ok', 'host')
    aw.decrement('ok', 'host')

    assert aw.ok['host'] == 0


# Generated at 2022-06-12 21:53:22.787953
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.ok = {'test': 1}
    stats.decrement('ok', 'test')
    assert stats.ok['test'] == 0

# Generated at 2022-06-12 21:53:29.547695
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate = AggregateStats()
    aggregate.ok = {'host1': 1, 'host2': 0, 'host3': 1, 'host4': 3}
    aggregate.decrement('ok', 'host1')
    aggregate.decrement('ok', 'host2')
    aggregate.decrement('ok', 'host3')
    aggregate.decrement('ok', 'host4')
    assert aggregate.ok == {'host1': 0, 'host3': 0, 'host4': 2}
    assert aggregate.ok.get('host2', 1) == 0

# Generated at 2022-06-12 21:53:34.152495
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    test_result = True
    # test when key exists
    stats = AggregateStats()
    stats.skipped['host'] = 2
    stats.decrement('skipped', 'host')
    if stats.skipped['host'] != 1:
        test_result = False
    # test when key doesn't exists
    stats = AggregateStats()
    stats.decrement('skipped', 'host')
    if stats.skipped['host'] != 0:
        test_result = False
    return test_result

# Generated at 2022-06-12 21:53:37.814819
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'test_host')
    assert stats.ok['test_host'] == 1
    stats.decrement('ok', 'test_host')
    assert stats.ok['test_host'] == 0
    stats.decrement('ok', 'test_host')
    assert stats.ok['test_host'] == 0

if __name__ == '__main__':
    test_AggregateStats_decrement()

# Generated at 2022-06-12 21:53:42.964843
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    agg = AggregateStats()
    agg.increment("ok", "127.0.0.1")
    agg.increment("ok", "127.0.0.1")
    assert agg.ok["127.0.0.1"] == 2
    agg.decrement("ok", "127.0.0.1")
    assert agg.ok["127.0.0.1"] == 1

# Generated at 2022-06-12 21:53:53.052192
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    from ansible.playbook.play import Play

    play = Play.load(None, dict(
        name={'all': {}},
        hosts='all',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='pause', args=dict(seconds=1)), register='ok_result'),
            dict(action=dict(module='pause', args=dict(seconds=1)), register='changed_result'),
            dict(action=dict(module='pause', args=dict(seconds=1)), register='failed_result', ignore_errors='yes'),
            dict(action=dict(module='pause', args=dict(seconds=1)), register='unreachable_result', ignore_unreachable='yes')
        ]
    ), play_context=dict())

    host = 'localhost'
    stats = AggregateStats()

   

# Generated at 2022-06-12 21:54:00.936217
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'hostA')
    stats.decrement('ok', 'hostA')
    assert stats.ok['hostA'] == 0

    stats.increment('ok', 'hostB')
    stats.increment('ok', 'hostB')
    stats.decrement('ok', 'hostB')
    assert stats.ok['hostB'] == 1

    stats.increment('ok', 'hostC')
    stats.decrement('ok', 'hostC')
    assert stats.ok['hostC'] == 0


# Generated at 2022-06-12 21:54:02.616734
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'localhost')
    assert stats.ok.get('localhost') == 0


# Generated at 2022-06-12 21:54:05.862546
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # Preparation
    stats = AggregateStats()
    # Expected values
    expected_ok = {'test':0}
    # Actual values
    stats.ok = {'test':1}
    stats.decrement('ok', 'test')
    actual_ok = stats.ok
    # End test
    assert actual_ok == expected_ok
