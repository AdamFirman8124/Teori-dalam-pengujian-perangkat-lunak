

# Generated at 2022-06-14 04:45:16.414302
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://jenkins.ci"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = "1"
    try:
        jenkins("master")
    except CiVerificationError as e:
        assert str(e) == "The verification check for the environment did not pass."


# Generated at 2022-06-14 04:45:28.582438
# Unit test for function travis
def test_travis():
    # Setup test environment
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "test_branch"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    # Run test
    try:
        travis("test_branch")
    except CiVerificationError:
        # This should be raised
        pass
    else:
        assert False

    travis("test_branch")

    try:
        travis("wrong_branch")
    except CiVerificationError:
        # This should be raised
        pass
    else:
        assert False

    os.environ["TRAVIS_PULL_REQUEST"] = "false"

    travis("test_branch")


# Generated at 2022-06-14 04:45:34.312883
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "12345"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "12345"
    import pytest

    with pytest.raises(CiVerificationError):
        bitbucket("master")
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("master")

# Generated at 2022-06-14 04:45:46.436741
# Unit test for function jenkins
def test_jenkins():
    # CI is not on
    os.environ["CIRCLE_BRANCH"] = "feature"
    with pytest.raises(CiVerificationError):
        check("feature")
    
    # Git branch is not equal to function argument
    os.environ["GIT_BRANCH"] = "feature"
    with pytest.raises(CiVerificationError):
        check("master")
    
    # CHANGE_ID is set
    os.environ["JENKINS_URL"] = "True"
    os.environ["CHANGE_ID"] = "1234"
    with pytest.raises(CiVerificationError):
        check("develop")
    
    # BRANCH_NAME is set
    os.environ.pop("GIT_BRANCH")

# Generated at 2022-06-14 04:45:52.439579
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = None
    check("master")
    os.environ["BITBUCKET_BRANCH"] = "foo"
    check("master")
    os.environ["BITBUCKET_PR_ID"] = "1"
    check("master")


# Generated at 2022-06-14 04:45:57.538052
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = None
    gitlab("master")
    del os.environ["CI_COMMIT_REF_NAME"]
    del os.environ["CI_MERGE_REQUEST_ID"]



# Generated at 2022-06-14 04:46:05.228144
# Unit test for function semaphore
def test_semaphore():
    def reset_environ():
        if os.environ.get('SEMAPHORE'):
            os.environ['SEMAPHORE'] = 'false'
        if os.environ.get('BRANCH_NAME'):
            os.environ['BRANCH_NAME'] = None
        if os.environ.get('PULL_REQUEST_NUMBER'):
            os.environ['PULL_REQUEST_NUMBER'] = None
        if os.environ.get('SEMAPHORE_THREAD_RESULT'):
            os.environ['SEMAPHORE_THREAD_RESULT'] = None

    os.environ['SEMAPHORE'] = 'true'
    os.environ['BRANCH_NAME'] = 'master'

# Generated at 2022-06-14 04:46:09.677161
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    frigg("master")

# Generated at 2022-06-14 04:46:15.671201
# Unit test for function checker
def test_checker():
    """
    Test the decorator checker

    :return:
    """
    @checker
    def dummy_check():
        """
        A dummy function that raises an AssertionError to test the checker decorator
        """
        assert False
    try:
        dummy_check()
    except AssertionError:
        assert False
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:46:20.732044
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore(os.environ.get("BRANCH_NAME"))



# Generated at 2022-06-14 04:46:31.141104
# Unit test for function check
def test_check():
    os.environ['TRAVIS'] = "true"
    os.environ['TRAVIS_BRANCH'] = "master"
    os.environ['TRAVIS_PULL_REQUEST'] = "false"
    check()

# Generated at 2022-06-14 04:46:34.091773
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'jenkins'
    os.environ['GIT_BRANCH'] = 'develop'
    jenkins('develop')

# Generated at 2022-06-14 04:46:40.270571
# Unit test for function circle
def test_circle():
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    circle(branch="master")
    del os.environ["CI_PULL_REQUEST"]
    circle(branch="master")
    # test for pull request
    os.environ["CI_PULL_REQUEST"] = "1"
    try:
        circle(branch="master")
        assert False, "Exception should be thrown"
    except CiVerificationError as error:
        assert str(error) == "The verification check for the environment did not pass."


# Generated at 2022-06-14 04:46:45.012820
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["GITLAB_CI"] = "true"
    check()
    del os.environ["GITLAB_CI"]

# Generated at 2022-06-14 04:46:48.286238
# Unit test for function travis
def test_travis():

        os.environ["TRAVIS_BRANCH"] = "master"
        os.environ["TRAVIS_PULL_REQUEST"] = "false"

        travis("master")


# Generated at 2022-06-14 04:47:00.796388
# Unit test for function jenkins
def test_jenkins():
    # Code coverage - on Jenkins
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "https://example.url"
    try:
        check()
    except CiVerificationError:
        assert False
    # Code coverage - not on Jenkins
    os.environ.pop("JENKINS_URL", None)
    try:
        check()
        assert False
    except CiVerificationError:
        pass
    # Code coverage -  on Jenkins, being in a pull request, branch master
    os.environ["CHANGE_ID"] = "123"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "https://example.url"

# Generated at 2022-06-14 04:47:01.838956
# Unit test for function frigg
def test_frigg():
    assert frigg("master") == True

# Generated at 2022-06-14 04:47:10.052593
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BUILD_NUMBER'] = "15"
    os.environ['BITBUCKET_BRANCH'] = "master"
    assert bitbucket("master") == True
    os.environ['BITBUCKET_BUILD_NUMBER'] = "15"
    os.environ['BITBUCKET_BRANCH'] = "non-master"
    assert bitbucket("non-master") == True
    os.environ['BITBUCKET_BUILD_NUMBER'] = "15"
    os.environ['BITBUCKET_BRANCH'] = "master"
    os.environ['BITBUCKET_PR_ID'] = "13"
    assert bitbucket("master") == True

# Generated at 2022-06-14 04:47:12.682416
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")

# Generated at 2022-06-14 04:47:15.689147
# Unit test for function checker
def test_checker():
    @checker
    def func():
        assert True == False

    try:
        func()
    except CiVerificationError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:47:26.584879
# Unit test for function checker
def test_checker():
    def test():
        assert 1 == 2

    def test2():
        assert 1 == 1

    try:
        test()
    except CiVerificationError:
        raise AssertionError("checker wasn't working")
    try:
        test2()
    except CiVerificationError:
        raise AssertionError("checker wasn't working")

# Generated at 2022-06-14 04:47:29.942676
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check()
    del os.environ["CI_COMMIT_REF_NAME"]
    os.environ["CI_COMMIT_REF_NAME"] = "not-master"
    try:
        check()
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:47:40.858376
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = True
    os.environ["BITBUCKET_BRANCH"] = "master"
    assert bitbucket("master") == True
    os.environ["BITBUCKET_PR_ID"] = True
    assert bitbucket("master") == False
    del os.environ["BITBUCKET_PR_ID"]
    os.environ["BITBUCKET_BRANCH"] = "not_master"
    assert bitbucket("master") == False
    del os.environ["BITBUCKET_BUILD_NUMBER"]
    del os.environ["BITBUCKET_BRANCH"]


# Generated at 2022-06-14 04:47:41.839546
# Unit test for function bitbucket
def test_bitbucket():
    assert bitbucket == None

# Generated at 2022-06-14 04:47:51.913259
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    os.environ["TRAVIS"] = "true"
    check("master")
    os.environ["TRAVIS_BRANCH"] = "master_branch"
    with pytest.raises(CiVerificationError):
        check("master")
    os.environ["CI_PULL_REQUEST"] = "true"
    with pytest.raises(CiVerificationError):
        check("master")



# Generated at 2022-06-14 04:47:53.037490
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = "master"
    os.environ['TRAVIS_PULL_REQUEST'] = "false"
    travis("master")


# Generated at 2022-06-14 04:47:56.603154
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check("master")
    os.environ["CI_COMMIT_REF_NAME"] = "develop"
    check("master")

# Generated at 2022-06-14 04:48:06.137734
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")

    os.environ["TRAVIS_BRANCH"] = "test"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    try:
        travis("master")
    except CiVerificationError:
        pass

    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        travis("master")
    except CiVerificationError:
        pass


# Generated at 2022-06-14 04:48:15.853260
# Unit test for function jenkins
def test_jenkins():
    d = {
    "BRANCH_NAME": "master",
    "JENKINS_URL": "https://github.com/sallen450/semantic_release",
    "TEST1": "2",
    "CHANGE_ID": "12345"
    }
    os.environ.update(d)
    assert jenkins("master") == True

    d = {
    "BRANCH_NAME": "develop",
    "GIT_BRANCH": "master",
    "JENKINS_URL": "https://github.com/sallen450/semantic_release",
    "TEST1": "2",
    "CHANGE_ID": "12345"
    }
    os.environ.update(d)
    assert jenkins("master") == False

# Generated at 2022-06-14 04:48:20.516347
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master")


# Generated at 2022-06-14 04:48:33.095734
# Unit test for function bitbucket
def test_bitbucket():
    """
    This is a test to check if the bitbucket function works as expected.

    The operating system variable BITBUCKET_BUILD_NUMBER is defined an
    empty value.

    We want our function to check that this is not true.

    """
    os.environ["BITBUCKET_BUILD_NUMBER"] = ""
    with pytest.raises(CiVerificationError):
        bitbucket("master")




# Generated at 2022-06-14 04:48:44.096791
# Unit test for function checker
def test_checker():
    from unittest.mock import patch
    import pytest

    # Wrong branch name should raise exception
    with pytest.raises(CiVerificationError):
        travis("wrong_branch")

    # Checking that the environment variable TRAVIS_PULL_REQUEST is false
    with patch.dict(os.environ, {"TRAVIS_PULL_REQUEST": "true"}):
        with pytest.raises(CiVerificationError):
            travis("master")

    # Checking that the environment variable TRAVIS_BRANCH is wrong
    with patch.dict(os.environ, {"TRAVIS_BRANCH": "wrong_branch"}):
        with pytest.raises(CiVerificationError):
            travis("master")

# Generated at 2022-06-14 04:48:56.022255
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master")

    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "123"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    try:
        semaphore("master")
        assert False
    except CiVerificationError:
        assert True

    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None

# Generated at 2022-06-14 04:49:02.196434
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")
    os.environ["TRAVIS_PULL_REQUEST"] = "5"
    try:
        travis("master")
    except CiVerificationError:
        pass
    else:
        assert False
    os.environ["TRAVIS_BRANCH"] = "develop"
    try:
        travis("master")
    except CiVerificationError:
        pass
    else:
        assert False



# Generated at 2022-06-14 04:49:07.567468
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    # Checking with a change in the environment variables
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        check()  # When the check fails
    except CiVerificationError:
        os.environ["TRAVIS_BRANCH"] = "master"
        os.environ["TRAVIS_PULL_REQUEST"] = "false"


# Generated at 2022-06-14 04:49:18.762201
# Unit test for function gitlab
def test_gitlab():
    os.environ['GITLAB_CI'] = 'true'
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    os.environ['CI_MERGE_REQUEST_ID'] = '123'
    try:
        gitlab('master')
    except CiVerificationError:
        pass

    os.environ['CI_MERGE_REQUEST_ID'] = None
    gitlab('master')

    try:
        os.environ['CI_COMMIT_REF_NAME'] = 'different'
        gitlab('master')
    except CiVerificationError:
        os.environ['CI_COMMIT_REF_NAME'] = 'master'
        pass

    del os.environ['CI_COMMIT_REF_NAME']

# Generated at 2022-06-14 04:49:28.762122
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "foo"
    try:
        travis("foo")
    except:
        print('Travis Failed')
        assert True is False
    os.environ["TRAVIS_BRANCH"] = "foo"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        travis("foo")
    except:
        assert True is False
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS_BRANCH"] = "foo"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"

# Generated at 2022-06-14 04:49:38.846049
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master")

    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        assert travis("master")
    except CiVerificationError:
        assert True
    else:
        assert False

    os.environ["TRAVIS_BRANCH"] = "test"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    try:
        assert travis("master")
    except CiVerificationError:
        assert True
    else:
        assert False



# Generated at 2022-06-14 04:49:43.106729
# Unit test for function bitbucket
def test_bitbucket():
    """
    Unit test for function bitbucket
    """
    os.environ["BITBUCKET_BRANCH"] = "release"
    os.environ["BITBUCKET_PR_ID"] = "1234"
    check(branch="release")

# Generated at 2022-06-14 04:49:48.450750
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    assert circle("master") is True
    os.environ["CIRCLE_BRANCH"] = "other_branch"
    assert circle("master") is False
    os.environ["CIRCLE_BRANCH"] = "other_branch"
    os.environ["CI_PULL_REQUEST"] = "bla"
    assert circle("master") is False


# Generated at 2022-06-14 04:50:01.681275
# Unit test for function bitbucket
def test_bitbucket():
    assert callable(bitbucket) == True

# Generated at 2022-06-14 04:50:10.337693
# Unit test for function bitbucket
def test_bitbucket():
    """
    Test function bitbucket
    :return:
    """
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("master")
    os.environ["BITBUCKET_BRANCH"] = "nonmaster"
    os.environ.pop("BITBUCKET_PR_ID")
    try:
        bitbucket("master")
        assert False
    except CiVerificationError:
        assert True


# Generated at 2022-06-14 04:50:14.748685
# Unit test for function gitlab
def test_gitlab():
    import os
    os.environ['CI_COMMIT_REF_NAME'] = "master"
    assert gitlab() == True
    os.environ['CI_COMMIT_REF_NAME'] = "develop"
    assert gitlab() == False
    os.environ['CI_COMMIT_REF_NAME'] = "production"
    assert gitlab() == False

# Generated at 2022-06-14 04:50:19.436376
# Unit test for function bitbucket
def test_bitbucket():
    from semantic_release import ci_checks
    #set env vars
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "some_branch"
    assert ci_checks.bitbucket("master") is True

# Generated at 2022-06-14 04:50:25.673588
# Unit test for function jenkins
def test_jenkins():
    """
    Test the jenkins function
    """
    # Success
    os.environ['JENKINS_URL'] = "true"
    os.environ['BRANCH_NAME'] = "master"
    jenkins("master")

    # Fail
    os.environ['BRANCH_NAME'] = "develop"
    os.environ['CHANGE_ID'] = "true"
    expected_msg = "The verification check for the environment did not pass."
    try:
        jenkins("master")
    except Exception as exc:
        assert str(exc) == expected_msg

# Generated at 2022-06-14 04:50:28.490656
# Unit test for function gitlab
def test_gitlab():
    """
    Performs necessary checks to ensure that the gitlab build is one
    that should create releases.

    :param branch: The branch the environment should be running against.
    """
    assert os.environ.get("CI_COMMIT_REF_NAME") == "master"
    # TODO - don't think there's a merge request indicator variable

# Generated at 2022-06-14 04:50:29.618316
# Unit test for function frigg
def test_frigg():
    assert frigg("master") == True

# Generated at 2022-06-14 04:50:33.741023
# Unit test for function checker
def test_checker():
    def func():
        raise AssertionError
    assert checker(func)() == True

    def func2():
        pass
    assert checker(func2)() == True


# Unit tests for travis

# Generated at 2022-06-14 04:50:40.795107
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "true"
    os.environ["CIRCLE_BRANCH"] = "fix/test"

    try:
        circle("fix/test")
    except CiVerificationError:
        pass
    else:
        raise AssertionError("CiVerificationError should be raised")

    os.environ["CI_PULL_REQUEST"] = "false"
    circle("fix/test")



# Generated at 2022-06-14 04:50:51.945996
# Unit test for function travis
def test_travis():
    os.environ.update(TRAVIS="true",TRAVIS_BRANCH="master",TRAVIS_PULL_REQUEST="false")
    assert travis("master") is True
    os.environ.update(TRAVIS="true",TRAVIS_BRANCH="master",TRAVIS_PULL_REQUEST="")
    assert travis("master") is True
    os.environ.update(TRAVIS="true",TRAVIS_BRANCH="master",TRAVIS_PULL_REQUEST="false")
    assert travis("stable") is False
    os.environ.update(TRAVIS="true",TRAVIS_BRANCH="master",TRAVIS_PULL_REQUEST="")
    assert travis("stable") is False

# Generated at 2022-06-14 04:51:27.020298
# Unit test for function semaphore
def test_semaphore():
    # Success case
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    check()

    # Branch error case
    os.environ["BRANCH_NAME"] = "develop"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    try:
        check()
        assert 0
    except CiVerificationError:
        pass

    # PR error case
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "10"
    os

# Generated at 2022-06-14 04:51:30.920775
# Unit test for function checker
def test_checker():
    @checker
    def test_function_true():
        assert True

    def test_function_false():
        assert False

    assert test_function_true() == True
    assert test_function_false() == False

# Unit test function check

# Generated at 2022-06-14 04:51:31.564657
# Unit test for function jenkins
def test_jenkins():
    assert jenkins("master") is True

# Generated at 2022-06-14 04:51:35.827369
# Unit test for function travis
def test_travis():
    # Set of environment variables to test
    environment = {
        "TRAVIS_BRANCH": "master",
        "TRAVIS_PULL_REQUEST": "false",
    }

    for varname, varvalue in environment.items():
        os.environ["TRAVIS"] = "true"
        os.environ[varname] = varvalue
        assert check()



# Generated at 2022-06-14 04:51:39.226855
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")

# Generated at 2022-06-14 04:51:44.336756
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "not_master"
    check("master") # AssertionError

    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "test"
    check("master") # AssertionError

# Generated at 2022-06-14 04:51:47.530531
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")



# Generated at 2022-06-14 04:51:57.482760
# Unit test for function checker
def test_checker():
    from semantic_release.errors import CiVerificationError

    try:
        @checker
        def func():
            assert False
        func()
    except CiVerificationError:
        pass
    else:
        raise Exception("Should have thrown")

    @checker
    def func2():
        assert True
    func2()

    try:
        def func3():
            assert False
        func3 = checker(func3)
        func3()
    except CiVerificationError:
        pass
    else:
        raise Exception("Should have thrown")

    def func4():
        assert True
    func4 = checker(func4)
    func4()

# Generated at 2022-06-14 04:52:01.299956
# Unit test for function jenkins
def test_jenkins():
    os.environ['BRANCH_NAME'] = "master"
    os.environ['JENKINS_URL'] = "https://jenkins.test/"
    os.environ['CHANGE_ID'] = "test"
    assert check("master")

# Generated at 2022-06-14 04:52:03.424570
# Unit test for function travis
def test_travis():
    assert travis(branch='master') is True


# Generated at 2022-06-14 04:52:54.772055
# Unit test for function jenkins
def test_jenkins():
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['GIT_BRANCH'] = 'master'
    os.environ['JENKINS_URL'] = 'https://ec2-54-169-46-22.ap-southeast-1.compute.amazonaws.com/'
    os.environ['CHANGE_ID'] = '1234'
    assert check()

# Generated at 2022-06-14 04:52:57.066721
# Unit test for function gitlab
def test_gitlab():
    try:
        gitlab("master")
        assert False
    except CiVerificationError:
        assert True

# Generated at 2022-06-14 04:53:02.211817
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "develop"
    os.environ["CI_PULL_REQUEST"] = "false"
    assert circle("develop")
    assert not circle("master")



# Generated at 2022-06-14 04:53:06.903928
# Unit test for function semaphore
def test_semaphore():
    envvar = os.environ
    envvar["BRANCH_NAME"] = "master"
    envvar["PULL_REQUEST_NUMBER"] = None
    envvar["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")

# Generated at 2022-06-14 04:53:09.908914
# Unit test for function checker
def test_checker():
    @checker
    def func():
        assert False
    try:
        func()
    except CiVerificationError:
        pass
    else:
        raise AssertionError('Expected CiVerificationError')

# Generated at 2022-06-14 04:53:17.628441
# Unit test for function check
def test_check():
    env = {
        "TRAVIS": "true", "TRAVIS_BRANCH": "master",
        "TRAVIS_PULL_REQUEST": "true",
    }
    assert not check(env=env)

    env = {
        "TRAVIS": "true", "TRAVIS_BRANCH": "master",
        "TRAVIS_PULL_REQUEST": "false",
    }
    assert check(env=env)

    env = {
        "SEMAPHORE": "true", "BRANCH_NAME": "master",
        "PULL_REQUEST_NUMBER": "1", "SEMAPHORE_THREAD_RESULT": "success",
    }
    assert not check(env=env)


# Generated at 2022-06-14 04:53:30.009317
# Unit test for function bitbucket
def test_bitbucket():
    """
    Unit test for function bitbucket
    """
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_PR_ID"] = ""
    try:
        bitbucket("master")
        os.environ["BITBUCKET_BRANCH"] = "other"
        bitbucket("master")
    except Exception as exception:
        assert type(exception) == CiVerificationError
        assert str(exception) == "The verification check for the environment did not pass."
        return
    assert False

# Generated at 2022-06-14 04:53:40.943074
# Unit test for function jenkins
def test_jenkins():
    """
    Unit test to check jenkins function
    """
    # Merge Request
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['GIT_BRANCH'] = 'master'
    os.environ['JENKINS_URL'] = 'jenkins'
    os.environ['CHANGE_ID'] = '1'
    try:
        jenkins('master')
    except Exception as e:
        if not isinstance(e, CiVerificationError):
            raise Exception("test_jenkins fails")

    # No Merge Request
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['GIT_BRANCH'] = 'master'
    os.environ['JENKINS_URL'] = 'jenkins'
    os.en

# Generated at 2022-06-14 04:53:48.571900
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check(branch="master")
    assert True
    os.environ["TRAVIS_BRANCH"] = "test"
    try:
        check(branch="master")
        assert False
    except CiVerificationError:
        assert True

    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ["PULL_REQUEST_NUMBER"] = None
    check(branch="master")


# Generated at 2022-06-14 04:53:55.612648
# Unit test for function bitbucket
def test_bitbucket():
    # Test 1
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "1"

    try:
        bitbucket("master")
        assert False
    except CiVerificationError:
        assert True

    # Test 2
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "0"

    try:
        bitbucket("master")
    except CiVerificationError:
        assert False
