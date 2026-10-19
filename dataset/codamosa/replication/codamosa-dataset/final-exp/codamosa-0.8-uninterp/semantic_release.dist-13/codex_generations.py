

# Generated at 2022-06-14 04:59:33.711429
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config_mock_false = {
        "remove_dist": "false",
        "upload_to_pypi": "false",
        "upload_to_release": "true",
        "build_command": "false",
    }

    config_mock_false_2 = {
        "remove_dist": "false",
        "upload_to_pypi": "true",
        "upload_to_release": "false",
        "build_command": "false",
    }

    config_mock_true = {
        "remove_dist": "true",
        "upload_to_pypi": "true",
        "upload_to_release": "true",
        "build_command": "false",
    }

    assert should_remove_dist(config=config_mock_false) is False


# Generated at 2022-06-14 04:59:34.440377
# Unit test for function should_build
def test_should_build():
    assert should_build()


# Generated at 2022-06-14 04:59:36.061041
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True


# Generated at 2022-06-14 04:59:41.828785
# Unit test for function should_build
def test_should_build():
    config.set("upload_to_pypi", True)
    config.set("build_command", "echo hello")
    assert should_build()
    config.set("upload_to_pypi", False)
    config.set("upload_to_release", True)
    assert should_build()
    config.set("build_command", "false")
    assert not should_build()

# Generated at 2022-06-14 04:59:42.845503
# Unit test for function should_build
def test_should_build():
    assert should_build()



# Generated at 2022-06-14 04:59:43.793270
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False

# Generated at 2022-06-14 04:59:51.675602
# Unit test for function should_build
def test_should_build():
    assert not should_build()

    config.update({"upload_to_pypi": True, "upload_to_release": False})
    assert should_build()

    config.update({"upload_to_pypi": False, "upload_to_release": True})
    assert should_build()

    config.update({"upload_to_pypi": True, "upload_to_release": True})
    assert should_build()



# Generated at 2022-06-14 04:59:57.463660
# Unit test for function should_remove_dist
def test_should_remove_dist():
    # test if it returns True when "remove_dist" is empty
    assert should_remove_dist()

    # test if it returns True when "remove_dist" equals "true"
    assert should_remove_dist()

    # test if it returns True when "remove_dist" equals "false"
    assert should_remove_dist()


# Generated at 2022-06-14 05:00:01.843567
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is False
    config["build_command"] = False
    assert should_remove_dist() is False
    config["build_command"] = True
    assert should_remove_dist() is True
    config["remove_dist"] = False
    assert should_remove_dist() is False

# Generated at 2022-06-14 05:00:04.181852
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("remove_dist", "true")
    assert should_remove_dist()

# Generated at 2022-06-14 05:03:55.186775
# Unit test for function should_build
def test_should_build():
    config.update({"upload_to_pypi": False, "upload_to_release": False, "build_command": False})
    assert should_build() == False
    config.update({"upload_to_pypi": True, "upload_to_release": False, "build_command": True})
    assert should_build() == True
    config.update({"upload_to_pypi": False, "upload_to_release": True, "build_command": True})
    assert should_build() == True



# Generated at 2022-06-14 05:03:56.165593
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert False == should_remove_dist()

# Generated at 2022-06-14 05:03:57.904962
# Unit test for function should_build
def test_should_build():
    # pylint: disable=fixme
    # TODO: Fix this test to be more effective.
    assert should_build()

# Generated at 2022-06-14 05:03:58.963942
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert(should_remove_dist() == True)

# Generated at 2022-06-14 05:04:03.357504
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    config["build_command"] = "build_command"
    config["upload_to_pypi"] = True
    assert should_remove_dist()

# Generated at 2022-06-14 05:04:10.239519
# Unit test for function should_build
def test_should_build():
    assert should_build() == False
    config.set("upload_to_pypi", True)
    assert should_build() == False
    config.set("upload_to_release", True)
    assert should_build() == False
    config.set("build_command", "echo foo")
    assert should_build() == True
    config.set("build_command", "echo foo", "false")
    assert should_build() == False


# Generated at 2022-06-14 05:04:14.726380
# Unit test for function should_remove_dist
def test_should_remove_dist():
    # Test if config.get("remove_dist") is True
    config["remove_dist"] = True
    assert should_remove_dist()
    # Test if config.get("remove_dist") is False
    config["remove_dist"] = False
    assert not should_remove_dist()



# Generated at 2022-06-14 05:04:16.903309
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True


# Generated at 2022-06-14 05:04:18.090236
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True



# Generated at 2022-06-14 05:04:25.814015
# Unit test for function should_build
def test_should_build():
    assert not should_build()

    config.set("upload_to_pypi", True)
    config.set("build_command", "true")
    assert should_build()

    config.set("upload_to_pypi", False)
    config.set("upload_to_release", True)
    assert should_build()

    config.set("build_command", "false")
    assert not should_build()

