

# Generated at 2022-06-14 05:26:57.318678
# Unit test for function overload_configuration
def test_overload_configuration():
    def foo(**kwargs):
        return kwargs

    @overload_configuration
    def foo_decorated(**kwargs):
        return kwargs

    assert foo_decorated(define=["foo=bar"]) == foo(define=["foo=bar"])

# Generated at 2022-06-14 05:27:04.667967
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test overload_configuration
    """
    @overload_configuration
    def mock_command(define=[]):
        """Mock CLI command
        """
        return ""

    config["foo"] = "bar"
    config["bar"] = "foo"

    mock_command(define=["foo=bar"])

    assert config["foo"] == "bar"
    assert config["bar"] == "foo"

    mock_command(define=["foo=foo", "bar=bar"])

    assert config["foo"] == "foo"
    assert config["bar"] == "bar"

# Generated at 2022-06-14 05:27:10.063333
# Unit test for function overload_configuration
def test_overload_configuration():
    override = UserDict({"define":["custom_setting=setting_value"]})
    @overload_configuration
    def test_function(*args, **kwargs):
        return config.get("custom_setting")

    assert "setting_value" == test_function(**override)



# Generated at 2022-06-14 05:27:16.435918
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(define):
        return config

    for pair in ["body=hello", "subject=world", "empty="]:
        assert test_function(define=pair) != config  # Function modifies config

    assert test_function(define="=world") == config  # No key to modify in config
    assert test_function(define="subjectworld") == config  # No '=' in parameter

# Generated at 2022-06-14 05:27:21.206987
# Unit test for function overload_configuration
def test_overload_configuration():
    config.clear()
    config["commit_message_template"] = "Initial template"

    @overload_configuration
    def _test_overload_configuration(define):
        return config["commit_message_template"]

    assert _test_overload_configuration(define=["commit_message_template=overload"]) == "overload"

# Generated at 2022-06-14 05:27:31.530044
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    Test that the overload_configuration decorator works as expected.
    """

    @overload_configuration
    def foo(a, b, define=None):
        pass

    initial_value = config["changelog_capitalize"]
    foo(1, 2, define=["changelog_capitalize=false"])
    assert not config["changelog_capitalize"]
    foo(1, 2, define=["changelog_capitalize=true"])
    assert config["changelog_capitalize"]
    foo(1, 2, define=["changelog_capitalize="])
    assert not config["changelog_capitalize"]
    foo(1, 2, define=["changelog_capitalize"])
    assert not config["changelog_capitalize"]

# Generated at 2022-06-14 05:27:34.380827
# Unit test for function current_changelog_components
def test_current_changelog_components():
    # No error should be raised
    assert callable(current_changelog_components()[0])

# Generated at 2022-06-14 05:27:39.531854
# Unit test for function overload_configuration
def test_overload_configuration():
    config_dict = {}
    config_dict["define"] = ["python_requires=2.7"]

    @overload_configuration
    def update_configuration(config_dict):
        return

    update_configuration(config_dict)
    assert config["python_requires"] == "2.7"

# Generated at 2022-06-14 05:27:50.076191
# Unit test for function current_changelog_components
def test_current_changelog_components():
    # test with a bad import
    config["changelog_components"] = "this.bad_package"
    try:
        current_changelog_components()
    except ImproperConfigurationError as error:
        # check the message
        assert (
            'Unable to import changelog component "this.bad_package"'
            in str(error)
        )

    # test with a good import
    config["changelog_components"] = "semantic_release.changelog.components.compute_breaking_changes_component"
    assert current_changelog_components()[0] == "semantic_release.changelog.components.compute_breaking_changes_component"

# Generated at 2022-06-14 05:27:56.466216
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_key"] = "test_value"

    @overload_configuration
    def print_config(define):
        print(config["test_key"])
        return

    print_config(define=["test_key=new_test_value"])
    assert config["test_key"] == "new_test_value"
    config.pop("test_key")

# Generated at 2022-06-14 05:28:06.657824
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def change_config(define):
        pass

    change_config(define=["define=value"])
    assert config["define"] == "value"

# Generated at 2022-06-14 05:28:10.146211
# Unit test for function current_commit_parser
def test_current_commit_parser():
    config["commit_parser"] = "semantic_release.commit_parser.parse"
    assert current_commit_parser() == "semantic_release.commit_parser.parse"


# Generated at 2022-06-14 05:28:18.281663
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "test"

    @overload_configuration
    def test_func(define, test=None):
        return test

    assert test_func(define=["test=success"]) == "success"

    config["test"] = "test"

    @overload_configuration
    def test_func2(define=[], test=None):
        return test

    assert test_func2(define=["test=failure"]) is None

# Generated at 2022-06-14 05:28:26.388913
# Unit test for function overload_configuration
def test_overload_configuration():
    config = {"foo": "foo"}

    @overload_configuration
    def func(define=None):
        pass

    func(define=["foo=bar"])
    assert config["foo"] == "bar"

    # TODO: Fix this test
    # func(define=["foo=bar", "a=b"])
    # assert config["foo"] == "bar"
    # assert config["a"] == "b"

# Generated at 2022-06-14 05:28:35.670849
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function tests the decorator overload_configuration
    """

 
    def test_func(a, b):
        return a, b

    # with argument define
    test_a = 1
    test_b = 1
    final_a, final_b = overload_configuration(test_func)(a=test_a, b=test_b, define=["a=2"])
    assert test_a != final_a
    assert final_a == 2
    assert final_b == test_b

test_overload_configuration()

# Generated at 2022-06-14 05:28:39.829657
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config["changelog_components"] = "tests.test_config:test_component"
    components = current_changelog_components()
    assert len(components) == 1
    assert components[0] == test_component



# Generated at 2022-06-14 05:28:47.944452
# Unit test for function overload_configuration
def test_overload_configuration():
    import semantic_release.configuration

    config_bak = semantic_release.configuration.config

    @overload_configuration
    def foo(bar):
        return semantic_release.configuration.config

    # Test that all is OK
    semantic_release.configuration.config["name"] = "test"
    assert foo(bar=None).get("name") == "test"

    # Test that present keys are overwritten
    foo(bar=None, define=["name=test2"])
    assert foo(bar=None).get("name") == "test2"

    # Test that missing keys are added
    foo(bar=None, define=["age=42"])
    assert foo(bar=None).get("age") == "42"

    semantic_release.configuration.config = config_bak

# Generated at 2022-06-14 05:28:52.741467
# Unit test for function overload_configuration
def test_overload_configuration():
    """This test checks that the overload_configuration decorator works
    """
    @overload_configuration
    def decor_func(key, value):
        config[key] = value

    decor_func("new_key", "new_value")
    assert config["new_key"] == "new_value"

# Generated at 2022-06-14 05:28:58.358924
# Unit test for function overload_configuration
def test_overload_configuration():
    func_called = False
    # pylint:disable=W0613
    def func(define=None):
        nonlocal func_called
        func_called = True

    func = overload_configuration(func)
    func(define=["key1=value1", "key2=value2"])
    assert func_called
    assert config["key1"] == "value1"
    assert config["key2"] == "value2"

# Generated at 2022-06-14 05:28:59.531432
# Unit test for function current_changelog_components
def test_current_changelog_components():
    current_changelog_components()

# Generated at 2022-06-14 05:29:10.046297
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def func(a = "default"):
        return config.get("a")

    assert func() == "default"
    assert func(define = ["a=toto"]) == "toto"
    assert func(define = ["a=toto", "a=tata"]) == "tata"

# Generated at 2022-06-14 05:29:14.776356
# Unit test for function overload_configuration
def test_overload_configuration():
    test_config = dict()

    def test_func_with_config(define=None):
        return True

    assert test_func_with_config(define="a=1,b=2")
    assert test_config["a"] == "1"
    assert test_config["b"] == "2"



# Generated at 2022-06-14 05:29:28.261397
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def myfunc(define):
        return define
    assert myfunc(define=["abc=3", "foo=bar"]) == ["abc=3", "foo=bar"]
    # The 2 parameters (abc, foo) should have been defined in config.
    assert config["abc"] == "3"
    assert config["foo"] == "bar"
    # Test with only one parameter defined
    assert myfunc(define=["abc=3"]) == ["abc=3"]
    assert config["abc"] == "3"
    assert config["foo"] == "bar"
    # Test with existing config
    assert myfunc(define=["abc=4", "foo=bar2"]) == ["abc=4", "foo=bar2"]
    assert config["abc"] == "4"

# Generated at 2022-06-14 05:29:30.886157
# Unit test for function current_commit_parser
def test_current_commit_parser():
    actual = current_commit_parser()
    expected = "semantic_release.commit_parser:default_commit_parser"
    assert actual != expected

# Generated at 2022-06-14 05:29:38.747010
# Unit test for function current_commit_parser
def test_current_commit_parser():
    config = _config()
    config['commit_parser'] = 'semantic_release.commit_parsers.parse_commit'
    parser = current_commit_parser()
    assert parser is not None
    assert parser.__name__ == 'parse_commit'

    config = _config()
    config['commit_parser'] = 'semantic_release.commit_parsers:parse_commit'
    parser = current_commit_parser()
    assert parser is not None
    assert parser.__name__ == 'parse_commit'

    # Given no commit_parser, the default parse_commit
    # is returned
    config = _config()
    del config['commit_parser']
    parser = current_commit_parser()
    assert parser is not None
    assert parser.__name__ == 'parse_commit'


# Generated at 2022-06-14 05:29:45.442479
# Unit test for function current_changelog_components
def test_current_changelog_components():
    import semantic_release.changelog_components as changelog_components

    assert current_changelog_components() == [
        changelog_components.date_component,
        changelog_components.type_header_component,
        changelog_components.requirements_header_component,
    ]

# Generated at 2022-06-14 05:29:49.179318
# Unit test for function overload_configuration
def test_overload_configuration():
    config["my_key"] = "old_configuration"
    @overload_configuration
    def func(define=None, my_key=None):
        return my_key
    assert func(define=["my_key=new_configuration"]) == "new_configuration"
    assert func() == "old_configuration"

# Generated at 2022-06-14 05:29:54.201681
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def example_func(define):
        return None

    assert example_func(define=[]) == None
    assert example_func(define=["a=1"]) == None
    assert config["a"] == "1"

# Generated at 2022-06-14 05:30:03.158440
# Unit test for function overload_configuration
def test_overload_configuration():
    """This test will use the overload_configuration decorator to edit an "overload" config
    for a function named f
    """

    def f(argument, define=None):
        """Function that prints its argument and the config dictionary
        """
        print("argument:", argument)
        print("config:", config)

    decorated_f = overload_configuration(f)
    decorated_f("value", define=["prop1=value1", "prop2=value2"])

    assert config["prop1"] == "value1"
    assert config["prop2"] == "value2"

# Generated at 2022-06-14 05:30:05.510113
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import components
    assert current_changelog_components() == [components.issue_reference, components.scope]



# Generated at 2022-06-14 05:30:23.810844
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    This decorator gets the content of the "define" array and edits "config"
    according to the pairs of key/value.
    """

    def test_func(arg1, arg2=0, define=[]):
        print(arg1, arg2, define)

    wrapped_func = overload_configuration(test_func)

    wrapped_func(1, 0, [])  # OK
    wrapped_func(1, 2, ["key=value"])  # OK
    wrapped_func(1, 2, ["key1=value1", "key2=value2"])  # OK
    wrapped_func(1, 2, ["key1=value1", "key2=value2", "key3=value3"])  # OK
    wrapped_func(1, define=["key=value"])  # OK
   

# Generated at 2022-06-14 05:30:27.543141
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config['changelog_components'] = 'semantic_release.changelog.components'
    assert len(current_changelog_components()) > 0

# Generated at 2022-06-14 05:30:38.731477
# Unit test for function overload_configuration
def test_overload_configuration():
    from . import cli
    from .api import verify_release_configuration
    from .context import is_dirty, has_local_changes, get_version

    # Cleanup config
    config.clear()

    # Test with no definition
    assert verify_release_configuration(get_version())
    assert not is_dirty()
    assert not has_local_changes()

    # Test with definition
    config["dirty_working_directory"] = "false"
    assert not is_dirty()

    config["dirty_working_directory"] = "true"
    assert is_dirty()

    config["dirty_working_directory"] = "is_true"
    assert is_dirty()

    config["dirty_working_directory"] = "is_false"
    assert is_dirty()

    # Test with args
    cli.verify_release_

# Generated at 2022-06-14 05:30:48.313775
# Unit test for function overload_configuration
def test_overload_configuration():
    _config = config
    @overload_configuration
    def func1(define):
        pass
    config = _config
    func1(define=["user_agent=test_user_agent", "release_limit=2"])
    assert config["user_agent"] == "test_user_agent"
    assert config["release_limit"] == "2"
    func1(define=["user_agent=test_user_agent", "release_limit=2"])
    assert config["user_agent"] == "test_user_agent"
    assert config["release_limit"] == "2"

# Generated at 2022-06-14 05:30:56.248524
# Unit test for function overload_configuration
def test_overload_configuration():
    config["package_name"] = "semantic_release"
    config["repository_url"] = "https://github.com/relekang/semantic-release"

    @overload_configuration
    def print_config():
        print(config["package_name"], config["repository_url"])

    assert print_config() == None

    # Overload configuration
    config["package_name"] = "semrel"
    config["repository_url"] = "https://github.com/relekang/semrel"

    @overload_configuration
    def print_config2(define: List[str]):
        print(config["package_name"], config["repository_url"])

    assert print_config2(define=["package_name=semrel"]) == None
    assert print_config

# Generated at 2022-06-14 05:31:05.764266
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """
    Tests the function current_changelog_components
    """
    from .changelog_components import (
        check_build,
        commit_messages,
        issue_closed,
        issue_type,
        merged_prs,
        pr_info,
    )
    components = [
        check_build,
        commit_messages,
        issue_closed,
        issue_type,
        merged_prs,
        pr_info,
    ]

    assert components == current_changelog_components()

# Generated at 2022-06-14 05:31:15.196893
# Unit test for function overload_configuration
def test_overload_configuration():
    # Given
    config["github_owner"] = "owner"
    config["github_repository"] = "repository"
    config["github_token"] = "token"
    config["github_token_secret"] = ""
    config["github_token_file"] = ""
    config["github_username"] = ""
    config["github_password"] = ""
    config["github_api_url"] = ""
    config["gitlab_repository"] = ""
    config["gitlab_token"] = ""
    config["gitlab_project"] = ""
    config["gitlab_api_url"] = ""
    config["gitlab_token_file"] = ""
    config["gitlab_username"] = ""
    config["gitlab_password"] = ""
    config["gitlab_ci_token"] = ""

    # When

# Generated at 2022-06-14 05:31:21.433427
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == [
        semantic_release.changelog.changelog_components.commit_title,
        semantic_release.changelog.changelog_components.commit_description,
        semantic_release.changelog.changelog_components.breaking_change_description,
    ]

# Generated at 2022-06-14 05:31:28.157774
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Test to check current_changelog_components.

    This test is to check whether current_changelog_components returns a list of
    callable functions.
    """
    _ = current_changelog_components()
    assert callable(
        current_changelog_components(
        )[0],
        "list of changelog_components should be callable",
    )

# Generated at 2022-06-14 05:31:35.078819
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == []
    config.update({"changelog_components": "semantic_release.components.changelog.build_changelog_components"})
    assert current_changelog_components() == [semantic_release.components.changelog.build_changelog_components]



# Generated at 2022-06-14 05:31:52.178824
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog_components import (
        add_issue_url,
        add_issue_numbers,
        add_breaking_change,
        add_github_issue_url,
    )

    components = current_changelog_components()

    assert len(components) == 4
    assert components[0] == add_issue_url
    assert components[1] == add_issue_numbers
    assert components[2] == add_breaking_change
    assert components[3] == add_github_issue_url

# Generated at 2022-06-14 05:31:55.778908
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from . import changelog

    components = current_changelog_components()
    assert len(components) == 2
    first, second = components
    assert first == changelog.feature_entry
    assert second == changelog.bugfix_entry

# Generated at 2022-06-14 05:32:03.404510
# Unit test for function overload_configuration
def test_overload_configuration():
    config["foo"] = "bar"
    config["fool"] = "baz"
    config["baz"] = "lol"

    @overload_configuration
    def test(**kwargs):
        return config

    configed = test(define=["foo=baz", "fool=bar", "baz=zabra"])

    assert configed["foo"] == "baz"
    assert configed["fool"] == "bar"
    assert configed["baz"] == "zabra"

# Generated at 2022-06-14 05:32:08.293088
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(define=None):
        assert config["test_key"] == "test_value"
    test_function(define=["test_key=test_value"])

# Generated at 2022-06-14 05:32:12.709318
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def config_example(define):
        return config

    expected = {"key_example": "value_example"}
    config_example(["key_example=value_example"])
    assert config == expected

# Generated at 2022-06-14 05:32:21.586858
# Unit test for function overload_configuration
def test_overload_configuration():
    assert config.get("check_build_status") is False
    assert config.get("patch_without_tag") is False
    assert config.get("upload_to_pypi") is False
    assert config.get("upload_to_release") is False

    @overload_configuration
    def configure(**kwargs):
        return kwargs

    new_config = configure(define=["check_build_status=True"])
    assert new_config is None
    assert config.get("check_build_status") is True
    assert config.get("patch_without_tag") is False
    assert config.get("upload_to_pypi") is False
    assert config.get("upload_to_release") is False


# Generated at 2022-06-14 05:32:26.970516
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_overload(define: str):
        pass

    params = ["key=value", "key2=value2"]
    modify_config = test_overload(define="key=value,key2=value2")
    assert config["key"] == "value"
    assert config["key2"] == "value2"

# Generated at 2022-06-14 05:32:30.123111
# Unit test for function current_changelog_components
def test_current_changelog_components():
    # test_error
    try:
        current_changelog_components()
    except ImproperConfigurationError:
        # should raise ImproperConfigurationError
        pass
    # test_success
    config["changelog_components"] = "semantic_release.changelog.get_breaking_changes,semantic_release.changelog.get_summary"
    try:
        current_changelog_components()
    except ImproperConfigurationError:
        raise AssertionError("Should not raise ImproperConfigurationError")

# Generated at 2022-06-14 05:32:31.989090
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() is not None



# Generated at 2022-06-14 05:32:37.647351
# Unit test for function overload_configuration
def test_overload_configuration():
    config_test = config.copy()
    config_test["dummy"] = "old"

    @overload_configuration
    def test(define):
        return config_test["dummy"]

    assert "dummy=new" in test.__wrapped__.__doc__
    assert test(define=["dummy=new"]) == "new"
    assert test() == "old"

# Generated at 2022-06-14 05:32:54.472910
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test that overload_configuration works as expected"""

    def tester(define=None):
        return "test"
    # Test that the decorator does nothing if there is no define parameter
    assert tester() == tester(overload_configuration(tester))
    # Test that the decorator does nothing if the define parameter is empty
    assert (tester(define=[]), {}) == (
        tester(overload_configuration(tester), define=[]),
        {}
    )
    # Test that the decorator modify destroy config if the define
    # parameter is full

# Generated at 2022-06-14 05:32:58.646400
# Unit test for function overload_configuration
def test_overload_configuration():
    from semantic_release.cli import main

    argv = ["scriptname", "major", "--define", "test_param=test_value"]
    main(argv=argv)

    assert config["test_param"] == "test_value"

# Generated at 2022-06-14 05:33:05.859950
# Unit test for function overload_configuration
def test_overload_configuration():
    config["custom_key"] = "original value"
    @overload_configuration
    def overloaded_function(define=None):
        if define is not None:
            if not isinstance(define, list):
                raise TypeError("define should be a list")
    overloaded_function(define=["custom_key=new value"])
    assert config["custom_key"] == "new value"

# Generated at 2022-06-14 05:33:15.382763
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_func(arg1, arg2, define=None):
        return [arg1, arg2]

    @overload_configuration
    def test_func2(arg1, arg2, define=None):
        return [arg1, arg2]

    assert test_func(1, 2) == [1, 2]
    assert test_func(1, 2, define=["key=value", "key2=value2"]) == [1, 2]
    assert test_func2(1, 2) == [1, 2]
    assert test_func2(1, 2, define=["key=value", "key2=value2"]) == [1, 2]
    assert config["key"] == "value"
    assert config["key2"] == "value2"



# Generated at 2022-06-14 05:33:19.203887
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import ChangelogEntry, VersionDiff

    config["changelog_components"] = "semantic_release.changelog.changelog"

    components = current_changelog_components()

    assert len(components) == 1
    assert components[0] == ChangelogEntry.diff_text



# Generated at 2022-06-14 05:33:31.168201
# Unit test for function current_commit_parser
def test_current_commit_parser():
    old_config = config.data.get('semantic_release', {})
    old_parser = config.data.get('commit_parser')

    config.data['semantic_release'] = {'commit_parser': 'semantic_release.commit_parser'}
    from semantic_release import commit_parser
    assert commit_parser == current_commit_parser()

    config.data['semantic_release'] = {'commit_parser': 'semantic_release.vcs_helpers.parse_commits'}
    from semantic_release.vcs_helpers import parse_commits
    assert parse_commits == current_commit_parser()

    config.data['semantic_release'] = old_config
    config.data['commit_parser'] = old_parser

# Generated at 2022-06-14 05:33:38.747951
# Unit test for function overload_configuration
def test_overload_configuration():
    _config["test"] = "test"

    @overload_configuration
    def test_func(define):
        assert config["test"] == "test"

    test_func(define=["test=new"])
    assert config["test"] == "new"
    test_func(define=["test=new", "new=new"])
    assert config["new"] == "new"
    assert config["test"] == "new"

# Generated at 2022-06-14 05:33:42.194685
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog.components import list_changes

    assert list_changes in current_changelog_components()

# Generated at 2022-06-14 05:33:46.618769
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    This function checks if overload_configuration overloads the config
    correctly
    """

    @overload_configuration
    def test_function(define):
        return define

    assert config["define"] == "test"  # should be the original config
    assert test_function(define="define=test") == "define=test"
    assert config["define"] == "test"  # should be overloaded

# Generated at 2022-06-14 05:33:52.756136
# Unit test for function overload_configuration
def test_overload_configuration():
    assert config["changelog_sections"] == "Features, Breaking changes, Fixes"

    @overload_configuration
    def test_load_config(define):
        return True

    test_load_config(define=["changelog_sections=Foo"])
    assert config["changelog_sections"] == "Foo"

# Generated at 2022-06-14 05:34:08.045474
# Unit test for function overload_configuration
def test_overload_configuration():
    CONFIG_KEY = "test_config_key"

    # Test that it works on a dummy function
    @overload_configuration
    def test_func(define=None):
        return

    test_func(define=["test_config_key=test_value"])
    assert config[CONFIG_KEY] == "test_value"

    # Test that it works on a function with arguments
    @overload_configuration
    def test_func_with_args(define=None, arg1=None):
        return

    test_func_with_args(define=["test_config_key=test_value"], arg1="test_arg")
    assert config[CONFIG_KEY] == "test_value"

# Generated at 2022-06-14 05:34:11.677356
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config["changelog_components"] = "semantic_release.history.components.JiraIssue"
    components = current_changelog_components()
    assert components == [semantic_release.history.components.JiraIssue]

# Generated at 2022-06-14 05:34:16.362145
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(*args, **kwargs):
        return kwargs

    assert test_function(define=["foo=bar"])["define"] == ["foo=bar"]



# Generated at 2022-06-14 05:34:21.109277
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """Import the commit_parser in setup.cfg"""

    # Arrange
    # Set up config:
    config["commit_parser"] = "semantic_release.commit_parser.parse"

    # Act
    # Try to import the function
    current_commit_parser()

    # Assert
    # Should not fail



# Generated at 2022-06-14 05:34:30.655764
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    This function tests that the key and value are to be added in the config dictionary
    """
    @overload_configuration
    def f(define):
        """
        :param define: An array of key value
        """
        return None

    # define has a wrong format
    assert f(define=["com=1"]) == None, "Config dictionary was not updated"
    assert len(config) == 1, "Config dictionary was not updated"
    assert config["com"] == "1", "Config dictionary was not updated"

    # define is empty
    f(define=[])
    assert len(config) == 2, "Config dictionary was not updated"

# Generated at 2022-06-14 05:34:36.125572
# Unit test for function overload_configuration
def test_overload_configuration():
    try:
        original_value = config["commit_parser"]
    except KeyError:
        original_value = None
    assert current_commit_parser()
    @overload_configuration
    def test(define):
        pass
    # Overload the value
    test(define="commit_parser=semantic_release.commit_parser:conventional_commit_parser")
    assert not original_value == current_commit_parser()

# Generated at 2022-06-14 05:34:49.502838
# Unit test for function overload_configuration
def test_overload_configuration():
    import inspect
    from .config import config

    # Create a dummy function that can be decorated
    @overload_configuration
    def dummy(define: str):
        """Dummy function for testing"""
        # No op
        pass

    # Test the function wrapper (in case decorator changes)
    assert dummy.__name__ == "dummy"
    assert dummy.__doc__ == "Dummy function for testing"

    # Test calling the wrapped function that takes 'define'
    # and doesn't change anything
    assert dummy() == None

    # Test calling the wrapped function that takes 'define'
    # and changes something
    assert dummy(define="debug=true") == None
    assert config["debug"] == "true"

    # Test calling the wrapped function that takes 'define'
    # that contains a pair of key/value

# Generated at 2022-06-14 05:34:53.625677
# Unit test for function overload_configuration
def test_overload_configuration():
    """Tests decorator overload_configuration"""

    @overload_configuration
    def my_function(define):
        """This function just adds define args to config"""
        assert config["a"] == "b"
        assert config["c"] == "d"
        assert config["e"] == "f"
        assert len(define) == 3

    my_function(define=["a=b", "c=d", "e=f"])

# Generated at 2022-06-14 05:35:05.445141
# Unit test for function overload_configuration
def test_overload_configuration():
    # Test: set up a fake config
    config["foo"] = "bar"
    # assert that it is set
    assert config["foo"] == "bar"
    # Test: decorate a function to overload the config
    @overload_configuration
    def fake_function(define: List[str]):
        if "foo" in kwargs:
            return kwargs["foo"]
        else:
            raise Exception("No value for foo in the kwargs")
    # Test: call it with define that sets "foo" to "baz"
    new_value = fake_function(define=["foo=baz"])
    # assert that it is set to the new value
    assert new_value == "baz"

# Generated at 2022-06-14 05:35:11.304514
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release import components

    components = current_changelog_components()
    assert hasattr(components[0], "__name__")
    assert components[0].__name__ == "IssueClosingComponent"
    assert hasattr(components[1], "__name__")
    assert components[1].__name__ == "MergeRequestsClosingComponent"

# # Unit test for function current_commit_parser
# def test_current_commit_parser():
#     from semantic_release import commit_parser
#
#     assert hasattr(current_commit_parser(), "__name__")
#     assert current_commit_parser().__name__ == "parse_commits"

# Generated at 2022-06-14 05:35:27.335989
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from . import changelog

    try:
        config["changelog_components"] = "semantic_release.changelog.format_changelog"
        assert current_changelog_components()[0] == changelog.format_changelog
    except ImproperConfigurationError:
        pass

    try:
        config["changelog_components"] = ""
        assert current_changelog_components() == []
    except ImproperConfigurationError:
        pass

    try:
        config["changelog_components"] = "semantic_release.changelog.format_changelog"
        changelog.format_changelog = None
        assert current_changelog_components() == []
    except ImproperConfigurationError:
        pass


# Generated at 2022-06-14 05:35:39.764640
# Unit test for function overload_configuration
def test_overload_configuration():
    # GIVEN
    config['version_pattern'] = "v{number}"
    config['changelog_components'] = "foo"
    config['no_override_settings'] = False
    config['changelog_scope'] = False

    @overload_configuration
    def get_config(arg):
        return config[arg]

    # WHEN
    version_pattern = get_config('version_pattern', define=['version_pattern=v{release_level}.{mayor}.{minor}'])
    no_override_settings = get_config('no_override_settings', define=["no_override_settings"])
    changelog_components = get_config('changelog_components', define=['changelog_components=bar'])
    changelog_scope = get_config

# Generated at 2022-06-14 05:35:44.724870
# Unit test for function overload_configuration
def test_overload_configuration():
    # mock load, we don't want to use loads here
    UserDict.load = UserDict.update
    # mock get, we don't want to use real get here
    UserDict.get = UserDict.__getitem__

    def parse(*args, **kwargs):
        return config

    parse = overload_configuration(parse)
    parse(define=["commit_parser=subdir.subdir2:parse"])
    assert config.get("commit_parser") == "subdir.subdir2:parse"

# Generated at 2022-06-14 05:35:53.250187
# Unit test for function overload_configuration
def test_overload_configuration():
    config["hello"] = "world"

    @overload_configuration
    def test_function(**kwargs):
        return config["hello"]

    assert test_function(define=["hello=world2"]) == "world2"
    assert test_function(define=["hello=world3"]) == "world3"
    assert test_function(define=["hello=world3", "hello2=world3"]) == "world3"
    assert test_function() == "world"

# Generated at 2022-06-14 05:35:56.475439
# Unit test for function current_changelog_components
def test_current_changelog_components():
    #This function will always return a list, because when it has to raise an exception,
    #it does it
    current_changelog_components()

# Generated at 2022-06-14 05:36:04.863269
# Unit test for function overload_configuration
def test_overload_configuration():
    try:
        @overload_configuration
        def some_function(arg, define=None):
            return config.get("foo")

        some_function("arg", define=["foo=42", "bar=hello world"])
        assert False
    except ImproperConfigurationError as e:
        pass

    @overload_configuration
    def some_function(arg, define=None):
        return config.get("foo")

    assert some_function("arg", define=["foo=42"]) == "42"
    assert config.get("foo") == "42"

# Generated at 2022-06-14 05:36:16.227973
# Unit test for function overload_configuration
def test_overload_configuration():
    config.clear()
    config.update(
        {
            "token": "token",
            "repo": "repo",
            "dry_run": False,
            "branch_name": "master",
            "commit_message": "v{new_version}",
            "tag_name": "v{new_version}",
            "tag_message": "Version {new_version}",
            "build_cmd": "./build.sh",
            "build_grace": "0",
            "ssh_host": "host",
            "ssh_port": "22",
        }
    )

    def assert_config(**kwargs):
        assert kwargs["define"] == "token=toto repo=toto"
        assert config["token"] == "toto"

# Generated at 2022-06-14 05:36:18.335149
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser().__name__ == "default_commit_parser"

# Generated at 2022-06-14 05:36:25.494309
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def foo(**kwargs):
        return config["foo"]

    # Don't overload
    assert foo() == config["foo"]
    assert foo(bar=42) == config["foo"]

    # Overload
    assert foo(define=["foo=bar"]) == "bar"
    assert foo(define=["foo=bar", "baz=42"]) == "bar"

# Generated at 2022-06-14 05:36:27.444736
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser()
    assert callable(current_commit_parser())

# Generated at 2022-06-14 05:36:35.595031
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert callable(current_commit_parser())

# Generated at 2022-06-14 05:36:40.516926
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "test"
    @overload_configuration
    def dummy_decorated_function(test):
        return test
    assert dummy_decorated_function(define=["test=value"]) == "value"

# Generated at 2022-06-14 05:36:48.227434
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    Test to ensure that the configuration dictionary is updated properly
    """
    config["test"] = "testing"
    config["number"] = 1
    assert config["test"] == "testing"
    assert config["number"] == 1

    @overload_configuration
    def test_update(define: str):
        pass

    test_update(define="test=updated,number=2")
    assert config["test"] == "updated"
    assert config["number"] == "2"