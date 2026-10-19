

# Generated at 2022-06-14 05:26:59.918502
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    This test is a simple example of how the `overload_configuration` decorator
    may be used to get pairs of key/value.
    """

    @overload_configuration
    def my_function(define: List[str]):
        return define

    res = my_function(define=["a=1", "b=2", "c=3"])
    assert res == ["a=1", "b=2", "c=3"]
    assert config["a"] == "1"
    assert config["b"] == "2"
    assert config["c"] == "3"

# Generated at 2022-06-14 05:27:03.799829
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = False
    @overload_configuration
    def test_func():
        if config["test"]:
            return True
        else:
            return False

    assert test_func(define=["test=True"]) == True
    assert test_func() == False

# Generated at 2022-06-14 05:27:04.943763
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser()

# Generated at 2022-06-14 05:27:09.380571
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def run(foo, define=None):
        print(config)
        return foo

    run("one", define=["foo=bar"])
    assert config["foo"] == "bar"
    config.pop("foo")

# Generated at 2022-06-14 05:27:13.515244
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def any_function(hello, define):
        pass

    any_function("Hello", ['hello=world','foo=bar'])
    assert config['hello']=='world'
    assert config['foo']=='bar'

# Generated at 2022-06-14 05:27:19.193155
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def foo(bar=None):
        pass

    foo(bar=1, define=["test_1=test", "test_2=test"])
    assert config["test_1"] == "test"
    assert config["test_2"] == "test"

# Generated at 2022-06-14 05:27:31.410898
# Unit test for function overload_configuration
def test_overload_configuration():
    from .main import setup_args

    # test overload by updating "tag_format"
    args = setup_args(["--define", "tag_format=v{new_version}"])
    assert args.tag_format == "v{new_version}"
    args = setup_args([])
    # test not updated
    assert args.tag_format == "v{new_version}"
    # test overload by updating "tag_format"
    args = setup_args(["--define", "tag_format=v.{new_version}"])
    assert args.tag_format == "v.{new_version}"
    # test no --define argument
    args = setup_args(["--tag-format", "v{new_version}"])
    assert args.tag_format == "v{new_version}"
    args = setup

# Generated at 2022-06-14 05:27:41.211952
# Unit test for function overload_configuration
def test_overload_configuration():
    # I know that it is a bad idea to test this way, but I couldn't find a better
    # way to do it.
    @overload_configuration
    def test_function(name, **kwargs):
        return name

    test_function("test1", define=["first=4"])
    assert config["first"] == "4"
    test_function("test1", define=["second=5"])
    assert config["second"] == "5"
    test_function("test1", define=["first=0"])
    assert config["first"] == "0"

# Generated at 2022-06-14 05:27:50.099528
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test that the decorator works correctly.
    """

    # A dummy function that should be decorated.
    def something_to_test(param1=None, define=None):
        return config

    SOME_KEY = "key"
    SOME_VALUE = "value"
    modified_config = dict()
    modified_config[SOME_KEY] = SOME_VALUE
    res = something_to_test()
    assert res == config
    res = something_to_test(define=[SOME_KEY + "=" + SOME_VALUE])
    assert res != config
    assert res[SOME_KEY] == modified_config[SOME_KEY]

# Generated at 2022-06-14 05:27:56.529506
# Unit test for function overload_configuration
def test_overload_configuration():
    def foo(a,b,c,define=None):
        return ""

    assert overload_configuration(foo)(1,2,3) == ""

    assert overload_configuration(foo)(1,2,3,define=["foo=bar"]) == ""
    assert config["foo"] == "bar"

    assert overload_configuration(foo)(1,2,3,define=[]) == ""

# Generated at 2022-06-14 05:28:12.737440
# Unit test for function overload_configuration
def test_overload_configuration():
    # It's possible to define 2 pairs of key/value
    @overload_configuration
    def f(define):
        return config.get("custom_key_1")

    assert f(define=["custom_key_1=custom_value"]) == "custom_value"
    assert f(define=["custom_key_2=custom_value", "custom_key_1=custom_value"]) == "custom_value"

    # If no pair of key/value is defined, return the default value
    assert f(define=["foo"]) == "__UNSET__"

    # If no pair of key/value is defined, return the default value
    assert f(define=["foo=bar"]) == "__UNSET__"

    # It's possible to pass only the key with no value

# Generated at 2022-06-14 05:28:18.501290
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release import get_changelog_components
    from semantic_release.changelog import default_components

    # Test: default components
    assert current_changelog_components() == default_components

    # Test: different components
    assert current_changelog_components() == get_changelog_components()

# Generated at 2022-06-14 05:28:25.301708
# Unit test for function overload_configuration
def test_overload_configuration():
    config = {}
    config['fake_config'] = 'default'

    def fake_func(first, define={}):
        return config['fake_config']

    decorated_func = overload_configuration(fake_func)
    assert decorated_func(1, define=['fake_config=new']) == 'new'

# Generated at 2022-06-14 05:28:32.877175
# Unit test for function current_commit_parser
def test_current_commit_parser():
    fake_config = {'commit_parser': 'semantic_release.commit_parser.parse'}

    def run_with_config(fake_config):
        return current_commit_parser()

    with_fake_config = wraps(run_with_config)(lambda: None)
    with_fake_config.__dict__['config'] = fake_config

    assert with_fake_config() == parse



# Generated at 2022-06-14 05:28:34.166249
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert callable(current_commit_parser())

# Generated at 2022-06-14 05:28:43.560012
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function checks that the decorator "overload_configuration" works
    as expected, it verifies that the dictionnary "config" is modified or not
    when the decorator is used with an empty array, with one item, with two
    items and with three items.
    """
    # Then we check that the "config" dictionnary is empty
    assert len(config) == 0

    # We define a function that will be decorated
    @overload_configuration
    def f(defined_param=[]):
        return

    # Case of an empty array
    f(define=[])
    assert len(config) == 0

    # Case of one item
    f(define=["key=value"])
    assert len(config) == 1

    # Case of two items

# Generated at 2022-06-14 05:28:46.590610
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def func():
        return config.get("version_variable")

    assert func(define=["version_variable=__version__"]) == "__version__"
    assert config.get("version_variable") == "__version__"



# Generated at 2022-06-14 05:28:54.260825
# Unit test for function overload_configuration
def test_overload_configuration():
    def mock_func(first_arg, second_arg, third_arg, define=None):
        pass

    func_with_mock = overload_configuration(mock_func)

    func_with_mock("arg1", "arg2", "arg3", define=["key1=value1", "key2=value2"])
    assert config.get("key1") == "value1"
    assert config.get("key2") == "value2"

# Generated at 2022-06-14 05:28:58.096361
# Unit test for function current_commit_parser
def test_current_commit_parser():
    import semantic_release.hvcs.git as git
    assert current_commit_parser() == git.parse_commit



# Generated at 2022-06-14 05:29:06.307525
# Unit test for function overload_configuration
def test_overload_configuration():
    global config
    config = UserDict()

    @overload_configuration
    def func(*args, **kwargs):
        return None

    func(define=["a=1", "b=2", "c=3", "d=4"])

    assert config["a"] == "1"
    assert config["b"] == "2"
    assert config["c"] == "3"
    assert config["d"] == "4"

# Generated at 2022-06-14 05:29:28.152788
# Unit test for function overload_configuration
def test_overload_configuration():
    config_copy = config["changelog_components"]

    def test_func(dict, define):
        return

    wrapper = overload_configuration(test_func)

    # Define an existent key to an existing value
    wrapper(
        dict=None,
        define=["changelog_components=semantic_release.changelog:components"],
    )
    assert config["changelog_components"] != config_copy

    # Define an existent key to an unexistent value
    wrapper(dict=None, define=["changelog_components=foo"])
    assert config["changelog_components"] != config_copy

    # Define an unexistent key to an existing value
    wrapper(dict=None, define=["foo=semantic_release.changelog:components"])
   

# Generated at 2022-06-14 05:29:35.976109
# Unit test for function overload_configuration
def test_overload_configuration():
    import semantic_release.hvcs
    import semantic_release.settings
    import semantic_release.versioning
    reload(semantic_release.hvcs)
    reload(semantic_release.settings)
    reload(semantic_release.versioning)
    test_string = "test string"
    assert not(semantic_release.settings.config['hvcs'])
    assert not(semantic_release.settings.config['version_variable'])
    semantic_release.versioning.get_version_from_file(define=["hvcs=" + test_string])
    assert semantic_release.settings.config['hvcs'] == test_string

# Generated at 2022-06-14 05:29:40.745593
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_func(a):
        return a

    decorated = overload_configuration(test_func)
    assert decorated(a=5) == 5
    assert decorated(a=5, define=["foo=bar"]) == 5
    assert config.get("foo") == "bar"

# Generated at 2022-06-14 05:29:48.456317
# Unit test for function overload_configuration
def test_overload_configuration():
    """Tests the proper behavior of the function overload_configuration
    """
    @overload_configuration
    def func_test(a, b, define=None):
        assert b == "test"
        assert config["a"] == "Value_of_define_a"
        assert config["b"] == "test"
        assert config["c"] == "Value_of_define_c"

    func_test("a", "test", define=["a=Value_of_define_a", "b", "c=Value_of_define_c"])



# Generated at 2022-06-14 05:29:50.225612
# Unit test for function overload_configuration
def test_overload_configuration():
    assert "version" not in config

# Generated at 2022-06-14 05:29:54.605042
# Unit test for function current_changelog_components

# Generated at 2022-06-14 05:30:05.388898
# Unit test for function overload_configuration
def test_overload_configuration():

    # All of these calls should overwrite the configuration file.
    overload_configuration(lambda: True)(define=["next_version=1.2.3"])
    assert config["next_version"] == "1.2.3"
    overload_configuration(lambda: True)(define=["tag_name=mytag"])
    assert config["tag_name"] == "mytag"
    overload_configuration(lambda: True)(define=["tag_name=mytag", "next_version=1.2.3"])
    assert config["next_version"] == "1.2.3"
    assert config["tag_name"] == "mytag"

    # These calls should not overwrite the configuration file
    overload_configuration(lambda: True)(define=["toto="])
    assert config["toto"] != ""
    overload_configuration

# Generated at 2022-06-14 05:30:08.334539
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser() == "semantic_release.commit_parser:CommitMessage"


# Generated at 2022-06-14 05:30:13.401630
# Unit test for function overload_configuration
def test_overload_configuration():
    config["verify_conditions"] = ["test1", "test2"]
    new_config = overload_configuration(lambda define: True)(define=["verify_conditions=test3"])
    assert config["verify_conditions"] == "test3"

# Generated at 2022-06-14 05:30:15.336346
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert callable(current_commit_parser())
    config["commit_parser"] = 1
    assert current_commit_parser() == 1
    config["commit_parser"] = None



# Generated at 2022-06-14 05:30:36.712133
# Unit test for function overload_configuration
def test_overload_configuration():
    # Test for command line arguments
    class TestName:
        @overload_configuration
        def __init__(self, define=False):
            pass

    # Test for command line arguments not passed
    class TestNameFail:
        @overload_configuration
        def __init__(self, define=False):
            pass

    # Test for two pairs of arguments (ex: semantic-release -d var=val -d var2=val2)
    class TestNameMulti:
        @overload_configuration
        def __init__(self, define=False):
            pass

    test1 = TestName(define=["name=joe", "age=20"])
    test2 = TestNameFail()

# Generated at 2022-06-14 05:30:43.024876
# Unit test for function overload_configuration
def test_overload_configuration():
    """test_overload_configuration tests the overload of configuration parameters.
    """
    # Augment configuration with a new parameter define=changelog_components=other_component
    assert overload_configuration(lambda x, y, define: y)(0, 1, ["changelog_components=other_components"]) == 1
    assert config["changelog_components"] == "other_components"

# Generated at 2022-06-14 05:30:44.953985
# Unit test for function current_commit_parser
def test_current_commit_parser():
    parser = current_commit_parser()
    assert callable(parser)



# Generated at 2022-06-14 05:30:53.895391
# Unit test for function current_changelog_components
def test_current_changelog_components():
    component_paths = "semantic_release.changelog.component.Features,semantic_release.changelog.component.BugFixes,semantic_release.changelog.component.PerformanceImprovements,semantic_release.changelog.component.BuildProcess,semantic_release.changelog.component.Documentation,semantic_release.changelog.component.Internationalization,semantic_release.changelog.component.GitHub"
    import_changelog_components = current_changelog_components()
    assert len(import_changelog_components) == 7

# Generated at 2022-06-14 05:31:00.124486
# Unit test for function current_changelog_components
def test_current_changelog_components():
    changelog_components = current_changelog_components()
    assert len(changelog_components) > 0
    assert isinstance(changelog_components, list)
    # Assert that all the changelog components are callable
    assert all([callable(component) for component in changelog_components])

# Generated at 2022-06-14 05:31:09.685419
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(foo, bar, define=[]):
        return f'foo={foo}, bar={bar}'

    def test_without_overload():
        assert test_function('a', 'b') == "foo=a, bar=b"

    def test_with_overload():
        assert test_function('a', 'b', define=['foo=overloaded', 'bar=overloaded']) == "foo=overloaded, bar=overloaded"

    test_without_overload()
    test_with_overload()

# Generated at 2022-06-14 05:31:14.955924
# Unit test for function overload_configuration
def test_overload_configuration():
    from . import utils

    def fake(parameter):
        return parameter

    utils.fake_func = fake

    assert utils.fake_func("hi") == "hi"

    @overload_configuration
    def fake_with_define(parameter, define):
        return parameter

    assert fake_with_define("hi") == "hi"
    assert fake_with_define("hi", define=["option=moi"]) == "hi"
    assert config.get("option") == "moi"

# Generated at 2022-06-14 05:31:18.767032
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .settings import current_changelog_components
    from .changelog import format_changelog_entry

    components = current_changelog_components()
    assert format_changelog_entry in components

# Generated at 2022-06-14 05:31:26.440727
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Check if current_changelog_components return the right changelog components"""

# Generated at 2022-06-14 05:31:32.926271
# Unit test for function overload_configuration
def test_overload_configuration():
    test_config = config.copy()
    _config = overload_configuration(lambda *args, **kwargs: None)
    assert config == test_config
    _config(define=["pypi_url=https://fake.pypi.org"])
    assert config["pypi_url"] == "https://fake.pypi.org"
    config.clear()
    config.update(test_config)

# Generated at 2022-06-14 05:31:42.649521
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert type(current_changelog_components()) == list

# Generated at 2022-06-14 05:31:47.264016
# Unit test for function current_changelog_components
def test_current_changelog_components():
    try:
        current_changelog_components()
    except ImproperConfigurationError as e:
        assert str(e) == "Unable to import changelog component 'semantic_release.changelog'"

# Generated at 2022-06-14 05:31:56.315133
# Unit test for function overload_configuration
def test_overload_configuration():
    sample_func = overload_configuration(lambda: None)
    assert sample_func.get("changelog_components") == "semantic_release.changelog.components"
    sample_func(\
        define=["major_on_zero=False", "patch_without_tag=True"])
    assert config["major_on_zero"] == "False"
    assert config["patch_without_tag"] == "True"
    sample_func(\
        define=["major_on_zero=False", "abc=123"])
    assert config["abc"] == "123"

# Generated at 2022-06-14 05:32:05.057803
# Unit test for function overload_configuration
def test_overload_configuration():
    assert config["changelog_components"] == "changelog.components"
    @overload_configuration
    def change_config():
        config["changelog_components"] = "foo.bar"

    change_config(define=[])
    assert config["changelog_components"] == "foo.bar"

    config["changelog_components"] = "changelog.components"
    change_config(define=["changelog_components=foo.baz"])
    assert config["changelog_components"] == "foo.baz"

# Generated at 2022-06-14 05:32:10.464978
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config["changelog_components"] = "semantic_release.changelog_components.parse_header"

    assert current_changelog_components()[0](
        "semantic_release.changelog_components.parse_header"
    )



# Generated at 2022-06-14 05:32:16.563197
# Unit test for function overload_configuration
def test_overload_configuration():
    def foo(name, define=None):
        return name

    foo = overload_configuration(foo)
    assert foo("Pavel") == "Pavel"
    assert foo("Pavel", define=["name=Sergey"]) == "Sergey"
    assert foo("Pavel", define=["name=Sergey", "age=34"]) == "Sergey"

# Generated at 2022-06-14 05:32:22.845012
# Unit test for function overload_configuration
def test_overload_configuration():
    """This is a test for the decorator overload_configuration.
    """

    from semantic_release.cli import bump_type

    @overload_configuration
    def foo(define):
        return define

    assert foo(define=["major"]) == ["major"]
    assert config["bump_type"] == "major"
    assert bump_type() == "major"



# Generated at 2022-06-14 05:32:34.315337
# Unit test for function overload_configuration
def test_overload_configuration():
    global config
    config = {
        "define": [],
        "foo": "bar",
        "name": "semantic_release",
        "url": "https://github.com/relekang/semantic-release",
    }

    @overload_configuration
    def foo(define: list):
        return config

    config_one = foo(define=["foo=new_bar", "name=new_name"])
    assert config_one["foo"] == "new_bar"
    assert config_one["name"] == "new_name"
    assert config_one["url"] == "https://github.com/relekang/semantic-release"

    config_two = foo(define=["foo_bar=new_foo_bar"])

# Generated at 2022-06-14 05:32:36.407318
# Unit test for function overload_configuration
def test_overload_configuration():
    config.update({"test_key": "value"})

    @overload_configuration
    def foo(define):
        pass

    foo(define=["test_key=new_value"])
    assert config["test_key"] == "new_value"

# Generated at 2022-06-14 05:32:44.123715
# Unit test for function overload_configuration
def test_overload_configuration():
    assert "define" not in config.keys()
    assert config.get("define") is None

    @overload_configuration
    def test_function(param1, _define=list()):
        _define = ["define=value"]
        return param1, _define

    result = test_function("hello")
    assert result == ("hello", ["define=value"])
    assert "define" in config
    assert config["define"] == "value"

# Generated at 2022-06-14 05:32:57.342909
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(*args, **kwargs):
        return True

    assert test_function()
    assert config.get("next_version") == "2.0.0"
    assert config.get("major_version_zero_name") == "major"

# Generated at 2022-06-14 05:33:08.106154
# Unit test for function overload_configuration
def test_overload_configuration():
    # default_config:
    #   tested_var: default
    #   other_var: other_default

    # Given
    config = {"tested_var": "default", "other_var": "other_default"}

    # When
    @overload_configuration
    def fake_function(define=None):
        return config

    # Then
    assert fake_function(define=["tested_var=new_value", "other_var=new_other_value"]) == {
        "tested_var": "new_value",
        "other_var": "new_other_value",
    }



# Generated at 2022-06-14 05:33:08.922026
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser()


# Generated at 2022-06-14 05:33:11.317305
# Unit test for function current_commit_parser
def test_current_commit_parser():
    config["commit_parser"] = "semantic_release.commit_parser:CommitParser"
    assert current_commit_parser() is not None



# Generated at 2022-06-14 05:33:15.275950
# Unit test for function overload_configuration
def test_overload_configuration():
    message = "Hello World"

    @overload_configuration
    def do_something(msg):
        return msg

    assert do_something(msg=message) == message
    assert do_something(msg=message, define=["message=Goodbye World"]) == "Goodbye World"

# Generated at 2022-06-14 05:33:19.401972
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from semantic_release.commit_parser import default_commit_parser

    assert config["commit_parser"] == "semantic_release.commit_parser:default_commit_parser"
    assert current_commit_parser() == default_commit_parser

# Generated at 2022-06-14 05:33:29.870007
# Unit test for function overload_configuration
def test_overload_configuration():
    config.clear()
    config["foo"] = "bar"
    config["bar"] = "baz"

    @overload_configuration
    def test_function(foo):
        assert foo == "bar"

    test_function(foo="foo", define=["foo=bar"])

# Generated at 2022-06-14 05:33:35.616266
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Test the function current_changelog_components."""
    # Overload the get to force the configuration
    config.get = lambda x: "semantic_release.changelog_config.get_current_changelog"
    assert callable(current_changelog_components()[0])

# Generated at 2022-06-14 05:33:37.143563
# Unit test for function current_commit_parser
def test_current_commit_parser():
    expected = "semantic_release.commit_parser:CommitMessage"
    assert expected == config.get("commit_parser")

# Generated at 2022-06-14 05:33:47.479921
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Unit test for function current_changelog_components."""
    def dummy_parser():
        """Dummy function."""
        return


# Generated at 2022-06-14 05:34:01.395007
# Unit test for function overload_configuration
def test_overload_configuration():
    # Initialize

    @overload_configuration
    def mock_func(a, b):
        return a, b

    def mock_func_orig(a, b):
        return a, b

    # Test
    assert mock_func(1, 2, define=["a=3"]) is not mock_func_orig(1, 2)

# Generated at 2022-06-14 05:34:14.737438
# Unit test for function overload_configuration
def test_overload_configuration():
    from .cli import get_config
    from .cli import get_parser

    # Define the config variable in the function get_config
    # but the variable is protected by the decorator
    # so we need to hack it to define it directly
    get_config.config = {}
    get_parser(["--help"])
    assert get_config.config == config

    # Test the config variable is replace by the defined one
    get_config.config = {}
    get_parser(["--help", "--define=set_by_test=test_value"])
    assert get_config.config["set_by_test"] == "test_value"

    # Test the config variable is replace by the defined one
    # in a wrong way
    get_config.config = {}

# Generated at 2022-06-14 05:34:21.238877
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(define: str = None, other: str = None):
        return config.get("test", "")

    assert config.get("test") is None

    # Define a missing key/value pair
    test_function(define="test")
    assert config.get("test") is None

    # Define an existing key
    test_function(define="test=value")
    assert config.get("test") == "value"

# Generated at 2022-06-14 05:34:31.229553
# Unit test for function overload_configuration
def test_overload_configuration():
    # Arrange
    import copy
    import semantic_release
    func = copy.deepcopy(semantic_release.config)
    semantic_release.config["changelog_components"] = "default"
    semantic_release.config["python_components"] = "default"

    # Act
    decorated_func = overload_configuration(func)
    decorated_func(define=["changelog_components=new_component1", "python_components=new_component2"])

    # Assert
    assert semantic_release.config["changelog_components"] == "new_component1"
    assert semantic_release.config["python_components"] == "new_component2"

# Generated at 2022-06-14 05:34:38.482381
# Unit test for function overload_configuration
def test_overload_configuration():
    expected_config = config.copy()
    expected_config["test_key"] = "test_value"
    expected_config["test_key2"] = "test_value2"

    @overload_configuration
    def dummy(define):
        return None

    dummy(define=["test_key=test_value"])
    assert config["test_key"] == "test_value"

    dummy(define=["test_key=test_value", "test_key2=test_value2"])
    assert config["test_key"] == "test_value"
    assert config["test_key2"] == "test_value2"

    config.clear()
    config.update(expected_config)

# Generated at 2022-06-14 05:34:40.267432
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert len(current_changelog_components()) >= 4

# Generated at 2022-06-14 05:34:51.874323
# Unit test for function overload_configuration
def test_overload_configuration():
    def foo(test, define=None):
        return test

    overloaded_func = overload_configuration(foo)

    # test: no overload
    assert overloaded_func("test") == "test"

    # test: overload a key/value
    overloaded_func(test="test2", define=["key=value"])
    assert config["key"] == "value"

    # test: overload a list of key/value
    overloaded_func(test="test3", define=["key2=value2", "key3=value3"])
    assert config["key2"] == "value2"
    assert config["key3"] == "value3"

    # test: overload an incomplete list of key/value
    overloaded_func(test="test4", define=["key4", "key5=value5"])
    assert config["key4"]

# Generated at 2022-06-14 05:35:01.999071
# Unit test for function overload_configuration
def test_overload_configuration():
    config_overloaded = config.copy()

    @overload_configuration
    def test_func(**kwargs):
        return config["release_commit_message"]

    config["release_commit_message"] = "overloaded"
    assert test_func() == "overloaded"

    assert test_func(define=["release_commit_message=release %s"]) == "release %s"
    assert config["release_commit_message"] == "release %s"

    @overload_configuration
    def test_func_wrong_syntax_1(**kwargs):
        return config["release_commit_message"]

    @overload_configuration
    def test_func_wrong_syntax_2(**kwargs):
        return config["release_commit_message"]


# Generated at 2022-06-14 05:35:08.155178
# Unit test for function overload_configuration
def test_overload_configuration():
    """Unit test for the overload_configuration decorator,
    check that the configuration has been updated.
    """

    def test_overload(define):
        assert define == "key=value"
        assert config['key'] == "value"

    assert config.get("key") is None
    test_overload(define='key=value')
    assert config['key'] == "value"

# Generated at 2022-06-14 05:35:13.782122
# Unit test for function overload_configuration
def test_overload_configuration():
    newconfig = config.copy()
    newconfig["foo"] = "bar"

    @overload_configuration
    def test_config_overload(define):
        return config

    assert test_config_overload(define=["foo=bar"]) == newconfig

# Generated at 2022-06-14 05:35:31.173461
# Unit test for function current_changelog_components
def test_current_changelog_components():

    # First we check that the function raise no error when everything is alright
    config.get = lambda key: "example_package.example_module.example_function"
    assert callable(current_changelog_components()[0]), "The function is not callable"

    # Then we check that the function raise an error when there are an error in the
    # configuration
    config.get = lambda key: "example_package.example_module.example_function,example_package.example_module.example_function2"
    try:
        current_changelog_components()
    except ImproperConfigurationError:
        assert True

# Generated at 2022-06-14 05:35:36.634766
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_function(a, b, test_value, define=None):
        config["test_value"] = test_value

    decorated = overload_configuration(test_function)
    decorated(1, 2, 3, define=["test_value=new_value"])
    assert config["test_value"] == "new_value"



# Generated at 2022-06-14 05:35:47.477129
# Unit test for function overload_configuration
def test_overload_configuration():
    """Tests 3 cases:
    1) One value of the "define" parameter
    2) Several values of the "define" parameter
    3) No value of the "define" parameter
    """

    @overload_configuration
    def test1(a, define=None):
        config["test1"] = a
        return config

    assert config["test1"] == "1"
    assert config["changelog_components"] == "changelog.component1"
    assert config["commit_parser"] == "parser.component1"

    @overload_configuration
    def test2(b, define=None):
        config["test2"] = b
        return config

    assert config["test2"] == "2"
    assert config["commit_parser"] == "parser.component2"

# Generated at 2022-06-14 05:35:51.214292
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """Test function current_commit_parser.

    :return: test result
    """
    from semantic_release.history.default_parser import parse

    assert parse == current_commit_parser()



# Generated at 2022-06-14 05:35:58.814790
# Unit test for function overload_configuration
def test_overload_configuration():

    @overload_configuration
    def foo(define):
        return define

    define = ["foo=bar", "hello=world"]
    assert foo(define=["foo=bar", "hello=world"]) == define

    assert config["foo"] == "bar"
    assert config["hello"] == "world"

    foo(define=["baz=qux", "spam=eggs"])
    assert config["baz"] == "qux"
    assert config["spam"] == "eggs"

# Generated at 2022-06-14 05:35:59.460207
# Unit test for function overload_configuration
def test_overload_configuration():
    pass

# Generated at 2022-06-14 05:36:13.465787
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function tests if the overload_configuration function is doing its job
    """
    global config

    # we need to define func as a "mock" of the real function to test
    def func(config_value):
        return config_value

    @overload_configuration
    def test_func(config_value):
        return func(config_value)

    # temporarily empty the config global
    config = {}

    # testing default return
    assert test_func("config_value") == "config_value"

    # testing return after "overloading"
    assert test_func("config_value", define=["config_value=overloaded"]) == "overloaded"

    # testing multiple return after "overloading"

# Generated at 2022-06-14 05:36:20.048383
# Unit test for function overload_configuration
def test_overload_configuration():
    from semantic_release.cli import main

    @overload_configuration
    def sample():
        return config.get("commit_message_format")

    sample()
    assert config.get("commit_message_format") == "Conventional Commit"
    main(["release", "--define", "commit_message_format=Simple"])
    assert config.get("commit_message_format") == "Simple"
    sample()
    assert config.get("commit_message_format") == "Simple"

# Generated at 2022-06-14 05:36:21.930814
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert callable(current_changelog_components()[0])

# Generated at 2022-06-14 05:36:27.813671
# Unit test for function current_changelog_components
def test_current_changelog_components():
    components = current_changelog_components()
    assert len(components) == 3
    assert components[0].__name__ == "parse_issue_numbers"
    assert components[1].__name__ == "parse_commit_urls"
    assert components[2].__name__ == "parse_merge_commits"

# Generated at 2022-06-14 05:36:42.051924
# Unit test for function overload_configuration
def test_overload_configuration():
    assert config['commit_parser'] == 'semantic_release.commit_parser.parse'
    @overload_configuration
    def test_function(define):
        pass
    test_function(define="commit_parser=test_parser")
    assert config['commit_parser'] == 'test_parser'