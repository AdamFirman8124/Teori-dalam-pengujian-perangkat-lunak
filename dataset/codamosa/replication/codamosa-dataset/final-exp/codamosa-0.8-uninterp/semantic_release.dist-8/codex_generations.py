

# Generated at 2022-06-14 04:59:14.155617
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    assert should_remove_dist()
    config["remove_dist"] = False
    assert not should_remove_dist()



# Generated at 2022-06-14 04:59:14.938733
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True


# Generated at 2022-06-14 04:59:25.408353
# Unit test for function should_build
def test_should_build():
    config.set("upload_to_pypi", False)
    config.set("upload_to_release", False)
    assert should_build() == False

    config.set("upload_to_pypi", True)
    config.set("upload_to_release", False)
    assert should_build() == True

    config.set("upload_to_pypi", False)
    config.set("upload_to_release", True)
    assert should_build() == True

    config.set("upload_to_pypi", True)
    config.set("upload_to_release", True)
    assert should_build() == True

    config.set("build_command", False)
    assert should_build() == False

# Generated at 2022-06-14 04:59:30.432223
# Unit test for function should_build
def test_should_build():
    config["build_command"] = "setup.py sdist"
    config["upload_to_pypi"] = True
    assert should_build() == True
    config["upload_to_release"] = True
    assert should_build() == True
    config["upload_to_pypi"] = False
    assert should_build() == True
    config["build_command"] = "false"
    assert should_build() == False
    config["build_command"] = "setup.py sdist"
    config["upload_to_release"] = False
    assert should_build() == False

# Generated at 2022-06-14 04:59:31.871027
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True

# Generated at 2022-06-14 04:59:33.053743
# Unit test for function should_build
def test_should_build():
    assert should_build() == True

# Generated at 2022-06-14 04:59:34.900818
# Unit test for function should_build
def test_should_build():
    assert should_build() is True
    assert should_remove_dist() is True

# Generated at 2022-06-14 04:59:45.013250
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True
    # Test for when remove_dist is set to false
    config.set({"remove_dist": "false"})
    assert should_remove_dist() == False
    # Test for when upload_to_pypi is set to false
    config.set({"remove_dist": "true", "upload_to_pypi": "false"})
    assert should_remove_dist() == True
    # Test for when upload_to_release is set to false
    config.set({"remove_dist": "true", "upload_to_release": "false"})
    assert should_remove_dist() == False
    # Test for when upload_to_release and upload_to_pypi are both false

# Generated at 2022-06-14 04:59:58.040181
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = None
    assert not should_build()

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["build_command"] = None
    assert not should_build()

    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = None
    assert not should_build()

    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = "ls"
    assert not should_build()

    config["upload_to_pypi"] = False

# Generated at 2022-06-14 05:00:04.566447
# Unit test for function should_build
def test_should_build():
    assert should_build() is False

    config["upload_to_pypi"] = True
    assert should_build() is True

    config["upload_to_release"] = False
    assert should_build() is True
    config["upload_to_pypi"] = False
    assert should_build() is False

    config["build_command"] = "fake_command"
    assert should_build() is True
    config["upload_to_pypi"] = False
    assert should_build() is False



# Generated at 2022-06-14 05:01:56.393299
# Unit test for function should_build
def test_should_build():
    config["build_command"] = "cat"
    assert should_build()
    config["upload_to_pypi"] = False
    assert should_build()
    config["upload_to_release"] = False
    assert not should_build()
    config["build_command"] = ""
    assert not should_build()
    config["build_command"] = "false"
    assert not should_build()



# Generated at 2022-06-14 05:02:07.431521
# Unit test for function should_build
def test_should_build():
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", True)
    config.set("build_command", "ls")
    assert should_build() is True
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", True)
    config.set("build_command", "false")
    assert should_build() is False
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", False)
    config.set("build_command", "ls")
    assert should_build() is True
    config.set("upload_to_pypi", False)
    config.set("upload_to_release", True)
    config.set("build_command", "ls")


# Generated at 2022-06-14 05:02:14.124764
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False
    config["remove_dist"] = True
    assert should_remove_dist() == False
    config["upload_to_release"] = True
    assert should_remove_dist() == False
    config["build_command"] = "Command"
    assert should_remove_dist() == True
    

# Generated at 2022-06-14 05:02:19.510602
# Unit test for function should_remove_dist
def test_should_remove_dist():
    from .mock import mock_config

    # should_build() is True
    # remove_dist is True (default)
    config = mock_config({"upload_to_pypi": True})
    assert should_remove_dist()

    # should_build() is True
    # remove_dist is False
    config = mock_config({"upload_to_pypi": True, "remove_dist": False})
    assert not should_remove_dist()

    # should_build() is False
    # remove_dist is True (default)
    config = mock_config({})
    assert not should_remove_dist()

    # should_build() is False
    # remove_dist is False
    config = mock_config({"remove_dist": False})
    assert not should_remove_dist()

# Generated at 2022-06-14 05:02:20.052197
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is True

# Generated at 2022-06-14 05:02:25.324011
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("remove_dist", "True")
    assert should_remove_dist() == True

    config.set("remove_dist", "False")
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:02:38.663597
# Unit test for function should_build
def test_should_build():
    config.pop("upload_to_pypi", None)
    config.pop("upload_to_release", None)
    config.pop("build_command", None)

    assert not should_build()

    config.pop("upload_to_pypi", None)
    config.pop("upload_to_release", None)
    config.pop("build_command", None)

    config.update({"build_command": "python setup.py bdist_wheel"})

    assert should_build()

    config.update({"upload_to_pypi": True})

    assert should_build()

    config.update({"upload_to_release": True})

    assert should_build()

    config.update({"build_command": "false"})

    assert not should_build()


# Generated at 2022-06-14 05:02:39.756253
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True

# Generated at 2022-06-14 05:02:52.621920
# Unit test for function should_build
def test_should_build():
    config = {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "",
    }
    assert should_build() == False
    assert should_remove_dist() == False

    config = {
        "upload_to_pypi": False,
        "upload_to_release": False,
        "build_command": "",
    }
    assert should_build() == False
    assert should_remove_dist() == False

    config = {
        "upload_to_pypi": False,
        "upload_to_release": True,
        "build_command": "",
    }
    assert should_build() == False
    assert should_remove_dist() == False


# Generated at 2022-06-14 05:02:57.833387
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = "true"
    config["build_command"] = "command"
    assert should_remove_dist()
    config["build_command"] = "false"
    assert not should_remove_dist()
    config["build_command"] = "command"
    config["remove_dist"] = "false"
    assert not should_remove_dist()

# Generated at 2022-06-14 05:04:50.365703
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = "true"
    config["upload_to_release"] = "true"
    config["build_command"] = "true"
    assert should_build() is True
    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = "false"
    assert should_build() is False
    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = "true"
    assert should_build() is True
    config["upload_to_pypi"] = "true"
    config["upload_to_release"] = "false"
    assert should_build() is True
    config["upload_to_pypi"] = "true"
    config["upload_to_release"] = "true"
   

# Generated at 2022-06-14 05:04:51.976110
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True



# Generated at 2022-06-14 05:04:53.085417
# Unit test for function should_build
def test_should_build():
    should_build()


# Generated at 2022-06-14 05:04:54.657910
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True


# Generated at 2022-06-14 05:04:55.829407
# Unit test for function should_build
def test_should_build():
    assert not should_build()


# Generated at 2022-06-14 05:05:00.507013
# Unit test for function should_remove_dist
def test_should_remove_dist():
    # Test if should_remove_dist() returns the correct value when "upload_to_pypi" is False.
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = "false"
    config["remove_dist"] = True

    assert(not should_remove_dist())

# Generated at 2022-06-14 05:05:09.674160
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.update({'build_command': 'false', 'remove_dist': True})
    assert should_remove_dist() == False

    config.update({'build_command': 'build', 'remove_dist': True})
    assert should_remove_dist() == True

    config.update({'build_command': 'false', 'remove_dist': False})
    assert should_remove_dist() == False

    config.update({'build_command': 'build', 'remove_dist': False})
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:05:17.273995
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = "false"
    config["build_command"] = "false"
    assert should_build() == False

    config["upload_to_pypi"] = True
    config["build_command"] = "false"
    assert should_build() == False

    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = True
    config["build_command"] = "false"
    assert should_build() == False

    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["build_command"] = "false"
    assert should_build() == False

    config["upload_to_pypi"] = False
    config["upload_to_release"] = "false"

# Generated at 2022-06-14 05:05:19.216517
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert not should_remove_dist()

# Generated at 2022-06-14 05:05:27.152186
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = "true"
    assert should_remove_dist()
    config["remove_dist"] = "false"
    assert not should_remove_dist()
    config["asset_loc"] = "wheelhouse"
    config["upload_to_release"] = "true"
    assert should_remove_dist()
    config["upload_to_pypi"] = "true"
    assert should_remove_dist()
    config["upload_to_release"] = "false"
    assert should_remove_dist()
    config["upload_to_pypi"] = "false"
    assert not should_remove_dist()
    config["asset_loc"] = "dist"
    config["upload_to_release"] = "true"
    assert should_remove_dist()