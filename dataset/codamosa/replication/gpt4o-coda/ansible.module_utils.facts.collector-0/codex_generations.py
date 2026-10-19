

# Generated at 2024-05-31 02:05:18.109522
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector],
    }

# Generated at 2024-05-31 02:05:22.284662
# Unit test for function build_fact_id_to_collector_map

# Generated at 2024-05-31 02:05:26.792334
# Unit test for function get_collector_names
def test_get_collector_names():    valid_subsets = frozenset(['all', 'network', 'hardware', 'software'])

# Generated at 2024-05-31 02:05:28.673147
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector]
    }

# Generated at 2024-05-31 02:05:31.766579
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector],
    }

# Generated at 2024-05-31 02:05:35.671509
# Unit test for function find_collectors_for_platform

# Generated at 2024-05-31 02:05:40.192449
# Unit test for function collector_classes_from_gather_subset

# Generated at 2024-05-31 02:05:43.894688
# Unit test for function build_dep_data
def test_build_dep_data():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': {'fact1', 'fact2'}})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'fact3'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': set()})]
    }

# Generated at 2024-05-31 02:05:47.482349
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:05:51.130977
# Unit test for function build_fact_id_to_collector_map

# Generated at 2024-05-31 02:06:05.280923
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:06:09.228854
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:06:12.540083
# Unit test for function build_fact_id_to_collector_map

# Generated at 2024-05-31 02:06:15.384597
# Unit test for function build_dep_data
def test_build_dep_data():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': {'fact1', 'fact2'}})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'fact3'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': set()})]
    }

# Generated at 2024-05-31 02:06:19.480092
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': {'fact_x'}})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'fact_y'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': set()})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:06:22.159358
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector],
    }

# Generated at 2024-05-31 02:06:25.936622
# Unit test for function collector_classes_from_gather_subset

# Generated at 2024-05-31 02:06:30.499232
# Unit test for function find_collectors_for_platform

# Generated at 2024-05-31 02:06:34.020169
# Unit test for function collector_classes_from_gather_subset

# Generated at 2024-05-31 02:06:37.777795
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:07:10.161307
# Unit test for function get_collector_names
def test_get_collector_names():    valid_subsets = frozenset(['all', 'network', 'hardware', 'software'])

# Generated at 2024-05-31 02:07:13.094203
# Unit test for function build_fact_id_to_collector_map

# Generated at 2024-05-31 02:07:16.815419
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:07:23.030182
# Unit test for function build_fact_id_to_collector_map

# Generated at 2024-05-31 02:07:25.001436
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector],
    }

# Generated at 2024-05-31 02:07:29.452595
# Unit test for function get_collector_names
def test_get_collector_names():    valid_subsets = frozenset(['all', 'network', 'hardware', 'software'])

# Generated at 2024-05-31 02:07:35.026158
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector]
    }

# Generated at 2024-05-31 02:07:44.790065
# Unit test for function build_dep_data
def test_build_dep_data():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': {'fact1', 'fact2'}})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'fact3'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': set()})]
    }

# Generated at 2024-05-31 02:07:49.115628
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:07:52.033619
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:08:37.346202
# Unit test for function get_collector_names
def test_get_collector_names():    valid_subsets = frozenset(['all', 'network', 'hardware', 'software'])

# Generated at 2024-05-31 02:08:41.356428
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class MockCollectorA(BaseFactCollector):
        name = 'collector_a'
        _fact_ids = {'fact_a1', 'fact_a2'}

    class MockCollectorB(BaseFactCollector):
        name = 'collector_b'
        _fact_ids = {'fact_b1', 'fact_b2'}

    collectors_for_platform = [MockCollectorA, MockCollectorB]
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    assert 'collector_a' in fact_id_to_collector_map
    assert 'collector_b' in fact_id_to_collector_map
    assert 'fact_a1' in fact_id_to_collector_map
    assert 'fact_a2' in fact_id_to_collector_map
    assert 'fact_b1' in fact_id_to_collector_map
    assert 'fact_b2' in fact_id_to_collector_map


# Generated at 2024-05-31 02:08:45.202273
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector]
    }

# Generated at 2024-05-31 02:08:49.534558
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': {'fact_b'}})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'fact_c'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': set()})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:08:58.033299
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector],
    }

# Generated at 2024-05-31 02:09:07.318677
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:09:16.509236
# Unit test for function get_collector_names
def test_get_collector_names():    valid_subsets = frozenset(['all', 'network', 'hardware', 'software'])

# Generated at 2024-05-31 02:09:19.444833
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector],
    }

# Generated at 2024-05-31 02:09:28.246856
# Unit test for function build_dep_data
def test_build_dep_data():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': {'fact1', 'fact2'}})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'fact3'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': set()})]
    }

# Generated at 2024-05-31 02:09:29.982512
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector],
    }

# Generated at 2024-05-31 02:11:01.488815
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector]
    }

# Generated at 2024-05-31 02:11:05.391864
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_b', 'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:11:09.082332
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:11:13.711823
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:11:18.239970
# Unit test for function build_fact_id_to_collector_map

# Generated at 2024-05-31 02:11:22.240247
# Unit test for function build_fact_id_to_collector_map

# Generated at 2024-05-31 02:11:25.175081
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:11:30.033793
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:11:33.166833
# Unit test for function build_fact_id_to_collector_map

# Generated at 2024-05-31 02:11:36.857748
# Unit test for function build_fact_id_to_collector_map

# Generated at 2024-05-31 02:13:48.794842
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': {'fact_b', 'fact_c'}})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'fact_d'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': set()})],
        'collector_d': [type('CollectorD', (BaseFactCollector,), {'required_facts': {'fact_e'}})],
    }
    collector_names = {'collector_a', 'collector_b', 'collector_c', 'collector_d'}
    expected_output = {
        'collector_a': {'fact_b', 'fact_c'},
        'collector_b': {'fact_d'},
        'collector_c': set(),
        'collector_d': {'fact_e'},
    }
    assert build_dep_data(collector_names, all_fact_subsets) == expected_output

# Generated at 2024-05-31 02:13:54.294614
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class MockCollectorA(BaseFactCollector):
        name = 'collector_a'
        _fact_ids = {'fact_a1', 'fact_a2'}

    class MockCollectorB(BaseFactCollector):
        name = 'collector_b'
        _fact_ids = {'fact_b1', 'fact_b2'}

    collectors_for_platform = [MockCollectorA, MockCollectorB]
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    assert 'collector_a' in fact_id_to_collector_map
    assert 'collector_b' in fact_id_to_collector_map
    assert 'fact_a1' in fact_id_to_collector_map
    assert 'fact_a2' in fact_id_to_collector_map
    assert 'fact_b1' in fact_id_to_collector_map
    assert 'fact_b2' in fact_id_to_collector_map


# Generated at 2024-05-31 02:13:58.901244
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': {'fact_b', 'fact_c'}})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'fact_d'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': set()})],
        'collector_d': [type('CollectorD', (BaseFactCollector,), {'required_facts': {'fact_e'}})],
    }
    collector_names = {'collector_a', 'collector_b', 'collector_c'}

    expected_output = {
        'collector_a': {'fact_b', 'fact_c'},
        'collector_b': {'fact_d'},
        'collector_c': set(),
    }

    assert build_dep_data(collector_names, all_fact_subsets) == expected_output

test_build_dep_data()

# Generated at 2024-05-31 02:14:02.113281
# Unit test for function build_fact_id_to_collector_map

# Generated at 2024-05-31 02:14:05.786249
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:14:09.146934
# Unit test for function build_fact_id_to_collector_map

# Generated at 2024-05-31 02:14:12.914940
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:14:14.525910
# Unit test for function select_collector_classes
def test_select_collector_classes():    all_fact_subsets = {
        'network': [BaseFactCollector],
        'hardware': [BaseFactCollector],
        'os': [BaseFactCollector],
    }

# Generated at 2024-05-31 02:14:17.478097
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_b', 'collector_d'}})],
    }

    # Test case where all required facts are resolved

# Generated at 2024-05-31 02:14:20.702060
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():    all_fact_subsets = {
        'collector_a': [type('CollectorA', (BaseFactCollector,), {'required_facts': set()})],
        'collector_b': [type('CollectorB', (BaseFactCollector,), {'required_facts': {'collector_a'}})],
        'collector_c': [type('CollectorC', (BaseFactCollector,), {'required_facts': {'collector_d'}})],
    }

    # Test case where all required facts are resolved