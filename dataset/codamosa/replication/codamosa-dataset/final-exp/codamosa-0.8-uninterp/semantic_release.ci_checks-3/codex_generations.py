

# Generated at 2022-06-14 04:45:18.644811
# Unit test for function frigg
def test_frigg():
    print("test_frigg")
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = None
    check()
    del os.environ["FRIGG"]
    del os.environ["FRIGG_BUILD_BRANCH"]
    del os.environ["FRIGG_PULL_REQUEST"]
    try:
        frigg("master")
    except AssertionError as e:
        print(e)
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"]

# Generated at 2022-06-14 04:45:21.658565
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "no-pull-request"
    assert bitbucket("no-pull-request")

# Generated at 2022-06-14 04:45:33.175758
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master") is True

    os.environ["BRANCH_NAME"] = "develop"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master") is False

    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "123"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
   

# Generated at 2022-06-14 04:45:39.187635
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = "https://ci.frigg.io/rasmus/semantic-release/"
    os.environ['BRANCH_NAME'] = "master"
    os.environ['CHANGE_ID'] = "0"
    assert jenkins("master")


if __name__ == "__main__":
    check()

# Generated at 2022-06-14 04:45:44.991255
# Unit test for function checker
def test_checker():
    @checker
    def error_func():
        assert False

    try:
        error_func()
    except CiVerificationError:
        assert True
    except:
        assert False

    @checker
    def pass_func():
        assert True

    try:
        assert pass_func() == True
    except:
        assert False


# Generated at 2022-06-14 04:45:51.127582
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    try:
        gitlab("master")
    except CiVerificationError:
        raise Exception("Function gitlab failed.")
    os.environ["CI_COMMIT_REF_NAME"] = "develop"
    try:
        gitlab("master")
        raise Exception("Function gitlab failed.")
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:46:01.128488
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    assert os.environ.get('TRAVIS_BRANCH') == 'master'
    assert os.environ.get('TRAVIS_PULL_REQUEST') == 'false'
    travis()
    os.environ['TRAVIS_BRANCH'] = 'random'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    assert os.environ.get('TRAVIS_BRANCH') == 'random'
    assert os.environ.get('TRAVIS_PULL_REQUEST') == 'false'

# Generated at 2022-06-14 04:46:12.695900
# Unit test for function check
def test_check():
    branch = "master"

    # travis
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = branch
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check(branch)
    # semaphore
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = branch
    os.environ["PULL_REQUEST_NUMBER"] = "None"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    check(branch)
    # frigg
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = branch


# Generated at 2022-06-14 04:46:15.720314
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "branch"
    os.environ["BITBUCKET_PR_ID"] = "random"
    check()

# Generated at 2022-06-14 04:46:27.427251
# Unit test for function jenkins
def test_jenkins():
    with jenkins.__globals__["os"].environ(
            JENKINS_URL="http://localhost:8080/job/test_job/"):
        assert jenkins()

    with jenkins.__globals__["os"].environ(
            GIT_BRANCH="test_branch",
            JENKINS_URL="http://localhost:8080/job/test_job/",
            CHANGE_ID="mytestid"):
        assert jenkins()

    with jenkins.__globals__["os"].environ(
            BRANCH_NAME="test_branch",
            JENKINS_URL="http://localhost:8080/job/test_job/",
            CHANGE_ID="mytestid"):
        assert jenkins()

   

# Generated at 2022-06-14 04:46:42.730619
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "1234"
    try:
        bitbucket("master")
        raise AssertionError("Should have failed.")
    except CiVerificationError:
        pass
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("master")


# Generated at 2022-06-14 04:46:48.079846
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master")

# Generated at 2022-06-14 04:46:48.670703
# Unit test for function check
def test_check():
    assert check() is None

# Generated at 2022-06-14 04:46:52.301466
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    try:
        travis("master")
    except CiVerificationError as e:
        assert "environment did not pass" in str(e)



# Generated at 2022-06-14 04:47:02.656914
# Unit test for function jenkins
def test_jenkins():
    # Test fails
    test_os_environ = {"JENKINS_URL": "test", "BRANCH_NAME": "test", "GIT_BRANCH": "test", "CHANGE_ID": "test"}
    check = jenkins(test_os_environ)
    assert check == False # it should be false because BRANCH_NAME is not master

    # Test is True
    test_os_environ = {"JENKINS_URL": "test", "BRANCH_NAME": "master", "GIT_BRANCH": "test", "CHANGE_ID": None}
    check = jenkins(test_os_environ)
    assert check == True

# Generated at 2022-06-14 04:47:06.601082
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "test"
    os.environ["BITBUCKET_PR_ID"] = "test"
    try:
        bitbucket()
    except CiVerificationError as err:
        assert str(err) == "The verification check for the environment did not pass."

# Generated at 2022-06-14 04:47:16.108099
# Unit test for function jenkins
def test_jenkins():
    """
    Unit test for function jenkins. Asserts that the function raises a
    CiVerificationError when the JENKINS_URL is not set, the BRANCH_NAME
    is not equal to 'master', and the CHANGE_ID is set.
    """
    os.environ.pop("JENKINS_URL")
    os.environ.pop("BRANCH_NAME")
    os.environ.pop("GIT_BRANCH")
    os.environ.pop("CHANGE_ID")
    try:
        jenkins('master')
        assert False
    except CiVerificationError:
        assert True
    os.environ["JENKINS_URL"] = "url"

# Generated at 2022-06-14 04:47:21.832820
# Unit test for function gitlab
def test_gitlab():
    """
    Unit test for function gitlab
    """
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_IID"] = ""

    expected = check("master")
    assert expected

    os.environ["CI_MERGE_REQUEST_IID"] = "1"

    with pytest.raises(CiVerificationError):
        check("master")

    del os.environ["CI_MERGE_REQUEST_IID"]
    del os.environ["GITLAB_CI"]



# Generated at 2022-06-14 04:47:22.374416
# Unit test for function circle
def test_circle():
    assert circle("master") == True


# Generated at 2022-06-14 04:47:24.271315
# Unit test for function gitlab
def test_gitlab():
    # Check function with right inputs
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    gitlab("master")



# Generated at 2022-06-14 04:47:31.573440
# Unit test for function circle
def test_circle():
    circle("master")
    pass

# Generated at 2022-06-14 04:47:40.661374
# Unit test for function jenkins
def test_jenkins():
    """
    Test for function jenkins
    """
    assert os.environ.get("JENKINS_URL") is None
    assert os.environ.get("GIT_BRANCH") == "master"
    assert not os.environ.get("CHANGE_ID")

    os.environ["JENKINS_URL"] = "http:localhost:8080"
    os.environ["GIT_BRANCH"] = "master"
    assert jenkins("master")

    os.environ["GIT_BRANCH"] = "development"
    assert not jenkins("master")

# Generated at 2022-06-14 04:47:49.316206
# Unit test for function travis
def test_travis():
    """
    Unit test for the travis CI
    """
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"

    travis("master")

    os.environ["TRAVIS_BRANCH"] = "other"

    try:
        travis("master")
        assert False, "Exception not raised"
    except CiVerificationError:
        assert True



# Generated at 2022-06-14 04:47:57.106634
# Unit test for function bitbucket
def test_bitbucket():
    """
    Testing Bitbucket CI Running.
    """
    from unittest import mock

    # Mock bitbucket environment
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    # Run the function
    check("master")
    # Clear the mocked environment
    os.environ.pop("BITBUCKET_BRANCH")
    os.environ.pop("BITBUCKET_PR_ID")



# Generated at 2022-06-14 04:48:01.349379
# Unit test for function circle
def test_circle():
    with pytest.raises(CiVerificationError):
        check(branch='master')
        check(branch='develop')
        circle(branch='master')
        circle(branch='develop')

test_circle()

# Generated at 2022-06-14 04:48:08.472285
# Unit test for function gitlab
def test_gitlab():
    import os
    branch = "master"
    os.environ["CI_COMMIT_REF_NAME"] = branch
    os.environ["CI_MERGE_REQUEST_IID"] = ""
    check(branch)
    os.environ["CI_MERGE_REQUEST_IID"] = "A"
    os.environ["CI_COMMIT_REF_NAME"] = branch
    check(branch)
    os.environ["CI_MERGE_REQUEST_IID"] = ""
    os.environ["CI_COMMIT_REF_NAME"] = branch + "1"
    check(branch)
    del os.environ["CI_MERGE_REQUEST_IID"]
    os.environ["CI_COMMIT_REF_NAME"] = branch
    check(branch)
    del os

# Generated at 2022-06-14 04:48:13.993148
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "https://github.com/org/repo/pulls/123"
    os.environ["CIRCLE_BRANCH"] = "feature"
    assert check() == 1
    os.environ["CIRCLE_BRANCH"] = "master"
    assert check() == 0



# Generated at 2022-06-14 04:48:20.206632
# Unit test for function circle
def test_circle():
    """
    Test that the check function sets environment variables correctly
    """
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "develop"
    os.environ["CI_PULL_REQUESTS"] = "1234"
    circle("develop")



# Generated at 2022-06-14 04:48:24.634909
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master") == True
    del os.environ["TRAVIS_BRANCH"]
    del os.environ["TRAVIS_PULL_REQUEST"]
    assert travis("master") == False



# Generated at 2022-06-14 04:48:35.101571
# Unit test for function check
def test_check():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    os.environ['TRAVIS'] = 'true'
    assert check() == True

    os.environ['TRAVIS_BRANCH'] = 'not-master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    os.environ['TRAVIS'] = 'true'
    try:
        check()
    except CiVerificationError:
        assert True

    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'true'
    os.environ['TRAVIS'] = 'true'

# Generated at 2022-06-14 04:48:46.557797
# Unit test for function checker
def test_checker():
    @checker
    def shoud_raise_on_assertion_error():
        assert 2 + 2 == 5

    try:
        shoud_raise_on_assertion_error()
    except AssertionError:
        assert False, "Function checker should have raised a CiVerificationError"
    except CiVerificationError:
        assert True, "Function checker should have raised a CiVerificationError"
    else:
        assert False, "Function checker should have raised a CiVerificationError"


# Generated at 2022-06-14 04:48:55.540745
# Unit test for function frigg
def test_frigg():
    """
    Unit test for function frigg
    """
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg("master")
    assert os.environ["FRIGG_BUILD_BRANCH"] == "master"

    with pytest.raises(CiVerificationError):
        frigg("test")

    os.environ["FRIGG_PULL_REQUEST"] = "true"
    with pytest.raises(CiVerificationError):
        frigg("master")


# Generated at 2022-06-14 04:49:00.367927
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    frigg("master")
    del os.environ["FRIGG"]
    del os.environ["FRIGG_BUILD_BRANCH"]
    del os.environ["FRIGG_PULL_REQUEST"]


# Generated at 2022-06-14 04:49:07.943038
# Unit test for function checker
def test_checker():
    def raise_assertion_error():
        raise AssertionError
    def return_true():
        return True

    # Test that the wrapped function returns True
    # and no exception was raised
    assert checker(return_true)()

    # Test that the wrapped function raises
    # CiVerificationError
    try:
        checker(raise_assertion_error)()
    except CiVerificationError:
        pass
    else:
        raise RuntimeError("CiVerificationError not raised.")

# Generated at 2022-06-14 04:49:11.647477
# Unit test for function jenkins
def test_jenkins():
    assert jenkins('master')
    os.environ['BRANCH_NAME'] = 'master'
    assert jenkins('master')
    os.environ['GIT_BRANCH'] = 'master'
    assert jenkins('master')

# Generated at 2022-06-14 04:49:15.307622
# Unit test for function checker

# Generated at 2022-06-14 04:49:21.710592
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = "true"
    os.environ['FRIGG_BUILD_BRANCH'] = "master"
    os.environ['FRIGG_PULL_REQUEST'] = "false"
    assert frigg(branch="master") == True
    os.environ['FRIGG'] = "true"
    os.environ['FRIGG_BUILD_BRANCH'] = "develop"
    os.environ['FRIGG_PULL_REQUEST'] = "false"
    try:
        frigg(branch="master")
    except AssertionError:
        assert True
    except Exception:
        assert False
    os.environ['FRIGG'] = ""
    os.environ['FRIGG_BUILD_BRANCH'] = ""
    os

# Generated at 2022-06-14 04:49:24.929861
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = "123"
    check()
    os.environ["CI_MERGE_REQUEST_ID"] = "false"
    check()
    del os.environ["CI_MERGE_REQUEST_ID"]
    check()
    del os.environ["CI_COMMIT_REF_NAME"]
    os.environ["CI_MERGE_REQUEST_ID"] = "123"
    check()


# Generated at 2022-06-14 04:49:25.621852
# Unit test for function check
def test_check():
    pass

# Generated at 2022-06-14 04:49:33.375127
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_COMMIT_REF_NAME"] = "false"
    gitlab(branch="master")
    # reset os.environ
    os.environ.pop("CI_COMMIT_REF_NAME")
    os.environ.pop("CI_COMMIT_REF_NAME")
    del os.environ["CI_COMMIT_REF_NAME"]
    del os.environ["CI_COMMIT_REF_NAME"]



# Generated at 2022-06-14 04:49:45.815056
# Unit test for function semaphore
def test_semaphore():
    assert semaphore(branch="master")
    assert semaphore(branch="semanticrelease")
    assert semaphore(branch="1.3")
    assert semaphore(branch="1.3.0")
    assert semaphore(branch="1.3.0-beta")
    assert semaphore(branch="1.3.0-beta.1")
    assert semaphore(branch="1.3.0-beta.1.1")



# Generated at 2022-06-14 04:49:47.230274
# Unit test for function gitlab
def test_gitlab():
    assert gitlab("master") == True

# Generated at 2022-06-14 04:49:56.876415
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_PROJECT_ID"] = "1234567"
    os.environ["CI_PIPELINE_ID"] = "1234567"
    try:
        gitlab("master")
    except CiVerificationError:
        raise AssertionError("gitlab should have passed")
    os.environ["CI_COMMIT_REF_NAME"] = "notmaster"
    try:
        gitlab("master")
        raise AssertionError("gitlab should have failed")
    except CiVerificationError:
        assert True



# Generated at 2022-06-14 04:49:59.149754
# Unit test for function bitbucket
def test_bitbucket():
    try:
        bitbucket('master')
    except CiVerificationError:
        return
    raise AssertionError('Should raise exception')

# Generated at 2022-06-14 04:50:03.742065
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "123"
    try:
        bitbucket("master")
    except CiVerificationError:
        pass
    else:
        assert False, "Should raise error"

# Generated at 2022-06-14 04:50:13.933309
# Unit test for function gitlab
def test_gitlab():
    def mocked_os_environ(dict_):
        """
        Create a temporary environment variable using dict_
        :param dict_: A dictionary containing variables to be set
        :return: Environment variable, dict_
        """
        original = dict(os.environ)
        os.environ.update(dict_)
        yield os.environ
        os.environ.clear()
        os.environ.update(original)


    # We must cover all "if" conditions in the function
    # Assume branch name is "master"
    branch = "master"

    # Case 1:
    # Failed because environment variable CI_COMMIT_REF_NAME does not match branch
    os_environ_dict = {"CI_COMMIT_REF_NAME": "feature/new-feature", "CI_BUILD_REF_NAME": "none"}

# Generated at 2022-06-14 04:50:17.246780
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master") == True



# Generated at 2022-06-14 04:50:26.019627
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "1234"
    try:
        semaphore("develop")
        assert False, "semaphore check should fail"
    except CiVerificationError:
        pass

    del os.environ["PULL_REQUEST_NUMBER"]
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    try:
        semaphore("master")
        assert False, "semaphore check should fail"
    except CiVerificationError:
        pass
    del os.environ["SEMAPHORE_THREAD_RESULT"]

    del os.environ["BRANCH_NAME"]

# Generated at 2022-06-14 04:50:26.953081
# Unit test for function travis
def test_travis():
    assert travis("master") == True
    

# Generated at 2022-06-14 04:50:33.741428
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "origin/master"
    os.environ["JENKINS_URL"] = "https://jenkins.local"
    os.environ["CHANGE_ID"] = "None"

    assert jenkins("master")

# Generated at 2022-06-14 04:50:54.796070
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = "true"
    os.environ['FRIGG_BUILDS'] = "[{'branch': 'master'}]"
    os.environ['FRIGG_BUILD_BRANCH'] = "master"

    assert frigg("master") == True

    os.environ['FRIGG_PULL_REQUEST'] = "true"
    assert frigg("master") == False

    os.environ['FRIGG_BUILD_BRANCH'] = "not_master"
    assert frigg("master") == False

# Generated at 2022-06-14 04:50:58.831341
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = "0"
    check()
    assert "gitlab" == "gitlab"

# Generated at 2022-06-14 04:51:00.699844
# Unit test for function semaphore
def test_semaphore():
    assert semaphore(branch = os.environ.get("BRANCH_NAME"))


# Generated at 2022-06-14 04:51:05.990156
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    frigg("master")



# Generated at 2022-06-14 04:51:12.397191
# Unit test for function circle
def test_circle():
    os.environ["CIRCLE_BRANCH"] = "master"
    del os.environ["CI_PULL_REQUEST"]
    assert circle("master") is True

    os.environ["CIRCLE_BRANCH"] = "feature"
    os.environ["CI_PULL_REQUEST"] = "1"
    with pytest.raises(CiVerificationError):
        circle("master")



# Generated at 2022-06-14 04:51:17.380382
# Unit test for function jenkins
def test_jenkins():
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = ""
    os.environ["JENKINS_URL"] = "http://127.0.0.1:8080"
    assert check() == True
    #os.environ["CHANGE_ID"] = "test"
    #assert check() == False

# Generated at 2022-06-14 04:51:20.476426
# Unit test for function circle
def test_circle():
    os.environ['CIRCLE_BRANCH'] = 'master'
    os.environ['CI_PULL_REQUEST'] = 'test'
    circle('master')

if __name__ == '__main__':
    test_circle()

# Generated at 2022-06-14 04:51:24.501265
# Unit test for function gitlab
def test_gitlab():
    from unittest.mock import patch
    with patch.dict('os.environ', {'CI_COMMIT_REF_NAME': 'master'}):
        check()


# Generated at 2022-06-14 04:51:31.698342
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://jenkins.com"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = "1"

    try:
        check()
        assert False
    except CiVerificationError:
        assert True
    del os.environ["JENKINS_URL"]
    del os.environ["BRANCH_NAME"]
    del os.environ["CHANGE_ID"]

# Generated at 2022-06-14 04:51:32.607512
# Unit test for function circle
def test_circle():
    assert checker(circle)() is True

# Generated at 2022-06-14 04:52:09.132837
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "42"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "1234"
    os.environ["BITBUCKET_PR_REPOSITORY_FULL_NAME"] = "foo/bar"
    os.environ["BITBUCKET_PR_SOURCE_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_TARGET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_TITLE"] = "A title"
    os.environ["BITBUCKET_REPO_SLUG"] = "foo/bar"

# Generated at 2022-06-14 04:52:19.930519
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "http://localhost"
    os.environ["BRANCH_NAME"] = "branch"

    try:
        jenkins(branch="branch")
        raise RuntimeError("jenkins() did not raise expected exception")
    except CiVerificationError:
        pass

    os.environ["BRANCH_NAME"] = "master"
    jenkins(branch="master")
    del os.environ["BRANCH_NAME"]

    os.environ["GIT_BRANCH"] = "branch"
    try:
        jenkins(branch="branch")
        raise RuntimeError("jenkins() did not raise expected exception")
    except CiVerificationError:
        pass


# Generated at 2022-06-14 04:52:21.909288
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = ""
    check()

# Generated at 2022-06-14 04:52:32.399454
# Unit test for function bitbucket
def test_bitbucket():
    os.environ.setdefault("BITBUCKET_BUILD_NUMBER", "1")
    os.environ.setdefault("BITBUCKET_BRANCH", "master")
    os.environ.setdefault("BITBUCKET_PR_ID", "")

    # Test for success
    assert bitbucket("master")

    # Test for failure - on pull request
    os.environ["BITBUCKET_PR_ID"] = "1"
    assert not bitbucket("master")

    # Test for failure - on wrong branch
    os.environ["BITBUCKET_PR_ID"] = ""
    assert not bitbucket("not-master")



# Generated at 2022-06-14 04:52:35.754158
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")


# Generated at 2022-06-14 04:52:42.898361
# Unit test for function semaphore
def test_semaphore():
    os.environ['SEMAPHORE'] = "true"
    os.environ['BRANCH_NAME'] = "master"
    os.environ['SEMAPHORE_THREAD_RESULT'] = "succeeded"
    semaphore('master')
    del os.environ['SEMAPHORE']
    del os.environ['BRANCH_NAME']
    del os.environ['SEMAPHORE_THREAD_RESULT']



# Generated at 2022-06-14 04:52:47.519794
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    check()

# Generated at 2022-06-14 04:52:53.443251
# Unit test for function circle
def test_circle():
    os.environ['CIRCLE_BRANCH']='master'
    os.environ['CI_PULL_REQUEST']=''
    assert circle('master')
    del os.environ['CI_PULL_REQUEST']
    assert circle('master')
    del os.environ['CIRCLE_BRANCH']
    

# Generated at 2022-06-14 04:52:54.852410
# Unit test for function frigg
def test_frigg():
    assert frigg(branch="master")



# Generated at 2022-06-14 04:53:06.552559
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = "JenkinsURL"
    os.environ['BRANCH_NAME'] = "my_branch"
    os.environ['CHANGE_ID'] = None
    assert jenkins("my_branch") == True
    os.environ['CHANGE_ID'] = "12345"
    assert jenkins("my_branch") == False
    os.environ['BRANCH_NAME'] = "other"
    assert jenkins("other") == True
    os.environ['GIT_BRANCH'] = "my_branch"
    os.environ['BRANCH_NAME'] = None
    assert jenkins("my_branch") == True

# Generated at 2022-06-14 04:54:05.645447
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    assert check() == None
    os.environ['FRIGG_PULL_REQUEST'] = 'true'
    try:
        check()
    except CiVerificationError as e:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:54:12.103183
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    del os.environ["TRAVIS"]
    del os.environ["TRAVIS_BRANCH"]
    del os.environ["TRAVIS_PULL_REQUEST"]
    
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "None"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    check()
    del os.environ["SEMAPHORE"]

# Generated at 2022-06-14 04:54:14.816685
# Unit test for function bitbucket
def test_bitbucket():
    """
    Test the bitbucket function.
    :return:
    """
    branch = "test"
    assert bitbucket(branch)

# Generated at 2022-06-14 04:54:17.086332
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check(branch="master")

# Generated at 2022-06-14 04:54:18.396371
# Unit test for function bitbucket
def test_bitbucket():
    result = bitbucket("master")
    assert result == True


# Generated at 2022-06-14 04:54:20.167524
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()



# Generated at 2022-06-14 04:54:24.904213
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'localhost:8080'
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['GIT_BRANCH'] = 'master'
    jenkins('master')


# Generated at 2022-06-14 04:54:36.706340
# Unit test for function semaphore
def test_semaphore():
    """
    Test the semaphore function by
    setting relationship variables from the CI environment
    and checking the semaphore function
    """
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master")
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert not semaphore("master")
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"]

# Generated at 2022-06-14 04:54:44.830811
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "my-branch"
    os.environ["JENKINS_URL"] = "https://jenkins.my-domain.com"
    os.environ["CHANGE_ID"] = "123"
    try:
        jenkins(os.environ["BRANCH_NAME"])
    except CiVerificationError as e:
        assert "The verification check for the environment did not pass." == str(e)
    else:
        raise AssertionError("CiVerificationError not raised.")
    finally:
        del os.environ["BRANCH_NAME"]
        del os.environ["JENKINS_URL"]
        del os.environ["CHANGE_ID"]

# Generated at 2022-06-14 04:54:55.417745
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "123"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert semaphore(None) == False
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "123"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore(None) == False
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
   