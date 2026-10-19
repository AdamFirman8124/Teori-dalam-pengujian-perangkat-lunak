

# Generated at 2022-06-12 21:51:16.278180
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    stats.update_custom_stats("foo", {"a": "b"})
    assert stats.custom["_run"]["foo"] == {"a": "b"}
    stats.update_custom_stats("bar", "foobar")
    assert stats.custom["_run"]["bar"] == "foobar"
    stats.update_custom_stats("bar", "foobar", "fake_host")
    assert stats.custom["fake_host"]["bar"] == "foobar"
    stats.update_custom_stats("bar", "barfoo", "fake_host")
    assert stats.custom["fake_host"]["bar"] == "barfoo"
    stats.update_custom_stats("foo", {"c": "d"})

# Generated at 2022-06-12 21:51:25.095291
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    as_object = AggregateStats()
    assert as_object.custom == {}
    as_object.update_custom_stats('my_name', 'my_value')
    assert as_object.custom == {'_run': {'my_name': 'my_value'}}
    as_object.update_custom_stats('my_name', 'my_other_value')
    assert as_object.custom == {'_run': {'my_name': 'my_other_value'}}
    as_object.update_custom_stats('my_other_name', 'my_value', 'example.com')
    assert as_object.custom == {'_run': {'my_name': 'my_other_value'}, 'example.com': {'my_other_name': 'my_value'}}
    as_object.update

# Generated at 2022-06-12 21:51:28.987339
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('skipped', 'host1')
    stats.decrement('skipped', 'host1')
    assert stats.skipped['host1'] == 0
    # Should not raise KeyError, set value to 0 instead
    stats.decrement('skipped', 'host1')
    assert stats.skipped['host1'] == 0

# Generated at 2022-06-12 21:51:33.130913
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # Create test object
    a = AggregateStats()

    # Check initial value of 'ok' dict
    assert a.ok == {}

    # Add an item to the dict
    a.ok['localhost'] = 5

    # Decrement this item by 3
    a.decrement('ok', 'localhost')
    a.decrement('ok', 'localhost')
    a.decrement('ok', 'localhost')

    # Check if dict is no 0
    assert a.ok['localhost'] == 0

    # Try to decrement by 1
    a.decrement('ok', 'localhost')

    # Check if dict is still 0
    assert a.ok['localhost'] == 0

# Generated at 2022-06-12 21:51:43.676962
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate = AggregateStats()
    aggregate.ok = {"host1": 1, "host2": 2, "host3": 3}
    aggregate.decrement("ok", "host1")
    assert aggregate.ok == {"host1": 0, "host2": 2, "host3": 3}
    aggregate.decrement("ok", "host1")
    assert aggregate.ok == {"host1": 0, "host2": 2, "host3": 3}
    aggregate.decrement("ok", "host2")
    assert aggregate.ok == {"host1": 0, "host2": 1, "host3": 3}
    aggregate.decrement("ok", "host3")
    assert aggregate.ok == {"host1": 0, "host2": 1, "host3": 2}

# Generated at 2022-06-12 21:51:52.881906
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    aggr = AggregateStats()
    aggr.ok = {"host1": 0, "host2": 0, "host3": 0, "host4": 0}
    aggr.increment("ok", "host1")
    assert aggr.ok["host1"] == 1
    assert aggr.ok["host2"] == 0
    assert aggr.ok["host3"] == 0
    assert aggr.ok["host4"] == 0
    aggr.increment("ok", "host2")
    assert aggr.ok["host2"] == 1
    aggr.increment("ok", "host3")
    assert aggr.ok["host3"] == 1
    aggr.increment("ok", "host4")
    assert aggr.ok["host4"] == 1

# Generated at 2022-06-12 21:51:59.549441
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    agg_stats = AggregateStats()

    agg_stats.increment('ok', 'host1')
    agg_stats.increment('changed', 'new_host1')
    agg_stats.increment('changed', 'new_host1')

    assert agg_stats.processed == {'host1': 1, 'new_host1': 1}
    assert agg_stats.ok == {'host1': 1}
    assert agg_stats.changed == {'new_host1': 2}
    assert agg_stats.ignored == {}
    assert agg_stats.dark == {}
    assert agg_stats.ok == {'host1': 1}
    assert agg_stats.skipped == {}


# Generated at 2022-06-12 21:52:09.874501
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    # Init
    stats = AggregateStats()
    stats.custom = {
        '_run': {
            'test': {
                'test1': {
                    'test2': 'test3'
                }
            }
        }
    }

    # Run
    stats.update_custom_stats('test', 'test4')

    # Assert
    assert stats.custom['_run']['test'] == {'test1': {'test2': 'test3'}}

    # Run
    stats.update_custom_stats('test', {'test1': 'test2'})

    # Assert
    assert stats.custom['_run']['test'] == {'test1': 'test2'}

    # Run

# Generated at 2022-06-12 21:52:12.921616
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    aggregate_stats = AggregateStats()
    what = "ok"
    host = 1
    aggregate_stats.increment(what, host)
    assert aggregate_stats.ok[1] == 1


# Generated at 2022-06-12 21:52:14.614135
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    '''
    make sure decrement doesn't leave a key in negative
    '''
    as_ = AggregateStats()
    as_.decrement('ok', 'test_hostname')
    assert as_.ok['test_hostname'] == 0
