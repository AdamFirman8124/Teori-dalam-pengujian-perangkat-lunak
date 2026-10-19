

# Generated at 2022-06-14 04:59:30.887493
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    config["build_command"] = True
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    assert should_remove_dist() == True

    config["build_command"] = False
    assert should_remove_dist() == False

    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = True
    assert should_remove_dist() == False


# Generated at 2022-06-14 04:59:43.080533
# Unit test for function should_build
def test_should_build():
    test_config = {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "sphinx-build",
    }
    assert should_build(config=test_config) == True
    test_config = {
        "upload_to_pypi": False,
        "upload_to_release": True,
        "build_command": "sphinx-build",
    }
    assert should_build(config=test_config) == True
    test_config = {
        "upload_to_pypi": False,
        "upload_to_release": False,
        "build_command": "sphinx-build",
    }
    assert should_build(config=test_config) == False

# Generated at 2022-06-14 04:59:44.023903
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is True

# Generated at 2022-06-14 04:59:48.333546
# Unit test for function should_remove_dist
def test_should_remove_dist():
    """
    Test to check should_remove_dist when remove_dist is false
    """
    config["remove_dist"] = False
    assert not should_remove_dist()



# Generated at 2022-06-14 05:00:00.727750
# Unit test for function should_remove_dist
def test_should_remove_dist():
    # upload_to_release is True, remove_dist is True
    logger.debug("Running test_should_remove_dist")
    config["upload_to_release"] = "true"
    config["remove_dist"] = "true"
    assert should_remove_dist()

    # upload_to_release is True, remove_dist is False
    config["upload_to_release"] = "true"
    config["remove_dist"] = "false"
    assert not should_remove_dist()

    # upload_to_release is False, remove_dist is False
    config["upload_to_release"] = "false"
    config["remove_dist"] = "true"
    assert not should_remove_dist()

    config["upload_to_release"] = "false"
    config["remove_dist"] = "false"

# Generated at 2022-06-14 05:00:02.656581
# Unit test for function should_remove_dist
def test_should_remove_dist():
    from .settings import config
    assert should_remove_dist() is True

# Generated at 2022-06-14 05:00:14.658982
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = "false"
    assert not should_build()

    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = "test"
    assert should_build()

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["build_command"] = "false"
    assert not should_build()

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["build_command"] = "true"
    assert should_build()



# Generated at 2022-06-14 05:00:22.176441
# Unit test for function should_remove_dist
def test_should_remove_dist():
    _config = {
        "build_command": "./setup.py sdist",
        "upload_to_release": True,
        "remove_dist": True,
    }
    assert should_remove_dist(_config)

    _config = {
        "build_command": "./setup.py sdist",
        "upload_to_release": True,
        "remove_dist": False,
    }
    assert not should_remove_dist(_config)

    _config = {"build_command": "false", "upload_to_release": True}
    assert not should_remove_dist(_config)

# Generated at 2022-06-14 05:00:22.691131
# Unit test for function should_build
def test_should_build():
    assert should_build()

# Generated at 2022-06-14 05:00:27.783343
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("remove_dist", True)
    config.set("build_command", "build")
    config.set("upload_to_pypi", True)
    assert should_remove_dist() == True

    config.set("upload_to_pypi", False)
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:03:58.630690
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert not should_remove_dist()

# Generated at 2022-06-14 05:04:00.813203
# Unit test for function should_build
def test_should_build():
    assert should_build() == True

# Generated at 2022-06-14 05:04:12.918917
# Unit test for function should_build
def test_should_build():
    config.values["upload_to_pypi"] = True
    assert should_build() is True
    config.values["upload_to_pypi"] = False
    config.values["upload_to_release"] = True
    assert should_build() is True
    config.values["upload_to_pypi"] = True
    config.values["upload_to_release"] = True
    assert should_build() is True
    config.values["upload_to_pypi"] = False
    config.values["upload_to_release"] = False
    assert should_build() is False

    # not upload_to_pypi and upload_to_release
    # but wrong build command
    config.values["build_command"] = "false"
    assert should_build() is False


# Generated at 2022-06-14 05:04:23.257360
# Unit test for function should_build
def test_should_build():
    # Test to make sure it returns True when we have the full build config.
    config["build_command"] = "python setup.py sdist"
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    assert should_build() is True
    # Test to make sure it returns False when no build command is given.
    config["build_command"] = False
    assert should_build() is False
    # Test to make sure it returns False when both upload options are False.
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    assert should_build() is False
    # Test to make sure it returns False when one upload option is False.
    config["upload_to_pypi"] = True

# Generated at 2022-06-14 05:04:28.608964
# Unit test for function should_remove_dist
def test_should_remove_dist():
    # GIVEN
    config["remove_dist"] = "true"

    # WHEN
    result = should_remove_dist()

    # THEN
    assert result == True

    # GIVEN
    config["remove_dist"] = "false"

    # WHEN
    result = should_remove_dist()

    # THEN
    assert result == False

# Generated at 2022-06-14 05:04:38.430354
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False
    config['remove_dist'] = 'true'
    assert should_remove_dist() == False # should be False for now.
    config['build_command'] = 'true'
    assert should_remove_dist() == True
    config['upload_to_pypi'] = 'true'
    assert should_remove_dist() == True
    config['upload_to_release'] = 'true'
    assert should_remove_dist() == True
    config['upload_to_pypi'] = 'false'
    assert should_remove_dist() == True
    config['upload_to_release'] = 'false'
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:04:44.789237
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("remove_dist", False)
    assert not should_remove_dist()
    config.set("remove_dist", True)
    config.set("build_command", "false")
    assert not should_remove_dist()
    config.set("build_command", "ls")
    assert should_remove_dist()
    config.config_vars.pop('remove_dist')
    config.config_vars.pop('build_command')



# Generated at 2022-06-14 05:04:46.738632
# Unit test for function should_build
def test_should_build():
    assert should_build() == True



# Generated at 2022-06-14 05:04:47.952805
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True

# Generated at 2022-06-14 05:04:50.556319
# Unit test for function should_build
def test_should_build():
    assert should_build() == True

#Unit test for function should_remove_dist()