

# Generated at 2022-06-14 04:59:33.513361
# Unit test for function should_build
def test_should_build():
    def _config(upload_to_pypi=None, upload_to_release=None, build_command=None):
        config["upload_to_pypi"] = upload_to_pypi
        config["upload_to_release"] = upload_to_release
        config["build_command"] = build_command

    _config()
    assert not should_build()

    _config(upload_to_pypi=True, build_command="python setup.py sdist")
    assert should_build()

    _config(upload_to_release=True, build_command="python setup.py sdist")
    assert should_build()

    _config(upload_to_pypi=True, upload_to_release=True, build_command="python setup.py sdist")
    assert should_build()

# Generated at 2022-06-14 04:59:38.826760
# Unit test for function should_remove_dist
def test_should_remove_dist():
    # test if it is false when build command is false
    config.set("build_command", "false")
    assert not should_remove_dist()

    # test if it is false if upload to pypi is False
    config.set("build_command", "python setup.py sdist")
    config.set("upload_to_pypi", False)
    assert not should_remove_dist()

    # test if it is false if upload to release is False
    config.set("upload_to_pypi", True)
    config.set("upload_to_release", False)
    assert not should_remove_dist()

    # test if it is true if everything is True
    config.set("upload_to_release", True)
    assert should_remove_dist()

# Generated at 2022-06-14 04:59:49.955269
# Unit test for function should_build
def test_should_build():
    config["build_command"] = "false"
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    assert not should_build()
    config["build_command"] = "python setup.py sdist bdist_wheel"
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    assert should_build()
    config["build_command"] = "false"
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert not should_build()
    config["build_command"] = "python setup.py sdist bdist_wheel"
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_build()

# Generated at 2022-06-14 04:59:51.348005
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True



# Generated at 2022-06-14 04:59:52.937994
# Unit test for function should_build
def test_should_build():
    assert should_build() == False

# Generated at 2022-06-14 04:59:59.134682
# Unit test for function should_build
def test_should_build():
    build_command = "python setup.py sdist"
    config["build_command"] = build_command
    assert should_build()
    config["build_command"] = False
    assert not should_build()
    config["upload_to_pypi"] = False
    assert not should_build()
    config["upload_to_release"] = True
    assert should_build()



# Generated at 2022-06-14 05:00:06.095544
# Unit test for function should_build
def test_should_build():
    assert should_build() == False
    config["upload_to_pypi"] = True
    assert should_build() == True
    config["upload_to_pypi"] = False
    assert should_build() == False
    config["upload_to_release"] = True
    assert should_build() == True
    config["upload_to_release"] = False
    assert should_build() == False
    config["build_command"] = "true"
    assert should_build() == True
    config["build_command"] = True
    assert should_build() == True


# Generated at 2022-06-14 05:00:16.955981
# Unit test for function should_build
def test_should_build():
    assert not should_build()
    config["build_command"] = "echo hello"
    assert should_build()
    config["build_command"] = "false"
    assert not should_build()
    config["build_command"] = "echo hello"
    config["upload_to_pypi"] = "true"
    assert should_build()
    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = "true"
    assert should_build()
    config["upload_to_pypi"] = "true"
    assert should_build()
    config["upload_to_release"] = "false"
    assert should_build()


if __name__ == "__main__":
    test_should_build()

# Generated at 2022-06-14 05:00:18.242456
# Unit test for function should_build
def test_should_build():
    assert should_build() == True


# Generated at 2022-06-14 05:00:27.949058
# Unit test for function should_build
def test_should_build():
    from .settings import config
    assert should_build() is False
    config["upload_to_pypi"] = True
    config["build_command"] = "test_command"
    assert should_build() is True
    config["upload_to_release"] = True
    assert should_build() is True
    config["upload_to_pypi"] = False
    assert should_build() is True
    config.pop("build_command")
    assert should_build() is False
    config["build_command"] = "false"
    assert should_build() is False

# Generated at 2022-06-14 05:02:19.366819
# Unit test for function should_build
def test_should_build():
    # Returns True if the build command exists, and either upload_to_pypi or upload_to_release is set to True
    assert should_build() is False
    config["build_command"] = "build"
    config["upload_to_pypi"] = False
    assert should_build() is False
    config["upload_to_release"] = False
    assert should_build() is False
    config["upload_to_release"] = True
    assert should_build() is True
    config["upload_to_pypi"] = True
    assert should_build() is True
    config["upload_to_pypi"] = False
    assert should_build() is True
    config["build_command"] = "false"
    assert should_build() is False

# Generated at 2022-06-14 05:02:24.563447
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config.set_config({
        "build_command": "python setup.py bdist_wheel",
        "remove_dist": "true",
    })
    assert should_remove_dist() is True
    config.set_config({
        "build_command": "python setup.py bdist_wheel",
        "remove_dist": "false"
    })
    assert should_remove_dist() is False
    config.set_config({
        "build_command": "false",
        "remove_dist": "true"
    })
    assert should_remove_dist() is False

# Generated at 2022-06-14 05:02:28.359709
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is False
    assert should_remove_dist([]) is False
    assert should_remove_dist(None) is True



# Generated at 2022-06-14 05:02:29.794918
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True

# Generated at 2022-06-14 05:02:32.986449
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = False
    assert should_remove_dist() is False
    config["remove_dist"] = True
    assert should_remove_dist() is True

# Generated at 2022-06-14 05:02:37.431975
# Unit test for function should_build
def test_should_build():
    assert should_build() == False
    config.update({"upload_to_pypi": True})
    assert should_build() == False
    config.update({"build_command": "true"})
    assert should_build() == True

# Generated at 2022-06-14 05:02:44.168637
# Unit test for function should_build
def test_should_build():
    config["build_command"] = "false"
    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = "false"
    assert not should_build()

    config["build_command"] = "true"
    assert not should_build()

    config["upload_to_pypi"] = "true"
    assert should_build()

    config["upload_to_pypi"] = "false"
    config["upload_to_release"] = "true"
    assert should_build()

    config["build_command"] = "false"
    assert not should_build()



# Generated at 2022-06-14 05:02:45.838606
# Unit test for function should_build
def test_should_build():
    assert should_build() == False
    # assert should_build(config) == True

# Generated at 2022-06-14 05:02:53.051786
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["remove_dist"] = True
    # When we should build, this should be true
    config["build_command"] = 'dummy_command'
    assert should_remove_dist()
    # But not when we shouldn't
    config["build_command"] = 'false'
    assert not should_remove_dist()
    # When we should remove, but should not build
    config["build_command"] = 'false'
    assert not should_remove_dist()

# Generated at 2022-06-14 05:02:54.513738
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert(should_remove_dist()) == True

# Generated at 2022-06-14 05:04:35.932114
# Unit test for function should_build
def test_should_build():
    assert should_build() is True


# Generated at 2022-06-14 05:04:44.920223
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = True
    assert should_build()

    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_build()

    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    assert not should_build()

    config["build_command"] = ""
    config["upload_to_pypi"] = True
    assert not should_build()

    config["build_command"] = "false"
    config["upload_to_pypi"] = True
    assert not should_build()

    config["build_command"] = False
    config["upload_to_pypi"] = True
    assert not should_build()


# Generated at 2022-06-14 05:04:56.555435
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = True
    assert should_build()
    config["upload_to_pypi"] = False
    assert not should_build()
    config["upload_to_release"] = True
    assert should_build()
    config["upload_to_release"] = False
    assert not should_build()
    config["build_command"] = "echo true"
    assert should_build()
    config["build_command"] = "false"
    assert not should_build()
    config["build_command"] = "false"
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    assert not should_build()



# Generated at 2022-06-14 05:05:00.155961
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True
    config["remove_dist"] = True
    config["upload_to_pypi"] = True
    config["build_command"] = "setup build"
    assert should_remove_dist() == True

# Generated at 2022-06-14 05:05:01.089153
# Unit test for function should_remove_dist
def test_should_remove_dist():
    logger.debug(should_remove_dist())

# Generated at 2022-06-14 05:05:02.025933
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:05:04.089303
# Unit test for function should_build
def test_should_build():
    assert should_build()



# Generated at 2022-06-14 05:05:11.687513
# Unit test for function should_build
def test_should_build():
    config.reload(data={
        "upload_to_pypi": True,
    })
    assert should_build() == True
    config.reload(data={
        "upload_to_pypi": False,
    }),
    assert should_build() == False
    config.reload(data={
        "upload_to_pypi": True,
        "build_command": "false",
    })
    assert should_build() == False

# Generated at 2022-06-14 05:05:12.712737
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist()



# Generated at 2022-06-14 05:05:16.926763
# Unit test for function should_remove_dist
def test_should_remove_dist():
    import pytest
    from ..config import Settings
    config = Settings()
    config._Settings__data = {"build_command": "false",
                              "remove_dist": "true"}
    assert should_remove_dist() is False
    config._Settings__data = {"build_command": "build",
                              "remove_dist": "true"}
    assert should_remove_dist() is True