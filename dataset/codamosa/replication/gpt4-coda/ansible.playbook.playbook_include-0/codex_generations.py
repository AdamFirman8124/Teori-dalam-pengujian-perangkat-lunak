

# Generated at 2024-03-18 02:57:02.770295
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:57:10.023165
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():    # Create a PlaybookInclude instance
    pb_include = PlaybookInclude()

    # Define test cases with expected results
    test_cases = [
        (
            {'import_playbook': 'other_playbook.yml', 'vars': {'my_var': 'value'}},
            {'import_playbook': 'other_playbook.yml', 'vars': {'my_var': 'value'}}
        ),
        (
            {'import_playbook': 'other_playbook.yml', 'my_var': 'value'},
            {'import_playbook': 'other_playbook.yml', 'vars': {'my_var': 'value'}}
        ),
        (
            {'import_playbook': 'other_playbook.yml', 'tags': 'test'},
            {'import_playbook': 'other_playbook.yml', 'tags': ['test']}
        ),
        (
            {'import_playbook': 'other_playbook.yml'},
            {'import_playbook': 'other_playbook.yml'}
        ),
    ]

    #

# Generated at 2024-03-18 02:57:18.133803
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:57:27.063421
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:57:36.080575
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():    # Setup test variables
    playbook_include = PlaybookInclude()
    valid_ds = {'import_playbook': 'some_playbook.yml', 'vars': {'key': 'value'}}
    invalid_ds_not_dict = 'not a dict'
    invalid_ds_bad_vars = {'import_playbook': 'some_playbook.yml', 'vars': 'not a dict'}
    invalid_ds_missing_import = {'vars': {'key': 'value'}}
    invalid_ds_non_string_import = {'import_playbook': 12345}

    # Test with valid data structure
    try:
        processed_data = playbook_include.preprocess_data(valid_ds)
        assert processed_data['import_playbook'] == 'some_playbook.yml', "Failed to preprocess valid data structure"
        assert processed_data['vars'] == {'key': 'value'}, "Failed to preprocess valid data structure"
    except Exception as e:
        assert False, f"Unexpected exception with valid data structure: {e}"

   

# Generated at 2024-03-18 02:57:41.417815
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():    # Create a PlaybookInclude instance
    pb_include = PlaybookInclude()

    # Define test cases with expected results

# Generated at 2024-03-18 02:57:49.306607
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:57:56.341616
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:58:02.945700
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():    # Create a PlaybookInclude instance
    pb_include = PlaybookInclude()

    # Test with a simple import statement
    simple_import = {'import_playbook': 'other_playbook.yml'}
    processed_simple_import = pb_include.preprocess_data(simple_import)
    assert processed_simple_import['import_playbook'] == 'other_playbook.yml', "Failed to preprocess simple import"

    # Test with import statement and vars
    import_with_vars = {
        'import_playbook': 'other_playbook.yml',
        'vars': {'some_var': 'value'}
    }
    processed_import_with_vars = pb_include.preprocess_data(import_with_vars)
    assert processed_import_with_vars['import_playbook'] == 'other_playbook.yml', "Failed to preprocess import with vars"
    assert processed_import_with_vars['vars'] == {'some_var': 'value'}, "Failed to preprocess vars in import"

    # Test with import statement and tags
    import_with

# Generated at 2024-03-18 02:58:10.523210
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:58:25.138080
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:58:32.593653
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:58:41.276846
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:58:48.037870
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:58:56.188484
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:59:05.744871
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:59:11.557234
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:59:21.295963
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:59:27.843186
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:59:36.098685
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 02:59:48.768081
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:00:00.222280
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:00:09.272422
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:00:15.596289
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:00:21.617783
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():    # Create a PlaybookInclude instance
    pb_include = PlaybookInclude()

    # Define test cases with expected results

# Generated at 2024-03-18 03:00:26.774245
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:00:33.058182
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:00:41.347292
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():    # Setup the test case
    playbook_include = PlaybookInclude()

    # Test with a simple import_playbook statement
    simple_ds = {'import_playbook': 'some_playbook.yml'}
    processed_simple_ds = playbook_include.preprocess_data(simple_ds)
    assert processed_simple_ds['import_playbook'] == 'some_playbook.yml', "Failed to preprocess simple import_playbook"

    # Test with import_playbook and vars
    vars_ds = {'import_playbook': 'some_playbook.yml', 'vars': {'my_var': 'value'}}
    processed_vars_ds = playbook_include.preprocess_data(vars_ds)
    assert processed_vars_ds['import_playbook'] == 'some_playbook.yml', "Failed to preprocess import_playbook with vars"
    assert processed_vars_ds['vars'] == {'my_var': 'value'}, "Failed to preprocess vars in import_playbook"

    # Test with import_playbook and tags

# Generated at 2024-03-18 03:00:47.068450
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:00:54.024780
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:01:04.901381
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:01:16.521504
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:01:26.186607
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:01:31.616869
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:01:38.546140
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:01:44.705601
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:01:53.608063
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:02:01.305428
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:02:07.662533
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:02:13.033364
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:02:32.896688
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:02:41.726572
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:02:48.544014
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:03:01.084014
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:03:07.578309
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:03:13.315976
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:03:19.166127
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:03:26.393458
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:03:34.121940
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:03:40.741722
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:03:51.777815
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:03:58.128148
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:04:07.102299
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:04:13.659688
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:04:18.894812
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():    # Setup the test environment and inputs
    fake_loader = None
    fake_basedir = '/fake/base/dir'
    fake_variable_manager = None

    # Test case: Simple import with no variables or tags
    simple_import = {'import_playbook': 'other_playbook.yml'}
    pi = PlaybookInclude()
    result = pi.preprocess_data(simple_import)
    assert 'import_playbook' in result
    assert result['import_playbook'] == 'other_playbook.yml'
    assert 'vars' not in result
    assert 'tags' not in result

    # Test case: Import with variables
    import_with_vars = {
        'import_playbook': 'other_playbook.yml',
        'vars': {'some_var': 'value'}
    }
    result = pi.preprocess_data(import_with_vars)
    assert 'import_playbook' in result
    assert result['import_playbook'] == 'other_playbook.yml'


# Generated at 2024-03-18 03:04:26.269572
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:04:32.313208
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:04:37.357564
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:04:45.574119
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:04:52.923213
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:05:07.229179
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:05:14.163912
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:05:20.218112
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:05:26.009309
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:05:35.277386
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():    # Create a PlaybookInclude instance
    pb_include = PlaybookInclude()

    # Test case with a simple import statement
    simple_import = {'import_playbook': 'other_playbook.yml'}
    processed_simple_import = pb_include.preprocess_data(simple_import)
    assert processed_simple_import['import_playbook'] == 'other_playbook.yml', "Failed to preprocess simple import"

    # Test case with import statement and vars
    import_with_vars = {
        'import_playbook': 'other_playbook.yml',
        'vars': {'some_var': 'value'}
    }
    processed_import_with_vars = pb_include.preprocess_data(import_with_vars)
    assert processed_import_with_vars['import_playbook'] == 'other_playbook.yml', "Failed to preprocess import with vars"
    assert processed_import_with_vars['vars'] == {'some_var': 'value'}, "Failed to preprocess vars in import"

    # Test case with import statement and tags


# Generated at 2024-03-18 03:05:41.521262
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:05:49.809157
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:05:58.216363
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:06:05.159948
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:06:11.734127
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():    # Create a PlaybookInclude instance
    pb_include = PlaybookInclude()

    # Define test cases with expected results

# Generated at 2024-03-18 03:06:39.659382
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:06:45.896015
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader

# Generated at 2024-03-18 03:06:51.452417
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():    from ansible.parsing.dataloader import DataLoader