

# Generated at 2022-06-14 05:27:02.911751
# Unit test for function overload_configuration
def test_overload_configuration():
    # Load defaults
    cwd = getcwd()
    ini_paths = [
        os.path.join(os.path.dirname(__file__), "defaults.cfg"),
        os.path.join(cwd, "setup.cfg"),
    ]
    ini_config = _config_from_ini(ini_paths)

    toml_path = os.path.join(cwd, "pyproject.toml")
    toml_config = _config_from_pyproject(toml_path)

    # Cast to a UserDict so that we can mock the get() method.
    config = UserDict({**ini_config, **toml_config})

    # Setup function to test
    def get_value(key):
        return config.get(str(key))


# Generated at 2022-06-14 05:27:15.438146
# Unit test for function overload_configuration
def test_overload_configuration():
    global config

    @overload_configuration
    def fake_function():
        return config["release_branch"]

    # Test a simple key/value pair
    config = {"release_branch": "master"}
    assert fake_function(define=["release_branch=dev"]) == "dev"
    assert config["release_branch"] == "dev"

    # Test an erroneous key/value pair
    config = {"release_branch": "master"}
    assert fake_function(define=["release_branch"]) == "master"
    assert config["release_branch"] == "master"

    # Test several key/value pairs
    config = {"release_branch": "master", "commit_message": "n/a"}

# Generated at 2022-06-14 05:27:19.610406
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def useless_function(*args, **kwargs):
        return args, kwargs

    _, defined_param = useless_function(1, define="foo=bar")
    assert defined_param["foo"] == "bar"

# Generated at 2022-06-14 05:27:27.876417
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """Test function current_commit_parser"""
    from .commit_parser import default as default_parser

    default = current_commit_parser()
    assert default == default_parser

    config["commit_parser"] = "semantic_release.commit_parser.default"
    assert current_commit_parser() == default_parser

    del config["commit_parser"]
    assert current_commit_parser() == default_parser



# Generated at 2022-06-14 05:27:34.591973
# Unit test for function overload_configuration
def test_overload_configuration():
    """Unit test for function overload_configuration
    """

    # pylint: disable=missing-function-docstring
    def foo(param):
        return config[param]

    @overload_configuration
    def bar(param):
        return foo(param)

    bar("test_param", define="test_param=test_value")

    assert config["test_param"] == "test_value"



# Generated at 2022-06-14 05:27:40.215418
# Unit test for function overload_configuration
def test_overload_configuration():
    def sample_function():
        return config["changelog_components"].split(",")

    decorated_function = overload_configuration(sample_function)
    sample = decorated_function(define=["changelog_components=A,B,C"])

    assert sample == ["A", "B", "C"]

# Generated at 2022-06-14 05:27:46.176206
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_value"] = "test"
    assert config.get("test_value") == "test"

    @overload_configuration
    def new_test_value():
        return config.get("test_value")

    assert new_test_value(define=["test_value=new_value"]) == "new_value"

# Generated at 2022-06-14 05:27:51.750354
# Unit test for function overload_configuration
def test_overload_configuration():
    def func(arg1, arg2, arg3, define):
        return (arg1, arg2, arg3)

    decorated_func = overload_configuration(func)

    config["config_overloaded"] = "before"
    result = decorated_func("test1", "test2", "test3", ["config_overloaded=after"])
    assert result == ("test1", "test2", "test3")
    assert config["config_overloaded"] == "after"

# Generated at 2022-06-14 05:27:56.048660
# Unit test for function current_changelog_components
def test_current_changelog_components():
    components = current_changelog_components()
    assert len(components) == 2
    assert components[0].__name__ == "changelog_issue"
    assert components[1].__name__ == "changelog_commit"

# Generated at 2022-06-14 05:28:08.641269
# Unit test for function overload_configuration
def test_overload_configuration():
    config["existing_key"] = "aaa"
    config["define"] = [
        "existing_key=bbb",
        "new_key=ccc",
        "empty_value=",
        "empty_key=",
        "no_second_value",
        "only_first_value=1234",
    ]

    @overload_configuration
    def test(arg1):
        assert arg1 == 123
        assert config["existing_key"] == "bbb"
        assert config["new_key"] == "ccc"
        assert config["empty_key"] == ""
        assert config["empty_value"] == ""
        assert "no_second_value" not in config
        assert config["only_first_value"] == "1234"
        return True

    assert test(123)

# Generated at 2022-06-14 05:28:19.208838
# Unit test for function current_commit_parser
def test_current_commit_parser():
    # All except the last part is the import path
    parts = config.get("commit_parser").split(".")
    module = ".".join(parts[:-1])
    # The final part is the name of the parse function
    parser = getattr(importlib.import_module(module), parts[-1])
    assert parser == current_commit_parser()


# Generated at 2022-06-14 05:28:24.066663
# Unit test for function overload_configuration
def test_overload_configuration():
    from semantic_release.history import print_history
    from semantic_release.cli import main

    result = main(["history", "--define=changelog_components=custom_components"])
    assert result == 0
    result = main(["history", "--define=changelog_components"])
    assert result is None

# Generated at 2022-06-14 05:28:29.854480
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def function(*args, **kwargs):
        return args, kwargs

    assert function((1, 2, 3,), define=["a=b"]) == ((1, 2, 3), {"define": ["a=b"]})

# Generated at 2022-06-14 05:28:37.906747
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.vcs_helpers import ChangelogParser

    components = current_changelog_components()

    assert component_formatter_template in components
    assert component_commit_type_template in components
    assert component_issue_url_template in components
    assert component_issue_title_template in components
    assert component_issue_list_template in components
    assert component_commit_list_template in components
    assert component_scope_template in components



# Generated at 2022-06-14 05:28:39.942587
# Unit test for function overload_configuration
def test_overload_configuration():
    assert False, "TODO: test_overload_configuration"


# Generated at 2022-06-14 05:28:44.508019
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from .parser import default_parser

    config.get = lambda *args, **kwargs: None
    assert current_commit_parser() is default_parser

    config.get = lambda *args, **kwargs: "foo.bar"
    with pytest.raises(ImproperConfigurationError):
        current_commit_parser()



# Generated at 2022-06-14 05:28:46.367438
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from . import default_parser

    assert current_commit_parser() == default_parser

# Generated at 2022-06-14 05:28:50.333609
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.utils import changelog
    assert current_changelog_components() == [changelog.get_changelog, changelog.get_diff]

# Generated at 2022-06-14 05:28:54.683342
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function overloads the value of "check_build_status" and assert
    it is changed. Then, it calls an inner function that asserts the value
    is correct in the local scope.
    """
    
    @overload_configuration
    def assert_value(define):
        assert config['check_build_status'] is False

    # activate function to test the overload of config
    assert_value(define=['check_build_status=False'])

# Generated at 2022-06-14 05:29:05.292881
# Unit test for function overload_configuration
def test_overload_configuration():

    @overload_configuration
    def test(arg1, arg2, arg3):
        return {"arg1": arg1, "arg2": arg2, "arg3": arg3}

    # Test "define" is not passed in the parameters
    assert test("1", "2", "3") == {"arg1": "1", "arg2": "2", "arg3": "3"}
    # Test "define" is passed in the parameters
    assert test("1", "2", "3", define=["arg1=str(1)", "arg3=str(3)"]) == {
        "arg1": "str(1)",
        "arg2": "2",
        "arg3": "str(3)",
    }
    # Test "define" is passed in the parameters but with a wrong syntax

# Generated at 2022-06-14 05:29:16.140782
# Unit test for function overload_configuration
def test_overload_configuration():
    assert config["major_on_zero"] is True

    @overload_configuration
    def test_func(define=[]):
        pass

    test_func(define=["major_on_zero=false"])
    assert config["major_on_zero"] is False

# Generated at 2022-06-14 05:29:25.118156
# Unit test for function overload_configuration
def test_overload_configuration():
    a = 1

    @overload_configuration
    def function_with_arg(a):
        if "define" in locals()['kwargs']:
            for defined_param in locals()['kwargs']['define']:
                pair = defined_param.split("=", maxsplit=1)
                if len(pair) == 2:
                    config[str(pair[0])] = pair[1]

    function_with_arg(define=["a=2"])
    assert config["a"] == "2"

# Generated at 2022-06-14 05:29:35.660936
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def func(token, define=None):
        if not define:
            return token

    token = "untouched_token"
    define = None
    assert func(token, define) == token

    token = "untouched_token"
    define = "key=value"
    assert func(token, define) == token
    assert config["key"] == "value"

    token = "untouched_token"
    define = "key_1=value_1 key_2=value_2 key_3=value_3"
    assert func(token, define) == token
    assert config["key_1"] == "value_1"
    assert config["key_2"] == "value_2"
    assert config["key_3"] == "value_3"

# Generated at 2022-06-14 05:29:39.369293
# Unit test for function overload_configuration
def test_overload_configuration():
    from semantic_release.cli import cli_config

    config["test"] = "content"
    cli_config(["test", "--define", "test=modified"])
    assert config["test"] == "modified"

# Generated at 2022-06-14 05:29:50.968643
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """Test current_commit_parser function.
    """
    import pytest
    from semantic_release.hvcs import git_commit_parser
    from semantic_release.errors import ImproperConfigurationError

    assert current_commit_parser() == git_commit_parser
    config["commit_parser"] = "semantic_release.hvcs.git_commit_parser"
    assert current_commit_parser() == git_commit_parser
    config["commit_parser"] = "semantic_release.tests.test_helpers.dummy_commit_parser"
    assert current_commit_parser() == dummy_commit_parser

    config["commit_parser"] = "semantic_release.hvcs.does_not_exist"
    with pytest.raises(ImproperConfigurationError):
        current_commit_parser()



# Generated at 2022-06-14 05:30:03.938394
# Unit test for function current_changelog_components
def test_current_changelog_components():

    # Test for import error, as for invalid parser
    def test_current_changelog_components_import_error():
        with patch.object(config, "get") as mock_get:
            mock_get.return_value = "nonexisting.module.changelogcomponent"
            with pytest.raises(ImproperConfigurationError):
                current_changelog_components()

    # Test for attribute error, as for invalid changelog_components
    def test_current_changelog_components_attribute_error():
        with patch.object(config, "get") as mock_get:
            mock_get.return_value = "semantic_release.changelog.changelog_components.nonexisting_component"
            with pytest.raises(ImproperConfigurationError):
                current_changelog

# Generated at 2022-06-14 05:30:05.510889
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == [current_commit_parser()]



# Generated at 2022-06-14 05:30:19.277296
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def func(*args, **kwargs):
        return config

    define = "first=1"
    func(define=define)
    assert config["first"] == "1"

    define = "second=2"
    func(define=define)
    assert config["first"] == "1"
    assert config["second"] == "2"

    define = "third=3,fourth=4"
    func(define=define)
    assert config["first"] == "1"
    assert config["second"] == "2"
    assert config["third"] == "3"
    assert config["fourth"] == "4"

    define = "fifth=5", "sixth=6"
    func(define=define)
    assert config["first"] == "1"
    assert config["second"] == "2"

# Generated at 2022-06-14 05:30:28.909628
# Unit test for function overload_configuration
def test_overload_configuration():

    class Dummy:
        """Dummy class to test configuration overload"""

        @overload_configuration
        def overload_me(self, define=None):
            """Function decorated by overload_configuration"""
            return define

    dummy = Dummy()
    # Test overload with a single key=value
    dummy_result = dummy.overload_me(define=["test_key=test_value"])
    assert dummy_result == ["test_key=test_value"]
    assert config["test_key"] == "test_value"
    # Test overload with several key=value
    dummy_result = dummy.overload_me(
        define=["test_key_2=test_value_2", "test_key_3=test_value_3"]
    )

# Generated at 2022-06-14 05:30:32.224173
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == [
        semantic_release.changelog.get_components
    ]
    # TODO: Mock the content of pyproject.toml

# Generated at 2022-06-14 05:30:46.091891
# Unit test for function overload_configuration
def test_overload_configuration():
    from .console_script import main

    # Decorate main with overload_configuration
    overload_configuration(main)

    # Also need overload_configuration to decorate main
    @overload_configuration
    def main(argv):
        pass

    # Call main
    main(["minor", "--define", "project_name=unittest"])

    # Assert project_name is unittest
    assert config["project_name"] == "unittest"

# Generated at 2022-06-14 05:30:49.628482
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def hello(name):
        print("Hello, ", name)

    config.update({"name": "World"})
    hello("name", define=["name=You"])
    assert config["name"] == "You"

# Generated at 2022-06-14 05:30:55.607002
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test(**kwargs):
        return config.get("define")

    assert test() is None
    assert test(define=["define=test"]) is None
    assert test(define=["define=test", "test=rfc"]) is None

    assert config.get("define") is None
    assert config.get("test") is None

    assert test(define=["define=test", "test=rfc"]) is None

    assert config.get("define") is None
    assert config.get("test") == "rfc"

# Generated at 2022-06-14 05:31:01.252772
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config.update({"changelog_components": "semantic_release.changelog.components.unreleased"})
    components = current_changelog_components()
    func = importlib.import_module("semantic_release.changelog.components.unreleased")
    assert components[0] == func

# Generated at 2022-06-14 05:31:06.309975
# Unit test for function current_changelog_components
def test_current_changelog_components():
    import semantic_release.hooks as hooks

    # See tests/test_requirements.txt for test hooks
    assert current_changelog_components() == [
        hooks.changelog_feature_component,
        hooks.changelog_fix_component,
    ]

# Generated at 2022-06-14 05:31:14.379617
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test if two calls to call_me with different parameters, defines
    different keys/values in "config", and if the second call overrides the
    first one.
    """

    @overload_configuration
    def call_me(define):
        return

    call_me(define=["key1=val1", "key2=val2"])
    assert config["key1"] == "val1"
    assert config["key2"] == "val2"

    call_me(define=["key1=val3", "key2=val4"])
    assert config["key1"] == "val3"
    assert config["key2"] == "val4"

# Generated at 2022-06-14 05:31:27.384831
# Unit test for function overload_configuration
def test_overload_configuration():
    config['key1'] = 'value1'
    assert config['key1'] == 'value1'
    assert config.get('key2', None) is None

    @overload_configuration
    def func(define=None):
        if define:
            pass

    func()
    assert config['key1'] == 'value1'
    assert config.get('key2', None) is None

    func(define=['key1=new_value1'])
    assert config['key1'] == 'new_value1'
    assert config.get('key2', None) is None

    func(define=['key1=new_value1', 'key2=value2'])
    assert config['key1'] == 'new_value1'
    assert config['key2'] == 'value2'

# Generated at 2022-06-14 05:31:37.404475
# Unit test for function overload_configuration
def test_overload_configuration():
    import click

    @overload_configuration
    def function(define):
        return define

    @click.command()
    @click.option("--define", "-d", multiple=True)
    def command(define):
        function(define=define)

    with click.testing.CliRunner().isolated_filesystem():
        result = command(["vcs_repo=local", "remove_dist=True"])
        assert result.exit_code == 0
        assert config["vcs_repo"] == "local"
        assert config["remove_dist"] == "True"

# Generated at 2022-06-14 05:31:41.787979
# Unit test for function current_commit_parser
def test_current_commit_parser():
    @overload_configuration
    def _test_current_commit_parser():
        from semantic_release.history.parser import parse_message

        assert current_commit_parser() == parse_message

    _test_current_commit_parser()


# Generated at 2022-06-14 05:31:45.665015
# Unit test for function overload_configuration
def test_overload_configuration():
    test_dict = {}
    @overload_configuration
    def test_func(dict_config):
        dict_config['new_key'] = 'new_value'
    test_func(test_dict, define=['new_key=new_value'])
    assert test_dict['new_key'] == 'new_value'

# Generated at 2022-06-14 05:31:56.930745
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_func(version):
        return version

    assert overload_configuration(test_func)("a") == "a"



# Generated at 2022-06-14 05:32:03.232662
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def dummy_function(foo, bar):
        return foo, bar

    assert dummy_function(2, 3, define=["foo=7"]) == (2, 3)
    assert dummy_function(2, 3, define=["foo=7", "bar=3"]) == (2, 3)
    assert config["foo"] == "7"
    assert config["bar"] == "3"

# Generated at 2022-06-14 05:32:07.525359
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def myfunc(**kwargs):
        return config.get("test")

    assert myfunc(define=["test=worked"]) == "worked"

# Generated at 2022-06-14 05:32:19.485931
# Unit test for function overload_configuration
def test_overload_configuration():
    test = overload_configuration(lambda a, b, c: None)

    # Test extra parameters in the function call are ignored
    test(1, 2, 3, define=["a=1"])
    assert config["a"] == "1"

    # Test only one key/value are allowed in a parameter
    test(1, 2, 3, define=["a=1", "b=2", "c=3"])
    assert config["a"] == "1"
    assert config["b"] == "2"
    assert config["c"] == "3"

    # Test Exception if not enough pair elements
    try:
        test(1, 2, 3, define=["a=1", "b", "c=3"])
        assert false, "Expected an exception"
    except ValueError:
        pass

# Generated at 2022-06-14 05:32:25.354462
# Unit test for function overload_configuration
def test_overload_configuration():
    from .scripts.cli import edit_config
    argv = ["edit-config", "-d", "new_item=1", "-d", "another_item=2"]
    edit_config(argv)
    assert config["another_item"] == "2"
    assert config["new_item"] == "1"

# Generated at 2022-06-14 05:32:28.877619
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def print_config():
        print(config)

    print_config()
    print_config(define=["package_name=semantic_release"])
    print_config()

# Generated at 2022-06-14 05:32:30.446583
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser() == config.get("commit_parser")

# Generated at 2022-06-14 05:32:37.558811
# Unit test for function overload_configuration
def test_overload_configuration():
    empty_config = {}
    empty_config_2 = UserDict(empty_config)

    @overload_configuration
    def test_function(var1, var2, var3, define=None):
        return locals()

    assert empty_config == test_function("test", "hello", "world")
    assert empty_config_2 == test_function("test", "hello", "world")
    assert {
        "define": None,
        "var1": "test",
        "var2": "hello",
        "var3": "world",
    } == test_function("test", "hello", "world")

# Generated at 2022-06-14 05:32:41.943445
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "test_old"

    @overload_configuration
    def _test(**kwargs):
        assert config["test"] == "test_new"

    _test(define=["test=test_new"])

# Generated at 2022-06-14 05:32:47.673205
# Unit test for function overload_configuration
def test_overload_configuration():
    new_config = config.get("start_version")
    test_dict = dict(define=["start_version=1.0"])
    overload_configuration(lambda **kwargs: None)(**test_dict)
    assert config.get("start_version") == "1.0"
    config["start_version"] = new_config

# Generated at 2022-06-14 05:33:02.409080
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_func(a, b=3):
        assert config["test"] == "test_value"
        return a + b

    decorated_func = overload_configuration(test_func)

    # Overload configuration with test_func
    decorated_func(1, define=["test=test_value"])
    assert decorated_func(1) == 4

# Generated at 2022-06-14 05:33:07.436362
# Unit test for function overload_configuration
def test_overload_configuration():
    def foo(define=None):
        pass

    foo = overload_configuration(foo)
    foo(define=["key=value", "key2=value2"])

    assert config["key"] == "value"
    assert config["key2"] == "value2"

# Generated at 2022-06-14 05:33:12.956519
# Unit test for function overload_configuration
def test_overload_configuration():
    # Create a fake function passing an argument with the custom key "define"
    @overload_configuration
    def foo(define=[]):
        return None

    # The "define" argument is interpreted and the current configuration
    # is modified
    foo(define=["pypi_token=token_test"])
    assert config["pypi_token"] == "token_test"

# Generated at 2022-06-14 05:33:17.156587
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function tests the logic of "overload_configuration"
    """
    func = overload_configuration(lambda a, b, c, define: None)
    obj = func(1, 2, c=3, define=["FOO=BAR", "BAR=FOO"])
    assert config.get("FOO") == "BAR"
    assert config.get("BAR") == "FOO"

# Generated at 2022-06-14 05:33:30.647913
# Unit test for function overload_configuration
def test_overload_configuration():

    config_bakup = config.copy()

    @overload_configuration
    def test_fct(n, define=None):
        return {"n": n, "define": define, "changelog_components": config["changelog_components"]}

    res = test_fct(1, define=["changelog_components=1"])
    assert res["changelog_components"] == "1"
    assert config["changelog_components"] == "1"

    res = test_fct(2, define=["changelog_components=t"])
    assert res["changelog_components"] == "t"
    assert config["changelog_components"] == "t"

    res = test_fct(3, define=["changelog_components"])


# Generated at 2022-06-14 05:33:34.914434
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = None

    @overload_configuration
    def test_function(define=None):
        return config.get("test")

    assert test_function(define=["test=test_value"]) == "test_value"

# Generated at 2022-06-14 05:33:40.617086
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "false"

    @overload_configuration
    def test_overload(test):
        assert test == "true"

    test_overload(define=["test=true"])
    assert config.get("test") == "true"

# Generated at 2022-06-14 05:33:44.988948
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_configuration(**kwargs):
        return None

    # First test
    test_configuration(define="foo=bar")
    assert config["foo"] == "bar"

    # Second test
    test_configuration(define="foo=bar")
    assert config["foo"] == "bar"

# Generated at 2022-06-14 05:33:46.327399
# Unit test for function overload_configuration
def test_overload_configuration():
    assert "define" in overload_configuration.__wrapped__.__dict__["_wrapped_signature"].parameters

# Generated at 2022-06-14 05:33:56.634747
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_only"] = False

    @overload_configuration
    def f(test_only=True):
        return test_only

    assert f(define=["test_only=1"], test_only=False) == True

    @overload_configuration
    def f(test_only=True):
        return test_only

    assert f(test_only=False) == False

    # No key/value pairs
    @overload_configuration
    def f(test_only=True):
        return test_only

    assert f(define=[""], test_only=False) == False

# Generated at 2022-06-14 05:34:17.865639
# Unit test for function overload_configuration
def test_overload_configuration():
    # We will test here the two possible branches of the if statement in the
    # decorator

    # The keys of the dictionary needs to be strings, so we need to first use
    # the overload_configuration decorator and then to run the test.

    # def function() is used as example function to decorate
    # it is not especially relevant, it only shows that the decorator
    # will not keep function name and docstring
    @overload_configuration
    def function():

        """
        This function will look like "wrap" if decorated.
        """
        pass

    # We need to run the wrapper to apply the decorator
    function()

    # If no define parameter is passed, the config should not change
    assert config == _config()

    # If a valid definition is passed, it should be added to the config

# Generated at 2022-06-14 05:34:26.366536
# Unit test for function overload_configuration
def test_overload_configuration():
    config.get = lambda value: "old"
    assert config["some_value"] == "old"

    @overload_configuration
    def func(**kwargs):
        return

    func(define=["some_value=new", "new_value=new_value"])

    assert config["some_value"] == "new"
    assert config["new_value"] == "new_value"

    config.get = lambda value: None
    assert config.get("some_value") is None

# Generated at 2022-06-14 05:34:37.694277
# Unit test for function overload_configuration
def test_overload_configuration():
    def test(A=None, B=None, C=None, D=None, E=None, F=None, G=None, define=None):
        pass

    # A global variable
    assert test.__globals__["B"] == "dummy"
    assert config["B"] == "dummy"

    new_test = overload_configuration(test)

    # define is used
    assert new_test(define=["B=new_value"]).__globals__["B"] == "new_value"
    assert config["B"] == "new_value"
    # Nothing else is changed
    assert test(A=1, B=2, C=3) == (1, 2, 3, None, None, None, None)

# Generated at 2022-06-14 05:34:39.157583
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser()



# Generated at 2022-06-14 05:34:44.994102
# Unit test for function overload_configuration
def test_overload_configuration():
    assert "initial_version" not in config

    @overload_configuration
    def test_overload_configuration_decorator(define):
        return
    test_overload_configuration_decorator(define="initial_version=1.0.0")
    assert config["initial_version"] == "1.0.0"

# Generated at 2022-06-14 05:34:50.004934
# Unit test for function overload_configuration
def test_overload_configuration():
    test_config = _config()

    @overload_configuration
    def test_function(define):
        pass

    test_function(define=["my_new_value=42"])
    assert test_config["my_new_value"] == "42"

    test_function(define=["my_new_value=43", "my_second_value=42"])
    assert test_config["my_new_value"] == "43"
    assert test_config["my_second_value"] == "42"


# Generated at 2022-06-14 05:34:52.926404
# Unit test for function overload_configuration
def test_overload_configuration():
    assert config["dry_run"] is False

    @overload_configuration
    def f(define=None):
        pass

    f(define=["dry_run=True"])
    assert config["dry_run"] is True

# Generated at 2022-06-14 05:34:59.138335
# Unit test for function overload_configuration
def test_overload_configuration():
    """Testing the overload configuration decorator"""

    @overload_configuration
    def overload_config(define):
        """A function that overloads the config"""
        return

    overload_config(define=["beep=boop", "changelog_components=foo.Bar"])
    assert config["beep"] == "boop"
    assert config["changelog_components"] == "foo.Bar"

# Generated at 2022-06-14 05:35:10.042557
# Unit test for function overload_configuration
def test_overload_configuration():
    def func(*args, **kwargs):
        return [args, kwargs]

    test_func = overload_configuration(func)

    assert test_func(**{"define": ["define_1=value"]}) == [(), {"define": ["define_1=value"]}]
    assert config == {"define_1": "value"}
    assert test_func(**{"define": ["define_2=1"]}) == [(), {"define": ["define_2=1"]}]
    assert test_func(**{"define": ["define_3"]}) == [(), {"define": ["define_3"]}]
    assert config == {"define_1": "value", "define_2": "1"}

# Generated at 2022-06-14 05:35:13.722221
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import get_changelog_components

    assert set(current_changelog_components()) == set(get_changelog_components())

# Generated at 2022-06-14 05:35:28.993169
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test that the wrapper function overloads config with attributes from
    commandline arguments define
    """

    @overload_configuration
    def foo(define=None):
        return define

    assert foo() is None
    assert foo(define=["key=value"]) is None
    assert foo(define=["key=value", "key2=value2"]) is None
    assert config.get("key") == "value"
    assert config.get("key2") == "value2"

# Generated at 2022-06-14 05:35:36.015603
# Unit test for function current_commit_parser
def test_current_commit_parser():
    try:
        # All except the last part is the import path
        parts = config.get("commit_parser")
        print(parts.split("."))
        module = ".".join(parts[:-1])
        # The final part is the name of the parse function
        print(getattr(importlib.import_module(module), parts[-1]))
    except (ImportError, AttributeError) as error:
        print(error, 'jj')

# Generated at 2022-06-14 05:35:43.857438
# Unit test for function overload_configuration
def test_overload_configuration():
    from . import config

    assert "package_files" in config
    assert "pyproject.toml" not in config["package_files"]

    @overload_configuration
    def foo():
        global config
        return config

    assert foo(define=["package_files=pyproject.toml", "test=test"])
    assert "pyproject.toml" in config["package_files"]
    assert "test" in config
    config = _config()

# Generated at 2022-06-14 05:35:52.793070
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_func(define, value):
        return config[value]

    config.update({"key": "orginal_value", "key2": "original_value2"})
    assert test_func(define=["key=new_value", "key2=new_value2"], value="key") == "new_value"
    assert test_func(define=["key=new_value", "key2=new_value2"], value="key2") == "new_value2"



# Generated at 2022-06-14 05:36:05.017818
# Unit test for function overload_configuration
def test_overload_configuration():
    """Check that the config is correctly overloaded."""
    from semantic_release.cli import parse_args

    def f(): pass
    g = overload_configuration(f)

    # Overloading of a boolean
    g(define=["remove_dist=true"])
    assert config.get("remove_dist")

    # Overloading of a boolean
    g(define=["remove_dist=false"])
    assert not config.get("remove_dist")

    # Overloading of a string
    g(define=["commit_parser=semantic_release.commit_parser.parse_commits"])
    assert config.get("commit_parser") == "semantic_release.commit_parser.parse_commits"

    # Overloading of a string with a space

# Generated at 2022-06-14 05:36:12.149351
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    Test for function overload_configuration.
    :return:
    """

    @overload_configuration
    def test_function(arg1):
        return config.get(arg1)

    config["test_param"] = "test_value"
    assert test_function(arg1="test_param", define=["test_param=overloaded_value"]) == "overloaded_value"

# Generated at 2022-06-14 05:36:23.240068
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test if the decorator overload_configuration works as expected."""

    @overload_configuration
    def foo(bar, baz):
        return bar + baz

    @overload_configuration
    def zonk(bar, baz, define):
        return bar + baz + define

    # Test if the config is not modified when the define field is not
    # present.
    assert foo(1, 2) == 3
    assert zonk(1, 2) == 3

    # We test two params
    assert zonk(1, 2, ["foo=bar"]) == 3
    assert config["foo"] == "bar"

    # We test three params
    assert zonk(1, 2, ["foo=bar", "baz=zonk"]) == 3
    assert config["foo"] == "bar"


# Generated at 2022-06-14 05:36:32.259969
# Unit test for function overload_configuration
def test_overload_configuration():
    values = {
        "commit_parser": "a",
        "changelog_scope": "b",
        "changelog_components": "c",
        "plugin_config": "d",
    }
    for key, value in values.items():
        assert key not in config
        config[key] = value
    assert config["commit_parser"] == "a"
    assert config["changelog_scope"] is True
    assert config["changelog_components"] == "c"
    assert config["plugin_config"] == "d"

    @overload_configuration
    def test(define):
        assert config["commit_parser"] == value
        assert config["changelog_scope"] == value
        assert config["changelog_components"] == value
        assert config["plugin_config"] == value

   

# Generated at 2022-06-14 05:36:40.184961
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_func(param1, param2):
        assert param1 == "false"
        assert param2 == "true"

    decorated_func = overload_configuration(test_func)
    decorated_func(define=["major_on_zero=false", "patch_without_tag=true"])
    assert config["major_on_zero"] == "false"
    assert config["patch_without_tag"] == "true"

# Generated at 2022-06-14 05:36:49.763054
# Unit test for function current_changelog_components
def test_current_changelog_components():
    local_config = configparser.ConfigParser()
    local_config.read("test_current_changelog_components.ini")
    test_config = dict(local_config.items("semantic_release"))

    assert current_changelog_components() == [
        importlib.import_module("semantic_release.changelog").changelog_message,
    ]

    assert current_changelog_components(config=test_config) == [
        importlib.import_module("semantic_release.changelog").changelog_message,
        importlib.import_module("tests.test_changelog_component").get_parameter,
    ]