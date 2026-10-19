

# Generated at 2022-06-14 04:45:16.771883
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ.pop("CI_MERGE_REQUEST_IID", None)
    try:
        gitlab("master")
    except CiVerificationError:
        assert False
    os.environ.pop("CI_COMMIT_REF_NAME", None)
    os.environ["CI_MERGE_REQUEST_IID"] = "1"
    try:
        gitlab("master")
        assert False
    except CiVerificationError:
        assert True


# Generated at 2022-06-14 04:45:17.677596
# Unit test for function frigg
def test_frigg():
    assert frigg("master") is True


# Generated at 2022-06-14 04:45:30.046741
# Unit test for function travis
def test_travis():
    # Travis run from master branch
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master") is True

    # Travis run from develop branch
    os.environ["TRAVIS_BRANCH"] = "develop"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("develop") is True

    # Travis run from a pull request
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    assert travis("master") is False

    # Travis run from a different branch

# Generated at 2022-06-14 04:45:34.514474
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "http://jenkins"
    os.environ["BRANCH_NAME"] = "master"
    check()
    del os.environ["JENKINS_URL"]
    del os.environ['BRANCH_NAME']

# Generated at 2022-06-14 04:45:35.381273
# Unit test for function travis
def test_travis():
    check()

# Generated at 2022-06-14 04:45:47.187123
# Unit test for function check
def test_check():
    os.environ['TRAVIS'] = 'true'
    os.environ['SEMAPHORE'] = 'true'
    os.environ['FRIGG'] = 'true'
    os.environ['CIRCLECI'] = 'true'
    os.environ['GITLAB_CI'] = 'true'
    os.environ['JENKINS_URL'] = 'some_url'
    os.environ['BITBUCKET_BUILD_NUMBER'] = 'some_num'
    check()
    assert os.environ['TRAVIS'] is not 'false'
    assert os.environ['SEMAPHORE'] is not 'false'
    assert os.environ['FRIGG'] is not 'false'
    assert os.environ['CIRCLECI'] is not 'false'

# Generated at 2022-06-14 04:45:49.859656
# Unit test for function gitlab
def test_gitlab():
    os.environ['CI_COMMIT_REF_NAME'] = "master"
    assert gitlab("master") == True



# Generated at 2022-06-14 04:45:54.874697
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "1"
    os.environ["CIRCLE_BRANCH"] = "dev"
    try:
        circle(branch="master")
    except CiVerificationError:
        assert True
    else:
        assert False



# Generated at 2022-06-14 04:46:03.799999
# Unit test for function jenkins
def test_jenkins():
    """
    Unit test for function jenkins
    """
    os.environ["JENKINS_URL"] = "some-jenkins-url"
    os.environ["BRANCH_NAME"] = "branch1"
    jenkins(branch="branch1")
    os.environ["BRANCH_NAME"] = "branch2"
    jenkins(branch="branch2")
    os.environ["GIT_BRANCH"] = "branch3"
    jenkins(branch="branch3")
    os.environ.pop("BRANCH_NAME")
    try:
        jenkins(branch="branch4")
        assert False
    except AssertionError:
        assert True

# Generated at 2022-06-14 04:46:04.554710
# Unit test for function check

# Generated at 2022-06-14 04:46:14.060371
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master") is True



# Generated at 2022-06-14 04:46:25.783885
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    os.environ["PULL_REQUEST_NUMBER"] = None

    semaphore("master")
    assert True

    with pytest.raises(CiVerificationError, match=r".*verification.*"):
        os.environ["BRANCH_NAME"] = "develop"
        semaphore("master")

    with pytest.raises(CiVerificationError, match=r".*verification.*"):
        os.environ["BRANCH_NAME"] = "master"
        os.environ["PULL_REQUEST_NUMBER"] = "1"
        sem

# Generated at 2022-06-14 04:46:30.204605
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master")
    del os.environ["TRAVIS_BRANCH"]
    del os.environ["TRAVIS_PULL_REQUEST"]


# Generated at 2022-06-14 04:46:35.552931
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://github.com/relekang/pytest-semantic-release"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = ""
    jenkins("master")
    assert True

# Generated at 2022-06-14 04:46:40.560841
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "test"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "22"
    check("master")

# Generated at 2022-06-14 04:46:48.238051
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = 'master'
    assert bitbucket('master')
    os.environ['BITBUCKET_BRANCH'] = 'develop'
    assert not bitbucket('master')
    os.environ['BITBUCKET_BRANCH'] = 'master'
    os.environ['BITBUCKET_PR_ID'] = '123'
    assert not bitbucket('master')

# Generated at 2022-06-14 04:46:51.140814
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")



# Generated at 2022-06-14 04:46:56.340494
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = None
    bitbucket("master")
    # TODO: check for ci verification error



# Generated at 2022-06-14 04:47:01.789746
# Unit test for function checker
def test_checker():
    """
    Test if the checker function matches exception
    """
    def test_function():
        """
        Test if the checker function matches exception
        """
        raise AssertionError

    checker_wrapper = checker(test_function)
    try:
        checker_wrapper()
    except CiVerificationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:47:07.868773
# Unit test for function semaphore
def test_semaphore():
    """
    Unit test for function semaphore
    """
    try:
        assert os.environ.get("BRANCH_NAME") == 'master'
        assert os.environ.get("PULL_REQUEST_NUMBER") is None
        assert os.environ.get("SEMAPHORE_THREAD_RESULT") != "failed"
    except AssertionError:
        raise CiVerificationError(
            "The verification check for the environment did not pass."
        )


# Generated at 2022-06-14 04:47:18.719745
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://jenkins.test.com/"
    os.environ["GIT_BRANCH"] = "test_branch"
    os.environ["CHANGE_ID"] = "1"
    
    check("test_branch")

# Generated at 2022-06-14 04:47:25.744371
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'https://jenkins.com'
    os.environ['BRANCH_NAME'] = 'master'
    jenkins('master')

if __name__ == "__main__":
    check(branch="master")

# Generated at 2022-06-14 04:47:30.008247
# Unit test for function bitbucket
def test_bitbucket():
    """
      Method to unit test the function to check GitLab environment
    """

    # Set up the environment variables
    os.environ["BITBUCKET_BUILD_NUMBER"] = "BITBUCKET_BUILD_NUMBER"
    os.environ["BITBUCKET_BRANCH"] = "BITBUCKET_BRANCH"

    check()

    # Make sure that the function passed by returning nothing
    assert True



# Generated at 2022-06-14 04:47:41.751256
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "true"
    os.environ["BRANCH_NAME"] = "devel"
    os.environ["CHANGE_ID"] = ""
    check()

    os.environ["BRANCH_NAME"] = "devel"
    os.environ["CHANGE_ID"] = "123"
    try:
        check()
        assert False
    except AssertionError:
        pass

    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = ""
    try:
        check()
        assert False
    except AssertionError:
        pass
        
    os.environ["JENKINS_URL"] = "dev"

# Generated at 2022-06-14 04:47:51.871199
# Unit test for function gitlab
def test_gitlab():
    """ Assert function gitlab will raise `CiVerificationError`
        if GITLAB_CI is true but CI_COMMIT_REF_NAME is not equal to "master"
    """
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"

    check()

    os.environ["CI_COMMIT_REF_NAME"] = "develop"

    try:
        check()
        assert False, "Should raise `CiVerificationError`."
    except CiVerificationError:
        assert True



# Generated at 2022-06-14 04:47:58.694233
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    assert bitbucket("master") is True
    os.environ["BITBUCKET_BRANCH"] = "3.0.2"
    os.environ["BITBUCKET_PR_ID"] = "3"
    assert bitbucket("master") is False
    assert bitbucket("3.0.2") is False
    del os.environ["BITBUCKET_PR_ID"]
    assert bitbucket("3.0.2") is True



# Generated at 2022-06-14 04:48:02.377040
# Unit test for function circle
def test_circle():

    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    circle("master")

# Generated at 2022-06-14 04:48:05.255778
# Unit test for function circle
def test_circle():
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = None
    check()



# Generated at 2022-06-14 04:48:14.615786
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    circle("master")
    os.environ["CIRCLE_BRANCH"] = "test"
    circle("test")
    os.environ["CI_PULL_REQUEST"] = "1"
    circle("master")
    os.environ["CI_PULL_REQUEST"] = "0"
    circle("master")
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CI_PULL_REQUEST"]
    del os.environ["CIRCLECI"]



# Generated at 2022-06-14 04:48:18.034665
# Unit test for function gitlab
def test_gitlab():
    """
    Test function gitlab
    """
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    gitlab("master")


# Generated at 2022-06-14 04:48:27.903707
# Unit test for function bitbucket
def test_bitbucket():
    if os.environ.get("BITBUCKET_BRANCH") == "master":
        assert bitbucket("master") == True
    else:
        assert bitbucket("master") == False

# Generated at 2022-06-14 04:48:32.939056
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")

# Generated at 2022-06-14 04:48:41.237518
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = "true"
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    check()
    os.environ['FRIGG_BUILD_BRANCH'] = 'other'
    os.environ['FRIGG_PULL_REQUEST'] = 'some-value'
    try:
        check()
        assert False, 'Should not be able to release from other branch.'
    except CiVerificationError:
        pass


# Generated at 2022-06-14 04:48:49.783474
# Unit test for function check
def test_check():

    # Initialize environment variables for testing
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS_BRANCH"] = "master"

    # Run function check
    try:
        check()
    except CiVerificationError:
        assert False

    # Change environment variables to trigger errors
    os.environ["TRAVIS_BRANCH"] = "feature"
    try:
        check()
        assert False
    except CiVerificationError:
        assert True

    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        check()
        assert False
    except CiVerificationError:
        assert True

# Unit tests for functions travis and semaphore

# Generated at 2022-06-14 04:48:58.027887
# Unit test for function checker
def test_checker():
    # Decorator works as expected
    try:
        @checker
        def test():
            assert False
        test()
    except CiVerificationError:
        pass
    else:
        raise AssertionError("Expected test decorated with checker to raise CiVerificationError")

    # Decorator wraps other exceptions
    try:
        @checker
        def test():
            raise ValueError('Value Error')
        test()
    except ValueError:
        pass
    else:
        raise AssertionError("Expected test decorated with checker to raise ValueError")

# Generated at 2022-06-14 04:49:04.781344
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = ""
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore(branch="master")

# Generated at 2022-06-14 04:49:07.817992
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = 'true'
    os.environ["CI_COMMIT_REF_NAME"] = 'master'
    gitlab('master')

# Generated at 2022-06-14 04:49:15.544201
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["JENKINS_URL"] = "https://jenkins.test.test"
    check('master')
    del os.environ['BRANCH_NAME']
    del os.environ['GIT_BRANCH']
    del os.environ['JENKINS_URL']

# Generated at 2022-06-14 04:49:17.621090
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    circle("master")

# Generated at 2022-06-14 04:49:22.510337
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"

    assert semaphore("asdf") is False

# Generated at 2022-06-14 04:49:34.576184
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    assert circle("master") is True

    os.environ["CIRCLE_BRANCH"] = "develop"
    assert circle("master") is False

    del os.environ["CIRCLE_BRANCH"]



# Generated at 2022-06-14 04:49:38.069080
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "develop"
    check("develop")
    del os.environ["GITLAB_CI"]
    del os.environ["CI_COMMIT_REF_NAME"]

# Generated at 2022-06-14 04:49:43.424368
# Unit test for function semaphore
def test_semaphore():
    # Arrange
    os.environ["BRANCH_NAME"] = "feature/branch"
    os.environ["PULL_REQUEST_NUMBER"] = "123"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "succeeded"

    # Act
    semaphore(branch="master")

    # Assert
    assert True

# Generated at 2022-06-14 04:49:45.778021
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    frigg(branch='master')


# Generated at 2022-06-14 04:49:52.038436
# Unit test for function jenkins
def test_jenkins():
    os.environ['GIT_BRANCH'] = 'master'
    os.environ['JENKINS_URL'] = 'true'
    os.environ['CHANGE_ID'] = 'true'

    try:
        jenkins('master')
    except Exception as e:
        print(e)
        assert type(e) == CiVerificationError

# Generated at 2022-06-14 04:49:57.843289
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")
    assert os.environ["TRAVIS_BRANCH"] == "master"
    assert os.environ["TRAVIS_PULL_REQUEST"] == "false"


# Generated at 2022-06-14 04:50:00.166709
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    bitbucket("master")
#test_bitbucket()

# Generated at 2022-06-14 04:50:08.907403
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    assert semaphore("master")
    del os.environ["BRANCH_NAME"]
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["SEMAPHORE_THREAD_RESULT"]
    assert not semaphore("master")


# Generated at 2022-06-14 04:50:16.608538
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = "true"

    os.environ['FRIGG_BUILD_BRANCH'] = "master"
    frigg('master')
    del os.environ['FRIGG_BUILD_BRANCH']

    os.environ['FRIGG_PULL_REQUEST'] = "true"
    try:
        frigg('master')
    except CiVerificationError as e:
        print (e)
    del os.environ['FRIGG_PULL_REQUEST']

    del os.environ['FRIGG']


# Generated at 2022-06-14 04:50:22.726203
# Unit test for function semaphore
def test_semaphore():
    """
    Test the checker semaphore in the branch master and branch develop
    """
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "successful"
    semaphore("master")
    os.environ["BRANCH_NAME"] = "develop"
    semaphore("develop")

# Generated at 2022-06-14 04:50:35.400780
# Unit test for function semaphore
def test_semaphore():
    env = {
        "BRANCH_NAME": "master",
        "PULL_REQUEST_NUMBER": None,
        "SEMAPHORE_THREAD_RESULT": "passed"
    }

    os.environ = env
    ci = "semaphore"
    branch = "master"
    check(ci, branch)

# Generated at 2022-06-14 04:50:37.216463
# Unit test for function check
def test_check():
    try:
        check()
    except CiVerificationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:50:41.042208
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'
    os.environ['FRIGG_PULL_REQUEST'] = 'N'

    check()


# Generated at 2022-06-14 04:50:41.974705
# Unit test for function semaphore
def test_semaphore():
    # TODO - write test
    pass

# Generated at 2022-06-14 04:50:49.924739
# Unit test for function check
def test_check():
    import pytest
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    assert os.environ.get("TRAVIS_BRANCH") == "master"

    os.environ["TRAVIS_BRANCH"] = "feature"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    with pytest.raises(CiVerificationError):
        check()

    os.environ["TRAVIS"] = "false"
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"

# Generated at 2022-06-14 04:50:51.520306
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    semaphore(branch="master")

# Generated at 2022-06-14 04:50:56.443094
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = "true"
    os.environ['CIRCLE_BRANCH'] = "master"
    assert(circle(branch='master') == True)
    os.environ['CIRCLE_BRANCH'] = "issue#1"
    assert(circle(branch='master') == False)
    del os.environ['CIRCLECI']
    del os.environ['CIRCLE_BRANCH']

# Generated at 2022-06-14 04:51:00.959284
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("master")
    del os.environ["BITBUCKET_PR_ID"]
    bitbucket("master")



# Generated at 2022-06-14 04:51:13.053009
# Unit test for function semaphore
def test_semaphore():
    os.environ['SEMAPHORE'] = 'true'
    os.environ['PULL_REQUEST_NUMBER'] = '1'
    os.environ['BRANCH_NAME'] = 'develop'
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'failed'
    try:
        check()
    except CiVerificationError:
        pass
    else:
        assert False, "CiVerificationError should have been raised"
    
    os.environ['SEMAPHORE'] = 'true'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'success'

# Generated at 2022-06-14 04:51:14.494343
# Unit test for function gitlab
def test_gitlab():
    assert gitlab(branch='master')
    assert gitlab(branch='feature-branch')

# Generated at 2022-06-14 04:51:22.867500
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "branch1"
    check(branch="branch1")


# Generated at 2022-06-14 04:51:31.782300
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = 'None'
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    os.environ['SEMAPHORE'] = 'true'

    assert semaphore('master') == True

    os.environ['SEMAPHORE_THREAD_RESULT'] = 'failed'

    try:
        semaphore('master')
    except CiVerificationError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:51:35.973531
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "false"
    os.environ["CIRCLE_BRANCH"] = "master"
    try:
        circle('master')
    except CiVerificationError as e:
        msg = "The verification check for the environment did not pass."
        assert str(e) == msg



# Generated at 2022-06-14 04:51:45.043595
# Unit test for function frigg
def test_frigg():
    """
    Ensure the frigg function correctly validates the frigg environment.
    """
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg("master")
    os.environ["FRIGG_PULL_REQUEST"] = "42"
    os.environ["FRIGG_BUILD_BRANCH"] = "development"
    try:
        frigg("master")
    except CiVerificationError:
        pass
    else:
        assert False, "should raise exception"



# Generated at 2022-06-14 04:51:50.148392
# Unit test for function checker
def test_checker():
    @checker
    def test_func(x):
        assert x > 0

    try:
        test_func(0)
    except CiVerificationError:
        # We should get here
        return
    assert False, "Did not raise CiVerificationError"

# Generated at 2022-06-14 04:51:51.746484
# Unit test for function semaphore
def test_semaphore():
    semaphore(branch="master")

# Generated at 2022-06-14 04:51:55.690666
# Unit test for function gitlab
def test_gitlab():
    # arrange
    branch = "master"
    os.environ["CI_COMMIT_REF_NAME"] = branch
    os.environ["CI_MERGE_REQUEST_IID"] = "123"
    # act
    check(branch)

# Generated at 2022-06-14 04:52:03.980224
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        check()
    except CiVerificationError as e:
        if "The verification check for the environment did not pass." in str(e):
            print("Caught expected CiVerificationError")
        else:
            print("Unexpected CiVerificationError")

    os.environ["TRAVIS"] = "true"

# Generated at 2022-06-14 04:52:14.689194
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "false"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    try:
        semaphore("master")
        assert False
    except CiVerificationError:
        assert True
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ["PULL_REQUEST_NUMBER"] = "5"
    try:
        semaphore("master")
        assert False
    except CiVerificationError:
        assert True

# Generated at 2022-06-14 04:52:17.087864
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "12345"
    check()

# Generated at 2022-06-14 04:52:30.013313
# Unit test for function travis
def test_travis():
    assert travis("master") == True


# Generated at 2022-06-14 04:52:35.915507
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = 'master'
    os.environ['BITBUCKET_PR_ID'] = '56'
    try:
        bitbucket('master')
    except CiVerificationError:
        pass
    del os.environ['BITBUCKET_BRANCH']
    del os.environ['BITBUCKET_PR_ID']

# Generated at 2022-06-14 04:52:38.594277
# Unit test for function travis
def test_travis():
    with pytest.raises(CiVerificationError):
        travis(branch)


# Generated at 2022-06-14 04:52:41.841082
# Unit test for function semaphore
def test_semaphore():
    assert semaphore("master")
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    try:
        semaphore("master")
    except CiVerificationError:
        assert True

# Generated at 2022-06-14 04:52:42.777916
# Unit test for function semaphore
def test_semaphore():
    assert semaphore("master")


# Generated at 2022-06-14 04:52:55.479331
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg("master")

    with pytest.raises(CiVerificationError) as excinfo:
        frigg("develop")
    assert "The verification check for the environment did not pass." == excinfo.value.args[0]
    os.environ.pop("FRIGG", None)
    os.environ["FRIGG_PULL_REQUEST"] = True
    with pytest.raises(CiVerificationError) as excinfo:
        frigg("master")
    assert "The verification check for the environment did not pass." == excinfo.value.args[0]
    os.environ.pop("FRIGG_PULL_REQUEST", None)


# Generated at 2022-06-14 04:52:59.512925
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg(branch="master")



# Generated at 2022-06-14 04:53:05.969979
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_IID"] = None
    
    check("master")
    try:
        check("develop")
    except CiVerificationError:
        pass
    else:
        assert False


# Generated at 2022-06-14 04:53:11.401671
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"

    check()
    try:
        os.environ["CIRCLE_BRANCH"] = "not master"
        check()
    except CiVerificationError:
        pass



# Generated at 2022-06-14 04:53:16.879217
# Unit test for function gitlab
def test_gitlab():
    try:
        os.environ["CI_COMMIT_REF_NAME"] = "master"
        gitlab("master")
    except Exception:
        assert False
    try:
        os.environ["CI_COMMIT_REF_NAME"] = "dev"
        gitlab("master")
        assert False
    except Exception:
        assert True

# Generated at 2022-06-14 04:53:51.891728
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["JENKINS_URL"] = "123"
    os.environ["CHANGE_ID"] = "1"
    try:
        jenkins(branch="master")
        assert False
    except CiVerificationError:
        pass
    os.environ["CHANGE_ID"] = ""
    try:
        jenkins(branch="master")
    except CiVerificationError:
        assert False

# Generated at 2022-06-14 04:53:54.747335
# Unit test for function checker
def test_checker():
    @checker
    def assert_check(branch):
        assert branch == "master"
        raise AssertionError("Test error")

    with pytest.raises(CiVerificationError):
        assert_check("master")

# Generated at 2022-06-14 04:54:00.721564
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = 'master'
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert semaphore('master') is True


# Generated at 2022-06-14 04:54:03.663252
# Unit test for function jenkins
def test_jenkins():
    os.environ = {"GIT_BRANCH": "master"}
    os.environ["JENKINS_URL"] = "true"

    assert jenkins(branch="master")

# Generated at 2022-06-14 04:54:07.607726
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"]='true'
    os.environ["BRANCH_NAME"]='master'
    os.environ["GIT_BRANCH"]='master'
    os.environ["CHANGE_ID"]=''
    check()

# Generated at 2022-06-14 04:54:12.926010
# Unit test for function checker
def test_checker():
    def func():
        assert 0 == 1
    
    func_wrapper = checker(func)
    try:
        func_wrapper()
    except CiVerificationError:
        assert True
    else:
        assert False, "CiVerificationError was not raised"

# Generated at 2022-06-14 04:54:14.010429
# Unit test for function semaphore
def test_semaphore():
    checker(semaphore)



# Generated at 2022-06-14 04:54:16.693839
# Unit test for function jenkins
def test_jenkins():
  assert os.environ.get("JENKINS_URL") is None or os.environ.get("JENKINS_URL") is not None

# Generated at 2022-06-14 04:54:26.427522
# Unit test for function bitbucket
def test_bitbucket():
    with os.popen('dd if=/dev/urandom of=./secret bs=1 count=20 status=none') as f:
        os.environ["BITBUCKET_BRANCH"] = f.readline()[:-1]
        os.environ["BITBUCKET_PR_ID"] = ""
        check()

    with os.popen('dd if=/dev/urandom of=./secret bs=1 count=20 status=none') as f:
        os.environ["BITBUCKET_BRANCH"] = ""
        os.environ["BITBUCKET_PR_ID"] = f.readline()[:-1]
        try:
            check()
        except CiVerificationError:
            return

    raise AssertionError

# Generated at 2022-06-14 04:54:35.729273
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master")
    os.environ["TRAVIS_BRANCH"] = "dev"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert not travis("master")
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    assert not travis("master")
