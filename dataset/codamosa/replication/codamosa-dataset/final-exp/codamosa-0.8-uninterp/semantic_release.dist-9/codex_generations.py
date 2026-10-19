

# Generated at 2022-06-14 04:59:26.135013
# Unit test for function should_build
def test_should_build():
    assert should_build() == False

    config["upload_to_pypi"] = True
    assert should_build() == False

    config["upload_to_release"] = True
    assert should_build() == False

    config["build_command"] = "python setup.py sdist"
    assert should_build() == True

# Generated at 2022-06-14 04:59:27.054549
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True

# Generated at 2022-06-14 04:59:28.156180
# Unit test for function should_build
def test_should_build():
    """Test the function should_build
    """
    assert should_build()

# Generated at 2022-06-14 04:59:29.518309
# Unit test for function should_build
def test_should_build():
    assert should_build()



# Generated at 2022-06-14 04:59:42.148258
# Unit test for function should_build
def test_should_build():
    config["build_command"] = "twine upload dist/*"
    # only upload to pypi
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    assert should_build()
    # only upload to release
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    assert should_build()
    # upload to both
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    assert should_build()
    # no upload and no command
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    assert not should_build()
    # no upload but command

# Generated at 2022-06-14 04:59:43.126606
# Unit test for function should_build
def test_should_build():
    assert should_build() == False



# Generated at 2022-06-14 04:59:44.067890
# Unit test for function should_build
def test_should_build():
    assert should_build() == False



# Generated at 2022-06-14 04:59:46.600892
# Unit test for function should_build
def test_should_build():
    assert should_build() == True

# Generated at 2022-06-14 04:59:58.784298
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config['remove_dist'] = True
    config['upload_to_pypi'] = True
    config['upload_to_release'] = False
    config['build_command'] = 'python setup.py sdist'
    assert should_remove_dist() == True
    config['remove_dist'] = False
    assert should_remove_dist() == False
    config['remove_dist'] = True
    config['upload_to_pypi'] = False  # noqa
    config['upload_to_release'] = True
    assert should_remove_dist() == True
    config['upload_to_pypi'] = False  # noqa
    config['upload_to_release'] = False  # noqa
    config['build_command'] = False  # noqa
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:00:08.366905
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    config["build_command"] = "ls -al"
    assert should_build()
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["build_command"] = "ls -al"
    assert should_build()
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True
    config["build_command"] = "ls -al"
    assert should_build()
    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = "ls -al"
    assert not should_build()

# Generated at 2022-06-14 05:02:01.788325
# Unit test for function should_build
def test_should_build():
    import os
    file_path = os.path.dirname(__file__)
    file_name = os.path.join(file_path, "..", "invoke.yaml")
    config.read(file_name)
    assert should_build() == False


# Generated at 2022-06-14 05:02:07.027858
# Unit test for function should_build
def test_should_build():
    config.update({
        "build_command": "echo 'hello'",
        "upload_to_pypi": True,
        "upload_to_release": True,
    })
    assert should_build()

    config.update({
        "upload_to_pypi": False,
        "upload_to_release": False,
    })
    assert not should_build()



# Generated at 2022-06-14 05:02:11.066377
# Unit test for function should_build
def test_should_build():
    assert not should_build()
    config["upload_to_pypi"] = True
    config["build_command"] = "true"
    assert should_build()



# Generated at 2022-06-14 05:02:22.447472
# Unit test for function should_remove_dist
def test_should_remove_dist():
    from .settings import Config
    from .settings import DummyYaml
    test_data = [
        ('true', {'upload_to_release':True, 'upload_to_pypi':False, 'build_command':'blah'}, True),
        ('true', {'upload_to_release':False, 'upload_to_pypi':False, 'build_command':'blah'}, False),
        ('true', {'upload_to_release':False, 'upload_to_pypi':True, 'build_command':None}, False),
        ('true', {'upload_to_release':False, 'upload_to_pypi':True, 'build_command':'false'}, False),
    ]

# Generated at 2022-06-14 05:02:25.109823
# Unit test for function should_build
def test_should_build():
    assert should_build() == config.get("build_command") != "false"
    config["build_command"] = "false"
    assert not should_build()

# Generated at 2022-06-14 05:02:29.679529
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = "true"
    config["upload_to_release"] = "true"
    config["build_command"] = "true"
    assert should_build()



# Generated at 2022-06-14 05:02:31.881968
# Unit test for function should_build
def test_should_build():
    assert should_build() == True

#Unit test for function should_build_return_false

# Generated at 2022-06-14 05:02:41.594199
# Unit test for function should_build
def test_should_build():
    config = {"build_command": "false"}
    assert should_build() == False

    config = {"build_command": "build",
              "upload_to_pypi": False,
              "upload_to_release": False}
    assert should_build() == False

    config = {"build_command": "build",
              "upload_to_pypi": False,
              "upload_to_release": True}
    assert should_build() == True

    config = {"build_command": "build",
              "upload_to_pypi": True,
              "upload_to_release": False}
    assert should_build() == True

    config = {"build_command": "build",
              "upload_to_pypi": True,
              "upload_to_release": True}

# Generated at 2022-06-14 05:02:42.924119
# Unit test for function should_build
def test_should_build():
    assert should_build() == True

# Generated at 2022-06-14 05:02:45.541347
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == False
    assert should_remove_dist() == False
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:04:40.291615
# Unit test for function should_build
def test_should_build():
    # GIVEN
    config["build_command"] = "python setup.py sdist"
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False

    # WHEN
    result = should_build()

    # THEN
    assert result

    # GIVEN
    config["build_command"] = "python setup.py sdist"
    config["upload_to_pypi"] = False
    config["upload_to_release"] = True

    # WHEN
    result = should_build()

    # THEN
    assert result



# Generated at 2022-06-14 05:04:46.635353
# Unit test for function should_build
def test_should_build():
    config["build_command"] = "echo 'hi'"
    assert should_build() is True
    config["upload_to_pypi"] = False
    assert should_build() is False
    config["upload_to_pypi"] = True
    config["upload_to_release"] = False
    assert should_build() is True
    config["upload_to_release"] = True
    config["build_command"] = "false"
    assert should_build() is False
    config["build_command"] = "echo 'hi'"
    assert should_build() is True



# Generated at 2022-06-14 05:04:53.891667
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["upload_to_pypi"] = True
    config["upload_to_release"] = True
    config["build_command"] = "true"
    config["remove_dist"] = True
    assert should_remove_dist() == True

    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    config["build_command"] = "false"
    config["remove_dist"] = False
    assert should_remove_dist() == False

# Generated at 2022-06-14 05:04:58.319257
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["upload_to_pypi"] = True
    assert should_remove_dist() is True
    config["remove_dist"] = True
    assert should_remove_dist() is False
    config["build_command"] = "true"
    assert should_remove_dist() is True

# Generated at 2022-06-14 05:05:04.471004
# Unit test for function should_build
def test_should_build():
    config['build_command'] = 'echo'
    assert should_build()

    config['upload_to_pypi'] = 'true'
    assert should_build()

    config['build_command'] = 'false'
    assert not should_build()

    config['build_command'] = 'echo'
    config['upload_to_pypi'] = 'false'
    config['upload_to_release'] = 'false'
    assert not should_build()

# Generated at 2022-06-14 05:05:06.116811
# Unit test for function should_build
def test_should_build():
    assert should_build() == True



# Generated at 2022-06-14 05:05:11.784382
# Unit test for function should_remove_dist
def test_should_remove_dist():
    config["upload_to_pypi"] = "true"
    config["upload_to_release"] = "false"
    config["build_command"] = "python setup.py sdist bdist_wheel"
    config["remove_dist"] = "true"
    assert should_remove_dist()
    config["remove_dist"] = "false"
    assert not should_remove_dist()

# Generated at 2022-06-14 05:05:13.286304
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() == True



# Generated at 2022-06-14 05:05:14.194225
# Unit test for function should_build
def test_should_build():
    assert should_build() is True


# Generated at 2022-06-14 05:05:18.250996
# Unit test for function should_remove_dist
def test_should_remove_dist():
    assert should_remove_dist() is False
    assert should_build() is False

    config.update({"upload_to_pypi": True, "remove_dist": True})
    assert should_remove_dist() is True
    assert should_build() is True

    config.update({"upload_to_release": True, "remove_dist": True})
    assert should_remove_dist() is True
    assert should_build() is True

# Generated at 2022-06-14 05:07:17.103463
# Unit test for function should_build
def test_should_build():
    with_build_command = {
        "upload_to_pypi": True,
        "upload_to_release": True,
        "build_command": "python setup.py sdist bdist_wheel",
    }
    assert should_build(with_build_command) == True

    with_no_upload_to_pypi = {
        "upload_to_pypi": False,
        "upload_to_release": True,
        "build_command": "python setup.py sdist bdist_wheel",
    }
    assert should_build(with_no_upload_to_pypi) == True


# Generated at 2022-06-14 05:07:22.905120
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = True
    assert should_build()

    config.pop("upload_to_pypi", None)
    config["upload_to_release"] = True
    config["build_command"] = "test"
    assert should_build()

    config.pop("build_command", None)
    assert not should_build()



# Generated at 2022-06-14 05:07:24.995471
# Unit test for function should_build
def test_should_build():
    assert not should_build()
    config["build_command"] = "test"
    assert should_build()


# Generated at 2022-06-14 05:07:29.254480
# Unit test for function should_build
def test_should_build():
    config["upload_to_pypi"] = True
    assert should_build()

    config["upload_to_pypi"] = False
    config["upload_to_release"] = False
    assert not should_build()
