

# Generated at 2022-06-14 04:59:27.553676
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False



# Generated at 2022-06-14 04:59:28.286531
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert not should_remove_dist()

# Generated at 2022-06-14 04:59:41.250223
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = "true"
    assert should_build()
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["build_command"] = "true"
    assert should_build()
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = "true"
    assert should_build()
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = "false"
    assert not should_build()
    config["upload_to_pypi"] = True

# Generated at 2022-06-14 04:59:50.332417
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("remove_dist", False)
    assert not should_remove_dist()
    config.set("remove_dist", True)
    config.set("build_command", "true")
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", False)
    assert should_remove_dist()
    config.set("upload_to_release", True)
    assert should_remove_dist()
    config.set("upload_to_release", False)
    config.set("upload_to_pypi", False)
    assert not should_remove_dist()
    config.set("build_command", "false")
    assert not should_remove_dist()
    config.set("build_command", "true")
    assert should_remove_dist()



# Generated at 2022-06-14 04:59:59.907951
# Unit test for function should_build
def test_should_build():
    assert should_build() is False
    config.set("remove_dist", "true")
    assert should_build() is False
    config.set("build_command", "false")
    assert should_build() is False
    config.set("build_command", "echo hello")
    assert should_build() is False
    config.set("upload_to_pypi", "true")
    assert should_build() is True
    config.set("upload_to_release", "true")
    assert should_build() is True
    config.set("upload_to_pypi", "false")
    assert should_build() is True
    config.set("upload_to_release", "false")
    assert should_build() is False



# Generated at 2022-06-14 05:00:05.572597
# Unit test for function should_build
def test_should_build():
    should_build_tests = [
        # (upload_pypi, upload_release, build_command, should_build)
        (False, False, "", False),
        (True, False, "", True),
        (False, True, "", True),
        (False, False, "false", False),
        (True, False, "false", True),
        (False, True, "false", True),
        (False, False, "build", True),
        (True, False, "build", True),
        (False, True, "build", True),
    ]
    for upload_pypi, upload_release, build_command, should_build in should_build_tests:
        config.upload_to_pypi = upload_pypi
        config.upload_to_release = upload_release

# Generated at 2022-06-14 05:00:16.923520
# Unit test for function should_build
def test_should_build():
    config.update({"upload_to_pypi": True, "build_command": "echo"})
    assert should_build()

    config.update({"upload_to_pypi": True, "build_command": False})
    assert should_build() is False

    config.update({"upload_to_pypi": False, "build_command": "echo"})
    assert should_build() is False

    config.update({"upload_to_pypi": False, "build_command": False})
    assert should_build() is False

    config.update({"upload_to_release": True, "build_command": "echo"})
    assert should_build()

    config.update({"upload_to_release": True, "build_command": False})
    assert should_build() is False


# Generated at 2022-06-14 05:00:29.973000
# Unit test for function should_build
def test_should_build():
    # test config should not have upload_to_pypi or upload_to_release
    assert not should_build()

    config.update({"build_command": "false"})
    assert not should_build()

    config.update({"build_command": "true"})
    # should_build() should return correct value for only upload_to_pypi
    config.update({"upload_to_pypi": "true"})
    config.update({"upload_to_release": "false"})
    assert should_build()

    # should_build() should return correct value for only upload_to_release
    config.update({"upload_to_pypi": "false"})
    config.update({"upload_to_release": "true"})
    assert should_build()

    # should_build() should return

# Generated at 2022-06-14 05:00:40.637683
# Unit test for function should_build
def test_should_build():
    def test_true():
        true_settings = {"build_command": "foo", "upload_to_release": True}
        assert should_build(true_settings)

    def test_false_no_build_command():
        false_settings = {"upload_to_release": True}
        assert not should_build(false_settings)

    def test_false_no_upload():
        false_settings = {"build_command": "foo"}
        assert not should_build(false_settings)

    def test_false_no_upload_and_no_build_command():
        assert not should_build({})

    test_true()
    test_false_no_build_command()
    test_false_no_upload()
    test_false_no_upload_and_no_build_command()



# Generated at 2022-06-14 05:00:43.644040
# Unit test for function should_build
def test_should_build():
    settings = {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "test",
    }
    settings = config.update_settings(settings)
    settings.freeze()
    should_build()
    assert settings

# Generated at 2022-06-14 05:04:38.601664
# Unit test for function should_build
def test_should_build():
    config["build_command"] = "python setup.py sdist"
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    assert should_build() is True
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    assert should_build() is False
    config["build_command"] = "false"
    assert should_build() is False



# Generated at 2022-06-14 05:04:42.807727
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("build_command", "false")
    assert not should_remove_dist()
    config.set("remove_dist", False)
    assert should_remove_dist()
    config.set("remove_dist", True)
    assert should_remove_dist()

# Generated at 2022-06-14 05:04:43.693495
# Unit test for function should_build
def test_should_build():
    assert should_build()
    assert should_build()

# Generated at 2022-06-14 05:04:45.818113
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["remove_dist"] = True
    assert should_remove_dist() is True

# Generated at 2022-06-14 05:04:53.488801
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = "http://localhost"
    config["build_command"] = "echo 'TEST'"
    assert should_build()
    config["upload_to_pypi"] = False
    config["upload_to_release"] = "http://localhost"
    assert should_build()
    config["upload_to_release"] = None
    config["build_distribution"] = False
    assert not should_build()

# Generated at 2022-06-14 05:04:59.152552
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["build_command"] = "build"
    config["remove_dist"] = "false"
    assert should_remove_dist() == True

    config["remove_dist"] = "true"
    assert should_remove_dist() == True

    config["build_command"] = "false"
    config["remove_dist"] = "true"
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:05:09.861199
# Unit test for function should_remove_dist
def test_should_remove_dist():
    '''Verify that the should_remove_dist function works'''

    default_config = config.copy()

    def test_case(remove_dist, upload_to_pypi, upload_to_release):
        """
        Test a certain configuration of the config parameters.
        """
        config['remove_dist'] = bool(remove_dist)
        config['upload_to_pypi'] = bool(upload_to_pypi)
        config['upload_to_release'] = bool(upload_to_release)
        assert should_remove_dist() == (upload_to_pypi or upload_to_release)

    test_case(1, 1, 1)
    test_case(0, 1, 1)
    test_case(1, 0, 1)
    test_case(1, 1, 0)


# Generated at 2022-06-14 05:05:10.989167
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert not should_remove_dist()



# Generated at 2022-06-14 05:05:17.639115
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config_with_remove = {
        "remove_dist": True,
        "upload_to_pypi": True,
        "upload_to_release": True,
        "build_command": "python setup.py sdist bdist_wheel",
    }

    assert should_remove_dist()
    config.set_dict(config_with_remove)
    assert should_remove_dist()
    config.set_dict({"remove_dist": False})
    assert not should_remove_dist()
    config.set_dict({"upload_to_pypi": False})
    assert not should_remove_dist()
    config.set_dict({"upload_to_release": False})
    assert not should_remove_dist()
    config.set_dict({"build_command": "false"})
    assert not should_

# Generated at 2022-06-14 05:05:19.685285
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is False

