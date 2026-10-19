

# Generated at 2022-06-14 05:26:55.172314
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def do_something(whatever):
        return whatever


    old_value = config['check_build_status']
    assert do_something("whatever", define=['check_build_status=False']) == "whatever"
    assert old_value != config['check_build_status']
    assert config['check_build_status'] == 'False'

# Generated at 2022-06-14 05:27:04.740525
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog_components import (
        commit_author,
        commit_subject,
        commit_body,
        commit_footer,
        commit_hash,
    )

    # Test with no changelog_components set in config
    assert current_changelog_components() == [
        commit_hash,
        commit_author,
        commit_subject,
        commit_body,
        commit_footer,
    ]

    # Test with empty changelog_components set in config
    config["changelog_components"] = ""
    assert current_changelog_components() == [
        commit_hash,
        commit_author,
        commit_subject,
        commit_body,
        commit_footer,
    ]

    # Test with only commit_hash in config

# Generated at 2022-06-14 05:27:06.952912
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert config.get("commit_parser") == "semantic_release.commit_parser"



# Generated at 2022-06-14 05:27:13.877466
# Unit test for function overload_configuration
def test_overload_configuration():
    config_bkp = config.data.copy()
    @overload_configuration
    def overload_configuration_func(define, undefined_param):
        assert config["undefined_param"] == "1"

    overload_configuration_func(define=["undefined_param=1"], undefined_param="2")
    assert config["undefined_param"] == "1"
    config.data = config_bkp

# Generated at 2022-06-14 05:27:18.795460
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def f(define):
        pass

    f(define=["foo=bar", "answer=42"])

    assert config.get("foo") == "bar"
    assert config.get("answer") == "42"

# Generated at 2022-06-14 05:27:28.957899
# Unit test for function overload_configuration
def test_overload_configuration():
    original_config = config.copy()
    @overload_configuration
    def run(define):
        pass
    run(define=["test1=1"])
    assert config["test1"] == "1"

    run(define=["test2=2", "test3=3"])
    assert config["test1"] == "1"
    assert config["test2"] == "2"
    assert config["test3"] == "3"

    config.clear()
    config.update(original_config)

# Generated at 2022-06-14 05:27:39.710866
# Unit test for function current_commit_parser
def test_current_commit_parser():
    try:
        default_commit_parser = current_commit_parser()
    except ImproperConfigurationError as error:
        assert False, error

    new_commit_parser = "semantic_release.commit_parser:parser_function"

    config["commit_parser"] = new_commit_parser

    try:
        assert current_commit_parser() != default_commit_parser
    except ImproperConfigurationError as error:
        assert False, error
    finally:
        config["commit_parser"] = "semantic_release.commit_parser:default_parser"

    try:
        assert current_commit_parser() == default_commit_parser
    except ImproperConfigurationError as error:
        assert False, error


# Generated at 2022-06-14 05:27:45.537783
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_overload(*args, **kwargs):
        return config["plugin_config"]

    try:
        assert test_overload(define=["plugin_config=test"]) == "test"
        assert test_overload() == "test"
    finally:
        del config["plugin_config"]

# Generated at 2022-06-14 05:27:50.648675
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "test_value"

    @overload_configuration
    def test_func(define=[]):
        assert config["test"] == "test_value"
        assert config["define"] is None

    test_func()
    test_func(define=["test=new_test_value"])
    assert config["test"] == "new_test_value"

# Generated at 2022-06-14 05:27:56.168115
# Unit test for function current_changelog_components
def test_current_changelog_components():
    test_config = {"changelog_components": "semantic_release.changelog.components"}
    test_config = UserDict(test_config)

    current_changelog_components()

    with CurrentConfiguration(config, test_config):
        current_changelog_components()



# Generated at 2022-06-14 05:28:13.451738
# Unit test for function overload_configuration
def test_overload_configuration():
    def testFunc(kwargs):
        return kwargs

    newFunction = overload_configuration(testFunc)

    result = newFunction(define=["testParam=hello"])
    assert config["testParam"] == "hello"
    assert result["define"] == ["testParam=hello"]
    result = newFunction(define=["testParam=hello"])
    assert config["testParam"] == "hello"
    assert result["define"] == ["testParam=hello"]
    result = newFunction(define=["testParam2=hello2"])
    assert config["testParam"] == "hello"
    assert config["testParam2"] == "hello2"
    assert result["define"] == ["testParam2=hello2"]
    result = newFunction(define=["testParam2=hello3"])
    assert config["testParam"]

# Generated at 2022-06-14 05:28:18.613697
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_function(define):
        return config["changelog_components"]

    assert test_function(["changelog_components=semantic_release.changelog.components.commit_body"]) == "semantic_release.changelog.components.commit_body"



# Generated at 2022-06-14 05:28:22.805096
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def foo(argument1):
        return argument1

    assert foo("a") == "a"
    assert foo("a", define=["a=b"]) == "a"
    assert config["a"] == "b"

# Generated at 2022-06-14 05:28:31.229012
# Unit test for function overload_configuration
def test_overload_configuration():
    config["env_var"] = "1"
    config["env_bool"] = False

    def function1(*, define: List[str]):
        assert config["env_var"] == "2"
        assert config["env_bool"] is True

    def function2():
        assert config["env_var"] == "1"
        assert config["env_bool"] is False

    @overload_configuration
    def function3(*, define: List[str]):
        assert config["env_var"] == "2"
        assert config["env_bool"] is True

    function1(define=["env_var=2"])
    function2()
    function3(define=["env_var=2", "env_bool=True"])

    config["env_var"] = "1"
    config["env_bool"] = False

# Generated at 2022-06-14 05:28:36.174706
# Unit test for function overload_configuration
def test_overload_configuration():
    config.update({"test": "value"})
    @overload_configuration
    def _test(define):
        pass

    assert config["test"] == "value"
    _test(define=["toto=tata"])
    assert config["toto"] == "tata"

# Generated at 2022-06-14 05:28:41.417544
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    Test if the decorator allows to edit config.
    """
    global config
    config = UserDict({"key": "value"})

    @overload_configuration
    def function(*args, **kwargs):
        nonlocal config
        return config

    assert function(define=["key=new_value"]) == {"key": "new_value"}



# Generated at 2022-06-14 05:28:50.289731
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .components import all_changelog_components, changelog_components

    assert current_changelog_components() == changelog_components
    config["changelog_components"] = ",".join(
        [f"{x.__module__}.{x.__name__}" for x in all_changelog_components]
    )
    assert current_changelog_components() == all_changelog_components

# Generated at 2022-06-14 05:28:56.684722
# Unit test for function current_changelog_components
def test_current_changelog_components():
    import semantic_release.history

    config["changelog_components"] = "semantic_release.history.changelog_components," + \
        "semantic_release.history.changelog_components"

    assert current_changelog_components() == [
        semantic_release.history.changelog_components,
        semantic_release.history.changelog_components,
    ]

# Generated at 2022-06-14 05:28:59.946596
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(*args, **kwargs):
        print("test")

    test_function(define="test_var=test_value")
    assert config.get("test_var") == "test_value"

# Generated at 2022-06-14 05:29:08.899487
# Unit test for function overload_configuration
def test_overload_configuration():
    """This decorator edits "config" according to the pairs key/value of the "define" array
    """
    import semantic_release

    def my_function(define):
        config["new_var"] = "def"
        assert config["new_var"] == "def"

    my_function = overload_configuration(my_function)
    my_function(define=["new_var=ghi"])
    assert config["new_var"] == "ghi"

# Generated at 2022-06-14 05:29:22.264551
# Unit test for function overload_configuration
def test_overload_configuration():
    global config
    config = UserDict({'token': 'aabb'})
    myfunction = overload_configuration(lambda: True)
    myfunction(token='foo', define=['token=bar'])
    assert config['token'] == 'bar'
    assert 'token' in config

# Generated at 2022-06-14 05:29:26.316770
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert (
        current_changelog_components()
        == [
            semantic_release.changelog.changelog_components.get_issues,
            semantic_release.changelog.changelog_components.get_merges,
        ]
    )

# Generated at 2022-06-14 05:29:31.348562
# Unit test for function overload_configuration
def test_overload_configuration():
    config["new_key"] = None

    @overload_configuration
    def new_key_test(chip, define=None):
        return config["new_key"]

    assert new_key_test("test1", define=["new_key=test2"]) == "test2"


# Generated at 2022-06-14 05:29:40.932485
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import create_components
    from semantic_release.changelog import breaking_change_component
    from semantic_release.changelog import features_and_fixes_component

    config["changelog_components"] = "semantic_release.changelog.features_and_fixes_component,semantic_release.changelog.breaking_change_component"
    components = current_changelog_components()
    assert components == [features_and_fixes_component, breaking_change_component]



# Generated at 2022-06-14 05:29:49.636484
# Unit test for function overload_configuration
def test_overload_configuration():
    config["repository_type"] = "git"

    @overload_configuration
    def function1(define=None):
        return config["repository_type"]

    @overload_configuration
    def function2(define=None):
        return config["repository_type"]

    assert function1() == "git"
    assert function1(define=["repository_type=hg"]) == "hg"

    assert function2(define=["repository_type=hg"]) == "hg"
    assert function2() == "hg"

# Generated at 2022-06-14 05:30:02.999188
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test function overload_configuration"""
    assert _config_from_ini(["tests/test_configuration/setup.cfg"]) == {
        "plugin_config": {
            "semantic_release.pypi_plugin.Plugins": "semantic_release.pypi_plugin.Plugins",
        },
        "plugin_version": "2.0",
        'python_version': '3.8',
    }

    def deco1(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)

        return wrap

    @deco1
    @overload_configuration
    def print_config(*args, **kwargs):
        return config


# Generated at 2022-06-14 05:30:07.377916
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "test"
    @overload_configuration
    def test_func(define=[]):
        if not define:
            return config["test"]
        else:
            return config["test"]+"_"+define[0]
    assert test_func() == "test"
    assert test_func(define=["2"]) == "test_2"

# Generated at 2022-06-14 05:30:12.118497
# Unit test for function current_commit_parser
def test_current_commit_parser():
    config['commit_parser'] = 'semantic_release.commit_parser.default_semantic_version_parser'
    parser = current_commit_parser()
    assert parser.__name__ == 'default_semantic_version_parser'

# Generated at 2022-06-14 05:30:19.895193
# Unit test for function overload_configuration
def test_overload_configuration():
    from .release.prepare import prepare

    # Prepare a new version
    prepare(
        "patch",
        default=False,
        commit_parser=current_commit_parser(),
        define=[
            "commit_parser=semantic_release.commit_parser.standard.parse",
            "level=info",
        ],
    )
    assert config["commit_parser"] == "semantic_release.commit_parser.standard.parse"
    assert config["level"] == "INFO"

# Generated at 2022-06-14 05:30:22.151861
# Unit test for function current_changelog_components
def test_current_changelog_components():
    class TestClass():
        def test_static_changelog_components(self):
            components = current_changelog_components()
            assert len(components) is 3

# Generated at 2022-06-14 05:30:39.632089
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    If the define argument is not set in the command line, the dict "config"
    is not modified
    """
    @overload_configuration
    def do_nothing():
        pass
    initial_value = config.get("commit_version_number", "")
    do_nothing()
    new_value = config.get("commit_version_number", "")
    assert initial_value == new_value
    """
    If the define argument is set in the command line, the dict "config"
    is modified accordingly
    """
    @overload_configuration
    def do_nothing():
        pass
    initial_value = config.get("commit_version_number", "")
    do_nothing(define=["commit_version_number=False"])

# Generated at 2022-06-14 05:30:48.726587
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config['changelog_components'] = 'semantic_release.changelog.components.title.title, semantic_release.changelog.components.body, semantic_release.changelog.components.footer'
    assert current_changelog_components() == [
        semantic_release.changelog.components.title.title,
        semantic_release.changelog.components.body.body,
        semantic_release.changelog.components.footer.footer,
    ]


# Generated at 2022-06-14 05:30:58.476112
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test the overload_configuration decorator."""
    class Mock:
        """Mock class to test the overload_configuration decorator."""

        @overload_configuration
        def func(self, define=[], **kwargs):
            """Test function for the overload_configuration decorator.

            :param define: List of strings of the form
                "<variable name>=<variable value>".
            :returns: The value of the "config" dictionary.
            """
            return config

    mock_obj = Mock()
    assert mock_obj.func() == config
    assert mock_obj.func(define=["a=1"]) == config
    assert mock_obj.func(define=["a=1", "b=2"]) == config

# Generated at 2022-06-14 05:31:03.639950
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog.components import scope_and_subject

    config['changelog_components'] = "semantic_release.changelog.components.scope_and_subject"
    assert current_changelog_components()[0] == scope_and_subject

# Generated at 2022-06-14 05:31:12.508614
# Unit test for function overload_configuration
def test_overload_configuration():
    from tests.repository_helper import RepositoryHelper
    from semantic_release import get_version
    from semantic_release.errors import ImproperConfigurationError

    @overload_configuration
    def test_decorated_function(repo):
        repo.add_commit("test: invalid configuration")
        return get_version(repo, "patch")

    try:
        with RepositoryHelper() as repo:
            test_decorated_function(repo, define=["test=test"])
    except ImproperConfigurationError as err:
        assert "Unable to import parser" in str(err)
    else:
        assert False

# Generated at 2022-06-14 05:31:21.435794
# Unit test for function overload_configuration
def test_overload_configuration():
    # Define a function using the configuration decorator
    @overload_configuration
    def func(define: List[str]):
        # Call the function
        func(define=["test=test", "key=val"])
        # Check the function with the decorator
        config["test"] == "test"
        config["key"] == "val"
        # Check the function without the decorator
        func_without_decorator(define=["name=Jean-Luc Picard"])
        config["name"] == "Jean-Luc Picard"



# Generated at 2022-06-14 05:31:32.400858
# Unit test for function current_commit_parser
def test_current_commit_parser():
    global config

    # Test on default device
    assert (
        current_commit_parser().__name__
        == "semantic_release.commit_parser.default_parse"
    )

    # Test with a wrong path
    config["commit_parser"] = "path_that_does_not_exists"
    try:
        current_commit_parser()
        assert False
    except ImproperConfigurationError:
        pass
    config["commit_parser"] = "semantic_release.commit_parser.default_parse"

    # Test with a wrong function name
    config["commit_parser"] = "semantic_release.commit_parser.wrong_name"
    try:
        current_commit_parser()
        assert False
    except ImproperConfigurationError:
        pass

# Generated at 2022-06-14 05:31:38.220368
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog_components import scope
    from .changelog_components import breaking_change
    from .changelog_components import commit_message
    from .changelog_components import commit_type

    assert current_changelog_components() == [
        scope.component,
        breaking_change.component,
        commit_type.component,
        commit_message.component,
    ]

# Generated at 2022-06-14 05:31:39.462974
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser() is not None

# Generated at 2022-06-14 05:31:49.058235
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release import changelog

    # Test changelog_components with one component
    config["changelog_components"] = "semantic_release.changelog.Changes"
    components = current_changelog_components()
    assert len(components) == 1
    assert components[0] == changelog.Changes

    # Test changelog_components with multiple components
    config["changelog_components"] = "semantic_release.changelog.Changes,semantic_release.changelog.Summary"
    components = current_changelog_components()
    assert len(components) == 2
    assert components[0] == changelog.Changes
    assert components[1] == changelog.Summary


# Generated at 2022-06-14 05:32:07.963664
# Unit test for function overload_configuration
def test_overload_configuration():
    import tempfile

    temp_file = tempfile.NamedTemporaryFile("w")


# Generated at 2022-06-14 05:32:14.987885
# Unit test for function overload_configuration
def test_overload_configuration():
    config["new_key"] = "new_value"
    @overload_configuration
    def function_to_decorate(new_key):
        assert config["new_key"] == "new_value"

    key = "new_key=overloaded_value"
    function_to_decorate(define=[key])
    assert config["new_key"] == "overloaded_value"

# Generated at 2022-06-14 05:32:17.784368
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser()



# Generated at 2022-06-14 05:32:24.536772
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "test"
    config["test1"] = 1
    config["test2"] = "test2"
    config["define"] = ["test=test1", "test2=test2"]

    @overload_configuration
    def overwritten_config():
        return config

    assert overwritten_config != config
    assert overwritten_config["test"] == "test1"
    assert overwritten_config["test1"] == 1
    assert overwritten_config["test2"] == "test2"

# Generated at 2022-06-14 05:32:29.648179
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    This is a sample function for testing
    """

    @overload_configuration
    def test_func(define):
        """
        Function for testing
        """
        return config

    assert test_func(define=["commit_parser=tests.parser.parser"]) == {
        "commit_parser": "tests.parser.parser"
    }

# Generated at 2022-06-14 05:32:37.942337
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(a, b):
        return a + b

    config.set("define", "define=one")
    assert test_function(1, 2) == 3
    config.set("define", "define=two")
    assert test_function(1, 2) == 3
    config.set("define", "define=three")
    assert test_function(1, 2) == 3
    config.set("define", "define=four")
    assert test_function(1, 2) == 3
    assert "define" not in config

# Generated at 2022-06-14 05:32:40.716066
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def func(a, b):
        print(a, b)

    func(1, 2, define=None)
    assert(config.get("a") == 1)
    assert(config.get("b") == 2)

# Generated at 2022-06-14 05:32:44.324808
# Unit test for function overload_configuration
def test_overload_configuration():
    """Unit test for the overload_configuration decorator"""
    @overload_configuration
    def f(a, define=None):
        """Function to test decorator overload_configuration"""
        return a
    assert f(1, define=["key=value"]) == 1


# Generated at 2022-06-14 05:32:54.030240
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test the function "overload_configuration" to see if the values of
    configuration file can be correctly overwritten by command-line arguments.
    """

    @overload_configuration
    def foo(define):
        pass

    # Test 1
    assert config["commits_regex"] == ".*"
    foo(define=["commits_regex=^type:(breaking|feature|fix)$"])
    assert config["commits_regex"] == "^type:(breaking|feature|fix)$"
    # Test 2
    assert config["commit_parser"] == "semantic_release.commit_parsers.parse_angular"
    foo(define=["commit_parser=semantic_release.commit_parsers.parse_angular2"])

# Generated at 2022-06-14 05:32:57.279777
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Test the function current_changelog_components
    :raises AssertionError: if the test failed
    """
    current_changelog_components()



# Generated at 2022-06-14 05:33:15.501960
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test if the decorator works well with a mocked object."""
    # Creating a mock of the changelog_capitalize parameter
    test_config = {
        "changelog_capitalize": False,
        "commit_parser": "semantic_release.commit_parser",
        "changelog_components": (
            "semantic_release.changelog.BreakingChange,"
            "semantic_release.changelog.Deprecation"
        ),
    }

    # Creating a mock of the function with a dictionary as argument
    @overload_configuration
    def mock_function_with_arg(arguments):
        return arguments

    test_arguments = {"define": ["changelog_capitalize=True"]}

    # Checking if the definition of the configuration parameters works well

# Generated at 2022-06-14 05:33:18.873816
# Unit test for function current_changelog_components
def test_current_changelog_components():
    components = current_changelog_components()
    assert len(components) == 1
    assert components[0].__qualname__ == "pytest.test_current_changelog_components.<locals>.test_changelog_components"


# Generated at 2022-06-14 05:33:30.021090
# Unit test for function overload_configuration
def test_overload_configuration():
    """Unit test for function overload_configuration
    """
    @overload_configuration
    def test_function(param1, param2, **kwargs):
        """
        :param param1: param 1
        :type param1: str
        :param param2: param 2
        :type param2: str
        :param kwargs: keyword args
        :type kwargs: dict
        """
        print("param1", param1)
        print("param2", param2)

    test_function("a", "b", define=["param1=c", "param2=d"])
    assert config["param1"] == "c"

# Generated at 2022-06-14 05:33:40.617720
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function tests the behavior of "overload_configuration" function."""
    import semantic_release.cli.main as cli

    # Test with a "define" argument
    cli.next_version(define=["test=test"])
    assert config["test"] == "test"

    # Test with a "define" argument but invalid value
    cli.next_version(define=["test"])
    assert config["test"] == "test"

    # Test without a "define" argument
    cli.next_version()
    assert "test" not in config

# Generated at 2022-06-14 05:33:43.098991
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "hello"
    @overload_configuration
    def test_func(define=None):
        pass

    test_func(define=["test=new_value"])
    assert config["test"] == "new_value"

# Generated at 2022-06-14 05:33:48.524402
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == [
        semantic_release.changelog._changelog_components.Component,
        semantic_release.changelog._changelog_components.CommitMessage,
    ]



# Generated at 2022-06-14 05:33:50.313250
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == []



# Generated at 2022-06-14 05:34:01.194461
# Unit test for function overload_configuration
def test_overload_configuration():
    """This test loads a file "define.cfg" and asserts that after
    the overloaded configuration, the content of the loaded file
    is contained in config
    """
    import semantic_release.cli as cli
    import semantic_release.configuration as configuration

    config_before = configuration.config.copy()
    cli.main(["--config", "define.cfg", "next-version"])
    config_after = configuration.config.copy()

    for key, value in config_before.items():
        assert key in config_after
        assert config_after[key] == value

    parser = configparser.ConfigParser()
    parser.read(["define.cfg"])

    for key, value in parser.items("semantic_release"):
        assert key in config_after
        assert config_after[key] == value

# Generated at 2022-06-14 05:34:04.291343
# Unit test for function current_commit_parser
def test_current_commit_parser():
    try:
        current_commit_parser()
    except ImproperConfigurationError:
        pass

# Generated at 2022-06-14 05:34:10.871988
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert (
        current_commit_parser() ==
        importlib.import_module("semantic_release.commit_parser").parse
    )
    config["commit_parser"] = "custom.commit_parser.valid_commit_parser"
    assert (
        current_commit_parser() ==
        importlib.import_module("custom.commit_parser").valid_commit_parser
    )



# Generated at 2022-06-14 05:34:23.766120
# Unit test for function overload_configuration
def test_overload_configuration():
    # Setup
    def f(x, define=[]):
        return x

    actual = f(1, ["a=b", "c=d"])
    expected = 1
    # Assert
    assert actual == expected



# Generated at 2022-06-14 05:34:25.494252
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser() is not None


# Generated at 2022-06-14 05:34:33.038418
# Unit test for function overload_configuration
def test_overload_configuration():
    config["some_param"] = "old_value"
    @overload_configuration
    def test_function(define=None):
        return config["some_param"]
    value = test_function(define=["some_param=new_value"])
    assert value == "new_value"

# Generated at 2022-06-14 05:34:38.833695
# Unit test for function overload_configuration
def test_overload_configuration():
    config["commands"] = "prepare"
    config["name"] = "semantic_release"
    config["version"] = "2.6.0"

    @overload_configuration
    def print_configuration(*args, **kwargs):
        print(config["version"] + ":" + config["name"])

    print_configuration(define=["version=2.6.1", "name=test"])
    # version and name are now 2.6.1 and test
    assert config["version"] == "2.6.1", "version should be 2.6.1"
    assert config["name"] == "test", "name should be test"

# Generated at 2022-06-14 05:34:42.180489
# Unit test for function overload_configuration
def test_overload_configuration():
    def test(**kwargs):
        pass
    test = overload_configuration(test)
    test(define=["a=b"])
    assert config["a"] == "b"

# Generated at 2022-06-14 05:34:43.384126
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components is not None

# Generated at 2022-06-14 05:34:53.279334
# Unit test for function overload_configuration
def test_overload_configuration():
    config['commit-parser'] = 'semantic_release.commit_parser.legacy'
    config['changelog-components'] = 'semantic_release.changelog.components.unreleased_changes'
    config['changelog-capitalize'] = False

    @overload_configuration
    def overload_func(define):
        print(config['commit-parser'])
        print(config['changelog-components'])
        print(config['changelog-capitalize'])

    overload_func(define=['commit-parser=semantic_release.commit_parser.legacy'])
    assert config['commit-parser'] == 'semantic_release.commit_parser.legacy'

# Generated at 2022-06-14 05:35:00.066152
# Unit test for function current_commit_parser
def test_current_commit_parser():
    # Test valid import
    assert config["commit_parser"] != ""
    assert current_commit_parser() is not None
    # Test invalid import
    config["commit_parser"] = "unknown.unknown"
    try:
        current_commit_parser()
        assert False
    except ImproperConfigurationError as e:
        assert config["commit_parser"] == str(e).split("'")[1]



# Generated at 2022-06-14 05:35:08.934239
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test function overload_configuration
    """
    @overload_configuration
    def test_func(a, b):
        """Test function test_func
        """
        return a + b

    assert test_func(a=1, b=2) == 3
    assert test_func(a=1, b=2, define=["test=test"]) == 3
    assert test_func(a=1, b=2, define=["test=test", "b=9"]) == 10



# Generated at 2022-06-14 05:35:18.316122
# Unit test for function overload_configuration
def test_overload_configuration():
    """Unit test for the decorator `overload_configuration`."""

    class TestOverload(object):

        @overload_configuration
        def fct(self, define):
            return config

    t = TestOverload()

    assert t.fct(define=["key=value"]) == {"key": "value"}
    assert t.fct(define=["key=value", "key2=value2"]) == {
        "key": "value",
        "key2": "value2",
    }

# Generated at 2022-06-14 05:35:28.249932
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from .commit_parser import parse_commits

    assert current_commit_parser() == parse_commits



# Generated at 2022-06-14 05:35:33.361491
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config["changelog_components"] = "semantic_release.changelog.components.breaking_change_log, semantic_release.changelog.components.issue_references_log"  # noqa: E501
    assert len(current_changelog_components()) == 2

# Generated at 2022-06-14 05:35:43.407828
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test that the configuration is overloaded with the new value"""
    config.clear()
    config["test_key"] = "test_value"
    config["test_key2"] = "test_value2"

    @overload_configuration
    def test_config(**kwargs):
        return config

    assert config["test_key"] == "test_value"
    assert config["test_key2"] == "test_value2"
    assert config["commit_parser"] == "semantic_release.commit_parser.parse"
    assert config["changelog_components"] == "semantic_release.changelog.components.section_changelog"


# Generated at 2022-06-14 05:35:44.594490
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert callable(current_commit_parser())



# Generated at 2022-06-14 05:35:57.577566
# Unit test for function overload_configuration
def test_overload_configuration():
    global config
    config = _config()
    assert config["changelog"] is False
    assert config["major"] == "foo"
    assert config["minor"] == "bar"
    assert config["patch"] == "hack"
    assert config["changelog_components"] == "bar, foo, baz"

    @overload_configuration
    def foo(x, y, z=1, **kwargs):
        return x, y, z

    assert foo(1, 2, z=3) == (1, 2, 3)
    assert foo(1, 2, z=3, define=["changelog=bar", "major=3"]) == (1, 2, 3)

    assert config["changelog"] is True
    assert config["major"] == "3"

# Generated at 2022-06-14 05:36:11.263288
# Unit test for function overload_configuration
def test_overload_configuration():
    from semantic_release import check, set_release_level
    from semantic_release.plugin_manager import run_hook_plugins

    @overload_configuration
    def overload_config():
        config["level"] = "patch"

    overload_config(define=["level=patch"])
    assert config["level"] == "patch"

    @overload_configuration
    def overload_check():
        check_list = run_hook_plugins("check")
        return check(check_list)

    @overload_configuration
    def overload_release():
        set_release_level("patch")
        return run_hook_plugins("post")

    overload_check(define=["check_build_status=True"])
    assert config["check_build_status"] is True


# Generated at 2022-06-14 05:36:17.394915
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == []

    config["changelog_components"] = (
        "semantic_release.changelog.components.unreleased_sections"
    )
    assert len(current_changelog_components()) == 1

    config["changelog_components"] = (
        "semantic_release.changelog.components.unreleased_sections,"
        "semantic_release.changelog.components.releasenotes"
    )
    assert len(current_changelog_components()) == 2



# Generated at 2022-06-14 05:36:23.181379
# Unit test for function overload_configuration
def test_overload_configuration():
    test_config = _config()
    # Overload the configuration with a "define" parameter
    @overload_configuration
    def overload_config(define):
        return

    overload_config(define=["upload_to_release=False"])
    assert not test_config.get("upload_to_release", True)
    overload_config(define=["upload_to_release=True"])
    assert test_config.get("upload_to_release", False)
    overload_config()

# Generated at 2022-06-14 05:36:31.766714
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Function current_changelog_components have to return a list of
    changelog components.
    """
    components = [
        "semantic_release.changelog_components.parser_utils.get_commit_hash",
        "semantic_release.changelog_components.parser_utils.get_author",
        "semantic_release.changelog_components.parser_utils.get_commit_date",
    ]
    assert current_changelog_components() == components


# Generated at 2022-06-14 05:36:38.630949
# Unit test for function overload_configuration
def test_overload_configuration():
    # Testing the decorator set the proper config
    @overload_configuration
    def test_function(a, b=False, c="c", d=None, define=None):
        return config

    assert test_function(a=False, define=["a=True", "d=4"]) == {'a': 'True', 'd': '4'}