

# Generated at 2022-06-12 21:51:14.481088
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    S = AggregateStats()
    S.decrement('ok', 'host1')
    assert S.ok['host1'] == 0

    S.decrement('ok', 'host1')
    assert S.ok['host1'] == 0

    S.ok['host1'] = 1
    S.decrement('ok', 'host1')
    assert S.ok['host1'] == 0

    S.ok['host1'] = 2
    S.decrement('ok', 'host1')
    assert S.ok['host1'] == 1

# Generated at 2022-06-12 21:51:18.264235
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('failures', 'localhost')
    assert stats.failures['localhost'] == 1
    stats.decrement('failures', 'localhost')
    assert stats.failures['localhost'] == 0
    stats.decrement('failures', 'localhost')
    assert stats.failures['localhost'] == 0


# Generated at 2022-06-12 21:51:25.060131
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    my = AggregateStats()
    my.increment('failures', 'somehost')
    my.increment('failures', 'somehost')
    my.increment('ok', 'somehost')
    my.increment('skipped', 'somehost')
    my.increment('skipped', 'somehost')
    my.increment('skipped', 'otherhost')
    assert my.failures['somehost'] == 2
    assert my.ok['somehost'] == 1
    assert my.skipped['somehost'] == 2
    assert my.skipped['otherhost'] == 1


# Generated at 2022-06-12 21:51:31.632224
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    import unittest
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    stats = AggregateStats()
    stats.increment('ok', 'test')
    assert stats.ok['test'] == 1
    stats.increment('ok', 'test')
    assert stats.ok['test'] == 2
    stats.decrement('ok', 'test')
    assert stats.ok['test'] == 1
    stats.decrement('ok', 'test')
    assert stats.ok['test'] == 0

# Generated at 2022-06-12 21:51:41.871202
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    test_object = AggregateStats()
    # test for changes
    test_object.processed = {'host': 1}
    test_object.failures = {'host': 1}
    test_object.changed = {'host': 1}
    test_object.decrement('ok', 'host')
    assert test_object.ok == {'host': 0}, 'ok is not 0'
    assert test_object.processed == {'host': 1}, 'processed is not 1'
    assert test_object.failures == {'host': 1}, 'failures is not 1'
    assert test_object.changed == {'host': 1}, 'changed is not 1'
    # test for no changes
    test_object.decrement('ok', 'host')

# Generated at 2022-06-12 21:51:43.976092
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'host1')
    stats.decrement('ok', 'host1')
    assert stats.ok['host1'] == 0

# Generated at 2022-06-12 21:51:48.504869
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    a = AggregateStats()
    assert len(a.processed) == 0
    assert len(a.ok) == 0

    a.increment("ok", "hostname")

    assert len(a.processed) == 1
    assert len(a.ok) == 1



# Generated at 2022-06-12 21:51:53.963015
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    obj = AggregateStats()
    for i in range(5):
        obj.increment('ok', 'hostA')
        obj.increment('rescued', 'hostA')
    obj.decrement('ok', 'hostA')
    obj.decrement('ok', 'hostA')
    obj.decrement('ok', 'hostA')
    obj.decrement('ok', 'hostA')
    obj.decrement('ok', 'hostA')
    assert obj.ok['hostA'] == 0

# Generated at 2022-06-12 21:51:59.184767
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    test_obj = AggregateStats()
    test_obj.ok = {'localhost': 1}
    test_obj.decrement('ok', 'localhost')
    assert test_obj.ok['localhost'] == 0

    test_obj.ok['localhost'] = 1
    test_obj.decrement('ok', 'localhost')
    assert test_obj.ok['localhost'] == 0

    test_obj.ok['localhost'] = 0
    test_obj.decrement('ok', 'localhost')
    assert test_obj.ok['localhost'] == 0

# Generated at 2022-06-12 21:52:00.423092
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0