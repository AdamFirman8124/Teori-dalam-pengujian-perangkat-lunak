

# Generated at 2022-06-14 04:45:15.880317
# Unit test for function checker
def test_checker():
    @checker
    def function_that_returns_true():
        return True

    @checker
    def function_that_raises_assertion_error():
        raise AssertionError

    assert function_that_returns_true() == True
    try:
        function_that_raises_assertion_error()
    except CiVerificationError:
        pass
    else:
        raise AssertionError("A CiVerificationError should be raised")

# Generated at 2022-06-14 04:45:16.992655
# Unit test for function bitbucket
def test_bitbucket():
    assert bitbucket() is True

# Generated at 2022-06-14 04:45:20.654660
# Unit test for function checker
def test_checker():
    def foo():
        raise AssertionError("Error")

    foo_checker = checker(foo)

    try:
        foo_checker()
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:45:26.641340
# Unit test for function gitlab
def test_gitlab():
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    os.environ['CI_PROJECT_NAME'] = 'project'
    check()
    assert os.environ['CI_COMMIT_REF_NAME'] == 'master'
    assert os.environ['CI_PROJECT_NAME'] == 'project'

# Generated at 2022-06-14 04:45:31.455607
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"]="true"
    os.environ["BRANCH_NAME"]="master"
    os.environ["PULL_REQUEST_NUMBER"]=None
    os.environ["SEMAPHORE_THREAD_RESULT"]="passed"

    semaphore("master")


# Generated at 2022-06-14 04:45:34.585696
# Unit test for function semaphore
def test_semaphore():
    # test with correct branch name
    assert semaphore('test-branch') is True
    # test with incorrect branch name
    try:
        semaphore('master')
    except CiVerificationError:
        assert True
    else:
        assert False



# Generated at 2022-06-14 04:45:40.072223
# Unit test for function check
def test_check():
    assert os.environ.get("CIRCLE") == "true"
    assert os.environ.get("CIRCLE_BRANCH") == "feature_branch"
    assert os.environ.get("CIRCLE_PULL_REQUEST") == ""
    assert not os.environ.get("CI_PULL_REQUEST")
    assert not os.environ.get("BITBUCKET_PR_ID")
    assert not os.environ.get("FRIGG_PULL_REQUEST")
    assert not os.environ.get("SEMAPHORE_PR")
    assert not os.environ.get("SEMAPHORE_PULL_REQUEST_NUMBER")
    assert not os.environ.get("TRAVIS_PULL_REQUEST")
    check("feature_branch")



# Generated at 2022-06-14 04:45:41.447487
# Unit test for function gitlab
def test_gitlab():
    gitlab("master")

# Generated at 2022-06-14 04:45:42.417779
# Unit test for function bitbucket
def test_bitbucket():
    assert checker(bitbucket)("test") == True

# Generated at 2022-06-14 04:45:47.780014
# Unit test for function checker
def test_checker():
    """
    Test to check whether the checker decorator converts AssertionErrors to
    CiVerificationError.
    """
    try:
        @checker
        def test_func():
            assert 1 == 0
        test_func()
    except AssertionError:
        assert False
    except CiVerificationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:45:57.550034
# Unit test for function bitbucket
def test_bitbucket():
    branch = "master"
    assert os.environ.get("BITBUCKET_BRANCH") == branch
    assert not os.environ.get("BITBUCKET_PR_ID")

# Generated at 2022-06-14 04:45:58.178401
# Unit test for function travis
def test_travis():
    pass

# Generated at 2022-06-14 04:46:01.793528
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'success'
    assert semaphore('master') is True



# Generated at 2022-06-14 04:46:07.534203
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert check()
    del os.environ["TRAVIS"]
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert check()
    del os.environ["SEMAPHORE"]
    os.environ["FRIGG"] = "true"

# Generated at 2022-06-14 04:46:16.447233
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()

    os.environ["TRAVIS_BRANCH"] = "qa"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check("qa")

    os.environ["TRAVIS_BRANCH"] = "qa"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    check("qa")

# Generated at 2022-06-14 04:46:19.908453
# Unit test for function checker
def test_checker():
    @checker
    def assert_true():
        assert False

    try:
        assert_true()
    except CiVerificationError:
        return

    raise RuntimeError("Should have raised CiVerificationError")

# Generated at 2022-06-14 04:46:25.894023
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "test"
    assert True == bitbucket("test")
    os.environ["BITBUCKET_BRANCH"] = "xxx"
    assert False == bitbucket("test")
    os.environ["BITBUCKET_PR_ID"] = "1"
    assert False == bitbucket("test")
    # Reset
    os.environ["BITBUCKET_BRANCH"] = ""
    os.environ["BITBUCKET_PR_ID"] = ""



# Generated at 2022-06-14 04:46:30.046008
# Unit test for function gitlab
def test_gitlab():
    # environment variable
    os.environ["GITLAB_CI"] = "true"
    assert os.environ.get("GITLAB_CI") == "true"
    gitlab("master")
    # pull request
    os.environ["CI_COMMIT_REF_NAME"] = "pull request"
    assert os.environ.get("CI_COMMIT_REF_NAME") != "master"
    gitlab("master")
    # branch not equal
    os.environ["CI_COMMIT_REF_NAME"] = "not master"
    assert os.environ.get("CI_COMMIT_REF_NAME") != "master"
    gitlab("master")
    # cleanup
    os.environ.pop("GITLAB_CI")
    os.environ.pop("CI_COMMIT_REF_NAME")


# Generated at 2022-06-14 04:46:36.537408
# Unit test for function semaphore
def test_semaphore():
    # Add test environment variables to the os environment
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"

    assert semaphore("master")
    del os.environ["BRANCH_NAME"]
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["SEMAPHORE_THREAD_RESULT"]



# Generated at 2022-06-14 04:46:39.720614
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_PROJECT_PATH"] = None
    check(branch = "master")

# Generated at 2022-06-14 04:46:56.698177
# Unit test for function checker
def test_checker():
    def my_func(a):
        return a

    assert checker(my_func)(1)
    try:
        checker(my_func)(2)
        assert "Should not have come here"
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:47:04.945949
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = ''
    assert travis('master') == True
    os.environ['TRAVIS_BRANCH'] = 'develop'
    os.environ['TRAVIS_PULL_REQUEST'] = ''
    assert travis('master') == False
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = '1'
    assert travis('master') == False


# Generated at 2022-06-14 04:47:12.634604
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "a"
    os.environ["CHANGE_ID"] = ""
    os.environ["GIT_BRANCH"] = "master"
    assert check("master")
    os.environ["BRANCH_NAME"] = "feature/hello"
    os.environ["JENKINS_URL"] = "a"
    os.environ["CHANGE_ID"] = ""
    os.environ["GIT_BRANCH"] = "feature/hello"
    assert not check("master")
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "a"
    os.environ["CHANGE_ID"]

# Generated at 2022-06-14 04:47:19.512902
# Unit test for function circle
def test_circle():
    # test success
    os.environ["CIRCLE_BRANCH"] = "test"
    del os.environ["CI_PULL_REQUEST"]
    assert circle("test")
    # test failure
    os.environ["CI_PULL_REQUEST"] = "xxx"
    try:
        circle("test")
    except CiVerificationError:
        pass
    else:
        raise AssertionError("test_circle_1: failed test")
    # test failure
    del os.environ["CI_PULL_REQUEST"]
    os.environ["CIRCLE_BRANCH"] = "test2"
    try:
        circle("test")
    except CiVerificationError:
        pass
    else:
        raise AssertionError("test_circle_2: failed test")

# Unit

# Generated at 2022-06-14 04:47:29.924298
# Unit test for function jenkins
def test_jenkins():

    assert not jenkins("MASTER")
    assert not jenkins("BRANCH_NAME")
    assert not jenkins("GIT_BRANCH")
    assert not jenkins("CHANGE_ID")

    #Create test variables
    BRANCH_NAME = "master"
    GIT_BRANCH = "master"
    CHANGE_ID = ""

    os.environ["BRANCH_NAME"] = BRANCH_NAME
    os.environ["GIT_BRANCH"] = GIT_BRANCH
    os.environ["CHANGE_ID"] = CHANGE_ID
    os.environ["JENKINS_URL"] = "http://jenkins.com"

    assert jenkins("masTeR")

# Generated at 2022-06-14 04:47:33.987399
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master")

# Generated at 2022-06-14 04:47:43.537237
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    bitbucket("master")

    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "1"

    from semantic_release.errors import CiVerificationError

    try:
        bitbucket("master")
        assert False
    except CiVerificationError:
        assert True

    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "develop"
    os.en

# Generated at 2022-06-14 04:47:55.768586
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "a"
    os.environ["GIT_BRANCH"] = "master"
    check(branch = "master")
    os.environ["GIT_BRANCH"] = "feature/my_feature"
    check(branch = "master")
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = "a"
    check(branch = "master")
    del os.environ["GIT_BRANCH"]
    os.environ["BRANCH_NAME"] = "master"
    check(branch = "master")
    os.environ["BRANCH_NAME"] = "feature/my_feature"
    check(branch = "master")
    os.en

# Generated at 2022-06-14 04:48:06.535574
# Unit test for function check
def test_check():
    for env_var in os.environ:
        if env_var.startswith("CI_"):
            del os.environ[env_var]

    check()

    os.environ["TRAVIS"] = "true"
    check()

    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    check()

    os.environ["GITLAB_CI"] = "true"
    check()

    os.environ["CIRCLECI"] = "true"
    check()

    os.environ["SEMAPHORE"] = "true"
    check()

    os.environ["FRIGG"] = "true"
    check()

    os.environ["JENKINS_URL"] = "https://jenkins.io"
    check()

# Generated at 2022-06-14 04:48:11.621432
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "develop"
    os.environ["CI_PULL_REQUEST"] = "2408"
    check("unittest")


# Generated at 2022-06-14 04:48:40.084604
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["JENKINS_URL"] = "https://example.com"
    os.environ["CHANGE_ID"] = None

    assert check() == True

    os.environ["JENKINS_URL"] = None
    assert check() == False

# Generated at 2022-06-14 04:48:45.092442
# Unit test for function gitlab
def test_gitlab():
    """
    Performs necessary checks to ensure that the gitlab build is one
    that should create releases.
    """
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    os.environ['CI_MERGE_REQUEST_IID'] = None

    check('master')
    try:
        check('release')
        assert False
    except CiVerificationError:
        assert True

# Generated at 2022-06-14 04:48:46.119334
# Unit test for function circle
def test_circle():
    assert circle("master") == True


# Generated at 2022-06-14 04:48:56.968179
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = None
    frigg("master")

    del os.environ["FRIGG"]
    del os.environ["FRIGG_BUILD_BRANCH"]
    del os.environ["FRIGG_PULL_REQUEST"]

    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    os.environ["FRIGG_PULL_REQUEST"] = None
    frigg("master")


# Generated at 2022-06-14 04:49:09.175954
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check()
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_IID"] = "1234"
    check()
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_IID"] = "1234"
    check("beta")
    os.environ["GITLAB_CI"] = "true"

# Generated at 2022-06-14 04:49:17.757014
# Unit test for function semaphore
def test_semaphore():
    # Without environment variables
    assert not semaphore(branch = 'master')

    # With all the right variables
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    assert semaphore(branch = 'master')

    # With some of the right variables
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'failed'
    assert not semaphore(branch = 'master')

# Generated at 2022-06-14 04:49:28.329227
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        check()
        assert False
    except CiVerificationError:
        try:
            os.environ["TRAVIS_PULL_REQUEST"] = "false"
            os.environ["TRAVIS_BRANCH"] = "develop"
            check("develop")
            assert False
        except CiVerificationError:
            assert True



# Generated at 2022-06-14 04:49:29.210762
# Unit test for function jenkins
def test_jenkins():
    assert jenkins("master") == True

# Generated at 2022-06-14 04:49:37.895824
# Unit test for function semaphore
def test_semaphore():
    """
    unit test for function semaphore
    """
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "123"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert semaphore("master") is False

    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "123"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    assert semaphore("master") is True

# Generated at 2022-06-14 04:49:40.777270
# Unit test for function semaphore
def test_semaphore():
    checker(semaphore)
    assert os.environ.get("BRANCH_NAME") == "master"



# Generated at 2022-06-14 04:50:26.611896
# Unit test for function semaphore
def test_semaphore():
    # On pull-request
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "123"
    try:
        semaphore("master")
        assert False
    except CiVerificationError:
        pass

    # Failed build
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    try:
        semaphore("master")
        assert False
    except CiVerificationError:
        pass

    # On correct branch
    os.environ["SEMAPHORE"] = "true"

# Generated at 2022-06-14 04:50:34.299220
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = None
    try:
        bitbucket()
        assert True
    except CiVerificationError:
        assert False
    del os.environ["BITBUCKET_BRANCH"]
    del os.environ["BITBUCKET_PR_ID"]



# Generated at 2022-06-14 04:50:40.279453
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "mybranch"
    assert frigg("mybranch") == True

    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "1"
    assert frigg("mybranch") == False


# Generated at 2022-06-14 04:50:43.996244
# Unit test for function checker
def test_checker():
    success = checker(lambda x: True)
    assert success() == True

    failure = checker(lambda x: False)
    try:
        failure()
    except CiVerificationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:50:46.170168
# Unit test for function checker
def test_checker():
    def func():
        assert False

    def func2():
        assert True

    assert checker(func)() is True
    assert checker(func2)() is False

# Generated at 2022-06-14 04:50:52.645931
# Unit test for function travis
def test_travis():
    """
    Unit test for function travis.
    """
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        travis("master")
        raise AssertionError("False positive for function travis")
    except CiVerificationError:
        pass
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS_BRANCH"] = "develop"
    try:
        travis("master")
        raise AssertionError("False positive for function travis")
    except CiVerificationError:
        pass


#

# Generated at 2022-06-14 04:50:55.186814
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()


# Generated at 2022-06-14 04:51:00.495453
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_TARGET_BRANCH_NAME"] = "master"
    check()
    del os.environ["CI_MERGE_REQUEST_TARGET_BRANCH_NAME"]
    check()

# Generated at 2022-06-14 04:51:03.479538
# Unit test for function checker
def test_checker():
    import pytest
    def fail_assertion_function():
        assert False

    def assert_raises_func():
        fail_assertion_function()

    assert assert_raises_func() is True

    def assert_no_raises_func():
        fail_assertion_function()

    with pytest.raises(CiVerificationError):
        assert_no_raises_func()

# Generated at 2022-06-14 04:51:05.360223
# Unit test for function check
def test_check():
    try:
        check()
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:52:35.586349
# Unit test for function check
def test_check():
    import unittest.mock as mock

    def side_effect(*args):
        check(*args)

    with mock.patch.object(__name__, "travis") as mock_travis:
        mock_travis.side_effect = side_effect

        with mock.patch.dict(os.environ, {"TRAVIS": "true"}):
            with mock.patch.dict(os.environ, {"TRAVIS_BRANCH": "master"}):
                with mock.patch.dict(os.environ, {"TRAVIS_PULL_REQUEST": "false"}):
                    check()
                    mock_travis.assert_called_once()


# Generated at 2022-06-14 04:52:39.739428
# Unit test for function gitlab
def test_gitlab():
    """
    Testing the gitlab function
    """
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    assert gitlab("master") is True



# Generated at 2022-06-14 04:52:43.247516
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "dev"
    os.environ["FRIGG_BUILD_BRANCH"] = "dev"
    check("dev")



# Generated at 2022-06-14 04:52:44.624059
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "false"
    frigg("master")


# Generated at 2022-06-14 04:52:56.189213
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ['FRIGG_PULL_REQUEST'] = 'false'
    try:
        frigg('master')
    except CiVerificationError:
        raise AssertionError("Frigg test failed.")

    os.environ['FRIGG_BUILD_BRANCH'] = 'develop'
    try:
        frigg('master')
    except CiVerificationError:
        pass
    else:
        raise AssertionError("Frigg test failed.")

    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ['FRIGG_PULL_REQUEST'] = 'true'

# Generated at 2022-06-14 04:52:57.818847
# Unit test for function check
def test_check():
    assert check("master")
    assert check()

# Generated at 2022-06-14 04:53:09.822513
# Unit test for function jenkins
def test_jenkins():
    # Set the evironment variable in the OS
    os.environ["JENKINS_URL"] = "https://jenkins-ci.org/"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    jenkins("master")
    os.environ["JENKINS_URL"] = "https://jenkins-ci.org/"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = "1234"
    os.environ.pop("GIT_BRANCH")
    jenkins("master")
    os.environ.pop("CHANGE_ID")
    os.en

# Generated at 2022-06-14 04:53:19.984008
# Unit test for function check
def test_check():
    """
    Test to make sure that the test functions do throw an exception when they are supposed to
    """
    os_env = os.environ.copy()
    os.environ.clear()
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert check()
    os.environ["TRAVIS_BRANCH"] = "not_master"
    try:
        check()
    except CiVerificationError:
        pass
    else:
        assert False, "Exception not thrown from check()"

    os.environ.clear()
    os.environ["SEMAPHORE"] = "true"

# Generated at 2022-06-14 04:53:26.044791
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    jenkins(branch="master")
    os.environ["BRANCH_NAME"] = "other"
    try:
        jenkins(branch="master")
        assert False
    except CiVerificationError:
        assert True



# Generated at 2022-06-14 04:53:35.834851
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("master")
    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("master")
    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = None
    bitbuck