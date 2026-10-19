

# Generated at 2022-06-14 04:59:35.833744
# Unit test for function should_build
def test_should_build():
    assert should_build()
    config["upload_to_pypi"] = "false"
    assert should_build()
    config["upload_to_release"] = "false"
    assert not should_build()
    config["build_command"] = "false"
    assert not should_build()

# Generated at 2022-06-14 04:59:39.384834
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = "false"
    assert not should_build()
    config["upload_to_pypi"] = True
    assert should_build()
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_build()
    config["upload_to_release"] = False
    config["build_command"] = "true"
    assert should_build()



# Generated at 2022-06-14 04:59:50.015795
# Unit test for function should_build
def test_should_build():
    assert should_build() == False

    config["upload_to_pypi"] = "true"
    assert should_build() == True

    config["upload_to_pypi"] = "false"
    assert should_build() == False

    config["upload_to_pypi"] = ""
    assert should_build() == False

    config["upload_to_release"] = "true"
    assert should_build() == True

    config["upload_to_release"] = ""
    assert should_build() == False

    config["build_command"] = "true"
    assert should_build() == False

    config["build_command"] = "false"
    assert should_build() == False

    config["build_command"] = "pwd"
    assert should_build() == True

# Generated at 2022-06-14 04:59:56.142273
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["build_command"] = "false"
    config["upload_to_release"] = False
    config["upload_to_pypi"] = False
    config["remove_dist"] = False
    assert not should_remove_dist()
    config["build_command"] = "bla"
    config["upload_to_release"] = True
    assert should_remove_dist()
    config["build_command"] = False
    config["upload_to_release"] = True
    assert not should_remove_dist()

# Generated at 2022-06-14 04:59:57.638379
# Unit test for function should_build
def test_should_build():
    assert should_build() == True

# Generated at 2022-06-14 05:00:00.062198
# Unit test for function should_build
def test_should_build():
    # build
    assert should_build()
    # do not build
    config.set("upload_to_pypi", False)
    config.set("upload_to_release", False)
    assert not should_build()

# Generated at 2022-06-14 05:00:01.173756
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is True

# Generated at 2022-06-14 05:00:04.122385
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False
    assert should_remove_dist("dist-newstyle/") == True

# Generated at 2022-06-14 05:00:05.782170
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True, "Should remove_dist"

# Generated at 2022-06-14 05:00:12.808681
# Unit test for function should_build
def test_should_build():
    ''' Test for should build condition'''
    config = {'build_command': 'false', 'remove_dist': True, 'upload_to_pypi': True, 'upload_to_release': False}
    assert not should_build()
    config = {'build_command': 'build', 'remove_dist': True, 'upload_to_pypi': False, 'upload_to_release': True}
    assert should_build()

# Generated at 2022-06-14 05:02:13.701810
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = "python setup.py sdist bdist_wheel"

    assert should_remove_dist()

    config["remove_dist"] = False
    assert not should_remove_dist()

# Generated at 2022-06-14 05:02:15.416855
# Unit test for function should_remove_dist
def test_should_remove_dist():
     config.set("remove_dist", "true")
     assert should_remove_dist()

# Generated at 2022-06-14 05:02:16.606641
# Unit test for function should_build
def test_should_build():
    assert should_build() == True



# Generated at 2022-06-14 05:02:17.760700
# Unit test for function should_build
def test_should_build():
    assert should_build() == True

# Generated at 2022-06-14 05:02:18.915339
# Unit test for function should_build
def test_should_build():
    assert should_build() == True



# Generated at 2022-06-14 05:02:19.491314
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True

# Generated at 2022-06-14 05:02:25.185282
# Unit test for function should_build
def test_should_build():
    assert not should_build(), "Should not build dist (default)"

    config["upload_to_release"] = True
    assert not should_build(), "Should not build dist (no command)"

    config["build_command"] = "echo 'foo'"
    assert should_build(), "Should build dist (release)"

    del config["upload_to_release"]
    config["upload_to_pypi"] = True
    assert should_build(), "Should build dist (pypi)"

    del config["upload_to_pypi"]
    config["build_command"] = "false"
    assert not should_build(), "Should not build dist (command false)"


# Generated at 2022-06-14 05:02:33.155881
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["build_command"] = "false"
    config["remove_dist"] = "true"
    assert should_remove_dist() is False
    config["build_command"] = "python setup.py sdist"
    config["remove_dist"] = "true"
    assert should_remove_dist() is True
    config["build_command"] = "false"
    config["remove_dist"] = "false"
    assert should_remove_dist() is False

# Generated at 2022-06-14 05:02:40.064446
# Unit test for function should_build
def test_should_build():
    assert should_build() is False

    config["upload_to_pypi"] = True
    assert should_build() is True

    config["upload_to_pypi"] = False
    assert should_build() is False

    config["upload_to_release"] = True
    assert should_build() is True

    config["upload_to_release"] = False
    assert should_build() is False

    config["build_command"] = True
    assert should_build() is True


# Generated at 2022-06-14 05:02:41.198478
# Unit test for function should_build
def test_should_build():
    assert should_build() == True

# Generated at 2022-06-14 05:06:39.951450
# Unit test for function should_build
def test_should_build():
    _config = {
        "upload_to_pypi": True,
        "upload_to_release": True,
        "build_command": "build command whatever",
    }
    assert should_build(config=_config) is True

    _config = {
        "upload_to_pypi": False,
        "upload_to_release": True,
        "build_command": "build command whatever",
    }
    assert should_build(config=_config) is True

    _config = {
        "upload_to_pypi": True,
        "upload_to_release": False,
        "build_command": "build command whatever",
    }
    assert should_build(config=_config) is True

    # here build_command is false

# Generated at 2022-06-14 05:06:40.700900
# Unit test for function should_build
def test_should_build():
    assert should_build() == True



# Generated at 2022-06-14 05:06:49.782208
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["remove_dist"] = True
    assert should_remove_dist() == True

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["remove_dist"] = True
    assert should_remove_dist() == True

    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["remove_dist"] = True
    assert should_remove_dist() == True

    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["remove_dist"] = True
    assert should_remove_dist() == False

    config["upload_to_pypi"]

# Generated at 2022-06-14 05:06:54.371028
# Unit test for function should_build
def test_should_build():
    assert should_build() is True
    assert config['build_command'] is not "false"
    assert config['upload_to_pypi'] is True or config['upload_to_release'] is True

if __name__ == "__main__":
    test_should_build()

# Generated at 2022-06-14 05:07:07.266927
# Unit test for function should_build
def test_should_build():
    assert should_build() == False

    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["build_command"] = "false"
    assert should_build() == False

    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["build_command"] = "setup.py sdist"
    assert should_build() == True

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["build_command"] = "setup.py sdist"
    assert should_build() == True

    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = "setup.py sdist"

# Generated at 2022-06-14 05:07:17.681301
# Unit test for function should_remove_dist
def test_should_remove_dist():
    build_command = True
    upload = True
    remove_dist = True
    assert should_remove_dist()

    build_command = True
    upload = False
    remove_dist = True
    assert should_remove_dist()

    build_command = True
    upload = False
    remove_dist = False
    assert should_remove_dist()

    build_command = False
    upload = True
    remove_dist = True
    assert should_remove_dist()

    build_command = False
    upload = False
    remove_dist = True
    assert should_remove_dist()

    build_command = False
    upload = True
    remove_dist = False
    assert should_remove_dist()

    build_command = True
    upload = True
    remove_dist = False
    assert should_remove_dist()

# Generated at 2022-06-14 05:07:18.525335
# Unit test for function should_build
def test_should_build():
    assert should_build()



# Generated at 2022-06-14 05:07:20.950997
# Unit test for function should_build
def test_should_build():
    assert should_build() is False
    config["upload_to_pypi"] = "true"
    config["upload_to_release"] = "false"
    assert should_build() is True
    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = "true"
    assert should_build() is True

# Generated at 2022-06-14 05:07:26.982037
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is False

    config.update({"build_command": "false"})
    assert should_remove_dist() is False

    config.update({"build_command": "some"})
    assert should_remove_dist() is False

    config.update({"build_command": "some", "remove_dist": "false"})
    assert should_remove_dist() is False

    config.update({"build_command": "some", "remove_dist": "true"})
    assert should_remove_dist() is True

# Generated at 2022-06-14 05:07:35.481844
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set_keys({"remove_dist": False})
    assert should_remove_dist() == False
    config.set_keys({"remove_dist": True})
    assert should_remove_dist() == True
    config.set_keys({"remove_dist": False, "build_command": False})
    assert should_remove_dist() == False
    config.set_keys({"remove_dist": True, "build_command": False})
    assert should_remove_dist() == False
