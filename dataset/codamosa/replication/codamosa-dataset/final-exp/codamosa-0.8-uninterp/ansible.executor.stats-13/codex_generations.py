

# Generated at 2022-06-12 21:51:06.628915
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    thing = AggregateStats()
    thing.processed['testhost'] = 1
    thing.dark['testhost'] = 10
    thing.decrement('dark', 'testhost')
    assert thing.dark['testhost'] == 9

# Generated at 2022-06-12 21:51:11.583196
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.increment('ok', 'hostA')
    stats.increment('ok', 'hostB')
    stats.decrement('ok', 'hostB')
    assert stats.ok['hostA'] == 1
    assert stats.ok['hostB'] == 0


# Generated at 2022-06-12 21:51:15.815327
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    # Test for negative number of ansible_facts
    stats.decrement('ok', 'localhost')
    stats.ok['localhost'] == 0

    # Test for ok with the number of ansible_facts still positive
    stats.ok['localhost'] = 9
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 8

# Generated at 2022-06-12 21:51:24.616878
# Unit test for method increment of class AggregateStats
def test_AggregateStats_increment():
    aggregate_stats = AggregateStats()

    # Test increment with ok
    assert len(aggregate_stats.ok) == 0
    assert len(aggregate_stats.processed) == 0
    aggregate_stats.increment("ok","127.0.0.1")
    assert len(aggregate_stats.ok) == 1
    assert len(aggregate_stats.processed) == 1
    aggregate_stats.increment("ok","127.0.0.1")
    assert len(aggregate_stats.ok) == 1
    assert aggregate_stats.ok["127.0.0.1"] == 2
    assert len(aggregate_stats.processed) == 1

    # Test increment with failures
    assert len(aggregate_stats.failures) == 0
    assert len(aggregate_stats.processed) == 1
   

# Generated at 2022-06-12 21:51:29.637345
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    aggregate_stats_object = AggregateStats()
    aggregate_stats_object.set_custom_stats('mytest', {'test1':1, 'test2':2}, host='_run')
    assert aggregate_stats_object.custom['_run']['mytest'] == {'test1':1, 'test2':2}
    aggregate_stats_object.decrement('custom', '_run')
    assert aggregate_stats_object.custom['_run'] == {}

# Generated at 2022-06-12 21:51:36.358265
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # A few test cases
    import pytest
    as_test = AggregateStats()

    as_test.increment('ok', 'test_host')
    as_test.decrement('ok', 'test_host')
    assert as_test.ok['test_host'] == 0
    as_test.decrement('ok', 'test_host')
    assert as_test.ok['test_host'] == 0

# Generated at 2022-06-12 21:51:46.395771
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():

    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class MyTest(unittest.TestCase):

        @staticmethod
        def _get_aggregate_stats():

            # New object
            my_aggregate_stats = AggregateStats()

            # Update custom stats
            my_aggregate_stats.update_custom_stats('a', {'b': 0}, host=None)
            my_aggregate_stats.update_custom_stats('a', {'b': 1}, host=None)
            my_aggregate_stats.update_custom_stats('a', {'b': 2}, host=None)

            return my_aggregate_stats

        def test_aggregate_stats(self):
            my_aggregate

# Generated at 2022-06-12 21:51:51.167453
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    stats = AggregateStats()
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0

    stats.ok['localhost'] = -1
    stats.decrement('ok', 'localhost')
    assert stats.ok['localhost'] == 0

    stats.decrement('dark', 'localhost')
    assert stats.dark['localhost'] == 0


# Generated at 2022-06-12 21:51:58.981513
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    # __init__
    aggr = AggregateStats()
    assert not aggr.ok
    assert not aggr.failures
    assert not aggr.dark

    # increment, decrement
    aggr.increment('ok', 'localhost')
    aggr.increment('failures', 'localhost')
    aggr.increment('dark', 'localhost')
    assert aggr.ok
    assert aggr.failures
    assert aggr.dark

    aggr.decrement('ok', 'localhost')
    aggr.decrement('failures', 'localhost')
    aggr.decrement('dark', 'localhost')
    aggr.decrement('ok', 'localhost')
    aggr.decrement('failures', 'localhost')
    aggr.decrement('dark', 'localhost')

    assert aggr

# Generated at 2022-06-12 21:52:03.157431
# Unit test for method decrement of class AggregateStats
def test_AggregateStats_decrement():
    agg_stats = AggregateStats()
    assert agg_stats.decrement('ok', 'test') == None
    agg_stats.ok['test'] = 1
    assert agg_stats.decrement('ok', 'test') == None
    assert agg_stats.ok['test'] == 0


# Generated at 2022-06-12 21:52:13.729381
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    stats = AggregateStats()
    stats.update_custom_stats('aggregate_results', {'foo': 42}, 'localhost')
    assert stats.custom['localhost']['aggregate_results'] == {'foo': 42}
    stats.update_custom_stats('aggregate_results', {'foo': 42, 'bar': 43}, 'localhost')
    assert stats.custom['localhost']['aggregate_results'] == {'foo': 84, 'bar': 43}
    stats.update_custom_stats('aggregate_results', {'bar': 'baz'}, 'localhost')
    assert stats.custom['localhost']['aggregate_results'] == {'foo': 84, 'bar': 'baz'}

# Generated at 2022-06-12 21:52:22.210453
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase

    # initialize needed objects
    tqm = None
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='tests/inventory')

# Generated at 2022-06-12 21:52:26.650894
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    aggregate_stats = AggregateStats()
    aggregate_stats.update_custom_stats('my_new', {'a':1, 'b':2})
    assert aggregate_stats.custom['_run']['my_new'] == {'a':1, 'b':2}

    aggregate_stats.update_custom_stats('my_new', {'b':3, 'c':4})
    assert aggregate_stats.custom['_run']['my_new'] == {'a':1, 'b':3, 'c':4}


# Generated at 2022-06-12 21:52:33.518835
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    import pytest
    # setup
    my_stats = AggregateStats()
    my_stats.custom = {}

    # test adding hosts to my_stats.custom
    host = 'test_host'
    which = 'which_1'
    what = {'foo': 'bar'}
    my_stats.update_custom_stats(which, what, host)
    assert my_stats.custom[host] == {'which_1': {'foo': 'bar'}}
    my_stats.update_custom_stats(which, what, host)
    assert my_stats.custom[host] == {'which_1': {'foo': 'bar'}}

    # test merging custom stats
    what = {'baz': 'qux'}
    my_stats.update_custom_stats(which, what, host)

# Generated at 2022-06-12 21:52:42.339230
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():

    statistics = AggregateStats()
    assert statistics.custom == {}

    # empty stat
    statistics.update_custom_stats("memory", None)

    # int stat
    statistics.update_custom_stats("memory", 42)
    statistics2 = AggregateStats()
    statistics2.update_custom_stats("memory", 42)
    assert statistics.custom == statistics2.custom

    # str stat
    statistics.update_custom_stats("error", "Error")
    assert statistics.custom == {'_run': {'memory': 42, 'error': 'Error'}}

    # dict stat
    statistics.update_custom_stats("dictionnary", {'key': 'value', 'key2': 'value2'})

# Generated at 2022-06-12 21:52:51.133845
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    ''' AggregateStats.update_custom_stats'''

    # Create new AggregateStats instance
    ag = AggregateStats()

    # Case 1: updating custom stats
    ag.update_custom_stats('memory', {'used': 100, 'total': 1000}, host = 'localhost')
    assert ag.custom['localhost']['memory']['used'] == 100
    assert ag.custom['localhost']['memory']['total'] == 1000

    # Case 2: updating custom stats with existing ones
    ag.update_custom_stats('memory', {'used': 200, 'total': 2000}, host = 'localhost')
    assert ag.custom['localhost']['memory']['used'] == 200
    assert ag.custom['localhost']['memory']['total'] == 2000

    # Case 3: updating custom stats without host provided
    ag

# Generated at 2022-06-12 21:52:59.817886
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    # setup
    aggregate_stats = AggregateStats()
    aggregate_stats.set_custom_stats('key1', {'k1': 'v1', 'k2': 'v2'}, 'host1')
    aggregate_stats.set_custom_stats('key1', {'k1': 'v1', 'k2': 'v2'}, 'host2')
    aggregate_stats.set_custom_stats('key1', {'k3': 'v3'}, 'host3')
    aggregate_stats.set_custom_stats('key2', 'val1', 'host1')
    aggregate_stats.set_custom_stats('key2', 'val2', 'host2')
    aggregate_stats.set_custom_stats('key2', 'val3', 'host3')

# Generated at 2022-06-12 21:53:07.007103
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():

    custom_stat = {'1' : '2'}
    as_custom_stat = AggregateStats()
    as_custom_stat.set_custom_stats('first', 'second')
    as_custom_stat.set_custom_stats('one', custom_stat)

    # this should not change anything
    as_custom_stat.update_custom_stats('first', 'second')
    assert as_custom_stat.custom['_run']['first'] == 'second'
    as_custom_stat.update_custom_stats('one', custom_stat)
    assert as_custom_stat.custom['_run']['one']['1'] == '2'

    custom_stat['1'] = '3'
    as_custom_stat.update_custom_stats('one', custom_stat)
    assert as_custom_

# Generated at 2022-06-12 21:53:11.531354
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():

    from ansible.compat.tests import unittest

    class TestAggregateStats(unittest.TestCase):

        def setUp(self):
            self.aggregate_stats = AggregateStats()

        #
        # Tests
        #
        def test_update_custom_stats_none_type(self):
            self.aggregate_stats.update_custom_stats('key', None)
            self.assertEqual(self.aggregate_stats.custom, {'_run': {'key': None}})

        def test_update_custom_stats_string_type(self):
            self.aggregate_stats.update_custom_stats('key', 'string')
            self.assertEqual(self.aggregate_stats.custom, {'_run': {'key': 'string'}})


# Generated at 2022-06-12 21:53:15.212469
# Unit test for method update_custom_stats of class AggregateStats
def test_AggregateStats_update_custom_stats():
    ''' test method update_custom_stats of class AggregateStats'''

    from ansible.module_utils.common._collections_compat import MutableMapping

    host = 'host1'
    which = 'custom_stat'
    asgs = AggregateStats()
    # Test when custom[host] does not exist
    asgs.update_custom_stats(which, 1, host)
    assert asgs.custom[host][which] == 1
    # Test when custom[host] exist and which does not in custom[host]
    asgs.update_custom_stats(which, 1, host)
    assert asgs.custom[host][which] == 2
    # Test when which exist as a str in custom[host]
    asgs.update_custom_stats(which, 'string1', host)
    assert asgs.custom