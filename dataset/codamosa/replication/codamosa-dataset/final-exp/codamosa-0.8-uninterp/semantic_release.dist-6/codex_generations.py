

# Generated at 2022-06-14 04:59:32.284842
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config['remove_dist'] = False
    assert should_remove_dist() is False
  

# Generated at 2022-06-14 04:59:34.589875
# Unit test for function should_build
def test_should_build():
    assert should_build()
    # TODO need to write unit tests
    assert should_remove_dist()

# Generated at 2022-06-14 04:59:44.893716
# Unit test for function should_remove_dist
def test_should_remove_dist():
    from invoke.config import Config
    from .settings import default_config
    config = Config(default_config)

    # should return false if "remove_dist" and "upload_to_pypi" are both False
    config.update({"remove_dist": False, "upload_to_pypi": False})
    assert not should_remove_dist()

    # should return false if "remove_dist" is False and "upload_to_pypi" is True
    config.update({"remove_dist": False, "upload_to_pypi": True})
    assert not should_remove_dist()

    # should return False if "remove_dist" is True and "upload_to_pypi" is False
    config.update({"remove_dist": True, "upload_to_pypi": False})

# Generated at 2022-06-14 04:59:58.041101
# Unit test for function should_build
def test_should_build():
    # when build_command is set to True
    data = {
        "upload_to_pypi": True,
        "upload_to_release": True,
        "build_command": True,
        "remove_dist": True,
    }
    assert should_build(**data) is True

    # when build_command is set to False
    data = {
        "upload_to_pypi": True,
        "upload_to_release": True,
        "build_command": False,
        "remove_dist": True,
    }
    assert should_build(**data) is False

    # when upload_to_pypi is set to False