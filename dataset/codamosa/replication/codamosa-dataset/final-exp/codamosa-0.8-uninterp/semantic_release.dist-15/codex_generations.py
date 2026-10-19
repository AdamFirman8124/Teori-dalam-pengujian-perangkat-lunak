

# Generated at 2022-06-14 04:59:29.121937
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = False
    assert not should_build()

    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = True
    assert should_build()

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["build_command"] = True
    assert should_build()

    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["build_command"] = True
    assert should_build()



# Generated at 2022-06-14 04:59:30.968751
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert not should_remove_dist()

# Generated at 2022-06-14 04:59:35.334522
# Unit test for function should_build
def test_should_build():
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", False)
    config.set("build_command", "foobar")

    assert should_build()
    config.set("upload_to_pypi", False)
    assert should_build()
    config.set("upload_to_release", False)
    config.set("build_command", False)
    assert not should_build()



# Generated at 2022-06-14 04:59:41.986900
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False
    config["remove_dist"] = False
    assert should_remove_dist() == False
    config["remove_dist"] = True
    assert should_remove_dist() == False
    config["upload_to_pypi"] = True
    assert should_remove_dist() == True
    config["remove_dist"] = False
    config["upload_to_release"] = True
    assert should_remove_dist() == True

# Generated at 2022-06-14 04:59:49.373304
# Unit test for function should_build
def test_should_build():
    assert should_build() == False
    assert should_remove_dist() == False
    assert should_build({'upload_to_pypi': 'yes', 'build_command': 'setup build'}) == True
    assert should_remove_dist({'remove_dist': 'yes', 'upload_to_pypi': 'yes', 'build_command': 'setup build'}) == True
    assert should_build({'upload_to_pypi': 'no', 'build_command': 'setup build'}) == False
    assert should_build({'upload_to_pypi': 'yes', 'build_command': 'false'}) == False

# Generated at 2022-06-14 04:59:52.804504
# Unit test for function should_build
def test_should_build():
    config.set("upload_to_pypi", "true")
    config.set("upload_to_release", "true")
    config.set("build_command", "something")

    assert should_build()



# Generated at 2022-06-14 04:59:57.149309
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("remove_dist", True)
    assert should_remove_dist() == True
    config.set("remove_dist", False)
    assert should_remove_dist() == False

# Unit tests for function should_build

# Generated at 2022-06-14 04:59:58.315035
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True

# Generated at 2022-06-14 04:59:59.478577
# Unit test for function should_build
def test_should_build():
    assert should_build() == True


# Generated at 2022-06-14 05:00:00.802510
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True

# Generated at 2022-06-14 05:03:28.016737
# Unit test for function should_build
def test_should_build():
    assert should_build()



# Generated at 2022-06-14 05:03:28.968308
# Unit test for function should_build
def test_should_build():
    assert should_build() is True

# Generated at 2022-06-14 05:03:38.475185
# Unit test for function should_build
def test_should_build():
    for command in [False, "false", None]:
        for upload_pypi in [False, "false", None]:
            for upload_release in [False, "false", None]:
                assert not should_build(
                    upload_pypi=upload_pypi,
                    upload_release=upload_release,
                    build_command=command
                )
    assert should_build(
        build_command="python setup.py sdist"
    )
    assert should_build(
        build_command="python setup.py sdist",
        upload_pypi=False,
        upload_release=True
    )



# Generated at 2022-06-14 05:03:41.963681
# Unit test for function should_build
def test_should_build():
    # Arrange
    config._settings = {
        "build_command": "false",
        "upload_to_pypi": False,
        "upload_to_release": False,
    }

    # Act
    build = should_build()

    # Assert
    assert build is False


# Generated at 2022-06-14 05:03:42.934283
# Unit test for function should_build
def test_should_build():
    assert should_build() is False


# Generated at 2022-06-14 05:03:56.323631
# Unit test for function should_remove_dist
def test_should_remove_dist():
    """
    Test should_remove_dist with two false values and one true.
    """
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["remove_dist"] = False
    assert should_remove_dist() == False
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["remove_dist"] = True
    assert should_remove_dist() == False
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["remove_dist"] = False
    assert should_remove_dist() == False
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["remove_dist"] = True


# Generated at 2022-06-14 05:04:02.172458
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    config["build_command"] = "command"
    config["upload_to_release"] = True
    assert should_remove_dist()
    config["remove_dist"] = True
    config["build_command"] = "command"
    config["upload_to_pypi"] = True
    assert should_remove_dist()
    config["remove_dist"] = True
    config["build_command"] = "command"
    config["upload_to_release"] = False
    assert should_remove_dist()

# Generated at 2022-06-14 05:04:03.297124
# Unit test for function should_build
def test_should_build():
    assert should_build() == False

# Generated at 2022-06-14 05:04:07.268974
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert not should_remove_dist()

    config["build_command"] = "python setup.py sdist bdist_wheel"
    assert not should_remove_dist()

    config["remove_dist"] = "true"
    assert should_remove_dist()

# Generated at 2022-06-14 05:04:09.842763
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.update({"upload_to_pypi": False, "upload_to_release": True})
    assert should_remove_dist()