

# Generated at 2022-06-14 04:45:13.720652
# Unit test for function checker
def test_checker():
    try:
        @checker
        def func():
            assert False
        func()
    except CiVerificationError:
        pass
    else:
        assert False

# Generated at 2022-06-14 04:45:17.506438
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    os.environ["TRAVIS_BRANCH"] = ""
    os.environ["TRAVIS_PULL_REQUEST"] = ""



# Generated at 2022-06-14 04:45:29.853624
# Unit test for function bitbucket
def test_bitbucket():
    # Testing for bitbucket pipeline environment variable set in Travis-CI
    os.environ["BITBUCKET_BUILD_NUMBER"] = "0"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "0"
    try:
        bitbucket("master")
    except CiVerificationError:
        pass
    else:
        assert False, "Semantic Release did not raise an exception"
    # Testing for bitbucket pipeline build branches that are not default branch
    os.environ["BITBUCKET_PR_ID"] = "32"
    os.environ["BITBUCKET_BRANCH"] = "not_default"

# Generated at 2022-06-14 04:45:33.447263
# Unit test for function frigg
def test_frigg():
    """ Test frigg CI checker """
    assert frigg("master") is True
    assert frigg("master1") is False


# Generated at 2022-06-14 04:45:44.240831
# Unit test for function jenkins
def test_jenkins():
    branch = "master"
    os.environ["JENKINS_URL"] = "sample"
    os.environ["BRANCH_NAME"] = branch
    os.environ["GIT_BRANCH"] = branch
    os.environ["CHANGE_ID"] = "false"
    
    # Case 1: All conditions for jenkins checks pass
    assert jenkins(branch) == True
    # Case 2: Any one condition for jenkins checks fails
    os.environ["GIT_BRANCH"] = "not master"
    assert jenkins(branch) == False

    # Make sure branch is reset
    os.environ["GIT_BRANCH"] = branch

# Generated at 2022-06-14 04:45:49.333418
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    with open('./test_travis.txt', 'r') as f:
        text = f.readlines()
        assert text[0] == "# the travis function passed\n"

# Generated at 2022-06-14 04:45:52.820504
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ['FRIGG_PULL_REQUEST'] = 'false'
    assert frigg(branch='master') == True


# Generated at 2022-06-14 04:45:54.204668
# Unit test for function frigg
def test_frigg():
    assert not frigg("master")
    assert frigg("dummy")



# Generated at 2022-06-14 04:46:02.680102
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = 3
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert semaphore(branch="does-not-match") is False
    assert semaphore(branch="master") is False
    assert semaphore(branch="master") is False
    assert semaphore(branch="master") is False
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore(branch="master") is True

# Generated at 2022-06-14 04:46:08.106445
# Unit test for function circle
def test_circle():
    ci_data = {
        "CIRCLECI": "true",
        "CIRCLE_BRANCH": "master",
        "CI_PULL_REQUEST": "",
    }
    inputs = [ci_data]
    value = circle(inputs[0]["CIRCLE_BRANCH"])
    assert value == True

# Generated at 2022-06-14 04:46:17.929999
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = ""
    check()

# Generated at 2022-06-14 04:46:21.931321
# Unit test for function checker
def test_checker():
    """
    It should raise a SemanticReleaseError on failed check
    """
    try:
        assert False
    except AssertionError:
        try:
            checker(assertFalse)()
        except CiVerificationError as e:
            assert "did not pass" in str(e)

# Generated at 2022-06-14 04:46:29.985484
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    circle("master")
    assert os.environ.get("CI_PULL_REQUEST") is None
    del os.environ["CIRCLECI"]
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CI_PULL_REQUEST"]


# Generated at 2022-06-14 04:46:37.034212
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BUILD_NUMBER'] = '100'
    os.environ['BITBUCKET_BRANCH'] = 'master'
    os.environ['BITBUCKET_PR_ID'] = ''
    assert bitbucket(branch='master') is True
    # For pull-request build, release shouldn't be created
    os.environ['BITBUCKET_PR_ID'] = '123'
    import pytest
    with pytest.raises(CiVerificationError):
        assert bitbucket(branch='master') is True


# Generated at 2022-06-14 04:46:44.436064
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = ""
    os.environ["CIRCLE_BRANCH"] = "master"
    assert circle(branch="master") is True
    os.environ["CI_PULL_REQUEST"] = "1"
    with pytest.raises(CiVerificationError):
        circle(branch="master")
    os.environ["CIRCLE_BRANCH"] = "unstable"
    with pytest.raises(CiVerificationError):
        circle(branch="master")



# Generated at 2022-06-14 04:46:45.592558
# Unit test for function jenkins
def test_jenkins():
    jenkins(branch="master")

# Generated at 2022-06-14 04:46:48.430195
# Unit test for function frigg
def test_frigg():
    assert frigg("master") is True
    try:
        frigg("other")
    except CiVerificationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:46:52.630158
# Unit test for function jenkins
def test_jenkins():
    """
    Test CI checks for jenkins
    """
    os.environ["JENKINS_URL"] = "True"
    os.environ["BRANCH_NAME"] = "master"
    check()
    del os.environ["JENKINS_URL"]
    del os.environ["BRANCH_NAME"]



# Generated at 2022-06-14 04:46:57.812276
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"

    try:
        check()
    except CiVerificationError as error:
        print(error.__str__())


# Generated at 2022-06-14 04:47:07.796250
# Unit test for function jenkins
def test_jenkins():
    os.environ["GIT_BRANCH"] = "master"
    os.environ["JENKINS_URL"] = "http://jenkins.com"
    os.environ["CHANGE_ID"] = "1"
    assert jenkins(branch="master") is True, "jenkins(branch=master) failed"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["JENKINS_URL"] = "http://jenkins.com"
    os.environ["CHANGE_ID"] = ""
    assert jenkins(branch="master") is True, "jenkins(branch=master) failed"
    os.environ["GIT_BRANCH"] = "master"

# Generated at 2022-06-14 04:47:17.605860
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "branch"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        travis("branch")
        assert False
    except CiVerificationError as e:
        assert "The verification check for the environment did not pass." in str(e)

# Generated at 2022-06-14 04:47:24.533218
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = None
    semaphore("master")

    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    semaphore("master")

# Generated at 2022-06-14 04:47:30.248489
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master") == True

    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert semaphore("master") == False

# Generated at 2022-06-14 04:47:41.787109
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "http://jenkins.com"

    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = "123123123"
    try:
        jenkins("master")
        assert False
    except CiVerificationError:
        assert True

    os.environ["CHANGE_ID"] = None
    jenkins("master")

    os.environ["BRANCH_NAME"] = "feat/test"
    try:
        jenkins("master")
        assert False
    except CiVerificationError:
        assert True

    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    jenkins("master")

   

# Generated at 2022-06-14 04:47:47.181342
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    circle("master")
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CIRCLECI"]

# Generated at 2022-06-14 04:47:57.921622
# Unit test for function semaphore
def test_semaphore():
    import os
    import unittest

    class Test_semaphore(unittest.TestCase):
        # Testing the correct behavior
        def test_semaphore_works(self):
            os.environ['BRANCH_NAME'] = 'master'
            os.environ['PULL_REQUEST_NUMBER'] = 'null'
            os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
            semaphore('master')

        # Testing if it fails when incorrect branch
        def test_semaphore_errors_on_wrong_branch(self):
            os.environ['BRANCH_NAME'] = 'master'
            os.environ['PULL_REQUEST_NUMBER'] = 'null'

# Generated at 2022-06-14 04:48:05.473397
# Unit test for function check
def test_check():
    """test check() function
    """
    # insufficiant checks
    os.environ['TRAVIS'] = "true"
    try:
        check("master")
        assert False
    except CiVerificationError:
        pass
    del os.environ['TRAVIS']

    # sufficient checks
    os.environ['TRAVIS_BRANCH'] = "master"
    os.environ['TRAVIS_PULL_REQUEST'] = "false"
    try:
        check("master")
        assert True
    except CiVerificationError:
        assert False



# Generated at 2022-06-14 04:48:09.473135
# Unit test for function circle
def test_circle():
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    check()



# Generated at 2022-06-14 04:48:10.533825
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["GITLAB_CI"] = "true"
    check()


# Generated at 2022-06-14 04:48:13.998228
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")


# Generated at 2022-06-14 04:48:28.117295
# Unit test for function semaphore
def test_semaphore():
    # Case: Successful
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "sleepy_cat"

    semaphore("master")

    # Case: PR
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "123"
    try:
        semaphore("master")
        raise Exception("This should not happen")
    except CiVerificationError:
        # This should happen
        pass

    # Case: Different branch
    os.environ["BRANCH_NAME"] = "develop"
    os.environ["PULL_REQUEST_NUMBER"] = None


# Generated at 2022-06-14 04:48:31.226472
# Unit test for function gitlab
def test_gitlab():
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    os.environ['CI_MERGE_REQUEST_ID'] = ''
    check()

# Generated at 2022-06-14 04:48:38.405946
# Unit test for function circle
def test_circle():
    os.environ.pop("CIRCLECI", None)
    os.environ.pop("CI_PULL_REQUEST", None)
    os.environ.pop("CIRCLE_BRANCH", None)
    os.environ.pop("CI_PULL_REQUEST")

    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = ""
    os.environ["CIRCLE_BRANCH"] = "master"

    check()

    os.environ["CIRCLE_BRANCH"] = "develop"

    # check() will raise an exception if the check failed
    check(branch="develop")
    # Branch not equal to master should raise an exception

# Generated at 2022-06-14 04:48:47.267823
# Unit test for function jenkins
def test_jenkins():
    """
    This function tests that the jenkins function works by testing that an exception is
    raised when it is called with incorrect values. Additionally, this function checks
    that the jenkins function does not raise an error when the correct values are given.
    """
    branch = "master"

    # We save the current environment variables.
    current_env_variables = dict(os.environ)

    # We create the environment variables to check for an enabled jenkins environment.
    os.environ["JENKINS_URL"] = "https://test.test"
    os.environ["BRANCH_NAME"] = branch
    os.environ["CHANGE_ID"] = ""

    # We check that this function does not raise an exception.
    jenkins(branch)

    # We check that the jenkins function raises an exception when

# Generated at 2022-06-14 04:48:51.597494
# Unit test for function gitlab
def test_gitlab():
    os.environ['GITLAB_CI'] = 'true'
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    os.environ['CI_PROJECT_DIR'] = 'false'
    assert check() is None

# Generated at 2022-06-14 04:48:56.348315
# Unit test for function checker
def test_checker():
    from semantic_release.errors import CiVerificationError

    @checker
    def func_with_error():
        raise AssertionError()

    try:
        func_with_error()
    except CiVerificationError:
        assert True
    except BaseException:
        assert False

# Unit tests for function check

# Generated at 2022-06-14 04:49:00.132913
# Unit test for function gitlab
def test_gitlab():
    """ Unit test for function gitlab """
    assert gitlab("master") is True
    assert gitlab("release/1.0.0") is True
    os.environ["CI_COMMIT_REF_NAME"] = "develop"
    assert gitlab("master") is False
    os.environ["CI_COMMIT_REF_NAME"] = "master"


# Generated at 2022-06-14 04:49:07.764009
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = None
    check()
    os.environ["BITBUCKET_BRANCH"] = "someotherbranch"
    check()
    del os.environ["BITBUCKET_BUILD_NUMBER"]


# Generated at 2022-06-14 04:49:17.174739
# Unit test for function jenkins
def test_jenkins():
    env = "JENKINS_URL"
    os.environ[env] = "URL"
    os.environ["GIT_BRANCH"] = 'master'
    jenkins("master")
    del os.environ[env]
    jenkins("master")

    for env in ["CHANGE_ID", "BRANCH_NAME"]:
        os.environ[env] = "anything"
        try:
            jenkins("master")
            raise AssertionError("below should have failed")
        except CiVerificationError:
            pass
        finally:
            del os.environ[env]

# Generated at 2022-06-14 04:49:21.539950
# Unit test for function bitbucket
def test_bitbucket():
    branch = "master"
    assert os.environ.get("BITBUCKET_BRANCH") == branch
    assert not os.environ.get("BITBUCKET_PR_ID")

# Generated at 2022-06-14 04:49:35.689168
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "any"
    os.environ["FRIGG_PULL_REQUEST"] = "any"
    assert frigg(branch="any") is True
    os.environ["FRIGG_PULL_REQUEST"] = None
    assert frigg(branch="any") is True
    del os.environ["FRIGG_PULL_REQUEST"]
    assert frigg(branch="any") is True
    assert frigg(branch="other") is False

# Generated at 2022-06-14 04:49:38.494275
# Unit test for function frigg
def test_frigg():
    assert frigg("master")
    assert frigg("develop")
    assert frigg("feature")

# Generated at 2022-06-14 04:49:46.171916
# Unit test for function frigg
def test_frigg():
    test_env = {"FRIGG": "true", "FRIGG_BUILD_BRANCH": "master"}
    with patch("os.environ") as mock_env:
        # Setup mock environment variables
        mock_env.dict = test_env
        mock_env.get.side_effect = os.environ.get

        # Testing if function works with frigg
        assert frigg("master") == True
        assert frigg("dev") == False
        mock_env.get.assert_any_call("FRIGG")
        mock_env.get.assert_any_call("FRIGG_BUILD_BRANCH")


# Generated at 2022-06-14 04:49:55.462503
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "https://jenkins.com/build/18"

    assert check() is None

    os.environ["JENKINS_URL"] = "https://jenkins.com/build/xx"

    try:
        check()
    except CiVerificationError as excinfo:
        print(excinfo)

    os.environ["CHANGE_ID"] = "1"
    try:
        check()
    except CiVerificationError as excinfo:
        print(excinfo)

# Generated at 2022-06-14 04:50:02.198672
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "release"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("release")

    os.environ["BITBUCKET_BRANCH"] = "release"
    os.environ["BITBUCKET_PR_ID"] = "1"
    try:
        bitbucket("release")
    except CiVerificationError:
        pass
    else:
        assert False



# Generated at 2022-06-14 04:50:06.807298
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'success'
    semaphore('master')


# Generated at 2022-06-14 04:50:07.859007
# Unit test for function travis
def test_travis():
  assert travis('master')


# Generated at 2022-06-14 04:50:11.325453
# Unit test for function check
def test_check():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS"] = "true"
    check()

# Generated at 2022-06-14 04:50:14.329831
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "abc123"
    bitbucket(branch="abc123")


# Generated at 2022-06-14 04:50:19.667326
# Unit test for function checker
def test_checker():
    """
    Test the checker decorator
    """
    @checker
    def decorated():
        raise AssertionError("I'm an assertion")

    try:
        decorated() # pylint: disable=assignment-from-no-return
    except CiVerificationError as error:
        assert str(error) == "The verification check for the environment did not pass."

# Generated at 2022-06-14 04:50:27.833891
# Unit test for function gitlab
def test_gitlab():
    def mock_get(key):
        if key == "CI_COMMIT_REF_NAME":
            return "master"
        else:
            return None
    os.environ.get = mock_get
    gitlab("master")

# Generated at 2022-06-14 04:50:39.757539
# Unit test for function semaphore
def test_semaphore():
    # Case 1 : Checking when the environment is set up correctly
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] != "failed"
    semaphore("master")
    # Case 2 : Checking when BRANCH_NAME is missing
    os.environ["BRANCH_NAME"] = None
    semaphore("master")
    # Case 3 : Checking when PULL_REQUEST_NUMBER is not None
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "test"
    semaphore("master")
    # Case 4 : Checking when SEMAPHORE_THREAD_RESULT is equal

# Generated at 2022-06-14 04:50:44.191402
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'test'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'success'
    assert semaphore('test') is True



# Generated at 2022-06-14 04:50:50.045946
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    del os.environ["FRIGG_PULL_REQUEST"]
    assert frigg("master") is True
    os.environ["FRIGG_BUILD_BRANCH"] = "dev"
    assert frigg("master") is False
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "yes"
    assert frigg("master") is False

# Generated at 2022-06-14 04:50:52.319314
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    check()

# Generated at 2022-06-14 04:51:00.247889
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "false"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")
    os.environ["SEMAPHORE"] = "false"
    os.environ["BRANCH_NAME"] = "feature"
    os.environ["PULL_REQUEST_NUMBER"] = "true"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    success = False
    try:
        semaphore("master")
    except CiVerificationError as e:
        success = True

# Generated at 2022-06-14 04:51:04.215126
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = "master"
    os.environ['TRAVIS_PULL_REQUEST'] = "false"
    travis("master")

# Generated at 2022-06-14 04:51:10.362737
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    travis('master')
    del os.environ['TRAVIS_BRANCH']
    del os.environ['TRAVIS_PULL_REQUEST']
    test_travis()


# Generated at 2022-06-14 04:51:13.472848
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BUILD_BRANCH'] = 'test'
    os.environ['FRIGG_PULL_REQUEST'] = 'False'
    frigg('test')


# Generated at 2022-06-14 04:51:21.922048
# Unit test for function gitlab
def test_gitlab():
    """
    Unit test for function gitlab
    """
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "release-branch"
    check()
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check()
    os.environ["CI_COMMIT_REF_NAME"] = "release-branch"
    os.environ["CI_MERGE_REQUEST_ID"] = "123"
    check(branch="release-branch")
    try:
        check()
    except CiVerificationError:
        pass



# Generated at 2022-06-14 04:51:35.005241
# Unit test for function checker
def test_checker():
    """
    Test the checker decorator
    """

    success = True

    # A function that is expected to raise an assertion error and return False
    @checker
    def test_func():
        assert False

    # A function that is expected to return True
    @checker
    def test_func_success():
        return True

    # Test that a function that raises an assertion error returns false
    try:
        success = test_func()
    except CiVerificationError:
        pass

    # Test that a function that returns True returns True
    success = test_func_success()

    assert not success

# Generated at 2022-06-14 04:51:38.481604
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket(branch="master")

# Generated at 2022-06-14 04:51:40.056994
# Unit test for function frigg
def test_frigg():
    assert frigg("master")

# Generated at 2022-06-14 04:51:44.754610
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = "master"
    os.environ['BITBUCKET_PR_ID'] = 0
    assert bitbucket() == True
    os.environ['BITBUCKET_PR_ID'] = 1
    assert bitbucket() == False


# Generated at 2022-06-14 04:51:52.026040
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master") == True
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        travis("master")
        assert False
    except:
        assert True


# Generated at 2022-06-14 04:51:59.103357
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "false"

    frigg("master")
    del os.environ["FRIGG"]
    del os.environ["FRIGG_BUILD_BRANCH"]
    del os.environ["FRIGG_PULL_REQUEST"]


# Generated at 2022-06-14 04:52:01.433794
# Unit test for function frigg
def test_frigg():
    assert frigg("master")
    assert frigg("develop")
    assert frigg("new_feature")
    assert frigg("hotfix")
    assert frigg("release")



# Generated at 2022-06-14 04:52:03.075025
# Unit test for function frigg
def test_frigg():
    assert frigg("master")


# Generated at 2022-06-14 04:52:05.474018
# Unit test for function semaphore
def test_semaphore():
    assert semaphore('master') is True


# Generated at 2022-06-14 04:52:11.418342
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check()

    os.environ["CI_COMMIT_REF_NAME"] = "release"
    check(branch="release")


# Generated at 2022-06-14 04:52:25.351502
# Unit test for function jenkins
def test_jenkins():
    os.environ.setdefault("JENKINS_URL","https://jenkins.com")
    os.environ.setdefault("BRANCH_NAME", "master")
    os.environ.setdefault("CHANGE_ID", "11")
    os.environ.setdefault("GIT_BRANCH", "master")
    assert jenkins("master") == True
    os.environ.setdefault("JENKINS_URL","https://jenkins.com")
    os.environ.setdefault("BRANCH_NAME", "develop")
    os.environ.setdefault("CHANGE_ID", "11")
    os.environ.setdefault("GIT_BRANCH", "master")
    assert jenkins("develop") == False

# Generated at 2022-06-14 04:52:28.212296
# Unit test for function checker
def test_checker():
    with pytest.raises(CiVerificationError):
        @checker
        def test_function():
            raise AssertionError("Test function raised a testing error")

        test_function()


# Generated at 2022-06-14 04:52:40.419877
# Unit test for function jenkins
def test_jenkins():
    test = False
    try:
        os.environ["JENKINS_URL"] = "http://localhost"
        os.environ["GIT_BRANCH"] = "develop"
        check("develop")
    except CiVerificationError:
        test = True

    assert not test

    test = False
    try:
        os.environ["GIT_BRANCH"] = "master"
        check("develop")
    except CiVerificationError:
        test = True

    assert test

    test = False
    try:
        os.environ["GIT_BRANCH"] = "master"
        os.environ["CHANGE_ID"] = "1234"
        check("master")
    except CiVerificationError:
        test = True

    assert test

# Generated at 2022-06-14 04:52:41.437967
# Unit test for function jenkins
def test_jenkins():
    jenkins('master')

# Generated at 2022-06-14 04:52:46.705960
# Unit test for function check
def test_check():
    os.environ['TRAVIS'] = "true"
    os.environ['TRAVIS_BRANCH'] = "master"
    os.environ['TRAVIS_PULL_REQUEST'] = "false"
    check()
    os.environ['TRAVIS_BRANCH'] = "test"
    try:
        check()
    except Exception:
        pass
    os.environ['TRAVIS_PULL_REQUEST'] = "true"
    try:
        check()
    except Exception:
        pass

# Generated at 2022-06-14 04:52:50.111548
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "http://localhost:8080/"
    os.environ["BRANCH_NAME"] = "master"
    jenkins("master")

# Generated at 2022-06-14 04:52:56.281253
# Unit test for function checker
def test_checker():
    def this_should_pass():
        assert True
    isinstance(checker(this_should_pass)(), bool)

    def this_should_fail():
        assert False
    try:
        checker(this_should_fail)()
    except CiVerificationError:
        pass
    else:
        raise AssertionError(
            "CiVerificationError was not raised on failed assertion."
        )

# Generated at 2022-06-14 04:53:04.097918
# Unit test for function bitbucket
def test_bitbucket():
    assert bitbucket(branch="master") is True
    os.environ['BITBUCKET_BUILD_NUMBER'] = None
    assert bitbucket(branch="master") is True
    os.environ['BITBUCKET_BRANCH'] = "master"
    assert bitbucket(branch="master") is True
    os.environ['BITBUCKET_PR_ID'] = 1
    assert bitbucket(branch="master") is False

# Generated at 2022-06-14 04:53:09.214083
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "Test"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = "Yes"
    check()
    os.environ["CHANGE_ID"] = None
    check()

# Generated at 2022-06-14 04:53:17.811429
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "not-failed"

    semaphore(branch="master")

    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"

    try:
        semaphore(branch="master")
    except CiVerificationError:
        pass
    else:
        assert False, "Semaphore should have raised a verification error"



# Generated at 2022-06-14 04:53:37.975346
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = 'true'
    os.environ['CIRCLE_BRANCH'] = 'branch'
    os.environ['CI_PULL_REQUEST'] = 'PR'
    assert circle('branch')

    os.environ.pop('CI_PULL_REQUEST')
    assert circle('branch')
    del os.environ['CIRCLECI']
    del os.environ['CIRCLE_BRANCH']


# Generated at 2022-06-14 04:53:39.173641
# Unit test for function frigg
def test_frigg():
    assert frigg("master")
    assert frigg("master")

# Generated at 2022-06-14 04:53:43.825710
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "my-pull-request"

    check(branch="my-branch")
    assert os.environ["BITBUCKET_BRANCH"] == "master"
    assert os.environ["BITBUCKET_PR_ID"] == "my-pull-request"

# Generated at 2022-06-14 04:53:50.419975
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://jenkins.com/"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = None

    check()
    del os.environ["JENKINS_URL"]
    del os.environ["BRANCH_NAME"]
    del os.environ["CHANGE_ID"]

# Generated at 2022-06-14 04:53:57.779810
# Unit test for function semaphore
def test_semaphore():
    semaphore('master')
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'failed'
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    try:
        semaphore('master')
        raise AssertionError('Assertion error not raised')
    except CiVerificationError as e:
        pass
    del os.environ['SEMAPHORE_THREAD_RESULT']
    os.environ['SEMAPHORE_THREAD_RESULT'] = ''
    try:
        semaphore('master')
        raise AssertionError('Assertion error not raised')
    except CiVerificationError as e:
        pass

# Generated at 2022-06-14 04:54:08.881349
# Unit test for function circle
def test_circle():
    """
    Test that correct setup of circleci is detected and the function behaves
    correctly.
    """
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "3"
    os.environ["CIRCLE_BRANCH"] = "master"

    check(branch="master")

    os.environ["CIRCLE_BRANCH"] = "other_branch"

    try:
        check(branch="other_branch")
        assert False, "Should raise a CiVerificationError"
    except CiVerificationError:
        pass

    os.environ["CI_PULL_REQUEST"] = "yes"


# Generated at 2022-06-14 04:54:12.077000
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"

    check(branch="master")



# Generated at 2022-06-14 04:54:16.836120
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "develop"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS"] = "true"
    travis("develop")


# Generated at 2022-06-14 04:54:20.184142
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"

    semaphore("master")


# Generated at 2022-06-14 04:54:29.072535
# Unit test for function gitlab
def test_gitlab():
    """
    Adds environment variable to simulate a correct gitlab build
    """
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    assert gitlab("master")
    # Add environment variable to simulate an incorrect gitlab build
    os.environ["CI_COMMIT_REF_NAME"] = "develop"
    del os.environ["CI_COMMIT_REF_NAME"]
    assert not gitlab("master")
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = "1"
    assert not gitlab("master")
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    del os.environ["CI_MERGE_REQUEST_ID"]

# Generated at 2022-06-14 04:55:01.575141
# Unit test for function bitbucket
def test_bitbucket():
    """
    A simple test to ensure that the names of the environment
    variables for bitbucket are correct.
    """
    try:
        bitbucket("master")
        assert False, "This should fail"
    except CiVerificationError:
        assert True
    assert bitbucket.__name__ == "bitbucket"