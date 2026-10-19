

# Generated at 2022-06-14 04:45:17.338728
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    assert bitbucket("master")
    del os.environ["BITBUCKET_BRANCH"]
    assert bitbucket("master") == False
    os.environ["BITBUCKET_BRANCH"] = "develop"
    assert bitbucket("master") == False
    os.environ["BITBUCKET_PR_ID"] = "1"
    assert bitbucket("master") == False
    del os.environ["BITBUCKET_PR_ID"]


# Generated at 2022-06-14 04:45:27.176372
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    assert travis('master')
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'true'
    assert not travis('master')
    os.environ['TRAVIS_BRANCH'] = 'develop'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    assert not travis('master')


# Generated at 2022-06-14 04:45:32.531905
# Unit test for function bitbucket
def test_bitbucket():
    try:
        os.environ["BITBUCKET_BRANCH"] = "master"
        os.environ["BITBUCKET_PR_ID"] = ""
        bitbucket("master")
    finally:
        del os.environ["BITBUCKET_BRANCH"]
        del os.environ["BITBUCKET_PR_ID"]

# Generated at 2022-06-14 04:45:44.096643
# Unit test for function semaphore
def test_semaphore():
    """
    Mock the environment variables on semaphore and assert that it works.
    """
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master")
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert not semaphore("master")
    os.environ["PULL_REQUEST_NUMBER"] = "1"
    assert not semaphore("master")
    os.environ["BRANCH_NAME"] = "develop"
    assert not semaphore("master")

# Generated at 2022-06-14 04:45:47.975362
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    assert gitlab("master") == True
    os.environ["CI_COMMIT_REF_NAME"] = "no-master"
    assert gitlab("master") == False


# Generated at 2022-06-14 04:45:56.992870
# Unit test for function travis
def test_travis():
    # Test for successful case
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    try:
        travis('master')
    except CiVerificationError as e:
        assert False
    # Test for unsuccessful case
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'true'
    try:
        travis('test')
    except CiVerificationError as e:
        return



# Generated at 2022-06-14 04:46:08.069309
# Unit test for function semaphore
def test_semaphore():
    # fail if thread is failed
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert semaphore("abc") is False
    # fail if branch is not correct
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ["BRANCH_NAME"] = "abc"
    assert semaphore("master") is False
    # pass if thread is passed
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = ""
    assert semaphore("master") is True
    # fail if pull request number is not null
    os.environ["PULL_REQUEST_NUMBER"]  = "123"
    assert semaphore("master") is False




# Generated at 2022-06-14 04:46:13.010228
# Unit test for function semaphore
def test_semaphore():
	os.environ["BRANCH_NAME"] = "master"
	os.environ["PULL_REQUEST_NUMBER"] = None
	os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
	semaphore(branch = "master")


# Generated at 2022-06-14 04:46:18.185385
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = 'master'
    os.environ["GIT_BRANCH"] = 'master'
    os.environ["JENKINS_URL"] = 'true'
    os.environ["CHANGE_ID"] = ''
    assert jenkins('master') == True


# Generated at 2022-06-14 04:46:21.380889
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")


# Generated at 2022-06-14 04:46:34.588043
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = ""

    # Check if tests fail
    try:
        frigg("my-branch")
    except CiVerificationError:
        pass
    assert True

    try:
        frigg("master")
    except CiVerificationError:
        assert False
    assert True



# Generated at 2022-06-14 04:46:40.459567
# Unit test for function semaphore
def test_semaphore():
    os.environ["PULL_REQUEST_NUMBER"] = "1"
    os.environ["BRANCH_NAME"] = "test"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    check()



# Generated at 2022-06-14 04:46:41.888349
# Unit test for function circle
def test_circle():
    circle(branch="test-branch")


# Generated at 2022-06-14 04:46:45.825761
# Unit test for function check
def test_check():
    try:
        check()
    except (AssertionError, CiVerificationError):
        pass
    # TODO - add more environments

# Generated at 2022-06-14 04:46:53.119913
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "succeeded"
    assert semaphore("master") == True
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert semaphore("master") == True
    os.environ["BRANCH_NAME"] = "test"
    assert semaphore("master") == True


# Generated at 2022-06-14 04:46:58.540681
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "release"
    os.environ["JENKINS_URL"] = "http://localhost:8080"
    assert check()
    os.environ["JENKINS_URL"] = ""
    assert check() is None


# Generated at 2022-06-14 04:47:08.233716
# Unit test for function check
def test_check():
    """Unit test for `semantic_release.ci_checks.check` function."""
    # Check that no error is raised when ``TRAVIS`` is set.
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()

    # Check that an error is raised when ``TRAVIS`` is set but the branch isn't master
    os.environ["TRAVIS_BRANCH"] = "develop"
    try:
        check()
    except CiVerificationError:
        pass

    # Check that no error is raised when ``SEMAPHORE`` is set.
    os.environ["SEMAPHORE"] = "true"
    os.environ

# Generated at 2022-06-14 04:47:16.860785
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "False"
    assert frigg(branch="master")
    os.environ["FRIGG_BUILD_BRANCH"] = "development"
    assert frigg(branch="development")
    os.environ["FRIGG_PULL_REQUEST"] = "True"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    assert not frigg(branch="master")
    os.environ["FRIGG_BUILD_BRANCH"] = "development"
    assert not frigg(branch="development")

# Generated at 2022-06-14 04:47:18.508623
# Unit test for function checker
def test_checker():
    @checker
    def test(arg: bool):
        assert arg

    assert test(True)

# Generated at 2022-06-14 04:47:28.534422
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    assert travis(branch='master')
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'true'
    try:
        travis(branch='master')
    except CiVerificationError:
        assert True
    else:
        assert False
    # Unit test for function semaphore

# Generated at 2022-06-14 04:47:36.964327
# Unit test for function travis
def test_travis():
    assert os.environ.get("TRAVIS_BRANCH") == branch
    assert os.environ.get("TRAVIS_PULL_REQUEST") == "false"


# Generated at 2022-06-14 04:47:42.897510
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"

    assert semaphore("master")



# Generated at 2022-06-14 04:47:55.542517
# Unit test for function check
def test_check():
    os.environ["BRANCH_NAME"] = 'master'
    os.environ["SEMAPHORE"] = 'true'
    os.environ["PULL_REQUEST_NUMBER"] = '3'
    os.environ["SEMAPHORE_THREAD_RESULT"] = 'failed'
    try:
        check()
    except CiVerificationError:
        pass
    os.environ["BRANCH_NAME"] = 'master'
    os.environ["SEMAPHORE"] = 'true'
    os.environ["PULL_REQUEST_NUMBER"] = '3'
    os.environ["SEMAPHORE_THREAD_RESULT"] = 'succeeded'
    try:
        check()
        assert False
    except CiVerificationError:
        pass
    os.en

# Generated at 2022-06-14 04:48:04.563396
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "true"
    os.environ["GIT_BRANCH"] = "develop"
    assert not check("develop")
    os.environ["GIT_BRANCH"] = "master"
    assert check("master")
    os.environ["CHANGE_ID"] = "1234"
    assert not check("master")
    os.environ.pop("CHANGE_ID")
    os.environ.pop("JENKINS_URL")



# Generated at 2022-06-14 04:48:13.364565
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BUILD_BRANCH'] = 'test'
    frigg('test')
    os.environ['FRIGG_BUILD_BRANCH'] = 'wrong'
    os.environ['FRIGG_PULL_REQUEST'] = 'true'
    try:
        frigg('test')
        assert False
    except CiVerificationError:
        assert True
    del os.environ['FRIGG']

# Generated at 2022-06-14 04:48:15.378441
# Unit test for function circle
def test_circle():
    assert circle('master')


# Generated at 2022-06-14 04:48:17.850326
# Unit test for function circle
def test_circle():
    assert circle(branch="master")
    assert circle(branch="my_fancy_branch")

# Generated at 2022-06-14 04:48:21.978467
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    check(branch="master")
    assert True
    del os.environ["GITLAB_CI"]



# Generated at 2022-06-14 04:48:33.507622
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    try:
        gitlab("master")
    except Exception as e:
        assert e.__class__ == CiVerificationError

    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "release"
    try:
        gitlab("master")
    except Exception as e:
        assert e.__class__ == AssertionError

    del os.environ["GITLAB_CI"]
    try:
        gitlab("master")
    except Exception as e:
        assert e.__class__ == AssertionError

# Generated at 2022-06-14 04:48:37.600190
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    checker(semaphore)
    del os.environ["SEMAPHORE"]



# Generated at 2022-06-14 04:48:46.120718
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    travis('master')



# Generated at 2022-06-14 04:48:55.817441
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["JENKINS_URL"] = True
    os.environ["CHANGE_ID"] = None
    assert jenkins("master")

    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["JENKINS_URL"] = True
    os.environ["CHANGE_ID"] = 'CHANGE_ID'
    assert jenkins("master") == False

# Generated at 2022-06-14 04:48:58.726827
# Unit test for function jenkins
def test_jenkins():
    assert not jenkins("master")
    assert not jenkins("master")
    assert not jenkins("master")
    assert not jenkins("master")
    assert not jenkins("master")
    assert not jenkins("master")

# Generated at 2022-06-14 04:49:05.164361
# Unit test for function checker
def test_checker():
    def test_func(name):
        return name

    assert checker(test_func)('test') == 'test'

    def broken_func(name):
        assert False
        return name

    try:
        checker(broken_func)('test')
    except Exception as e:
        assert isinstance(e, CiVerificationError)

# Generated at 2022-06-14 04:49:12.978836
# Unit test for function frigg
def test_frigg():
    # Arange
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "test_branch"
    os.environ["FRIGG_PULL_REQUEST"] = "true"

    # Act
    frigg(branch="test_branch")

    # Clean Up
    os.environ.pop("FRIGG")
    os.environ.pop("FRIGG_BUILD_BRANCH")
    os.environ.pop("FRIGG_PULL_REQUEST")



# Generated at 2022-06-14 04:49:15.920883
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "test"
    del os.environ["BITBUCKET_PR_ID"]
    bitbucket("test")


# Generated at 2022-06-14 04:49:18.920653
# Unit test for function check
def test_check():
    """
    Test that if the checking function can not find a suitable
    CI environment it will raise a mistake.
    """

    # Mock the environment
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'

    check()

# Generated at 2022-06-14 04:49:24.130183
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "test_frigg"
    os.environ["FRIGG_PULL_REQUEST"] = "false"

    frigg("test_frigg")
    assert True



# Generated at 2022-06-14 04:49:28.028147
# Unit test for function checker
def test_checker():
    @checker
    def fail_func():
        raise AssertionError

    @checker
    def pass_func():
        pass

    assert fail_func() is False
    assert pass_func() is True



# Generated at 2022-06-14 04:49:30.447916
# Unit test for function semaphore
def test_semaphore():
    try:
        semaphore("master")
    except CiVerificationError:
        raise AssertionError("The semaphore check should have passed")



# Generated at 2022-06-14 04:49:37.506232
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()


# Generated at 2022-06-14 04:49:46.816514
# Unit test for function travis
def test_travis():
    travis("master")

    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")

    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        travis("master")
    except CiVerificationError:
        print("exception caught")
        assert True
    else:
        assert False

    os.environ["TRAVIS_BRANCH"] = "develop"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    try:
        travis("master")
    except CiVerificationError:
        print("exception caught")

# Generated at 2022-06-14 04:49:47.432354
# Unit test for function semaphore
def test_semaphore():
    pass

# Generated at 2022-06-14 04:49:56.621594
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BUILD_NUMBER'] = "true"
    os.environ['BITBUCKET_BRANCH'] = "master"
    try:
        bitbucket("master")
    except:
        assert False

    os.environ['BITBUCKET_BRANCH'] = "develop"
    try:
        bitbucket("master")
        assert False
    except CiVerificationError:
        assert True

    del os.environ['BITBUCKET_BUILD_NUMBER']
    del os.environ['BITBUCKET_BRANCH']

# Generated at 2022-06-14 04:50:02.658425
# Unit test for function check
def test_check():
    """
    Test check with simple mocked environment
    """
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"

    check()

    del os.environ["TRAVIS"]
    del os.environ["TRAVIS_BRANCH"]
    del os.environ["TRAVIS_PULL_REQUEST"]

# Generated at 2022-06-14 04:50:06.908516
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    check("master")



# Generated at 2022-06-14 04:50:10.504093
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    try:
        travis("master")
    except:
        assert False



# Generated at 2022-06-14 04:50:13.196243
# Unit test for function jenkins
def test_jenkins():
    test_env = {
        "JENKINS_URL": "URL",
        "GIT_BRANCH": "master"
    }
    assert jenkins == check
    jenkins(test_env)

# Generated at 2022-06-14 04:50:17.206868
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = False
    check()



# Generated at 2022-06-14 04:50:20.431341
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = "true"
    os.environ['BRANCH_NAME'] = "master"
    os.environ['CHANGE_ID'] = ""
    jenkins()

# Generated at 2022-06-14 04:50:30.359608
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_PROJECT_PATH"] = "repo"
    check(branch="master")
    assert os.environ["CI_COMMIT_REF_NAME"] == "master"
    os.environ.pop("CI_COMMIT_REF_NAME")
    assert os.environ["CI_PROJECT_PATH"] == "repo"
    os.environ.pop("CI_PROJECT_PATH")


# Generated at 2022-06-14 04:50:40.076403
# Unit test for function circle
def test_circle():
    os.environ['CIRCLE_BRANCH'] = 'master'
    check('master')
    os.environ['CIRCLE_BRANCH'] = 'feature/new'
    with pytest.raises(CiVerificationError):
        check('master')
    os.environ.pop('CIRCLE_BRANCH')
    with pytest.raises(CiVerificationError):
        check('master')

    os.environ['CI_PULL_REQUEST'] = ''
    with pytest.raises(CiVerificationError):
        check('master')
    os.environ.pop('CI_PULL_REQUEST')


# Generated at 2022-06-14 04:50:46.663435
# Unit test for function travis
def test_travis():
    # No travis env
    os.environ["TRAVIS"] = "false"
    # Not on master
    os.environ["TRAVIS_BRANCH"] = "dev"
    #  fails
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    assert travis("master") == False

    os.environ["TRAVIS_BRANCH"] = "master"
    assert travis("master") == True


# Generated at 2022-06-14 04:50:53.224189
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "branch-to-be-released"
    os.environ["PULL_REQUEST_NUMBER"] = "55"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"

    expected_exception = "The verification check for the environment did not pass."
    try:
        semaphore("branch-to-be-released")
    except CiVerificationError as e:
        actual_exception = str(e)
    assert expected_exception == actual_exception


# Generated at 2022-06-14 04:50:55.636474
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master")

# Generated at 2022-06-14 04:51:06.882589
# Unit test for function bitbucket
def test_bitbucket():
    # Test valid environment
    os.environ["BITBUCKET_BRANCH"] = "master"
    bitbucket(branch="master")

    # Test bad branch
    os.environ["BITBUCKET_BRANCH"] = "staging"
    try:
        bitbucket(branch="master")
        raise AssertionError("Expected an exception.")
    except CiVerificationError:
        pass

    # Test pull-request
    os.environ["BITBUCKET_PR_ID"] = "42"
    try:
        bitbucket(branch="master")
        raise AssertionError("Expected an exception.")
    except CiVerificationError:
        pass



# Generated at 2022-06-14 04:51:15.267766
# Unit test for function bitbucket
def test_bitbucket():
    # Setting environment variable
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ.pop("BITBUCKET_PR_ID", None)
    assert bitbucket("master")
    assert not bitbucket("develop")
    assert not bitbucket("")
    os.environ.pop("BITBUCKET_BRANCH", None)
    os.environ["BITBUCKET_PR_ID"] = "5"
    bitbucket("master") is None
    os.environ.pop("BITBUCKET_PR_ID", None)
    assert not bitbucket("master")
    assert not bitbucket("develop")
    assert not bitbucket("")


# Generated at 2022-06-14 04:51:20.311639
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")
    assert os.environ["TRAVIS_BRANCH"] == "master"
    assert os.environ["TRAVIS_PULL_REQUEST"] == "false"



# Generated at 2022-06-14 04:51:28.046891
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    check("staging")
    os.environ["TRAVIS_BRANCH"] = "staging"
    check("staging")
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    check("staging")
    check("master")

# Generated at 2022-06-14 04:51:31.231354
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    gitlab("master")

# Generated at 2022-06-14 04:51:50.171745
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = "master"
    os.environ['BITBUCKET_PR_ID'] = ""
    checker(bitbucket)
    os.environ['BITBUCKET_BRANCH'] = "master"
    os.environ['BITBUCKET_PR_ID'] = "1"
    try:
        checker(bitbucket)
    except AssertionError:
        pass
    os.environ['BITBUCKET_BRANCH'] = "feature"
    os.environ['BITBUCKET_PR_ID'] = ""
    try:
        checker(bitbucket)
    except AssertionError:
        pass



# Generated at 2022-06-14 04:51:55.056080
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'success'
    semaphore('master')



# Generated at 2022-06-14 04:51:56.969011
# Unit test for function jenkins
def test_jenkins():
    import os
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "https://jenkins.com/"
    os.environ["CHANGE_ID"] = ""
    with pytest.raises(CiVerificationError):
        assert jenkins("abc")

# Generated at 2022-06-14 04:52:01.399049
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "staging"
    os.environ["BITBUCKET_PR_ID"] = "1"
    with pytest.raises(CiVerificationError):
        bitbucket("master")
    del os.environ["BITBUCKET_PR_ID"]
    bitbucket("staging")


# Generated at 2022-06-14 04:52:11.147121
# Unit test for function frigg
def test_frigg():

    os.environ['FRIGG'] = 'true'
    os.environ['FRIGG_BRANCH'] = 'master'
    os.environ['FRIGG_PULL_REQUEST'] = ''
    os.environ['FRIGG_BUILD_BRANCH'] = 'master'

    frigg('master')

    os.environ['FRIGG_PULL_REQUEST'] = '1'

    try:
        frigg('master')
    except CiVerificationError as e:
        assert(e.args[0] == 'The verification check for the environment did not pass.')
        return

    assert(False)


# Generated at 2022-06-14 04:52:12.156102
# Unit test for function travis
def test_travis():
    assert travis("master")

# Generated at 2022-06-14 04:52:15.943698
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "master"
    assert bitbucket(branch="master")



# Generated at 2022-06-14 04:52:24.196281
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = "true"
    os.environ['CIRCLE_BRANCH'] = "master"
    os.environ['CI_PULL_REQUEST'] = ""
    assert circle("master")

    os.environ['CIRCLECI'] = ""
    os.environ['CIRCLE_BRANCH'] = ""
    os.environ['CI_PULL_REQUEST'] = ""
    assert not circle("master")

    os.environ['CIRCLECI'] = "true"
    os.environ['CIRCLE_BRANCH'] = "master"
    os.environ['CI_PULL_REQUEST'] = "1"
    assert not circle("master")

    os.environ['CIRCLECI'] = "true"

# Generated at 2022-06-14 04:52:29.756336
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")  # will pass
    try:
        travis("develop")  # will fail
    except CiVerificationError:
        return
    assert False


# Generated at 2022-06-14 04:52:35.682018
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    gitlab(branch="master")
    assert os.environ.get("CI_COMMIT_REF_NAME") == "master"

    del os.environ["CI_COMMIT_REF_NAME"]
    with pytest.raises(CiVerificationError):
        gitlab(branch="master")



# Generated at 2022-06-14 04:53:02.758445
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_BUILD_BRANCH"] = "true"
    frigg("master")
    # Test that branch does not match
    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    frigg("master")


# Generated at 2022-06-14 04:53:10.296211
# Unit test for function frigg
def test_frigg():
    orig_environ = os.environ.copy()
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"

    frigg("master")

    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    os.environ["FRIGG_PULL_REQUEST"] = "1"

    frigg("master")
    os.environ = orig_environ



# Generated at 2022-06-14 04:53:15.603117
# Unit test for function semaphore
def test_semaphore():
    assert not semaphore
    assert os.environ["BRANCH_NAME"] == "master"
    assert os.environ["PULL_REQUEST_NUMBER"] is None
    assert os.environ["SEMAPHORE_THREAD_RESULT"] != "failed"

# Generated at 2022-06-14 04:53:17.937013
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis(os.environ['TRAVIS_BRANCH'])


# Generated at 2022-06-14 04:53:22.405694
# Unit test for function circle
def test_circle():
    """
    Unit test for function circle
    """
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "develop"
    os.environ["CI_PULL_REQUEST"] = "true"
    check("develop")

    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    check("master")


# Generated at 2022-06-14 04:53:30.396466
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_PULL_REQUEST'] = "true"
    os.environ['TRAVIS_BRANCH'] = "master"

    try:
        check()
        assert 0
    except AssertionError:
        pass
    except:
        assert 0

    os.environ['TRAVIS_PULL_REQUEST'] = "false"
    os.environ['TRAVIS_BRANCH'] = "master"

    try:
        check()
    except AssertionError:
        assert 0
    except:
        assert 0


# Generated at 2022-06-14 04:53:41.271553
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "feature/branch"
    os.environ["FRIGG_PULL_REQUEST"] = "1"
    try:
        frigg("feature")
    except CiVerificationError:
        pass
    else:
        assert False
    os.environ["FRIGG_BUILD_BRANCH"] = "feature"
    os.environ["FRIGG_PULL_REQUEST"] = "0"
    try:
        frigg("feature")
    except CiVerificationError:
        assert False
    finally:
        del os.environ["FRIGG"]
        del os.environ["FRIGG_BUILD_BRANCH"]

# Generated at 2022-06-14 04:53:44.816720
# Unit test for function checker
def test_checker():
    def check():
        raise AssertionError("Check failed!")
    check = checker(check)
    try:
        check()
    except CiVerificationError as cive:
        assert cive.msg == "The verification check for the environment did not pass."
    else:
        raise Exception("CiVerificationError not raised on faulty check")

# Generated at 2022-06-14 04:53:46.268780
# Unit test for function check
def test_check():
    assert check("whatever") is None

# Generated at 2022-06-14 04:53:50.771394
# Unit test for function checker
def test_checker():
    """False function"""
    @checker
    def false_func():
        """A function that always fails to ensure that the checker always raises CiVerificationError"""
        assert False

    # Assert that the false function returns false
    assert false_func() == False


# Generated at 2022-06-14 04:54:52.862026
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "develop"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert check("master") is True
    os.environ["TRAVIS_BRANCH"] = "master"
    assert check("master") is True
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        check("master")
    except CiVerificationError:
        assert True
    else:
        assert False
    os.environ["TRAVIS_BRANCH"] = "develop"
    try:
        check("master")
    except CiVerificationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:54:59.689745
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "False"
    assert frigg("master"), "Frigg should be working with branch master"
    os.environ["FRIGG_PULL_REQUEST"] = "True"
    assert frigg("master") is False, "Frigg should not be working with pullrequests"
    try:
        frigg("test")
        assert False, "Frigg should not be working on branch test and should raise a CiVerificationError"
    except CiVerificationError as e:
        assert "Frigg" in str(e), "CiVerificationError in frigg should include the name Frigg"

#