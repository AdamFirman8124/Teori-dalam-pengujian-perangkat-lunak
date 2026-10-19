

# Generated at 2022-06-14 04:59:26.051009
# Unit test for function should_build
def test_should_build():
    assert should_build() == True


# Generated at 2022-06-14 04:59:27.005048
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True

# Generated at 2022-06-14 04:59:32.481391
# Unit test for function should_build
def test_should_build():
    build_command = "python setup.py sdist bdist_wheel"
    assert should_build() == False
    config["build_command"] = build_command
    assert should_build() == False
    config["upload_to_pypi"] = True
    assert should_build() == True
    del config["upload_to_pypi"]
    config["upload_to_release"] = True
    assert should_build() == True

# Generated at 2022-06-14 04:59:43.944923
# Unit test for function should_build
def test_should_build():
    config_dict = {
        "upload_to_pypi": True,
        "upload_to_release": True,
        "build_command": "tox",
    }
    config.update(config_dict)
    assert should_build() is True, "Should build dists"

    config_dict = {
        "upload_to_pypi": False,
        "upload_to_release": False,
        "build_command": "tox",
    }
    config.update(config_dict)
    assert should_build() is False, "Should not build dists"

    config_dict = {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "tox",
    }
    config.update(config_dict)
   

# Generated at 2022-06-14 04:59:51.448468
# Unit test for function should_build
def test_should_build():
    assert should_build() is False
    config["build_command"] = True
    assert should_build() is False
    config["upload_to_release"] = True
    assert should_build() is True
    config["build_command"] = "true"
    assert should_build() is True
    config["build_command"] = "false"
    assert should_build() is False



# Generated at 2022-06-14 04:59:54.588087
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = "true"
    config["upload_to_release"] = "false"
    config["build_command"] = "true"

    assert should_build() == True



# Generated at 2022-06-14 04:59:55.791718
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False

# Generated at 2022-06-14 04:59:58.243089
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert not should_remove_dist()

# Generated at 2022-06-14 05:00:03.326226
# Unit test for function should_build
def test_should_build():
    config["build_command"] = "bdist_wheel"
    assert should_build()
    config["build_command"] = False
    assert not should_build()
    config["build_command"] = "bdist_wheel"
    config["upload_to_pypi"] = False
    assert not should_build()
    config["upload_to_pypi"] = True
    assert should_build()
    config["build_command"] = False
    config["upload_to_pypi"] = False
    assert not should_build()

# Generated at 2022-06-14 05:00:15.601871
# Unit test for function should_build
def test_should_build():
    config.set("build_command", "false")
    config.set("upload_to_pypi", False)
    config.set("upload_to_release", False)
    assert not should_build()

    config.set("build_command", "false")
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", True)
    assert not should_build()

    config.set("build_command", "some command")
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", True)
    assert should_build()

    config.set("build_command", "false")
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", True)

# Generated at 2022-06-14 05:02:08.586349
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["build_command"] = "false"
    assert should_build() == False
    config["upload_to_pypi"] = True
    assert should_build() == True
    config["build_command"] = "rm -rf ./*"
    assert should_build() == True
    config["upload_to_release"] = False
    assert should_build() == True


# Generated at 2022-06-14 05:02:13.523625
# Unit test for function should_build
def test_should_build():
    config.update({"upload_to_pypi": True,
                   "upload_to_release": False,
                   "build_command": "sphinx-build docs docs/build"})
    assert should_build() is True


# Generated at 2022-06-14 05:02:17.587353
# Unit test for function should_build
def test_should_build():
    config['build_command'] = "sphinx-build -b html docs/sphinx/source dist/docs"
    assert should_build()
    config.pop("build_command")
    assert not should_build()

# Generated at 2022-06-14 05:02:19.714231
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False
    config["remove_dist"] = True
    assert should_remove_dist() == False
    config["build_command"] = "build"
    assert should_remove_dist() == True



# Generated at 2022-06-14 05:02:25.951251
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = "true"
    config["upload_to_pypi"] = "true"
    assert should_remove_dist() is True
    # Turn off upload to pypi and test again
    config["upload_to_pypi"] = "false"
    assert should_remove_dist() is False
    config["upload_to_release"] = "true"
    assert should_remove_dist() is True
    config["upload_to_release"] = "false"
    assert should_remove_dist() is False
    # turn it back on
    config["upload_to_pypi"] = "true"
    assert should_remove_dist() is True
    # Turn off dist removal and test
    config["remove_dist"] = "false"
    assert should_remove_dist() is False

# Generated at 2022-06-14 05:02:39.086923
# Unit test for function should_build
def test_should_build():
    # Should return true
    config_true = {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "echo"
    }
    assert should_build(config_true) is True

    # Should return false
    config_false = {
        "upload_to_pypi": False,
        "upload_to_release": True,
        "build_command": "echo"
    }
    assert should_build(config_false) is False

    # Should return false
    config_invalid_command = {
        "upload_to_pypi": False,
        "upload_to_release": False,
        "build_command": "invale"
    }
    assert should_build(config_invalid_command) is False

    # Should

# Generated at 2022-06-14 05:02:45.901975
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is False
    config["remove_dist"] = "true"
    assert should_remove_dist() is True
    config["remove_dist"] = "false"
    config["build_command"] = "true"
    assert should_remove_dist() is False
    config["upload_to_pypi"] = "true"
    assert should_remove_dist() is True

# Generated at 2022-06-14 05:02:56.185772
# Unit test for function should_build
def test_should_build():
    assert should_build() == True
    config["build_command"] = "false"
    assert should_build() == False
    config["upload_to_pypi"] = "false"
    assert should_build() == False
    config["upload_to_release"] = "false"
    assert should_build() == False
    config["build_command"] = "sphinx-build -b html ./docs ./docs/_build"
    assert should_build() == True
    config["upload_to_pypi"] = True
    assert should_build() == True
    config["upload_to_release"] = True
    assert should_build() == True

# Generated at 2022-06-14 05:03:09.291799
# Unit test for function should_remove_dist
def test_should_remove_dist():
    """Unit test for function should_remove_dist."""
    # Get original config
    original_config = config.get("remove_dist")

    try:
        config.set("remove_dist", "False")
        assert should_remove_dist() == False

        config.set("remove_dist", "True")
        assert should_remove_dist() == False

        config.set("upload_to_pypi", "True")
        assert should_remove_dist() == True

        config.set("upload_to_release", "True")
        assert should_remove_dist() == True

        config.set("build_command", "")
        assert should_remove_dist() == False

    finally:
        config.set("remove_dist", original_config)
        config.set("upload_to_pypi", "False")
       

# Generated at 2022-06-14 05:03:17.572322
# Unit test for function should_remove_dist
def test_should_remove_dist():
    # remove_dist = true and should_build = true
    remove_dist = True
    should_build = True
    assert should_remove_dist() == True

    # remove_dist = true and should_build = false
    remove_dist = True
    should_build = False
    assert should_remove_dist() == False

    # remove_dist = false and should_build = true
    remove_dist = False
    should_build = True
    assert should_remove_dist() == False

    # remove_dist = false and should_build = false
    remove_dist = False
    should_build = False
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:06:55.375996
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["build_command"] = config.get("build_command")
    config["remove_dist"] = config.get("remove_dist")
    assert should_remove_dist()

# Generated at 2022-06-14 05:06:57.492661
# Unit test for function should_build
def test_should_build():
    assert should_build() == True

# Generated at 2022-06-14 05:06:58.691342
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:07:02.368738
# Unit test for function should_remove_dist
def test_should_remove_dist():
    remove_dist = True
    no_remove_dist = False
    assert should_remove_dist(remove_dist)
    assert not should_remove_dist(no_remove_dist)


# Generated at 2022-06-14 05:07:04.870729
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is True
    config["remove_dist"] = "false"
    assert should_remove_dist() is False

# Generated at 2022-06-14 05:07:07.501555
# Unit test for function should_build
def test_should_build():
    assert should_build() == False
    assert should_remove_dist() == False
    build_dists()

# Generated at 2022-06-14 05:07:09.246681
# Unit test for function should_build
def test_should_build():
    assert should_build() == True, "Should build when values have been given in configuration"

# Generated at 2022-06-14 05:07:18.991416
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["build_command"] = "true"
    assert should_build() == True
    config["upload_to_pypi"] = False
    assert should_build() == True
    config["upload_to_pypi"] = "false"
    assert should_build() == False
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    assert should_build() == True
    config["upload_to_release"] = "false"
    assert should_build() == False
    config["upload_to_pypi"] = False
    assert should_build() == False
    config["build_command"] = False
    assert should_build() == False

# Generated at 2022-06-14 05:07:28.438415
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = "true"
    assert should_build() is True
    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = "true"
    assert should_build() is True
    config["upload_to_pypi"] = "true"
    config["upload_to_release"] = "true"
    assert should_build() is True
    # Inverse
    config["upload_to_pypi"] = "true"
    config["upload_to_release"] = "false"
    config["build_command"] = "false"
    assert should_build() is False
    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = "false"

# Generated at 2022-06-14 05:07:29.559842
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True