

# Generated at 2022-06-14 05:27:03.936864
# Unit test for function overload_configuration
def test_overload_configuration():
    function_with_define = overload_configuration(lambda x: x)
    assert config["check_build_status"]
    assert config["major_on_zero"]
    assert config["upload_to_release"]
    assert config["upload_to_pypi"]
    assert config["commit_parser"] == "semantic_release.commit_parser.default_commit_parser"
    assert config["changelog_components"] == "semantic_release.changelog.component.Features,semantic_release.changelog.component.Bugfixes"
    assert config["changelog_components"] == "semantic_release.changelog.component.Features,semantic_release.changelog.component.Bugfixes"

# Generated at 2022-06-14 05:27:16.911186
# Unit test for function overload_configuration
def test_overload_configuration():
    global config
    config = _config()
    @overload_configuration
    def test_function(define, **kwargs):
        expected_config = _config()
        expected_config["tag_name"] = "release-{version}"
        expected_config["rewrite_version"] = False
        expected_config["remove_dist"] = False
        assert config == expected_config
    test_function(define=["tag_name=release-{version}",
                          "rewrite_version=false",
                          "remove_dist=false"])

# Generated at 2022-06-14 05:27:22.482975
# Unit test for function overload_configuration
def test_overload_configuration():
    config["changelog_components"] = "changelog.my_component"

    @overload_configuration
    def my_function(define):
        config["changelog_components"] = "changelog.your_component"

    my_function(define="changelog_components=changelog.our_component")
    assert current_changelog_components()[0].__name__ == "our_component"

# Generated at 2022-06-14 05:27:32.160818
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == []
    config["changelog_components"] = "random, random_stuff"
    with pytest.raises(ImproperConfigurationError) as exc:
        current_changelog_components()
    assert "Unable to import changelog component" in str(exc.value)
    config["changelog_components"] = "semantic_release.commit_parser"
    with pytest.raises(ImproperConfigurationError) as exc:
        current_changelog_components()
    assert "is not a valid changelog component" in str(exc.value)
    config["changelog_components"] = "semantic_release.changelog_components"
    with pytest.raises(ImproperConfigurationError) as exc:
        current_changelog

# Generated at 2022-06-14 05:27:42.390326
# Unit test for function overload_configuration
def test_overload_configuration():
    """fake a "define" argument in the argparse's Namespace and check if the values are
    added locally to the config dict.
    """

    def test(arg):  # pylint: disable=unused-argument
        return config

    wrapped = overload_configuration(test)
    assert wrapped("")["commit_parser"] == "semantic_release.commit_parser.default"

    wrapped("", define=["commit_parser=my-custom-commit-parser", "configured_key=value"])
    assert config["commit_parser"] == "my-custom-commit-parser"
    assert config["configured_key"] == "value"

# Generated at 2022-06-14 05:27:52.409225
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog import component_sections
    from .components import changes, bugs, security

    from .components import ChangelogComponent

    class DummyComponent(ChangelogComponent):
        pass

    config["changelog_components"] = ",".join(
        [component.__name__ for component in component_sections]
    )
    for component in component_sections:
        assert component in current_changelog_components()

    config["changelog_components"] = ",".join(["DummyComponent"])
    assert DummyComponent in current_changelog_components()

    config["changelog_components"] = ",".join(
        [DummyComponent.__name__, changes.__name__]
    )
    assert changes in current_changelog_components()

    config

# Generated at 2022-06-14 05:27:58.289731
# Unit test for function overload_configuration
def test_overload_configuration():
    config["new_key"] = "old_value"

    @overload_configuration
    def overloaded_func(new_key):
        assert config["new_key"] == "new_value"

    overloaded_func(define=["new_key=new_value"])
    assert config["new_key"] == "old_value"

# Generated at 2022-06-14 05:28:09.853184
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.components import Changelog
    from semantic_release.changelog import ChangelogParser

    path = "tests.fixtures.dummy_components"
    config["changelog_components"] = f"{path}.set_commits,{path}.set_milestone"
    components = current_changelog_components()

    changelog_parser = ChangelogParser(milestone_pattern="(?<=\[)(.*)(?=\])")
    changelog = Changelog(changelog_parser=changelog_parser)
    for component in components:
        component(changelog)

    assert config["commits"] == "dummy_commits"
    assert config["milestone"] == "dummy_milestone"

# Generated at 2022-06-14 05:28:18.443440
# Unit test for function overload_configuration
def test_overload_configuration():
    config['test_key'] = "original value"
    @overload_configuration
    def func_with_overload_configuration(define):
        return config['test_key']

    # change the value of config['test_key']
    assert func_with_overload_configuration(define="test_key=new value") == "new value"

    # make sure the original value of config['test_key'] is not changed
    assert config['test_key'] == "original value"

# Generated at 2022-06-14 05:28:25.170916
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function():
        pass

    with open("/tmp/setup.cfg", "w") as setup_cfg:
        setup_cfg.write(
            """
[semantic_release]
commit_parser = semantic_release.commit_parser.default
changelog_components =
upload_to_pypi = True
"""
        )
    test_function(define=["upload_to_pypi=False"])
    assert config["upload_to_pypi"] == "False"



# Generated at 2022-06-14 05:28:39.139822
# Unit test for function overload_configuration
def test_overload_configuration():
    def dummy(x, y, **kwargs):
        return x * y

    decorated = overload_configuration(dummy)
    assert decorated(2, 3) == 6
    assert config["verbosity"] == "info"

    decorated(2, 3, define=["verbosity=critical"])
    assert config["verbosity"] == "critical"



# Generated at 2022-06-14 05:28:44.130164
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(define=[], key1=None, key2=None):
        return key1, key2

    assert test_function(define=["key1=value1"]) == ("value1", None)

    assert test_function(define=["key1=value1", "key2=value2"]) == ("value1", "value2")

# Generated at 2022-06-14 05:28:48.478268
# Unit test for function overload_configuration
def test_overload_configuration():
    config['test'] = 'initial value'
    @overload_configuration
    def test(define=[]):
        return config['test']

    assert test(define=['test=new value']) == 'new value'

# Generated at 2022-06-14 05:28:55.925005
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert (
        "semantic_release.changelog.components_list"
        in config.get("changelog_components")
    )
    assert "semantic_release.changelog" in config.get("changelog_components")
    assert "semantic_release.changelog.default" in config.get("changelog_components")
    assert "semantic_release.changelog.issues" in config.get("changelog_components")

# Generated at 2022-06-14 05:28:58.237922
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components()
    assert isinstance(current_changelog_components(), list)

# Generated at 2022-06-14 05:29:00.426719
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """
    Test current commit parser function and the selected commit parser class
    """
    pass



# Generated at 2022-06-14 05:29:03.599984
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == []


test_current_changelog_components()

# Generated at 2022-06-14 05:29:15.393883
# Unit test for function overload_configuration
def test_overload_configuration():
    old_config = config

    # mock a configuration
    config = {
        "custom_key_1": "old_value",
        "custom_key_2": "old_value",
        "custom_key_3": "old_value",
    }

    @overload_configuration
    def custom_function(define):
        return define

    # test 1: defining new key
    assert custom_function(define=["custom_key_4=new_value"]) == ["custom_key_4=new_value"]
    assert config["custom_key_4"] == "new_value"
    del config["custom_key_4"]

    # test 2: updating existing key
    assert custom_function(define=["custom_key_1=new_value"]) == ["custom_key_1=new_value"]
    assert config

# Generated at 2022-06-14 05:29:22.206392
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_config"] = "test_ok"

    @overload_configuration
    def test_func(define: List[str]):
        assert config["test_config"] == "overload_ok"

    test_func(define=["test_config=overload_ok"])
    assert config["test_config"] == "test_ok"

# Generated at 2022-06-14 05:29:26.633602
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def foo(x):
        return x

    config["foo"] = "bar"
    assert foo("baz", define=["foo=baz"]) == "baz"
    assert config["foo"] == "baz"



# Generated at 2022-06-14 05:29:47.221130
# Unit test for function current_changelog_components
def test_current_changelog_components():
    commit_data1 = "The commit title 1."
    commit_data2 = "The commit title 2."
    commit_data3 = "The commit title 3."
    valid_title1 = "The commit title 1. The commit body."
    valid_title2 = "The commit title 2. The commit body."
    valid_title3 = "The commit title 3. The commit body."

    def valid_parser1(message):
        title, _, body = message.partition("\n")
        return {
            "title": title.replace(" ", "_"),
            "body": body,
            "footer": "The commit footer 1.",
            "revert": "",
        }

    def valid_parser2(message):
        title, _, body = message.partition("\n")

# Generated at 2022-06-14 05:29:50.697253
# Unit test for function overload_configuration
def test_overload_configuration():
    config["no_token"] = "False"

    @overload_configuration
    def test():
        return config["no_token"]

    assert test() == "False"
    assert test(define=["no_token=True"]) == "True"

# Generated at 2022-06-14 05:30:03.692033
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function tests the overload_configuration function."""
    # Declare the function that will be used for testing
    @overload_configuration
    def function_to_decorate(define):
        """This is a dummy function that plays the role of a command."""
        pass
    # Define and launch unit tests for the decorator
    for defined_param in [["first=two"],
                          ["third=4"],
                          ["test=test", "third=4", "first=two"],
                          ["test=test", "third=four", "first=2"],
                          ["test=test", "third=0", "first=two"],
                          ["test=test", "third=4", "first=2", "other=value"]]:
        function_to_decorate(define=defined_param)

# Generated at 2022-06-14 05:30:12.124058
# Unit test for function overload_configuration
def test_overload_configuration():
    result = {}

    def test_function(define=None):
        if define:
            for defined_param in define:
                pair = defined_param.split("=", maxsplit=1)
                if len(pair) == 2:
                    result[str(pair[0])] = pair[1]

    # Using the overload_configuration decorator
    overload_configuration(test_function)(define=['test_name=test_value'])
    assert result == {'test_name': 'test_value'}

    # Using the test_function with default parameters
    test_function()
    assert result == {'test_name': 'test_value'}

    # Using the test_function with define parameter
    test_function(define=['test_name=test_value'])

# Generated at 2022-06-14 05:30:17.987970
# Unit test for function overload_configuration
def test_overload_configuration():
    conf = dict(hello="world")
    conf_copy = conf.copy()

    @overload_configuration
    def func(define):
        assert conf["hello"] == "world2"
        assert conf_copy["hello"] == "world"  # unmodified

    func(define=["hello=world2"])



# Generated at 2022-06-14 05:30:25.369151
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Test current_changelog_components"""

    config["changelog_components"] = "semantic_release.tests.changelog_components.test_component1"
    assert len(current_changelog_components()) == 1
    assert callable(current_changelog_components()[0])

    config["changelog_components"] = "semantic_release.tests.changelog_components.test_component1,semantic_release.tests.changelog_components.test_component2"
    assert len(current_changelog_components()) == 2
    assert callable(current_changelog_components()[0])
    assert callable(current_changelog_components()[1])


# Generated at 2022-06-14 05:30:33.692826
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog import (
        author,
        date,
        group_commits,
        package_name,
        section_titles,
        sort_commits,
        title,
    )

    comp = current_changelog_components()
    assert set(comp) == {
        author,
        date,
        group_commits,
        package_name,
        section_titles,
        sort_commits,
        title,
    }

# Generated at 2022-06-14 05:30:38.842623
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_func(age):
        return config.get("age")

    assert test_func(age=30, define=["age=26"]) == "26"
    assert config.get("age") == "26"

# Generated at 2022-06-14 05:30:42.467064
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert all(
        [x.__name__ == "zero_or_more_commits" for x in current_changelog_components()]
    )

# Generated at 2022-06-14 05:30:51.887089
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function tests function overload_configuration. It tests with
    keyword "define" and without.
    """

    def test_call_without_define(config):
        assert config.get("hello") == "world"

    @overload_configuration
    def test_call_with_define(config):
        assert config.get("hello") == "world"

    # This should not modify config
    test_call_without_define(config)
    # This should modify config
    test_call_with_define(config, define=["hello=python"])
    assert config.get("hello") == "python"

# Generated at 2022-06-14 05:31:05.071075
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from .commit_parser import parse_commits

    config["commit_parser"] = "semantic_release.commit_parser.parse_commits"
    assert current_commit_parser() == parse_commits



# Generated at 2022-06-14 05:31:13.695044
# Unit test for function overload_configuration
def test_overload_configuration():
    test_config = _config()
    test_config["new_key"] = "new_value"
    test_config["existing_key"] = "new_value"

    @overload_configuration
    def func():
        pass

    func(define=["new_key=new_value", "existing_key=new_value"])
    assert config.data == test_config

    @overload_configuration
    def func_error():
        raise ImproperConfigurationError("test")

    try:
        func_error(define=["wrong_param_number"])
    except ImproperConfigurationError as e:
        assert "test" in str(e)



# Generated at 2022-06-14 05:31:19.067033
# Unit test for function overload_configuration
def test_overload_configuration():
    config["overload"] = "before"

    # Parameters
    @overload_configuration
    def my_function(define):
        return config["overload"]

    # Define test_function parameters
    assert my_function(define="overload=after") == "after"
    assert config["overload"] == "after"

# Generated at 2022-06-14 05:31:21.808398
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from semantic_release.commit_parser import standard_parse

    assert current_commit_parser() == standard_parse



# Generated at 2022-06-14 05:31:28.009521
# Unit test for function overload_configuration
def test_overload_configuration():
    config = {"define": ["first_key=first_value", "second_key=second_value"]}
    @overload_configuration
    def deco_overload_configuration(**kwargs):
        print(config)
    deco_overload_configuration(**config)
    assert config == {"first_key": "first_value", "second_key": "second_value"}

# Generated at 2022-06-14 05:31:38.753164
# Unit test for function overload_configuration
def test_overload_configuration():
    from . import settings

    assert "commit_message" in settings.config
    assert "changelog_components" in settings.config

    @settings.overload_configuration
    def test_call_with_overload():
        settings.commit_message()
        settings.changelog_components()

    test_call_with_overload(define=["commit_message=foo"])
    assert settings.config["commit_message"] == "foo"

    test_call_with_overload(define=["changelog_components=foo"])
    assert settings.config["changelog_components"] == "foo"

# Generated at 2022-06-14 05:31:41.401604
# Unit test for function overload_configuration
def test_overload_configuration():
    from .main import main
    overload_configuration(main)
    assert True

# Generated at 2022-06-14 05:31:47.294590
# Unit test for function overload_configuration
def test_overload_configuration():
    from .cli import main

    test_config = config.copy()
    test_config["no_confirm"] = "True"
    test_config["pypi_url"] = "https://test.pypi.org/legacy/"

    # test_config is not overloaded
    assert test_config != config

    # test_config is overloaded
    main(["-D", "no_confirm=True", "-D", "pypi_url=https://test.pypi.org/legacy/"], test_config)
    assert test_config == config

# Generated at 2022-06-14 05:31:55.081160
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    This test that the config is correctly updated with the value given in the define array
    """
    # We start by defining two dummy functions
    def f(define):
        return {'define': define}

    def g(define):
        return {'define': define}

    # We use the decorator function
    f = overload_configuration(f)
    g = overload_configuration(g)

    # The config is not changed
    assert len(config) == 0

    # We call the function
    f(define=['test=test'])

    assert config.get('test') == 'test'

    # We delete the key test
    del config['test']

    # We call the function with several keys
    g(define=['test1=test1', 'test2=test2', 'test3=test3'])



# Generated at 2022-06-14 05:31:57.298140
# Unit test for function current_commit_parser
def test_current_commit_parser():
    try:
        current_commit_parser()
    except ImproperConfigurationError:
        pass



# Generated at 2022-06-14 05:32:08.783193
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .lib.components import link, summary

    assert current_changelog_components() == [link, summary]

# Generated at 2022-06-14 05:32:20.063317
# Unit test for function current_changelog_components

# Generated at 2022-06-14 05:32:27.789703
# Unit test for function current_changelog_components
def test_current_changelog_components():
    changelog_components = config.get("changelog_components")
    config["changelog_components"] = "semantic_release.changelog.components.issues,semantic_release.changelog.components.user"

    from semantic_release.changelog import components

    assert current_changelog_components() == [components.issues, components.user]
    config["changelog_components"] = changelog_components

# Generated at 2022-06-14 05:32:35.001576
# Unit test for function overload_configuration
def test_overload_configuration():
    dict_original = config
    # Call function with an undefined parameter
    current_commit_parser()

    # Execute function with a defined parameter
    @overload_configuration
    def function(a):
        return a

    function(define=["commit_parser=semantic_release.commit_parser.default"], a=[1, 2, 3])

    assert config["commit_parser"] == "semantic_release.commit_parser.default"

    config = dict_original

# Generated at 2022-06-14 05:32:47.602067
# Unit test for function overload_configuration
def test_overload_configuration():
    def add(x, y):
        return x + y

    def multiply(x, y):
        return x * y

    add_decorated = overload_configuration(add)
    multiply_decorated = overload_configuration(multiply)

    result = add_decorated(5, 10, define=None)
    assert result == 15

    result = multiply_decorated(5, 10, define=None)
    assert result == 50

    result = add_decorated(5, 10, define=["x=2", "y=1"])
    assert result == 2

    result = multiply_decorated(5, 10, define=["x=2", "y=1"])
    assert result == 10

# Generated at 2022-06-14 05:32:53.712295
# Unit test for function overload_configuration
def test_overload_configuration():
    def func():
        pass

    # overload_configuration should return a function which will return nothing
    assert overload_configuration(func)() is None

    @overload_configuration
    def func(define=[]):
        return config["key"]

    config["key"] = "value"
    # key is defined in config and config["key"] is "value"
    assert func() == "value"
    # key is redefined with "new_value"
    assert func(define=["key=new_value"]) == "new_value"

# Generated at 2022-06-14 05:33:07.308663
# Unit test for function overload_configuration
def test_overload_configuration():
    config["commit_parser"] = "semantic_release.hvcs.git.commit_parser"

    @overload_configuration
    def test_method(define):
        return config["commit_parser"]

    assert test_method(["commit_parser=semantic_release.hvcs.hg.commit_parser"]) == "semantic_release.hvcs.hg.commit_parser"
    assert test_method(["commit_parser=semantic_release.hvcs.hg.commit_parser", "version_variable=__version__"]) == "semantic_release.hvcs.hg.commit_parser"

# Generated at 2022-06-14 05:33:16.659966
# Unit test for function overload_configuration
def test_overload_configuration():

    @overload_configuration
    def func(foo, bar="default_bar", define=None):
        return foo, bar

    assert func(1, define=["foo=2"]) == (1, "default_bar")
    assert func(1, define=["bar=3"]) == (1, "3")
    assert config["foo"] == "2"
    assert config["bar"] == "3"
    assert config["commit_parser"] == "semantic_release.commit_parser"
    assert config["changelog_components"] == "semantic_release.changelog.component"

    # Raise an error if the key/value are not supposed
    try:
        func(1, define=["foo"])
    except ValueError:
        pass
    else:
        assert False

# Generated at 2022-06-14 05:33:23.976154
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def overload_config_test(x):
        return x

    assert overload_config_test(define=["python_module_name=semantic_release"], x="x") == "x"
    assert config["python_module_name"] == "semantic_release"
    assert overload_config_test(x="x") == "x"

# Generated at 2022-06-14 05:33:32.013564
# Unit test for function overload_configuration
def test_overload_configuration():
    import click

    @click.command()
    @click.argument("src", nargs=-1)
    @click.option("--define", "-D", default=['version=1.2.0'], help="Define parameters")
    @overload_configuration
    def test(src, define):
        pass

    result = test(["1", "2", "--define", "key=value"])
    assert result == 0

    result = test(["1", "2", "--define", "key=value"], standalone_mode=False)
    assert result == 0

# Generated at 2022-06-14 05:33:43.927873
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test overload_configuration decorator for a config value
    """

    @overload_configuration
    def test_func(define=list()):
        return config.get("test_func")

    assert test_func() == ""
    assert test_func(define=["test_func=value"]) == "value"

# Generated at 2022-06-14 05:33:48.541802
# Unit test for function current_commit_parser
def test_current_commit_parser():  # pragma: no cover
    """Unit test for function current_commit_parser"""
    import semantic_release.commit_parser

    assert current_commit_parser() == semantic_release.commit_parser.parse

    config["commit_parser"] = "semantic_release.commit_parser.parse"
    assert current_commit_parser() == semantic_release.commit_parser.parse

    config["commit_parser"] = "semantic_release.commit_parser:parse"
    assert current_commit_parser() == semantic_release.commit_parser.parse

# Generated at 2022-06-14 05:33:53.019772
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog.components import breaking_change

    config["changelog_components"] = "semantic_release.changelog.components.breaking_change"
    assert current_changelog_components() == [breaking_change]

    config["changelog_components"] = ""
    assert current_changelog_components() == []

# Generated at 2022-06-14 05:33:54.738283
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert current_changelog_components() == [
        semantic_release.changelog.changelog_components.changes_sections
    ]

# Generated at 2022-06-14 05:33:59.371154
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog import DefaultComponent

    config["changelog_components"] = "semantic_release.changelog.DefaultComponent"
    assert current_changelog_components() == [DefaultComponent]


# Unit tests for function current_changelog_components

# Generated at 2022-06-14 05:34:03.333378
# Unit test for function overload_configuration
def test_overload_configuration():
    def dummy(value, define=None):
        return value

    @overload_configuration
    def overload(value, define=None):
        return value

    assert dummy(1) == overload(1)
    assert dummy(define=["foo=bar"]) == overload(define=["foo=bar"])
    assert config["foo"] == "bar"

# Generated at 2022-06-14 05:34:05.781579
# Unit test for function current_commit_parser
def test_current_commit_parser():
    def parse_commit_message(message):
        return message

    assert current_commit_parser() == parse_commit_message

# Generated at 2022-06-14 05:34:09.504419
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def foo(bar):
        return config["bar"]

    assert foo("foo") == "foo"
    assert foo("foo", define="bar=buzz") == "buzz"

# Generated at 2022-06-14 05:34:19.439305
# Unit test for function overload_configuration
def test_overload_configuration():
    """This test is done by patching the config. The call to
       cli.semantic_release_cli(define=['patch_without_tag=True'])
       should change the config to {'patch_without_tag': 'True'}
    """
    semantic_release_cli = None
    try:
        import semantic_release.cli as cli
        semantic_release_cli = cli.semantic_release_cli
    except ModuleNotFoundError:
        raise ImportError(
            "Impossible to import cli module, please install in develop mode"
        )
    semantic_release_cli(define=["patch_without_tag=True"])
    assert config["patch_without_tag"] == "True"

# Generated at 2022-06-14 05:34:25.300505
# Unit test for function overload_configuration
def test_overload_configuration():
    import semantic_release

    @overload_configuration
    def my_func(param1, param2):
        return {"param1": param1, "param2": param2}

    semantic_release.config["commit_parser"] = "semantic_release.commit_parser.default_parser"
    semantic_release.config["changelog_components"] = "semantic_release.changelog.components.commit_parser,semantic_release.changelog.components.author_email"

    assert my_func("a", "b", define=["commit_parser=semantic_release.commit_parser.custom_parser"]) == {"param1": "a", "param2": "b"}
    assert semantic_release.config["commit_parser"] == "semantic_release.commit_parser.custom_parser"

    assert my

# Generated at 2022-06-14 05:34:38.913972
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from . import changelog
    from . import commit_parser

    components = current_changelog_components()

    assert len(components) == 4
    assert components[0] == changelog.parse_description
    assert components[1] == changelog.parse_body
    assert components[2] == commit_parser.parse_body
    assert components[3] == changelog.generate

# Generated at 2022-06-14 05:34:47.700799
# Unit test for function overload_configuration
def test_overload_configuration():
    config["previous_version"] = "v0"
    config["new_version"] = "v1"

    @overload_configuration
    def test(previous_version=config["previous_version"],
             new_version=config["new_version"]):
        return previous_version, new_version

    assert test() == ("v0", "v1")
    assert test(define=["previous_version=v2"]) == ("v2", "v1")
    assert test() == ("v0", "v1")

# Generated at 2022-06-14 05:34:52.092545
# Unit test for function overload_configuration
def test_overload_configuration():
    # test non-overloaded config
    assert config.get('case_insensitive') == 'true'
    # test overloaded config
    @overload_configuration
    def test_function(define=list()):
        pass
    test_function(define=['case_insensitive=false'])
    assert config.get('case_insensitive') == 'false'

# Generated at 2022-06-14 05:35:02.177687
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test overload_configuration decorator"""

    class FakePlugin:
        """Fake plugin class"""
        @overload_configuration
        def on_parse_arguments(self, **kwargs):
            """Fake function called by overload_configuration function"""
            pass

        @overload_configuration
        def on_test(self, **kwargs):
            pass

    parser = FakePlugin()

    parser.on_test(define=['foo=bar'])
    assert config['foo'] == 'bar'

    parser.on_parse_arguments(define=['foo=bar', 'baz=qux'])
    assert config['foo'] == 'bar'
    assert config['baz'] == 'qux'

    parser.on_parse_arguments(define=['foo=foo', 'baz=qux'])
   

# Generated at 2022-06-14 05:35:12.060998
# Unit test for function overload_configuration
def test_overload_configuration():
    import sys
    module_name = "semantic_release.tests.test_settings"
    my_module = sys.modules[module_name]
    my_module.config_func = overload_configuration(lambda: config.get("foo"))

    # Empty config, so "foo" value is not set
    assert my_module.config_func() is None

    # Set one parameter in config
    assert my_module.config_func(define=["foo=bar"]) == "bar"

    # Overload the previous parameter and set another
    assert config["foo"] == "bar"
    assert my_module.config_func(define=["foo=bar2", "bar=foo"]) == "bar2"
    assert config["bar"] == "foo"

# Generated at 2022-06-14 05:35:23.117648
# Unit test for function overload_configuration
def test_overload_configuration():
    """The configuration should be overloaded with the define parameter"""

    config['test_int'] = 1
    config['test_str'] = "test_str"
    config['test_list'] = ["a", "b"]

    @overload_configuration
    def test(define):
        """this function overload the config from define"""
        return

    # Here is a list of test
    test(define=[
        "test_int=2",
        "test_str=overloaded_str",
        "test_list=['z', 'y']",
    ])

    assert config["test_int"] == 2
    assert config["test_str"] == "overloaded_str"
    assert config["test_list"] == ["z", "y"]

# Generated at 2022-06-14 05:35:34.953047
# Unit test for function overload_configuration

# Generated at 2022-06-14 05:35:46.732380
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def config_utils_config_key(key: str) -> str:
        return config[key]

    assert config_utils_config_key("changelog_components") == (
        "semantic_release.changelog.components.feature_added, "
        "semantic_release.changelog.components.feature_removed, "
        "semantic_release.changelog.components.feature_deprecated, "
        "semantic_release.changelog.components.feature_changed, "
        "semantic_release.changelog.components.feature_security, "
        "semantic_release.changelog.components.feature_fixed, "
        "semantic_release.changelog.components.feature_docs"
    )

    config

# Generated at 2022-06-14 05:35:52.675422
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_key"] = "test_value"

    @overload_configuration
    def test_function():
        assert config["test_key"] == "overload_value"

    test_function(define=["test_key=overload_value"])
    assert config["test_key"] == "overload_value"

# Generated at 2022-06-14 05:36:04.942204
# Unit test for function overload_configuration
def test_overload_configuration():
    def func(param):
        return config[param]

    func = overload_configuration(func)

    # The changes does not persist
    assert func("commit_parser") == "semantic_release.commit_parser.parse"
    assert func("changelog_components") == "semantic_release.changelog.Changes"
    assert func("changelog_components") == "semantic_release.changelog.Changes"
    func(define=["commit_parser=semantic_release.other_commit_parser.parse"])
    assert func("commit_parser") == "semantic_release.other_commit_parser.parse"
    func(define=["changelog_components=semantic_release.other_changelog_components.Changes"])

# Generated at 2022-06-14 05:36:21.027338
# Unit test for function overload_configuration
def test_overload_configuration():
    def dummy_func(param):
        assert param == 1
        assert config[
            "changelog_components"
        ] == "semantic_release.changelog.changelog_components.Breaking,semantic_release.changelog.changelog_components.Feature"

    wrap = overload_configuration(dummy_func)
    wrap(1, define=["changelog_components=semantic_release.changelog.changelog_components.Breaking,semantic_release.changelog.changelog_components.Feature"])

# Generated at 2022-06-14 05:36:23.846660
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import sections, subsections
    assert current_changelog_components() == [sections, subsections]

# Generated at 2022-06-14 05:36:32.465379
# Unit test for function overload_configuration
def test_overload_configuration():

    @overload_configuration
    def test_func(arg1, arg2, arg3=None):
        return arg1, arg2, arg3

    config["test_overload_key"] = "test_overload_value"

    assert test_func("1", "2") == ("1", "2", None)
    assert config["test_overload_key"] == "test_overload_value"

    assert test_func("1", "2", arg3="3") == ("1", "2", "3")
    assert config["test_overload_key"] == "test_overload_value"

    assert test_func("1", "2", define=["test_overload_key=new_value"]) == ("1", "2", None)

# Generated at 2022-06-14 05:36:42.330934
# Unit test for function overload_configuration
def test_overload_configuration():
    from .cli import prepare_default_config

    @overload_configuration
    def test_func(*args, **kwargs):
        return config.get('changelog_components')

    real_components = config.get('changelog_components')
    prepare_default_config()
    config.update({'changelog_components': real_components})
    assert test_func(define=['changelog_components=a.b,c']) == 'a.b,c'

# Generated at 2022-06-14 05:36:46.701480
# Unit test for function overload_configuration
def test_overload_configuration():
    func = lambda x: x
    decorated = overload_configuration(func)
    assert decorated(1, define=['key1=value1', 'key2=value2']) == 1
    assert config['key1'] == 'value1'
    assert config['key2'] == 'value2'