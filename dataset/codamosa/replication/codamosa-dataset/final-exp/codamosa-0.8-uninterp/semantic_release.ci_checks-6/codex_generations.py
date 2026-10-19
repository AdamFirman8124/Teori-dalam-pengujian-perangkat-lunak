

# Generated at 2022-06-14 04:45:15.723733
# Unit test for function semaphore
def test_semaphore():
    """
    Testing the function Semaphore
    """
    branch = "master"
    os.environ["BRANCH_NAME"] = branch
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_PROJECT_NAME"] = "Test"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"

    semaphore(branch)

# Generated at 2022-06-14 04:45:25.141099
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "test-branch"
    os.environ["PULL_REQUEST_NUMBER"] = "666"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    try:
        semaphore("test-branch")
        assert False
    except CiVerificationError:
        os.environ.pop("BRANCH_NAME")
        os.environ.pop("PULL_REQUEST_NUMBER")
        os.environ.pop("SEMAPHORE_THREAD_RESULT")

# Generated at 2022-06-14 04:45:27.952369
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    check()



# Generated at 2022-06-14 04:45:31.495592
# Unit test for function jenkins
def test_jenkins():
    """
    Unit test for function jenkins
    """
    os.environ['JENKINS_URL'] = "true"
    os.environ['GIT_BRANCH'] = "master"
    check()



# Generated at 2022-06-14 04:45:34.313402
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'jenkins'
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['CHANGE_ID'] = 'test'
    jenkins("master")

# Generated at 2022-06-14 04:45:46.437348
# Unit test for function circle
def test_circle():
    environ_ci_pull_request = os.environ.get("CI_PULL_REQUEST")
    os.environ["CI_PULL_REQUEST"] = ""
    environ_circle_branch = os.environ.get("CIRCLE_BRANCH")
    os.environ["CIRCLE_BRANCH"] = "master"
    assert circle(branch="master")
    os.environ["CI_PULL_REQUEST"] = "true"
    assert circle(branch="master") is False
    os.environ["CI_PULL_REQUEST"] = ""
    os.environ["CIRCLE_BRANCH"] = "other"
    assert circle(branch="master") is False
    os.environ["CIRCLE_BRANCH"] = environ_circle_branch


# Generated at 2022-06-14 04:45:49.899902
# Unit test for function checker
def test_checker():
    def foo():
        assert False

    def bar():
        raise AssertionError

    foo = checker(foo)
    bar = checker(bar)

    try:
        assert foo()
    except CiVerificationError:
        assert False

    try:
        bar()
        assert False
    except CiVerificationError:
        assert True

# Generated at 2022-06-14 04:45:52.338695
# Unit test for function bitbucket
def test_bitbucket():
    assert not bitbucket("master")
    assert not bitbucket("develop")
    assert not bitbucket("hotfix")

# Generated at 2022-06-14 04:46:02.115305
# Unit test for function frigg
def test_frigg():
    environ = {
        "FRIGG_BUILD_BRANCH": "master",
        "FRIGG_PULL_REQUEST": "false",
    }

    with frigg(environ=environ):
        pass

    frigg(branch="master")
    with frigg(branch="blabla", environ=environ):
        pass

    with frigg(branch="master", environ=environ):
        pass

    with frigg(branch="master", environ=environ):
        os.environ["FRIGG_BUILD_BRANCH"] = "blabla"

    with frigg(branch="blabla", environ=environ):
        os.environ["FRIGG_BUILD_BRANCH"] = "blabla"


# Generated at 2022-06-14 04:46:05.366652
# Unit test for function checker
def test_checker():
    @checker
    def func():
        assert False

    try:
        func()
    except CiVerificationError:
        return

    raise AssertionError('should raise CiVerificationError')

# Generated at 2022-06-14 04:46:19.345319
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore(branch="test")
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert not semaphore(branch="test")

# Generated at 2022-06-14 04:46:22.876800
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    assert semaphore('master')

# Generated at 2022-06-14 04:46:27.164425
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = "http://example.com"
    os.environ['GIT_BRANCH'] = "stage"
    check(branch="stage")


# Generated at 2022-06-14 04:46:33.194458
# Unit test for function gitlab
def test_gitlab():
    os.environ.update({"CI_COMMIT_REF_NAME": "master"}) # simulate working dir is on master branch
    check()

    os.environ.update({"CI_COMMIT_REF_NAME": "not-master"}) # simulate working dir is on master branch
    try:
        check()
        assert False, "An exception should have occurred"
    except CiVerificationError:
        pass
    finally:
        os.environ.pop("CI_COMMIT_REF_NAME")


# Generated at 2022-06-14 04:46:39.873509
# Unit test for function bitbucket
def test_bitbucket():
    """
    Test for function bitbucket
    """
    os.environ["BITBUCKET_BUILD_NUMBER"] = "BUILD_NUMBER"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "PULL_REQUEST_ID"
    check()
    del os.environ["BITBUCKET_BRANCH"]
    check()
    del os.environ["BITBUCKET_BUILD_NUMBER"]
    check()
    del os.environ["BITBUCKET_PR_ID"]

# Generated at 2022-06-14 04:46:45.247897
# Unit test for function gitlab
def test_gitlab():
    """
    Test the function gitlab
    """
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    try:
        gitlab("master")
    except Exception as e:
        print(e)
        assert False

# Generated at 2022-06-14 04:46:53.247547
# Unit test for function checker
def test_checker():
    # Set up

    # Execution
    @checker
    def test_func(a, b):
        raise AssertionError("Shouldn't get here")

    # Verification
    try:
        test_func(1, 2)
        assert False
    except CiVerificationError:
        pass
    except:
        assert False

    try:
        test_func(a=1, b=2)
        assert False
    except CiVerificationError:
        pass
    except:
        assert False

    def test_func2():
        return True

    test_func2()

    assert test_func(1, 2)
    assert test_func(a=1, b=2)


# Generated at 2022-06-14 04:46:59.213103
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    del os.environ["TRAVIS_BRANCH"]
    del os.environ["TRAVIS_PULL_REQUEST"]


# Generated at 2022-06-14 04:47:08.575605
# Unit test for function circle
def test_circle():
    # Test for status = "failed"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "true"
    try:
        circle("master")
        assert False
    except CiVerificationError as e:
        assert str(e) == 'The verification check for the environment did not pass.'
        assert os.environ["CIRCLE_BRANCH"] == "master"
        assert os.environ["CI_PULL_REQUEST"] == "true"
        assert e.__cause__ == None

    # Test for status = "success"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    assert circle("master")
    os.environ

# Generated at 2022-06-14 04:47:17.138777
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check(branch="master")
    os.environ["TRAVIS_PULL_REQUEST"] = "1"
    try:
        check(branch="master")
    except CiVerificationError:
        pass
    else:
        assert False, "CiVerificationError should be raised"
    del os.environ["TRAVIS"]
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"

# Generated at 2022-06-14 04:47:25.056746
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = 'master'
    bitbucket('master')

# Generated at 2022-06-14 04:47:26.126193
# Unit test for function check
def test_check():
    test_check.var = 1
    assert test_check.var == 1



# Generated at 2022-06-14 04:47:29.815953
# Unit test for function checker
def test_checker():
    """
    Test that the checker-function raises a CiVerificationError when decorating
    a function that raises an AssertionError.
    """
    import pytest

    @checker
    def test_failing_function():
        assert False

    with pytest.raises(CiVerificationError):
        test_failing_function()



# Generated at 2022-06-14 04:47:41.718383
# Unit test for function check
def test_check():
    # Test for travis
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "test"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check("test")
    with os.environ:
        del os.environ["TRAVIS_BRANCH"]
        del os.environ["TRAVIS_PULL_REQUEST"]
    with os.environ:
        del os.environ["TRAVIS"]

    # Test for semaphore
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "test"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ

# Generated at 2022-06-14 04:47:54.685037
# Unit test for function frigg
def test_frigg():
    try:
        os.environ.setdefault("FRIGG", "true")
        frigg("master")
    except Exception:
        assert 1 == 0
    finally:
        os.environ["FRIGG"] = "false"
    try:
        os.environ.setdefault("FRIGG", "true")
        os.environ.setdefault("FRIGG_PULL_REQUEST", "true")
        frigg("master")
        assert 1 == 0
    except Exception:
        pass
    finally:
        os.environ["FRIGG"] = "false"
        os.environ["FRIGG_PULL_REQUEST"] = "false"

# Generated at 2022-06-14 04:48:01.346888
# Unit test for function checker
def test_checker():
    def dummy_func():
        return True

    def dummy_func_1():
        raise AssertionError()

    assert checker(dummy_func)() is True
    if checker(dummy_func_1)():
        raise AssertionError()

# Generated at 2022-06-14 04:48:06.420539
# Unit test for function semaphore
def test_semaphore():
    assert not os.environ.get("BRANCH_NAME") == "dev"
    assert not os.environ.get("SEMAPHORE_THREAD_RESULT") == "failed"
    assert os.environ.get("PULL_REQUEST_NUMBER") == None



# Generated at 2022-06-14 04:48:09.473489
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    frigg("master")
    frigg("foo")

# Generated at 2022-06-14 04:48:13.327049
# Unit test for function jenkins
def test_jenkins():
    """Unit test for function jenkins"""
    os.environ["JENKINS_URL"] = "True"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = ""
    jenkins("master")

# Generated at 2022-06-14 04:48:23.232909
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = ""
    frigg("master")

    os.environ["FRIGG_BUILD_BRANCH"] = "thisbranchdoesnotexist"
    with pytest.raises(CiVerificationError):
        frigg("master")

    os.environ["FRIGG_PULL_REQUEST"] = "true"
    with pytest.raises(CiVerificationError):
        frigg("master")



# Generated at 2022-06-14 04:48:35.708798
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    os.environ["FRIGG_PULL_REQUEST"] = "1"
    try:
        check(branch="develop")
        assert False
    except CiVerificationError:
        assert True
    del os.environ["FRIGG"]
    del os.environ["FRIGG_BUILD_BRANCH"]
    del os.environ["FRIGG_PULL_REQUEST"]


# Generated at 2022-06-14 04:48:45.616728
# Unit test for function checker
def test_checker():
    def function_to_test(branch: str):
        assert os.environ.get("TRAVIS_BRANCH") == branch
        assert os.environ.get("TRAVIS_PULL_REQUEST") == "false"

    test_func = checker(function_to_test)
    os.environ['TRAVIS_BRANCH'] = "master"
    os.environ['TRAVIS_PULL_REQUEST'] = "false"
    test_func("master")

    del os.environ['TRAVIS_BRANCH']
    del os.environ['TRAVIS_PULL_REQUEST']
    try:
        test_func("master")
    except ValueError as e:
        assert type(e) == CiVerificationError

# Generated at 2022-06-14 04:48:56.162043
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = "true"
    os.environ['FRIGG_BUILD_BRANCH'] = "master"
    assert frigg("master") == True
    os.environ['FRIGG_BUILD_BRANCH'] = "develop"
    assert frigg("master") == False
    os.environ['FRIGG_PULL_REQUEST'] = "1"
    assert frigg("master") == False
    del os.environ['FRIGG_BUILD_BRANCH']
    os.environ['FRIGG'] = "false"
    assert frigg("master") == False
    del os.environ['FRIGG']


# Generated at 2022-06-14 04:48:56.784135
# Unit test for function semaphore
def test_semaphore():
    pass

# Generated at 2022-06-14 04:49:01.724112
# Unit test for function circle
def test_circle():
    """
    Test the checker function of circle
    """
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "false"
    os.environ["CIRCLE_BRANCH"] = "master"
    check()
    del os.environ["CI_PULL_REQUEST"]
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CIRCLECI"]


# Generated at 2022-06-14 04:49:05.462705
# Unit test for function circle
def test_circle():
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    assert circle()

# Generated at 2022-06-14 04:49:12.351195
# Unit test for function checker
def test_checker():
    def checker_test(branch: str) -> None:
        assert os.environ.get("TRAVIS_BRANCH") == branch
        assert os.environ.get("TRAVIS_PULL_REQUEST") == "false"

    checker_test = checker(checker_test)
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert checker_test("master") is True

# Generated at 2022-06-14 04:49:16.432449
# Unit test for function check
def test_check():
    """
    Unit test for function check.
    """
    for var in ["TRAVIS", "SEMAPHORE", "FRIGG", "CIRCLECI", "GITLAB_CI", "JENKINS_URL"]:
        os.environ.pop(var, None)
    check()

# Generated at 2022-06-14 04:49:23.674117
# Unit test for function circle
def test_circle():
    """
    Checks that circle environment variables are detected
    """
    assert os.environ.get("CIRCLECI") == "true"
    assert os.environ.get("CI_PULL_REQUEST") is None
    assert os.environ.get("CIRCLE_BRANCH") == "master"
    circle("master")
    circle("develop")



# Generated at 2022-06-14 04:49:28.715372
# Unit test for function semaphore
def test_semaphore():
    """
    Test semaphore
    """
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    assert semaphore("master")



# Generated at 2022-06-14 04:49:42.942103
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ['FRIGG_PULL_REQUEST'] = 'false'

    frigg('master')



# Generated at 2022-06-14 04:49:43.782645
# Unit test for function frigg
def test_frigg():
    assert frigg("master")

# Generated at 2022-06-14 04:49:46.625861
# Unit test for function checker
def test_checker():
    @checker
    def travis_fail(branch: str):
        assert os.environ.get("TRAVIS_BRANCH") != branch
    try:
        travis_fail("master")
    except CiVerificationError:
        pass
    else:
        assert False

# Generated at 2022-06-14 04:49:52.089540
# Unit test for function checker
def test_checker():
    @checker
    def test_function():
        assert 1 == 0

    try:
        test_function()
    except CiVerificationError:
        pass
    else:
        assert False, 'CiVerificationError not raised on assertion failure'

    @checker
    def test_function():
        assert 1 == 1

    assert test_function() is True

# Generated at 2022-06-14 04:49:56.162477
# Unit test for function checker
def test_checker():
    @checker
    def foo(val):
        assert val == True
    foo(True)
    try:
        foo(False)
    except CiVerificationError:
        pass
    else:
        assert False, "CiVerificationError not raised."

# Generated at 2022-06-14 04:49:59.531489
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg("master")


# Generated at 2022-06-14 04:50:03.614827
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    frigg('master')
    os.environ['FRIGG_BUILD_BRANCH'] = 'develop'
    try:
        frigg('master')
        assert False
    except:
        pass



# Generated at 2022-06-14 04:50:08.772788
# Unit test for function checker
def test_checker():
    """
    Test the function decorator checker.
    :return:
    """

    @checker
    def test_func():
        assert False

    try:
        test_func()
        assert False
    except CiVerificationError as ve:
        assert ve.args[0] == "The verification check for the environment did not pass."

# Generated at 2022-06-14 04:50:11.633866
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")


# Generated at 2022-06-14 04:50:19.087299
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = None
    assert frigg("master")
    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    assert not frigg("master")
    os.environ["FRIGG_PULL_REQUEST"] = "42"
    assert not frigg("master")
    del os.environ["FRIGG"]


# Generated at 2022-06-14 04:50:49.672740
# Unit test for function checker
def test_checker():
    @checker
    def check_success():
        assert True

    @checker
    def check_failure():
        assert False

    try:
        check_success()
        check_failure()
    except CiVerificationError:
        pass
    except:
        raise AssertionError("Unexpected exception for checker decorator")
    else:
        raise AssertionError("Expected to raise exception for checker decorator")

# Generated at 2022-06-14 04:51:01.304043
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "some-branch"
    assert bitbucket("some-branch") is True
    del os.environ["BITBUCKET_BRANCH"]
    try:
        bitbucket("some-branch")
        raise Exception("This should have raised")
    except CiVerificationError:
        pass
    os.environ["BITBUCKET_BRANCH"] = "some-branch"
    os.environ["BITBUCKET_PR_ID"] = "1"
    try:
        bitbucket("some-branch")
        raise Exception("This should have raised")
    except CiVerificationError:
        pass
    del os.environ["BITBUCKET_BRANCH"]

# Generated at 2022-06-14 04:51:08.345642
# Unit test for function circle
def test_circle():
    """
    We test the function circle by checking if the 
    os.environ.get("CIRCLE_BRANCH") == branch 
    and the function os.environ.get("CI_PULL_REQUEST") is not a valid number ("false" = false)
    is working. 

    If this works, then all conditions are met and the function circle will return True. 
    """
    assert circle("master")


# Generated at 2022-06-14 04:51:14.284156
# Unit test for function checker
def test_checker():
    """
    Test the checker decorator by providing it a function that raises an
    AssertionError, it should then convert this into a CiVerificationError.
    """
    @checker
    def func():
        assert False

    try:
        func()
    except CiVerificationError:
        pass
    else:
        raise AssertionError("The checker decorator didn't raise a "
                             "CiVerificationError like it should have.")

# Generated at 2022-06-14 04:51:21.458963
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    del os.environ["CI_PULL_REQUEST"]
    circle("master")

    # now with a pull request
    os.environ["CI_PULL_REQUEST"] = "1"
    try:
        circle("master")
        assert False
    except CiVerificationError:
        assert True

    try:
        circle("other")
        assert False
    except CiVerificationError:
        assert True



# Generated at 2022-06-14 04:51:27.834163
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg("develop")
    assert os.environ.get("FRIGG_PULL_REQUEST") is not None
    del os.environ["FRIGG_PULL_REQUEST"]
    frigg("master")

# Generated at 2022-06-14 04:51:36.699584
# Unit test for function jenkins
def test_jenkins():
    """
    Tests the jenkins function
    """
    def set_variables(variables):
        for var, val in variables.items():
            os.environ[var] = val

    # Success
    set_variables({"JENKINS_URL": "http://example.com",
                   "GIT_BRANCH": "master"})
    try:
        jenkins(branch="master")
    except Exception:
        assert False
    else:
        assert True

    # Failure - incorrect branch
    set_variables({"JENKINS_URL": "http://example.com",
                   "GIT_BRANCH": "release1"})
    try:
        jenkins(branch="master")
    except Exception:
        assert True
    else:
        assert False

    # Failure -

# Generated at 2022-06-14 04:51:40.513527
# Unit test for function checker
def test_checker():
    """
    Test for checker decorator
    """
    @checker
    def test_method():
        assert False
    try:
        test_method()
    except CiVerificationError:
        return
    assert False

# Generated at 2022-06-14 04:51:45.447359
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "false"
    os.environ["CIRCLE_BRANCH"] = "master"
    try:
        circle("master")
        assert True
    except AssertionError:
        assert False


# Generated at 2022-06-14 04:51:55.266106
# Unit test for function frigg
def test_frigg():
  # Should be able to upgrade
  os.environ["FRIGG_BUILD_BRANCH"] = "master"
  os.environ["FRIGG_PULL_REQUEST"] = "false"
  frigg("master")
  # Should not be able to upgrade
  os.environ["FRIGG_BUILD_BRANCH"] = "stable"
  os.environ["FRIGG_PULL_REQUEST"] = "true"
  try:
    frigg("master")
    assert False
  except CiVerificationError:
    pass

# Generated at 2022-06-14 04:52:46.777004
# Unit test for function semaphore
def test_semaphore():
    os.environ['SEMAPHORE'] = "true"
    os.environ['BRANCH_NAME'] = "master"
    os.environ['SEMAPHORE_THREAD_RESULT'] = "passed"
    os.environ['PULL_REQUEST_NUMBER'] = "None"
    semaphore("master")
    # test with a wrong branch
    os.environ['BRANCH_NAME'] = "wrongbranch"
    try:
        semaphore("master")
        assert False, "'master' should be asserted as the current branch"
    except CiVerificationError:
        pass
    # test with a pull request
    os.environ['BRANCH_NAME'] = "master"
    os.environ['PULL_REQUEST_NUMBER'] = "12345"

# Generated at 2022-06-14 04:52:54.304237
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "branch"
    os.environ["BITBUCKET_PR_ID"] = "1"
    assert bitbucket(branch="branch") == False
    del os.environ["BITBUCKET_PR_ID"]
    assert bitbucket(branch="branch") == True



# Generated at 2022-06-14 04:52:59.865693
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = None
    bitbucket("master")
    del os.environ["BITBUCKET_BRANCH"]
    del os.environ["BITBUCKET_PR_ID"]



# Generated at 2022-06-14 04:53:01.315793
# Unit test for function gitlab
def test_gitlab():
    assert os.environ.get("CI_PIPELINE_SOURCE") == "push"

# Generated at 2022-06-14 04:53:08.940262
# Unit test for function travis
def test_travis():
    assert travis("master")
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    try:
        travis("development")
    except CiVerificationError:
        assert True
    finally:
        del os.environ["TRAVIS_BRANCH"]
        del os.environ["TRAVIS_PULL_REQUEST"]



# Generated at 2022-06-14 04:53:11.733795
# Unit test for function bitbucket
def test_bitbucket():
    assert bitbucket("master")
    assert not bitbucket("branch")


# Generated at 2022-06-14 04:53:17.266959
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "True"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    assert check() == None
    assert check("dev") == None
    os.environ["CHANGE_ID"] = "True"
    assert check() == False

# Generated at 2022-06-14 04:53:29.271530
# Unit test for function bitbucket
def test_bitbucket():
    try:
        bitbucket("master")
        assert False
    except CiVerificationError:
        pass
    os.environ["BITBUCKET_BUILD_NUMBER"] = ""
    try:
        bitbucket("master")
        assert False
    except CiVerificationError:
        pass
    os.environ["BITBUCKET_BRANCH"] = "master"
    bitbucket("master")
    try:
        bitbucket("develop")
        assert False
    except CiVerificationError:
        pass
    os.environ["BITBUCKET_PR_ID"] = "1"
    try:
        bitbucket("master")
        assert False
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:53:32.869375
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BUILD_NUMBER'] = '1'
    os.environ['BITBUCKET_BRANCH'] = 'master'
    bitbucket('master')

# Generated at 2022-06-14 04:53:37.393580
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = ""
    check()

