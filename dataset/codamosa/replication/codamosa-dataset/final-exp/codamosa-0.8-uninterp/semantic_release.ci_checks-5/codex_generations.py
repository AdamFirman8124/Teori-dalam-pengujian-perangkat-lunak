

# Generated at 2022-06-14 04:45:18.395465
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    try:
        semaphore("master")
    except CiVerificationError as e:
        assert False

    # WHEN: No SEMAPHORE env
    os.environ.pop("SEMAPHORE", 0)
    try:
        semaphore("master")
    except CiVerificationError as e:
        assert False

    # WHEN: No BRANCH_NAME env
    os.environ["SEMAPHORE"] = "true"
    os.environ.pop("BRANCH_NAME", 0)

# Generated at 2022-06-14 04:45:25.692912
# Unit test for function jenkins
def test_jenkins():
    # os.environ["BRANCH_NAME"] = "develop"
    # assert jenkins("develop") is None

    os.environ["BRANCH_NAME"] = "master"
    assert jenkins("master") is None

    os.environ["BRANCH_NAME"] = "develop"
    os.environ["CHANGE_ID"] = "9"
    assert jenkins("master") is None

# Generated at 2022-06-14 04:45:29.222101
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "false"
    os.environ["CIRCLE_BRANCH"] = "master"
    check()

# Generated at 2022-06-14 04:45:38.499166
# Unit test for function travis
def test_travis():
    # If TRAVIS is set to true, the function will fail
    if os.environ.get("TRAVIS") == "true":
        assert os.environ.get("TRAVIS_BRANCH") == "master"
        assert os.environ.get("TRAVIS_PULL_REQUEST") == "false"
    else:
        assert True



# Generated at 2022-06-14 04:45:50.138800
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    check()
    assert os.environ["TRAVIS_BRANCH"] == "master"
    assert os.environ["TRAVIS_PULL_REQUEST"] == "false"

    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_PULL_REQUEST"] = "18"
    try:
        check()
        raise AssertionError
    except CiVerificationError:
        pass

    os.environ["SEMAPHORE"] = "true"
    os.environ.pop("PULL_REQUEST_NUMBER", None)
    check()
    assert os.environ["BRANCH_NAME"] == "master"
    assert os.environ["SEMAPHORE_THREAD_RESULT"]

# Generated at 2022-06-14 04:46:00.301038
# Unit test for function bitbucket
def test_bitbucket():
    for k in os.environ:
        if "BITBUCKET" in k:
            os.environ[k] = ""
    os.environ["BITBUCKET_BUILD_NUMBER"] = "12"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    check()

    for k in os.environ:
        if "BITBUCKET" in k:
            os.environ[k] = ""
    os.environ["BITBUCKET_BUILD_NUMBER"] = "12"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "12"

# Generated at 2022-06-14 04:46:05.399718
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://jenkins"
    os.environ["BRANCH_NAME"] = "master"
    jenkins("develop")

    os.environ["BRANCH_NAME"] = "develop"
    jenkins("develop")

    del os.environ["BRANCH_NAME"]

    os.environ["GIT_BRANCH"] = "master"
    jenkins("develop")

    os.environ["GIT_BRANCH"] = "develop"
    jenkins("develop")

# Generated at 2022-06-14 04:46:10.730198
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"

    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg("master")

    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    frigg("develop")

    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "true"
    try:
        frigg("develop")
        raise Exception()
    except:
        pass



# Generated at 2022-06-14 04:46:16.536042
# Unit test for function jenkins
def test_jenkins():
    """
    Should return true if the jenkins environment variable is true and the correct
    variables are set.

    :returns: `True` if successful.
    """
    os.environ["JENKINS_URL"] = "True"
    os.environ["GIT_BRANCH"] = "master"
    return check(branch="master")



# Generated at 2022-06-14 04:46:28.224167
# Unit test for function checker
def test_checker():
    """
    A decorator that will convert AssertionErrors into
    CiVerificationError.
    """

    from semantic_release.errors import CiVerificationError

    def test_func():
        """
        A function that will raise AssertionError
        """
        raise AssertionError("")

    def test_wrapper():
        """
        A function that will raise a CiVerificationError on AssertionError
        """
        try:
            test_func()
            return True
        except AssertionError:
            raise CiVerificationError(
                "The verification check for the environment did not pass."
            )

    def test_func_wrapper():
        """
        A function that will raise a CiVerificationError on AssertionError
        """

# Generated at 2022-06-14 04:46:43.074996
# Unit test for function travis
def test_travis():
    # test_travis_without_assertion
    assert os.environ.get("TRAVIS_BRANCH") != 'master'
    assert os.environ.get("TRAVIS_PULL_REQUEST") != 'false'
    try:
        travis('master')
    except CiVerificationError:
        pass
    assert os.environ.get("TRAVIS_BRANCH") == 'master'
    assert os.environ.get("TRAVIS_PULL_REQUEST") == 'false'


# Generated at 2022-06-14 04:46:46.650986
# Unit test for function jenkins
def test_jenkins():
    os.environ['BRANCH_NAME'] = 'master'
    jenkins(branch='master')
    assert True

# Generated at 2022-06-14 04:46:50.656420
# Unit test for function semaphore
def test_semaphore():
    """
    Testing the semaphore CI
    """
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    check()


# Generated at 2022-06-14 04:46:56.254136
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = "true"
    os.environ['CIRCLE_BRANCH'] = "master"
    os.environ['CI_PULL_REQUEST'] = "false"
    check('master')


# Generated at 2022-06-14 04:47:06.562881
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BUILD_NUMBER'] = "BITBUCKET_BUILD_NUMBER"
    os.environ['BITBUCKET_BRANCH'] = "master"
    os.environ['BITBUCKET_PR_ID'] = "BITBUCKET_PR_ID"
    os.environ['BITBUCKET_REPO_OWNER'] = "BITBUCKET_REPO_OWNER"
    
    try:
        bitbucket("master")
    except CiVerificationError:
        pass
    else:
        raise RuntimeError("Expected error")
    
    os.environ['BITBUCKET_PR_ID'] = None
    
    bitbucket("master")
    
    del os.environ['BITBUCKET_BUILD_NUMBER']


# Generated at 2022-06-14 04:47:16.108758
# Unit test for function checker
def test_checker():
    def checker_func(branch: str):
        assert os.environ.get("TRAVIS") == "true"
        assert os.environ.get("TRAVIS_BRANCH") == branch
        assert os.environ.get("TRAVIS_PULL_REQUEST") == "false"

    checker_func = checker(checker_func)

    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    checker_func("master")

    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        checker_func("master")
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:47:18.259364
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "true"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = "false"
    jenkins("master")

# Generated at 2022-06-14 04:47:19.499533
# Unit test for function semaphore
def test_semaphore():
    assert semaphore(branch="master") == True
    assert semaphore(branch="test") == False

# Generated at 2022-06-14 04:47:23.053900
# Unit test for function travis
def test_travis():
    assert os.environ.get("TRAVIS") == "true"



# Generated at 2022-06-14 04:47:30.628202
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "true"
    os.environ["BITBUCKET_BRANCH"] = "feature/test"

    with pytest.raises(CiVerificationError):
        bitbucket("master")
    os.environ["BITBUCKET_BRANCH"] = "master"
    assert bitbucket("master")

    os.environ["BITBUCKET_PR_ID"] = "test"
    os.environ["BITBUCKET_BRANCH"] = "master"
    with pytest.raises(CiVerificationError):
        bitbucket("master")
    del os.environ["BITBUCKET_PR_ID"]

    del os.environ["BITBUCKET_BUILD_NUMBER"]


# Unit test

# Generated at 2022-06-14 04:47:39.904152
# Unit test for function travis
def test_travis():
    """
    Test a travis build with branch set.
    """
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"

    check(branch="master")



# Generated at 2022-06-14 04:47:41.317951
# Unit test for function semaphore
def test_semaphore():
    assert semaphore("master")
    assert not semaphore("develop")

# Generated at 2022-06-14 04:47:43.674882
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ["PULL_REQUEST_NUMBER"] = None
    semaphore("master")



# Generated at 2022-06-14 04:47:45.973190
# Unit test for function travis
def test_travis():
    assert checker(travis)("master") is None


# Generated at 2022-06-14 04:47:47.090895
# Unit test for function circle
def test_circle():
    assert circle() is True


# Generated at 2022-06-14 04:47:57.845477
# Unit test for function check
def test_check():
    """Test to ensure that check correctly identifies the CI that is used
    """
    # Travis CI
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    os.environ['TRAVIS'] = 'true'
    assert check()

    # Semaphore CI
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    os.environ['SEMAPHORE'] = 'true'
    assert check()

    # Frigg CI
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os

# Generated at 2022-06-14 04:48:01.296499
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://url"
    os.environ["BRANCH_NAME"] = "test-branch"

    jenkins("test-branch")

# Generated at 2022-06-14 04:48:13.623340
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")
    # wrong branch
    try:
        travis("develop")
    except CiVerificationError as e:
        assert "CI_BRANCH" in str(e)
    else:
        raise AssertionError
    # wrong pull request
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        travis("master")
    except CiVerificationError as e:
        assert "CI_PULL_REQUEST" in str(e)
    else:
        raise AssertionError
    # clean
    del os.environ["TRAVIS_BRANCH"]

# Generated at 2022-06-14 04:48:22.548730
# Unit test for function frigg
def test_frigg():
    map_env = {
        "TRAVIS": None, "SEMAPHORE": None, "FRIGG": "true", "CIRCLECI": None,
        "GITLAB_CI": None, "JENKINS_URL": None
    }
    os.environ.clear()
    os.environ.update(map_env)
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    check()

# Generated at 2022-06-14 04:48:29.323023
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG_BUILD_BRANCH'] = 'frigg'
    frigg('frigg')
    os.environ['FRIGG_PULL_REQUEST'] = 'True'
    try:
        frigg('frigg')
    except AssertionError:
        pass


# Generated at 2022-06-14 04:48:41.025322
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'jenkins_url'
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['GIT_BRANCH'] = 'master'
    print(os.environ.get("BRANCH_NAME"))
    print(os.environ.get("GIT_BRANCH"))
    jenkins(branch='master')

# Generated at 2022-06-14 04:48:45.851937
# Unit test for function travis
def test_travis():
    # Environment variable TRAVIS is set
    os.environ['TRAVIS'] = 'true'
    # Environment variable TRAVIS_BRANCH is set
    os.environ['TRAVIS_BRANCH'] = 'master'
    # Environment variable TRAVIS_PULL_REQUEST is not set
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    assert check()



# Generated at 2022-06-14 04:48:57.469858
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'https://example.com'
    os.environ['BRANCH_NAME'] = 'BRANCH_NAME'
    os.environ['GIT_BRANCH'] = 'GIT_BRANCH'
    os.environ['CHANGE_ID'] = 'CHANGE_ID'
    check()
    os.environ['BRANCH_NAME'] = ''
    check()
    os.environ['BRANCH_NAME'] = 'GIT_BRANCH'
    del (os.environ['CHANGE_ID'])
    jenkins('GIT_BRANCH')
    os.environ['CHANGE_ID'] = 'CHANGE_ID'
    os.environ['JENKINS_URL'] = ''
    check()

# Generated at 2022-06-14 04:49:02.818405
# Unit test for function frigg
def test_frigg():
    assert os.environ.get("FRIGG") == "true"
    assert os.environ.get("FRIGG_BUILD_BRANCH") == "master"
    assert not os.environ.get("FRIGG_PULL_REQUEST")

    frigg("master")

# Generated at 2022-06-14 04:49:10.434137
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'true'
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['GIT_BRANCH'] = 'master'
    os.environ['CHANGE_ID'] = 'x'
    assert check()
    os.environ.pop('JENKINS_URL')
    os.environ.pop('BRANCH_NAME')
    os.environ.pop('GIT_BRANCH')
    os.environ.pop('CHANGE_ID')

# Generated at 2022-06-14 04:49:19.507417
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ['FRIGG_PULL_REQUEST'] = '12'
    try:
        frigg('master')
    except Exception as e:
        assert isinstance(e, CiVerificationError)
        assert e.args[0] == 'The verification check for the environment did not pass.'
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ['FRIGG_PULL_REQUEST'] = 'False'
    try:
        frigg('master')
    except Exception as e:
        assert not isinstance(e, CiVerificationError)
        assert e.args[0] != 'The verification check for the environment did not pass.'

# Generated at 2022-06-14 04:49:30.449007
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master") is True
    del os.environ["BRANCH_NAME"]
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["SEMAPHORE_THREAD_RESULT"]
    assert semaphore("master") is False
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "123"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"

# Generated at 2022-06-14 04:49:35.313254
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    try:
        circle("master")
    except:
        raise RuntimeError("test_circle failed")



# Generated at 2022-06-14 04:49:36.480027
# Unit test for function travis
def test_travis():
    try:
        travis("test")
    except:
        pass


# Generated at 2022-06-14 04:49:46.659834
# Unit test for function semaphore
def test_semaphore():
    """Unit test for function semaphore"""
    os.environ['SEMAPHORE'] = 'true'
    os.environ['BRANCH_NAME'] = 'test'
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'test'
    os.environ['PULL_REQUEST_NUMBER'] = 'test'
    try:
        semaphore('test')
        assert False
    except CiVerificationError:
        assert True
    os.environ['PULL_REQUEST_NUMBER'] = 'test'
    try:
        semaphore('test')
        assert False
    except CiVerificationError:
        assert True
    os.environ['BRANCH_NAME'] = 'test'
    os.environ['PULL_REQUEST_NUMBER'] = 'test'


# Generated at 2022-06-14 04:49:54.722947
# Unit test for function checker
def test_checker():
    """Unit test for function checker"""
    def test_func():
        """Test function"""
        assert False

    with pytest.raises(CiVerificationError):
        checker(test_func)()

# Generated at 2022-06-14 04:49:55.856867
# Unit test for function gitlab
def test_gitlab():
    assert 1

# Generated at 2022-06-14 04:50:00.609001
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = 'master'
    bitbucket(branch="master")
    os.environ['BITBUCKET_PR_ID'] = '123'
    try:
        bitbucket(branch="master")
        assert False
    except CiVerificationError:
        assert True

# Generated at 2022-06-14 04:50:05.142395
# Unit test for function travis
def test_travis():
    assert travis("master") == True
    try:
        travis("develop")
    except CiVerificationError:
        print("travis is throwing CiVerificationError, that's a good thing")
    else:
        assert False


# Generated at 2022-06-14 04:50:14.912669
# Unit test for function semaphore
def test_semaphore():
    """
    Test the semaphore function

    :return:
    """
    # Set environ vars required by travis
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'not failed'
    # Test that nothing raises an exception
    semaphore('master')
    # Test that an error is raised
    os.environ['BRANCH_NAME'] = 'other'
    os.environ['PULL_REQUEST_NUMBER'] = '1234'
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'failed'
    try:
        semaphore('master')
    except CiVerificationError:
        return
   

# Generated at 2022-06-14 04:50:20.458875
# Unit test for function gitlab
def test_gitlab():
    assert os.environ.get("CI_COMMIT_REF_NAME") == "master"
    assert not os.environ.get("CI_MERGE_REQUEST_ID")
    assert not os.environ.get("CI_MERGE_REQUEST_SOURCE_BRANCH_NAME")
    assert not os.environ.get("CI_MERGE_REQUEST_TARGET_BRANCH_NAME")

# Generated at 2022-06-14 04:50:24.588024
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://ci.frigg.io/frigg/clippy/"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = "123"
    jenkins("master")

# Generated at 2022-06-14 04:50:29.159815
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check()
    os.environ["CI_COMMIT_REF_NAME"] = "wrong"
    try:
        check()
        raise Exception("Should have raised exception")
    except CiVerificationError as e:
        assert "The verification check for the environment did not pass." in str(e)
    del os.environ["GITLAB_CI"]
    del os.environ["CI_COMMIT_REF_NAME"]



# Generated at 2022-06-14 04:50:32.531786
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = 'true'
    os.environ["BRANCH_NAME"] = 'master'
    os.environ["SEMAPHORE_THREAD_RESULT"] = 'success'
    try:
        check()
    except CiVerificationError:
        assert  False
    assert True


# Generated at 2022-06-14 04:50:36.024028
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    checker(travis)(branch = "master")


# Generated at 2022-06-14 04:50:45.986978
# Unit test for function semaphore
def test_semaphore():
    """Ensure semaphore checker works"""
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = ""
    semaphore("master")



# Generated at 2022-06-14 04:50:51.306857
# Unit test for function semaphore
def test_semaphore():
    """
    This function is used to test `semaphore` function. It does so
    by populating os.environ with the necessary environment variables
    for semaphore, and then it calls the `semaphore` function to tests
    if it passes or fails.

    :return: Returns a `CiVerificationError` on failure.
    """
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "1234"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    semaphore("master")

# Generated at 2022-06-14 04:50:52.235378
# Unit test for function semaphore
def test_semaphore():
    semaphore("master")

# Generated at 2022-06-14 04:50:58.941596
# Unit test for function semaphore
def test_semaphore():
    """
    Verifies that the semaphore env does not raise
    exception.
    """
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["BRANCH_NAME"]
    del os.environ["SEMAPHORE"]


# Generated at 2022-06-14 04:51:02.482630
# Unit test for function checker
def test_checker():
    """
    Checks that checker converts AssertionError to CiVerificationError
    """
    @checker
    def dummy_func():
        """
        Does nothing except raise an AssertionError
        """
        assert False

    dummy_func()

# Generated at 2022-06-14 04:51:07.998033
# Unit test for function circle
def test_circle():
    os.environ.update(
        {
            "CIRCLECI": "true",
            "CIRCLE_BRANCH": "master",
            "CI_PULL_REQUEST": "https://github.com/org/rep/pull/1",
        }
    )

    check()

# Generated at 2022-06-14 04:51:12.799741
# Unit test for function gitlab
def test_gitlab():
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    assert gitlab('master')
    os.environ['CI_COMMIT_REF_NAME'] = 'not-master'
    try:
        gitlab('master')
    except CiVerificationError:
        return
    assert False

# Generated at 2022-06-14 04:51:16.279576
# Unit test for function checker
def test_checker():
    def good_func():
        pass

    def bad_func():
        assert False

    for f in good_func, checker(good_func):
        assert f() == True

    for f in bad_func, checker(bad_func):
        try:
            f()
        except CiVerificationError:
            pass

# Generated at 2022-06-14 04:51:27.602735
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "jenkins"
    os.environ["BRANCH_NAME"] = "branch"
    assert jenkins("branch")
    os.environ["BRANCH_NAME"] = "wrong_branch"
    failed = False
    try:
        jenkins("branch")
    except CiVerificationError:
        failed = True
    assert failed
    del os.environ["BRANCH_NAME"]
    os.environ["GIT_BRANCH"] = "branch"
    assert jenkins("branch")
    os.environ["GIT_BRANCH"] = "wrong_branch"
    failed = False
    try:
        jenkins("branch")
    except CiVerificationError:
        failed = True

# Generated at 2022-06-14 04:51:33.218433
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "sprint/26/dev"
    bitbucket("sprint/26/dev")
    assert "BITBUCKET_PR_ID" not in os.environ
    # assert "BITBUCKET_BRANCH" in os.environ

if __name__ == '__main__':
    test_bitbucket()

# Generated at 2022-06-14 04:51:54.519215
# Unit test for function bitbucket
def test_bitbucket():
    """Test function bitbucket"""
    os.environ["BITBUCKET_BUILD_NUMBER"] = "test"
    os.environ["BITBUCKET_BRANCH"] = "test"
    os.environ["BITBUCKET_REPO_OWNER"] = "test"
    os.environ["BITBUCKET_REPO_SLUG"] = "test"
    os.environ["BITBUCKET_PR_ID"] = "test"
    bitbucket("test")



# Generated at 2022-06-14 04:51:58.769424
# Unit test for function circle
def test_circle():
    try:
        os.environ['CIRCLECI'] = "true"
        os.environ['CIRCLE_BRANCH'] = "master"
        circle("master")
        assert True
    except AssertionError:
        assert False
        

# Generated at 2022-06-14 04:52:05.405413
# Unit test for function bitbucket
def test_bitbucket():
    # Check that it works when the environment is appropriate
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    assert bitbucket("master")

    # Check that it works when the environment is appropriate
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "2"
    try:
        bitbucket("master")
        assert False
    except CiVerificationError:
        assert True

    # Check that it works when the environment is appropriate
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"


# Generated at 2022-06-14 04:52:11.068841
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["SEMAPHORE"] = "true"
    os.environ["CIRCLECI"] = "true"
    os.environ["GITLAB_CI"] = "true"
    os.environ["JENKINS_URL"] = "http://localhost"
    os.environ["BITBUCKET_BUILD_NUMBER"] = "true"

    assert check("master") is True

# Generated at 2022-06-14 04:52:20.486595
# Unit test for function jenkins
def test_jenkins():
    assert jenkins("master")
    os.environ["BRANCH_NAME"] = "something"
    assert not jenkins("master")
    os.environ["BRANCH_NAME"] = "master"
    assert jenkins("master")
    del(os.environ['BRANCH_NAME'])
    os.environ["GIT_BRANCH"] = "something"
    assert not jenkins("master")
    os.environ["GIT_BRANCH"] = "master"
    assert jenkins("master")
    del(os.environ['GIT_BRANCH'])
    os.environ["JENKINS_URL"] = "http://example.com"
    assert not jenkins("master")

# Generated at 2022-06-14 04:52:27.206854
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "test"
    os.environ["PULL_REQUEST_NUMBER"] = "1"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert semaphore("test") is True
    assert semaphore("granch") is False
    assert semaphore("") is False

    os.environ["PULL_REQUEST_NUMBER"] = None
    assert semaphore("test") is True
    assert semaphore("granch") is False
    assert semaphore("") is False

    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    assert semaphore("test") is True
    assert semaphore("granch") is False
    assert semaphore("") is False

   

# Generated at 2022-06-14 04:52:30.111975
# Unit test for function frigg
def test_frigg():
    test_frigg_basic()
    test_frigg_pr()
    test_frigg_incorrect_branch()


# Generated at 2022-06-14 04:52:31.286032
# Unit test for function travis
def test_travis():
    assert travis("master")



# Generated at 2022-06-14 04:52:32.351259
# Unit test for function jenkins
def test_jenkins():
    assert checker(jenkins)("master")

# Generated at 2022-06-14 04:52:43.599823
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    check("master")

    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "true"
    try:
        check("master")
        assert False
    except CiVerificationError:
        pass

    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"

# Generated at 2022-06-14 04:53:10.708455
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "1"

    branch_name = os.environ["BITBUCKET_BRANCH"]
    assert branch_name is not None
    assert os.environ["BITBUCKET_PR_ID"]  # pull request id
    
    

# Generated at 2022-06-14 04:53:13.485621
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master") is True

# Generated at 2022-06-14 04:53:14.814468
# Unit test for function frigg
def test_frigg():
    assert frigg('master') == True



# Generated at 2022-06-14 04:53:22.285713
# Unit test for function semaphore
def test_semaphore():
    import os
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = ''
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    semaphore('master')
    os.environ['BRANCH_NAME'] = 'develop'
    try:
        semaphore('master')
    except CiVerificationError:
        pass
    finally:
        os.environ['BRANCH_NAME'] = 'master'
        os.environ['PULL_REQUEST_NUMBER'] = '1'
        try:
            semaphore('master')
        except CiVerificationError:
            pass
        finally:
            os.environ['BRANCH_NAME'] = 'master'
            os.en

# Generated at 2022-06-14 04:53:28.150177
# Unit test for function jenkins
def test_jenkins():
    """
    Unit test for function jenkins
    """
    assert jenkins("abc")
    os.environ["BRANCH_NAME"] = "abc"
    assert jenkins("abc")
    os.environ["JENKINS_URL"] = "https://jenkins.example.com"
    assert jenkins("abc")



# Generated at 2022-06-14 04:53:31.585209
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    travis('master')


# Generated at 2022-06-14 04:53:34.725221
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "test"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("test")



# Generated at 2022-06-14 04:53:36.651748
# Unit test for function frigg
def test_frigg():
    assert frigg("master") == True



# Generated at 2022-06-14 04:53:40.820417
# Unit test for function bitbucket
def test_bitbucket():
    assert bitbucket("master")
    os.environ["BITBUCKET_BUILD_NUMBER"] = "12345"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "0"
    assert not bitbucket("master")


# Generated at 2022-06-14 04:53:48.503148
# Unit test for function semaphore
def test_semaphore():
    # We expect all the tests to pass
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")

    # Wrong branch, still expect it to pass
    os.environ["BRANCH_NAME"] = "wrong"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert not semaphore("master")

    # Pull request, expect to fail
    os.environ["BRANCH_NAME"] = "master"

# Generated at 2022-06-14 04:54:43.373595
# Unit test for function circle
def test_circle():
    circle("master")

# Generated at 2022-06-14 04:54:47.949291
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_IID"] = "12345"
    try:
        gitlab(branch="master")
    except CiVerificationError as e:
        assert "verification check" in str(e)



# Generated at 2022-06-14 04:54:57.279541
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "testBranch"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    assert frigg("testBranch") is True
    os.environ["FRIGG_BUILD_BRANCH"] = "testBranch2"
    assert frigg("testBranch") is False
    del os.environ["FRIGG_BUILD_BRANCH"]
    assert frigg("testBranch") is False
    os.environ["FRIGG_PULL_REQUEST"] = "true"
    assert frigg("testBranch") is False
    del os.environ["FRIGG_PULL_REQUEST"]

# Generated at 2022-06-14 04:55:08.733706
# Unit test for function gitlab
def test_gitlab():
    os.environ = {
        "CI_COMMIT_REF_NAME": "master",
        "GITLAB_CI": "true"
    }
    try:
        gitlab("master")
    except CiVerificationError as e:
        assert False, "gitlab checker should pass for a successful build"
    os.environ['CI_COMMIT_REF_NAME'] = "develop"
    try:
        gitlab("master")
        assert False, "gitlab checker should fail for a merge request"
    except CiVerificationError:
        pass
    os.environ['CI_COMMIT_REF_NAME'] = "master"
    os.environ['GITLAB_CI'] = "false"