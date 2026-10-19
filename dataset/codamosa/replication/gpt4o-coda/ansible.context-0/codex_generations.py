

# Generated at 2024-05-30 21:01:43.481398
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:01:46.726215
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:01:51.762854
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:01:55.692466
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not CLIARGS['test_list']  # Ensure it's a shallow copy

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not CLIARGS

# Generated at 2024-05-30 21:01:58.630768
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:02:04.416528
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:02:09.507521
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not CLIARGS['test_list']  # Ensure it's a shallow copy

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not CLIARGS

# Generated at 2024-05-30 21:02:12.989035
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:02:17.330076
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:02:21.648651
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:02:34.375456
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test retrieving a simple value
    get_test_key = cliargs_deferred_get('test_key')
    assert get_test_key() == 'test_value'

    # Test retrieving a list with shallow copy
    get_test_list = cliargs_deferred_get('test_list', shallowcopy=True)
    list_value = get_test_list()
    assert list_value == [1, 2, 3]
    assert list_value is not test_args['test_list']  # Ensure it's a shallow copy

    # Test retrieving a dictionary with shallow copy
    get_test_dict = cliargs_deferred_get('test_dict', shallowcopy=True)
    dict_value = get_test

# Generated at 2024-05-30 21:02:38.730661
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:02:44.452393
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1}
    assert getter() is not test

# Generated at 2024-05-30 21:02:50.656124
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:02:56.984564
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:03:03.591110
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:03:10.585364
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:03:15.692965
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:03:19.940999
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:03:23.245949
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not CLIARGS['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not CLIARGS

# Generated at 2024-05-30 21:03:44.639935
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:03:48.371485
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}

# Generated at 2024-05-30 21:03:54.278845
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:03:58.295491
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Setup
    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}}
    _init_global_context(cli_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not cli_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1}
    assert getter() is not cli_args['test_dict']  # Ensure it's a different object

    # Test with default value


# Generated at 2024-05-30 21:04:03.950231
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize CLIARGS with some test data
    _init_global_context({'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}})

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not CLIARGS['test_list']

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1}
    assert getter() is not CLIARGS['test_dict']

    # Test with shallow copy for set
   

# Generated at 2024-05-30 21:04:08.604093
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:04:12.925490
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:04:16.930256
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:04:20.774507
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:04:23.997687
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:05:01.272572
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a shallow copy

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:05:06.047660
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:05:10.264865
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}
    _init_global_context(test_args)

    # Test retrieving a simple value
    get_test_key = cliargs_deferred_get('test_key')
    assert get_test_key() == 'test_value'

    # Test retrieving a list with shallow copy
    get_test_list = cliargs_deferred_get('test_list', shallowcopy=True)
    list_value = get_test_list()
    assert list_value == [1, 2, 3]
    assert list_value is not CLIARGS['test_list']  # Ensure it's a shallow copy

    # Test retrieving a dictionary with shallow copy

# Generated at 2024-05-30 21:05:14.128567
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:05:18.338370
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize CLIARGS with some test data
    _init_global_context({'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}})

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not CLIARGS['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1}
    assert getter() is not CLIARGS['test_dict']  #

# Generated at 2024-05-30 21:05:22.474501
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a shallow copy

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:05:29.963803
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a shallow copy

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:05:38.907591
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:05:43.937621
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test retrieving a simple value
    get_test_key = cliargs_deferred_get('test_key')
    assert get_test_key() == 'test_value'

    # Test retrieving a list with shallow copy
    get_test_list = cliargs_deferred_get('test_list', shallowcopy=True)
    list_value = get_test_list()
    assert list_value == [1, 2, 3]
    assert list_value is not CLIARGS['test_list']  # Ensure it's a shallow copy

    # Test retrieving a dictionary with shallow copy
    get_test_dict = cliargs_deferred_get('test_dict', shallowcopy=True)
    dict_value = get_test

# Generated at 2024-05-30 21:05:47.320333
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:06:58.339141
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:07:03.144759
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:07:07.802005
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:07:12.969983
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:07:16.862769
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a shallow copy

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:07:20.711710
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not CLIARGS['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not CLIARGS

# Generated at 2024-05-30 21:07:24.528056
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:07:28.072365
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:07:31.618471
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:07:35.727403
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:09:53.502385
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}

# Generated at 2024-05-30 21:09:56.962201
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test retrieving a simple value
    get_test_key = cliargs_deferred_get('test_key')
    assert get_test_key() == 'test_value'

    # Test retrieving a list with shallow copy
    get_test_list = cliargs_deferred_get('test_list', shallowcopy=True)
    assert get_test_list() == [1, 2, 3]
    assert get_test_list() is not test_args['test_list']  # Ensure it's a shallow copy

    # Test retrieving a dictionary with shallow copy
    get_test_dict = cliargs_deferred_get('test_dict', shallowcopy=True)

# Generated at 2024-05-30 21:10:00.291412
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:10:08.088895
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    cli_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}

# Generated at 2024-05-30 21:10:11.855835
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test retrieving a simple value
    get_test_key = cliargs_deferred_get('test_key')
    assert get_test_key() == 'test_value'

    # Test retrieving a list with shallow copy
    get_test_list = cliargs_deferred_get('test_list', shallowcopy=True)
    list_value = get_test_list()
    assert list_value == [1, 2, 3]
    assert list_value is not CLIARGS['test_list']  # Ensure it's a shallow copy

    # Test retrieving a dictionary with shallow copy
    get_test_dict = cliargs_deferred_get('test_dict', shallowcopy=True)
    dict_value = get_test

# Generated at 2024-05-30 21:10:16.330889
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not CLIARGS['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1}
    assert getter() is not CLI

# Generated at 2024-05-30 21:10:19.852490
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:10:23.928272
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args

# Generated at 2024-05-30 21:10:27.110169
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize CLIARGS with some test data
    _init_global_context({'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1}, 'test_set': {1, 2, 3}})

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not CLIARGS['test_list']

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1}
    assert getter() is not CLIARGS['test_dict']

    # Test with shallow copy for set
   

# Generated at 2024-05-30 21:10:30.519572
# Unit test for function cliargs_deferred_get
def test_cliargs_deferred_get():    # Initialize the global context with some test arguments
    test_args = {'test_key': 'test_value', 'test_list': [1, 2, 3], 'test_dict': {'a': 1, 'b': 2}}
    _init_global_context(test_args)

    # Test without shallow copy
    getter = cliargs_deferred_get('test_key')
    assert getter() == 'test_value'

    # Test with shallow copy for list
    getter = cliargs_deferred_get('test_list', shallowcopy=True)
    assert getter() == [1, 2, 3]
    assert getter() is not test_args['test_list']  # Ensure it's a different object

    # Test with shallow copy for dict
    getter = cliargs_deferred_get('test_dict', shallowcopy=True)
    assert getter() == {'a': 1, 'b': 2}
    assert getter() is not test_args