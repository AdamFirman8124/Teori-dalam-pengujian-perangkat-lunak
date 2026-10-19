

# Generated at 2022-06-12 21:51:12.873781
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    # Initialize an AggregateStats object
    as_obj = AggregateStats()

    # Initialize a hostname
    host = "some.host.name"

    # Initialize a statistic we want to track
    what = "ok"

    # Call the method increment of class AggregateStats
    as_obj.increment(what, host)

    return as_obj.ok[host] == 1

# Generated at 2022-06-12 21:51:17.491907
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    print('Testing method decrement of class AggregateStats...')
    stats = AggregateStats()
    stats.ok['127.0.0.1'] = 1
    stats.decrement('ok', '127.0.0.1')
    print('ok = {}'.format(stats.ok))
    print('PASSED')
    stats.decrement('ok', '127.0.0.1')
    print('ok = {}'.format(stats.ok))
    print('PASSED')


# Generated at 2022-06-12 21:51:26.047255
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # create an instance of AggregateStats
    astats = AggregateStats()
    astats.increment('ok', 'host-0')
    astats.decrement('ok', 'host-0')
    assert astats.ok.get('host-0', None) == 0
    assert astats.ok.get('host-1', None) == None
    astats.decrement('ok', 'host-0')
    assert astats.ok.get('host-0', None) == 0
    assert astats.ok.get('host-1', None) == None
    astats.decrement('failures', 'host-0')
    assert astats.failures.get('host-0', None) == 0
    assert astats.failures.get('host-1', None) == None
    astats.decre

# Generated at 2022-06-12 21:51:36.020962
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    stats.update_custom_stats('toto', 1)
    assert stats.custom['_run']['toto'] == 1
    stats.update_custom_stats('toto', 2)
    assert stats.custom['_run']['toto'] == 3
    stats.update_custom_stats('toto', 3)
    assert stats.custom['_run']['toto'] == 6
    stats.update_custom_stats('toto', -1)
    assert stats.custom['_run']['toto'] == 5
    stats.update_custom_stats('toto', -5)
    assert stats.custom['_run']['toto'] == 0
    stats.update_custom_stats('toto', -5)

# Generated at 2022-06-12 21:51:43.253321
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    agg_stats = AggregateStats()
    agg_stats.decrement('custom', '_test_host')
    assert agg_stats.custom['_test_host'] == 0

    agg_stats.custom['_test_host'] = 2
    agg_stats.decrement('custom', '_test_host')
    assert agg_stats.custom['_test_host'] == 1

    agg_stats.custom['_test_host'] = -1
    agg_stats.decrement('custom', '_test_host')
    assert agg_stats.custom['_test_host'] == 0



# Generated at 2022-06-12 21:51:52.769605
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    aggr = AggregateStats()
    def get_custom_stats(which, host=None):
        return aggr.custom[host][which]

    # 1. update_custom_stats() with nested dicts
    d1 = {'k1':{'k11':{'k111':'v111'}}}
    d2 = {'k1':{'k12':'v12'}}
    d3 = {'k2':'v2'}
    d4 = {'k1':{'k11':{'k112':'v112'}}}
    aggr.set_custom_stats('foo',d1)
    aggr.update_custom_stats('foo',d2)
    aggr.update_custom_stats('foo',d3)
    aggr.update_custom_stats('foo',d4)

# Generated at 2022-06-12 21:51:59.435843
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    from collections import namedtuple
    test = namedtuple('test', ('what host'))
    tests = [
        test(what='ok', host='localhost'),
        test(what='ignored', host='localhost'),
        test(what='changed', host='')
    ]
    stats = AggregateStats()
    stats.ok['localhost'] = 1
    stats.increment('ok', 'localhost')
    stats.increment('ignored', 'localhost')
    stats.increment('changed', '')

    for t in tests:
       stats.decrement(t.what, t.host)
       assert stats.__dict__[t.what][t.host] == 0


# Generated at 2022-06-12 21:52:07.815143
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    asobj = AggregateStats()
    asobj.increment("ok", "localhost")
    asobj.increment("ok", "localhost")
    assert asobj.ok["localhost"] == 2

    asobj.decrement("ok", "localhost")
    assert asobj.ok["localhost"] == 1

    asobj.decrement("ok", "localhost")
    assert asobj.ok["localhost"] == 0

    try:
        asobj.decrement("ok", "localhost")
    except KeyError:
        pass
    else:
        raise AssertionError("KeyError not raised")


# Generated at 2022-06-12 21:52:12.844450
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    assert stats.decrement('failures', 'host-a') == None
    assert stats.failures == {'host-a': 0}
    stats.increment('failures', 'host-a')
    assert stats.decrement('failures', 'host-a') == None
    assert stats.failures == {'host-a': 0}


# Generated at 2022-06-12 21:52:18.964393
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    aggregate = AggregateStats()
    aggregate.increment('ok', 'testhost')

    assert aggregate.ok == {'testhost': 1}
    assert aggregate.processed == {'testhost': 1}

    aggregate.increment('ok', 'testhost')

    assert aggregate.ok == {'testhost': 2}
    assert aggregate.processed == {'testhost': 1}

    aggregate.increment('ok', 'testhost2')

    assert aggregate.ok == {'testhost': 2, 'testhost2': 1}
    assert aggregate.processed == {'testhost': 1, 'testhost2': 1}

    aggregate.increment('ok', 'testhost2')

    assert aggregate.ok == {'testhost': 2, 'testhost2': 2}

# Generated at 2022-06-12 21:52:22.876900
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()

    stats.increment('ok', 'localhost')
    stats.increment('ok', 'localhost')

    stats.decrement('ok', 'localhost')

    assert stats.ok['localhost'] == 1


# Generated at 2022-06-12 21:52:25.821487
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # GIVEN
    stats = AggregateStats()
    stats.increment("skipped", "example.com")

    # WHEN
    stats.decrement("skipped", "example.com")

    # THEN
    assert stats.skipped["example.com"] == 0

# vim: set filetype=python ts=4 sw=4 et si

# Generated at 2022-06-12 21:52:30.952128
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'localhost')
    stats.increment('ok', 'localhost')
    stats.increment('ignored', 'localhost')
    assert stats.ok['localhost'] == 2
    assert stats.ignored['localhost'] == 1
    stats.decrement('ok', 'localhost')
    stats.decrement('ignored', 'localhost')
    assert stats.ok['localhost'] == 1
    assert stats.ignored['localhost'] == 0
    stats.decrement('ignored', 'localhost')
    assert stats.ignored['localhost'] == 0
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0



# Generated at 2022-06-12 21:52:35.583073
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.ok['host'] = 2
    assert stats.ok['host'] == 2

    stats.decrement('ok', 'host')
    assert stats.ok['host'] == 1

    stats.decrement('ok', 'host')
    assert stats.ok['host'] == 0

    # Test KeyError
    stats.decrement('ignored', 'host')


# Generated at 2022-06-12 21:52:40.558950
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    agg = AggregateStats()
    agg.decrement('ok', 'localhost')
    assert agg.ok['localhost'] == 0
    agg.ok['localhost'] = 3
    agg.decrement('ok', 'localhost')
    assert agg.ok['localhost'] == 2
    agg.decrement('ok', 'localhost')
    assert agg.ok['localhost'] == 1

# Generated at 2022-06-12 21:52:45.012048
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.ok['127.0.0.1'] = 2
    stats.failures['127.0.0.1'] = 3
    stats.decrement("ok", "127.0.0.1")
    stats.decrement("failures", "127.0.0.1")
    res = stats.custom.get("127.0.0.1")
    if res['failures'] != 2 and res['ok'] != 1:
        raise ValueError("AggregateStats decrement fail")



# Generated at 2022-06-12 21:52:54.424824
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    astats = AggregateStats()

    astats.increment('ok', 'localhost')
    astats.increment('ok', 'localhost')
    astats.increment('ok', 'localhost')
    astats.increment('ok', 'localhost')
    astats.increment('ok', 'localhost')
    astats.increment('ok', 'localhost')
    astats.increment('ok', 'localhost')
    astats.increment('ok', 'localhost')

    assert astats.ok['localhost'] == 8

    astats.decrement('ok', 'localhost')
    assert astats.ok['localhost'] == 7

    astats.decrement('ok', 'localhost')
    assert astats.ok['localhost'] == 6

    astats.decrement('ok', 'localhost')

# Generated at 2022-06-12 21:52:59.460594
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    from ansible.utils.vars import combine_vars
    a = AggregateStats()

    a.ok = { "foo": 1, "bar": 2 }
    a.decrement("ok", "foo")
    a.decrement("ok", "foo")
    a.decrement("ok", "bar")

    assert a.ok["foo"] == 0
    assert a.ok["bar"] == 1


# Generated at 2022-06-12 21:53:06.725786
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # Create the class
    stats = AggregateStats()

    # Set the dictionary
    dic = {}
    dic['host1'] = 3
    dic['host2'] = 0
    dic['host3'] = 1
    dic['host4'] = 3
    stats.ok = dic.copy()

    # Test the decrement method
    stats.decrement('ok', 'host1')
    assert stats.ok == {'host1': 2, 'host2': 0, 'host3': 1, 'host4': 3}
    stats.decrement('ok', 'host2')
    assert stats.ok == {'host1': 2, 'host2': 0, 'host3': 1, 'host4': 3}
    stats.decrement('ok', 'host3')

# Generated at 2022-06-12 21:53:10.111254
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'localhost')
    assert stats.ok['localhost'] == 1
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0
    # Now decrement when there is no value
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0