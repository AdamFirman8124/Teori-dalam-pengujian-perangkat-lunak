

# Generated at 2022-06-14 04:59:16.381036
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist()

# Generated at 2022-06-14 04:59:17.490805
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True

# Generated at 2022-06-14 04:59:23.806373
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    config["upload_to_pypi"] = True
    assert should_remove_dist()
    config["remove_dist"] = True
    config["upload_to_release"] = True
    assert should_remove_dist()
    config["remove_dist"] = True
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    assert not should_remove_dist()

# Generated at 2022-06-14 04:59:26.318349
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_build()
    assert should_remove_dist()



# Generated at 2022-06-14 04:59:27.341029
# Unit test for function should_build
def test_should_build():
    assert should_build() == False

# Generated at 2022-06-14 04:59:30.018908
# Unit test for function should_build
def test_should_build():
    assert should_build() is False
    config.update({'build_command': "build", 'upload_to_pypi': True})
    assert should_build() is True
    config.update({'build_command': "build", 'upload_to_release': True})
    assert should_build() is True



# Generated at 2022-06-14 04:59:32.404281
# Unit test for function should_build
def test_should_build():
    assert should_build() is True, "The setting `build_command` is required"


# Generated at 2022-06-14 04:59:36.721863
# Unit test for function should_build
def test_should_build():
    assert should_build() == False
    config["build_command"]  = "touch dist/foo.tar.gz"
    assert should_build() == False
    config["upload_to_pypi"] = True
    assert should_build() == True
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_build() == True
    config["upload_to_release"] = False
    config["build_command"] = False
    assert should_build() == False

# Generated at 2022-06-14 04:59:44.476525
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config['build_command'] = 'test'
    config['remove_dist'] = "true"
    assert should_remove_dist() is True
    config['build_command'] = 'false'
    config['remove_dist'] = "true"
    assert should_remove_dist() is False
    config['build_command'] = 'test'
    config['remove_dist'] = "false"
    assert should_remove_dist() is False
    config['build_command'] = 'false'
    config['remove_dist'] = "false"
    assert should_remove_dist() is False



# Generated at 2022-06-14 04:59:55.215100
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = True
    assert should_remove_dist()

    config["remove_dist"] = False
    assert not should_remove_dist()

    config["remove_dist"] = True
    config["upload_to_pypi"] = False
    assert not should_remove_dist()

    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = False
    assert not should_remove_dist()

# Generated at 2022-06-14 05:01:35.791406
# Unit test for function should_build
def test_should_build():
    assert should_build()



# Generated at 2022-06-14 05:01:42.706043
# Unit test for function should_build
def test_should_build():
    assert should_build() is False

    # pypi=true
    config["upload_to_pypi"] = True
    assert should_build() is False

    # release=true
    config["upload_to_release"] = True
    assert should_build() is False

    # build_command=true
    config["build_command"] = "true"
    assert should_build() is True



# Generated at 2022-06-14 05:01:52.086447
# Unit test for function should_build
def test_should_build():
    config_for_upload_to_pypi = {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "sphinx-build docs docs/_build",
    }
    config_for_upload_to_release = {
        "upload_to_pypi": False,
        "upload_to_release": True,
        "build_command": "sphinx-build docs docs/_build",
    }
    config_for_upload_to_pypi_and_release = {
        "upload_to_pypi": True,
        "upload_to_release": True,
        "build_command": "sphinx-build docs docs/_build",
    }

# Generated at 2022-06-14 05:01:55.949037
# Unit test for function should_build
def test_should_build():
    from .. import utils
    from invoke import Dict
    config = Dict(
        build_command="make",
        upload_to_pypi=True,
        upload_to_release=False
    )
    assert utils.should_build(config)

    config = Dict(
        build_command="make",
        upload_to_pypi=False,
        upload_to_release=True
    )
    assert utils.should_build(config)

# Generated at 2022-06-14 05:02:05.928785
# Unit test for function should_build
def test_should_build():
    # test good config
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = "ls"
    assert should_build()

    # test false for no command
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = "false"
    assert not should_build()

    # test false for no upload
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = "ls"
    assert not should_build()



# Generated at 2022-06-14 05:02:19.375831
# Unit test for function should_build
def test_should_build():
    # upload to pypi is true, upload to release is true
    assert should_build({"upload_to_pypi": True, "upload_to_release": True, "build_command": "setup.py sdist bdist_wheel"})
    # upload to pypi is true, upload to release is false
    assert should_build({"upload_to_pypi": True, "upload_to_release": False, "build_command": "setup.py sdist bdist_wheel"})
    # upload to pypi is false, upload to release is true
    assert should_build({"upload_to_pypi": False, "upload_to_release": True, "build_command": "setup.py sdist bdist_wheel"})
    # upload to pypi is false, upload to release is false

# Generated at 2022-06-14 05:02:22.820756
# Unit test for function should_build
def test_should_build():
    assert should_build() is False
    config.set("upload_to_release", True)
    config.set("build_command", "setup.py sdist")
    assert should_build() is True
    config.set("upload_to_release", False)
    assert should_build() is False



# Generated at 2022-06-14 05:02:23.891925
# Unit test for function should_build
def test_should_build():
    assert should_build() == False

# Generated at 2022-06-14 05:02:34.288690
# Unit test for function should_build
def test_should_build():
    assert should_build() is False
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = "false"
    assert should_build() is False
    config["upload_to_pypi"] = True
    assert should_build() is True
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_build() is True
    config["upload_to_release"] = False
    config["build_command"] = "ls"
    assert should_build() is True

# Generated at 2022-06-14 05:02:42.499259
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = False
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["build_command"] = "echo 'Hello World'"
    assert should_remove_dist() is False

    config["remove_dist"] = True
    assert should_remove_dist() is True

    config["remove_dist"] = False
    assert should_remove_dist() is False

    config["upload_to_pypi"] = False
    assert should_remove_dist() is False

    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    assert should_remove_dist() is False

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_remove_dist

# Generated at 2022-06-14 05:04:33.714230
# Unit test for function should_build
def test_should_build():
    assert not should_build()
    config.update({"upload_to_pypi": False, "build_command": "false"})
    assert not should_build()
    config.update({"upload_to_pypi": False, "build_command": "echo ok"})
    assert not should_build()
    config.update({"upload_to_pypi": True, "build_command": "false"})
    assert should_build()
    config.update({"upload_to_pypi": False, "upload_to_release": True})
    assert should_build()
    config.update({"upload_to_pypi": False, "upload_to_release": False})
    assert not should_build()

# Generated at 2022-06-14 05:04:42.290754
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = 1
    assert should_remove_dist() is True, "Should return true as remove_dist is set to 1"
    config["remove_dist"] = "1"
    assert should_remove_dist() is True, "Should return true as remove_dist is set to 1"
    config["remove_dist"] = 0
    assert should_remove_dist() is False, "Should return true as remove_dist is set to 0"
    config["remove_dist"] = "0"
    assert should_remove_dist() is False, "Should return true as remove_dist is set to 0"

# Generated at 2022-06-14 05:04:43.652328
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True


# Generated at 2022-06-14 05:04:44.679490
# Unit test for function should_build
def test_should_build():
    assert not should_build() == True


# Generated at 2022-06-14 05:04:46.620099
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert not should_remove_dist()

# Generated at 2022-06-14 05:04:51.582527
# Unit test for function should_build
def test_should_build():
    settings = {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "make build",
        "remove_dist": True,
    }
    config.update(settings)
    assert should_build() is True

# Generated at 2022-06-14 05:04:58.203569
# Unit test for function should_build
def test_should_build():
    config.set_section("upload_to_pypi", True)
    config.set_section("upload_to_release", True)
    config.set_section("build_command", "true")
    assert should_build() is True

    config.set_section("upload_to_release", False)
    assert should_build() is True

    config.set_section("build_command", "false")
    assert should_build() is False



# Generated at 2022-06-14 05:05:09.381902
# Unit test for function should_build
def test_should_build():
    # using data from tests/data/settings.toml

    # build_command=true, but upload_to_pypi is not set, therefore should be false
    assert should_build() == False
    return

    # build_command=false, but upload_to_pypi is set, therefore should be false
    assert should_build() == False
    return
    
    # build_command=true, and upload_to_pypi=true, therefore should be true
    assert should_build() == True
    return

    # build_command=true, and upload_to_release=true, therefore should be true
    assert should_build() == True
    return

    # build_command=true, upload_to_pypi is not set, and upload_to_release=true, therefore should be true

# Generated at 2022-06-14 05:05:10.990079
# Unit test for function should_build
def test_should_build():
    result = should_build()
    assert result == True



# Generated at 2022-06-14 05:05:14.447638
# Unit test for function should_build
def test_should_build():
    build_command = "python setup.py sdist"
    upload_pypi = True
    upload_release = True
    assert should_build() == True
    config.set({"build_command": "false"})
    assert should_build() == False