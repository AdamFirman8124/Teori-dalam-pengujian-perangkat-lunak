

# Generated at 2022-06-14 04:59:14.446486
# Unit test for function should_build
def test_should_build():
    assert should_build()


# Generated at 2022-06-14 04:59:16.320902
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False

# Generated at 2022-06-14 04:59:19.209733
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("remove_dist", 1)
    config.set("build_command", "pip")
    assert should_remove_dist() == True



# Generated at 2022-06-14 04:59:28.934209
# Unit test for function should_build
def test_should_build():
    logger.debug("Running test_should_build")

    config.set("upload_to_pypi", False)
    config.set("upload_to_release", False)
    assert not should_build()

    config.set("upload_to_pypi", False)
    config.set("upload_to_release", True)
    assert should_build()

    config.set("upload_to_pypi", False)
    config.set("build_command", False)
    config.set("upload_to_release", True)
    assert not should_build()

    config.set("upload_to_pypi", True)
    config.set("upload_to_release", True)
    config.set("build_command", "python setup.py sdist")
    assert should_build()


# Generated at 2022-06-14 04:59:42.041174
# Unit test for function should_build
def test_should_build():
    assert should_build() is False
    config.set("upload_to_pypi", False)
    config.set("upload_to_release", False)
    config.set("build_command", "")
    assert should_build() is False
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", True)
    config.set("build_command", "command")
    assert should_build() is True
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", False)
    assert should_build() is False
    config.set("upload_to_pypi", False)
    config.set("upload_to_release", True)
    assert should_build() is False

# Generated at 2022-06-14 04:59:50.411084
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["remove_dist"] = False
    assert should_remove_dist() is False

    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["remove_dist"] = False
    assert should_remove_dist() is False

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["remove_dist"] = False
    assert should_remove_dist() is False

    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["remove_dist"] = True
    assert should_remove_dist() is True



# Generated at 2022-06-14 04:59:58.034285
# Unit test for function should_build
def test_should_build():
    assert should_build() == False
    config["upload_to_pypi"] = "true"
    assert should_build() == False
    config["upload_to_release"] = "true"
    assert should_build() == False
    config["build_command"] = "ls -la"
    assert should_build() == True
    config["upload_to_pypi"] = "false"
    assert should_build() == True
    config["upload_to_release"] = "false"
    assert should_build() == False


# Generated at 2022-06-14 05:00:04.663296
# Unit test for function should_build
def test_should_build():
    config.update({
        "upload_to_pypi": True,
        "upload_to_release": True,
        "build_command": "setup.py sdist bdist_wheel",
    })
    assert should_build()
    config.update({
        "upload_to_pypi": False,
        "upload_to_release": True,
        "build_command": "setup.py sdist bdist_wheel",
    })
    assert should_build()
    config.update({
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "setup.py sdist bdist_wheel",
    })
    assert should_build()

# Generated at 2022-06-14 05:00:05.840567
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is False

# Generated at 2022-06-14 05:00:07.528529
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True



# Generated at 2022-06-14 05:03:41.600915
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = "build"
    config["remove_dist"] = True
    assert should_remove_dist() is True
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["build_command"] = "build"
    config["remove_dist"] = True
    assert should_remove_dist() is True
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["build_command"] = "build"
    config["remove_dist"] = False
    assert should_remove_dist() is False
    config["upload_to_pypi"] = False

# Generated at 2022-06-14 05:03:49.037998
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.settings = {
        "upload_to_pypi": "true",
        "upload_to_release": "",
        "build_command": "python setup.py sdist bdist_wheel",
        "remove_dist": "true",
    }
    assert should_remove_dist() == True

    config.settings = {
        "upload_to_pypi": "true",
        "upload_to_release": "",
        "build_command": "false",
        "remove_dist": "true",
    }
    assert should_remove_dist() == False


# Generated at 2022-06-14 05:03:50.317291
# Unit test for function should_build
def test_should_build():
    assert should_build() == True


# Generated at 2022-06-14 05:03:53.169325
# Unit test for function should_build
def test_should_build():
    assert should_build() is False
    # should_build(build_command=True, upload_to_pypi=True) is True



# Generated at 2022-06-14 05:03:54.343540
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist()


# Generated at 2022-06-14 05:04:00.785645
# Unit test for function should_build
def test_should_build():
    config_true = {"upload_to_pypi": True,
                   "upload_to_release": True,
                   "build_command": "some command"}
    assert should_build(config_true)

    config_false = {"upload_to_pypi": False,
                    "upload_to_release": False,
                    "build_command": "some command"}
    assert not should_build(config_false)

    config_false = {"upload_to_pypi": True,
                    "upload_to_release": False,
                    "build_command": False}
    assert not should_build(config_false)



# Generated at 2022-06-14 05:04:05.448261
# Unit test for function should_build
def test_should_build():
    config["build_command"] = "pytest"
    assert should_build() == True

    config["build_command"] = False
    assert should_build() == False

    config["upload_to_pypi"] = True
    assert should_build() == False


# Generated at 2022-06-14 05:04:15.530131
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_remove_dist() == True
    config["remove_dist"] = True
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    assert should_remove_dist() == True
    config["remove_dist"] = False
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    assert should_remove_dist() == False
    config["remove_dist"] = False
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_remove_dist() == False
    config["remove_dist"] = False
   

# Generated at 2022-06-14 05:04:17.148617
# Unit test for function should_build
def test_should_build():
    assert should_build() == True



# Generated at 2022-06-14 05:04:22.678267
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    assert should_remove_dist()
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_remove_dist()
    config["build_command"] = False
    assert not should_remove_dist()
