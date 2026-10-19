

# Generated at 2022-06-14 04:59:32.225547
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    assert should_remove_dist() == True
    config["remove_dist"] = False
    assert should_remove_dist() == False

# Generated at 2022-06-14 04:59:36.873545
# Unit test for function should_remove_dist
def test_should_remove_dist():
    test_config = {
        "build_command": "sdist",
        "remove_dist": "true",
        "upload_to_pypi": "true",
        "upload_to_release": "false",
    }
    assert should_remove_dist(test_config)

# Generated at 2022-06-14 04:59:45.734151
# Unit test for function should_build
def test_should_build():
    config_default = {
        "upload_to_pypi": False,
        "upload_to_release": False,
        "build_command": "false",
        "remove_dist": False,
    }
    config.update(config_default)
    assert not should_build()
    config.update({"upload_to_pypi": True, "build_command": "true"})
    assert should_build()
    config.update({"upload_to_pypi": True, "build_command": "false"})
    assert not should_build()
    config.update({"upload_to_pypi": False, "upload_to_release": True})
    assert should_build()

# Generated at 2022-06-14 04:59:58.258752
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["build_command"] = "mock command"
    assert should_remove_dist() == True

    config["build_command"] = "false"
    assert should_remove_dist() == False

    del config["build_command"]
    assert should_remove_dist() == False

    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    assert should_remove_dist() == True

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_remove_dist() == True

    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    assert should_remove_dist() == True

    config["remove_dist"] = False
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:00:03.756666
# Unit test for function should_build
def test_should_build():
    assert should_build() is False
    config["upload_to_pypi"] = True
    assert should_build() is True
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_build() is True
    config["upload_to_release"] = False
    config["build_command"] = "echo"
    assert should_build() is False


# Generated at 2022-06-14 05:00:04.946186
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert not should_remove_dist()

# Generated at 2022-06-14 05:00:11.044259
# Unit test for function should_build
def test_should_build():
    assert not should_build()
    config["build_command"] = "echo"
    assert not should_build()
    config["upload_to_pypi"] = True
    assert should_build()
    config["upload_to_pypi"] = False
    assert not should_build()
    config["upload_to_release"] = True
    assert should_build()


# Generated at 2022-06-14 05:00:17.212004
# Unit test for function should_build
def test_should_build():
    """Test function should_build"""
    assert should_build() == False
    config["upload_to_pypi"] = True
    assert should_build() == False
    config["upload_to_release"] = True
    assert should_build() == False
    config["build_command"] = "false"
    assert should_build() == False
    config["build_command"] = "python setup.py sdist"
    assert should_build() == True


# Generated at 2022-06-14 05:00:19.343706
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is False



# Generated at 2022-06-14 05:00:23.389025
# Unit test for function should_build
def test_should_build():
    # check that default value is false
    # check with `upload_to_pypi` only
    # check with `upload_to_release` only
    # check with both
    # check with neither
    pass



# Generated at 2022-06-14 05:02:25.393918
# Unit test for function should_remove_dist
def test_should_remove_dist():
    # GIVEN
    config["upload_to_pypi"] = True
    config["build_command"] = "sdist bdist_wheel"

    # WHEN
    should_remove = should_remove_dist()

    # THEN
    assert should_remove

# Generated at 2022-06-14 05:02:35.585057
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = "true"
    config["upload_to_pypi"] = "true"
    config["upload_to_release"] = "true"
    assert should_remove_dist()

    config["upload_to_pypi"] = "false"
    assert should_remove_dist()

    config["upload_to_pypi"] = "true"
    config["upload_to_release"] = "false"
    assert should_remove_dist()

    config["remove_dist"] = "false"
    assert not should_remove_dist()

# Generated at 2022-06-14 05:02:36.889715
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert not should_remove_dist()

# Generated at 2022-06-14 05:02:38.692458
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist()

# Generated at 2022-06-14 05:02:42.513253
# Unit test for function should_build
def test_should_build():
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", True)
    config.set("build_command", "echo")
    assert should_build()

    confi

# Generated at 2022-06-14 05:02:46.546402
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["build_command"] = "true"
    assert should_remove_dist()

# Generated at 2022-06-14 05:02:48.333861
# Unit test for function should_build
def test_should_build():
    assert should_build() == False

# Generated at 2022-06-14 05:02:49.485449
# Unit test for function should_build
def test_should_build():
    assert not should_build()



# Generated at 2022-06-14 05:02:56.306721
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is False
    config.set("build_command", False)
    assert should_remove_dist() is False
    config.set("build_command", "sdist")
    assert should_remove_dist() is False
    config.set("remove_dist", False)
    assert should_remove_dist() is False
    config.set("remove_dist", True)
    assert should_remove_dist() is True

# Generated at 2022-06-14 05:03:05.720876
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["build_command"] = "false"
    config["remove_dist"] = False
    assert should_remove_dist() is False
    config["build_command"] = "true"
    config["remove_dist"] = True
    assert should_remove_dist() is True
    config["build_command"] = "true"
    config["remove_dist"] = False
    assert should_remove_dist() is False
    config["build_command"] = "false"
    config["remove_dist"] = True
    assert should_remove_dist() is False

# Generated at 2022-06-14 05:07:12.694262
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert not should_remove_dist()
    config.set("build_command", "false")
    assert not should_remove_dist()
    config.set("upload_to_pypi", False)
    config.set("upload_to_release", False)
    config.set("build_command", "python setup.py sdist bdist_wheel")
    assert not should_remove_dist()
    config.set("remove_dist", True)
    assert should_remove_dist()



# Generated at 2022-06-14 05:07:22.513838
# Unit test for function should_build
def test_should_build():
    assert not should_build()
    config.set("build_command", "echo foo")
    assert not should_build()
    config.set("build_command", "echo foo")
    config.set("upload_to_pypi", True)
    assert should_build()
    config.set("upload_to_release", True)
    assert should_build()
    config.set("build_command", "false")
    assert not should_build()
    config.set("build_command", "not false")
    config.set("upload_to_release", False)
    assert should_build()



# Generated at 2022-06-14 05:07:28.148653
# Unit test for function should_remove_dist
def test_should_remove_dist():
    package_data = {
        "build_command": "echo 'building'"
    }
    upload_to_pypi = True
    config.set("upload_to_pypi", upload_to_pypi)
    upload_to_release = False
    config.set("upload_to_release", upload_to_release)
    config.set("remove_dist", "true")
    result = should_remove_dist()
    assert result is True, "Should return true"