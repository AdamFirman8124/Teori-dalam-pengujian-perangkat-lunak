

# Generated at 2022-06-14 05:26:54.479533
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """Test that the current_commit_parser returns a parser."""
    assert callable(current_commit_parser())

# Generated at 2022-06-14 05:27:02.369606
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    Test if we can overload the configuration by adding new key/value pairs
    at runtime.

    A new "test" key/value pair is added and we check if it has been
    effectively added.
    """

    @overload_configuration
    def test_config_overload():
        return config

    assert not "test" in test_config_overload()
    assert "test" in test_config_overload(define=["test=tester"])

# Generated at 2022-06-14 05:27:15.162830
# Unit test for function overload_configuration
def test_overload_configuration():
    config["dry_run"] = False
    config["verbose"] = False
    @overload_configuration
    def func(dry_run, verbose):
        return (dry_run, verbose)
    assert func(dry_run=True, verbose=True) == (True, True)
    assert config["dry_run"] == True
    assert config["verbose"] == True
    assert func(dry_run=False, verbose=True, define=["dry_run"]) == (False, True)
    assert config["dry_run"] == False
    assert config["verbose"] == True
    assert func(
        dry_run=True, verbose=True, define=["dry_run", "verbose"]
    ) == (True, True)
    assert config["dry_run"] == True

# Generated at 2022-06-14 05:27:21.247245
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_func(a, b, c):
        pass

    config["test"] = "true"
    config["test2"] = "2"
    test_func(2, 3, a=2, b=3, define=["test=false", "test2=test"])
    assert config["test"] == "false"
    assert config["test2"] == "test"

# Generated at 2022-06-14 05:27:26.857870
# Unit test for function overload_configuration
def test_overload_configuration():
    config = dict()

    @overload_configuration
    def func(define=[]):
        pass

    func()
    assert config == dict()

    func(define=["foo=bar"])
    assert config == {"foo": "bar"}

    func(define=["foo=baz", "qux=quux"])
    assert config == {"foo": "baz", "qux": "quux"}

# Generated at 2022-06-14 05:27:32.631840
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import BreakingChange
    from semantic_release.changelog import Feature
    from semantic_release.changelog import FixChange

    config["changelog_components"] = (
        "semantic_release.changelog.BreakingChange,"
        "semantic_release.changelog.Feature,"
        "semantic_release.changelog.FixChange"
    )

    assert current_changelog_components() == [
        BreakingChange,
        Feature,
        FixChange,
    ]

# Generated at 2022-06-14 05:27:40.652978
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test that overload_configuration correctly modifies the config"""
    original_config_value = config.get("changelog_filename", None)
    assert original_config_value is None

    @overload_configuration
    def set_configuration_value(name: str, value: str):
        config[name] = value

    set_configuration_value(name="changelog_filename", value="CHANGELOG.md")

    assert config.get("changelog_filename") == "CHANGELOG.md"

# Generated at 2022-06-14 05:27:47.136128
# Unit test for function current_commit_parser
def test_current_commit_parser():
    def test_parser(message):
        return message

    # Set the parser to the test_parser function
    config["commit_parser"] = "semantic_release.tests.test_config.test_parser"

    # Try to get the parser
    parser = current_commit_parser()

    # Check if the parser is the test parser
    assert parser is test_parser



# Generated at 2022-06-14 05:27:49.453098
# Unit test for function current_changelog_components
def test_current_changelog_components():
    current_changelog_components() == None

# Generated at 2022-06-14 05:27:57.015347
# Unit test for function overload_configuration
def test_overload_configuration():
    # Arbitrary function to check if the decorator works
    # The content of "define" should impact the "key" in "config"
    def test_func(define=[]):
        return config["key"]

    # Check that the "key" in "config" is correctly modified
    config["key"] = "value1"
    assert test_func() == "value1"
    assert test_func(define=["key=value2"]) == "value2"

# Generated at 2022-06-14 05:28:13.538324
# Unit test for function current_changelog_components
def test_current_changelog_components():
    def comp_one():
        pass

    def comp_two():
        pass

    class FakeModule:
        comp_one = comp_one
        comp_two = comp_two

    def custom_import(name):
        return FakeModule


    config['changelog_components'] = 'one, two'

    assert len(current_changelog_components()) == 2

    assert current_changelog_components()[0] == comp_one
    assert current_changelog_components()[1] == comp_two

    # Unit test for function current_commit_parser

    def custom_parser():
        pass


    config['commit_parser'] = 'one'

    with pytest.raises(ImproperConfigurationError):
        current_commit_parser()


# Generated at 2022-06-14 05:28:20.412519
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def f(define=[]):
        return config["plugin_config"]

    config.update({"plugin_config": "default"})
    assert f() == "default"
    assert f(define=["plugin_config=other"]) == "other"
    assert f(define=["plugin_config=other1", "plugin_config=other2"]) == "other2"

# Generated at 2022-06-14 05:28:30.185818
# Unit test for function overload_configuration
def test_overload_configuration():
    """Unit test for function overload_configuration"""

    # Dummy function to test
    def func(param, define=None):
        """Dummy function to test"""
        return config.get(param)

    func_overload = overload_configuration(func)

    # Config content before function call
    assert config.get("name") == "semantic_release"

    # Config content after function call with empty array
    func_overload("name", define=[])
    assert config.get("name") == "semantic_release"

    # Config content after function call with pair key/value
    func_overload("name", define=["name=test"])
    assert config.get("name") == "test"

    # Config content after function call with string
    func_overload("version")

# Generated at 2022-06-14 05:28:32.551454
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from .commit_parser import parse_message as parser

    assert current_commit_parser() == parser



# Generated at 2022-06-14 05:28:42.947679
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(verbose, define):
        print(verbose)
        print(config)

    # Add a new key in config
    test_function(verbose=False, define=["test_function=test_function"])
    assert config["test_function"] == "test_function"
    # Change the value of an existing key in config
    test_function(verbose=False, define=["test_function=test_function_bis"])
    assert config["test_function"] == "test_function_bis"
    # Try to add a key with an invalid format
    test_function(verbose=False, define=["test_function_bad_format"])
    assert len(config) == 2
    # Try to add two pairs of key/value in one define

# Generated at 2022-06-14 05:28:56.149026
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import format_changelog

    # test no components
    config.clear()
    assert current_changelog_components() == []

    # test single component
    config.clear()
    config["changelog_components"] = "semantic_release.changelog.format_changelog"
    assert current_changelog_components()[0] == format_changelog

    # test multiple components
    config.clear()
    config[
        "changelog_components"
    ] = "semantic_release.changelog.format_changelog,semantic_release.changelog.format_changelog"
    assert current_changelog_components()[0] == format_changelog
    assert current_changelog_components()[1]

# Generated at 2022-06-14 05:29:02.549603
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert(config.get("changelog_components") == "semantic_release.changelog.components.fix,semantic_release.changelog.components.merge,semantic_release.changelog.components.breaking,semantic_release.changelog.components.other,semantic_release.changelog.components.features")
    assert(len(current_changelog_components()) == 5)

# Generated at 2022-06-14 05:29:14.466738
# Unit test for function current_changelog_components
def test_current_changelog_components():
    import semantic_release.changelog

    def sub_list(lst1, lst2):
        lst1 = lst1.copy()
        lst2 = lst2.copy()
        lst1.sort()
        lst2.sort()
        return lst1 == lst2

    assert sub_list(
        current_changelog_components(),
        [
            semantic_release.changelog.changelog_header,
            semantic_release.changelog.changelog_features,
            semantic_release.changelog.changelog_bugs,
            semantic_release.changelog.changelog_other,
            semantic_release.changelog.changelog_footer,
        ],
    )

# Generated at 2022-06-14 05:29:24.211828
# Unit test for function overload_configuration
def test_overload_configuration():
    config['foo'] = 'bar'
    config['bar'] = 'bar'
    config['foobar'] = 'bar'

    @overload_configuration
    def test_func(define):
        return None

    test_func(define=['foo='])
    test_func(define=['bar=foo'])
    test_func(define=['foobar=foo', 'bar=foo'])

    assert config['foo'] == ''
    assert config['bar'] == 'foo'
    assert config['foobar'] == 'foo'

# Generated at 2022-06-14 05:29:25.825280
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def f(define=[]):
        return config.get("foo")

    config["foo"] = "bar"
    assert f() == "bar"
    assert f(define=["foo=baz"]) == "baz"
    assert f() == "bar"

# Generated at 2022-06-14 05:29:37.858650
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test that overload_configuration set config correctly.
    """
    @overload_configuration
    def dummy(foo, define=[]):
        """A dummy function that takes a foo param and a define param.
        """
        return foo

    assert dummy("bar", define=["hello=world"]) == "bar"
    assert config["hello"] == "world"

# Generated at 2022-06-14 05:29:45.700593
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config["changelog_components"] = "semantic_release.changelog.components.npm_component,semantic_release.changelog.components.maven_component"
    config["changelog_components_path"] = "semantic_release.changelog.components"
    components = current_changelog_components()
    assert len(components) == 2

# Generated at 2022-06-14 05:29:48.640410
# Unit test for function overload_configuration
def test_overload_configuration():

    @overload_configuration
    def my_test_hook(*, define):
        return True

    assert my_test_hook(define=["major_on_zero=True"])
    assert config["major_on_zero"] == "True"



# Generated at 2022-06-14 05:29:52.286641
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert isinstance(current_changelog_components(), list)
    assert len(current_changelog_components()) == 2

# Generated at 2022-06-14 05:30:02.600814
# Unit test for function overload_configuration
def test_overload_configuration():
    config["new_key"] = "old_value"

    # Decorator functions
    @overload_configuration
    def overloaded_function(define: List[str]):
        config["new_key"] = "old_value"

    @overload_configuration
    def overloaded_function_with_params(define: List[str], set_to: str):
        config["new_key"] = set_to

    # Test the decorator
    overloaded_function(define=["new_key=overloaded_value"])
    assert config["new_key"] == "old_value"

    overloaded_function(define=["new_key=overloaded_value", "other_key=other_value"])
    assert config["new_key"] == "old_value"
    assert "other_key" not in config

    overloaded_function

# Generated at 2022-06-14 05:30:10.845809
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test for function overload_configuration.
    """
    config["plugin_core"] = "core_1"
    config["plugin_a"] = "core_2"
    config["plugin_b"] = "core_3"

    def test(plugin_core, plugin_a, plugin_b, define=None):
        return config[plugin_core], config[plugin_a], config[plugin_b]

    test = overload_configuration(test)
    assert test("plugin_core", "plugin_a", "plugin_b") == ("core_1", "core_2", "core_3")
    assert test("plugin_a", "plugin_b", "plugin_core", define="plugin_core=my_core") == (
        "my_core",
        "core_2",
        "core_3",
    )

# Generated at 2022-06-14 05:30:13.717908
# Unit test for function overload_configuration
def test_overload_configuration():
    config["my_var"] = "my_value"

    @overload_configuration
    def my_function(my_var):
        return my_var

    assert my_function(define=["my_var=custom_value"], my_var="overload_value") == "custom_value"

# Generated at 2022-06-14 05:30:20.296184
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """
    Test the current_changelog_components function
    """

    def test_function(config):
        """
        this function is defined to test the current_changelog_components function
        """
        return config
    changelog = config.get("changelog_components")
    assert current_changelog_components(
    ) == [test_function]
    return

# Generated at 2022-06-14 05:30:23.542596
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """"Test for function current_changelog_components"""
    from semantic_release.changelog_components import format_changelog_components
    assert current_changelog_components() == [format_changelog_components]

# Generated at 2022-06-14 05:30:28.316908
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def foo(a, b, define=None):
        return config.get("foo")

    foo(1, 2, define=["foo=42"])
    assert config.get("foo") == "42"

# Generated at 2022-06-14 05:30:46.252845
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def f(x):
        return x

    # No change
    assert f(1) == 1

    # Add the key/value 1/a
    assert f(1, define=["1=a"]) == 1
    assert config["1"] == "a"

    # Add the key/value 2/b
    assert f(1, define=["1=a", "2=b"]) == 1
    assert config["2"] == "b"

    # Add the key/value 3/c=d
    assert f(1, define=["1=a", "2=b", "3=c=d"]) == 1
    assert config["3"] == "c=d"

    # Add the key/value 4/e/f

# Generated at 2022-06-14 05:30:50.585871
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "old_value"
    @overload_configuration
    def test_func(define: List[str]):
        pass
    test_func(define=["test=new_value"])
    assert config["test"] == "new_value"

# Generated at 2022-06-14 05:30:55.064028
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release import current_changelog_components

    assert len(current_changelog_components()) == 1
    assert current_changelog_components()[0] == "semantic_release.history.changelog_section"
    assert current_commit_parser() == " semantic_release.commit_parser"

# Generated at 2022-06-14 05:31:03.007438
# Unit test for function current_changelog_components
def test_current_changelog_components():
    import semantic_release.changelog_components_from_git

    config["changelog_components"] = "semantic_release.changelog_components_from_git.git_commit_message_analyzer"
    config["plugin_config"] = {}
    expected = [semantic_release.changelog_components_from_git.git_commit_message_analyzer]

    assert(current_changelog_components() == expected)

# Generated at 2022-06-14 05:31:06.852318
# Unit test for function overload_configuration
def test_overload_configuration():
    """We test the decorator overload_configuration first.
    """
    function = overload_configuration(lambda message: print(message))
    function("hello!")
    assert config["message"] == "hello!"

# Generated at 2022-06-14 05:31:12.464280
# Unit test for function current_changelog_components
def test_current_changelog_components():
    import semantic_release.changelog_components_plugins.components as components

    components_list = current_changelog_components()
    print("components_list: {}".format(components_list))

    assert len(components_list) == len(components.components)

# Generated at 2022-06-14 05:31:15.390700
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def func():
        pass
    func(define=["test=test"])
    assert config["test"] == "test"



# Generated at 2022-06-14 05:31:21.612064
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "original"

    @overload_configuration
    def test_func(name, define=None):
        return config["test"]

    assert test_func("name") == "original"
    assert test_func("name", define="test=new") == "new"
    assert test_func("name") == "new"

# Generated at 2022-06-14 05:31:22.802807
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == []

# Generated at 2022-06-14 05:31:28.009527
# Unit test for function overload_configuration
def test_overload_configuration():
    # Function to test
    @overload_configuration
    def test_function(param1, param2, define):
        return param1, param2, config["param3"]

    arguments = test_function(1, 2, define=["param3=value"])
    assert arguments == (1, 2, "value")

# Generated at 2022-06-14 05:31:46.410909
# Unit test for function overload_configuration
def test_overload_configuration():
    from tests.conftest import config as tmp_config

    @overload_configuration
    def func(*args, **kwargs):
        return args, kwargs

    args, kwargs = func(
        "test",
        test2="test2",
        test3=3,
        define=[
            "plugin_class=semantic_release.plugins.gitlab:GitLab",
            "dry_run=True",
        ],
    )
    assert args == ("test",)
    assert kwargs == {"test2": "test2", "test3": 3, "define": ["dry_run=True"]}
    assert tmp_config["dry_run"]
    assert tmp_config["plugin_class"] == "semantic_release.plugins.gitlab:GitLab"



# Generated at 2022-06-14 05:31:48.660186
# Unit test for function current_changelog_components
def test_current_changelog_components():
    merge_message = current_changelog_components()[0]

    assert callable(merge_message) == True

# Generated at 2022-06-14 05:31:55.763921
# Unit test for function overload_configuration
def test_overload_configuration():
    from semantic_release.cli import main

    assert config.get("commit_parser") == "semantic_release.commit_parser.parse_commit"
    main(["--define", "commit_parser=semantic_release.tests.fixtures.dummy_commit_parser.parse_commit"], standalone_mode=False)
    assert config.get("commit_parser") == "semantic_release.tests.fixtures.dummy_commit_parser.parse_commit"

# Generated at 2022-06-14 05:32:05.629885
# Unit test for function overload_configuration
def test_overload_configuration():
    config["version_variable"] = "__version__"
    config["version_source"] = "module"
    config["changelog_capitalize"] = "False"
    config["changelog_scope"] = "False"

    @overload_configuration
    def test_func(a, b, define=None, c=None):
        return [a, b, c, config["version_variable"], config["version_source"], config["changelog_capitalize"], config["changelog_scope"]]

    assert test_func(a=1, b=2, c=3) == [1, 2, 3, "__version__", "module", "False", "False"]

# Generated at 2022-06-14 05:32:11.016682
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "foo"

    @overload_configuration
    def test(test):
        return config[test]

    assert test("test") == "foo"
    assert test("test", define=["test=bar"]) == "bar"


# Generated at 2022-06-14 05:32:18.826781
# Unit test for function overload_configuration
def test_overload_configuration():
    def function(param1, define=None):
        function.param1 = param1
        function.define = define

    function("value1", define=["define1=value1", "define2=value2"])
    assert function.param1 == "value1"
    assert function.define == ["define1=value1", "define2=value2"]
    assert config["define1"] == "value1"
    assert config["define2"] == "value2"
    assert config["param1"] == "value1"

# Generated at 2022-06-14 05:32:24.108154
# Unit test for function current_commit_parser
def test_current_commit_parser():
    module = 'semantic_release.commit_parser'
    func = 'parse'
    with config.override(commit_parser=f'{module}.{func}'):
        assert current_commit_parser() == getattr(importlib.import_module(module), func)

# Generated at 2022-06-14 05:32:28.592629
# Unit test for function overload_configuration
def test_overload_configuration():
    from . import cli

    assert "skip_ci" not in config

    @overload_configuration
    def fake_release():
        pass

    fake_release(define=["skip_ci=true"])

    assert config["skip_ci"] == "true"

# Generated at 2022-06-14 05:32:33.678768
# Unit test for function overload_configuration
def test_overload_configuration():
    config.clear()
    config["a"] = "b"  # different from default to check values are replaced

    @overload_configuration
    def func(define=None):
        for key, value in config.items():
            assert value == "c"

    func(define=["a=c", "b=c"])



# Generated at 2022-06-14 05:32:40.443777
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def do_overload_configuration(define=None):
        return None

    do_overload_configuration(define="foo=bar")
    do_overload_configuration(define="foo=bar,baz=bam")
    do_overload_configuration(define="foo=bar,baz=bam,quux=qux")
    assert len(config) == 3
    assert config["foo"] == "bar"
    assert config["baz"] == "bam"
    assert config["quux"] == "qux"

# Generated at 2022-06-14 05:32:53.369579
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """Test the current parser function.
    """

    test_config = {'commit_parser': 'semantic_release.commit_parser:parse_commits'}
    expected_parser = 'parse_commits'

    # Assert import
    assert current_commit_parser() == expected_parser


# Generated at 2022-06-14 05:33:06.998558
# Unit test for function overload_configuration
def test_overload_configuration():
    config["define"] = []
    assert config["define"] == []
    config["define"] = ["define="]
    assert config["define"] == ["define="]
    config["define"] = ["repo=https://github.com/relekang/semantic-release"]
    assert config["define"] == [
        "repo=https://github.com/relekang/semantic-release"
    ]
    config["define"] = ["define=repo=https://github.com/relekang/semantic-release"]
    assert config["define"] == [
        "define=repo=https://github.com/relekang/semantic-release"
    ]

# Generated at 2022-06-14 05:33:16.771230
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    Tests the overload_configuration decorator
    :return:
    """
    @overload_configuration
    def test_func(arg1, arg2, arg3=None):
        return arg1, arg2, arg3

    assert test_func("arg1", "arg2") == ("arg1", "arg2", None)
    assert test_func("arg1", "arg2", arg3="arg3") == ("arg1", "arg2", "arg3")
    assert test_func("arg1", "arg2", define=["arg3=value3", "arg4=value4"]) == (
        "arg1",
        "arg2",
        None,
    )
    assert config["arg3"] == "value3"
    assert config["arg4"] == "value4"

# Generated at 2022-06-14 05:33:25.654053
# Unit test for function overload_configuration
def test_overload_configuration():
    def func(arg1, arg2, define=None):
        return arg1, arg2, define

    config["extra"] = "not_defined"
    rst = overload_configuration(func)("arg1", "arg2", define=["define=ok"])
    assert ("arg1", "arg2", ["define=ok"]) == rst
    assert "ok" == config["define"]
    # Extra configuration should still be there
    assert "not_defined" == config["extra"]

# Generated at 2022-06-14 05:33:28.732256
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """Test that the function current_commit_parser returns the parser function
    """
    from semantic_release.commit_parser import parse

    assert current_commit_parser() == parse



# Generated at 2022-06-14 05:33:34.223074
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_overloading(define=None):
        test_configuration = config

    test_overloading(define=["my_plugin.plugin_function", "value"])
    assert test_configuration["my_plugin.plugin_function"] == "value"



# Generated at 2022-06-14 05:33:37.166424
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import generate_changelog
    components = generate_changelog.current_changelog_components()
    assert len(components) == 3

# Generated at 2022-06-14 05:33:42.257513
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "test"
    @overload_configuration
    def dummy(arg):
        return arg
    dummy(None, define=["test=toto"])
    assert config["test"] == "toto"

# Generated at 2022-06-14 05:33:44.967852
# Unit test for function overload_configuration
def test_overload_configuration():
    from semantic_release.cli import main

    main(["--help"])
    assert config["dry_run"] is False
    main(["--dry-run"])
    assert config["dry_run"] is True

# Generated at 2022-06-14 05:33:47.180603
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert isinstance(current_commit_parser(), Callable)


# Generated at 2022-06-14 05:34:02.082420
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_function(define=None):
        return define

    func_overloaded_configuration = overload_configuration(test_function)

    assert config['requirements'] == ""
    func_overloaded_configuration(define=["requirements=requirements_test.txt"])
    assert "requirements_test.txt" in config['requirements']

    assert config['requirements'] == "requirements_test.txt"

# Generated at 2022-06-14 05:34:07.773535
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "old"
    @overload_configuration
    def test_function(define=None):
        return config["test"]

    assert test_function(define=["test=new"]) == "new"
    config["test"] = "old"

# Generated at 2022-06-14 05:34:19.327116
# Unit test for function overload_configuration
def test_overload_configuration():
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

    def fake_function(define):
        return True

    overload_configuration(fake_function)(define=["branch=test_branch"])
   

# Generated at 2022-06-14 05:34:23.341127
# Unit test for function overload_configuration
def test_overload_configuration():
    def add(a, b=3):
        return a + b

    add_overloaded = overload_configuration(add)
    add_overloaded(1, define=["b=2"])
    assert config["b"] == "2"


# Unit tests for function current_commit_parser()

# Generated at 2022-06-14 05:34:31.795430
# Unit test for function overload_configuration
def test_overload_configuration():
    # Given a fonction "func" which will, once executed, return all the values
    # of "config" with the function "list".
    def func():
        return list(config.items())

    # We decorate the function with overload_configuration.
    func = overload_configuration(func)

    # When we call the function with the define array ["package_name=test"]
    func(define=["package_name=test"])

    # Then the package_name in "config" is equal to "test".
    assert config["package_name"] == "test"

# Generated at 2022-06-14 05:34:36.041003
# Unit test for function current_commit_parser
def test_current_commit_parser():

    from semantic_release.hvcs import parse_commit_message

    assert parse_commit_message == current_commit_parser()


# Unit tests for function current_changelog_components

# Generated at 2022-06-14 05:34:40.713437
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_1(a,b):
        return config['a']

    assert test_1(1, 2, define = ['a=3']) == '3'

# Generated at 2022-06-14 05:34:50.913468
# Unit test for function overload_configuration
def test_overload_configuration():
    """Simply calls the function overload_configuration to check that
    it behaves correctly.
    """
    import inspect

    @overload_configuration
    def my_func(x, y=2, define=None):
        return (str(x), str(y), bool(define))

    assert len(inspect.signature(my_func).parameters) == 3
    assert my_func(3) == ("3", "2", False)
    assert my_func(10, y=5) == ("10", "5", False)
    assert my_func(100, define=["name=Doe"]) == ("100", "2", True)
    assert config["name"] == "Doe"

# Generated at 2022-06-14 05:35:00.922166
# Unit test for function overload_configuration
def test_overload_configuration():
    # Test with a dummy function.
    @overload_configuration
    def dummy(a: int, b: int, c: int = 1) -> int:
        return a + b + c
    assert dummy(1, 2, define=["c=10"]) == 13
    # Test with a function that can take a variable number of arguments.
    @overload_configuration
    def dummy_(*args, **kwargs) -> int:
        return (args[0] + args[1]) * kwargs["c"]
    assert dummy_(1, 2, c=10, define=["d=100"]) == 30
    # Test that the function leaves the original "config" unchanged.
    assert config.get("c", None) is None
    assert config.get("d", None) is None

# Generated at 2022-06-14 05:35:02.225086
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser() is not None

# Generated at 2022-06-14 05:35:21.329073
# Unit test for function overload_configuration
def test_overload_configuration():
    test_config = _config()
    assert test_config == config

    @overload_configuration
    def test_overload(define):
        # This function is called to test the effect of "overload_configuration"
        assert test_config == config

    test_overload(define=["hello=world"])
    assert "hello" in config
    assert config["hello"] == "world"

    test_config["hello"] = "world"
    test_overload(define=["hello=universe"])
    assert "hello" in config
    assert config["hello"] == "universe"
    assert test_config["hello"] == "world"

# Generated at 2022-06-14 05:35:33.563565
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test overload_configuration decorator that doesn't raise exception
    """
    config["semantic_release.foo"] = "Original value"
    config["python_module_name"] = "Original value"
    config["python_package_dir"] = "Original value"
    config["first_release"] = "Original value"
    config["second_release"] = "Original value"

    @overload_configuration
    def foo(define):
        return "Anything"

    foo(define=["semantic_release.foo=changed", "python_module_name=changed"])
    assert config["semantic_release.foo"] == "changed"
    assert config["python_module_name"] == "changed"
    assert config["python_package_dir"] == "Original value"
    assert config["first_release"] == "Original value"
   

# Generated at 2022-06-14 05:35:43.509915
# Unit test for function overload_configuration
def test_overload_configuration():
    def dummy_func(*args, **kwargs):
        return True

    assert overload_configuration(dummy_func)(a=1) is True
    assert overload_configuration(dummy_func)(a=1, define=["a"]) is True
    assert overload_configuration(dummy_func)(a=1, define=["a=1"]) is True
    assert overload_configuration(dummy_func)(a=1, define=["a=1", "b"]) is True
    assert overload_configuration(dummy_func)(a=1, define=["a=1", "b=1"]) is True
    assert overload_configuration(dummy_func)(a=1, define=["a=1", "b=1", "c"]) is True

# Generated at 2022-06-14 05:35:56.332423
# Unit test for function overload_configuration
def test_overload_configuration():
    all_keys = [
        "prepare_release_message",
        "get_changelog",
        "commit_changelog",
        "add_changelog",
        "git_push",
        "upload_to_pypi",
        "upload_to_release",
        "remove_dist",
        "commit_version_number",
        "create_tag",
        "patch_without_tag",
        "changelog_capitalize",
        "changelog_scope",
        "check_build_status",
        "major_on_zero",
        "commit_parser",
        "changelog_components",
        "plugin_config",
    ]
    # Initialize the test dict
    dict_test = dict()
    for key in all_keys:
        dict_test[key]

# Generated at 2022-06-14 05:36:03.284706
# Unit test for function overload_configuration
def test_overload_configuration():
    def return_configuration_param(param):
        return config.get(param)

    overloaded_return_configuration_param = overload_configuration(
        return_configuration_param
    )

    assert return_configuration_param("version-variable") is not "__version__"
    assert (
        overloaded_return_configuration_param("version-variable", define=["version-variable=__version__"])
        == "__version__"
    )

# Generated at 2022-06-14 05:36:06.735332
# Unit test for function current_commit_parser
def test_current_commit_parser():
    importlib.import_module("semantic_release.commit_parser").default.return_value = "func"
    assert current_commit_parser() == "func"



# Generated at 2022-06-14 05:36:11.143755
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def my_function(define):
        return define

    assert my_function(define=["foo=baz"]) == ["foo=baz"]
    assert config["foo"] == "baz"

# Generated at 2022-06-14 05:36:15.008948
# Unit test for function overload_configuration
def test_overload_configuration():
    config.get = lambda x: x
    config["define"] = []
    print(config["define"])
    assert config["define"] == []
    config["define"] = ["foo=bar"]
    assert config["foo"] == "bar"



# Generated at 2022-06-14 05:36:22.902925
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test that an overloaded configuration is correctly added to the config dict."""
    config["new_key"] = "old_value"
    @overload_configuration
    def overload(define):
        return

    assert(config["new_key"] == "old_value")
    overload(define=["new_key=new_value"])
    assert(config["new_key"] == "new_value")


# Generated at 2022-06-14 05:36:28.779996
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.cli import run

    components = current_changelog_components()
    # Importing the code of the CLI to run the code in the
    # changelog components
    run()
    for component in components:
        print(component)
        result = component()
        if result is not None:
            assert result

# Generated at 2022-06-14 05:36:43.941654
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_key"] = "test_value"

    def test_function(define):
        assert "test_key=test_value2" in define
        return True

    overloaded_function = overload_configuration(test_function)
    overloaded_function(define=["test_key=test_value2"])
    assert config["test_key"] == "test_value2"

# Generated at 2022-06-14 05:36:48.710748
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from semantic_release import CommitParser
    from semantic_release.commit_parser import default_commit_parser

    assert current_commit_parser() == configparser.ConfigParser().get
    assert current_commit_parser() == CommitParser.get
    assert current_commit_parser() == default_commit_parser
