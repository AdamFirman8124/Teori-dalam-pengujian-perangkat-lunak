

# Generated at 2022-06-14 04:45:17.889405
# Unit test for function circle
def test_circle():
    assert not circle(branch="master")
    assert not circle(branch="test")
    os.environ["CIRCLE_BRANCH"] = "test"
    assert circle(branch="test")
    assert not circle(branch="master")
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "true"
    assert not circle(branch="master")
    assert not circle(branch="test")
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CI_PULL_REQUEST"]


# Generated at 2022-06-14 04:45:18.608358
# Unit test for function check
def test_check():
    assert check() == True

# Generated at 2022-06-14 04:45:20.280103
# Unit test for function travis
def test_travis():
    assert travis() == True

# Generated at 2022-06-14 04:45:32.024051
# Unit test for function circle
def test_circle():
    env_vars = os.environ.copy()
    env_vars['CIRCLECI'] = 'true'
    env_vars['CIRCLE_BRANCH'] = 'master'
    # PULL REQUEST test
    env_vars['CI_PULL_REQUEST'] = 'https://github.com/jhermann/artifacts/pull/1'
    env_vars['CI_PULL_REQUESTS'] = 'https://github.com/jhermann/artifacts/pull/1'
    try:
        with os.scopenviron(env_vars):
            circle('master')
    except Exception as err:
        assert err.args[0] == 'The verification check for the environment did not pass.'
    # SUCCESS test

# Generated at 2022-06-14 04:45:34.670866
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = ""
    frigg()

# Generated at 2022-06-14 04:45:39.689252
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "feature/test"
    assert gitlab(branch="master") is False
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    assert gitlab(branch="master") is True



# Generated at 2022-06-14 04:45:51.458709
# Unit test for function frigg
def test_frigg():
    """
    Unit test for the function ``frigg``.
    """
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = ""
    try:
        frigg("master")
    except CiVerificationError:
        assert False, "Should not raise CiVerificationError"
    try:
        frigg("develop")
        assert False, "Should raise CiVerificationError"
    except CiVerificationError:
        assert True

    os.environ["FRIGG_PULL_REQUEST"] = "42"

# Generated at 2022-06-14 04:45:55.152785
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    celery_tasks.check("master")
    os.environ["CI_COMMIT_REF_NAME"] = "feature/test"
    celery_tasks.check("master")

# Generated at 2022-06-14 04:46:05.805648
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    os.environ["PULL_REQUEST_NUMBER"] = "123"

    assert os.environ["SEMAPHORE"] == "true"
    assert os.environ["BRANCH_NAME"] == "master"
    assert os.environ["PULL_REQUEST_NUMBER"] == "123"
    assert os.environ["SEMAPHORE_THREAD_RESULT"] == "failed"

    try:
        semaphore("master")
    except CiVerificationError:
        pass
    else:
        assert False, "Expected CiVerificationError"

    os.environ

# Generated at 2022-06-14 04:46:07.510076
# Unit test for function bitbucket
def test_bitbucket():
    bitbucket('mybranch')

# Generated at 2022-06-14 04:46:20.355625
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    circle("master")



# Generated at 2022-06-14 04:46:31.181880
# Unit test for function semaphore
def test_semaphore():
    os.environ.update(
        {"BRANCH_NAME": "master", "PULL_REQUEST_NUMBER": "1", "SEMAPHORE_THREAD_RESULT": "failed"}
        )
    import pytest
    with pytest.raises(CiVerificationError):
        semaphore("master")
    os.environ.update(
        {"BRANCH_NAME": "develop", "PULL_REQUEST_NUMBER": "1", "SEMAPHORE_THREAD_RESULT": "failed"}
        )
    with pytest.raises(CiVerificationError):
        semaphore("master")

# Generated at 2022-06-14 04:46:40.011420
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    try:
        bitbucket("develop")
    except CiVerificationError:
        pass
    else:
        assert False
    del os.environ['BITBUCKET_BRANCH']
    try:
        bitbucket("develop")
    except CiVerificationError:
        pass
    else:
        assert False
    os.environ['BITBUCKET_BRANCH'] = "develop"
    try:
        bitbucket("master")
    except CiVerificationError:
        pass
    else:
        assert False
    os.environ['BITBUCKET_PR_ID'] = '1'
    try:
        bitbucket("develop")
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:46:42.692379
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "some_branch"
    os.environ["BITBUCKET_PR_ID"] = "123"
    check("some_branch")

# Generated at 2022-06-14 04:46:53.249148
# Unit test for function check
def test_check():
    """
    Unit test for function check
    """
    # Set up
    os.environ['TRAVIS']='true'
    os.environ['TRAVIS_BRANCH']='master'
    os.environ['TRAVIS_PULL_REQUEST']='false'

    # Test 1
    check()

    # Set up
    os.environ['TRAVIS_BRANCH']='develop'

    # Test 2
    try:
        check()
        raise Exception("Test 2 Error")
    except CiVerificationError as e:
        print(e)

    # Set up
    os.environ['TRAVIS_BRANCH']='master'
    os.environ['TRAVIS_PULL_REQUEST']='true'

    # Test 3

# Generated at 2022-06-14 04:46:56.534255
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = branch
    assert gitlab(branch) is True



# Generated at 2022-06-14 04:47:03.759854
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    assert circle('master') is True
    assert bitbucket('master') is False
    del os.environ["CIRCLECI"]
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CI_PULL_REQUEST"]


# Generated at 2022-06-14 04:47:06.890577
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"

    with pytest.raises(CiVerificationError):
        frigg("develop")
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg("master")


# Generated at 2022-06-14 04:47:07.872633
# Unit test for function semaphore
def test_semaphore():
    check(branch = "dev")


# Generated at 2022-06-14 04:47:10.373337
# Unit test for function checker
def test_checker():
    @checker
    def myfunc(param):
        assert param == test_checker.code

    myfunc(True)
    myfunc(False)
    test_checker.code = True
    myfunc(True)

# Generated at 2022-06-14 04:47:22.839738
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    assert semaphore("master")
    os.environ["SEMAPHORE"] = "false"
    assert semaphore("master")
    os.environ["BRANCH_NAME"] = "master"
    assert semaphore("master")
    assert semaphore("develop")
    os.environ["BRANCH_NAME"] = "develop"
    os.environ["PULL_REQUEST_NUMBER"] = "1"
    assert semaphore("master")
    assert semaphore("develop")
    del os.environ["PULL_REQUEST_NUMBER"]
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    assert semaphore("master")
    assert semaphore("develop")


# Generated at 2022-06-14 04:47:25.348876
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master")



# Generated at 2022-06-14 04:47:29.391500
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    assert frigg("master")
    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    assert not frigg("master")

    del os.environ["FRIGG"]
    assert not frigg("master")

# Generated at 2022-06-14 04:47:31.224184
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = 'master'
    os.environ['BITBUCKET_PR_ID'] = '1'
    bitbucket(branch='master')

# Generated at 2022-06-14 04:47:37.311157
# Unit test for function jenkins
def test_jenkins():
    os.environ['BRANCH_NAME'] = "master"
    os.environ['GIT_BRANCH'] = "master"
    os.environ['JENKINS_URL'] = "https://jenkins.com"
    os.environ['CHANGE_ID'] = ""

    with open(os.devnull, 'w') as devnull:
        jenkins("master")

# Generated at 2022-06-14 04:47:48.352995
# Unit test for function frigg
def test_frigg():

    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "False"
    assert frigg("master") is True

    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "True"
    assert frigg("master") is False

    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    os.environ["FRIGG_PULL_REQUEST"] = "True"
    assert frigg("master") is False


# Generated at 2022-06-14 04:47:54.882430
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = 'master'
    os.environ["BITBUCKET_PR_ID"] = ''
    assert bitbucket('master') == True
    del os.environ["BITBUCKET_BRANCH"]
    del os.environ["BITBUCKET_PR_ID"]
    assert bitbucket('master') == False


# Generated at 2022-06-14 04:48:06.501267
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    check()
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "10"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    with pytest.raises(CiVerificationError):
        check()
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"]

# Generated at 2022-06-14 04:48:12.005344
# Unit test for function travis
def test_travis():
    os.environ.update(
        {
            "TRAVIS_BRANCH": "master",
            "TRAVIS_PULL_REQUEST": "false",
            "TRAVIS": "true"
        }
    )

    travis(branch="master")



# Generated at 2022-06-14 04:48:23.125072
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "some-branch"
    assert check()
    os.environ["CI_MERGE_REQUEST_IID"] = "10"
    try:
        check()
    except CiVerificationError:
        assert True
    else:
        assert False, "Should raise CiVerificationError"
    del os.environ["CI_MERGE_REQUEST_IID"]
    del os.environ["GITLAB_CI"]
    try:
        check()
    except CiVerificationError:
        assert True
    else:
        assert False, "Should raise CiVerificationError"



# Generated at 2022-06-14 04:48:40.836473
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    assert frigg("master") is True
    os.environ["FRIGG_BUILD_BRANCH"] = "devel"
    try:
        frigg("master")
    except CiVerificationError:
        pass
    else:
        raise Exception("Should have failed")

    assert os.environ["FRIGG_BUILD_BRANCH"] == "devel"
    os.environ["FRIGG_PULL_REQUEST"] = "123"
    try:
        frigg("master")
    except CiVerificationError:
        pass
    else:
        raise Exception("Should have failed")
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    assert frigg("master") is True
    del os.en

# Generated at 2022-06-14 04:48:46.172880
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "True"
    os.environ["BRANCH_NAME"] = "hotfix/test"
    os.environ["GIT_BRANCH"] = "hotfix/test"
    os.environ["CHANGE_ID"] = "123"
    assert(jenkins("test") == True)

# Generated at 2022-06-14 04:48:51.305129
# Unit test for function checker
def test_checker():
    @checker
    def add(x, y):
        assert x == y

    add(1, 1)
    try:
        add(1, 2)
    except CiVerificationError as e:
        assert "environment did not pass" in str(e)
    else:
        assert False

# Generated at 2022-06-14 04:48:58.213121
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "dev"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    with pytest.raises(CiVerificationError):
        check("master")
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    with pytest.raises(CiVerificationError):
        check("master")



# Generated at 2022-06-14 04:49:03.584174
# Unit test for function jenkins
def test_jenkins():
    os.environ.update({"JENKINS_URL":"test", "GIT_BRANCH":"test"})
    check()
    os.environ.update({"JENKINS_URL": "test", "GIT_BRANCH": "master"})
    check()

# Generated at 2022-06-14 04:49:06.491199
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "true"
    os.environ["GIT_BRANCH"] = "master"

    check("master")

    os.environ["CHANGE_ID"] = "true"

    try:
        check("master")
    except CiVerificationError:
        return True
    return False


# Generated at 2022-06-14 04:49:09.719795
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    assert 1

# Generated at 2022-06-14 04:49:19.285416
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    try:
        travis('master')
    except CiVerificationError:
        assert False
    os.environ['TRAVIS_BRANCH'] = 'otherBranch'
    try:
        travis('master')
        assert False
    except CiVerificationError:
        os.environ['TRAVIS_BRANCH'] = 'master'
        os.environ['TRAVIS_PULL_REQUEST'] = 'true'
        try:
            travis('master')
            assert False
        except CiVerificationError:
            del os.environ['TRAVIS_BRANCH']

# Generated at 2022-06-14 04:49:22.311584
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = "true"
    os.environ['CIRCLE_BRANCH'] = "master"
    check()



# Generated at 2022-06-14 04:49:29.292701
# Unit test for function frigg
def test_frigg():
    with open('fixture.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('fixture.txt', 'w') as fout:
        fout.writelines(data[1:])
    os.environ["FRIGG_PULL_REQUEST"] = "123"
    try:
        frigg("master")
        assert False
    except CiVerificationError:
        assert True
    os.environ["FRIGG_PULL_REQUEST"] = None

# Generated at 2022-06-14 04:49:46.690836
# Unit test for function gitlab
def test_gitlab():
    os.environ['GITLAB_CI'] = 'true'
    os.environ['CI_COMMIT_REF_NAME'] = 'some_branch'
    assert gitlab('some_branch') is True
    del os.environ['CI_COMMIT_REF_NAME']
    os.environ['CI_MERGE_REQUEST_ID'] = 'some_id'
    assert gitlab('whatever') is False
    del os.environ['CI_MERGE_REQUEST_ID']
    del os.environ['GITLAB_CI']
    assert gitlab('whatever') is True

# Generated at 2022-06-14 04:49:57.692855
# Unit test for function semaphore
def test_semaphore():
    """
    Perform a unit test on the necessary checks to ensure that the semaphore
    build is successful, on the correct branch and not a pull-request.

    :param branch:  The branch the environment should be running against.
    """
    assert os.environ.get("BRANCH_NAME") == "master", "BRANCH_NAME not match"
    assert os.environ.get("PULL_REQUEST_NUMBER") is None, "PULL_REQUEST_NUMBER not match"
    assert os.environ.get(
        "SEMAPHORE_THREAD_RESULT"
    ) != "failed", "SEMAPHORE_THREAD_RESULT not match"

    print("Unit test for function semaphore success")

# Generated at 2022-06-14 04:50:05.997366
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    # os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert check() == True
    """
    Test Case 1:
    master branch, no pull-request
    """

    os.environ["PULL_REQUEST_NUMBER"] = ""
    assert check() == False

    """
    Test Case 2:
    development branch, no pull-request
    """
    os.environ["BRANCH_NAME"] = "development"
    assert check("development") == True

    """
    Test Case 3:
    development branch, no pull-request
    """

# Generated at 2022-06-14 04:50:16.389469
# Unit test for function semaphore
def test_semaphore():
    os.environ.pop('BRANCH_NAME', None)
    os.environ.pop('PULL_REQUEST_NUMBER', None)
    os.environ.pop('SEMAPHORE_THREAD_RESULT', None)

    os.environ.update({"SEMAPHORE": "true"})
    semaphore("master")

    os.environ.update({"SEMAPHORE": "false"})
    try:
        semaphore("master")
        assert False, "semaphore() should have raised"
    except CiVerificationError:
        pass

    os.environ.update({"SEMAPHORE_THREAD_RESULT": "failed"})

# Generated at 2022-06-14 04:50:17.855073
# Unit test for function travis
def test_travis():
    # TODO: Find a way to mock environment variables
    pass


# Generated at 2022-06-14 04:50:24.477438
# Unit test for function gitlab
def test_gitlab():
    from mock import patch

    with patch.dict(os.environ, {
        'CI_COMMIT_REF_NAME': 'master',
    }):
        gitlab('master')

    with patch.dict(os.environ, {
        'CI_COMMIT_REF_NAME': 'not-master',
    }):
        try:
            gitlab('master')
        except CiVerificationError:
            pass
        else:
            raise Exception("Test should have failed")

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 04:50:28.305455
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "123"
    try:
        bitbucket(branch="master")
        assert False
    except CiVerificationError:
        assert True
    del os.environ["BITBUCKET_PR_ID"]

    try:
        bitbucket(branch="master")
        assert True
    except CiVerificationError:
        assert False

# Generated at 2022-06-14 04:50:29.864909
# Unit test for function gitlab
def test_gitlab():
    os.environ['CI_COMMIT_REF_NAME'] = "master"
    os.environ['CI_MERGE_REQUEST_IID'] = None
    gitlab("master")

# Generated at 2022-06-14 04:50:38.497597
# Unit test for function gitlab
def test_gitlab():
    if os.environ.get("GITLAB_CI") != "true":
        # Test is not needed, exit
        return

    if os.environ.get("CI_COMMIT_REF_NAME") != "master":
        # Test is not needed, exit
        return

    # Test that the check succeeds
    assert gitlab("master") is True

    # Test that the CI_COMMIT_REF_NAME needed for gitlab to run, is absent
    old_name = os.environ.get("CI_COMMIT_REF_NAME")
    os.environ.pop("CI_COMMIT_REF_NAME")

    with pytest.raises(CiVerificationError):
        gitlab("master")

    # Restore state
    os.environ["CI_COMMIT_REF_NAME"] = old_name

    # Test that

# Generated at 2022-06-14 04:50:44.375247
# Unit test for function frigg
def test_frigg():
    """
    Test for function frigg with two cases:
    one that should pass and one that should raise a
    CiVerificationError
    """
    try:
        frigg('master')
    except CiVerificationError as e:
        raise AssertionError(e)
    try:
        frigg('not-master')
    except CiVerificationError:
        pass
    else:
        raise AssertionError

# Generated at 2022-06-14 04:51:07.742607
# Unit test for function bitbucket
def test_bitbucket():
    '''
    Verify if the environment variables are set and
    not set as expected for bitbucket CI
    '''
    os.environ["BITBUCKET_BUILD_NUMBER"] = "TEST_BUILD_NUMBER"
    os.environ["BITBUCKET_BRANCH"] = "TEST_BRANCH"
    os.environ["BITBUCKET_PR_ID"] = "TEST_PR_ID"

    bitbucket("TEST_BRANCH_2")

    assert os.environ["BITBUCKET_BRANCH"] == "TEST_BRANCH"
    assert os.environ["BITBUCKET_PR_ID"] == "TEST_PR_ID"

    del os.environ["BITBUCKET_BRANCH"]

# Generated at 2022-06-14 04:51:13.156482
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["BITBUCKET_BRANCH"] = "master"
    bitbucket("master")
    del os.environ["BITBUCKET_BRANCH"]
    os.environ["BITBUCKET_BRANCH"] = "develop"
    bitbucket("master")

# Generated at 2022-06-14 04:51:19.849605
# Unit test for function check
def test_check():
    environ_backup = os.environ.copy()
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()

    # Cleanup
    os.environ.clear()
    os.environ.update(environ_backup)

if __name__ == "__main__":
    test_check()

# Generated at 2022-06-14 04:51:25.826882
# Unit test for function checker
def test_checker():
    with test_case():
        pass
    with test_case():
        raise AssertionError
    with test_case(error=CiVerificationError):
        raise AssertionError

    @checker
    def test_case2():
        raise AssertionError

    with test_case(error=CiVerificationError):
        test_case2()

# Generated at 2022-06-14 04:51:35.562817
# Unit test for function gitlab
def test_gitlab():
    # Let's say a gitlab ci environment with 'develop' as a current branch.
    # Actual gitlab ci variables: https://docs.gitlab.com/ee/ci/variables/README.html
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "develop"
    # I expect a CiVerificationError to be raised no matter what
    try:
        gitlab("master")
    except CiVerificationError:
        assert True
    # I expect no errors to be raised if the given branch is 'develop'
    try:
        gitlab("develop")
    except CiVerificationError:
        assert False
    del os.environ["CI_COMMIT_REF_NAME"]
    del os.environ["GITLAB_CI"]

# Generated at 2022-06-14 04:51:42.529315
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "true"
    try:
        frigg(branch="master")
    except AssertionError:
        pass
    except Exception as e:
        raise e
    else:
        raise Exception("Test failed")



# Generated at 2022-06-14 04:51:45.359428
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "test_branch"
    assert check("test_branch") is None


# Generated at 2022-06-14 04:51:49.677278
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis(branch="master")


# Generated at 2022-06-14 04:51:53.717385
# Unit test for function gitlab
def test_gitlab():
    assert os.environ.get("CI_COMMIT_REF_NAME") == "master"
    assert os.environ.get("CI_COMMIT_REF_NAME") != "pull"

# Generated at 2022-06-14 04:51:57.514995
# Unit test for function jenkins
def test_jenkins():
    with os.environ.copy() as environ:
        assert not jenkins("foo")

        environ.update({"JENKINS_URL": "true"})
        assert not jenkins("foo")

        environ.update({"CHANGE_ID": "true"})
        assert not jenkins("foo")

        environ.update({"GIT_BRANCH": "master"})
        assert not jenkins("foo")

        environ.update({"GIT_BRANCH": "foo"})
        assert jenkins("foo")

        environ.update({"BRANCH_NAME": "foo"})
        assert jenkins("foo")

# Generated at 2022-06-14 04:52:22.027146
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()


# Generated at 2022-06-14 04:52:23.377123
# Unit test for function bitbucket
def test_bitbucket():
    assert bitbucket("master")
    assert not bitbucket("develop")



# Generated at 2022-06-14 04:52:35.539016
# Unit test for function bitbucket
def test_bitbucket():
    """
    This test will check if the bitbucket function is triggering the correct
    error.
    """
    bitbucket_build_number = {"BITBUCKET_BUILD_NUMBER": "123", "BITBUCKET_BRANCH": "master"}
    bitbucket_pull_request = {"BITBUCKET_BUILD_NUMBER": "123",
                              "BITBUCKET_BRANCH": "master", "BITBUCKET_PR_ID": "456"}
    bitbucket_branch_name = {"BITBUCKET_BUILD_NUMBER": "123", "BITBUCKET_BRANCH": "test"}
    os.environ.update(bitbucket_build_number)
    check()
    os.environ.update(bitbucket_pull_request)
    check()


# Generated at 2022-06-14 04:52:40.506398
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    del os.environ["CI_PULL_REQUEST"]
    check()
    assert True



# Generated at 2022-06-14 04:52:47.588536
# Unit test for function bitbucket
def test_bitbucket():
    # test for a non false value
    os.environ["BITBUCKET_BRANCH"] = "test"
    os.environ["BITBUCKET_PR_ID"] = "test"
    assert bitbucket("test") is None

    # test for a false value
    os.environ["BITBUCKET_BRANCH"] = "test"
    os.environ["BITBUCKET_PR_ID"] = None
    assert bitbucket("test") is True

    # test for wrong branch
    os.environ["BITBUCKET_BRANCH"] = "test2"
    os.environ["BITBUCKET_PR_ID"] = None
    assert bitbucket("test") is None



# Generated at 2022-06-14 04:52:53.493438
# Unit test for function checker
def test_checker():
    @checker
    def check_1():
        raise AssertionError("should raise exception")

    @checker
    def check_2():
        return True

    try:
        check_1()
    except CiVerificationError:
        pass
    else:
        raise Exception("No exception was raised")
    assert check_2()

# Generated at 2022-06-14 04:53:05.676702
# Unit test for function semaphore
def test_semaphore():
    # set up environment variables
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore(branch="master")

    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "1234"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    try:
        semaphore(branch="master")
    except Exception:
        assert True

# Generated at 2022-06-14 04:53:11.209261
# Unit test for function bitbucket
def test_bitbucket():
    """
    Test the bitbucket function
    :return: nothing
    """
    os.environ['BITBUCKET_BRANCH'] = 'master'
    bitbucket('master')

# Generated at 2022-06-14 04:53:20.439426
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    semaphore("master")
    del os.environ["BRANCH_NAME"]
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["SEMAPHORE_THREAD_RESULT"]
    os.environ["BRANCH_NAME"] = "not master"
    os.environ["PULL_REQUEST_NUMBER"] = "3"
    semaphore("master")
    del os.environ["BRANCH_NAME"]
    del os.environ["PULL_REQUEST_NUMBER"]

# Generated at 2022-06-14 04:53:21.594676
# Unit test for function semaphore
def test_semaphore():
    assert semaphore("master")

# Generated at 2022-06-14 04:54:19.440073
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "mybranch"
    os.environ["BITBUCKET_PR_ID"] = "123"
    bitbucket("master")

# Generated at 2022-06-14 04:54:24.209426
# Unit test for function gitlab
def test_gitlab():
    os.environ['GITLAB_CI'] = 'true'
    os.environ['CI_COMMIT_REF_NAME'] = 'master'
    gitlab('master')
    try:
        gitlab('foo')
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:54:30.539617
# Unit test for function frigg
def test_frigg():
    os.environ.setdefault('FRIGG', 'true')
    os.environ.setdefault('FRIGG_BUILD_BRANCH', 'master')
    os.environ.setdefault('FRIGG_PULL_REQUEST', 'false')
    frigg('master')
    os.environ.setdefault('FRIGG_BUILD_BRANCH', 'feature')
    try:
        frigg('master')
        raise Exception(
            'Expecting a CiVerificationError to be raised for wrong branch')
    except CiVerificationError:
        pass
    del os.environ['FRIGG']
    del os.environ['FRIGG_BUILD_BRANCH']
    del os.environ['FRIGG_PULL_REQUEST']


# Generated at 2022-06-14 04:54:36.088990
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    assert travis('master')

    # This will cause an assertion error because the variable has a wrong value
    os.environ['TRAVIS_BRANCH'] = 'dev'
    assert travis('master')


# Generated at 2022-06-14 04:54:40.382229
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = 'true'
    os.environ['CIRCLE_BRANCH'] = 'master'
    circle('master')
    os.environ['CIRCLE_BRANCH'] = 'develop'
    circle('develop')

# Generated at 2022-06-14 04:54:44.829298
# Unit test for function checker
def test_checker():
    """
    Test that the checker decorator raises checker
    """
    @checker
    def mock_function():
        raise AssertionError

    try:
        mock_function()
    except CiVerificationError:
        pass
    except Exception:
        raise RuntimeError("The checker decorator raised an unexpected exception.")



# Generated at 2022-06-14 04:54:50.173122
# Unit test for function frigg
def test_frigg():
    """
    Test the frigg checker.
    """
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    os.environ["FRIGG_PULL_REQUEST"] = "true"
    assert frigg("master") is False


# Generated at 2022-06-14 04:54:56.180709
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["BITBUCKET_PR_ID"] = None
    assert gitlab("master") == True
    os.environ["CI_COMMIT_REF_NAME"] = "test"
    assert gitlab("test") == True
    os.environ["BITBUCKET_PR_ID"] = "1234"
    assert gitlab("test") is None


# Generated at 2022-06-14 04:55:07.846471
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["GNOME_SYSTEM_MONITOR_BRANCH"] = "master"
    os.environ["CI_PROJECT_NAME"] = "semantic-release"
    os.environ["CI_PROJECT_ID"] = "semantic-release"
    os.environ["CI_PROJECT_NAMESPACE"] = "semantic-release"
    os.environ["CI_SERVER"] = "https://gitlab.com"

    # checks if master branch and CI_COMMIT_REF_NAME is in master
    check()

    # checks if master branch and CI_COMMIT_REF_NAME is not in master
    os.environ["CI_COMMIT_REF_NAME"] = "development"