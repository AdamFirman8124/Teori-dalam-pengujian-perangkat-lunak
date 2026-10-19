

# Generated at 2022-06-12 21:51:01.588939
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate_stats_object = AggregateStats()
    aggregate_stats_object.decrement('ignored', 'localhost')
    assert aggregate_stats_object.ignored == {'localhost': 0}

# Generated at 2022-06-12 21:51:06.821049
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    '''
    This test case ensure the correct operation of AggregateStats.decrement
    '''
    class FakeHost:
        name = 'fake_host'

    fake_host = FakeHost()
    stats = AggregateStats()
    stats.ok[fake_host.name] = 1
    stats.decrement('ok', fake_host.name)
    assert stats.ok[fake_host.name] == 0
    stats.decrement('ok', fake_host.name)
    assert stats.ok[fake_host.name] == 0

    stats.ok[fake_host.name] = 0
    stats.decrement('ok', fake_host.name)
    assert stats.ok[fake_host.name] == 0



# Generated at 2022-06-12 21:51:16.365097
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    stats.update_custom_stats('test', {'answer': 42}, host='_run')
    assert stats.custom['_run']['test']['answer'] == 42
    stats.update_custom_stats('test', {'answer': 43}, host='_run')
    assert stats.custom['_run']['test']['answer'] == 43
    stats.update_custom_stats('test', {'answer': 'hello'}, host='_run')  # do not override with different type
    assert stats.custom['_run']['test']['answer'] == 43
    stats.update_custom_stats('test', {'answer': 44})
    assert stats.custom['_run']['test']['answer'] == 44
    # stats.custom['_run']['test'][

# Generated at 2022-06-12 21:51:24.060023
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    agg_stats = AggregateStats()
    agg_stats.increment("failures", "localhost")
    agg_stats.increment("failures", "localhost")
    agg_stats.increment("failures", "localhost")

    assert agg_stats.failures["localhost"] == 3
    agg_stats.decrement("failures", "localhost")
    assert agg_stats.failures["localhost"] == 2
    agg_stats.decrement("failures", "localhost")
    assert agg_stats.failures["localhost"] == 1
    agg_stats.decrement("failures", "localhost")
    assert agg_stats.failures["localhost"] == 0


# Generated at 2022-06-12 21:51:31.523307
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    test_stats = AggregateStats()
    test_stats.decrement("ok", "host1")
    assert test_stats.ok["host1"] == 0
    test_stats.increment("ok", "host2")
    assert test_stats.ok["host2"] == 1
    test_stats.decrement("ok", "host2")
    assert test_stats.ok["host2"] == 0
    test_stats.decrement("ok", "host3")
    assert test_stats.ok["host3"] == 0

# Generated at 2022-06-12 21:51:35.929031
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    ''' Test whether we can decrement a stat, given an existing value '''

    agg_stats = AggregateStats()
    agg_stats.increment('failures', 'host1')

    agg_stats.decrement('failures', 'host1')

    assert agg_stats.failures['host1'] == 0

# Generated at 2022-06-12 21:51:38.508710
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():

    aggregate = AggregateStats()
    host = 'localhost'

    aggregate.increment('ok', host)
    assert aggregate.ok[host] == 1



# Generated at 2022-06-12 21:51:43.714281
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggstats = AggregateStats()
    aggstats.ok["host1"] = 10

    aggstats.decrement("ok", "host1")
    assert aggstats.ok["host1"] == 9

    aggstats.decrement("ok", "host1")
    assert aggstats.ok["host1"] == 8

    aggstats.decrement("ok", "host1")
    assert aggstats.ok["host1"] == 7


# Generated at 2022-06-12 21:51:53.220128
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # test aggregate_stats.decrement with empty dictionary
    agg_stats = AggregateStats()

    agg_stats.decrement("ok", "host1")
    assert agg_stats.ok.get("host1") == 0

    agg_stats.decrement("ok", "host2")
    assert agg_stats.ok.get("host2") == 0

    agg_stats.decrement("ok", "host1")
    assert agg_stats.ok.get("host1") == 0

    agg_stats.decrement("ok", "host2")
    assert agg_stats.ok.get("host2") == 0

    agg_stats.increment("ok", "host1")
    agg_stats.increment("ok", "host1")
    agg_stats.increment("ok", "host1")
    agg

# Generated at 2022-06-12 21:52:00.375855
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    # Simple case: adding a single value
    my_aggregate = AggregateStats()
    my_aggregate.update_custom_stats('foo', 42)
    assert(my_aggregate.custom.get('_run', {}).get('foo') == 42)
    # Add a second value: both values are added
    my_aggregate.update_custom_stats('foo', 24)
    assert(my_aggregate.custom.get('_run', {}).get('foo') == 66)
    # Add using a different host: the previous value is left untouched
    my_aggregate.update_custom_stats('foo', 42, 'other_host')
    assert(my_aggregate.custom.get('_run', {}).get('foo') == 66)

# Generated at 2022-06-12 21:52:04.785734
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # Set up the object
    aggregate = AggregateStats()

    # Test decrement
    aggregate.decrement("ok", "foo_host")

    # Check that the ok field is now empty
    assert aggregate.ok == {}



# Generated at 2022-06-12 21:52:06.606011
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    fixture = AggregateStats()
    fixture.increment('failures', '127.0.0.1')
    assert fixture.failures['127.0.0.1'] == 1
    fixture.decrement('failures', '127.0.0.1')
    assert fixture.failures['127.0.0.1'] == 0

# Generated at 2022-06-12 21:52:11.528306
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():

    agg = AggregateStats()
    agg.increment('ok', 'test')
    agg.increment('ok', 'test')
    agg.increment('ok', 'test')
    agg.increment('ok', 'test')
    agg.decrement('ok', 'test')

    assert agg.ok['test'] == 3, "Failed to decrement."


# Generated at 2022-06-12 21:52:18.155431
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # host does not exist in failures
    a = AggregateStats()
    a.decrement('failures', host='ping')
    assert a.failures.get('ping', 0) == 0

    # host exist in failures
    a = AggregateStats()
    a.processed['ping'] = 1
    a.failures['ping'] = 5
    a.decrement('failures', host='ping')
    assert a.failures['ping'] == 4

    # value is zero
    a = AggregateStats()
    a.processed['ping'] = 1
    a.failures['ping'] = 0
    a.decrement('failures', host='ping')
    assert a.failures['ping'] == 0

    # value is lower than zero
    a = AggregateStats()
    a.processed['ping']

# Generated at 2022-06-12 21:52:23.042398
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('failures', 'somenodes')
    assert stats.failures['somenodes'] == 1
    stats.decrement('failures', 'somenodes')
    assert stats.failures['somenodes'] == 0
    stats.increment('ok', 'somenodes')
    assert stats.ok['somenodes'] == 1
    stats.decrement('ok', 'somenodes')
    assert stats.ok['somenodes'] == 0


# Generated at 2022-06-12 21:52:28.938952
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.custom['host1'] = {'foo': 1, 'bar': 2}
    # Host does not exist
    stats.decrement('custom', 'baz')
    assert stats.custom == {'host1': {'foo': 1, 'bar': 2}}
    # Key does not exist
    stats.decrement('custom', 'host1')
    assert stats.custom == {'host1': {'foo': 1, 'bar': 2}}
    # Key exists, but is not decrementable
    stats.decrement('custom', 'host1', "foo")
    assert stats.custom['host1']['foo'] == 1
    # Key exists, decrement it
    stats.decrement('custom', 'host1', "bar")

# Generated at 2022-06-12 21:52:32.520164
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    s = AggregateStats()
    s.increment("ignored", "example.com")
    s.decrement("ignored", "example.com")
    assert s.ignored["example.com"] == 0

    # test decrement to make sure the value is not negative
    s.decrement("ignored", "example.com")
    assert s.ignored["example.com"] == 0

# Generated at 2022-06-12 21:52:39.873750
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()

    stats.increment('ok', 'host1')
    assert stats.ok == {'host1': 1}
    stats.decrement('ok', 'host1')
    assert stats.ok == {'host1': 0}

    # test negative number
    stats.ok['host1'] = 0
    stats.decrement('ok', 'host1')
    assert stats.ok == {'host1': 0}

    # test missing host
    stats.decrement('ok', 'nonexist')
    assert stats.ok == {'host1': 0}


# Generated at 2022-06-12 21:52:46.193330
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    # No exception raised
    stats.decrement('rescued', 'test')
    assert stats.rescued['test'] == 0
    stats.increment('rescued', 'test')
    stats.increment('rescued', 'test')
    stats.increment('rescued', 'test')
    assert stats.rescued['test'] == 3
    # No exception raised
    stats.decrement('rescued', 'test')
    assert stats.rescued['test'] == 2
    stats.decrement('rescued', 'test')
    stats.decrement('rescued', 'test')
    assert stats.rescued['test'] == 0
    # KeyError
    stats.decrement('rescued', 'test')
    assert stats.res

# Generated at 2022-06-12 21:52:55.514948
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    def test_helper(what, host, the_dict):
        agg_stats = AggregateStats()
        if isinstance(the_dict, dict):
            agg_stats.__dict__[what] = the_dict
        else:
            agg_stats.__dict__[what] = {host: the_dict}
        agg_stats.decrement(what, host)
        # Put 'host' in the dict, even if it does not exist
        the_dict[host] = the_dict.get(host, 0)
        the_dict[host] -= 1
        return agg_stats.__dict__[what] == the_dict

    assert test_helper("ok", "test_host", {
            "test_host": 0,
            "another_host": 0,
            }
        )
    assert test_

# Generated at 2022-06-12 21:53:03.410908
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    agg = AggregateStats()
    agg.increment("ok", "localhost")
    agg.increment("ok", "localhost")
    agg.increment("ok", "localhost")
    assert agg.ok["localhost"] == 3
    agg.decrement("ok", "localhost")
    assert agg.ok["localhost"] == 2
    agg.decrement("ok", "localhost")
    agg.decrement("ok", "localhost")
    assert agg.ok["localhost"] == 0
    agg.decrement("ok", "localhost")

# Generated at 2022-06-12 21:53:10.238114
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # Test all cases of decrementing each statistic for 1 host
    test_stats = AggregateStats()
    test_stats.increment('ok', 'test_host')
    test_stats.increment('ok', 'test_host')
    test_stats.increment('ok', 'test_host')
    test_stats.increment('failures', 'test_host')
    test_stats.increment('failures', 'test_host')
    test_stats.increment('dark', 'test_host')
    test_stats.increment('skipped', 'test_host')
    test_stats.increment('skipped', 'test_host')
    test_stats.increment('skipped', 'test_host')
    test_stats.increment('skipped', 'test_host')

# Generated at 2022-06-12 21:53:13.188944
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate_stats = AggregateStats()
    aggregate_stats.increment('ok', 'host')
    aggregate_stats.decrement('ok', 'host')
    assert aggregate_stats.ok['host'] == 0

# Generated at 2022-06-12 21:53:15.164895
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    as_obj = AggregateStats()
    as_obj.ok = {'host': 1}
    as_obj.decrement('ok', 'host')
    assert as_obj.ok == {'host': 0}


# Generated at 2022-06-12 21:53:19.201110
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('rescued', 'localhost')
    assert stats.rescued['localhost'] == 1
    stats.decrement('rescued', 'localhost')
    assert stats.rescued['localhost'] == 0



# Generated at 2022-06-12 21:53:26.511444
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('changed', 'testhost')
    assert dict(changed={'testhost': 0}) == stats.__dict__
    stats.increment('changed', 'testhost')
    assert dict(changed={'testhost': 1}) == stats.__dict__
    stats.decrement('changed', 'testhost')
    assert dict(changed={'testhost': 0}) == stats.__dict__
    stats.decrement('changed', 'testhost')
    assert dict(changed={'testhost': 0}) == stats.__dict__

# Generated at 2022-06-12 21:53:32.082467
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():

    from ansible.playbook.play_context import PlayContext
    from ansible.utils.display import Display

    display = Display()
    pc = PlayContext()

    stats = AggregateStats()
    stats.ok={"host1": 1}

    stats.decrement("ok", "host1")
    assert stats.ok.get("host1", 0)==0

    stats.decrement("ok", "host1")
    assert stats.ok.get("host1", 0)==0


# Generated at 2022-06-12 21:53:37.634805
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate = AggregateStats()
    aggregate.increment("dark", "host1")
    aggregate.increment("dark", "host1")
    aggregate.increment("dark", "host1")
    assert aggregate.dark["host1"] == 3
    aggregate.decrement("dark", "host1")
    assert aggregate.dark["host1"] == 2
    aggregate.decrement("dark", "host1")
    assert aggregate.dark["host1"] == 1
    aggregate.decrement("dark", "host1")
    assert aggregate.dark["host1"] == 0
    aggregate.decrement("dark", "host1")
    assert aggregate.dark["host1"] == 0


# Generated at 2022-06-12 21:53:42.119890
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    s = AggregateStats()

    s.ok['host'] = 2
    s.decrement('ok', 'host')
    assert s.ok['host'] == 1

    s.decrement('ok', 'host')
    assert s.ok['host'] == 0

    s.ok['host'] = 0
    s.decrement('ok', 'host')
    assert s.ok['host'] == 0



# Generated at 2022-06-12 21:53:46.095163
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    instance = AggregateStats()

    instance.decrement("ok", "host")
    assert instance.ok["host"] == 0

    instance.ok["host"] = 1
    instance.decrement("ok", "host")
    assert instance.ok["host"] == 0
