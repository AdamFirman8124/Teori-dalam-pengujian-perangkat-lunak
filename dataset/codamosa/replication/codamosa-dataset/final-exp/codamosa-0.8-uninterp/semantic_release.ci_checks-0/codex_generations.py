

# Generated at 2022-06-14 04:45:15.683792
# Unit test for function checker
def test_checker():
    """
    Unit test for checker using standard assert
    """
    def func(string: str):
        """Returns true if string is equal to 'testing'"""
        assert string == "testing"
    @checker
    def func_wrapper(*args, **kwargs):
        """Returns true if string is equal to 'testing'"""
        assert args[0] == "testing"

    func("testing")

    func_wrapper("testing")



# Generated at 2022-06-14 04:45:23.679312
# Unit test for function checker
def test_checker():
    def raises_exception():
        raise AssertionError()

    def returns_false():
        return False

    def returns_true():
        return True

    def returns_none():
        return None

    assert checker(returns_true)()
    assert not checker(returns_false)()
    assert not checker(returns_none)()

    try:
        checker(raises_exception)()
        assert False, 'Raised exception was not captured'
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:45:31.407462
# Unit test for function semaphore
def test_semaphore():
    # remove all variables from the environment
    for var in os.environ:
        del os.environ[var]

    # add the variables for semaphore
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"

    check()

    # add the variables for semaphore
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "1"


# Generated at 2022-06-14 04:45:41.865775
# Unit test for function travis
def test_travis():
    os.system('export TRAVIS=true && export TRAVIS_BRANCH=master && export TRAVIS_PULL_REQUEST=false')
    travis('master')
    os.system('export TRAVIS_BRANCH=develop && export TRAVIS_PULL_REQUEST=false')
    try:
        travis('master')
    except CiVerificationError:
        assert True
    os.system('export TRAVIS_BRANCH=master && export TRAVIS_PULL_REQUEST=true')
    try:
        travis('master')
    except CiVerificationError:
        assert True


# Generated at 2022-06-14 04:45:47.232320
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["FRIGG"] = None
    os.environ["SEMAPHORE"] = None

    check()
    del os.environ["CI_COMMIT_REF_NAME"]
    del os.environ["FRIGG"]
    del os.environ["SEMAPHORE"]

# Generated at 2022-06-14 04:45:52.394082
# Unit test for function checker
def test_checker():
    @checker
    def _():
        assert False

    try:
        _()
        # If the assert from _ doesn't raise then the exception we expect
        # to be thrown hasn't been.
        raise AssertionError("Expected AssertionError")
    except CiVerificationError:
        pass # Expected



# Generated at 2022-06-14 04:45:57.491245
# Unit test for function checker
def test_checker():
    @checker
    def check_fail():
        assert False
    
    @checker
    def check_pass():
        assert True

    try:
        check_fail()
    except:
        assert True
    else:
        assert False

    try:
        check_pass()
    except:
        assert False
    else:
        assert True

# Generated at 2022-06-14 04:46:05.201902
# Unit test for function jenkins
def test_jenkins():
    """
    Test for the jenkins check.

    :return: True if the tests passes successfully.
    """
    # Test branch name not set
    os.environ["JENKINS_URL"] = "https://example.com/jenkins"
    os.environ["BRANCH_NAME"] = "release/1.2.3"
    os.environ["GIT_BRANCH"] = None
    os.environ["CHANGE_ID"] = None
    try:
        jenkins()
        # Shouldn't get here, because jenkins should raise an assertion error
        return False
    except CiVerificationError:
        pass
    os.environ["GIT_BRANCH"] = "release/1.2.3"
    os.environ["BRANCH_NAME"] = None

# Generated at 2022-06-14 04:46:07.945307
# Unit test for function travis
def test_travis():
    """
    Unit test for function travis
    :param
    :return:
    """
    travis("master")


# Generated at 2022-06-14 04:46:19.779914
# Unit test for function frigg
def test_frigg():
    """
    test_frigg
    """
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "5"
    assert frigg("master") is True
    os.environ["FRIGG_PULL_REQUEST"] = None
    assert frigg("master") is False
    os.environ["FRIGG_BUILD_BRANCH"] = "feature/1"
    assert frigg("master") is True
    del os.environ["FRIGG"]
    del os.environ["FRIGG_BUILD_BRANCH"]
    del os.environ["FRIGG_PULL_REQUEST"]

# Generated at 2022-06-14 04:46:45.986881
# Unit test for function semaphore
def test_semaphore():
    """
    The function semaphore is tested when a correct environment is
    simulated, and when an empty environment is simulated.
    """
    try:
        os.environ["BRANCH_NAME"] = "master"
        os.environ["PULL_REQUEST_NUMBER"] = None
        os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
        semaphore("master")
    except CiVerificationError:
        os.environ.clear()
        raise AssertionError('The function semaphore did not pass the CiVerificationError test.')

    try:
        os.environ.clear()
        semaphore("master")
    except CiVerificationError:
        pass
    else:
        os.environ.clear()

# Generated at 2022-06-14 04:46:57.472779
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
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    check()
    del os.environ["SEMAPHORE"]
    del os.environ["BRANCH_NAME"]

# Generated at 2022-06-14 04:47:04.191564
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["BRANCH_NAME"] = "develop"
    os.environ["CI_PULL_REQUEST"] = ""
    assert check("develop")

    os.environ["CIRCLECI"] = "true"
    os.environ["BRANCH_NAME"] = "develop"
    os.environ["CI_PULL_REQUEST"] = "true"
    assert not check("develop")

# Generated at 2022-06-14 04:47:11.166299
# Unit test for function check
def test_check():
    # Test Travis CI
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS"] = "true"
    check()
    del os.environ["TRAVIS_BRANCH"]
    del os.environ["TRAVIS_PULL_REQUEST"]
    del os.environ["TRAVIS"]

    # Test Circle CI
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CIRCLECI"] = "true"
    check()
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CIRCLECI"]

    # Test Semaphore CI

# Generated at 2022-06-14 04:47:20.352079
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = ""
    frigg("master")

    os.environ["FRIGG_BUILD_BRANCH"] = "not_master"
    os.environ["FRIGG_PULL_REQUEST"] = ""
    try:
        frigg("master")
        assert False, "Wrong environment checks should have been failed."
    except CiVerificationError as e:
        assert str(e) == "The verification check for the environment did not pass."

    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"]

# Generated at 2022-06-14 04:47:22.858505
# Unit test for function gitlab
def test_gitlab():
    try:
        os.environ["CI_COMMIT_REF_NAME"] = "master"
        assert gitlab("master") == True
        os.environ["CI_COMMIT_REF_NAME"] = "not-master"
        gitlab("master")
    except CiVerificationError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:47:26.584500
# Unit test for function gitlab
def test_gitlab():
    assert gitlab("master")
    os.environ["CI_COMMIT_REF_NAME"] = "not_master"
    with pytest.raises(CiVerificationError) as excinfo:
        gitlab("master")
    assert "verification check for the environment did not pass." in str(excinfo.value)


# Generated at 2022-06-14 04:47:29.424748
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "true"
    os.environ["GIT_BRANCH"] = "test"
    os.environ["CHANGE_ID"] = "test"
    jenkins("test")


# Generated at 2022-06-14 04:47:34.247424
# Unit test for function circle
def test_circle():
    assert circle.__name__ == 'circle'
    assert circle.__doc__ == "Performs necessary checks to ensure that the circle build is one that should create releases.\n\n:param branch: The branch the environment should be running against.\n"

# Generated at 2022-06-14 04:47:42.081766
# Unit test for function travis
def test_travis():
    # Set up Travis environment variable
    os.environ['TRAVIS_BRANCH'] = 'dev'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'

    # Unit test function travis
    try:
        travis(branch='dev')
    except Exception:
        print('Unit test failed! Environment variables are not in place')
    # Tear down Travis
    os.environ.pop('TRAVIS_BRANCH', None)
    os.environ.pop('TRAVIS_PR', None)



# Generated at 2022-06-14 04:48:00.754192
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()



# Generated at 2022-06-14 04:48:04.425708
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "test"
    os.environ["PULL_REQUEST_NUMBER"] = "123"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    semaphore("test")

# Generated at 2022-06-14 04:48:13.872197
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "branch"
    os.environ["JENKINS_URL"] = "jobs"
    os.environ["CHANGE_ID"] = "1234"
    try:
        jenkins("master")
        assert False  # Should raise
    except CiVerificationError:
        pass
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "jobs"
    os.environ["CHANGE_ID"] = None
    jenkins("master")

# Generated at 2022-06-14 04:48:15.683572
# Unit test for function bitbucket
def test_bitbucket():
    assert bitbucket("master")


# Generated at 2022-06-14 04:48:20.414510
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "jenkins1.com"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = ""

    check()

    assert 1 == 1

# Generated at 2022-06-14 04:48:26.851884
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "false"
    os.environ["CIRCLE_BRANCH"] = "master"

    check()

    os.environ["CIRCLE_BRANCH"] = "other"

    try:
        check()
        assert False
    except CiVerificationError:
        pass

    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CI_PULL_REQUEST"]
    del os.environ["CIRCLECI"]

# Generated at 2022-06-14 04:48:28.922897
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "CI_COMMIT_REF_NAME"
    gitlab("master")



# Generated at 2022-06-14 04:48:31.962340
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()



# Generated at 2022-06-14 04:48:42.881408
# Unit test for function gitlab
def test_gitlab():
    assert gitlab("master")
    os.environ["CI_COMMIT_REF_NAME"] = "not master"
    try:
        gitlab("master")
    except CiVerificationError:
        assert True
    else:
        assert False
    del os.environ["CI_COMMIT_REF_NAME"]
    os.environ["CI_MERGE_REQUEST_ID"] = "1234"
    try:
        gitlab("master")
    except CiVerificationError:
        assert True
    else:
        assert False
    del os.environ["CI_MERGE_REQUEST_ID"]



# Generated at 2022-06-14 04:48:45.081436
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'test'
    travis('test')


# Generated at 2022-06-14 04:49:22.930781
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = 'branch'
    os.environ['BITBUCKET_PR_ID'] = '1'
    check('branch') # should not raise an error
    os.environ['BITBUCKET_PR_ID'] = ''
    check('branch') # should not raise an error
    os.environ['BITBUCKET_PR_ID'] = '1'
    check('not_branch') # should raise an error
    os.environ['BITBUCKET_PR_ID'] = '1'
    os.environ['BITBUCKET_BRANCH'] = 'not_branch'
    check('branch') # should raise an error
    del os.environ['BITBUCKET_BRANCH']

# Generated at 2022-06-14 04:49:26.387826
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("master")


# Generated at 2022-06-14 04:49:32.476470
# Unit test for function jenkins
def test_jenkins():
    # Set some environment variables
    os.environ["JENKINS_URL"] = "http://example.com"
    os.environ["BRANCH_NAME"] = "feature-branch"
    os.environ["GIT_BRANCH"] = "feature-branch"
    os.environ["CHANGE_ID"] = "123"

    # Run the check, which should fail
    check()

# Generated at 2022-06-14 04:49:36.060690
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = 'true'
    os.environ['CIRCLE_BRANCH'] = 'master'
    os.environ['CI_PULL_REQUEST'] = '' # empty value returns false
    check("master")

# Generated at 2022-06-14 04:49:45.853407
# Unit test for function circle
def test_circle():
    """
    Test that the circle ci check works
    """
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    assert circle("master")
    del os.environ["CIRCLE_BRANCH"]
    assert not circle("master")
    os.environ["CIRCLE_BRANCH"] = "develop"
    assert not circle("master")
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "True"
    assert not circle("master")
    del os.environ["CIRCLECI"]
    assert not circle("master")

# Generated at 2022-06-14 04:49:52.402013
# Unit test for function checker
def test_checker():
    def test_function():
        assert True

    def broken_test_function():
        assert False

    decorated_function = checker(test_function)
    decorated_function()

    try:
        decorated_function = checker(broken_test_function)
        decorated_function()
    except CiVerificationError:
        pass
    else:
        raise AssertionError("CiVerificationError not raised")

# Generated at 2022-06-14 04:49:59.025375
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    check()
    del os.environ["CIRCLECI"]
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CI_PULL_REQUEST"]



# Generated at 2022-06-14 04:50:11.834949
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    try:
        travis()
    except CiVerificationError:
        assert False
    os.environ["TRAVIS_BRANCH"] = "develop"
    try:
        travis()
        assert False
    except CiVerificationError:
        pass
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        travis()
        assert False
    except CiVerificationError:
        pass
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS_BRANCH"] = "master"


# Generated at 2022-06-14 04:50:14.790250
# Unit test for function checker
def test_checker():
    @checker
    def foo():
        pass

    assert foo() is True

    @checker
    def bar():
        raise AssertionError()

    try:
        bar()
        assert False
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:50:24.400173
# Unit test for function jenkins
def test_jenkins():
    # Test that no environment variables is set
    os.environ["BRANCH_NAME"] = None
    os.environ["GIT_BRANCH"] = None
    os.environ["JENKINS_URL"] = None
    os.environ["CHANGE_ID"] = None
    try:
        jenkins('master')
    except CiVerificationError:
        assert not os.environ.get('CHANGE_ID')

    # Test for Pull Request
    os.environ["BRANCH_NAME"] = 'master'
    os.environ["GIT_BRANCH"] = 'master'
    os.environ["JENKINS_URL"] = 'http://localhost'
    os.environ["CHANGE_ID"] = '1'

# Generated at 2022-06-14 04:51:28.775902
# Unit test for function bitbucket
def test_bitbucket():
    """
    Unit test for function bitbucket
    """
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "1"
    try:
        bitbucket("master")
        assert False
    except CiVerificationError:
        assert True
    os.environ["BITBUCKET_PR_ID"] = None
    assert bitbucket("master")


# Generated at 2022-06-14 04:51:32.222765
# Unit test for function travis
def test_travis():
    # Given
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    # When
    travis("master")


# Generated at 2022-06-14 04:51:34.967989
# Unit test for function gitlab
def test_gitlab():
    """
    Test that semantic_release.ci_checks.gitlab is working properly.
    """
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    gitlab("master")



# Generated at 2022-06-14 04:51:46.492156
# Unit test for function circle
def test_circle():
    import os
    import unittest
    os.environ['CIRCLECI'] = 'true'
    os.environ['CIRCLE_BRANCH'] = 'master'
    os.environ['CI_PULL_REQUEST'] = 'false'

    from semantic_release import ci_cd
    unittest.TestCase().assertEqual(ci_cd.circle('master'), True)
    os.environ['CIRCLE_BRANCH'] = 'release'
    unittest.TestCase().assertEqual(ci_cd.circle('master'), False)
    os.environ['CIRCLE_BRANCH'] = 'master'
    os.environ['CI_PULL_REQUEST'] = 'true'

# Generated at 2022-06-14 04:51:49.136855
# Unit test for function checker
def test_checker():
    @checker
    def foo():
        assert False

    with pytest.raises(CiVerificationError):
        foo()

# Generated at 2022-06-14 04:52:00.591543
# Unit test for function gitlab
def test_gitlab():
    """
    Test for ci_checks.gitlab.
    """
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = "100"
    try:
        gitlab("master")
    except CiVerificationError as error:
        assert error.message == "The verification check for the environment did not pass."
    else:
        assert False
    os.environ.pop("CI_MERGE_REQUEST_ID")
    try:
        gitlab("master")
    except CiVerificationError as error:
        assert error.message == "The verification check for the environment did not pass."
    else:
        assert False
    os.environ.pop("CI_COMMIT_REF_NAME")

# Generated at 2022-06-14 04:52:06.836099
# Unit test for function checker
def test_checker():
    def func(a):
        return a

    assert checker(func)(1) == 1

    def func2(p):
        assert p == 1

    try:
        checker(func2)(2)
    except CiVerificationError:
        return
    assert False

# Generated at 2022-06-14 04:52:10.206615
# Unit test for function gitlab
def test_gitlab():
    os.environ.pop('GITLAB_CI', None)
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    os.environ['CI_MERGE_REQUEST_IID'] = '1234'
    gitlab('master')

# Generated at 2022-06-14 04:52:16.497152
# Unit test for function gitlab
def test_gitlab():
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    os.environ['CI_MERGE_REQUEST_ID'] = ''
    check()
    assert os.environ.get('CI_COMMIT_REF_NAME') == 'master'
    os.environ.pop('CI_COMMIT_REF_NAME')
    os.environ.pop('CI_MERGE_REQUEST_ID')



# Generated at 2022-06-14 04:52:19.402583
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    assert bitbucket('master') == True

# Generated at 2022-06-14 04:54:19.656516
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    assert semaphore("master")
    del os.environ["BRANCH_NAME"]
    assert semaphore("master")



# Generated at 2022-06-14 04:54:20.465308
# Unit test for function gitlab
def test_gitlab():
    branch = "master"
    assert checker(gitlab)(branch)

# Generated at 2022-06-14 04:54:28.376842
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "succeeded"
    assert semaphore("master")

    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert semaphore("master")

    os.environ["BRANCH_NAME"] = "dev"
    assert semaphore("dev")

    os.environ["PULL_REQUEST_NUMBER"] = "123"
    assert semaphore("dev")



# Generated at 2022-06-14 04:54:29.201913
# Unit test for function bitbucket
def test_bitbucket():
    branch = "master"
    assert bitbucket(branch) == None

# Generated at 2022-06-14 04:54:30.388558
# Unit test for function gitlab
def test_gitlab():
    """ Check if we can detect that the CI is gitlab """
    os.environ["GITLAB_CI"] = "true"
    check()

# Generated at 2022-06-14 04:54:31.290149
# Unit test for function check
def test_check():
    # test check function
    try:
        check()
    except:
        assert False

# Generated at 2022-06-14 04:54:32.879432
# Unit test for function semaphore
def test_semaphore():
    """
    Perform a test against the function semaphore.
    """
    semaphore('master')

# Generated at 2022-06-14 04:54:41.018117
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master")
    os.environ["TRAVIS_BRANCH"] = "develop"
    with assertRaises(CiVerificationError):
        travis("master")
    assert travis("develop")
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    with assertRaises(CiVerificationError):
        travis("develop")



# Generated at 2022-06-14 04:54:48.590606
# Unit test for function gitlab
def test_gitlab():
    #
    # Setup
    #
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = "21"

    #
    # gitlab pull request
    #
    try:
        gitlab("master")
    except CiVerificationError as err:
        assert str(err) == "The verification check for the environment did not pass."
        assert type(err) == CiVerificationError

    #
    # gitlab master, tag
    #
    del os.environ["CI_MERGE_REQUEST_ID"]
    try:
        gitlab("master")
        gitlab("v1.2.3")
    except CiVerificationError as err:
        assert str(err) == "The verification check for the environment did not pass."

# Generated at 2022-06-14 04:54:55.599172
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    circle("master")
    del os.environ["CIRCLE_BRANCH"]
    os.environ["CI_PULL_REQUEST"] = "true"
    os.environ["CIRCLE_BRANCH"] = "release"
    circle("release")
    del os.environ["CI_PULL_REQUEST"]
    del os.environ["CIRCLECI"]
