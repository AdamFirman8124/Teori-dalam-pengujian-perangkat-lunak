

# Generated at 2022-06-13 13:42:03.965301
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    unittest.TestCase.assertEqual(
        LookupModule.run({
            "lookups": "lookups",
            "lookup_plugins": "/home/ansible/ansible/plugins/lookup",
            "basedir": "/home/ansible/ansible",
            "terms": '*.txt',
            "variables": [{
                "ansible_inventory": "/.ansible/cp/ansible_inventory"
            }],
            "wantlist": False
        }),
    )


# Generated at 2022-06-13 13:42:15.334896
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Ensure that fileglob returns the paths of all files matching the glob pattern, separated by a comma
    # when invoked with the fileglob lookup plugin.
    lookup = LookupModule()
    lookup.set_options({'wantlist': True})
    results = lookup.run(terms=['/path/to/files/*.txt'], variables={'ansible_search_path': ['/path/to/files/']})
    assert results == ['/path/to/files/test1.txt', '/path/to/files/test2.txt']

    # Ensure that fileglob returns an empty list when no files match the glob pattern.
    results = lookup.run(terms=['/path/to/files/*.json'], variables={'ansible_search_path': ['/path/to/files/']})
    assert results == []

# Generated at 2022-06-13 13:42:19.990153
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    all_paths = lookup_module.run([u'*.txt'], variables={u"ansible_search_path": [u'/tmp']})
    assert isinstance(all_paths, list)



# Generated at 2022-06-13 13:42:29.816897
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    terms = [
            r'C:\Users\TempUser\source\repos\Ansible\Test\test_data\test_LookupModule_data',
            ]
    variables = dict()
    expected = [
            r'C:\Users\TempUser\source\repos\Ansible\Test\test_data\test_LookupModule_data',
            ]

    # Act
    lookup_module = LookupModule()
    results = lookup_module.run(terms, variables)

    # Assert
    assert len(results) == len(expected)
    assert sorted(results) == sorted(expected)

# Generated at 2022-06-13 13:42:38.008180
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # args
    l = LookupModule()
    l.set_options({})

    env = {"ansible_search_path":["/path/to/files"]}
    l.set_environment(env)

    # root path
    expected = ['/path/to/files/abc']
    terms = ['abc']
    result = l.run(terms)
    assert result == expected

    # sub path
    expected = ['/path/to/files/sub/def.py']
    terms = ['sub/def.py']
    result = l.run(terms)
    assert result == expected

    # sub path with wildcard
    expected = ['/path/to/files/sub/def.py', '/path/to/files/sub/def.yml']
    terms = ['sub/*.py', 'sub/*.yml']

# Generated at 2022-06-13 13:42:43.370496
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['/home/testuser/Documents/*']
    try:
        results = module.run(terms, None, wantlist=True)
        print(results)
        assert results != None
    except AnsibleFileNotFound as e:
        print(e)
        assert True

# Generated at 2022-06-13 13:42:49.490169
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_args = [ '/etc/ansible/hosts' ]
    test_kwargs = {}

    module = LookupModule()

    res = module.run(terms=test_args, **test_kwargs)

    assert isinstance(res, list)
    assert res[0] == '/etc/ansible/hosts'

# Generated at 2022-06-13 13:42:52.826340
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # This examples actually fails because test_data does not exist in the local system
    # However, we have to create a LookupModule object to run the test

    my_obj = LookupModule()
    assert my_obj.run(['test_data']) == []

# Generated at 2022-06-13 13:42:55.175552
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(['*'], dict(ansible_search_path=['.']), wantlist=True) == ['README.md']

# Generated at 2022-06-13 13:43:01.267718
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ansible_search_path = os.path.join(os.path.dirname(__file__), '..', '..')
    lookup_object = LookupModule()
    dummy_terms = ['lookup_fuzz.py']
    result = lookup_object.run(terms=dummy_terms, variables={'ansible_search_path': ansible_search_path})
    assert result