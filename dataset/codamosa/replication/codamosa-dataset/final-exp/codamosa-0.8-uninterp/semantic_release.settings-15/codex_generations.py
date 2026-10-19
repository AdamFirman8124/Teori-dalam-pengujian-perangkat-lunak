

# Generated at 2022-06-14 05:26:56.297347
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def func(config):
        return config

    config["key"] = "value"
    new_config = func(define=["key=new_value"])
    assert new_config["key"] == "new_value"

# Generated at 2022-06-14 05:26:58.587611
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert callable(current_changelog_components()[0])

# Generated at 2022-06-14 05:27:03.734822
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test overload_configuration decorator"""
    expected_config = config
    new_config = {**expected_config, **{"define": ["key=value"]}}
    expected_config["key"] = "value"

    @overload_configuration
    def function(**kwargs):
        return kwargs, config

    assert function(**new_config)[1] == expected_config

# Generated at 2022-06-14 05:27:16.215967
# Unit test for function overload_configuration
def test_overload_configuration():
    """Tests the "overload_configuration" decorator and the written content of
    the "config" dict, to be sure that the content of the "define" array
    overrides the content of the "config" dict.
    """
    from semantic_release.cli import main

    overload_configuration(main)

    assert config["version_variable_name"] == "__version__"
    main(["--define", "version_variable_name=VERSION"])
    assert config["version_variable_name"] == "VERSION"
    main(["--define", "version_variable_name=VERSION", "--define", "version_variable_name=__version__"])
    assert config["version_variable_name"] == "__version__"

    assert config["package_name"] == "semantic_release"

# Generated at 2022-06-14 05:27:21.133218
# Unit test for function overload_configuration
def test_overload_configuration():
    def func(define=None):
        return config["changelog_capitalize"]

    decor_func = overload_configuration(func)
    assert decor_func(define=["changelog_capitalize=False"]) is False

    assert decor_func(define=["changelog_capitalize=True"]) is False
    assert config["changelog_capitalize"] is False

# Generated at 2022-06-14 05:27:28.399334
# Unit test for function overload_configuration
def test_overload_configuration():  # noqa
    def test(arg):
        pass

    test = overload_configuration(test)

    assert "commit_parser" not in config
    test(define=["commit_parser=stdout"])
    assert config["commit_parser"] == "stdout"
    assert "initial_version" not in config
    test(define=["initial_version=1.0.0"])
    assert config["initial_version"] == "1.0.0"

# Generated at 2022-06-14 05:27:32.530864
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog_components import issues, breaking, merge_requests
    assert current_changelog_components() == [issues, breaking, merge_requests]

# Generated at 2022-06-14 05:27:39.593224
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_func(a, b, define=[]):
        return config.get(a) == b

    config.setdefault("a", "a_value")

    assert test_func(a="a", b="not_a_value", define=["a=not_a_value"])
    assert not test_func(a="a", b="a_value", define=["a=not_a_value"])

# Generated at 2022-06-14 05:27:41.148341
# Unit test for function current_commit_parser
def test_current_commit_parser():
    # change config to import my_parser
    config["commit_parser"] = "my_parser"
    assert current_commit_parser() is my_parser



# Generated at 2022-06-14 05:27:47.673245
# Unit test for function overload_configuration
def test_overload_configuration():
    import argparse
    from io import StringIO

    @overload_configuration
    def a(define):
        return define

    args = argparse.Namespace()
    args.define = ["a=b", "c=d"]

    assert a(args.define) == ["a=b", "c=d"]
    assert len(config.keys()) == 2

# Generated at 2022-06-14 05:28:07.642578
# Unit test for function overload_configuration
def test_overload_configuration():
    from click.testing import CliRunner

    # Unit test for function overload_configuration
    @overload_configuration
    def my_function(define: List[str] = None):
        print(config.get("new_key"))

    config.update({"new_key": "new_value"})
    assert config.get("new_key") == "new_value"

    runner = CliRunner()
    result = runner.invoke(
        my_function, ["--define", "new_key=new_value_overloaded"]
    )
    assert result.exit_code == 0
    assert config.get("new_key") == "new_value_overloaded"

    result = runner.invoke(my_function)
    assert result.exit_code == 0

# Generated at 2022-06-14 05:28:16.693672
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function tests the overload_configuration decorator to check that
    the config is correctly overriden.
    """
    # Create a fake dictionary
    fake_config_dict = {"version": "the_version", "define": ["version=1.1.1"]}
    # Call the decorated function and check that the config contains the new
    # version instead of the old one.
    assert overload_configuration(lambda x: x)(fake_config_dict)["version"] == "1.1.1"

# Generated at 2022-06-14 05:28:21.428282
# Unit test for function overload_configuration
def test_overload_configuration():

    @overload_configuration
    def test_function(**kwargs):
        print(config)

    test_function(define=["token=1234", "uri=https://localhost"])
    assert config == {"token": "1234", "uri": "https://localhost"}

# Generated at 2022-06-14 05:28:27.545111
# Unit test for function overload_configuration
def test_overload_configuration():
    config_test = config.copy()
    config_test["tag_format"] = "v{version}"

    args = ("DEFAULT", "DEFAULT")
    kwargs = {"define": ["tag_format=v{version}"]}
    config = overload_configuration(lambda x, y, **kwargs: [x, y, kwargs])(*args, **kwargs)

    assert config == [*args, kwargs]
    assert config_test == _config()

# Generated at 2022-06-14 05:28:40.463202
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function makes sure the parameters defined by the user are correctly
    added to the configuration.
    """

    from semantic_release.cli import main

    # Case 1: No parameters to overload
    config_no_overload = dict(config)
    main([])
    assert config == config_no_overload

    # Case 2: One parameter to overload
    config_overload_1 = dict(config)
    config_overload_1["dry_run"] = True
    main(["--define", "dry_run=True"])
    assert config == config_overload_1

    # Case 3: Two parameters to overload
    config_overload_2 = dict(config)
    config_overload_2["dry_run"] = True
    config_overload_2["commit_version_number"] = False

# Generated at 2022-06-14 05:28:54.261222
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog_components import changelog_header
    from .changelog_components import changelog_body

    assert current_changelog_components() == [changelog_header, changelog_body]

    config["changelog_components"] = ""
    assert current_changelog_components() == []

    config["changelog_components"] = (
        "semantic_release.changelog_components.changelog_header"
    )
    assert current_changelog_components() == [changelog_header]

    config["changelog_components"] = (
        "semantic_release.changelog_components.changelog_header,"
        "semantic_release.changelog_components.changelog_body"
    )

# Generated at 2022-06-14 05:28:57.278159
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser() == 'semantic_release.commit_parser.default'

# Generated at 2022-06-14 05:29:02.798802
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config['changelog_components'] = 'semantic_release.changelog.components.version,semantic_release.changelog.components.changes'
    assert len(current_changelog_components()) == 2
    for component in current_changelog_components():
        assert callable(component)

# Generated at 2022-06-14 05:29:13.525001
# Unit test for function overload_configuration
def test_overload_configuration():
    from . import semantic_release

    old_config = config.copy()
    overload_configuration(semantic_release.main)(define=['version_variable="__version__"',
                                                          'next_version="1.0"',
                                                          'upload_to_pypi="True"'])
    assert config["version_variable"] == '__version__', "version_variable failed"
    assert config["next_version"] == '1.0', "next_version failed"
    assert config["upload_to_pypi"] is True, "upload_to_pypi failed"
    config.update(old_config)

# Generated at 2022-06-14 05:29:20.776391
# Unit test for function overload_configuration
def test_overload_configuration():
    test_config = {"a": "A", "b": "B"}
    config = UserDict(test_config.copy())

    @overload_configuration
    def test(a, **kwargs):
        return a

    assert test(a="1", define=["a=test"]) == "test"
    assert test(a="2", define=["c=3"]) == "2"
    assert test(a="2", define=["a=test", "c=3"]) == "test"

# Generated at 2022-06-14 05:29:36.673509
# Unit test for function overload_configuration
def test_overload_configuration():
    expected = {'init_version': '1.0.0', 'tag_format': '{tag}'}

    @overload_configuration
    def function_to_test(define):
        return define

    assert function_to_test(define=['init_version=1.0.0', 'tag_format={tag}']) == expected
    assert function_to_test(define=['init_version=1.0.0', 'tag_format={tag}', 'other_param=value']) == expected
    assert function_to_test(define=['init_version=1.0.0', 'tag_format={tag}', 'other_param=']) == expected
    assert function_to_test(define=['init_version=1.0.0', 'tag_format={tag}', 'other_param']) == expected

# Generated at 2022-06-14 05:29:39.931990
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog_parser import ChangelogParser
    assert isinstance(current_changelog_components()[0], ChangelogParser)

# Generated at 2022-06-14 05:29:49.630951
# Unit test for function overload_configuration
def test_overload_configuration():
    from .cli import version, changelog, run, check_compatibility

    version = overload_configuration(version)
    changelog = overload_configuration(changelog)
    check_compatibility = overload_configuration(check_compatibility)
    run = overload_configuration(run)

    assert config["tag_format"] == "v{new_version}"
    assert config["version_variable"] == "__version__"
    config["tag_format"] = "1.0.0"
    config["version_variable"] = "version"
    assert config["tag_format"] == "1.0.0"
    assert config["version_variable"] == "version"
    version(define=["tag_format=v{new_version}", "version_variable=__version__"])

# Generated at 2022-06-14 05:29:54.721781
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_meth(define, verbosity):
        pass

    wrapped = overload_configuration(test_meth)
    wrapped(define=["verbosity=1"], verbosity="2")
    assert config["verbosity"] == "1"

# Generated at 2022-06-14 05:30:02.354245
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import (
        CollectCommits,
    )
    from semantic_release.utils import get_current_version, check_output  # noqa: F401

    components = current_changelog_components()
    assert len(components) == 1
    assert components[0] == CollectCommits
    assert config.get("changelog_components") == "semantic_release.changelog.CollectCommits"



# Generated at 2022-06-14 05:30:04.685890
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import ChangeLogComponents

    components = current_changelog_components()
    assert components == ChangeLogComponents

# Generated at 2022-06-14 05:30:16.514609
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def my_function(a, b, define=None):
        pass

    assert ("changelog_capitalize" in config) is True
    assert (type(config["changelog_capitalize"]) is bool) is True
    assert config["changelog_capitalize"] is False
    for param in ["changelog_capitalize=True", "changelog_scope=FALSE"]:
        my_function(a="a", b="b", define=[param])
    assert config["changelog_capitalize"] is True
    assert config["changelog_scope"] is False
    assert ("changelog_scope" in config) is True

# Generated at 2022-06-14 05:30:26.813788
# Unit test for function current_commit_parser
def test_current_commit_parser():
    # Set up a temporary file with a parser
    with open("pyproject.toml", "w") as f:
        f.write('[tool.semantic_release]\ncommit_parser="semantic_release.commit_parser.default"')
    current_commit_parser()
    os.remove("pyproject.toml")
    # Set up a temporary file with a bad parser
    with open("pyproject.toml", "w") as f:
        f.write('[tool.semantic_release]\ncommit_parser="semantic_release.commit_parser.default_bad_name"')
    try:
        current_commit_parser()
    except ImproperConfigurationError:
        os.remove("pyproject.toml")

# Generated at 2022-06-14 05:30:31.351985
# Unit test for function overload_configuration
def test_overload_configuration():
    config["plugin_test"] = None
    config["plugin_test2"] = "yes"

    @overload_configuration
    def get_config(define):
        assert config["plugin_test"] == "first"
        assert config["plugin_test2"] == "second"
        return config

    get_config(define=["plugin_test=first", "plugin_test2=second"])
    # Global config modification should not be persistant
    assert config["plugin_test"] is None
    assert config["plugin_test2"] == "yes"

# Generated at 2022-06-14 05:30:39.933148
# Unit test for function overload_configuration
def test_overload_configuration():
    config["python_interpreter"] = "python_interpreter_value"
    with overload_configuration(lambda x : x):
        pass
    assert config["python_interpreter"] == "python_interpreter_value"

    with overload_configuration(lambda x : x):
        config["python_interpreter"] = "python_interpreter_value2"
    assert config["python_interpreter"] == "python_interpreter_value2"

    with overload_configuration(lambda x : x):
        assert config["python_interpreter"] == "python_interpreter_value2"

    with overload_configuration(lambda x : x):
        assert config["python_interpreter"] == "python_interpreter_value2"

# Generated at 2022-06-14 05:30:53.185715
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_overload_configuration"] = "foo"

    @overload_configuration
    def overload_configuration_function(define=None):
        if define:
            return config["test_overload_configuration"] == "bar"
        else:
            return config["test_overload_configuration"] == "foo"

    assert overload_configuration_function()
    assert overload_configuration_function(define="test_overload_configuration=bar")


# Generated at 2022-06-14 05:30:57.095476
# Unit test for function overload_configuration
def test_overload_configuration():
    # Before
    assert "name" in config
    assert config["name"] == "semantic-release"
    # When
    test_func = overload_configuration(lambda x: x)(define=["name=foo"])
    # After
    assert "name" in config
    assert config["name"] == "foo"



# Generated at 2022-06-14 05:31:06.792645
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_overload(define):
        return {
            key: config[key]
            for key in ("changelog_capitalize", "changelog_scope", "commit_parser")
        }

    assert test_overload(define=("changelog_capitalize=True", "commit_parser=my.function")) == {
        "changelog_capitalize": True,
        "changelog_scope": "",
        "commit_parser": "my.function",
    }



# Generated at 2022-06-14 05:31:07.998923
# Unit test for function current_commit_parser
def test_current_commit_parser():
    current_commit_parser()

# Generated at 2022-06-14 05:31:16.213103
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test the function overload_configuration."""
    # Test with a bad config
    @overload_configuration
    def test_overload_configuration(define=None):
        return define
    config["info"] = "value"

    assert test_overload_configuration(define=["info=value"]) == None
    assert config["info"] == "value"
    assert test_overload_configuration(define=["info=new_value"]) == None
    assert config["info"] == "new_value"

    # Test with a good config
    @overload_configuration
    def test_overload_configuration(define=None):
        return define
    config["info"] = "value"

    assert test_overload_configuration(define=["info=value"]) is None

# Generated at 2022-06-14 05:31:22.223904
# Unit test for function overload_configuration
def test_overload_configuration():
    config["foo"] = "false"
    config["bar"] = "false"

    @overload_configuration
    def test_func(*args, **kwargs):
        return

    test_func(define=["foo=true", "bar=true"])

    assert config["foo"] == "true"
    assert config["bar"] == "true"

# Generated at 2022-06-14 05:31:30.557760
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from .commit_parser import parse_commits

    # Set the config attribute to a custom function
    config["commit_parser"] = "semantic_release.history.my_parse_commits"
    
    # Test if the function returns the custom function
    assert current_commit_parser() == my_parse_commits
    
    # Set the config attribute to the default function
    config["commit_parser"] = "semantic_release.commit_parser.parse_commits"
    
    # Test if the function returns the default function
    assert current_commit_parser() == parse_commits


# Generated at 2022-06-14 05:31:40.517504
# Unit test for function overload_configuration
def test_overload_configuration():
    # We define a function which will be decorated
    def my_function(my_str):
        # We edit the value of key "value"
        config["value"] = my_str
        return config
    # The value of "value" is "init"
    assert my_function("init")["value"] == "init"
    # We decorate the function
    my_function_decorated = overload_configuration(my_function)
    # We overload the config with "value=overload"
    assert my_function_decorated("hello", define=["value=overload"])["value"] == "overload"

# Generated at 2022-06-14 05:31:45.469766
# Unit test for function overload_configuration
def test_overload_configuration():
    assert current_commit_parser() == current_commit_parser()
    # Config is declared "config = _config" at the begining of this file
    assert config.get("changelog_components") == "nolint:duplicate"
    assert config.get("commit_parser") == "semantic_release.commit_parser:parse"
    assert current_commit_parser() != current_commit_parser()

# Generated at 2022-06-14 05:31:57.239004
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import Changelog

    test_changelog_components = [
        "semantic_release.changelog.ChangelogSection.feature_changes",
        "semantic_release.changelog.ChangelogSection.bug_fixes",
    ]
    config["changelog_components"] = ",".join(test_changelog_components)
    changelog_components = current_changelog_components()

    assert changelog_components[0] == ChangelogSection.feature_changes
    assert changelog_components[1] == ChangelogSection.bug_fixes
    assert len(changelog_components) == 2



# Generated at 2022-06-14 05:32:17.021585
# Unit test for function overload_configuration
def test_overload_configuration():
    def f(define):
        return define

    def f2(define, define2):
        return define, define2

    assert f(["key=value"]) == ["key=value"]
    assert f2(["key=value"]) == (["key=value"],)
    assert f2(["key=value", "key2=value2"]) == (["key=value", "key2=value2"],)

    @overload_configuration
    def f(define):
        return define

    @overload_configuration
    def f2(define, define2):
        return define, define2

    assert f(["key=value"]) == ["key=value"]
    assert f2(["key=value"]) == (["key=value"],)

# Generated at 2022-06-14 05:32:22.148508
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert "changelog_components" not in config
    assert current_changelog_components() == []
    config['changelog_components'] = "semantic_release.changelog.components.new_features"
    assert current_changelog_components() == [component_new_features]

# Generated at 2022-06-14 05:32:29.822164
# Unit test for function overload_configuration
def test_overload_configuration():
    """ Test overload configuration for sharing plugins """
    plugin_config = {"config": "config"}
    test_overload_configuration.called = False
    test_overload_configuration.plugin_config = plugin_config

    @overload_configuration
    def foo(plugin_config):
        test_overload_configuration.called = True
        return plugin_config

    foo(define=["package_name=my_package_name"], plugin_config=plugin_config)
    assert test_overload_configuration.called

# Generated at 2022-06-14 05:32:35.942540
# Unit test for function overload_configuration
def test_overload_configuration():
    # The function must have at least one argument,
    # so we use a fake function with a "define" argument.
    @overload_configuration
    def fake_function(define=None):
        pass
    # To test this, the config is empty, so we add a "prerelease" key,
    # and then check that the value has been correctly added in the config.
    assert "prerelease" not in config
    fake_function(define=["prerelease=true"])
    assert config["prerelease"] == "true"



# Generated at 2022-06-14 05:32:38.671453
# Unit test for function current_commit_parser
def test_current_commit_parser():
    path = current_commit_parser()
    assert path == config.get("commit_parser")

# Generated at 2022-06-14 05:32:39.981402
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser()



# Generated at 2022-06-14 05:32:49.421107
# Unit test for function overload_configuration
def test_overload_configuration():
    from .commands import release

    # Check the temporary replacement of a configuration
    assert config["tag_format"] == "v{version}"

    # Release with a modified configuration
    release(define=["tag_format=new"])

    # Check if the configuration was updated
    assert config["tag_format"] == "new"
    # Restore the default configuration
    config["tag_format"] == "v{version}"

    # Check the case when the configuration is not updated
    assert config["tag_format"] == "v{version}"
    release(define=[])
    assert config["tag_format"] == "v{version}"

# Generated at 2022-06-14 05:32:54.028220
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def foo(x, y, define=None):
        assert x == 1
        assert y == 2
        assert config['user_agent'] == "foo"
        assert config['plugins'] == "tuple"

    foo(1, 2, define=["user_agent=foo", "plugins=tuple"])

# Generated at 2022-06-14 05:33:02.925050
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function tests the overload_configuration function with the following cases:

    - empty "define" parameter
    - undefined parameter
    - two parameters with a value
    """

    @overload_configuration
    def func(define=None):
        pass

    func()
    func(define=["foo"])
    func(define=["foo=bar", "biz=baz"])
    func(define=["foo=bar", "biz=baz", "biz=boz"])



# Generated at 2022-06-14 05:33:07.436962
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config["changelog_components"] = "semantic_release.changelog.components.Unreleased,semantic_release.changelog.components.Commits"
    assert len(current_changelog_components()) == 2

# Generated at 2022-06-14 05:33:18.191675
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == [
        semantic_release.changelog.components.AngularCommitStyleguide,
        semantic_release.changelog.components.RstChangelog,
    ]



# Generated at 2022-06-14 05:33:24.187780
# Unit test for function current_changelog_components
def test_current_changelog_components():
    import_path = "test.test_helpers"
    config["changelog_components"] = import_path
    component = importlib.import_module(import_path).changelog_component
    assert current_changelog_components() == [component]

# Generated at 2022-06-14 05:33:35.998423
# Unit test for function overload_configuration
def test_overload_configuration():
    def initial_config():
        return {"a": "b", "c": "d"}

    def no_config():
        return {}

    @overload_configuration
    def test_func(config):
        return config

    assert test_func(config=initial_config()) == {"a": "b", "c": "d"}
    assert test_func(config=initial_config(), define=["x=y"]) == {"a": "b", "c": "d", "x": "y"}
    assert test_func(config=initial_config(), define=["c=e", "x=y"]) == {"a": "b", "c": "e", "x": "y"}

# Generated at 2022-06-14 05:33:46.999639
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    Test that the overload_configuration decorator creates a correct config
    """

    @overload_configuration
    def test_func(arg1, arg2, kwarg1, kwarg2, kwarg3=None):
        pass

    # Check that the default value is used
    test_func("a", "b", "c", "d")
    assert config.get("kwarg3") is None

    # Check that the key is added to the config
    test_func("a", "b", "c", "d", define=["kwarg3=4"])
    assert config.get("kwarg3") == "4"

    # Check that the value of the key is updated in the config
    test_func("a", "b", "c", "d", define=["kwarg3=5"])
   

# Generated at 2022-06-14 05:33:56.192111
# Unit test for function overload_configuration
def test_overload_configuration():
    config["project_name"] = "old_project_name"
    config["project_name_genitive"] = "old_project_name_genitive"

    @overload_configuration
    def func():
        pass

    func(define=["project_name=new_project_name", "project_name_genitive=new_project_name_genitive,"])

    assert config["project_name"] == "new_project_name"
    assert config["project_name_genitive"] == "new_project_name_genitive"



# Generated at 2022-06-14 05:34:05.269580
# Unit test for function overload_configuration
def test_overload_configuration():
    # Get the content of the "define" array and edit "config" according to the pairs of key/value
    def mock_function(myargument, define=None):
        if myargument in config:
            return config[myargument]
        else:
            return "None"

    decorated = overload_configuration(mock_function)
    defined = ["changelog_components=foo,bar", "commit_parser=baz.qux"]
    assert decorated("changelog_components", define=defined) == "foo,bar"
    assert decorated("commit_parser", define=defined) == "baz.qux"
    assert decorated("plugin1", define=defined) == "None"



# Generated at 2022-06-14 05:34:18.106678
# Unit test for function overload_configuration
def test_overload_configuration():
    # Calls the function without value of "define" field
    assert overload_configuration(lambda: 0)() == 0
    # Sets the value of "define" to an empty array
    assert overload_configuration(lambda: 0)(define=[]) == 0

    # Overloads the existing configuration value
    assert overload_configuration(lambda: 0)(define=["verbose=True"]) == 0
    assert config["verbose"] == "True"

    # Overloads the existing configuration value with whitespaces
    assert overload_configuration(lambda: 0)(define=["verbose = True"]) == 0
    assert config["verbose"] == "True"

    # Overloads the non existing configuration value
    assert overload_configuration(lambda: 0)(define=["new_value=1"]) == 0
    assert config["new_value"] == "1"

    #

# Generated at 2022-06-14 05:34:27.664070
# Unit test for function overload_configuration
def test_overload_configuration():
    configuration_dict = {"a": "A", "b": "B"}
    config.update(configuration_dict)

    @overload_configuration
    def test_function(define):
        if "define" in locals():
            for pair in define.split(","):
                for k, v in configuration_dict.items():
                    if k in pair:
                        configuration_dict[k] = pair.split("=", maxsplit=1)[1]

    test_function(define="a=AA,b=BB")
    assert configuration_dict == {"a": "AA", "b": "BB"}

# Generated at 2022-06-14 05:34:36.715090
# Unit test for function overload_configuration
def test_overload_configuration():
    config.clear()
    config["foo"] = "bar"
    @overload_configuration
    def test():
        return config["foo"]
    test()
    assert config["foo"] == "bar"
    test(define=["foo=baz"])
    assert config["foo"] == "baz"
    test()
    assert config["foo"] == "baz"
    test(define=["foo=baz", "foo=bar", "bar=baz"])
    assert config["foo"] == "bar"
    assert config["bar"] == "baz"

# Generated at 2022-06-14 05:34:47.157244
# Unit test for function overload_configuration
def test_overload_configuration():
    class TestObject:
        @overload_configuration
        def test(self, defined_param):
            pass

    test_object = TestObject()
    assert (
        test_overload_configuration.__doc__
        == overload_configuration.__doc__
    )
    assert (
        test_overload_configuration.__name__
        == overload_configuration.__name__
    )
    test_object.test(define=["keytest=valuetest"])
    assert config["keytest"] == "valuetest"



# Generated at 2022-06-14 05:34:57.882127
# Unit test for function overload_configuration
def test_overload_configuration():
    def my_function(name="default_value"):
        return name

    assert my_function() == "default_value"

    my_function = overload_configuration(my_function)
    assert my_function(define=["name=my_name"]) == "my_name"

# Generated at 2022-06-14 05:35:05.332853
# Unit test for function overload_configuration
def test_overload_configuration():
    # Define a very simple config
    @overload_configuration
    def test_function(define):
        return define

    # Test with a list of keys
    fake_define = ["key=value", "key2=value2"]
    test_function(define=fake_define)

    assert config["key"] == "value"
    assert config["key2"] == "value2"

# Generated at 2022-06-14 05:35:10.525972
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test that overload_configuration decorator works as expected.

    The test is done by faking the function that would be decorated and
    checking that the function parameters have been updated according to the
    overload.
    """

    from semantic_release.config import get_config

    @overload_configuration
    def load_config(**kwargs):
        return kwargs

    assert load_config(config={"test": "value"}, define=["test=new_value"]) == {
        "test": "new_value"
    }
    assert get_config()["test"] == "value"

# Generated at 2022-06-14 05:35:17.275904
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test if the configuration can be overloaded by calling the function with
    the option --define."""
    @overload_configuration
    def _test_overload_configuration(option: str) -> str:
        return config[str(option)]

    assert _test_overload_configuration("dry_run", define=["dry_run=True"]) == "True"

# Generated at 2022-06-14 05:35:23.629396
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test overload_configuration decorator.
    """

    def foo():
        return config["commit_parser"]

    # Default config value
    assert foo() == "semantic_release.commit_parser.default_parser"

    # Overloaded config value
    @overload_configuration
    def foo():
        return config["commit_parser"]

    assert foo(define=["commit_parser=foo.bar"]) == "foo.bar"

# Generated at 2022-06-14 05:35:27.292166
# Unit test for function overload_configuration
def test_overload_configuration():
    config["dry_run"] = True

    @overload_configuration
    def dry_run(define):
        return config["dry_run"]

    assert dry_run(define=["dry_run=false"]) is False
    assert dry_run() is True

# Generated at 2022-06-14 05:35:30.905463
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def _test(define):
        pass

    _test(define=["foo=bar"])
    assert config["foo"] == "bar"

# Generated at 2022-06-14 05:35:41.999359
# Unit test for function overload_configuration
def test_overload_configuration():
    assert config["branch"] == "master"
    assert config["tag_format"] == "v{version}"

    # Call the current_version() function with a "define" parameter
    # The value of "define" is a list of string "key=value"
    # As the current_version() function is decorated, the "config" dictionary
    # will be modified before the function is called.
    # Thus, the new values of config will be used by the function.
    # This allows to override the values of "config" only for the function.
    #
    # Here we change the value of two parameters: "branch" and "tag_format"
    # to test that the decorator works as expected.
    from .utils import current_version
    from .version import Version

# Generated at 2022-06-14 05:35:53.382316
# Unit test for function current_commit_parser
def test_current_commit_parser():
    import semantic_release.commit_parser

    config["commit_parser"] = "semantic_release.commit_parser.default"
    assert callable(current_commit_parser())
    assert (
        current_commit_parser()
        == semantic_release.commit_parser.default
    )

    config["commit_parser"] = "semantic_release.commit_parser.no_breaking_or_features"
    assert callable(current_commit_parser())
    assert (
        current_commit_parser()
        == semantic_release.commit_parser.no_breaking_or_features
    )



# Generated at 2022-06-14 05:35:59.227333
# Unit test for function overload_configuration
def test_overload_configuration():
    # Unitary test for overload_configuration
    def test_function(foo, bar="default", *args, **kwargs):
        return foo, bar

    u_test_function = overload_configuration(test_function)

    assert u_test_function(*["foo"], define=["bar=baz"]) == ("foo", "baz")

# Generated at 2022-06-14 05:36:09.551506
# Unit test for function current_changelog_components
def test_current_changelog_components():
    components = current_changelog_components()
    assert isinstance(components,list)
    assert len(components)==3


# Generated at 2022-06-14 05:36:16.893725
# Unit test for function overload_configuration
def test_overload_configuration():
    config["key"] = "original_value"
    assert config["key"] == "original_value"

    @overload_configuration
    def func(definition):
        return definition

    overloaded_value = func(define=["key=overloaded_value"])
    assert overloaded_value == {"key": "overloaded_value"}
    assert config["key"] == overloaded_value["key"]

# Generated at 2022-06-14 05:36:26.109329
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def fct(a, b):
        return (a, b)

    config["test"] = "old_config_value"
    assert fct(a="a", b="b") == ("a", "b")
    assert config["test"] == "old_config_value"

    assert fct(a="a", b="b", define=["test=new_config_value"]) == ("a", "b")
    assert config["test"] == "new_config_value"

# Generated at 2022-06-14 05:36:35.175279
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import (
        header_component,
        tasks_component,
        features_component,
        breaking_changes_component,
        issues_component,
        authors_component,
        footer_component,
    )
    from semantic_release.version_check import get_version_components

    component_paths = config.get("changelog_components").split(",")

    components = list()


# Generated at 2022-06-14 05:36:46.925620
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_setting"] = "test_setting_value"
    config["test_setting_2"] = "test_setting_value_2"

    @overload_configuration
    def example_function(define):
        pass

    example_function(define=["test_setting=overloaded_value"])
    assert config["test_setting"] == "overloaded_value"
    assert config["test_setting_2"] == "test_setting_value_2"

    example_function(define=["test_setting_3=overloaded_value_3"])
    assert "test_setting_3" in config
    assert config["test_setting_3"] == "overloaded_value_3"