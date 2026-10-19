

# Generated at 2022-06-14 04:45:13.905535
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("master")
    os.environ["BITBUCKET_PR_ID"] = "16"
    bitbucket("master")


# Generated at 2022-06-14 04:45:17.163841
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "false"
    os.environ["CIRCLE_BRANCH"] = "master"
    
    assert check()



# Generated at 2022-06-14 04:45:22.440640
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    travis('master')
    del os.environ['TRAVIS_BRANCH']
    del os.environ['TRAVIS_PULL_REQUEST']


# Generated at 2022-06-14 04:45:33.776370
# Unit test for function semaphore
def test_semaphore():
    assert semaphore("master") == True

    from semantic_release.errors import CiVerificationError

    try:
        semaphore("master1")
    except CiVerificationError:
        assert True
    else:
        assert False

    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    try:
        semaphore("master")
    except CiVerificationError:
        assert True
    else:
        assert False

    os.environ["PULL_REQUEST_NUMBER"] = "pull_request_number"
    try:
        semaphore("master")
    except CiVerificationError:
        assert True
    else:
        assert False

    del os.environ["SEMAPHORE_THREAD_RESULT"]

# Generated at 2022-06-14 04:45:39.098105
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "CI_SERVER_URL"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = None
    check("master")

# Generated at 2022-06-14 04:45:43.722911
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "3"
    os.environ["BITBUCKET_BRANCH"] = "test"
    os.environ["BITBUCKET_PR_ID"] = "4"
    check()



# Generated at 2022-06-14 04:45:51.083705
# Unit test for function jenkins
def test_jenkins():
    # Arrange
    os.environ["JENKINS_URL"] = "https://jenkins.com"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = "1234"

    # Act
    try:
        jenkins("master")
    # Assert - if no exception raises, the test passes.
    except CiVerificationError:
        assert False

# Generated at 2022-06-14 04:45:54.295563
# Unit test for function circle
def test_circle():

    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"

    check()



# Generated at 2022-06-14 04:46:03.491573
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "develop"
    os.environ["PULL_REQUEST_NUMBER"] = "12345"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    try:
        semaphore("develop")
        assert False
    except CiVerificationError:
        pass
    del os.environ["BRANCH_NAME"]
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["SEMAPHORE_THREAD_RESULT"]
    try:
        semaphore("develop")
        assert False
    except CiVerificationError:
        pass
    os.environ["BRANCH_NAME"] = "master"

# Generated at 2022-06-14 04:46:09.199240
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "1"
    try:
        check()
    except CiVerificationError:
        return
    raise AssertionError



# Generated at 2022-06-14 04:46:27.556280
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    try:
        circle("master")
    except CiVerificationError as e:
        assert "The verification check for the environment did not pass." == str(e)

    os.environ["CIRCLECI"] = "false"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "1"
    try:
        circle("master")
    except CiVerificationError as e:
        assert "The verification check for the environment did not pass." == str(e)

    os.environ["CIRCLECI"] = "true"

# Generated at 2022-06-14 04:46:31.300117
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    semaphore('master')
    

# Generated at 2022-06-14 04:46:33.471230
# Unit test for function circle
def test_circle():
    """
    Test circle function
    """
    assert os.environ.get("CIRCLECI") == "true"


# Generated at 2022-06-14 04:46:39.136964
# Unit test for function jenkins
def test_jenkins():
    branch = "master"
    os.environ["BRANCH_NAME"] = branch
    os.environ["JENKINS_URL"] = "https://example.com"
    os.environ["CHANGE_ID"] = ""
    assert jenkins(branch)

# Generated at 2022-06-14 04:46:42.159061
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()


# Generated at 2022-06-14 04:46:53.173256
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    del os.environ["TRAVIS"]
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ["PULL_REQUEST_NUMBER"] = None
    check()
    del os.environ["SEMAPHORE"]
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"


# Generated at 2022-06-14 04:46:57.812929
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = "true"
    os.environ['FRIGG_PULL_REQUEST'] = "1"
    try:
        frigg("master")
        assert False
    except CiVerificationError:
        assert True

# Generated at 2022-06-14 04:47:03.403838
# Unit test for function semaphore
def test_semaphore():
    """
    Unit test for function semaphore
    """
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore(branch="master")



# Generated at 2022-06-14 04:47:09.844402
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "random"
    test_result = bitbucket("master")
    assert test_result == False

    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    test_result = bitbucket("master")
    assert test_result == True

# Generated at 2022-06-14 04:47:16.020114
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "5"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "123"

    try:
        bitbucket(branch="master")
    except CiVerificationError as e:
        assert str(e) == "The verification check for the environment did not pass."
    else:
        assert False, "Verification check should have failed."



# Generated at 2022-06-14 04:47:27.228154
# Unit test for function checker
def test_checker():
    # Test for when function does not raise an error
    @checker
    def true_test():
        assert True

    assert true_test()

    # Test for when function raises an error
    @checker
    def false_test():
        assert False

    try:
        false_test()
        raise AssertionError("checker raised no error.")
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:47:32.227612
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "develop"
    os.environ["PULL_REQUEST_NUMBER"] = "34"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    try:
        semaphore("master")
    except CiVerificationError:
        pass
    else:
        assert False

    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["SEMAPHORE_THREAD_RESULT"]



# Generated at 2022-06-14 04:47:36.362769
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = "true"
    os.environ['CIRCLE_BRANCH'] = "master"
    os.environ['CI_PULL_REQUEST'] = ""
    circle("master")



# Generated at 2022-06-14 04:47:40.574881
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_IID"] = "123"
    check()
    assert 1 == 1  # pass

test_gitlab()

# Generated at 2022-06-14 04:47:52.962704
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "development"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    with pytest.raises(CiVerificationError):
        check()
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    with pytest.raises(CiVerificationError):
        check()
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS"] = "false"
    os.environ["SEMAPHORE"] = "true"

# Generated at 2022-06-14 04:48:00.138289
# Unit test for function bitbucket
def test_bitbucket():
    env = {
        "BITBUCKET_BUILD_NUMBER": "123456",
        "BITBUCKET_BRANCH": "master",
    }
    os.environ.update(env)
    assert os.environ.get("BITBUCKET_BUILD_NUMBER") == "123456"
    assert os.environ.get("BITBUCKET_BRANCH") == "master"
    bitbucket("master")
    assert os.environ.get("BITBUCKET_BUILD_NUMBER") == "123456"
    assert os.environ.get("BITBUCKET_BRANCH") == "master"



# Generated at 2022-06-14 04:48:01.007116
# Unit test for function checker
def test_checker():
    def test_func():
        pass

    assert checker(test_func)() == True

# Generated at 2022-06-14 04:48:12.491106
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master")

    os.environ.pop("BRANCH_NAME")
    assert not semaphore("master")

    os.environ["BRANCH_NAME"] = "dev"
    assert not semaphore("master")

    os.environ["PULL_REQUEST_NUMBER"] = "10"
    assert not semaphore("master")

    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert not semaphore("master")

# Generated at 2022-06-14 04:48:23.703757
# Unit test for function check
def test_check():
    """
    Test if the check function work.
    """
    branch = "master"
    os.environ["TRAVIS"] = "true"
    check(branch)

    os.environ["SEMAPHORE"] = "true"
    check(branch)

    os.environ["FRIGG"] = "true"
    check(branch)

    os.environ["CIRCLECI"] = "true"
    check(branch)

    os.environ["BITBUCKET_BUILD_NUMBER"] = "1234"
    check(branch)

    os.environ["GITLAB_CI"] = "true"
    check(branch)

    os.environ["JENKINS_URL"] = "url"
    check(branch)

# Generated at 2022-06-14 04:48:27.397482
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"

    check()

# Generated at 2022-06-14 04:48:36.551785
# Unit test for function gitlab
def test_gitlab():
    assert os.environ.get("GITLAB_CI") == "true"

# Generated at 2022-06-14 04:48:40.703956
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    assert check()
    os.environ["CI_COMMIT_REF_NAME"] = "develop"
    assert check("develop")
    del os.environ["CI_COMMIT_REF_NAME"]


# Generated at 2022-06-14 04:48:45.386464
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"

    check()

    del os.environ["FRIGG"]
    del os.environ["FRIGG_BUILD_BRANCH"]

# Generated at 2022-06-14 04:48:48.884340
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "test"
    frigg("test")



# Generated at 2022-06-14 04:48:51.985305
# Unit test for function gitlab
def test_gitlab():
    os.environ.update(GITLAB_CI='true',CI_COMMIT_REF_NAME='master')
    check()
    os.environ.clear()


# Generated at 2022-06-14 04:48:55.579088
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = "true"
    os.environ['FRIGG_BUILD_BRANCH'] = "dev"
    frigg("dev")


# Generated at 2022-06-14 04:48:59.681430
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    gitlab("master")
    os.environ["CI_COMMIT_REF_NAME"] = "dev"
    with pytest.raises(CiVerificationError):
        gitlab("master")

    assert \
        os.environ["CI_COMMIT_REF_NAME"] == "dev"

# Generated at 2022-06-14 04:49:11.604881
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = 'master'
    os.environ["JENKINS_URL"] = "https://jenkins_server/job/my_job/"
    os.environ["CHANGE_ID"] = ""
    jenkins('master')
    os.environ.pop("BRANCH_NAME")
    os.environ["GIT_BRANCH"] = 'master'
    os.environ["JENKINS_URL"] = "https://jenkins_server/job/my_job/"
    os.environ["CHANGE_ID"] = ""
    jenkins('master')
    os.environ.pop("GIT_BRANCH")
    os.environ.pop("JENKINS_URL")

# Generated at 2022-06-14 04:49:14.419845
# Unit test for function checker
def test_checker():
    with pytest.raises(CiVerificationError):
        @checker
        def good():
            assert True

        @checker
        def bad():
            assert False
        bad()

# Generated at 2022-06-14 04:49:15.827769
# Unit test for function travis
def test_travis():
    assert travis(branch = "master")


# Generated at 2022-06-14 04:49:33.819525
# Unit test for function gitlab
def test_gitlab():
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    os.environ['CI_MERGE_REQUEST_SOURCE_BRANCH_NAME'] = 'master'
    check('master')
    check('dev')
    os.environ['CI_COMMIT_REF_NAME'] = 'dev'
    os.environ['CI_MERGE_REQUEST_SOURCE_BRANCH_NAME'] = 'master'
    check('master')
    check('dev')
    del os.environ['CI_COMMIT_REF_NAME']
    del os.environ['CI_MERGE_REQUEST_SOURCE_BRANCH_NAME']


# Generated at 2022-06-14 04:49:36.553942
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"

    assert travis("master")



# Generated at 2022-06-14 04:49:41.270860
# Unit test for function checker
def test_checker():
    @checker
    def raise_value():
        raise AssertionError("Raised an AssertionError.")

    # assert the function raises the correct exception
    try:
        raise_value()
    except CiVerificationError:
        pass



# Generated at 2022-06-14 04:49:45.992161
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    assert bitbucket("master") is True
    del os.environ["BITBUCKET_BRANCH"]
    assert bitbucket("master") is False

    os.environ["BITBUCKET_PR_ID"] = "12"
    assert bitbucket("master") is False
    del os.environ["BITBUCKET_PR_ID"]

# Generated at 2022-06-14 04:49:49.875864
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "testbranch"
    frigg("testbranch")


# Generated at 2022-06-14 04:49:52.962483
# Unit test for function circle
def test_circle():
    os.environ.update({
        "CIRCLE_BRANCH": "master",
        "CIRCLE_PULL_REQUEST": ""
    })
    check()



# Generated at 2022-06-14 04:50:01.941826
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "false"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master") == True
    del os.environ["SEMAPHORE"]
    del os.environ["BRANCH_NAME"]
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["SEMAPHORE_THREAD_RESULT"]


# Generated at 2022-06-14 04:50:13.032430
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "dev"
    os.environ["FRIGG_PULL_REQUEST"] = ""

    check("dev")
    os.environ.pop("FRIGG_BUILD_BRANCH")
    with pytest.raises(CiVerificationError) as exc:
        check("dev")
        assert exc.value.args[0] == "The verification check for the environment did not pass."

    os.environ["FRIGG_BUILD_BRANCH"] = "test"
    with pytest.raises(CiVerificationError) as exc:
        check("dev")
        assert exc.value.args[0] == "The verification check for the environment did not pass."

   

# Generated at 2022-06-14 04:50:17.989455
# Unit test for function jenkins
def test_jenkins():
    """
    Tests the function jenkins
    """
    os.environ["BRANCH_NAME"] = "feature/test"
    os.environ["JENKINS_URL"] = "test"
    os.environ["CHANGE_ID"] = "test"
    try:
        check("feature/test")
    except:
        assert False


# Generated at 2022-06-14 04:50:18.959225
# Unit test for function check
def test_check():
  assert check() == None

# Generated at 2022-06-14 04:50:51.253272
# Unit test for function semaphore
def test_semaphore():
    assert os.environ.get('BRANCH_NAME') is None
    assert os.environ.get('PULL_REQUEST_NUMBER') is None
    assert os.environ.get('SEMAPHORE_THREAD_RESULT') is None

    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = 'false'
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'failed'

    try:
        semaphore('master')
    except CiVerificationError:
        assert os.environ.get('BRANCH_NAME') is None
        assert os.environ.get('PULL_REQUEST_NUMBER') is None

# Generated at 2022-06-14 04:50:54.904522
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"

    assert semaphore()


# Unit tests for function travis

# Generated at 2022-06-14 04:51:04.313872
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    try:
        gitlab("master")
    except:
        assert True
    else:
        assert False

    os.environ["CI_COMMIT_REF_NAME"] = "testing"
    try:
        gitlab("master")
    except:
        assert False
    else:
        assert True

    del os.environ["CI_COMMIT_REF_NAME"]
    try:
        gitlab("master")
    except:
        assert False
    else:
        assert False


# Generated at 2022-06-14 04:51:15.043143
# Unit test for function travis
def test_travis():
    assert os.environ.get("TRAVIS_BRANCH") == "master"
    assert os.environ.get("TRAVIS_PULL_REQUEST") == "false"
    travis('master')
    os.environ["TRAVIS_BRANCH"] = 'test'
    try:
        travis('master')
    except CiVerificationError:
        os.environ["TRAVIS_BRANCH"] = 'master'
        assert os.environ.get("TRAVIS_BRANCH") == "master"
        os.environ["TRAVIS_PULL_REQUEST"] = 'true'
        try:
            travis('master')
        except CiVerificationError:
            os.environ["TRAVIS_PULL_REQUEST"] = 'false'
            assert os.environ

# Generated at 2022-06-14 04:51:18.709594
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    circle("master")

# Generated at 2022-06-14 04:51:25.199847
# Unit test for function travis
def test_travis():
    # No errors with expected env vars
    travis(branch="master")
    # Correct exception is raised with bad branch and is pull request
    try:
        travis(branch="dev")
    except CiVerificationError as e:
        assert True
    else:
        assert False

    try:
        travis(branch="master")
    except CiVerificationError as e:
        assert False
    else:
        assert True

# Generated at 2022-06-14 04:51:30.919309
# Unit test for function semaphore
def test_semaphore():
    def test(branch):
        os.environ['BRANCH_NAME'] = branch
        del os.environ['PULL_REQUEST_NUMBER']
        del os.environ['SEMAPHORE_THREAD_RESULT']
        semaphore(branch)
    yield test, 'master'
    yield test, 'dev'


# Generated at 2022-06-14 04:51:33.536403
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check("master")
    # assert False

# Generated at 2022-06-14 04:51:46.173085
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "some-branch"
    try:
        frigg("some-other-branch")
        assert False
    except CiVerificationError:
        pass
    try:
        os.environ["FRIGG_BUILD_BRANCH"] = "some-branch"
        os.environ["FRIGG_PULL_REQUEST"] = "1"
        frigg("some-branch")
        assert False
    except CiVerificationError:
        pass
    os.environ["FRIGG_BUILD_BRANCH"] = "some-branch"
    assert frigg("some-branch")
    del os.environ["FRIGG"]
    del os.en

# Generated at 2022-06-14 04:51:47.486921
# Unit test for function bitbucket
def test_bitbucket():
    bitbucket("master")

# Generated at 2022-06-14 04:52:34.208895
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_COMMIT_REF_SLUG"] = "master"
    check()

# Generated at 2022-06-14 04:52:37.064093
# Unit test for function checker
def test_checker():
    @checker
    def test_func():
        assert 0

    try:
        test_func()
    except CiVerificationError:
        pass
    else:
        assert False, "Should be a verification error"

# Generated at 2022-06-14 04:52:41.242214
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    travis('master')


# Generated at 2022-06-14 04:52:47.306511
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    circle("master")
    os.environ["CIRCLE_BRANCH"] = "develop"
    with raises(CiVerificationError):
        circle("master")
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "true"
    with raises(CiVerificationError):
        circle("master")


# Generated at 2022-06-14 04:52:50.988570
# Unit test for function gitlab
def test_gitlab():
    os.environ['CI_COMMIT_REF_NAME'] = '0.0.4'
    assert checker(gitlab)('0.0.4') is True


# Generated at 2022-06-14 04:52:54.654770
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://jenkins.com"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = "10"

    check()

# Generated at 2022-06-14 04:53:00.218826
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "5"
    try:
        assert bitbucket("master")
    except CiVerificationError:
        pass
    else:
        raise AssertionError("Should raise CiVerificationError")

# Generated at 2022-06-14 04:53:05.374285
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    circle(branch="master")
    del os.environ["CIRCLECI"]
    del os.environ["CIRCLE_BRANCH"]



# Generated at 2022-06-14 04:53:11.643555
# Unit test for function checker
def test_checker():
    """Unit tests for function checker()
    """
    # This function raises no exceptions
    @checker
    def func_no_exception():
        return None

    func_no_exception()

    # This function raises an AssertionError
    @checker
    def func_exception():
        assert False

    raised = False
    try:
        func_exception()
    except CiVerificationError:
        raised = True
    assert raised



# Generated at 2022-06-14 04:53:13.982907
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check()