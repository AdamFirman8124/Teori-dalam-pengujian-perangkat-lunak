

# Generated at 2022-06-14 05:26:57.489642
# Unit test for function current_changelog_components
def test_current_changelog_components():
    os.environ["SEMANTIC_RELEASE_CHANGELOG_COMPONENTS"] = "semantic_release.changelog.components.ChangelogEntry,semantic_release.changelog.components.Commit,semantic_release.changelog.components.Author"
    assert len(current_changelog_components()) == 3


# Generated at 2022-06-14 05:27:07.713083
# Unit test for function overload_configuration
def test_overload_configuration():

    # Test if the original configuration is not altered by the decorator
    ORIG_CONFIG = {
        "upload_to_pypi": False,
        "upload_to_release": False,
        "remove_dist": False,
        "major_on_zero": False,
        "check_build_status": False,
        "changelog_capitalize": False,
        "changelog_scope": False,
        "commit_version_number": False,
        "patch_without_tag": False,
        "changelog_components": "semantic_release.changelog.components.scope,semantic_release.changelog.components.breaking_change",
        "commit_parser": "semantic_release.commit_parser.setuptools_parser.parse",
    }

# Generated at 2022-06-14 05:27:12.263937
# Unit test for function overload_configuration
def test_overload_configuration():
    assert overload_configuration(lambda x: (x,))(1, define=["foo=bar", "abc=def"]) == (1,)
    assert config.get('foo') == 'bar'
    assert config.get('abc') == 'def'

# Generated at 2022-06-14 05:27:15.022206
# Unit test for function current_commit_parser
def test_current_commit_parser():
    current_commit_parser()



# Generated at 2022-06-14 05:27:19.650490
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_function(value):
        return value

    config["a"] = "a"
    decorated_function = overload_configuration(test_function)
    assert decorated_function(define=["a=b"]) == "b"
    assert config["a"] == "b"

# Generated at 2022-06-14 05:27:29.499788
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    This test overloads the "config" dictionary using
    the decorator overload_configuration
    """
    @overload_configuration
    def test_func(a, b, c, e, g, define):
        pass

    test_func(1, 2, 3, e="ee", g="gg", define=["a=a", "b=2"])

    assert config['a'] == 'a'
    assert config['b'] == '2'
    assert 'c' not in config
    assert config['e'] == 'ee'
    assert config['g'] == 'gg'

# Generated at 2022-06-14 05:27:40.712866
# Unit test for function overload_configuration
def test_overload_configuration():
    class FakeConfig:
        def __init__(self, conf):
            self.conf = conf

        def set(self, key, value):
            self.conf[key] = value

    @overload_configuration
    def fake_test(arg1, arg2, define=None):
        pass

    fake_conf = FakeConfig({})

    fake_test(1, 2, define=None)
    assert fake_conf.conf == {}

    fake_test(3, 4, define=["a=1"])
    assert fake_conf.conf == {"a": "1"}

    fake_test(5, 6, define=["a=2", "b=2"])
    assert fake_conf.conf == {"a": "2", "b": "2"}


# Generated at 2022-06-14 05:27:43.438947
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog_components import title_capitalize
    assert current_changelog_components() == [title_capitalize]

# Generated at 2022-06-14 05:27:50.949480
# Unit test for function overload_configuration
def test_overload_configuration():
    import pytest

    @overload_configuration
    def test(param1, param2, define=None):
        return param1, param2, config.get("param3")

    param1, param2, param3 = test("value1", "value2", define=["param3=value3"])
    assert param1 == "value1"
    assert param2 == "value2"
    assert param3 == "value3"

    with pytest.raises(configparser.NoOptionError):
        test("value1", "value2")

# Generated at 2022-06-14 05:27:53.944979
# Unit test for function current_changelog_components
def test_current_changelog_components():
    components = current_changelog_components()
    assert len(components) >= 1
    assert callable(components[0])

# Generated at 2022-06-14 05:28:07.588239
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from tests.dummy_parser.parser import parse

    from semantic_release.errors import ImproperConfigurationError
    from semantic_release.config import current_commit_parser, config
    
    # Successful import
    config['commit_parser'] = 'tests.dummy_parser.parser.parse'
    assert current_commit_parser() == parse

    # ImportError / AttributeError
    config['commit_parser'] = 'tests.dummy_parser.parser'
    with pytest.raises(ImproperConfigurationError):
        current_commit_parser()
    
    # Exception
    config['commit_parser'] = 'tests.dummy_parser.parser.parse2'
    with pytest.raises(ImproperConfigurationError):
        current_commit_parser()

# Generated at 2022-06-14 05:28:14.682645
# Unit test for function overload_configuration
def test_overload_configuration():
    config['initial_version'] = 2

    @overload_configuration
    def get_initial_version():
        return config['initial_version']

    assert get_initial_version() == 2
    assert get_initial_version(define=['initial_version=3']) == 3
    assert get_initial_version(define=['initial_version=1']) == 1

# Generated at 2022-06-14 05:28:23.625595
# Unit test for function overload_configuration
def test_overload_configuration():
    """
    Test function overload_configuration.
    """
    config.clear()
    config["version"] = "3.14"

    @overload_configuration
    def dummy(my_config=False):
        if my_config:
            return config

    result = dummy()
    assert result is None
    assert config["version"] == "3.14"

    result = dummy(True)
    assert config["version"] == "3.14"
    assert result["version"] == "3.14"

    result = dummy(define=["version=2.72"])
    assert config["version"] == "2.72"

# Generated at 2022-06-14 05:28:32.618525
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test of the function overload_configuration"""
    @overload_configuration
    def add(a: int, b: int, define: list=None) -> int:
        return a+b
    a = 1
    b = 2
    c = 3
    define = ["a="+str(c), "b="+str(a), "b="+str(b)]
    assert add(1, 1, define) == 4
    assert add(1, 1) == 2
    return True

# Generated at 2022-06-14 05:28:34.423326
# Unit test for function current_commit_parser
def test_current_commit_parser():
    parser = current_commit_parser()
    assert parser.__name__ == "parse"

# Generated at 2022-06-14 05:28:38.732227
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "1"

    def fake_func(*, define):
        pass

    fake_func = overload_configuration(fake_func)
    fake_func(define=("test=2",))

    assert config["test"] == "2"

# Generated at 2022-06-14 05:28:45.958338
# Unit test for function overload_configuration
def test_overload_configuration():
    """This function tests that the overload_configuration decorator
    set the config content according to the define parameter.
    """

    global config
    config = _config()

    @overload_configuration
    def func_to_overload(define=tuple(), **kwargs):
        return config

    assert len(config) > 0
    new_config = func_to_overload(define=("check_build_status=false",))
    assert new_config["check_build_status"] == "false"
    assert len(config) > len(new_config)

# Generated at 2022-06-14 05:28:57.217514
# Unit test for function overload_configuration
def test_overload_configuration():
    from semantic_release.settings import config

    assert config.get("major_on_zero") == False
    assert config.get("commit_parser") == "semantic_release.commit_parser.parse_message"

    @overload_configuration
    def test_func():
        pass

    # Test for boolean
    test_func(define=["major_on_zero=true"])
    assert config.get("major_on_zero") == True

    # Test for arbitrary string
    test_func(define=["commit_parser=semantic_release.commit_parser.parse_message_alternative"])
    assert config.get("commit_parser") == "semantic_release.commit_parser.parse_message_alternative"


# Generated at 2022-06-14 05:28:59.034387
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser()()[1] == {"msg": "feat: New feature"}


# Generated at 2022-06-14 05:29:05.213162
# Unit test for function overload_configuration
def test_overload_configuration():
    def test(**kwargs):
        return config.get("version_variable_name") == "version"

    config["version_variable_name"] = "version"
    assert test(define=["version_variable_name=variable"])

    config["version_variable_name"] = "version"
    assert test()

# Generated at 2022-06-14 05:29:21.032419
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_function(*args, **kwargs):
        return kwargs

    decorated = overload_configuration(test_function)
    assert decorated("a") == dict()
    assert decorated("a", "b") == dict()
    assert decorated("a", "b", define=["c=d"]) == {"define": ["c=d"]}
    assert decorated("a", "b", define=["c=d", "e=f"]) == {"define": ["c=d", "e=f"]}

    decorated("a", "b", define=["c=d"])
    assert config["c"] == "d"

# Generated at 2022-06-14 05:29:25.793048
# Unit test for function current_commit_parser
def test_current_commit_parser():
    try:
        assert os.environ["TEST_CONFIG_PARSER"] != ""
        assert config.get("commit_parser") != ""
        current_commit_parser()
    except ImproperConfigurationError:
        raise ImproperConfigurationError
    except Exception as e:
        raise e



# Generated at 2022-06-14 05:29:31.390789
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def dummy(foo, bar):
        assert foo == "baz"
        assert bar == "qux"

    # With keyword arguments
    dummy(foo="baz", define=["bar=qux"])
    # With positional arguments
    dummy("baz", define=["bar=qux"])

# Generated at 2022-06-14 05:29:33.137221
# Unit test for function overload_configuration
def test_overload_configuration():
    assert callable(overload_configuration)
    assert callable(overload_configuration(lambda: None))

# Generated at 2022-06-14 05:29:39.056068
# Unit test for function overload_configuration
def test_overload_configuration():
    config["dummy"] = "old_value"

    @overload_configuration
    def test_func(define):
        pass

    test_func(define=["dummy=new_value"])
    assert config["dummy"] == "new_value"

# Generated at 2022-06-14 05:29:43.682056
# Unit test for function overload_configuration
def test_overload_configuration():
    conf = config.copy()

    @overload_configuration
    def edit_config(**kwargs):
        return

    edit_config(define=["test=test"])
    assert config["test"] == "test"
    config.clear()
    config.update(conf)

# Generated at 2022-06-14 05:29:46.537627
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test(define=None):
        pass
    test(define=["foo=bar"])
    assert config["foo"] == "bar"

# Generated at 2022-06-14 05:29:56.604043
# Unit test for function overload_configuration
def test_overload_configuration():
    from .context import get_commit_parser, get_changelog_components

    config["commit_parser"] = "test.test"
    config["changelog_components"] = "test.test"

    @overload_configuration
    def get_commit_parser_test():
        return get_commit_parser()

    @overload_configuration
    def get_changelog_components_test():
        return get_changelog_components()

    # change the value of the "commit_parser" config item
    get_commit_parser_test(define=["commit_parser=semantic_release.commit_parser:default"])
    assert (
        config["commit_parser"]
        == "semantic_release.commit_parser:default"
    ), "fail to change commit_parser config value"

    #

# Generated at 2022-06-14 05:30:02.355018
# Unit test for function overload_configuration
def test_overload_configuration():
    config_store = config.copy()
    config["user.name"] = "John Doe"
    assert config_store != config
    @overload_configuration
    def func(define=None):
        return config

    config["user.name"] = func(define=["user.name=Jane Doe"])
    assert config_store == config

# Generated at 2022-06-14 05:30:07.886226
# Unit test for function overload_configuration
def test_overload_configuration():
    global config
    config["commit_parser"] = "semantic_release.commit_parser.parse_commit"

    @overload_configuration
    def test_function(**kwargs):
        return config["commit_parser"]

    assert (
        test_function(define=["commit_parser=semantic_release._semantic_release.overload_configuration"])
        == "semantic_release._semantic_release.overload_configuration"
    )

# Generated at 2022-06-14 05:30:19.278333
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def my_function(define=[]):
        return config

    current_config = config.copy()
    current_config["key"] = "value"
    assert my_function(define=["key=value"]) == current_config

# Generated at 2022-06-14 05:30:21.620609
# Unit test for function current_commit_parser
def test_current_commit_parser():
    from semantic_release.commit_parser import parse_commits

    assert parse_commits.__name__ == current_commit_parser().__name__

# Generated at 2022-06-14 05:30:32.357892
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_func(arg1, arg2, define=None):
        assert config.get("arg1") == "val1"
        assert config.get("arg2") == "val2"
        assert arg1 == "value_for_arg1"
        assert arg2 == "value_for_arg2"

    wrapped_func = overload_configuration(test_func)
    wrapped_func("value_for_arg1", "value_for_arg2", define=["arg1=val1", "arg2=val2"])


# Unit tests for function current_commit_parser

# Generated at 2022-06-14 05:30:40.897568
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changes import changelog_components
    from .utils import _capitalize_scope
    from .utils import _scope_changes
    from .utils import _format_scope_changes
    from .utils import _format_scope_with_mappings

    # A command line which should generate a result  changelog components
    # close to the default one
    components = current_changelog_components()
    assert components == [
        _capitalize_scope,
        _scope_changes,
        _format_scope_changes,
        _format_scope_with_mappings,
    ]

# Generated at 2022-06-14 05:30:47.176783
# Unit test for function overload_configuration
def test_overload_configuration():
    """overload_configuration should update config according to arguments"""
    @overload_configuration
    def dummy(message):
        """This function is only a dummy, in order to be decorated"""
        message = "dummy_" + str(config.get("message"))
        return message

    assert dummy(message="hello") == "dummy_hello"
    assert dummy(message="hello", define=["message=world"]) == "dummy_world"
    assert dummy(message="hello", define=["message=world", "foo=bar"]) == "dummy_world"

# Generated at 2022-06-14 05:30:53.461131
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def func(a, b, c=None, d=None):
        if c is None:
            c = d
        return a + b + c

    assert func(1, 2, define="d=2") == 5
    assert func(1, 2, d=3, define="d=2") == 6


# Unit tests for the config_from_* functions

# Generated at 2022-06-14 05:30:56.391483
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "not_overloaded"

    @overload_configuration
    def test_fun(define):
        return config["test"]

    assert test_fun(define=["test=overloaded"]) == "overloaded"

# Generated at 2022-06-14 05:31:05.922331
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test(**kwargs):
        return kwargs

    assert "changelog_components" in test(define=("changelog_components=foo,bar"))["define"]
    assert "changelog_components" not in test(define=("changelog_components=foo,bar"))
    assert "define" in test(define=("changelog_components=foo,bar"))
    assert "define" not in test(define=("changelog_components=foo,bar"))["define"]

# Generated at 2022-06-14 05:31:15.262713
# Unit test for function overload_configuration
def test_overload_configuration():
    """This unit test checks whether the content of the "define" array is
    correctly edited.
    """

    # Defining the configuration of the test.
    configuration = config
    configuration["base_path"] = "base_path"
    configuration["upload_to_pypi"] = True
    configuration["upload_to_release"] = False
    configuration["changelog_components"] = "valid_components,invalid_components"
    configuration["major_on_zero"] = True
    configuration["dry_run"] = False

    # Defining the tests.

# Generated at 2022-06-14 05:31:22.573623
# Unit test for function overload_configuration
def test_overload_configuration():
    global config
    config["test_parameter"] = "old_value"

    @overload_configuration
    def test_function(test_parameter):
        assert test_parameter == config.get("test_parameter")

    test_function(test_parameter="old_value")
    test_function(test_parameter="old_value", define=["test_parameter=new_value"])

# Generated at 2022-06-14 05:31:31.847489
# Unit test for function current_commit_parser
def test_current_commit_parser():
    current_commit_parser()

# Generated at 2022-06-14 05:31:35.157042
# Unit test for function current_changelog_components
def test_current_changelog_components():
    """Test if current_changelog_components returns the expected components."""
    assert current_changelog_components() == [
        semantic_release.changelog.components.body
    ]

# Generated at 2022-06-14 05:31:46.661104
# Unit test for function overload_configuration
def test_overload_configuration():
    def foo(a, b):
        return a

    @overload_configuration
    def bar(a, b):
        return a

    foo(1, 2)
    assert not hasattr(foo, "define")

    bar(1, 2)
    assert hasattr(bar, "define")

    assert foo(1, 2) == bar(1, 2)

    bar(b=3, a=2, define=["a=1"])
    assert not hasattr(func, "define")
    assert foo(1, 3) == bar(1, 3)

    func(1, 2)
    assert not hasattr(foo, "define")

    bar(1, 2)
    assert hasattr(bar, "define")

    assert foo(1, 2) == bar(1, 2)


# Generated at 2022-06-14 05:31:52.286840
# Unit test for function overload_configuration
def test_overload_configuration():
    class Example:
        @overload_configuration
        def defined_function(define=None):
            if "test_key" in config:
                return True
            else:
                return False

    example = Example()
    param_list=["test_key=test_value"]
    assert example.defined_function(define=param_list)

# Generated at 2022-06-14 05:32:03.961798
# Unit test for function overload_configuration
def test_overload_configuration():
    from .__main__ import parse_args

    # We need to reset the load_configuration() function because otherwise
    # the config will be read from the setup.cfg file.
    from . import load_configuration

    from unittest.mock import Mock

    load_configuration = Mock(return_value=config)

    # Configure the parser with the decorator
    parse_args = overload_configuration(parse_args)

    # In the default configuration, there are no server and token defined
    assert config.get("server", None) is None
    assert config.get("token", None) is None

    # We define a new server and token
    args = parse_args(["release", "--define", "server=http://test.com", "--define", "token=1234"])

    # Now, we should have the new server

# Generated at 2022-06-14 05:32:10.096036
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert config.get("changelog_components") == (
        "semantic_release.changelog.components.changelog_items"
    )

    changelog_components = current_changelog_components()
    assert len(changelog_components) == 1

# Generated at 2022-06-14 05:32:20.527162
# Unit test for function overload_configuration
def test_overload_configuration():
    flags = {
        "changelog_capitalize",
        "changelog_scope",
        "check_build_status",
        "commit_version_number",
        "patch_without_tag",
        "major_on_zero",
        "remove_dist",
        "upload_to_pypi",
        "upload_to_release",
    }


    # testing boolean values
    for flag in flags:
        config[flag] = False
    @overload_configuration
    def ack_func(*args, **kwargs):
        pass
    for flag in flags:
        kwargs = dict()
        kwargs["define"] = [flag + "=true"]
        ack_func(**kwargs)
        assert config[flag] is True
        config[flag] = False

# Generated at 2022-06-14 05:32:32.437417
# Unit test for function overload_configuration
def test_overload_configuration():
    config = _config()

    @overload_configuration
    def add_to_config(config, k, v):
        config[k] = v

    @overload_configuration
    def add_to_config_with_define(config, k, v, define=None):
        config[k] = v

    add_to_config(config, "debug", True)
    add_to_config(config, "remove_dist", False)
    add_to_config_with_define(config, "remove_dist", True, define=["debug=False"])

    assert config["debug"] == True
    assert config.getboolean("debug") == True

    assert config["remove_dist"] == False
    assert config.getboolean("remove_dist") == False


# Generated at 2022-06-14 05:32:34.186299
# Unit test for function current_changelog_components
def test_current_changelog_components():
    return current_changelog_components()

# Generated at 2022-06-14 05:32:42.202459
# Unit test for function overload_configuration
def test_overload_configuration():
    config.clear()
    config.update({
        'key1': 'value1',
        'key2': True,
        'key3': 'value3'
    })

    @overload_configuration
    def foo(define):
        pass

    @overload_configuration
    def bar(define, **kwargs):
        pass

    foo(define=["define3=value6", "define4=value7"])
    assert config['key1'] == 'value1'
    assert config['key2'] is True
    assert config['key3'] == 'value3'
    assert config['define3'] == 'value6'
    assert config['define4'] == 'value7'

    del config['define3']
    del config['define4']


# Generated at 2022-06-14 05:32:57.197634
# Unit test for function overload_configuration
def test_overload_configuration():
    """Test for the overload_configuration decorator"""
    # First test
    @overload_configuration
    def test(define):
        """Functions that are only used to test the decorator"""
        return define

    assert test(define=["base_version=3"]) == ["base_version=3"]

    # Second test
    @overload_configuration
    def test(define):
        """Functions that are only used to test the decorator"""
        return config.get("base_version")

    assert test(define=["base_version=3"]) == "3"

# Generated at 2022-06-14 05:33:05.797254
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test"] = "test_value"

    @overload_configuration
    def check_config_value(**kwargs):
        assert config["test"] == "test_value"

    check_config_value()

    @overload_configuration
    def check_config_value_overloaded(**kwargs):
        assert config["test"] == "new_value"

    check_config_value_overloaded(define=["test=new_value"])

# Generated at 2022-06-14 05:33:13.862257
# Unit test for function overload_configuration
def test_overload_configuration():
    def foo(a=1, b=2, c=3, **options):
        for key in ("a", "b", "c"):
            options[key] = locals()[key]
        return options

    # The configuration of a and b are overwritten
    # by the definition in the CLI
    res = foo(1, 2, 3, define=["a=4", "b=5"])
    assert res == {
        "a": 4,
        "b": 5,
        "c": 3,
        "define": ["a=4", "b=5"]
    }

# Generated at 2022-06-14 05:33:24.897894
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_overload_configuration"] = "test"
    @overload_configuration
    def test1(define):
        assert config["test_overload_configuration"] == "test"
    test1(define=["test_overload_configuration=test1"])
    assert config["test_overload_configuration"] == "test1"
    @overload_configuration
    def test2(define):
        assert config["test_overload_configuration"] == "test1"
    test2(define=["test_overload_configuration=test2"])
    assert config["test_overload_configuration"] == "test2"

# Generated at 2022-06-14 05:33:32.112008
# Unit test for function overload_configuration
def test_overload_configuration():
    config["test_overload"] = "foo"

    @overload_configuration
    def test_overload():
        return config["test_overload"]

    assert test_overload() == "foo"
    assert test_overload(define=["test_overload=bar"]) == "bar"
    assert test_overload(define=["test_overload=bar"], not_defined="baz") == "bar"

# Generated at 2022-06-14 05:33:44.622122
# Unit test for function current_changelog_components
def test_current_changelog_components():
    # Tests valid component list
    config["changelog_components"] = "tests.test_config.test_changelog_component_1, " \
        + "tests.test_config.test_changelog_component_2"
    components = current_changelog_components()
    assert len(components) == 2
    assert callable(components[0])
    assert callable(components[1])
    # Tests invalid component list
    config["changelog_components"] = "tests.test_config.missing_changelog_component_1, " \
        + "tests.test_config.missing_changelog_component_2"
    with pytest.raises(ImproperConfigurationError):
        current_changelog_components()

# Generated at 2022-06-14 05:33:50.345187
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def some_function(a, b, c):
        return a, b, c

    # Test that the parameters are not changed if there is no "define"
    assert some_function(1, 2, 3) == (1, 2, 3)

    # Test if the parameters are changed according to the define array
    # The define array is a list of "key=value" strings
    assert some_function(1, 2, 3, define=["a=4", "b=5", "c=6"]) == (4, 5, 6)

    # Test if the overload works only for the first value of the "define" array
    assert some_function(1, 2, 3, define=["a=4", "b=5", "c=6", "a=7"]) == (4, 5, 6)



# Generated at 2022-06-14 05:34:00.152235
# Unit test for function overload_configuration
def test_overload_configuration():

    @overload_configuration
    def test_function(arg1, arg2):
        return arg1, arg2

    assert test_function("value1", "value2") == ("value1", "value2")
    assert test_function("value1", arg2="value2") == ("value1", "value2")
    assert test_function("value1", "value2", define=["k1=v1", "k2=v2"]) == ("value1", "value2")
    assert config.get("k1") == "v1"
    assert config.get("k2") == "v2"

# Generated at 2022-06-14 05:34:13.506121
# Unit test for function overload_configuration
def test_overload_configuration():
    # Test if the decorator functions work
    @overload_configuration
    def test_function1(one, two=2, three=3, define=None):
        return config.get("one", one), config.get("two", two), config.get("three", three)

    assert test_function1(one=1, two=4, three=9, define=["three=3", "one=1"]) == (1, 4, 3)

    # Test if define is allowed to be omitted
    @overload_configuration
    def test_function2(one=1, two=2, three=3):
        return config.get("one", one), config.get("two", two), config.get("three", three)

    assert test_function2() == (1, 2, 3)

    # Test if "overload_config

# Generated at 2022-06-14 05:34:19.442026
# Unit test for function overload_configuration
def test_overload_configuration():
    """Utility function to check that the overload_configuration decorator
    is working well
    """

    def func(new_version, define):
        return define

    func = overload_configuration(func)

    ret = func(None, define=["major_on_zero=False"])

    assert ret == ["major_on_zero=False"]
    assert config.get("major_on_zero") == "False"

# Generated at 2022-06-14 05:34:36.753412
# Unit test for function overload_configuration
def test_overload_configuration():
    assert config["changelog_components"] == "components.breaking_change,other_components.something_else"
    @overload_configuration
    def func(define=None):
        assert config["changelog_components"] == "components.breaking_change,other_components.something_else"
        return define
    define = ["changelog_components=my_components.something,else"]
    assert func(define=define) == define
    assert config["changelog_components"] == "my_components.something,else"

# Generated at 2022-06-14 05:34:45.596385
# Unit test for function overload_configuration
def test_overload_configuration():
    # Declare the function to overload
    @overload_configuration
    def test(define):
        return config["key"]

    # Check the overload_configuration
    test(define=["key=value"])
    assert config["key"] == "value"
    test(define=["key=value_2"])
    assert config["key"] == "value_2"
    test(define=[])
    assert config["key"] == "value_2"

# Generated at 2022-06-14 05:34:50.615660
# Unit test for function current_changelog_components
def test_current_changelog_components():
    components = current_changelog_components()
    assert isinstance(components, list)
    assert len(components) == 3
    assert hasattr(components[0], "__call__")
    assert components[0].__name__ == "section_changelog"
    assert hasattr(components[1], "__call__")
    assert components[1].__name__ == "section_commits"
    assert hasattr(components[2], "__call__")
    assert components[2].__name__ == "section_commits_not_included"

# Generated at 2022-06-14 05:34:55.966788
# Unit test for function overload_configuration
def test_overload_configuration():
    from .__main__ import main

    # We mock get() because we don't have a real setup.cfg file.
    config.get = lambda x, y=None: y

    assert main(
        ["version"],
        define=["changelog_components=semantic_release.changelog.config_reader.current_changelog_components"]
    ) == 0

# Generated at 2022-06-14 05:35:03.778254
# Unit test for function current_changelog_components
def test_current_changelog_components():
    path = os.path.dirname(__file__)
    config["changelog_components"] = "semantic_release.changelog_components.commit_parser"
    components = current_changelog_components()
    assert len(components) == 1
    assert components[0] == current_commit_parser()
    os.remove(os.path.join(path, "pyproject.toml"))

# Generated at 2022-06-14 05:35:10.837630
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from .changelog.components import breaking, feature, fix, security

    conf = config.copy()
    conf["changelog_components"] = "semantic_release.changelog.components.breaking,semantic_release.changelog.components.feature,semantic_release.changelog.components.fix,semantic_release.changelog.components.security"

    new_config = _config_from_pyproject("pyproject.toml")
    new_config.update(conf)

    # Cast to a UserDict so that we can mock the get() method.
    config.data = UserDict(new_config)

    assert current_changelog_components() == [breaking, feature, fix, security]



# Generated at 2022-06-14 05:35:14.476825
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def foo(a):
        return config.get("a")

    assert foo(define=["a=42"], a=43) == 42



# Generated at 2022-06-14 05:35:20.014173
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def test_function(define, **kwargs):
        return define

    assert test_function(define="test=ok") == ["test=ok"]
    assert test_function(define=["test=ok", "n=v"]) == ["test=ok", "n=v"]



# Generated at 2022-06-14 05:35:25.916047
# Unit test for function overload_configuration
def test_overload_configuration():
    # We need to make a copy of the config to compare it after the execution
    backup_of_config = UserDict(config)
    # We make a function that returns True
    def function_returning_true():
        return True
    # We overload "config" with a line in the define array
    function_returning_true = overload_configuration(function_returning_true)
    function_returning_true(define=["is_true=True"])
    assert config["is_true"]=="True"
    # We restore the config to its initial state
    config=backup_of_config

# Generated at 2022-06-14 05:35:32.608327
# Unit test for function current_changelog_components
def test_current_changelog_components():
    config = {
        "changelog_components": "semantic_release.changelog.parse_merge_commit, semantic_release.changelog.parse_issue_ref"
    }
    components = current_changelog_components()
    assert len(components) == 2
    for c in components:
        assert callable(c)

# Generated at 2022-06-14 05:35:52.473949
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def set_configuration(**kwargs):
        return config["plugin_config"]

    # Set a default value
    config["plugin_config"] = "my_default_config"
    assert set_configuration() == "my_default_config"

    # Use this value
    assert set_configuration(define=["plugin_config=my_config"]) == "my_config"

    # Back to default
    assert (
        set_configuration(define=["prefix_for_plugin_config=my_other_config"])
        == "my_default_config"
    )

# Generated at 2022-06-14 05:35:55.959102
# Unit test for function current_commit_parser
def test_current_commit_parser():
    default_commit_message_parser = current_commit_parser()
    assert "ConventionalCommit" in str(type(default_commit_message_parser))


# Generated at 2022-06-14 05:35:57.095054
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert current_commit_parser()



# Generated at 2022-06-14 05:36:00.041623
# Unit test for function current_commit_parser
def test_current_commit_parser():
    """
    Test function current_commit_parser
    """

    commit_parser = current_commit_parser()
    assert callable(commit_parser)



# Generated at 2022-06-14 05:36:01.977109
# Unit test for function current_commit_parser
def test_current_commit_parser():
    assert callable(current_commit_parser())



# Generated at 2022-06-14 05:36:10.340294
# Unit test for function overload_configuration
def test_overload_configuration():
    @overload_configuration
    def overload_config(define=None):
        config["overloaded"] = "OK"

    # Simple overload
    config["overloaded"] = "KO"
    overload_config()
    assert config["overloaded"] == "OK"

    # Overload with define array
    config["overloaded"] = "KO"
    overload_config(define=["overloaded=OK"])
    assert config["overloaded"] == "OK"

    # Overload with multiple elements in array
    config["overloaded"] = "KO"
    config["overloaded2"] = "KO"
    overload_config(define=["overloaded=OK", "overloaded2=OK"])
    assert config["overloaded"] == "OK"
    assert config["overloaded2"] == "OK"

    # Overload with multiple elements in array

# Generated at 2022-06-14 05:36:15.914604
# Unit test for function current_changelog_components
def test_current_changelog_components():
    from semantic_release.changelog import ChangelogGitHubParser
    changelog_components = current_changelog_components()
    assert changelog_components == [(ChangelogGitHubParser)]



# Generated at 2022-06-14 05:36:17.964272
# Unit test for function current_changelog_components
def test_current_changelog_components():
    assert len(current_changelog_components()) == 1

# Generated at 2022-06-14 05:36:29.761818
# Unit test for function overload_configuration
def test_overload_configuration():
    def test_func(define):
        assert config["define1"] == "value1"
        assert config["define2"] == "value2"
        assert config["define3"] == "value3"

    new_config = {
        "define1": "not_value1",
        "define2": "not_value2",
        "define3": "not_value3",
    }
    config_bkp = config.copy()
    config.clear()
    config.update(new_config)
    overload_configuration(test_func)(define=["define1=value1", "define2=value2", "define3=value3"])
    config.clear()
    config.update(config_bkp)

# Generated at 2022-06-14 05:36:37.923015
# Unit test for function overload_configuration
def test_overload_configuration():

    @overload_configuration
    def func(a, b):
        return a, b

    assert func(1, 2, define=["a=3"]) == (3, 2)
    assert config["a"] == "3"
    assert func(a=1, b=2) == (1, 2)

    assert func(1, 2, define="a=3") == (3, 2)
    assert func(1, 2, define=["a=3", "b=4"]) == (3, 4)