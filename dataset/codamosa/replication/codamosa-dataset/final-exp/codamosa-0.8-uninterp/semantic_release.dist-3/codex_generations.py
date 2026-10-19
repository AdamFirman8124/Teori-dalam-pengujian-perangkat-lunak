

# Generated at 2022-06-14 04:59:38.251295
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist()
    assert (should_remove_dist() == True)
    assert (should_remove_dist() == False)


# Generated at 2022-06-14 04:59:39.043324
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True


# Generated at 2022-06-14 04:59:50.105361
# Unit test for function should_remove_dist
def test_should_remove_dist():
    from .settings import config
    # Test 1: When upload_to_pypi is False,
    # remove_dist should be False
    config.upload_to_pypi = False
    assert not should_remove_dist()

    # Test 2: When upload_to_release is False,
    # remove_dist should be False
    config.upload_to_pypi = True
    config.upload_to_release = False
    assert not should_remove_dist()

    # Test 3: When build_command is False
    # remove_dist should be False
    config.upload_to_release = True
    config.build_command = False
    assert not should_remove_dist()

    # Test 4: When all variables are True,
    # remove_dist should be True
    config.build_command = "True"

# Generated at 2022-06-14 05:00:01.889328
# Unit test for function should_build
def test_should_build():
    # Build for pypi upload
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", False)
    config.set("build_command", "true")
    assert should_build()

    # Build for release upload
    config.set("upload_to_pypi", False)
    config.set("upload_to_release", True)
    assert should_build()

    # Build for release and pypi upload
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", True)
    assert should_build()

    # Build for nothing
    config.set("upload_to_pypi", False)
    config.set("upload_to_release", False)
    assert not should_build()

    # Build for

# Generated at 2022-06-14 05:00:08.041506
# Unit test for function should_remove_dist
def test_should_remove_dist():
    remove_dist = {
        "remove_dist": "false",
        "upload_to_pypi": "true",
        "upload_to_release": "false",
        "build_command": "true",
    }
    assert should_remove_dist() == False
    assert should_remove_dist(remove_dist) == True

# Generated at 2022-06-14 05:00:16.923456
# Unit test for function should_remove_dist
def test_should_remove_dist():
    # When remove_dist is not set, should return false
    config.set("remove_dist", None)
    assert not should_remove_dist()

    # When remove_dist is set (to something), should return true
    config.set("remove_dist", "foo")
    assert should_remove_dist()

    # When remove_dist is set to false, should return false
    config.set("remove_dist", "false")
    assert not should_remove_dist()

    # When remove_dist is set to true, should return true
    config.set("remove_dist", "true")
    assert should_remove_dist()



# Generated at 2022-06-14 05:00:18.195276
# Unit test for function should_build
def test_should_build():
    assert should_build()



# Generated at 2022-06-14 05:00:20.007602
# Unit test for function should_build
def test_should_build():
    assert should_build is True

# Generated at 2022-06-14 05:00:25.800905
# Unit test for function should_remove_dist
def test_should_remove_dist():
    env = {"upload_to_pypi": True}
    config.load_dict(env)
    assert should_remove_dist()

    env = {"upload_to_pypi": True, "remove_dist": False}
    config.load_dict(env)
    assert not should_remove_dist()



# Generated at 2022-06-14 05:00:28.914341
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("upload_to_pypi", "true")
    config.set("build_command", "test build command")
    assert should_remove_dist()

# Generated at 2022-06-14 05:04:37.016968
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = True
    assert should_build()

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_build()

    config["upload_to_release"] = False
    config["build_command"] = "false"
    assert not should_build()


# Generated at 2022-06-14 05:04:43.904540
# Unit test for function should_build
def test_should_build():
    config['upload_to_pypi'] = 'true'
    config['upload_to_release'] = 'false'
    config['build_command'] = 'false'
    assert should_build() == False
    config['build_command'] = 'python setup.py sdist'
    assert should_build() == True
    config['build_command'] = 'false'
    config['upload_to_pypi'] = 'false'
    config['upload_to_release'] = 'true'
    assert should_build() == True


# Generated at 2022-06-14 05:04:56.840021
# Unit test for function should_build
def test_should_build():
    config_true_false = [
        {"upload_to_pypi": True, "upload_to_release": False, "build_command": True},
        {"upload_to_pypi": False, "upload_to_release": True, "build_command": True},
        {"upload_to_pypi": True, "upload_to_release": True, "build_command": True},
        {"upload_to_pypi": False, "upload_to_release": False, "build_command": False},
        {"upload_to_pypi": False, "upload_to_release": True, "build_command": False},
        {"upload_to_pypi": True, "upload_to_release": False, "build_command": False},
    ]


# Generated at 2022-06-14 05:04:59.309507
# Unit test for function should_build
def test_should_build():
    assert should_build() == True, "should_build FAILS"
    assert should_remove_dist() == True, "should_remove_dist FAILS"

# Generated at 2022-06-14 05:05:09.895763
# Unit test for function should_build
def test_should_build():
    # Without build command
    assert not should_build()

    config["build_command"] = "do_something"
    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = "false"
    assert not should_build()

    config["upload_to_release"] = "true"
    assert should_build()

    config["upload_to_release"] = "false"
    config["upload_to_pypi"] = "true"
    assert should_build()

    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = "false"
    config["build_command"] = "do_something"
    assert not should_build()

    config["upload_to_release"] = "true"
    assert should_build()

    config

# Generated at 2022-06-14 05:05:18.433809
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set("remove_dist", True)
    config.set("upload_to_pypi", True)
    config.set("build_command", True)
    assert should_remove_dist()

    config.set("remove_dist", True)
    config.set("upload_to_pypi", True)
    config.set("build_command", False)
    assert not should_remove_dist()

    config.set("remove_dist", True)
    config.set("upload_to_pypi", False)
    config.set("build_command", True)
    assert not should_remove_dist()

    config.set("remove_dist", True)
    config.set("upload_to_pypi", False)
    config.set("build_command", False)
    assert not should_remove_dist()



# Generated at 2022-06-14 05:05:19.578812
# Unit test for function should_build
def test_should_build():
    assert should_build() == True


# Generated at 2022-06-14 05:05:26.844830
# Unit test for function should_build
def test_should_build():
    """Test should_build
    """
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = "false"
    assert should_build() is False

    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = True
    config["build_command"] = "echo 'hello' "
    assert should_build() is True



# Generated at 2022-06-14 05:05:28.450756
# Unit test for function should_build
def test_should_build():
    assert should_build() is True


# Generated at 2022-06-14 05:05:31.150684
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    config["upload_to_pypi"] = True
    config["build_command"] = "ls"
    assert should_remove_dist() is True