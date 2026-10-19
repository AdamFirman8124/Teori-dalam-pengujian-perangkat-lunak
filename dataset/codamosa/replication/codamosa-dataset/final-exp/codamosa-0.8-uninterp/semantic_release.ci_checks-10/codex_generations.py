

# Generated at 2022-06-14 04:45:13.767395
# Unit test for function checker
def test_checker():
    @checker
    def failing_function():
        assert False

    @checker
    def succeeding_function():
        assert True

    try:
        failing_function()
        assert False
    except CiVerificationError:
        pass

    succeeding_function()

# Generated at 2022-06-14 04:45:19.987333
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master")

    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "1"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    try:
        semaphore("master")
    except CiVerificationError:
        return True

    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None

# Generated at 2022-06-14 04:45:31.738411
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = "https://travis-ci.org/relekang/semantic-release"
    os.environ['BRANCH_NAME'] = "master"
    os.environ.pop('CHANGE_ID', None)
    jenkins()

    os.environ['GIT_BRANCH'] = "master"
    os.environ.pop('BRANCH_NAME', None)
    jenkins()

    os.environ.pop('JENKINS_URL', None)
    os.environ['CHANGE_ID'] = "12345"
    with pytest.raises(CiVerificationError) as exception_info:
        jenkins()

# Generated at 2022-06-14 04:45:36.464042
# Unit test for function gitlab
def test_gitlab():
  """
  Unit test for function gitlab

  :param branch: The branch the environment should be running against.
  """
  os.environ['CI_COMMIT_REF_NAM'] = "master"
  os.environ['CI_PROJECT_NAME'] = "test"
  os.environ['CI_COMMIT_MESSAGE'] = "Release 2.0.0"
  os.environ['CI_MERGE_REQUEST_ID'] = None
  assert check()

# Generated at 2022-06-14 04:45:36.847404
# Unit test for function check
def test_check():
    pass

# Generated at 2022-06-14 04:45:47.976131
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'TEST'
    os.environ['BRANCH_NAME'] = 'TEST'
    check()
    os.environ['GIT_BRANCH'] = 'TEST'
    check()
    os.environ['CHANGE_ID'] = 'TEST'
    try:
        check()
    except CiVerificationError as e:
        assert e.args[0] == "The verification check for the environment did not pass."
    del os.environ['CHANGE_ID']
    check()
    os.environ['BRANCH_NAME'] = 'NOT_TEST'
    try:
        check()
    except CiVerificationError as e:
        assert e.args[0] == "The verification check for the environment did not pass."
    del os

# Generated at 2022-06-14 04:45:52.186642
# Unit test for function circle
def test_circle():
    """
    Checks that the correct environment variable was returned
    """
    os.environ['CIRCLECI'] = 'true'
    os.environ['CI_PULL_REQUEST'] = 'false'
    assert check("master") == True

# Generated at 2022-06-14 04:45:55.164057
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "test"
    os.environ["BITBUCKET_BRANCH"] = "test"
    bitbucket("test")

# Generated at 2022-06-14 04:46:02.169955
# Unit test for function jenkins
def test_jenkins():
    """
    Performs necessary checks to ensure that the jenkins build is one
    that should create releases.

    :param branch: The branch the environment should be running against.
    """

    assert os.environ.get("BRANCH_NAME") == "master"
    assert os.environ.get("JENKINS_URL") is not None
    # assert os.environ.get("GIT_BRANCH") == "master"
    assert not os.environ.get("CHANGE_ID")  # pull request id

# Generated at 2022-06-14 04:46:09.634524
# Unit test for function circle
def test_circle():
    # Setup
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"

    # Execute
    circle("master")

    # Verify
    del os.environ["CIRCLECI"]
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CI_PULL_REQUEST"]


# Generated at 2022-06-14 04:46:28.889945
# Unit test for function bitbucket
def test_bitbucket():
    # Verify bitbucket checks returns true when environment variables are set appropriately.

    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = None
    assert bitbucket("master") is True

    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "12"
    assert bitbucket("master") is False

    os.environ["BITBUCKET_BRANCH"] = "master"
    assert bitbucket("master") is True

    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "12"
    assert bitbucket("master") is False



# Generated at 2022-06-14 04:46:37.692002
# Unit test for function frigg
def test_frigg():
    """
    testing function frigg
    """
    os.environ["FRIGG_PULL_REQUEST"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    with pytest.raises(CiVerificationError):
        frigg("master")
    os.environ.pop("FRIGG_PULL_REQUEST")
    assert frigg("master") == True
    os.environ.pop("FRIGG_BUILD_BRANCH")
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    with pytest.raises(CiVerificationError):
        semaph

# Generated at 2022-06-14 04:46:39.956536
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "True"
    os.environ["GIT_BRANCH"] = "master"
    check()



# Generated at 2022-06-14 04:46:50.568841
# Unit test for function semaphore
def test_semaphore():
    import os
    import shutil
    os.mkdir("test")
    os.chdir("test")
    os.chdir("..")
    filename = "semaphore.txt"
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, "w") as f:
        pass
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "None"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    check("master")
    os.remove(filename)
    shutil.rmtree("test")

# Generated at 2022-06-14 04:46:54.844017
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg("master")



# Generated at 2022-06-14 04:47:01.977694
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "none"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    semaphore("master")
    del os.environ["BRANCH_NAME"]
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["SEMAPHORE_THREAD_RESULT"]


# Generated at 2022-06-14 04:47:05.744815
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"

    bitbucket("master")
    print("Bitbucket integration test completed successfully")


# Generated at 2022-06-14 04:47:08.388989
# Unit test for function semaphore
def test_semaphore():
    """
    Unit test for function semaphore
    """
    pass

# Generated at 2022-06-14 04:47:16.989487
# Unit test for function jenkins
def test_jenkins():
    
    # Test to see if the function works properly.
    # Result should be True.
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "https://url.com"
    os.environ["CHANGE_ID"] = "0"
    assert jenkins("master") == True
    
    # Test to see if the function fails when the commit is not on master branch.
    # Result should be False.
    os.environ["BRANCH_NAME"] = "testing"
    os.environ["JENKINS_URL"] = "https://url.com"
    os.environ["CHANGE_ID"] = "0"
    assert jenkins("master") == False
    
    # Test to see if the function fails when the the environment is

# Generated at 2022-06-14 04:47:19.909214
# Unit test for function bitbucket
def test_bitbucket():
    """
    Unit test for function: bitbucket()
    """
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    assert bitbucket(branch="master") == True

# Generated at 2022-06-14 04:47:36.513642
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = 'true'
    os.environ['CIRCLE_BRANCH'] = 'master'
    os.environ['CI_PULL_REQUEST'] = ''
    check(branch='master')

# Generated at 2022-06-14 04:47:49.226632
# Unit test for function semaphore
def test_semaphore():
    # Positive test case
    os.environ.update(
        {
            "SEMAPHORE": "true",
            "BRANCH_NAME": "master",
            "SEMAPHORE_THREAD_RESULT": "passed",
            "SEMAPHORE_REPO_SLUG": "vinothkumar/test",
        }
    )
    semaphore("master")

    # Negative test case
    os.environ.update(
        {
            "SEMAPHORE": "true",
            "BRANCH_NAME": "master",
            "SEMAPHORE_THREAD_RESULT": "failed",
            "SEMAPHORE_REPO_SLUG": "vinothkumar/test",
        }
    )

# Generated at 2022-06-14 04:47:52.788609
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master")


# Generated at 2022-06-14 04:48:00.927444
# Unit test for function frigg
def test_frigg():
    os.environ.update({"FRIGG": "true", "FRIGG_BUILD_BRANCH": "test_branch"})
    check("test_branch")
    os.environ.update({"FRIGG": "true", "FRIGG_BUILD_BRANCH": "test_branch", "FRIGG_PULL_REQUEST": "true"})
    try:
        check("test_branch")
        raise AssertionError("Should not reach this line")
    except CiVerificationError:
        pass
    del os.environ["FRIGG"]
    os.environ.update({"FRIGG": "true", "FRIGG_BUILD_BRANCH": "another_branch"})

# Generated at 2022-06-14 04:48:11.229237
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "localhost:8080"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = ""
    assert check()
    os.environ["JENKINS_URL"] = "localhost:8080"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = "foo"
    assert not check()



# Generated at 2022-06-14 04:48:16.262341
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")
    assert True


# Generated at 2022-06-14 04:48:18.163788
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = None
    gitlab("master")


# Generated at 2022-06-14 04:48:21.321770
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check()
    os.environ["CI_COMMIT_REF_NAME"] = None
    assert check() is None



# Generated at 2022-06-14 04:48:25.349894
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = ''
    os.environ['CIRCLE_BRANCH'] = 'foo'
    os.environ['CI_PULL_REQUEST'] = ''

    with pytest.raises(CiVerificationError) as exception_info:
        check()

    assert str(exception_info.value) == "The verification check for the environment did not pass."


# Generated at 2022-06-14 04:48:31.597987
# Unit test for function semaphore
def test_semaphore():
    import os
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = None
    semaphore('master')
    # Check pull request branch
    os.environ['BRANCH_NAME'] = 'test'
    os.environ['PULL_REQUEST_NUMBER'] = 'test'
    with pytest.raises(CiVerificationError):
        semaphore('emaster')
    # Check failed branch
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'failed'
    with pytest.raises(CiVerificationError):
        semaphore

# Generated at 2022-06-14 04:49:00.368933
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "some_value"
    os.environ["BRANCH_NAME"] = "test_branch"
    os.environ["CHANGE_ID"] = "some_value"
    try:
        jenkins("test_branch")
    except CiVerificationError:
        assert True
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = None
    try:
        jenkins("master")
    except CiVerificationError:
        assert False
    assert True

# Generated at 2022-06-14 04:49:12.118843
# Unit test for function jenkins
def test_jenkins():
    def test_jenkins_details(env_settings):
        env = os.environ.copy()
        env.update(env_settings)
        try:
            jenkins("master")
        except:
            assert False
        else:
            assert True

    test_jenkins_details({"JENKINS_URL": "example.com", "GIT_BRANCH": "master"})

    # test_jenkins_details(
    #     {"JENKINS_URL": "example.com", "GIT_BRANCH": "master", "CHANGE_ID": "123"}
    # )

    # test_jenkins_details({"JENKINS_URL": "example.com", "GIT_BRANCH": "not_master"})

    # test_jenkins_details({"JENKINS

# Generated at 2022-06-14 04:49:15.166652
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "Release/8.0"

    check()


# Generated at 2022-06-14 04:49:21.038687
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "release-test"
    gitlab("release-test")

    os.environ["CI_COMMIT_REF_NAME"] = "release-test-2"
    try:
        gitlab("release-test")
    except CiVerificationError:
        pass

    os.environ["CI_COMMIT_REF_NAME"] = "release-test"
    os.environ["GITLAB_MERGE_REQUEST_ID"] = "1"
    try:
        gitlab("release-test")
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:49:27.379786
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = ""
    os.environ["CIRCLE_BRANCH"] = "master"
    check()
    assert os.environ["CI_PULL_REQUEST"] == ""
    assert os.environ["CIRCLE_BRANCH"] == "master"


# Generated at 2022-06-14 04:49:28.286536
# Unit test for function frigg
def test_frigg():
	assert frigg("master") is True

# Generated at 2022-06-14 04:49:35.821008
# Unit test for function semaphore
def test_semaphore():
    """
    Unit test for function semaphore
    """
    os.environ["BRANCH_NAME"] = "master"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    os.environ["PULL_REQUEST_NUMBER"] = None
    assert semaphore("master") == False
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master") == True


# Generated at 2022-06-14 04:49:39.734668
# Unit test for function frigg
def test_frigg():

    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"

    frigg("master")



# Generated at 2022-06-14 04:49:46.155194
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = 'false'
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ['FRIGG_PULL_REQUEST'] = '12345'

    branch = 'master'
    try:
        frigg(branch)
    except CiVerificationError:
        pass

    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ['FRIGG_PULL_REQUEST'] = '12345'

    try:
        frigg(branch)
    except CiVerificationError:
        assert False

    os.environ['FRIGG'] = 'true'

# Generated at 2022-06-14 04:49:56.316507
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ.setdefault('FRIGG_PULL_REQUEST', 'false')
    frigg('master')
    os.environ['FRIGG_PULL_REQUEST'] = 'true'
    try:
        frigg('master')
    except Exception:
        pass
    del os.environ['FRIGG']
    del os.environ['FRIGG_BUILD_BRANCH']
    del os.environ['FRIGG_PULL_REQUEST']


# Generated at 2022-06-14 04:50:46.662661
# Unit test for function checker
def test_checker():
    @checker
    def is_empty(value: str) -> bool:
        assert not value

    is_empty("this will fail")



# Generated at 2022-06-14 04:50:49.673492
# Unit test for function checker
def test_checker():
    @checker
    def func():
        raise AssertionError

    try:
        func()
    except CiVerificationError:
        pass
    except Exception as e:
        assert False, e


# Unit tests for the actual CI checkers

# Generated at 2022-06-14 04:50:57.323735
# Unit test for function checker
def test_checker():

    @checker
    def raise_assertionerror():
        assert False

    @checker
    def raise_other():
        raise ValueError

    # this should not raise
    assert raise_assertionerror() is True

    try:
        raise_other()
    except CiVerificationError:
        pass
    else:
        assert False, "Should have raised."

    try:
        raise_assertionerror()
    except CiVerificationError:
        pass
    else:
        assert False, "Should have raised."

# Generated at 2022-06-14 04:51:00.062506
# Unit test for function gitlab
def test_gitlab():
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    os.environ['CI_MERGE_REQUEST_ID'] = None
    assert check()

# Generated at 2022-06-14 04:51:04.026460
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check()
    del os.environ["CI_COMMIT_REF_NAME"]



# Generated at 2022-06-14 04:51:08.346140
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg("master")
    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    frigg("develop")



# Generated at 2022-06-14 04:51:15.699527
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "False"

    check()
    os.environ.pop("FRIGG", None)
    os.environ.pop("FRIGG_BUILD_BRANCH", None)
    os.environ.pop("FRIGG_PULL_REQUEST", None)
    check()


# Generated at 2022-06-14 04:51:19.723847
# Unit test for function check
def test_check():
    """
    Tests that check is working as intended.
    """
    def test_func(branch="master"):
        """
        Test function.
        :param branch:
        :return:
        """
        pass

    assert checker(test_func)()

# Generated at 2022-06-14 04:51:27.415544
# Unit test for function bitbucket
def test_bitbucket():
    assert os.environ.get("BITBUCKET_BRANCH") == None
    assert os.environ.get("BITBUCKET_PR_ID") == None
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("master")
    del os.environ["BITBUCKET_BRANCH"]
    del os.environ["BITBUCKET_PR_ID"]

# Generated at 2022-06-14 04:51:29.457897
# Unit test for function travis
def test_travis():
    assert travis(branch="master")
    assert travis(branch="dev")


# Generated at 2022-06-14 04:52:59.610425
# Unit test for function jenkins
def test_jenkins():
    branch = "master"
    assert jenkins(branch) == True
    branch = "test"
    assert jenkins(branch) == False

# Generated at 2022-06-14 04:53:05.614762
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_SOURCE_PROJECT_NAME"] = ""

    check(branch="master")

    del os.environ["CI_COMMIT_REF_NAME"]
    del os.environ["CI_MERGE_REQUEST_SOURCE_PROJECT_NAME"]

# Generated at 2022-06-14 04:53:09.821919
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = ''
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    semaphore('master')



# Generated at 2022-06-14 04:53:14.402824
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    circle("master")

# Generated at 2022-06-14 04:53:22.256590
# Unit test for function semaphore
def test_semaphore():
    """Test semaphore function.
    Define environment variables for semaphore, then test func semaphore
    """
    os.environ["SEMAPHORE"] = "true"
    os.environ["PULL_REQUEST_NUMBER"] = "None"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ["BRANCH_NAME"] = "master"
    assert semaphore("master") == True

    os.environ["SEMAPHORE"] = "true"
    os.environ["PULL_REQUEST_NUMBER"] = "1"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ["BRANCH_NAME"] = "master"

# Generated at 2022-06-14 04:53:23.762596
# Unit test for function circle
def test_circle():
    assert checker(circle)('master')


# Generated at 2022-06-14 04:53:33.446379
# Unit test for function bitbucket
def test_bitbucket():
    class Test:
        """
        Mocking BITBUCKET_BUILD_NUMBER and BITBUCKET_PULLREQUEST_ID to test 
        """

        def __init__(self):
            self.BITBUCKET_BUILD_NUMBER = 1
            self.BITBUCKET_PULLREQUEST_ID = 2
            self.BITBUCKET_BRANCH = 3
            self.BITBUCKET_COMMIT = 4
            self.BITBUCKET_REPO_SLUG = 5
            self.BITBUCKET_TAG = 6
            self.BITBUCKET_COMMITTER = 7
            self.BITBUCKET_FILEPATH = 8
            self.BITBUCKET_PR_ID = None
            self.BITBUCKET_PULLREQUEST_TITLE = 9

# Generated at 2022-06-14 04:53:37.245249
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["GITLAB_CI"] = "true"

    check()

    assert os.environ.get("GITLAB_CI") == "true"



# Generated at 2022-06-14 04:53:40.575702
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME']='master'
    os.environ['PULL_REQUEST_NUMBER']=None
    os.environ['SEMAPHORE_THREAD_RESULT']='success'
    branch = "master"
    semaphore(branch)

# Generated at 2022-06-14 04:53:48.746487
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = "true"
    os.environ['FRIGG_BUILD_BRANCH'] = "master"
    os.environ['FRIGG_PULL_REQUEST'] = None

    check("master")
    del os.environ['FRIGG']
    del os.environ['FRIGG_BUILD_BRANCH']
    del os.environ['FRIGG_PULL_REQUEST']
