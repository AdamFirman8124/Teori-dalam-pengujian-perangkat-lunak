

# Generated at 2022-06-14 04:59:22.326915
# Unit test for function should_build
def test_should_build():
    assert not should_build()



# Generated at 2022-06-14 04:59:28.202041
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.update({
        "upload_to_pypi": True,
        "upload_to_release": False,
        "remove_dist": True,
        "build_command": "echo running_build_command"
    })
    assert should_remove_dist()



# Generated at 2022-06-14 04:59:30.501245
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is True
    assert should_remove_dist() != False

# Generated at 2022-06-14 04:59:31.930997
# Unit test for function should_build
def test_should_build():
    assert should_build() == False

# Generated at 2022-06-14 04:59:34.345557
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = "true"
    config["build_command"] = "rm -rf dist"
    assert should_build() == True


# Generated at 2022-06-14 04:59:37.392450
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["build_command"] = "True"
    config["remove_dist"] = "True"
    assert should_remove_dist() == True
    assert should_build() == True

# Generated at 2022-06-14 04:59:37.984606
# Unit test for function should_build
def test_should_build():
    assert should_build() == False


# Generated at 2022-06-14 04:59:40.962791
# Unit test for function should_build
def test_should_build():
    # Check all positive cases
    assert should_build()
    # Check all negative cases
    assert not should_build(build_command=False)



# Generated at 2022-06-14 04:59:46.558630
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    config["upload_to_pypi"] = True
    config["build_command"] = "echo 'hello world'"
    assert should_remove_dist() is True

    config["remove_dist"] = True
    config["upload_to_pypi"] = False
    config["build_command"] = "false"
    assert should_remove_dist() is False


# Generated at 2022-06-14 04:59:54.127388
# Unit test for function should_build
def test_should_build():
    assert should_build() == False
    config["upload_to_pypi"] = "true"
    assert should_build() == False
    config["build_command"] = "true"
    assert should_build() == True
    config["upload_to_pypi"] = "false"
    assert should_build() == True
    config["upload_to_release"] = "false"
    assert should_build() == False
    config["upload_to_release"] = ""
    assert should_build() == False

# Generated at 2022-06-14 05:01:47.082789
# Unit test for function should_build
def test_should_build():
    config.update({"upload_to_pypi": True,
                   "upload_to_release": False,
                   "build_command": "test"})
    assert should_build() is True
    config.update({"upload_to_pypi": False,
                   "upload_to_release": True,
                   "build_command": "test"})
    assert should_build() is True
    config.update({"upload_to_pypi": True,
                   "upload_to_release": True,
                   "build_command": "test"})
    assert should_build() is True
    config.update({"upload_to_pypi": False,
                   "upload_to_release": False,
                   "build_command": "test"})
    assert should_build() is False

# Generated at 2022-06-14 05:01:51.859884
# Unit test for function should_build
def test_should_build():
    assert should_build() == False
    # config["build_command"] = "echo 'RUN'"
    # assert should_build() == True
    # assert should_remove_dist() == False
    # config["remove_dist"] = True
    # assert should_remove_dist() == True
    # config["remove_dist"] = False
    # config["build_command"] = "false"
    # assert should_build() == False

# Generated at 2022-06-14 05:01:53.031777
# Unit test for function should_build
def test_should_build():
    assert should_build() == False

# Generated at 2022-06-14 05:01:53.716222
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist()


# Generated at 2022-06-14 05:01:54.480595
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True


# Generated at 2022-06-14 05:01:58.184822
# Unit test for function should_build
def test_should_build():
    assert should_build() == False
    assert should_remove_dist() == False



# Generated at 2022-06-14 05:02:05.546314
# Unit test for function should_build
def test_should_build():
    assert not should_build()
    config["upload_to_pypi"] = True
    assert should_build()
    config["build_command"] = False
    assert not should_build()
    config["upload_to_pypi"] = False
    config["build_command"] = True
    assert not should_build()
    config["upload_to_release"] = True
    assert should_build()
    config["upload_to_release"] = False
    config["upload_to_pypi"] = True
    assert should_build()

# Generated at 2022-06-14 05:02:06.360670
# Unit test for function should_build
def test_should_build():
    assert should_build()

# Generated at 2022-06-14 05:02:07.692468
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is True

# Generated at 2022-06-14 05:02:09.346681
# Unit test for function should_build
def test_should_build():
    assert should_build()



# Generated at 2022-06-14 05:05:38.396625
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True

# Generated at 2022-06-14 05:05:45.910701
# Unit test for function should_build
def test_should_build():
    config["upload_release"] = True
    config["upload_pypi"] = True
    config["build_command"] = "python setup.py sdist"
    assert should_build()
    config[
        "build_command"
    ] = "false"  # Test that "false" will not raise a build
    assert not should_build()
    config["upload_release"] = False
    assert not should_build()
    config["upload_release"] = True
    config["upload_pypi"] = False
    assert should_build()

# Generated at 2022-06-14 05:05:53.002910
# Unit test for function should_build
def test_should_build():
    build_command = "echo build"
    assert should_build() is False
    config["build_command"] = build_command
    assert should_build() is False
    config["upload_to_pypi"] = True
    assert should_build() is True
    config["upload_to_pypi"] = False
    assert should_build() is False
    config["upload_to_release"] = True
    assert should_build() is True
    config["upload_to_release"] = False
    assert should_build() is False
    config["build_command"] = False
    assert should_build() is False

# Generated at 2022-06-14 05:06:00.449605
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["build_command"] = "echo 'Beware of the leopard'"
    assert should_remove_dist() is False

    config["remove_dist"] = "true"
    assert should_remove_dist() is False

    config["upload_to_release"] = "true"
    assert should_remove_dist() is True

    config["upload_to_release"] = "false"
    config["upload_to_pypi"] = "true"
    assert should_remove_dist() is True

# Generated at 2022-06-14 05:06:06.122369
# Unit test for function should_build
def test_should_build():
    """Test the should_build function.
    """
    config.set("upload_to_pypi", True)
    assert should_build()

    config.set("upload_to_release", True)
    assert should_build()

    config.set("upload_to_other", True)
    assert not should_build()

    config.set("upload_to_pypi", False)
    config.set("upload_to_release", False)
    assert not should_build()

# Generated at 2022-06-14 05:06:16.740831
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("upload_to_release", True)
    config.set("build_command", "echo test")
    assert should_remove_dist()
    config.set("upload_to_release", False)
    config.set("upload_to_pypi", True)
    assert should_remove_dist()
    config.set("upload_to_pypi", False)
    config.set("build_command", "false")
    assert not should_remove_dist()
    config.set("upload_to_pypi", True)
    config.set("build_command", "false")
    assert not should_remove_dist()
    config.set("build_command", "echo test")
    config.set("upload_to_pypi", False)
    assert not should_remove_dist()

# Generated at 2022-06-14 05:06:24.743095
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = False
    assert not should_build()

    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = "sdist"
    assert should_build()

    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["build_command"] = "sdist"
    assert should_build()

# Generated at 2022-06-14 05:06:28.325377
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("remove_dist", "true")
    config.set("upload_to_pypi", "true")
    config.set("upload_to_release", "true")
    assert should_remove_dist()

# Generated at 2022-06-14 05:06:39.850489
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = True
    config["remove_dist"] = True
    assert should_remove_dist() == True

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["build_command"] = True
    config["remove_dist"] = True
    assert should_remove_dist() == True

    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["build_command"] = True
    config["remove_dist"] = True
    assert should_remove_dist() == True

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config

# Generated at 2022-06-14 05:06:41.217893
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is True
