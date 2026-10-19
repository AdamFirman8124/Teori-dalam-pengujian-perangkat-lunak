

# Generated at 2022-06-14 04:45:19.016880
# Unit test for function semaphore
def test_semaphore():
    """
    Unit test for function semaphore
    """
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")

    os.environ["BRANCH_NAME"] = "dev"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"

    success = False
    try:
        semaphore("master")
    except CiVerificationError:
        success = True
    assert success



# Generated at 2022-06-14 04:45:28.358447
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"

    assert semaphore("master")

    del os.environ["SEMAPHORE_THREAD_RESULT"]

    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ["BRANCH_NAME"] = "develop"

    assert semaphore("master") == False

# Generated at 2022-06-14 04:45:38.503240
# Unit test for function bitbucket
def test_bitbucket():
    """
    Test case for function bitbucket
    """
    os.environ['BITBUCKET_BUILD_NUMBER'] = '15'
    os.environ['BITBUCKET_BRANCH'] = 'master'
    os.environ['BITBUCKET_PR_ID'] = '1'
    try:
        bitbucket("master")
        assert False
    except CiVerificationError as err:
        assert True
        assert err.message == 'The verification check for the environment did not pass.'
    os.environ.pop('BITBUCKET_PR_ID')



# Generated at 2022-06-14 04:45:42.928811
# Unit test for function circle
def test_circle():
    """
    Test circle function
    """
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    os.environ["CIRCLE_BUILD_NUM"] = "123"
    os.environ["CIRCLE_JOB"] = "check_semantic_release"
    try:
        circle()
    except CiVerificationError:
        assert False, "Error in circle function"
    os.environ["CIRCLE_JOB"] = "should_fail"
    try:
        circle()
        assert False, "Error in circle function"
    except CiVerificationError:
        assert True
    os.environ["CIRCLE_JOB"]

# Generated at 2022-06-14 04:45:54.020950
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = 'master'
    os.environ['BITBUCKET_PR_ID'] = '1'
    assert bitbucket('master') == False
    os.environ['BITBUCKET_BRANCH'] = 'master'
    os.environ['BITBUCKET_PR_ID'] = '0'
    assert bitbucket('master') == True
    os.environ['BITBUCKET_BRANCH'] = 'test'
    os.environ['BITBUCKET_PR_ID'] = '1'
    assert bitbucket('master') == False
    os.environ['BITBUCKET_BRANCH'] = 'test'
    os.environ['BITBUCKET_PR_ID'] = '0'

# Generated at 2022-06-14 04:46:01.006415
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    del os.environ["CI_MERGE_REQUEST_ID"]
    assert os.environ.get("CI_COMMIT_REF_NAME") == "master"
    assert not os.environ.get("CI_MERGE_REQUEST_ID")
    check(branch="master")
    del os.environ["CI_COMMIT_REF_NAME"]
    del os.environ["CI_MERGE_REQUEST_ID"]

# Generated at 2022-06-14 04:46:03.461398
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    circle("master")



# Generated at 2022-06-14 04:46:08.388915
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    assert frigg("master")

    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    assert not frigg("master")

    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "20"
    assert not frigg("master")

    del os.environ["FRIGG"]

# Generated at 2022-06-14 04:46:18.347457
# Unit test for function semaphore
def test_semaphore():
    # Set environment variables
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    semaphore("master")

    # Assert False
    os.environ["BRANCH_NAME"] = "staging"
    os.environ["PULL_REQUEST_NUMBER"] = "false"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    try:
        semaphore("master")
    except CiVerificationError:
        assert True

# Generated at 2022-06-14 04:46:26.789427
# Unit test for function bitbucket
def test_bitbucket():
    """
    Unit test for function bitbucket
    """

    os.environ["BITBUCKET_BRANCH"] = "master"
    check()

    os.environ["BITBUCKET_BRANCH"] = "bugfix"
    check(branch="bugfix")

    os.environ["BITBUCKET_PR_ID"] = "1234"
    check()  # Check passes without error because there is an error in the CI checker
    del os.environ["BITBUCKET_PR_ID"]

# Generated at 2022-06-14 04:46:39.417860
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'https://my.jenkins.com'
    os.environ['BRANCH_NAME'] = 'master'
    check()


# Generated at 2022-06-14 04:46:42.032923
# Unit test for function checker
def test_checker():
    try:
        raise AssertionError
    except AssertionError:
        try:
            checker(lambda: 1 / 0)()
        except CiVerificationError:
            pass

# Generated at 2022-06-14 04:46:48.573932
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["JENKINS_URL"] = "jenkins_url"
    os.environ["CHANGE_ID"] = "pull_request_id"
    jenkins("master")

# Generated at 2022-06-14 04:46:50.288626
# Unit test for function checker
def test_checker():
    def func():
        raise AssertionError("This")

    assert checker(func)()

# Generated at 2022-06-14 04:47:02.968748
# Unit test for function jenkins
def test_jenkins():
    os.environ["CI_COMMIT_REF_NAME"] = "branch"
    os.environ["CI_PULL_REQUEST"] = "false"
    os.environ["JENKINS_URL"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = "pull request"
    
    check()

    del os.environ["CI_COMMIT_REF_NAME"]
    del os.environ["CI_PULL_REQUEST"]
    del os.environ["JENKINS_URL"]
    del os.environ["BRANCH_NAME"]
    del os.environ["GIT_BRANCH"]
    del os.environ

# Generated at 2022-06-14 04:47:08.604282
# Unit test for function jenkins
def test_jenkins():
    assert os.environ.get("JENKINS_URL") is None
    assert os.environ.get("BRANCH_NAME") is None
    os.environ["JENKINS_URL"] = 'true'   
    os.environ["BRANCH_NAME"] = 'master'
    assert os.environ.get("JENKINS_URL") == 'true'
    assert os.environ.get("BRANCH_NAME") == 'master'
    jenkins('master')

# Generated at 2022-06-14 04:47:12.919381
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BUILD_NUMBER'] = '1'
    os.environ['BITBUCKET_BRANCH'] = 'master'
    os.environ['BITBUCKET_PR_ID'] = '0'
    branch = 'master'

    bitbucket(branch)



# Generated at 2022-06-14 04:47:20.624962
# Unit test for function circle
def test_circle():
    # Test when the branch is correct
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    assert circle("master") is True

    # Test when the branch is different
    os.environ["CIRCLE_BRANCH"] = "develop"
    with pytest.raises(CiVerificationError):
        circle("master")

    # Test when the branch is correct but the build is a pull request
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "1"
    with pytest.raises(CiVerificationError):
        circle("master")



# Generated at 2022-06-14 04:47:28.313648
# Unit test for function checker
def test_checker():
    """
    test_checker - test for function checker
    """
    import pytest
    from semantic_release.errors import CiVerificationError

    @checker
    def test(branch: str):
        """
        test - function used to test checker
        """
        assert os.environ.get("TRAVIS_BRANCH") == branch

    test("master")

    with pytest.raises(CiVerificationError):
        test("")



# Generated at 2022-06-14 04:47:31.086152
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    # raise error
    os.environ["TRAVIS_BRANCH"] = "dev"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    assert check() == False


# Generated at 2022-06-14 04:47:50.902583
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg("master")
    # FRIGG_PULL_REQUEST is not set
    frigg("master")
    # FRIGG_PULL_REQUEST is set
    os.environ["FRIGG_PULL_REQUEST"] = "1"
    assert frigg("master") is False
    del os.environ["FRIGG_PULL_REQUEST"]
    # FRIGG_BUILD_BRANCH is not set
    assert frigg("master") is False
    # FRIGG_BUILD_BRANCH is not master
    os.environ["FRIGG_BUILD_BRANCH"] = "develop"

# Generated at 2022-06-14 04:47:52.061372
# Unit test for function check
def test_check():
    assert check("master") == True

# Generated at 2022-06-14 04:47:58.280153
# Unit test for function bitbucket
def test_bitbucket():
    '''
    Unit test for function bitbucket
    '''
    # Set environment variables
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = None
    # Call the function
    bitbucket("master")
    # Delete environment variables
    del os.environ["BITBUCKET_BRANCH"]
    del os.environ["BITBUCKET_PR_ID"]


# Generated at 2022-06-14 04:48:04.905112
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")
    del os.environ["BRANCH_NAME"]
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["SEMAPHORE_THREAD_RESULT"]


# Generated at 2022-06-14 04:48:10.182110
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    check()



# Generated at 2022-06-14 04:48:16.348077
# Unit test for function semaphore
def test_semaphore():
    """Unit test"""
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = 'master'
    os.environ["PULL_REQUEST_NUMBER"] = '123'
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"

    branch = 'master'

    try:
        semaphore(branch)
    except CiVerificationError:
        assert True

    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    try:
        semaphore(branch)
    except CiVerificationError:
        assert False

# Generated at 2022-06-14 04:48:24.477965
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    semaphore(branch='master')
    os.environ['BRANCH_NAME'] = 'develop'
    os.environ['PULL_REQUEST_NUMBER'] = '123'
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'failed'
    try:
        semaphore(branch='master')
    except CiVerificationError:
        assert True

# Generated at 2022-06-14 04:48:32.978898
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    assert semaphore("master")
    del os.environ["SEMAPHORE_THREAD_RESULT"]
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert not semaphore("master")
    del os.environ["SEMAPHORE_THREAD_RESULT"]

# Generated at 2022-06-14 04:48:37.771547
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    assert travis("master")


# Generated at 2022-06-14 04:48:43.524426
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "false"
    os.environ["CIRCLE_BRANCH"] = "master"
    check()
    del os.environ["CIRCLECI"]
    del os.environ["CI_PULL_REQUEST"]
    del os.environ["CIRCLE_BRANCH"]



# Generated at 2022-06-14 04:48:59.676658
# Unit test for function frigg
def test_frigg():
    """
    Test for frigg build
    """
    expected = "master"
    actual = os.environ.get("FRIGG_BUILD_BRANCH")
    if os.environ.get("FRIGG") == "true":
        frigg(expected)



# Generated at 2022-06-14 04:49:09.892119
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    del os.environ["PULL_REQUEST_NUMBER"]
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    assert semaphore("master")

    os.environ["BRANCH_NAME"] = "dev"
    assert not semaphore("master")

    os.environ["PULL_REQUEST_NUMBER"] = "5"
    assert not semaphore("master")

    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert not semaphore("master")

# Generated at 2022-06-14 04:49:17.295524
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    assert circle("master")

    os.environ["CIRCLE_BRANCH"] = "non-master"
    assert not circle("master")

    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "18"
    assert not circle("master")

# Generated at 2022-06-14 04:49:27.546623
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "abc"
    os.environ["BITBUCKET_PR_ID"] = "0"
    assert bitbucket("abc")
    os.environ["BITBUCKET_PR_ID"] = "123"
    assert bitbucket("abc")
    del os.environ["BITBUCKET_BRANCH"]
    os.environ["BITBUCKET_PULL_REQUEST_BRANCH"] = "abc"
    assert bitbucket("abc")


# Generated at 2022-06-14 04:49:32.730066
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    test_gitlab.thrown_exception = False
    try:
        gitlab("master")
    except CiVerificationError:
        test_gitlab.thrown_exception = True
    assert not test_gitlab.thrown_exception



# Generated at 2022-06-14 04:49:40.663808
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "pull_request"
    try:
        circle("master")
    except CiVerificationError as err:
        assert str(err) == "The verification check for the environment did not pass."
    del os.environ["CIRCLE_BRANCH"]
    try:
        circle("master")
    except CiVerificationError as err:
        assert str(err) == "The verification check for the environment did not pass."
    os.environ["CI_PULL_REQUEST"] = "false"

# Generated at 2022-06-14 04:49:44.497085
# Unit test for function checker
def test_checker():
    """
    Test function checker by calling the checker
    with a function that raises an exception.
    """
    def func():
        """ Raises an exception"""
        raise AssertionError("This is an exception")

    assert checker(func)() is False

    try:
        checker(func)()
    except CiVerificationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:49:46.727606
# Unit test for function checker
def test_checker():
    # Given a function returning 0
    @checker
    def my_function():
        return 0

    # When I call the function
    # Then it should return 0
    assert my_function() == 0



# Generated at 2022-06-14 04:49:52.918423
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    if travis("master") == True:
        assert True
    elif travis("develop") == None:
        assert False
    elif travis("master") == None:
        assert False
    else:
        assert False



# Generated at 2022-06-14 04:50:03.327555
# Unit test for function frigg
def test_frigg():
    assert "TRAVIS" not in os.environ
    assert "SEMAPHORE" not in os.environ
    assert "CIRCLECI" not in os.environ
    assert "GITLAB_CI" not in os.environ
    assert "JENKINS_URL" not in os.environ
    assert "BITBUCKET_BUILD_NUMBER" not in os.environ

    branch = "somebranch"

    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = branch
    assert frigg(branch) is True

    os.environ["FRIGG_PULL_REQUEST"] = "true"

# Generated at 2022-06-14 04:50:33.697511
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ['FRIGG_PULL_REQUEST'] = ""
    assert frigg('master')



# Generated at 2022-06-14 04:50:37.133732
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = 'true'
    os.environ['CIRCLE_BRANCH'] = 'master'
    os.environ['CI_PULL_REQUEST'] = ''
    check()

# Generated at 2022-06-14 04:50:40.994501
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master")

# Generated at 2022-06-14 04:50:46.534061
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ.pop('FRIGG_PULL_REQUEST', None)
    check()
    os.environ['FRIGG_PULL_REQUEST'] = '123'
    check()
    os.environ['FRIGG_BUILD_BRANCH'] = 'test'
    check('test')

test_frigg()

# Generated at 2022-06-14 04:50:52.917081
# Unit test for function jenkins
def test_jenkins():
    from semantic_release.ci_checks import jenkins
    os.environ['JENKINS_URL'] = "https://ci.jenkins.io"
    os.environ['BRANCH_NAME'] = "master"
    os.environ['GIT_BRANCH'] = "master"
    os.environ['CHANGE_ID'] = ""
    assert jenkins()

    os.environ['BRANCH_NAME'] = "develop"
    os.unsetenv('GIT_BRANCH')
    try:
        jenkins()
        assert False
    except CiVerificationError:
        pass

    os.environ['BRANCH_NAME'] = "master"
    os.environ['CHANGE_ID'] = "jio"

# Generated at 2022-06-14 04:50:57.803257
# Unit test for function checker
def test_checker():
    @checker
    def func(branch: str):
        assert os.environ.get("TRAVIS") == "true"
        assert branch == "master"
        raise AssertionError()

    # Assert that it raises CiVerificationError
    try:
        func("master")
    except CiVerificationError:
        pass
    else:
        assert False, "Should have raised CiVerificationError"

    # Assert that it returns True
    func("master")

# Generated at 2022-06-14 04:51:02.905054
# Unit test for function gitlab
def test_gitlab():
    assert not gitlab("master")
    assert not gitlab("master")
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    assert not gitlab("master")
    assert gitlab("test")
    os.environ['CI_COMMIT_REF_NAME'] = ''
    assert gitlab("test")

# Generated at 2022-06-14 04:51:08.392841
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "succeeded"
    check()



# Generated at 2022-06-14 04:51:13.121528
# Unit test for function semaphore
def test_semaphore():
  branch = 'master'
  os.environ["BRANCH_NAME"] = branch
  os.environ["PULL_REQUEST_NUMBER"] = None
  os.environ["SEMAPHORE_THREAD_RESULT"] = None
  semaphore(branch)


# Generated at 2022-06-14 04:51:17.580806
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'test'
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['GIT_BRANCH'] = 'master'
    os.environ['CHANGE_ID'] = None
    
    check()

# Generated at 2022-06-14 04:52:15.003069
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = 'master'
    os.environ["BITBUCKET_PR_ID"] = ''

    bitbucket(branch='master')

    del os.environ["BITBUCKET_BRANCH"]
    del os.environ["BITBUCKET_PR_ID"]


# Generated at 2022-06-14 04:52:22.743389
# Unit test for function travis
def test_travis():
    os.environ["BRANCH_NAME"] = "master"

    try:
        travis("master")
    except:
        raise AssertionError("travis check failed")

    del os.environ["BRANCH_NAME"]
    try:
        travis("master")
        raise AssertionError("travis check failed")
    except AssertionError:
        pass

    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "1"
    try:
        travis("master")
        raise AssertionError("travis check failed")
    except AssertionError:
        pass



# Generated at 2022-06-14 04:52:28.654749
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "7"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = None
    os.environ["BITBUCKET_REPO_SLUG"] = "johndoe/project"
    os.environ["BITBUCKET_COMMIT"] = "753b49d053e3d63cff7e211fa490c1b8d4b4c4ec"
    os.environ["CI_MESSAGE"] = "This is a test commit message"
    os.environ["CI_COMMITTER_NAME"] = "John Doe"
    os.environ["CI_COMMITTER_EMAIL"] = "john@example.com"

# Generated at 2022-06-14 04:52:31.015379
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "release"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    frigg("release")
    assert "FRIGG" in os.environ
    assert "FRIGG_BUILD_BRANCH" in os.environ
    assert "FRIGG_PULL_REQUEST" in os.environ



# Generated at 2022-06-14 04:52:34.902154
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"

    result = travis("master")

    assert result == True



# Generated at 2022-06-14 04:52:41.751896
# Unit test for function checker
def test_checker():
    def a_func():
        raise AssertionError

    b_func = checker(a_func)

    try:
        a_func()
    except AssertionError:
        pass
    else:
        raise AssertionError("a_func should raise AssertionError")

    try:
        b_func()
    except CiVerificationError:
        pass
    else:
        raise AssertionError("Should have raised CiVerificationError")

# Generated at 2022-06-14 04:52:47.644419
# Unit test for function frigg
def test_frigg():
    """
    Test the frigg function if it works and throws the right error if not.
    """
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"

    # If the branch is the right one, it should pass
    frigg("master")

    # If the branch is wrong, it should raise the right error
    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    try:
        frigg("master")
        raise EnvironmentError("Expected assertion")
    except CiVerificationError:
        pass



# Generated at 2022-06-14 04:52:52.325132
# Unit test for function gitlab
def test_gitlab():
    """
    Test that correct variables are set in gitlab environment.
    """
    os.environ["CI_COMMIT_REF_NAME"] = "release-v0.1.0"
    check()
    assert 1



# Generated at 2022-06-14 04:53:02.364956
# Unit test for function travis
def test_travis():

    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master") is True
    del os.environ["TRAVIS_BRANCH"]
    del os.environ["TRAVIS_PULL_REQUEST"]

    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        travis("master")
    except CiVerificationError:
        return True
    raise SyntaxError("Travis verification did not throw error")


# Generated at 2022-06-14 04:53:13.204521
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "http://www.example.com/"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = None
    check()
    os.environ["BRANCH_NAME"] = "test"
    os.environ["GIT_BRANCH"] = "test"
    check("test")
    os.environ["GIT_BRANCH"] = None
    os.environ["CHANGE_ID"] = "test"
    try:
        check("test")
        assert False, "This is a pull request, should not pass"
    except CiVerificationError:
        pass

    os.environ["BRANCH_NAME"] = None