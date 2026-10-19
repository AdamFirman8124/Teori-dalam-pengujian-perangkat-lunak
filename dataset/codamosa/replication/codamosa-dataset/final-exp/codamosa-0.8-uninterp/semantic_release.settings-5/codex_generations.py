

# Generated at 2022-06-14 05:26:56.393255
# Unit test for function current_changelog_components
def test_current_changelog_components():
    try:
        config["changelog_components"] = "semantic_release.output.changelog.writer.writer"
        _ = current_changelog_components()
    except ImproperConfigurationError as e:
        logger.error(e)
        raise



# Generated at 2022-06-14 05:27:00.541907
# Unit test for function current_changelog_components
def test_current_changelog_components():
    import semantic_release.changelog

    components = current_changelog_components()
    for component in components:
        assert hasattr(semantic_release.changelog, component.__name__)



# Generated at 2022-06-14 05:27:06.874331
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .components import (
        commit_message,
        commit_subject,
        commit_author,
        commit_hash,
        commit_time,
    )
    assert sorted(
        current_changelog_components(), key=lambda cmpt: cmpt.__name__
    ) == sorted(
        [
            commit_message,
            commit_subject,
            commit_author,
            commit_hash,
            commit_time,
        ],
        key=lambda x: x.__name__,
    )

# Generated at 2022-06-14 05:27:11.415080
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def f():
        pass

    assert config["patch_without_tag"] is False
    f(define=["patch_without_tag=true"])
    assert config["patch_without_tag"] is True



# Generated at 2022-06-14 05:27:16.324141
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == [
        semantic_release.changelog_components.build_changelog,
        semantic_release.changelog_components.version_components,
        semantic_release.changelog_components.commit_change_type,
    ]

# Generated at 2022-06-14 05:27:23.090855
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(config_param):
        return config.get(config_param)

    assert test_function("token_url") == "https://github.com/login/oauth/access_token"
    assert test_function("token_url", define=["token_url=http://test.com"]) == "http://test.com"
    assert test_function("repository_url", define=["token_url=http://test.com"]) == "https://github.com/<owner>/<name>"

# Generated at 2022-06-14 05:27:25.060475
# Unit test for function current_commit_parser
def test_current_commit_parser():
    config.get = lambda arg: arg

    assert current_commit_parser() == "commit_parser"

# Generated at 2022-06-14 05:27:27.737795
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def a():
        return config["key"]
    
    assert a(define=["key=foo", "bar=baz"]) == "foo"

# Generated at 2022-06-14 05:27:39.580015
# Unit test for function overload_configuration
def test_overload_configuration():
    from semantic_release.hvcs import get_hvcs_repository

    original_config = config.copy()
    original_get_hvcs_repository = get_hvcs_repository
    original_get_hvcs_repository.__wrapped__ = original_get_hvcs_repository

    @overload_configuration
    def dummy():
        pass

    # Test overload_configuration with no pairs of key/value
    dummy()
    assert original_config == config
    assert original_get_hvcs_repository.__wrapped__ == get_hvcs_repository

    # Test overload_configuration with one pair of key/value
    dummy(define=["full_name=semantic_release"])
    assert "full_name" in config

# Generated at 2022-06-14 05:27:51.025074
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser()(
        "commit message"
    ) == "commit message", "Message without format should work"
    assert (
        current_commit_parser()("feat(foo): commit message")
        == "feat foo: commit message"
    ), "Scope should be added"
    assert (
        current_commit_parser()(
            "feat(foo): commit message\n\nBREAKING CHANGE: something is broken"
        )
        == "feat foo: commit message\n\nBREAKING CHANGE: something is broken"
    ), "Breaking change should be preserved"

# Generated at 2022-06-14 05:28:01.986218
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """Test with a valid configuration"""
    config['commit_parser'] = 'semantic_release.commit_parser.parse_commits'
    assert current_commit_parser()



# Generated at 2022-06-14 05:28:06.448891
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(arg1, define=None):
        return arg1

    result = test_function("test", define=["foo=bar"])
    assert result == "test"
    assert config["foo"] == "bar"

    result = test_function("test", define=["foo=bar", "foo=baz"])
    assert result == "test"
    assert config["foo"] == "baz"

# Generated at 2022-06-14 05:28:16.382786
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Function current_changelog_components returns a list of components"""
    expected = ['changelog_components.component1', 'changelog_components.component2']
    config['changelog_components'] = expected[0]+','+expected[1]
    components = current_changelog_components()
    assert len(components) == 2
    assert components[0].__name__ == expected[0].split('.')[1]
    assert components[1].__name__ == expected[1].split('.')[1]

# Generated at 2022-06-14 05:28:17.500032
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert config.get("changelog_components") == "semantic_release.changelog.components.from_commits"

# Generated at 2022-06-14 05:28:24.662019
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def func(a, b, define=None):
        return a + b
    assert func(1, 2) == 3
    # Get the default configuration
    default_dict = config.copy()
    # Test a simple overload (changelog_capitalize)
    func(1, 2, define=["changelog_capitalize=false"])
    assert config["changelog_capitalize"] == "false"
    # Cleanup
    config.clear()
    config.update(default_dict)

# Generated at 2022-06-14 05:28:36.365730
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    This function checks that the function overload_configuration works as
    intended.
    """
    from click.testing import CliRunner
    from semantic_release.cli import main as cli_main

    # Test with a command including the optional argument "define"
    runner = CliRunner()
    result = runner.invoke(cli_main, ["check", "--define", "custom_releaser=custom_releaser"])
    assert result.exit_code == 0
    runner.invoke(cli_main, ["--help"])
    assert result.exit_code == 0
    assert config["custom_releaser"] == "custom_releaser"

# Generated at 2022-06-14 05:28:42.200268
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_key"] = "test_value"
    assert config["test_key"] == "test_value"
    @overload_configuration
    def func():
        return None
    func(define=["test_key=overloaded_value"])
    assert config["test_key"] == "overloaded_value"

# Generated at 2022-06-14 05:28:49.679327
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from semantic_release.history.commit_parser import default_parser
    assert current_commit_parser() is default_parser
    config.get = lambda *args, **kwargs: "semantic_release.history.parser.jetbrains_parser"
    from semantic_release.history.jetbrains_parser import jetbrains_parser
    assert current_commit_parser() is jetbrains_parser



# Generated at 2022-06-14 05:28:54.318405
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_name"] = "start"
    @overload_configuration
    def test(name):
        return name

    assert test(name="start") == "start"
    assert test(name="start", define=["test_name=end"]) == "end"



# Generated at 2022-06-14 05:28:58.473414
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test configuration value can be overloaded"""
    assert config.get("major_on_zero") is True
    assert config.get("remove_dist") is True



# Generated at 2022-06-14 05:29:11.452205
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(a, b, c, define=None):
        assert config["foo"] == "bar"

    config["foo"] = "not bar"
    test_function(a=1, b=2, c=3, define=["foo=bar"])



# Generated at 2022-06-14 05:29:18.187081
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    Tests if the function overload_configuration overrides the old config
    values when the define argument is specified.
    """
    global config
    # We want to test the setup.cfg configuration, not the defaults.cfg
    # configuration.
    cwd = getcwd()
    ini_paths = [os.path.join(cwd, "setup.cfg")]
    config = _config_from_ini(ini_paths)

    @overload_configuration
    def test_config(define):
        return config

    config_before_overload = config.copy()
    test_config(define="commit_parser=semantic_release.commit_parser")
    assert config_before_overload != config
    assert "semantic_release.commit_parser" == config["commit_parser"]

# Generated at 2022-06-14 05:29:21.104783
# Unit test for function current_changelog_components
def test_current_changelog_components():
    try:
        current_changelog_components()
    except ImproperConfigurationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 05:29:23.136713
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from .commit_parser import parse_commits
    assert current_commit_parser() == parse_commits


# Generated at 2022-06-14 05:29:29.593942
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config['changelog_components'] = 'semantic_release.changelog.standard_changelog,tests.test_changelog.test_changelog'
    assert len(current_changelog_components()) == 2
    config['changelog_components'] = 'semantic_release.changelog.standard_changelog'
    assert len(current_changelog_components()) == 1

# Generated at 2022-06-14 05:29:35.349376
# Unit test for function overload_configuration

# Generated at 2022-06-14 05:29:47.426847
# Unit test for function overload_configuration
def test_overload_configuration():
    from unittest.mock import patch

    def test_func(one, define):
        return one

    test_args = ['value']
    with patch('semantic_release.settings.current_commit_parser') as mock_parser:
        test_func = overload_configuration(test_func)
        test_func(*test_args, define=['commit_parser=test_commit_parser'])
        assert mock_parser.called is False
    with patch('semantic_release.settings.current_commit_parser') as mock_parser:
        test_func(*test_args, define=['commit_parser=semantic_release.hacks.parse_commit'])
        assert mock_parser.called

    with patch('semantic_release.settings.current_changelog_components') as mock_components:
        test_func

# Generated at 2022-06-14 05:29:57.383969
# Unit test for function overload_configuration
def test_overload_configuration():
    global config
    # Test with one pair key/value
    test_dict = {"define": ["key=value"]}
    overload_configuration(lambda x: x)(test_dict)
    assert isinstance(config, dict)
    assert config["key"] == "value"
    # Test with multiple pairs key/value
    test_dict = {"define": ["key1=value1", "key2=value2"]}
    overload_configuration(lambda x: x)(test_dict)
    assert config["key1"] == "value1"
    assert config["key2"] == "value2"
    # Test with wrong syntax
    test_dict = {"define": ["key1=value1", "wrong_syntax", "key2=value2"]}

# Generated at 2022-06-14 05:30:03.426833
# Unit test for function overload_configuration
def test_overload_configuration():
    class A:
        @overload_configuration
        def foo(self):
            self.bar = config.get("plugin_config", dict())

    ss = A()
    ss.foo()
    assert ss.bar == dict()

    ss.foo(define=["plugin_config.foo=bar"])
    assert ss.bar == {"foo": "bar"}



# Generated at 2022-06-14 05:30:06.812122
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def foo(define):
        pass

    foo(["foo=bar"])
    assert config["foo"] == "bar"

    foo(["foo=baz", "bar=1"])
    assert config["foo"] == "baz"
    assert config["bar"] == "1"

# Generated at 2022-06-14 05:30:19.810963
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test(define=None):
        print(f"{config}")

    load_config = {"define": ["major_on_zero=True"]}
    test(**load_config)

# Generated at 2022-06-14 05:30:23.156984
# Unit test for function overload_configuration
def test_overload_configuration():
    """Overload configure function with a non-existing entry"""
    @overload_configuration
    def foo():
        return config.get("foo")

    assert foo(define=["foo=bar"]) == "bar"
    assert foo() is None

# Generated at 2022-06-14 05:30:31.252486
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    This function tests if the overload_configuration function works well.
    """
    is_config_updated = False
    config["testparam"] = False
    f = overload_configuration(lambda define: [setattr(item, "commit_parser", "") for item in define])
    f(define=["testparam=True"])

    if config["testparam"]:
        is_config_updated = True

    assert is_config_updated

# Generated at 2022-06-14 05:30:38.315368
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_func(parameter):
        return config[parameter]

    # Test command line overriding
    test_func.__wrapped__.__defaults__ = (None,)
    test_func.__wrapped__.__defaults__ = {"parameter": "test_value"}

    assert test_func.__wrapped__("test_value") == "test_value"
    assert test_func.__wrapped__(parameter="test_value") == "test_value"

# Generated at 2022-06-14 05:30:50.586993
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test(arg):
        return arg

    assert test("foo") == "foo"
    # The same test with a value in the kwargs
    assert test("foo", define="bar=baz") == "foo"
    # Overload a value
    assert test("foo", define="remove_dist=False") == "foo"
    # Overload a value and check that it is the right one
    assert test("foo", define="remove_dist=False") == "foo"
    assert config["remove_dist"] is False
    # Test with more than one value
    assert test("foo", define="bar=baz,test=test") == "foo"
    assert config["bar"] == "baz"
    assert config["test"] == "test"

# Generated at 2022-06-14 05:30:55.088710
# Unit test for function overload_configuration
def test_overload_configuration():
    """This tests the overload_configuration function.
    """

    @overload_configuration
    def test_function(define=None):
        if define is not None:
            return True

    assert not test_function()
    assert test_function(define="test=test")
    assert "test" not in config
    assert test_function(define="test=test")
    assert config["test"] == "test"

# Generated at 2022-06-14 05:31:04.629929
# Unit test for function overload_configuration
def test_overload_configuration():
    """This test overloads the defined_param configuration with the keys
    "hello" and "world" and tests that their values are correctly defined.
    """

    config["hello"] = ""
    config["world"] = ""

    def my_func(define=None):
        return config

    with overload_configuration(my_func) as modif_func:
        modif_func(define=["hello=1", "world=2"])
        assert (config["hello"]) == "1"
        assert (config["world"]) == "2"

# Generated at 2022-06-14 05:31:14.025957
# Unit test for function overload_configuration
def test_overload_configuration():
    config = {"test": "unit_test", "server": "dashboard"}
    func = overload_configuration(lambda **kwargs: kwargs["config"])
    assert func(define=["test=new_value"], config=config) == {
        "test": "new_value",
        "server": "dashboard",
    }
    assert func(define=["server=new_dashboard", "test=new_value"], config=config) == {
        "test": "new_value",
        "server": "new_dashboard",
    }
    assert func(define=["server=new_dashboard"], config=config) == {
        "test": "unit_test",
        "server": "new_dashboard",
    }

# Generated at 2022-06-14 05:31:18.085245
# Unit test for function overload_configuration
def test_overload_configuration():
    def func(**kwargs):
        return config.get("release_script")

    func = overload_configuration(func)
    assert func(define=["release_script=hello"]) == "hello"

# Generated at 2022-06-14 05:31:26.505224
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """Test the current_commit_parser function to check it return the
    correct commit parser function
    """
    from semantic_release.commit_parser import parse_commit

    from semantic_release import main
    import os

    with open(
        "{}/setup.cfg".format(os.path.dirname(main.__file__)), "w"
    ) as setup_file:
        setup_file.write(
            "[semantic_release]\n"
            "commit_parser = semantic_release.commit_parser.parse_commit\n"
        )

    assert (
        current_commit_parser()
        == "semantic_release.commit_parser.parse_commit"
    )



# Generated at 2022-06-14 05:31:37.872365
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """
    :raises ImproperConfigurationError: if the unit test fails
    """
    config["commit_parser"] = "semantic_release.commit_parser:parse_commits"
    assert current_commit_parser()

# Generated at 2022-06-14 05:31:46.594333
# Unit test for function overload_configuration
def test_overload_configuration():
    # pylint: disable=unused-variable
    @overload_configuration
    def func(args, define=None):
        # pylint: disable=pointless-statement
        args, define
        return define is None

    assert func("dummy")
    assert func("dummy", define=["a=b", "c=d"])
    assert func("dummy", define=["a=b", "c=d", "e=f"])
    assert not func("dummy", define=["a=b", "c=d", "e=f", "g=h=i"])

# Generated at 2022-06-14 05:31:59.445509
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    This unit test checks the expected behavior of the
    overload_configuration decorator.
    """

    @overload_configuration
    def test_func(key, value):
        config[key] = value

    @overload_configuration
    def test_func_no_define(key, value):
        config[key] = value

    test_func("test_key", "test_value", define=["test_key=test_value_overloaded"])
    assert config["test_key"] == "test_value_overloaded"

    # Test that if there is no "define" kwarg, the function still works
    test_func_no_define("test_key_no_define", "test_value_no_define")

# Generated at 2022-06-14 05:32:05.416098
# Unit test for function overload_configuration
def test_overload_configuration():
    with overload_configuration:
        config["new_param"] = "first_value"
        overload_configuration(lambda x, define=["new_param=second_value"]: None)(0)
        assert config["new_param"] == "second_value"
        overload_configuration(lambda x, define=["new_param=third_value"]: None)(0)
        assert config["new_param"] == "third_value"



# Generated at 2022-06-14 05:32:11.751383
# Unit test for function overload_configuration
def test_overload_configuration():
    # Define a dummy function
    def dummy_function(foo, bar, define):
        return foo, bar

    func = overload_configuration(dummy_function)
    func("foo", "bar", define=["release_type="])

    # Assert the release type is correctly set in the config
    assert config.release_type is ""

# Generated at 2022-06-14 05:32:13.356711
# Unit test for function current_changelog_components
def test_current_changelog_components():
    components = current_changelog_components()
    assert len(components) == 2

# Generated at 2022-06-14 05:32:18.337950
# Unit test for function overload_configuration
def test_overload_configuration():
    # First we need to create a dummy object
    def test_function(**kwargs):
        pass

    # Then we should get the dummy object's content by using the overload_configuration decorator
    overload_configuration(test_function)(
        define=["semantic_release.commit_parser=semantic_release.hvcs.bitbucket_client.parse_commit"]
    )

    # The content in config should be edited by the definition in 'define'
    assert config.get("commit_parser") == "semantic_release.hvcs.bitbucket_client.parse_commit"

# Generated at 2022-06-14 05:32:26.761363
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test that parameter "define" can be used to overload
    the configuration.
    """
    @overload_configuration
    def get_config(key):
        return config[key]

    assert get_config("upload_to_pypi") == "false"

    # Overload a fake parameter
    assert get_config("fake_param", define=["fake_param=test"]) == "test"

    # Overload a real parameter
    assert get_config("upload_to_pypi", define=["upload_to_pypi=true"]) == "true"

# Generated at 2022-06-14 05:32:30.218720
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == [
        semantic_release.changelog.components.breaking_changes,
        semantic_release.changelog.components.features,
        semantic_release.changelog.components.fixes,
    ]

# Generated at 2022-06-14 05:32:37.478252
# Unit test for function overload_configuration
def test_overload_configuration():
    # Test with a new parameter
    @overload_configuration
    def foo(define=None):
        return config["new_param"]

    foo(["new_param=value"])
    assert config["new_param"] == "value"

    # Test with an existing parameter
    @overload_configuration
    def foo(define=None):
        return config["config_version"]

    foo(["config_version=2"])
    assert config["config_version"] == "2"

# Generated at 2022-06-14 05:32:52.105802
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import (
        create_header,
        create_summary,
        create_dependencies,
    )
    from .tests.test_repository import test_changelog_components

    assert create_header in test_changelog_components
    assert create_summary in test_changelog_components
    assert create_dependencies in test_changelog_components

    assert current_changelog_components() == test_changelog_components

# Generated at 2022-06-14 05:32:58.228774
# Unit test for function overload_configuration
def test_overload_configuration():
    def func(x):
        return x

    func = overload_configuration(func)
    assert func("a") == "a"
    assert func("a", define=["b=1", "c=2"]) == "a"
    assert config.get("b") == "1"
    assert config.get("c") == "2"

# Generated at 2022-06-14 05:33:10.864646
# Unit test for function overload_configuration
def test_overload_configuration():
    # Pretend that we are in the root folder
    config["dry_run"] = False
    config["commit_version_number"] = True
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["remove_dist"] = False
    config["commit_version_number"] = True
    config["git_push"] = True

    @overload_configuration
    def test_func(**kwargs):
        return

    assert config.get("dry_run") == False

    @overload_configuration
    def test_func(**kwargs):
        return

    assert config.get("dry_run") == False

    @overload_configuration
    def test_func(**kwargs):
        return

    assert config.get("dry_run") == False


# Generated at 2022-06-14 05:33:16.098981
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test the decorator overload_configuration"""

    def func(key):
        """Simple function which returns the value of the key in config"""
        return config.get(key)

    func = overload_configuration(func)

    assert func("key") == None
    assert func("define", define=["key=val"]) == "val"
    assert func("key") == None

# Generated at 2022-06-14 05:33:19.634402
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def func(*args, **kwargs):
        return config

    # Test that a define that would not alter the configuration is ignored
    assert func(define=["foo=bar"]) == _config()

    # Test that a define that would alter the configuration is applied
    assert func(define=["no_confirm=True"])["no_confirm"] == "True"

# Generated at 2022-06-14 05:33:31.972218
# Unit test for function overload_configuration
def test_overload_configuration():
    """This test check that the decorator overload_configuration is correctly
    updating the config
    """

    def dummy():
        return config

    @overload_configuration
    def test_overload_with_no_params():
        return config

    assert dummy() == {"hello": "world"}

    # Adding a new parameter
    test_overload_with_no_params(define="define=yes")
    assert config == {"hello": "world", "define": "yes"}

    # Overloading parameter
    test_overload_with_no_params(define="hello=world")
    assert config == {"hello": "world", "define": "yes"}

    # Overloading parameter (only key provided)
    test_overload_with_no_params(define="hello")

# Generated at 2022-06-14 05:33:43.481572
# Unit test for function current_changelog_components
def test_current_changelog_components():
    # Mock the current config with changelog components
    config = UserDict({"changelog_components": "fake_component_paths.component_1,fake_component_paths.component_2"})
    # Verify the mock
    assert config.get("changelog_components") == "fake_component_paths.component_1,fake_component_paths.component_2"
    # Call the function which will parse the config
    components = current_changelog_components()

    assert len(components) == 2
    assert components[0].__name__ == "component_1"
    assert components[1].__name__ == "component_2"

# Generated at 2022-06-14 05:33:57.144140
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def f(a, b, **kwargs):
        return kwargs

    assert f(1, 2, define=["a=b"]) == {"define": ["a=b"]}
    assert config == {"a": "b"}

    assert f(1, 2, define=["a=c", "b=d"]) == {"define": ["a=c", "b=d"]}
    assert config == {"a": "c", "b": "d"}

    assert f(1, 2, define=["a=c", "b=d", "c"]) == {"define": ["a=c", "b=d", "c"]}
    assert config == {"a": "c", "b": "d"}
    assert f(1, 2) == {}

# Generated at 2022-06-14 05:34:04.705575
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    Verify overload_configuration works as intended
    """
    def foo(define=[], **kwargs):
        return define
    foo = overload_configuration(foo)
    assert foo() == []
    assert foo(define=["blaz=2"]) == ["blaz=2"]
    assert foo(define=["blaz=2", "1=2"]) == ["blaz=2", "1=2"]
    assert foo(define=["blaz"]) == []
    assert foo(define=["blaz", "1=2"]) == ["1=2"]

# Generated at 2022-06-14 05:34:08.915371
# Unit test for function overload_configuration
def test_overload_configuration():
    config = {}
    @overload_configuration
    def test_func(define=None):
        return

    test_func(define=["a=1", "a=2"])
    assert config == {"a": "2"}

# Generated at 2022-06-14 05:34:21.364450
# Unit test for function overload_configuration
def test_overload_configuration():
    from semantic_release.cli import set_config
    from semantic_release.cli import config

    original_config = {"name": "original value"}
    config.update(original_config)

    set_config(define=["name=new value"])
    assert config["name"] == "new value"

    config.update(original_config)

# Generated at 2022-06-14 05:34:30.050567
# Unit test for function overload_configuration
def test_overload_configuration():
    assert config["commit_parser"] == "semantic_release.commit_parser"
    assert config["changelog_components"] == "semantic_release.changelog.components"

    @overload_configuration
    def test_function(arg1, arg2, define=None):
        return arg1, arg2

    test_function('a', 'b', define=['changelog_components=c','commit_parser=d'])
    assert config["commit_parser"] == 'd'
    assert config["changelog_components"] == 'c'

# Generated at 2022-06-14 05:34:38.066058
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def add(x, y):
        return x + y

    # Load the initial config
    from .config import config as initial_config
    assert config != initial_config
    # Restore the initial config
    from .config import config as initial_config
    assert config == initial_config

    # Load the initial config
    from .config import config as initial_config
    assert config != initial_config
    # Restore the initial config
    from .config import config as initial_config
    assert config == initial_config

    # Load the initial config
    from .config import config as initial_config
    assert config != initial_config
    # Restore the initial config
    from .config import config as initial_config
    assert config == initial_config

# Generated at 2022-06-14 05:34:45.902600
# Unit test for function overload_configuration
def test_overload_configuration():
    config["name"] = "original"
    @overload_configuration
    def my_func(name, define=None):
        return "This is name " + name

    assert my_func(name="default_value", define=["name=overwrite"]) == "This is name overwrite"
    assert config["name"] == "overwrite"
    assert my_func(name="default_value") == "This is name default_value"
    assert config["name"] == "overwrite"

# Generated at 2022-06-14 05:34:46.999308
# Unit test for function overload_configuration
def test_overload_configuration():
    assert config["check_build_status"] is False



# Generated at 2022-06-14 05:34:50.655853
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test overload_configuration decorator.
    """

    @overload_configuration
    def function(define):
        print(config['test'])

    function(['test=test_value'])
    assert config['test'] == 'test_value'

# Generated at 2022-06-14 05:34:57.555026
# Unit test for function overload_configuration
def test_overload_configuration():
    # pylint: disable=missing-function-docstring,missing-class-docstring,no-self-use
    class SomeClass:

        @overload_configuration
        def some_func(self, arg1, arg2, arg3, define=None):
            pass

    some_class = SomeClass()
    some_class.some_func("a", "b", "c", define=["a=b"])
    assert config["a"] == "b"

# Generated at 2022-06-14 05:35:02.833112
# Unit test for function overload_configuration
def test_overload_configuration():
    class Tester():
        def __init__(self):
            self.test_var = "Tester variable"

        @overload_configuration
        def do_something(self, define = None):
            self.test_var = config["test_var"]

    tester = Tester()
    assert tester.test_var == "Tester variable"
    tester.do_something(define = ["test_var=modified variable"])
    assert tester.test_var == "modified variable"

# Generated at 2022-06-14 05:35:10.538050
# Unit test for function overload_configuration
def test_overload_configuration():
    config['plugin_config'] = {"option1": "value1", "option2": "value2"}
    config['strategy'] = 'post-release'

    @overload_configuration
    def test_function(define=None):
        return config

    assert test_function(define=['plugin_config.option1=value3', 'strategy=pre-release']) == \
        {
            'plugin_config': {'option1': 'value3', 'option2': 'value2'},
            'strategy': 'pre-release'
        }

# Generated at 2022-06-14 05:35:23.015827
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function tests that the decorator load_config works
    as expected.
    """

    import semantic_release

    # global "config" needs to be reset
    semantic_release._config.update(_config())

    @overload_configuration
    def print_config_define(define=None):
        out = str(config["python"])
        out += " " + str(define)
        return out

    assert print_config_define() == "python=3.6 None"
    assert print_config_define(define=["python=2.7"]) == "python=2.7 ['python=2.7']"
    assert print_config_define(define=["python=2.7", "test=test2"]) == "python=2.7 ['python=2.7', 'test=test2']"

# Generated at 2022-06-14 05:35:34.809781
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test(name):
        return config[name]

    config["name"] = "tom"
    assert test("name") == "tom"
    assert test(name="name", define=["name=jerry"]) == "jerry"

# Generated at 2022-06-14 05:35:37.721479
# Unit test for function current_changelog_components
def test_current_changelog_components():
    components = current_changelog_components()
    assert len(components) == 1
    assert components[0].__name__ == "components"

# Generated at 2022-06-14 05:35:42.177505
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_func(a):
        assert config["test_1"] == "test_2"
        assert config["test_3"] == "test_4"
        return a

    test_func("test_5", define=["test_1=test_2", "test_3=test_4"])

# Generated at 2022-06-14 05:35:55.944068
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_config"] = "test_config"
    config["test_config_2"] = "test_config_2"

    @overload_configuration
    def test_function(define=[], test_config="test_config", test_config_2="test_config_2"):
        return test_config, test_config_2

    test_function()
    assert(config["test_config_2"] == "test_config_2")
    assert(config["test_config"] == "test_config")

    test_function(define=["test_config=test_config_new"])
    assert(config["test_config"] == "test_config_new")
    assert(config["test_config_2"] == "test_config_2")


# Generated at 2022-06-14 05:36:01.977868
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_function(hello):
        pass

    def test_call(hello):
        return hello

    @overload_configuration
    def test_func_overloaded(hello):
        return hello

    overload_configuration(test_function)
    assert test_call("world") == "world"
    assert test_func_overloaded("world") == "world"



# Generated at 2022-06-14 05:36:15.102554
# Unit test for function overload_configuration
def test_overload_configuration():
    # Create a mock for config
    class MockConfig:
        def __init__(self):
            self.data = dict()

        def __getitem__(self, key):
            return self.data[key]

        def __setitem__(self, key, value):
            self.data[key] = value

    config = MockConfig()
    config["foo"] = "bar"

    # Create a mock for the function to decorate
    class MockFunc:
        def __init__(self):
            self.data = dict()

        def __call__(self, *args, **kwargs):
            self.data["args"] = args
            self.data["kwargs"] = kwargs
            return "success"

    func = MockFunc()

    wrapped = overload_configuration(func)

    # Call the wrapped function

# Generated at 2022-06-14 05:36:24.860413
# Unit test for function overload_configuration
def test_overload_configuration():
    from . import cli  # noqa
    from .log import set_logging  # noqa
    from .version import version  # noqa

    cli.overload_configuration(set_logging)(
        "set_logging_level", None, "--define", "log_level=DEBUG"
    )
    assert config["log_level"] == "DEBUG"
    cli.overload_configuration(version)("version", None, "--define", "verbose=False")
    assert config["verbose"] == "False"

# Generated at 2022-06-14 05:36:30.228835
# Unit test for function overload_configuration
def test_overload_configuration():
    config["overloaded"] = "overloaded-content"

    @overload_configuration
    def test_func(define):
        return config["overloaded"]

    assert test_func(define=["overloaded=new-content"]) == "new-content"
    assert config["overloaded"] == "new-content"

# Generated at 2022-06-14 05:36:37.947204
# Unit test for function overload_configuration
def test_overload_configuration():
    """Tests if it's possible to overload configuration by using the "define" array"""

    config = _config()

    @overload_configuration
    def overload_by_define(*args, **kwargs):
        print(f"define: {kwargs['define']}")

    print(config)
    overload_by_define(define=["key_string=Value", "key_int=1"])
    assert (config["key_string"] == "Value")
    assert (config["key_int"] == "1")

# Generated at 2022-06-14 05:36:42.497401
# Unit test for function overload_configuration
def test_overload_configuration():
    config["define"] = "key1=value1"
    @overload_configuration
    def mock(define, **kwargs):
        pass
    mock(define=["key1=value1"])
    assert config["key1"] == "value1"