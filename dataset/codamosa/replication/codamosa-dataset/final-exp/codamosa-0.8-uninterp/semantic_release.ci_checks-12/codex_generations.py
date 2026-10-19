

# Generated at 2022-06-14 04:45:15.149710
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")

# Generated at 2022-06-14 04:45:20.407370
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["JENKINS_URL"] = "http://jenkins.com"
    os.environ["CHANGE_ID"] = "1234"

    try:
        jenkins(branch="master")
    except:
        raise AssertionError("check jenkins")

    os.environ["CHANGE_ID"] = "12345"
    try:
        jenkins(branch="master")
        assert False
    except AssertionError:
        pass

    os.environ["GIT_BRANCH"] = "gh-pages"

# Generated at 2022-06-14 04:45:28.818951
# Unit test for function checker
def test_checker():
    @checker
    def func(x, y, z):
        assert x == y
        assert y == z
        assert z == x

    func(1, 1, 1)

    try:
        func(1, 1, 2)
        assert False
    except CiVerificationError:
        assert True

    try:
        func(1, 2, 1)
        assert False
    except CiVerificationError:
        assert True

    try:
        func(2, 1, 1)
        assert False
    except CiVerificationError:
        assert True

# Generated at 2022-06-14 04:45:35.219623
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = "master"
    os.environ['TRAVIS_PULL_REQUEST'] = "false"
    travis("master")
    os.environ['TRAVIS_BRANCH'] = "dev"
    os.environ['TRAVIS_PULL_REQUEST'] = "true"
    try:
        travis("master")
    except:
        print("Unit test for function travis is success")
        return
    print("Unit test for function travis is failed")


# Generated at 2022-06-14 04:45:42.639379
# Unit test for function semaphore
def test_semaphore():
    os.environ['SEMAPHORE'] = 'true'
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    assert semaphore('master')
    os.environ['BRANCH_NAME'] = 'develop'
    assert not semaphore('master')


# Generated at 2022-06-14 04:45:47.935869
# Unit test for function jenkins
def test_jenkins():
    test_env = os.environ.copy()
    test_env["JENKINS_URL"] = "https://jenkins.example.com"
    test_env["BRANCH_NAME"] = "feature/11"

    os.environ = test_env # pylint: disable=assigning-non-slot
    jenkins("feature/11")



# Generated at 2022-06-14 04:45:52.392879
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'test'
    os.environ['PULL_REQUEST_NUMBER'] = ''
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    semaphore('test')


# Generated at 2022-06-14 04:45:58.827449
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    frigg("master")
    del os.environ["FRIGG"]
    del os.environ["FRIGG_PULL_REQUEST"]
    del os.environ["FRIGG_BUILD_BRANCH"]


# Generated at 2022-06-14 04:46:02.371924
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BUILD_NUMBER"] = '10'
    os.environ["TRAVIS_PULL_REQUEST"] = 'false'
    os.environ["TRAVIS_BRANCH"] = 'master'
    travis('master')


# Generated at 2022-06-14 04:46:05.584096
# Unit test for function gitlab
def test_gitlab():
    assert not gitlab("master")
    try:
        gitlab("foo")
        assert False, 'gitlab() should raise exception'
    except CiVerificationError:
        pass


# Generated at 2022-06-14 04:46:18.668081
# Unit test for function semaphore
def test_semaphore():
    """
    Unit test for function semaphore
    """
    # Set env variables
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    semaphore()



# Generated at 2022-06-14 04:46:29.980084
# Unit test for function frigg
def test_frigg():
    fake_env_frigg = {"FRIGG": "true", "FRIGG_BUILD_BRANCH": "master"}
    fake_env_frigg_pull = {"FRIGG": "true", "FRIGG_PULL_REQUEST": "123"}
    os.environ.update(fake_env_frigg)
    frigg("master")
    os.environ.update(fake_env_frigg_pull)
    try:
        frigg("master")
    except CiVerificationError:
        pass
    finally:
        for key in fake_env_frigg.keys():
            os.environ.pop(key)
        for key in fake_env_frigg_pull.keys():
            os.environ.pop(key)


# Generated at 2022-06-14 04:46:35.325783
# Unit test for function checker
def test_checker():
    def test(branch: str) -> None:
        assert os.environ.get("BAD_VAR") == branch

    test = checker(test)

    os.environ["BAD_VAR"] = "master"
    test("master")

    os.environ["BAD_VAR"] = "develop"
    try:
        test("master")
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:46:40.128041
# Unit test for function checker
def test_checker():
    def my_check(data):
        assert data == "data"
    my_check = checker(my_check)
    my_check("data")
    try:
        my_check("invalid")
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:46:47.699840
# Unit test for function bitbucket
def test_bitbucket():
    os.environ.update(
        {
            "BITBUCKET_REPO_OWNER": "neil",
            "BITBUCKET_REPO_NAME": "test",
            "BITBUCKET_BUILD_NUMBER": "100",
            "BITBUCKET_BRANCH": "master",
            "BITBUCKET_PR_ID": "",
        }
    )
    bitbucket("master")
    assert os.environ.get("BITBUCKET_PR_ID") is None
    assert os.environ.get("BITBUCKET_BRANCH") == "master"

# Generated at 2022-06-14 04:46:49.449575
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    bitbucket("master")

# Generated at 2022-06-14 04:46:57.326397
# Unit test for function jenkins
def test_jenkins():
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['JENKINS_URL'] = "https://jenkins.com"
    os.environ['CHANGE_ID'] = "0000"
    assert jenkins('master') == True
    del os.environ['BRANCH_NAME']
    os.environ['GIT_BRANCH'] = "master"
    assert jenkins('master') == True
    os.environ['BRANCH_NAME'] = 'qwerty'
    assert jenkins('master') == False
    del os.environ['BRANCH_NAME']
    del os.environ['JENKINS_URL']
    assert jenkins('master') == False

# Generated at 2022-06-14 04:47:00.625261
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    assert check('master') is None

# Generated at 2022-06-14 04:47:03.888103
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_IID"] = None
    gitlab("master")



# Generated at 2022-06-14 04:47:06.712248
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI']='true'
    os.environ['CIRCLE_BRANCH']='release/next'
    os.environ['CI_PULL_REQUEST']='false'
    circle('release')

# Generated at 2022-06-14 04:47:16.427936
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = 'true'
    os.environ['CIRCLE_BRANCH'] = 'test'
    os.environ['CI_PULL_REQUEST'] = 'none'
    check('test')


# Generated at 2022-06-14 04:47:20.487194
# Unit test for function checker
def test_checker():
    # Check that checker returns original function
    def check(branch):
        assert(branch == "master")
    wrapped_check = checker(check)
    assert(wrapped_check == check)

    # Check that checker returns wrapped function that raises error
    @checker
    def wrapped_check(branch):
        assert(branch == "master")
    try:
        wrapped_check("dev")
        assert(False)
    # pylint: disable=broad-except
    except Exception as e:
        assert(isinstance(e, CiVerificationError))

# Generated at 2022-06-14 04:47:29.529672
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = '1'
    os.environ["BITBUCKET_BRANCH"] = 'develop'
    os.environ["BITBUCKET_PR_ID"] = '2'

    try:
        bitbucket('develop')
    except AssertionError:
        pass
    else:
        assert False

    try:
        bitbucket('master')
    except AssertionError:
        pass
    else:
        assert False

    os.environ["BITBUCKET_PR_ID"] = '3'
    bitbucket('master')

# Generated at 2022-06-14 04:47:33.816517
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = "master"
    os.environ['TRAVIS_PULL_REQUEST'] = "false"

    travis("master")


# Generated at 2022-06-14 04:47:36.412869
# Unit test for function circle
def test_circle():
    assert circle(branch="develop") is True
    assert circle(branch="test_branch") is False


# Generated at 2022-06-14 04:47:41.463676
# Unit test for function checker
def test_checker():
    class obj:
        def method(self):
            return False

    o = obj()
    assert not o.method()

    o.method = checker(o.method)

    try:
        o.method()
    except CiVerificationError:
        pass
    else:
        assert False

# Generated at 2022-06-14 04:47:49.318809
# Unit test for function check
def test_check():
    """
    Unit test for function check.
    """
    # Given
    original_os_environ = os.environ.copy()
    os.environ.update({"TRAVIS": "true", "TRAVIS_PULL_REQUEST": "false"})
    # When
    check()
    # Then there should be no exception
    os.environ.clear()
    os.environ.update(original_os_environ)


# Generated at 2022-06-14 04:47:59.131004
# Unit test for function bitbucket
def test_bitbucket():
    """
    Test function bitbucket
    """

    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "master"
    assert bitbucket("master") is True
    del os.environ["BITBUCKET_BRANCH"]
    assert bitbucket("master") is False
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "123"
    assert bitbucket("master") is False
    del os.environ["BITBUCKET_PR_ID"]
    assert bitbucket("master") is True
    os.environ["BITBUCKET_BRANCH"] = "masterx"
    assert bitbucket

# Generated at 2022-06-14 04:48:06.049114
# Unit test for function jenkins
def test_jenkins():
    # Test branch name as env variable
    os.environ["BRANCH_NAME"] = "test_branch"
    os.environ["JENKINS_URL"] = "TRUE"
    assert check("test_branch")
    del os.environ["BRANCH_NAME"]
    # Test branch name as env variable
    os.environ["GIT_BRANCH"] = "test_branch"
    os.environ["JENKINS_URL"] = "TRUE"
    assert check("test_branch")
    del os.environ["GIT_BRANCH"]



# Generated at 2022-06-14 04:48:15.799366
# Unit test for function semaphore
def test_semaphore():
    print("Executing test for function 'semaphore()'")
    env_vars = {}
    os.environ = env_vars

    # Test with CORRECT branch
    env_vars["BRANCH_NAME"] = "master"
    env_vars["PULL_REQUEST_NUMBER"] = None
    env_vars["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")

    # Test with WRONG branch
    env_vars["BRANCH_NAME"] = "feature-1"
    env_vars["PULL_REQUEST_NUMBER"] = "1"
    env_vars["SEMAPHORE_THREAD_RESULT"] = "passed"

# Generated at 2022-06-14 04:48:24.699071
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"

    assert travis() == True


# Generated at 2022-06-14 04:48:27.725990
# Unit test for function bitbucket
def test_bitbucket():
    try:
        os.environ["BITBUCKET_BRANCH"] = "master"
        os.environ["BITBUCKET_PR_ID"] = ""
        bitbucket("master")
    except CiVerificationError:
        assert False



# Generated at 2022-06-14 04:48:33.134685
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "test_branch"
    os.environ["GIT_BRANCH"] = "test_branch"
    os.environ["JENKINS_URL"] = "https://jenkins.example.com"
    os.environ["CHANGE_ID"] = ""

    check("test_branch")

# Generated at 2022-06-14 04:48:42.796073
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master") == True

    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        travis("master")
    except Exception as e:
        assert type(e) == CiVerificationError
        assert str(e) == "The verification check for the environment did not pass."


# Generated at 2022-06-14 04:48:44.997719
# Unit test for function circle
def test_circle():
    assert circle(branch="master") == True
    assert circle(branch="not_master") == False


# Generated at 2022-06-14 04:48:56.688310
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "TestBranch"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        travis()
        raise Exception("There should be a CI verification error")
    except CiVerificationError:
        pass
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis()  # Should not throw exception
    os.environ["TRAVIS_BRANCH"] = "master"
    travis("master")
    del os.environ["TRAVIS_BRANCH"]
    try:
        travis()
        raise Exception("There should be a CI verification error")
    except CiVerificationError:
        pass
    del os.environ["TRAVIS_PULL_REQUEST"]

# Generated at 2022-06-14 04:49:03.469577
# Unit test for function check
def test_check():
    """
    Makes sure that the check function is doing what it should be doing.
    """
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS"] = "true"
    assert check() is True

    # Reset env
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    del os.environ["TRAVIS"]

    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None

# Generated at 2022-06-14 04:49:08.494189
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = "true"
    try:
        jenkins("master")
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:49:13.283776
# Unit test for function gitlab
def test_gitlab():
    os.environ['GITLAB_CI'] = "true"
    os.environ['CI_COMMIT_REF_NAME'] = "master"
    os.environ['CI_MERGE_REQUEST_ID'] = ""
    check()

# Generated at 2022-06-14 04:49:20.922502
# Unit test for function circle
def test_circle():
    for os_value in [ "true", "false", None ]:
        os.environ["CIRCLECI"] = os_value
        for branch_value in ["some_branch", "master", "xxx"]:
            os.environ["CIRCLE_BRANCH"] = branch_value
            for pull_request_value in ["true", "false", None]:
                os.environ["CI_PULL_REQUEST"] = pull_request_value
                try:
                    check()
                except Exception:
                    if os_value == "true" and branch_value == "master" and pull_request_value == "false":
                        # Expected exception
                        del os.environ["CI_PULL_REQUEST"]
                        del os.environ["CIRCLE_BRANCH"]

# Generated at 2022-06-14 04:49:34.625970
# Unit test for function checker
def test_checker():
    """
    Test for function checker
    """
    @checker
    def checker_func(branch: str):
        """
        Test for a successful assertion
        """
        assert os.environ.get("BITBUCKET_BRANCH") == branch

    checker_func("master")

    try:
        @checker
        def checker_func(branch: str):
            """
            Test for an unsuccessful assertion
            """
            assert os.environ.get("BITBUCKET_BRANCH") == branch
            assert False

        checker_func("branch")
    except CiVerificationError:
        # If it fails, it fails as expected.
        pass



# Generated at 2022-06-14 04:49:44.562221
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    del os.environ["CI_MERGE_REQUEST_ID"]
    check("master")

    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = "123"
    assert check("master") == CiVerificationError("The verification check for the environment did not pass.")

    os.environ["CI_COMMIT_REF_NAME"] = "staging"
    os.environ["CI_MERGE_REQUEST_ID"] = "123"
    assert check("master") == CiVerificationError("The verification check for the environment did not pass.")

# Generated at 2022-06-14 04:49:53.959244
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "https://www.example.com"
    jenkins("master")

    os.environ["BRANCH_NAME"] = "develop"
    os.environ["JENKINS_URL"] = "https://www.example.com"
    try:
        jenkins("master")
        assert False
    except CiVerificationError as e:
        assert str(e) == "The verification check for the environment did not pass."



# Generated at 2022-06-14 04:49:57.986243
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = "true"
    os.environ['CIRCLE_BRANCH'] = "master"
    os.environ['CI_PULL_REQUEST'] = ""
    check("master")

# Generated at 2022-06-14 04:50:01.206078
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()


# Generated at 2022-06-14 04:50:05.639667
# Unit test for function checker
def test_checker():
    def func():
        assert 1 == 2

    try:
        func_check = checker(func)
    except:
        pass

    try:
        func_check()
    except CiVerificationError:
        pass



# Generated at 2022-06-14 04:50:15.854652
# Unit test for function frigg
def test_frigg():
    from tempfile import mkdtemp
    from shutil import rmtree
    from semantic_release.errors import CiVerificationError
    from semantic_release.tests.test_ci_verify import checker as mock_checker

    @mock_checker
    def mock_os(branch):
        assert branch == "master"
        assert os.environ.get("FRIGG_BUILD_BRANCH") == "master"
        assert not os.environ.get("FRIGG_PULL_REQUEST")


# Generated at 2022-06-14 04:50:18.675838
# Unit test for function circle
def test_circle():
    try:
        circle("master")
    except CiVerificationError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:50:22.121878
# Unit test for function jenkins
def test_jenkins():
    os.environ.setdefault("JENKINS_URL", "true")
    os.environ.setdefault("BRANCH_NAME", "test")
    os.environ.setdefault("CHANGE_ID", "true")
    jenkins("test")

# Generated at 2022-06-14 04:50:24.158021
# Unit test for function travis
def test_travis():
    assert travis('master')
    assert not travis('release/1.0.0')
    assert not travis('release/1.0.0')


# Generated at 2022-06-14 04:50:41.089640
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = "https://some-url.com"
    os.environ['BRANCH_NAME'] = "my-branch"
    os.environ['CHANGE_ID'] = ""
    check()

    os.environ['BRANCH_NAME'] = "wrong-branch"
    with pytest.raises(CiVerificationError):
        check()
    os.environ['BRANCH_NAME'] = "my-branch"

    os.environ['CHANGE_ID'] = "some-pr-id"
    with pytest.raises(CiVerificationError):
        check()


# Generated at 2022-06-14 04:50:43.302583
# Unit test for function gitlab
def test_gitlab():
    assert os.environ.get("CI_COMMIT_REF_NAME") == 'abc'
    assert not os.environ.get("CI_MERGE_REQUEST_ID")

# Generated at 2022-06-14 04:50:50.841406
# Unit test for function circle
def test_circle():
    """test_ci.test_circle
    Ensure the circle ci checks pass on a successful environment
    """
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    check()

    # Ensure it fails on a pull request
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "true"
    try:
        check()
    except CiVerificationError:
        pass
    else:
        raise AssertionError(
            "Check should have raised error on a PR. "
            "It did not. This is a bug."
        )

    # Ensure it fails on the wrong branch

# Generated at 2022-06-14 04:50:52.362368
# Unit test for function jenkins
def test_jenkins():
    assert check(branch = "test_branch")


# Generated at 2022-06-14 04:50:57.070848
# Unit test for function gitlab
def test_gitlab():
    # Variable is not set
    os.environ.pop("CI_COMMIT_REF_NAME", None)
    os.environ.pop("CI_MERGE_REQUEST_ID", None)
    check()

    # Branch name is other than master
    os.environ["CI_COMMIT_REF_NAME"] = "release"
    check("release")

    # Pull request
    os.environ["CI_MERGE_REQUEST_ID"] = "1"
    check()

# Generated at 2022-06-14 04:51:04.461536
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "false"
    os.environ["CIRCLE_BRANCH"] = "master"
    check("master")
    del os.environ["CIRCLECI"]
    del os.environ["CI_PULL_REQUEST"]
    del os.environ["CIRCLE_BRANCH"]


# Generated at 2022-06-14 04:51:15.124750
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"

    with pytest.raises(CiVerificationError):
        check(branch="dev")

    check(branch="master")

    del os.environ["TRAVIS"]

    os.environ["SEMAPHORE"] = "true"

    with pytest.raises(CiVerificationError):
        check(branch="wrong")

    check(branch="master")

    del os.environ["SEMAPHORE"]

    os.environ["FRIGG"] = "true"

    with pytest.raises(CiVerificationError):
        check(branch="wrong")

    check(branch="master")

    del os.environ["FRIGG"]

    os.environ["CIRCLECI"] = "true"

   

# Generated at 2022-06-14 04:51:22.952546
# Unit test for function frigg
def test_frigg():
    os.environ['FRIGG'] = "true"
    os.environ['FRIGG_BUILD_BRANCH'] = "master"
    os.environ['FRIGG_TASK'] = "Test Task"
    os.environ['FRIGG_MODULE_NAME'] = "repo"
    # should return True
    assert frigg("master")
    # should throw CiVerificationError
    os.environ['FRIGG_PULL_REQUEST'] = "true"
    assert frigg("master") == CiVerificationError


# Generated at 2022-06-14 04:51:26.699607
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis()



# Generated at 2022-06-14 04:51:36.036184
# Unit test for function semaphore
def test_semaphore():

    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")

    del os.environ["SEMAPHORE_THREAD_RESULT"]
    try:
        semaphore("master")
    except CiVerificationError:
        os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
        del os.environ["SEMAPHORE"]
        pass
    else:
        assert False

    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"

# Generated at 2022-06-14 04:51:52.446422
# Unit test for function travis
def test_travis():
    # os.environ['TRAVIS_BRANCH'] = 'master'
    # os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    assert travis('master') == True


# Generated at 2022-06-14 04:52:02.272555
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    check("master")

    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "develop"
    os.environ["BITBUCKET_PR_ID"] = ""
    check("develop")

    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = "123"
    check("develop")

# Generated at 2022-06-14 04:52:05.632300
# Unit test for function circle
def test_circle():
    assert not checker(circle)("master")
    assert not checker(circle)("release/1")
    assert checker(circle)("release/2")

# Generated at 2022-06-14 04:52:17.481736
# Unit test for function gitlab
def test_gitlab():
    gitlab_envs = [
        # Base scenario
        ("master", {"CI_COMMIT_REF_NAME": "master"}, None),
        # not the correct branch
        (
            "master",
            {"CI_COMMIT_REF_NAME": "develop"},
            CiVerificationError,
        ),
        # it's a pull request
        (
            "master",
            {"CI_COMMIT_REF_NAME": "master", "CI_MERGE_REQUEST_IID": "something"},
            CiVerificationError,
        ),
    ]
    for branch, kwargs, exception in gitlab_envs:
        for key, value in kwargs.items():
            os.environ[key] = value

# Generated at 2022-06-14 04:52:22.813223
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = ""
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore("master")
    del os.environ["BRANCH_NAME"]
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["SEMAPHORE_THREAD_RESULT"]

# Generated at 2022-06-14 04:52:27.857730
# Unit test for function jenkins
def test_jenkins():
    os.environ['BRANCH_NAME']='master'
    os.environ['GIT_BRANCH']='master'
    os.environ['JENKINS_URL']='some url'
    os.environ['CHANGE_ID']='some id'
    branch='master'
    branch_name = os.environ.get("BRANCH_NAME") or os.environ.get("GIT_BRANCH")
    assert os.environ.get("JENKINS_URL") is not None
    assert branch_name == branch
    assert not os.environ.get("CHANGE_ID")  # pull request id

# Generated at 2022-06-14 04:52:30.013351
# Unit test for function travis
def test_travis():
    try:
        travis("master")
    except:
        raise


# Generated at 2022-06-14 04:52:31.983253
# Unit test for function circle
def test_circle():
    os.environ['CIRCLE_BRANCH'] = 'master'
    check()


# Generated at 2022-06-14 04:52:38.595455
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    gitlab("master")
    os.environ["CI_COMMIT_REF_NAME"] = "not_master"
    try:
        gitlab("master")
    except CiVerificationError:
        assert True
    else:
        assert False
    del os.environ["CI_COMMIT_REF_NAME"]


# Generated at 2022-06-14 04:52:46.804325
# Unit test for function jenkins
def test_jenkins():
    branch = "master"
    branch_name = os.environ.get("BRANCH_NAME") or os.environ.get("GIT_BRANCH")

    def mock_os_environ_jenkins(branch_name, branch):
        os.environ["JENKINS_URL"] = "http://jenkins.com"
        os.environ["BRANCH_NAME"] = branch_name
        os.environ["CHANGE_ID"] = ""

    mock_os_environ_jenkins(branch_name, branch)

    jenkins(branch)

    branch_name = "develop"
    branch = "master"


# Generated at 2022-06-14 04:53:17.579858
# Unit test for function semaphore
def test_semaphore():
    os.environ['SEMAPHORE'] = 'true'
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'

    semaphore('master')
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'failed'

    try:
        semaphore('master')
    except CiVerificationError:
        # Pass the test
        pass
    else:
        assert False, "Should have raised an exception"

# Generated at 2022-06-14 04:53:22.031143
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")

# Generated at 2022-06-14 04:53:23.076198
# Unit test for function semaphore
def test_semaphore():
    assert semaphore("master")

# Generated at 2022-06-14 04:53:25.998750
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "develop"

    frigg("develop")



# Generated at 2022-06-14 04:53:32.698793
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "release"
    os.environ["FRIGG_PULL_REQUEST"] = "true"
    assert not frigg("release")

    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    assert not frigg("release")

    os.environ["FRIGG_PULL_REQUEST"] = False
    assert frigg("master")


# Generated at 2022-06-14 04:53:41.060665
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    bitbucket("master")
    assert True
    os.environ["BITBUCKET_BRANCH"] = "branch"
    bitbucket("master")
    assert False
    del os.environ["BITBUCKET_BRANCH"]

    os.environ["BITBUCKET_PR_ID"] = "1"
    bitbucket("master")
    assert False
    del os.environ["BITBUCKET_PR_ID"]
    bitbucket("master")
    assert True


# Generated at 2022-06-14 04:53:46.909586
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "123"
    try:
        frigg("master")
    except CiVerificationError as e:
        assert "Failed verification for frigg environment." in str(e)
    finally:
        os.environ.pop("FRIGG")
        os.environ.pop("FRIGG_BUILD_BRANCH")
        os.environ.pop("FRIGG_PULL_REQUEST")


# Generated at 2022-06-14 04:53:50.582175
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis("master")

# Generated at 2022-06-14 04:53:51.933597
# Unit test for function semaphore
def test_semaphore():
    assert semaphore("master")

# Generated at 2022-06-14 04:53:54.448582
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = ""

    gitlab("master")



# Generated at 2022-06-14 04:54:58.840393
# Unit test for function frigg
def test_frigg():
    """
    Test the frigg CI checks.
    """
    # Test passed check
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    assert frigg("master") is True
    # Test failed check
    os.environ["FRIGG_BUILD_BRANCH"] = "wrong-branch"
    os.environ["FRIGG_PULL_REQUEST"] = "true"
    assert frigg("master") is False
    # Test environment check
    del os.environ["FRIGG"]
    assert frigg("master") is False



# Generated at 2022-06-14 04:55:00.426151
# Unit test for function circle
def test_circle():
    """
    Function for testing circle
    """
    circle("master")

# Generated at 2022-06-14 04:55:11.240843
# Unit test for function check
def test_check():
    """test check function :
    - raise assertion error if the branch is not the right one
    - don't raise exception if the branch is the right one
    """
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "not_master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    try:
        check()
        assert False
    except CiVerificationError:
        assert True
    os.environ["TRAVIS_BRANCH"] = "master"
    try:
        check()
        assert True
    except CiVerificationError:
        assert False
    del os.environ["TRAVIS"]
    del os.environ["TRAVIS_BRANCH"]