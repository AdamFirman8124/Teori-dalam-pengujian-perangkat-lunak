

# Generated at 2022-06-14 05:27:01.954388
# Unit test for function overload_configuration
def test_overload_configuration():
    def foo(bar, baz, **kwargs):
        return (bar, baz, config.get("baz"))

    # We should be able to overload multiple times config
    foo = overload_configuration(foo)
    foo = overload_configuration(foo)
    bar = foo(bar="bar", baz="baz")
    assert bar[1] == "baz"
    assert bar[2] == "baz"
    bar = foo(bar="bar", baz="baz", define=["baz=baz2"])
    assert bar[1] == "baz"
    assert bar[2] == "baz2"



# Generated at 2022-06-14 05:27:10.621892
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_function(a, b, **kwargs):
        return (a, b, kwargs)

    assert test_function(1, 2) == (1, 2, {})
    assert test_function(1, 2, define=["c=3"]) == (1, 2, {"c": "3"})
    assert test_function(1, 2, define=["c=3", "d=4"]) == (1, 2, {"c": "3", "d": "4"})

# Generated at 2022-06-14 05:27:17.164573
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog import (
        generate_changelog_heading,
        generate_changelog_scope_list,
        generate_changelog_scope_links,
    )

    assert current_changelog_components() == [
        generate_changelog_heading,
        generate_changelog_scope_links,
        generate_changelog_scope_list,
    ]

# Generated at 2022-06-14 05:27:20.386035
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog import commit_component
    from .changelog import changelog_component

    components = current_changelog_components()
    assert commit_component in components
    assert changelog_component in components

# Generated at 2022-06-14 05:27:27.329910
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog_components import Issue, PackageReference, Summary
    assert current_changelog_components() == [Issue, Summary]
    config["changelog_components"] = "semantic_release.changelog_components.Issue"
    assert current_changelog_components() == [Issue]

# Generated at 2022-06-14 05:27:33.269947
# Unit test for function current_changelog_components
def test_current_changelog_components():
    class A:
        pass

    @config.setdefault("changelog_components", "B.C")
    def test_one():
        from .changelog.components import B, C

        assert current_changelog_components() == [B, C]

    @config.setdefault("changelog_components", "B.C, D.E")
    def test_two():
        from .changelog.components import B, C, D, E

        assert current_changelog_components() == [B, C, D, E]

    @config.setdefault("changelog_components", "B.C, D.E, F.G.H")
    def test_three():
        from .changelog.components import B, C, D, E, F

        assert current_

# Generated at 2022-06-14 05:27:38.276995
# Unit test for function overload_configuration
def test_overload_configuration():
    old_value = config.get("define")

    @overload_configuration
    def dummy():
        print(config.get("define"))

    dummy(define=["define=new_value"])
    assert config.get("define") == "new_value"

    config["define"] = old_value

# Generated at 2022-06-14 05:27:43.009248
# Unit test for function overload_configuration
def test_overload_configuration():
    for config_item in config:
        assert config[config_item] == config.get(config_item)
    overload_configuration(lambda: None)(define=["upload_to_pypi=False"])
    assert config.get("upload_to_pypi") == "False"

# Generated at 2022-06-14 05:27:52.766230
# Unit test for function overload_configuration
def test_overload_configuration():
    config_copy = {"test": "not replaced"}

    def test_func(define=None):
        return config_copy

    def test_func2(define):
        return config_copy

    test_func_overloaded = overload_configuration(test_func)
    test_func_overloaded()
    assert config_copy == {"test": "not replaced"}

    test_func_overloaded = overload_configuration(test_func)
    test_func_overloaded(define=["test=replaced"])
    assert config_copy == {"test": "replaced"}

    test_func2_overloaded = overload_configuration(test_func2)
    test_func2_overloaded(define=["test=replaced"])
    assert config_copy == {"test": "replaced"}


# Generated at 2022-06-14 05:27:57.432465
# Unit test for function overload_configuration
def test_overload_configuration():
    class Dummy(object):
        @overload_configuration
        def dummy_function(self):
            pass

    dummy = Dummy()
    dummy.dummy_function(define=["test_key=test_value"])
    assert config["test_key"] == "test_value"

# Generated at 2022-06-14 05:28:11.642020
# Unit test for function current_commit_parser
def test_current_commit_parser():
    def expected_commit_parser():
        pass

    import sys

    sys.modules["semantic_release.commit_parser"] = expected_commit_parser

    # Test valid config
    config["commit_parser"] = "semantic_release.commit_parser"
    assert current_commit_parser() == expected_commit_parser

    # Test invalid config
    config["commit_parser"] = "invalid_module.commit_parser"
    try:
        assert current_commit_parser()
    except ImproperConfigurationError:
        pass
    else:
        assert False

# Generated at 2022-06-14 05:28:16.264023
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from semantic_release.history import parse_commits
    from semantic_release.history.parsers import parse_commits

    parser = current_commit_parser()
    assert parser
    assert parser == parse_commits


# Generated at 2022-06-14 05:28:20.593800
# Unit test for function current_commit_parser
def test_current_commit_parser():
    import semantic_release  # noqa: F401
    ccp = current_commit_parser()
    assert ccp.__module__ == "semantic_release.commit_parser"
    assert ccp.__name__ == "parse"

# Generated at 2022-06-14 05:28:24.799748
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_foo(arg1, arg2):
        return "foo:{0}, bar:{1}".format(arg1, arg2)

    test_foo(1, 2, define=["foo=hello"])
    assert config["foo"] == "hello"

# Generated at 2022-06-14 05:28:31.179568
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def fake_func(*args, **kwargs):
        pass

    fake_func(define=["token=my-token", "username=my-name"])
    assert config["token"] == "my-token"
    assert config["username"] == "my-name"

# Generated at 2022-06-14 05:28:42.368026
# Unit test for function overload_configuration
def test_overload_configuration():
    class FakeArgs:
        pass

    current_config = config

    args = FakeArgs()

    @overload_configuration
    def fake_func_1(args):
        assert args.branch_name == "master"
        assert config == current_config

    @overload_configuration
    def fake_func_2(args):
        assert args.branch_name == "master"
        assert config["branch_name"] == "master"

    @overload_configuration
    def fake_func_3(args):
        assert args.branch_name == "master"
        assert config["branch_name"] == "master"

    args.branch_name = "master"
    args.define = []
    fake_func_1(args)

    args.define = ["branch_name=master"]
   

# Generated at 2022-06-14 05:28:50.771291
# Unit test for function current_changelog_components
def test_current_changelog_components():
    # Test when there is a changelog_components in config
    mocked_config = {'changelog_components': 'Changelog.components.issues,Changelog.components.merges'}
    assert len(current_changelog_components()) == 2

    # Test when there is no changelog_components in config
    mocked_config = {'changelog_components': ''}
    assert len(current_changelog_components()) == 0

# Generated at 2022-06-14 05:28:55.709704
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function tests the decorator overload_configuration"""
    @overload_configuration
    def function(my_dict):
        """This is a dummy function that is used to test the overload_configuration decorator"""
        config_overloaded = config.copy()
        config_overloaded.update(my_dict)
        return config_overloaded

    new_config = {"key_1": "value_1", "key_2": "value_2"}
    assert function(my_dict=new_config) == function(define=["key_1=value_1", "key_2=value_2"])

# Generated at 2022-06-14 05:29:00.242724
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def my_function(define):
        return config["plugin_config"]

    assert my_function(define=["plugin_config=value"]) == "value"
    assert my_function(define=["plugin_config=value", "test=value"]) == "value"

# Generated at 2022-06-14 05:29:14.155554
# Unit test for function overload_configuration
def test_overload_configuration():
    def func0(a):
        return a
    func0 = overload_configuration(func0)

    # Case 0: "define" not in kwargs
    assert func0(123) == 123

    # Case 1: "define" in kwargs, but "define" is not a list/tuple
    assert func0(123, define=1) == 123
    assert func0(123, define={"a":1}) == 123

    # Case 2: "define" in kwargs, "define" is a list/tuple, but empty
    assert func0(123, define=[]) == 123

    # Case 2: "define" in kwargs, "define" is a list/tuple, not empty
    assert func0(123, define=["a=1"]) == 123
    assert config["a"] == "1"



# Generated at 2022-06-14 05:29:24.336818
# Unit test for function current_commit_parser
def test_current_commit_parser():
    import semantic_release.commit_parser
    assert current_commit_parser() == semantic_release.commit_parser.parse

# Generated at 2022-06-14 05:29:28.263865
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Test to check if a call to current_changelog_components() will return a list of
    changelog components.
    """
    functions = current_changelog_components()
    assert isinstance(functions, list)
    if len(functions) > 0:
        assert callable(functions[0])

# Generated at 2022-06-14 05:29:32.061371
# Unit test for function overload_configuration
def test_overload_configuration():
    class Test:
        @overload_configuration
        def f(self):
            pass

    test = Test()
    test.f(define=["a=b"])
    assert (config["a"] == "b")



# Generated at 2022-06-14 05:29:41.942242
# Unit test for function overload_configuration
def test_overload_configuration():
    from pprint import pprint
    from semantic_release import setup_utils

    @overload_configuration
    def mock_func(a,b):
        return (a,b)

    mock_func("a","b")
    assert config['foo'] == 'bar'

    config['foo'] = 'bar'
    assert mock_func("a","b") == ('a', 'b')

    config['foo'] = 'baz'
    assert mock_func("a","b", define=['foo=bar']) == ('a', 'b')

# Generated at 2022-06-14 05:29:50.385713
# Unit test for function overload_configuration
def test_overload_configuration():
    from semantic_release.settings import config

    # This function is to test the overload configuration scenario.
    @overload_configuration
    def overloaded_function(define):
        pass

    # Some non-existing key in the config to check if it adds a new key in the config
    non_existing_key = "non_existing_key"

    # Check if the key is already there, if yes, then remove it to test the "overload functionality"
    if non_existing_key in config:
        del config[non_existing_key]

    value_of_non_existing_key = "Overloaded_Value"

    assert non_existing_key not in config

    overloaded_function(define=[f"{non_existing_key}={value_of_non_existing_key}"])

    assert config[non_existing_key] == value_

# Generated at 2022-06-14 05:29:56.084821
# Unit test for function overload_configuration
def test_overload_configuration():

    @overload_configuration
    def some_function(define: List[str]) -> int:
        return config["test"]

    some_function(define=["test=42"])
    assert config["test"] == "42"
    assert some_function(define=["test=42"]) == 42

# Generated at 2022-06-14 05:29:58.346028
# Unit test for function current_commit_parser
def test_current_commit_parser():
    func = current_commit_parser()
    assert func.__name__ == "parser"



# Generated at 2022-06-14 05:30:06.560675
# Unit test for function overload_configuration
def test_overload_configuration():
    from .cli import get_version

    @overload_configuration
    def overload_configuration_test(args):
        return args

    args = overload_configuration_test(["--define=foo=bar"])
    assert args == ["--define=foo=bar"]
    assert config["foo"] == "bar"

    args = overload_configuration_test(["--define=foo=bar", "--define=foo=baz"])
    assert args == ["--define=foo=bar", "--define=foo=baz"]
    assert config["foo"] == "baz"

    args = overload_configuration_test(["--define=commit_parser=semantic_release.vcs.git.commit_parser"])

# Generated at 2022-06-14 05:30:20.352380
# Unit test for function overload_configuration
def test_overload_configuration():
    # Define a function
    def test_func(arg1, arg2):
        print(arg1, arg2)
        return arg1, arg2

    # Define a function wrapped by overload configuration
    test_overload_configuration_func = overload_configuration(test_func)

    # Call the test_overload_configuration_func without overload
    assert test_overload_configuration_func(1,2) == (1,2)

    # Call the test_overload_configuration_func with overload
    assert test_overload_configuration_func(1,2,define=["test=test"]) == (1,2)
    assert config["test"] == "test"

    # Call the test_overload_configuration_func with overload missing '='

# Generated at 2022-06-14 05:30:25.510826
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test that the configuration can be overloaded.
    """
    @overload_configuration
    def print_config():
        return str(config)
    assert print_config() != print_config(define=["major_on_zero=True"])
    assert (
        print_config(define=["tag_format=None"])
        != print_config(define=["major_on_zero=True"])
    )

# Generated at 2022-06-14 05:30:36.768094
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser()  # we are using the default parser

# Generated at 2022-06-14 05:30:44.946293
# Unit test for function overload_configuration
def test_overload_configuration():
    # Overload the config with the 'define' argument
    @overload_configuration
    def overloaded_configuration(define=None):
        if define is None:
            define = []

    overloaded_configuration(define=["a=1"])
    assert config["a"] == "1"

    overloaded_configuration(define=["b=2"])
    assert config["a"] == "1"
    assert config["b"] == "2"

    overloaded_configuration(define=["a=3"])
    assert config["a"] == "3"
    assert config["b"] == "2"



# Generated at 2022-06-14 05:30:46.320182
# Unit test for function overload_configuration
def test_overload_configuration():
    import semantic_release.cli

# Generated at 2022-06-14 05:30:52.887810
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def doing_nothing(*args, **kwargs):
        pass

    assert config.get("test_key") is None
    assert config.get("test_number") is None
    doing_nothing(define=["test_key=test_value", "test_number=42"])
    assert config.get("test_key") == "test_value"
    assert config.get("test_number") == "42"

# Generated at 2022-06-14 05:30:53.746835
# Unit test for function current_changelog_components
def test_current_changelog_components():
    current_changelog_components()

# Generated at 2022-06-14 05:30:58.238651
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_func(define):
        return config["hello"] + config["world"]

    config["hello"] = "H"
    config["world"] = "W"
    assert test_func(define=["hello=A", "world=B"]) == "AB"
    assert test_func(define=["hello=A", "world=B", "undefined_var=C"]) == "AB"

# Generated at 2022-06-14 05:31:05.979853
# Unit test for function overload_configuration
def test_overload_configuration():
    import semantic_version

    def test_function(version):
        return semantic_version.Version(version, partial=True)

    test_function = overload_configuration(test_function)

    assert test_function("1.0.0") == semantic_version.Version("1.0.0")
    assert test_function("1.0.0-beta", define=["partial=False"]) == semantic_version.Version("1.0.0", partial=False)

# Generated at 2022-06-14 05:31:15.303835
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def some_function(a, b, define=None):
        return True

    assert some_function("x", "y")

    assert some_function("x", "y", ["test=test"]) is True
    assert config["test"] == "test"

    assert some_function("x", "y", ["test=test2"]) is True
    assert config["test"] == "test2"

    assert some_function("x", "y", ["test=1"]) is True
    assert config["test"] == "1"

    assert some_function("x", "y", ["test=1", "test2=test3"]) is True
    assert config["test"] == "1"
    assert config["test2"] == "test3"


# Generated at 2022-06-14 05:31:28.375421
# Unit test for function overload_configuration
def test_overload_configuration():
    from . import get_version

    # Ensure that "config" do not have the two keys
    assert ("repo_token" not in config) and ("try_ci" not in config)

    # Ensure that "config" does not contain the key but that the function
    # contains it
    assert ("repo_token" not in config) and ("repo_token" in get_version.__annotations__)

    # Ensure that "config" do not have the two keys
    assert ("repo_token" not in config) and ("try_ci" not in config)

    # Ensure that "config" contains the two keys and that the value of
    # "repo_token" was changed
    get_version(define=["repo_token=hello"])

# Generated at 2022-06-14 05:31:33.162387
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(a, define=None):
        assert a == 'a'
        assert config['some_key'] == 'some_value'

    test_function(a='a', define=['some_key=some_value'])

# Generated at 2022-06-14 05:31:47.137984
# Unit test for function overload_configuration
def test_overload_configuration():
    # define a dummy function
    def my_function(value):
        assert config["a"] == "1"
        assert config["b"] == "2"
        assert value == 1

    # decorate with overload_configuration
    decorated = overload_configuration(my_function)
    # run function without define parameter
    try:
        my_function(1)
    except AssertionError:
        assert True
    # run function with define parameter
    try:
        decorated(value=1, define=["a=1", "b=2"])
    except AssertionError:
        assert False

# Generated at 2022-06-14 05:31:56.685367
# Unit test for function overload_configuration
def test_overload_configuration():
    t = overload_configuration(lambda x: x)

    assert t("Useless value") == "Useless value"
    assert t("Useless value", define=["a=b"]) == "Useless value"
    assert t("Useless value", define=["a=b", "c=d"]) =="Useless value"
    assert t("Useless value", define=["a=b", "c=d", "c2=d2"]) == "Useless value"
    assert config["a"] == "b"
    assert config["c"] == "d"
    assert config["c2"] == "d2"

# Generated at 2022-06-14 05:31:58.571944
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser().__name__ == "parse"



# Generated at 2022-06-14 05:31:59.803006
# Unit test for function overload_configuration
def test_overload_configuration():
    pass


# Generated at 2022-06-14 05:32:05.057619
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test function to test decorator overload_configuration"""
    config["fake_key"] = 42
    assert config["fake_key"] == 42

    @overload_configuration
    def test_func(define):
        """Test function with @overload_configuration
        """
        return config["fake_key"]

    assert test_func(define=["fake_key=1"]) == 1

# Generated at 2022-06-14 05:32:07.656247
# Unit test for function current_commit_parser
def test_current_commit_parser():
    def test_parse_message(message):
        pass

    assert(current_commit_parser() == test_parse_message)

# Generated at 2022-06-14 05:32:11.138258
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test(**kwargs):
        return config.get("define")

    assert test(define="define=bar") == "bar"

# Generated at 2022-06-14 05:32:15.810836
# Unit test for function overload_configuration
def test_overload_configuration():
    # given
    @overload_configuration
    def test_func(a):
        pass
    config["foo"] = "bar"

    # then when
    test_func(define=["foo=baz"])

    # then
    assert config["foo"] == "baz"

# Generated at 2022-06-14 05:32:18.779109
# Unit test for function current_changelog_components
def test_current_changelog_components():
    func = current_changelog_components()
    assert func[0](0) == "0"


# Generated at 2022-06-14 05:32:31.010561
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(param1, param2, define=None):
        assert config["define_param1"] == "overloaded_value"
        assert config["define_param2"] == "value2"
        assert config["define_param3"] == "value3"
        assert param1 == "value4"
        assert param2 == "value5"
        return True

    config["define_param1"] = "original_value"
    config["define_param2"] = "original_value"
    config["define_param3"] = "original_value"
    test_function("value4", "value5", define=["define_param2=value2", "define_param1=overloaded_value", "define_param3=value3"])

# Generated at 2022-06-14 05:32:51.096543
# Unit test for function overload_configuration
def test_overload_configuration():
    from .config import config
    from . import cli

    @overload_configuration
    def test_overload_configuration():
        pass

    test_overload_configuration()

    assert config["skip_tag"] is False

    test_overload_configuration(define=["skip_tag=True"])

    assert config["skip_tag"] is True

# Generated at 2022-06-14 05:32:52.949382
# Unit test for function current_changelog_components
def test_current_changelog_components():
    parts = '.'.split(".")
    module = ".".join(parts[:-1])
    assert module == ''

# Generated at 2022-06-14 05:32:58.585590
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def some_function(pipeline_config):
        print(config.get("another_value", "default value"))
        print(config.get("user_email", "default value"))

    some_function(define=["user_email=myemail@gmail.com", "another_value=10"])

# Generated at 2022-06-14 05:33:08.413584
# Unit test for function overload_configuration
def test_overload_configuration():
    """Unit test for function overload_configuration"""
    @overload_configuration
    def test_function(arg1, arg2, value, define="changelog_components=changelog_component1.py"):
        """
        The config variable has now been overloaded with a new value.
        We can now test the value
        """
        assert config.get("changelog_components") == "changelog_component1.py"
        return arg1, arg2, value
    test_function("test1", "test2", "test3")

# Generated at 2022-06-14 05:33:19.168619
# Unit test for function overload_configuration
def test_overload_configuration():
    def get_config_value(key):
        return config[key]

    @overload_configuration
    def test_function(define=None):
        for defined_param in define:
            yield get_config_value(defined_param.split("=")[0])

    assert get_config_value('release_commit_message') == 'chore(release): ${next_version}'
    assert get_config_value('upload_to_release') is True

    test_function(define=['release_commit_message=test_release_commit_message',
                          'upload_to_release=False'])

    assert get_config_value('release_commit_message') == 'test_release_commit_message'
    assert get_config_value('upload_to_release') is False

# Generated at 2022-06-14 05:33:23.798984
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == [
        semantic_release.changelog.get_new_changes,
        semantic_release.changelog.get_remove_changes
    ]

# Generated at 2022-06-14 05:33:26.413371
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Test if the function current_changelog_components works without errors."""
    assert len(current_changelog_components()) == 2

# Generated at 2022-06-14 05:33:31.787307
# Unit test for function overload_configuration
def test_overload_configuration():
    """Tests that the overload_configuration decorator works properly"""

    config["overload"] = False

    @overload_configuration
    def decorated(args):
        return config["overload"]

    assert decorated(define="overload=true") == True
    assert decorated(define="overload=false") == False
    assert decorated(define="something=else") == False

# Generated at 2022-06-14 05:33:42.947808
# Unit test for function overload_configuration
def test_overload_configuration():
    # create test function
    def test_func(name, define=None):
        return name

    decorated_func = overload_configuration(test_func)

    # test with "define" parameter
    assert decorated_func("test1", ["test_key=test_value"]) == "test1"
    assert config["test_key"] == "test_value"

    # test without "define" parameter
    assert decorated_func("test2") == "test2"

    # test override
    assert decorated_func("test3", ["test_key=another_value"]) == "test3"
    assert config["test_key"] == "another_value"

# Generated at 2022-06-14 05:33:50.377559
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Test the current_changelog_components function"""

    # Given a config file where the changelog components are configured
    # Then the function returns the right components
    assert (
        current_changelog_components()
        == [semantic_release.changelog.components.parse_issue, semantic_release.changelog.components.parse_single_line]
    )

# Generated at 2022-06-14 05:34:08.658198
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_func(a, b, c):
        print(a, b, c)

    overload_func = overload_configuration(test_func)
    overload_func("1", "2", "3", define=["a=12", "c=6"])

    assert("12" == config.get("a"))
    assert("6" == config.get("c"))

# Generated at 2022-06-14 05:34:10.813934
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser().__name__ == "parse_commits"


# Generated at 2022-06-14 05:34:14.101975
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def get_config():
        return config

    new_config = get_config()
    assert new_config is not None
    assert isinstance(new_config, dict)

# Generated at 2022-06-14 05:34:22.316142
# Unit test for function overload_configuration
def test_overload_configuration():
    """Unit test for overload_configuration."""
    from .cli import setup_logging

    @overload_configuration
    def test_func():
        pass

    # Set a default parameter
    config["log_level"] = "DEBUG"
    logger = setup_logging()
    assert logger.getEffectiveLevel() == logging.DEBUG

    # Overload parameters, even those not existing.
    test_func(define=["log_level=ERROR", "not_existing=foobar"])
    assert logger.getEffectiveLevel() == logging.ERROR
    assert config.get("not_existing") == "foobar"

# Generated at 2022-06-14 05:34:29.146689
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_func(a, b, c=3, **kwargs):
        assert config["token_auth"] == "new_token"
        assert config["dev_branch"] == "my_dev_branch"
        return a + b + c
    assert overload_configuration(test_func)(1, 2, define=["token_auth=new_token", "dev_branch=my_dev_branch"]) == 6

# Generated at 2022-06-14 05:34:35.017542
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test that the decorator overloads the configuration."""
    tmp_config = dict(config)
    tmp_config["overload_value"] = "not_overloaded_yet"

    @overload_configuration
    def test_function(**kwargs):
        pass

    test_function(define=["overload_value=overloaded"])

    assert tmp_config["overload_value"] == "overloaded"

# Generated at 2022-06-14 05:34:41.520617
# Unit test for function overload_configuration
def test_overload_configuration():
    """Ensure that overload_configuration overrides config correctly
    """

    config["pip_args"] = "--user"
    config["python_args"] = "-m pip"

    @overload_configuration
    def run_update(**kwargs):
        pass

    run_update(define=["pip_args=--user --no-warn-script-location",
                       "python_args=python3 -m pip"])

    assert config["pip_args"] == "--user --no-warn-script-location"
    assert config["python_args"] == "python3 -m pip"

# Generated at 2022-06-14 05:34:49.851972
# Unit test for function current_commit_parser
def test_current_commit_parser():

    # Unit test for function current_commit_parser
    def test_current_commit_parser():
        try:
            current_commit_parser()
        except ImproperConfigurationError as exc:
            print(exc)
            assert False

        config["commit_parser"] = "semantic_release.commit_parser.default"
        assert config["commit_parser"] == "semantic_release.commit_parser.default"

        try:
            current_commit_parser()
        except ImproperConfigurationError as exc:
            print(exc)
            assert False

        config["commit_parser"] = "semantic_release.commit_parser.custom"
        try:
            current_commit_parser()
        except ImproperConfigurationError as exc:
            print(exc)
            assert True


# Generated at 2022-06-14 05:34:51.584703
# Unit test for function current_commit_parser
def test_current_commit_parser():
    import semantic_release

    current_commit_parser() == semantic_release.hooks.parse_commit


# Generated at 2022-06-14 05:35:01.233697
# Unit test for function overload_configuration
def test_overload_configuration():
    func = overload_configuration(lambda x, define=None: define)

    define = func(1)
    assert define is None

    define = func(1, define=["foo"])
    assert define is None

    define = func(1, define=["foo=bar"])
    assert define == ["foo=bar"]

    define = func(1, define=["foo=bar", "hello=world"])
    assert define == ["foo=bar", "hello=world"]

    assert config.get("foo") == "bar"
    assert config.get("hello") == "world"

# Generated at 2022-06-14 05:35:25.203497
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    Test that decorator overload_configuration works correctly
    """
    config['version_variable'] = '__version__'
    config['version_source'] = 'semantic_release/__init__.py'
    call_count = 0
    config_info = config.copy()

    @overload_configuration
    def helper(define=None):
        nonlocal call_count
        call_count += 1
        # Assert that the config was edited according to the key/value
        # pairs before calling the decorated function.
        assert config['version_variable'] == 'version'
        assert config['version_source'] == 'module.py'
        return True

    # Test when define is None
    helper()
    assert call_count == 1

    # Restore the config
    config.clear()

# Generated at 2022-06-14 05:35:32.954148
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog_components import commit_message, issue_and_pr

    assert current_changelog_components() == [commit_message, issue_and_pr]

    config["changelog_components"] = "semantic_release.changelog_components.release"
    from .changelog_components import release

    assert current_changelog_components() == [release]



# Generated at 2022-06-14 05:35:39.659228
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Test current_changelog_components function"""
    import semantic_release.changelog_components as cmp
    cmp_list = current_changelog_components()
    assert cmp_list[0] == cmp.ChangelogCommitHeader
    assert cmp_list[1] == cmp.ChangelogCommitDescription
    assert cmp_list[2] == cmp.ChangelogSectionHeader

# Generated at 2022-06-14 05:35:44.803106
# Unit test for function overload_configuration
def test_overload_configuration():
    def dummy(a):
        return a

    dummy = overload_configuration(dummy)

    assert dummy("foo") == "foo"
    assert dummy("foo", define=["foo=bar"]) == "bar"
    assert dummy("foo", define=["foo=bar", "a=b"]) == "bar"
    assert dummy("foo", define=["foo=bar", "a=b", "c=d=e"]) == "bar"

# Generated at 2022-06-14 05:35:53.729615
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    This function tests the decorator overload_configuration
    """

    def test_func(define = None):
        pass

    test_func_de = overload_configuration(test_func)

    before = config["build_image"]
    test_func_de(define=["build_image=docker-ubuntu"])
    after = config["build_image"]

    assert before != after
    assert before == "relekang/pybuild"
    assert after == "docker-ubuntu"



# Generated at 2022-06-14 05:36:00.182827
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def debug(**kwargs):
        return

    from unittest.mock import Mock

    debug(define=["name=value"])
    assert config.get("name") == "value"

    config.get = Mock(return_value="value")
    assert debug() == debug(define=["name=value"]) == "value"

# Generated at 2022-06-14 05:36:02.485534
# Unit test for function current_commit_parser
def test_current_commit_parser():
    try:
        current_commit_parser()
    except ImproperConfigurationError:
        pass

# Generated at 2022-06-14 05:36:09.938528
# Unit test for function overload_configuration
def test_overload_configuration():

    @overload_configuration
    def mocked_function(value: str, define: list = None):
        return value

    config["test_param"] = "unchanged"

    assert mocked_function("new value", define=["test_param=new test_param value"]) == "new value"
    assert mocked_function("new value") == "new value"

    assert config["test_param"] == "new test_param value"

# Generated at 2022-06-14 05:36:21.027453
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def my_func(definitions):
        print(config['pypi_token'])
        print(config['github_token'])
    # test with empty list
    my_func(definitions=[])
    assert(config['pypi_token'] == "")
    assert(config['github_token'] == "")
    # test with key/value pairs
    my_func(definitions=["github_token=my_github_token", "pypi_token=my_pypi_token"])
    assert(config['pypi_token'] == "my_pypi_token")
    assert(config['github_token'] == "my_github_token")

# Generated at 2022-06-14 05:36:32.828430
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_function(first, second, define):
        return first, second, define

    decorated_function = overload_configuration(test_function)

    first, second, define = decorated_function("hello", "world", ["foo=bar", "bar=foo"])
    assert first == "hello"
    assert second == "world"
    assert define == ["foo=bar", "bar=foo"]
    assert config["foo"] == "bar"
    assert config["bar"] == "foo"

    # Test that define parameters with wrong syntax are
    # ignored.
    config.clear()
    first, second, define = decorated_function("hello", "world", ["foo", "bar=foo"])
    assert first == "hello"
    assert second == "world"
    assert define == ["foo", "bar=foo"]
    assert "foo"