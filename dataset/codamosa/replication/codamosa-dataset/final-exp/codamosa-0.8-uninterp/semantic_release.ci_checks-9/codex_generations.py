

# Generated at 2022-06-14 04:45:18.693183
# Unit test for function check
def test_check():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS"] = "true"
    assert check() == True
    del os.environ["TRAVIS"]

    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "false"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ["SEMAPHORE"] = "true"
    assert check() == True
    del os.environ["SEMAPHORE"]

    os.environ["FRIGG_BUILD_BRANCH"] = "master"

# Generated at 2022-06-14 04:45:24.781235
# Unit test for function checker
def test_checker():
    from semantic_release.errors import CiVerificationError

    @checker
    def assertion_error():
        raise AssertionError("test")

    try:
        assertion_error()
    except CiVerificationError:
        pass
    else:
        assert False, "checker did not wrap function properly"

# Generated at 2022-06-14 04:45:34.525452
# Unit test for function jenkins
def test_jenkins():
    # test if function mantains the value, if function is called normally
    os.environ["JENKINS_URL"] = "Testvalue"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = None
    check("master")
    assert os.environ["JENKINS_URL"] == "Testvalue"
    assert os.environ["BRANCH_NAME"] == "master"
    assert os.environ["GIT_BRANCH"] == "master"
    assert os.environ["CHANGE_ID"] is None

    # test if function mantains the value, if function is called normally
    os.environ["JENKINS_URL"] = "Testvalue"
    os

# Generated at 2022-06-14 04:45:36.419440
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"

    check("master")
    assert True

# Generated at 2022-06-14 04:45:40.216771
# Unit test for function frigg
def test_frigg():
    branch = "master"
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = branch
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    frigg(branch)

# Generated at 2022-06-14 04:45:43.670568
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    assert travis("master") == True
    del os.environ["FRIGG"]


# Generated at 2022-06-14 04:45:46.337047
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket("master")

# Generated at 2022-06-14 04:45:48.086093
# Unit test for function circle
def test_circle():
    assert circle(branch="master")
    assert circle(branch="v1.6.3")

# Generated at 2022-06-14 04:45:51.854647
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    semaphore("master")
    assert True



# Generated at 2022-06-14 04:45:56.067110
# Unit test for function jenkins
def test_jenkins():
    assert os.environ["JENKINS_URL"] == "foo"
    assert os.environ["BRANCH_NAME"] == "foobar"
    assert os.environ["CHANGE_ID"] == "foobar"
    assert jenkins("foobar")

# Generated at 2022-06-14 04:46:06.181981
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = "true"
    os.environ['CI_PULL_REQUEST'] = "true"
    os.environ['CIRCLE_BRANCH'] = "feature/test"
    try:
        circle("feature/test")
    except AssertionError:
        print("test_circle test failure")

# Generated at 2022-06-14 04:46:16.627698
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "my-branch"
    os.environ["CI_PULL_REQUEST"] = "false"
    assert circle(branch="my-branch")
    os.environ["CIRCLE_BRANCH"] = "other-branch"
    os.environ["CI_PULL_REQUEST"] = "true"

    try:
        circle(branch="my-branch")
        assert falso
    except CiVerificationError as e:
        assert isinstance(e, CiVerificationError)


# Generated at 2022-06-14 04:46:20.449123
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "branch"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis(branch="branch")


# Generated at 2022-06-14 04:46:23.644839
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'https://jenkins.com'
    os.environ['BRANCH_NAME'] = 'master'

    jenkins('master')


# Generated at 2022-06-14 04:46:30.671106
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BUILD_NUMBER'] = '1'
    os.environ['BITBUCKET_BRANCH'] = 'master'
    os.environ['BITBUCKET_PR_ID'] = '0'
    bitbucket()
    del os.environ['BITBUCKET_BUILD_NUMBER']
    del os.environ['BITBUCKET_BRANCH']
    del os.environ['BITBUCKET_PR_ID']

# Generated at 2022-06-14 04:46:33.150032
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    assert check()



# Generated at 2022-06-14 04:46:36.936208
# Unit test for function semaphore
def test_semaphore():
    assert os.environ.get("BRANCH_NAME") == "master"
    assert os.environ.get("PULL_REQUEST_NUMBER") is None
    assert os.environ.get("SEMAPHORE_THREAD_RESULT") != "failed"

# Unit tests for function frigg

# Generated at 2022-06-14 04:46:37.615799
# Unit test for function gitlab
def test_gitlab():
    assert not gitlab("fjalla")



# Generated at 2022-06-14 04:46:40.902204
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CHANGE_ID"] = False
    checker(gitlab)("master")
    del os.environ["CI_COMMIT_REF_NAME"]
    del os.environ["CHANGE_ID"]


# Generated at 2022-06-14 04:46:44.735393
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"]="true"
    os.environ["CI_COMMIT_REF_NAME"]="master"
    check()

# Generated at 2022-06-14 04:46:52.591555
# Unit test for function bitbucket
def test_bitbucket():
    assert bitbucket("master") is not False

# Generated at 2022-06-14 04:47:02.058490
# Unit test for function circle
def test_circle():
    # Set the environment variable to test for
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"

    # Call the function
    check()

    # Verify the exit code is correct.
    assert os.environ.get("CIRCLECI") == "true"
    assert os.environ.get("CIRCLE_BRANCH") == "master"

    # Delete the environment variable
    del os.environ["CIRCLECI"]
    del os.environ["CIRCLE_BRANCH"]


# Generated at 2022-06-14 04:47:05.157945
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = 'master'
    os.environ["BITBUCKET_PR_ID"] = ''
    assert bitbucket('master')



# Generated at 2022-06-14 04:47:12.828454
# Unit test for function frigg
def test_frigg():
    os.environ.update({"FRIGG": "true"})

    for branch in ["master", "develop"]:
        os.environ.update({"FRIGG_BUILD_BRANCH": branch})
        os.environ.update({"FRIGG_PULL_REQUEST": "false"})
        assert frigg(branch) is True

    for branch in ["master", "develop"]:
        os.environ.update({"FRIGG_BUILD_BRANCH": branch})
        os.environ.update({"FRIGG_PULL_REQUEST": "true"})
        try:
            frigg(branch)
        except CiVerificationError as e:
            assert "The verification check for the environment did not pass" in str(e)

# Generated at 2022-06-14 04:47:14.043768
# Unit test for function checker
def test_checker():
    def func():
        assert True
    assert checker(func)()

# Generated at 2022-06-14 04:47:17.410946
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = "master"
    os.environ['TRAVIS_PULL_REQUEST'] = "false"
    travis('master')
    with pytest.raises(CiVerificationError):
        travis('develop')
    travis('develop')

# Generated at 2022-06-14 04:47:26.745552
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "branch1"
    os.environ["CI_PULL_REQUEST"] = "false"
    # Should pass
    circle("branch1")
    # Should fail
    os.environ["CI_PULL_REQUEST"] = "true"
    try:
        circle("branch1")
    except CiVerificationError:
        pass
    else:
        raise Exception("CircleCI check should have failed.")



# Generated at 2022-06-14 04:47:30.355766
# Unit test for function gitlab
def test_gitlab():
    assert gitlab("master") is True
    os.environ.pop("CI_COMMIT_REF_NAME")
    assert gitlab("other") is False
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_TARGET_BRANCH_NAME"] = "master"
    assert gitlab("master") is False

# Generated at 2022-06-14 04:47:31.674262
# Unit test for function semaphore
def test_semaphore():
    assert semaphore("master") is True

# Generated at 2022-06-14 04:47:36.602498
# Unit test for function checker
def test_checker():
    import pytest
    @checker
    def always_fails():
        assert True == False

    with pytest.raises(CiVerificationError):
        always_fails()

    @checker
    def always_works():
        assert True == True

    assert True is always_works()

# Generated at 2022-06-14 04:47:49.946442
# Unit test for function checker
def test_checker():
    def test1():
        raise AssertionError

    def test2():
        pass

    test1 = checker(test1)
    test2 = checker(test2)

    # Test that test1 raises a CiVerificationError
    try:
        test1()
    except CiVerificationError:
        pass
    else:
        raise AssertionError

    # Test that test2 returns True
    assert test2() is True

# Generated at 2022-06-14 04:47:56.104621
# Unit test for function circle
def test_circle():
    """
    Unit test for function circle.
    """
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    circle("master")
    os.environ["CIRCLE_BRANCH"] = "develop"
    try:
        circle("master")
        assert False
    except CiVerificationError:
        assert True



# Generated at 2022-06-14 04:48:01.606505
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = "master"
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = "success"
    semaphore("master")
    assert True

# Generated at 2022-06-14 04:48:09.724994
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = 'test'
    os.environ['BRANCH_NAME'] = 'master'
    check()
    os.environ['BRANCH_NAME'] = 'dummy'
    check()
    os.environ['GIT_BRANCH'] = 'master'
    check()
    os.environ['GIT_BRANCH'] = 'dummy'
    check()



# Generated at 2022-06-14 04:48:12.441761
# Unit test for function check
def test_check():
    assert check(branch="master") == None
    assert check(branch="develop") == None
    assert check(branch="release/0.1.0") == None

# Generated at 2022-06-14 04:48:13.298800
# Unit test for function circle
def test_circle():
    assert circle("master")



# Generated at 2022-06-14 04:48:21.545163
# Unit test for function jenkins
def test_jenkins():
    os.environ['JENKINS_URL'] = "https://jenkins.example.com/"
    os.environ['BRANCH_NAME'] = "build_branch"
    os.environ['CHANGE_ID'] = "12345"
    with pytest.raises(CiVerificationError):
        jenkins("build_branch")
    os.environ['CHANGE_ID'] = ""
    jenkins("build_branch")

# Generated at 2022-06-14 04:48:27.043394
# Unit test for function checker
def test_checker():
    """Testing checker"""
    def func_succeed():
        assert True

    def func_fail():
        assert False

    def func_custom_exception():
        raise ValueError('This is an exception')

    func_succeed_wrapper = checker(func_succeed)
    func_fail_wrapper = checker(func_fail)
    func_exception_wrapper = checker(func_custom_exception)

    assert func_succeed_wrapper()
    assert func_fail_wrapper()
    assert func_exception_wrapper()

# Generated at 2022-06-14 04:48:31.764540
# Unit test for function checker
def test_checker():
    @checker
    def my_function():
        raise AssertionError("not the same")

    try:
        my_function()
        assert False, "should raise exception"
    except CiVerificationError as e:
        assert str(e) == "The verification check for the environment did not pass."

# Generated at 2022-06-14 04:48:38.731010
# Unit test for function check
def test_check():
    # Set environment variable
    os.environ["TRAVIS"] = "true"
    os.environ["SEMAPHORE"] = "true"
    os.environ["FRIGG"] = "true"
    os.environ["CIRCLECI"] = "true"
    os.environ["GITLAB_CI"] = "true"
    os.environ["JENKINS_URL"] = "localhost:8080"
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["BRANCH_NAME"] = "master"

# Generated at 2022-06-14 04:48:49.354061
# Unit test for function bitbucket
def test_bitbucket():
    """
    Test for function bitbucket
    """
    os.environ["BITBUCKET_BRANCH"] = "BITBUCKET_BRANCH"
    os.environ["BITBUCKET_PR_ID"] = "BITBUCKET_PR_ID"
    bitbucket("BITBUCKET_BRANCH")

# Generated at 2022-06-14 04:48:53.824151
# Unit test for function checker
def test_checker():
    @checker
    def function():
        assert False

    from semantic_release.errors import CiVerificationError

    try:
        function()
        assert False
    except CiVerificationError:
        assert True


# Generated at 2022-06-14 04:48:56.780427
# Unit test for function gitlab
def test_gitlab():
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "release-0.7"
    check("release-0.7")

# Generated at 2022-06-14 04:48:59.923697
# Unit test for function frigg
def test_frigg():
    branch = "master"

    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = branch
    os.environ["FRIGG_PULL_REQUEST"] = "true"
    check(branch)



# Generated at 2022-06-14 04:49:02.113591
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "23"
    os.environ["BITBUCKET_BRANCH"] = "master"
    bitbucket("master")


# Generated at 2022-06-14 04:49:06.728926
# Unit test for function jenkins
def test_jenkins():
    """Perform a test on function jenkins.
    Function jenkins is the popper of CiVerificationError
    and therefore the test will pass if an assertion error
    is raised.
    """
    os.environ["BRANCH_NAME"] = "abc"
    os.environ["JENKINS_URL"] = "true"
    try:
        jenkins("def")
        assert False
    except CiVerificationError:
        os.environ.pop("BRANCH_NAME")
        os.environ.pop("JENKINS_URL")
        assert True

# Generated at 2022-06-14 04:49:12.271157
# Unit test for function checker
def test_checker():
    def func(msg):
        assert 0, msg

    wrapper = checker(func)

    try:
        wrapper("foo")
    except CiVerificationError as exc:
        assert "verification check for the environment did not pass" == str(exc)
    else:
        assert False, "CiVerificationError not raised"

    def func():
        pass
    wrapper = checker(func)
    assert True is wrapper()

# Generated at 2022-06-14 04:49:17.247863
# Unit test for function checker
def test_checker():
    @checker
    def ok():
        pass

    @checker
    def nok():
        assert False

    @checker
    def exc():
        raise AssertionError

    ok()

    try:
        nok()
        assert False
    except CiVerificationError:
        pass

    try:
        exc()
        assert False
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:49:29.252653
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "123"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PULLREQUEST_ID"] = "123"
    try:
        bitbucket("master")
    except CiVerificationError:
        assert True
    except Exception:
        assert False
    try:
        bitbucket("xxx")
    except CiVerificationError:
        assert True
    except Exception:
        assert False
    try:
        os.environ["BITBUCKET_PULLREQUEST_ID"] = None
        bitbucket("master")
    except CiVerificationError:
        assert False
    except Exception:
        assert False

# Generated at 2022-06-14 04:49:35.317152
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = ""
    try:
        check()
    except CiVerificationError:
        pass


# Generated at 2022-06-14 04:49:48.058344
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://jenkins.com"
    os.environ["BRANCH_NAME"] = "master"
 
    assert check() is None
 
    os.environ["BRANCH_NAME"] = "release/v2.0.0"
    assert check() is None
 
    os.environ["BRANCH_NAME"] = "release/v2.0.0"
    os.environ["CHANGE_ID"] = "some_number"
    assert check() == False
 
    os.environ["BRANCH_NAME"] = "release/v2.0.0"
    os.environ["CHANGE_ID"] = "some_number"
    assert check() == False

# Generated at 2022-06-14 04:49:50.746648
# Unit test for function gitlab
def test_gitlab():
    """
    Tests the gitlab function.
    """
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    gitlab("master")



# Generated at 2022-06-14 04:49:55.684346
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"

    try:
        travis("master")
    except CiVerificationError:
        assert False, 'test_travis() failed!'


# Generated at 2022-06-14 04:50:01.406181
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = None

    check()
    del os.environ["CIRCLECI"]
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CI_PULL_REQUEST"]

# Generated at 2022-06-14 04:50:07.911931
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://jenkins.com/"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = "1"
    jenkins("master")  # should raise an exception
    os.environ["CHANGE_ID"] = ""
    jenkins("master")  # should not raise an exception

# Generated at 2022-06-14 04:50:17.876121
# Unit test for function gitlab
def test_gitlab():
    """
    Tests gitlab's environment checks.
    """
    # Test GITLAB_CI=true, BRANCH_NAME=master, CI_MERGE_REQUEST_ID=null
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_ID"] = ""
    del os.environ["CI_MERGE_REQUEST_IID"]  # Not null
    check()

    # Test GITLAB_CI=true, BRANCH_NAME=non_master, CI_MERGE_REQUEST_ID=null
    os.environ["GITLAB_CI"] = "true"

# Generated at 2022-06-14 04:50:20.670407
# Unit test for function travis
def test_travis():
    os.environ.update({"TRAVIS_BRANCH": "master", "TRAVIS_PULL_REQUEST": "false"})
    check()



# Generated at 2022-06-14 04:50:25.236990
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    check()
    del os.environ["CIRCLECI"]
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CI_PULL_REQUEST"]


# Generated at 2022-06-14 04:50:28.256557
# Unit test for function checker
def test_checker():
    @checker
    def failure_func():
        raise AssertionError("failure_func")
    
    @checker
    def success_func():
        pass
    
    try:
        failure_func()
    except CiVerificationError:
        pass
    else:
        assert False, "Should have raised a CiVerificationError"
    
    success_func()

# Generated at 2022-06-14 04:50:33.482610
# Unit test for function frigg
def test_frigg():
    branch = "test"
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = branch
    del os.environ["FRIGG_PULL_REQUEST"]
    frigg(branch)



# Generated at 2022-06-14 04:50:46.506039
# Unit test for function travis
def test_travis():
    """Tests the travis checker
    """
    # This is a travis environment
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS_BRANCH"] = "master"

    # The travis checker should not raise any errors
    travis("master")



# Generated at 2022-06-14 04:50:52.894437
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"

    semaphore(branch="master")
    del os.environ["BRANCH_NAME"]
    del os.environ["PULL_REQUEST_NUMBER"]
    del os.environ["SEMAPHORE_THREAD_RESULT"]

    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"


# Generated at 2022-06-14 04:50:57.195082
# Unit test for function jenkins
def test_jenkins():
    try:
        jenkins("master")
    except CiVerificationError:
        pass
    else:
        raise Exception("Jenkins CI should have failed check")
    os.environ["JENKINS_URL"] = "jenkins.example.com"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    jenkins("master")

# Generated at 2022-06-14 04:50:57.966941
# Unit test for function check
def test_check():
    check("master")

# Generated at 2022-06-14 04:51:00.701209
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "true"
    os.environ["GIT_BRANCH"] = "master"
    check()



# Generated at 2022-06-14 04:51:06.456672
# Unit test for function checker
def test_checker():
    """Test the checker by asserting that the wrapped function raises a CiVerificationError instead of AssertionError"""
    @checker
    def fail():
        assert False
    try:
        fail()
    except CiVerificationError:
        return
    raise Exception("checker decorator isn't working")

# Generated at 2022-06-14 04:51:15.668133
# Unit test for function checker
def test_checker():
    """
    Unit test for function checker.
    """
    def test_success_check():
        """
        A successful check.
        """
        assert 1 == 1

    def test_failed_check():
        """
        A failed check.
        """
        assert 1 == 0  # pylint: disable=C0123

    test_success_check = checker(test_success_check)
    test_failed_check = checker(test_failed_check)

    test_success_check()
    try:
        test_failed_check()
    except CiVerificationError as error:
        assert str(error) == "The verification check for the environment did not pass."
    else:
        assert False

# Generated at 2022-06-14 04:51:27.065546
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "testing_branch"
    os.environ["JENKINS_URL"] = "test"
    os.environ["CHANGE_ID"] = "test"
    try:
        jenkins(os.environ["BRANCH_NAME"])
        assert False
    except CiVerificationError as e:
        assert "The verification check for the environment did not pass." in str(e)
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "test"
    os.environ["CHANGE_ID"] = "test"

# Generated at 2022-06-14 04:51:30.167543
# Unit test for function checker

# Generated at 2022-06-14 04:51:36.811860
# Unit test for function frigg
def test_frigg():
    env = {
        'FRIGG_BUILD_BRANCH': 'bugfix/1',
        'FRIGG_PULL_REQUEST': 'True',
    }

    def test_frigg(branch):
        return frigg(branch)

    assert not test_frigg('master')

    env = {
        'FRIGG_BUILD_BRANCH': 'master',
        'FRIGG_PULL_REQUEST': 'False',
    }

    def test_frigg(branch):
        return frigg(branch)

    assert test_frigg('master')



# Generated at 2022-06-14 04:51:45.922513
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    bitbucket(branch="master")

# Generated at 2022-06-14 04:51:49.245128
# Unit test for function gitlab
def test_gitlab():
    os.environ['GITLAB_CI'] = "true"
    os.environ['CI_COMMIT_REF_NAME'] = "master"
    check()

# Generated at 2022-06-14 04:51:53.713166
# Unit test for function bitbucket
def test_bitbucket():
    branch: str = "master"
    os.environ["BITBUCKET_BRANCH"] = branch
    del os.environ["BITBUCKET_PR_ID"]

    bitbucket(branch)



# Generated at 2022-06-14 04:52:02.431711
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = "true"
    os.environ['CIRCLE_BRANCH'] = "master"
    try:
        circle("master")
    except CiVerificationError:
        assert False

    #should trigger error
    os.environ['CI_PULL_REQUEST'] = "123"
    try:
        circle("master")
        assert False
    except CiVerificationError:
        assert True
    os.environ['CI_PULL_REQUEST'] = None

    #should trigger error
    os.environ['CIRCLE_BRANCH'] = "develop"
    try:
        circle("master")
        assert False
    except CiVerificationError:
        assert True



# Generated at 2022-06-14 04:52:07.423031
# Unit test for function bitbucket
def test_bitbucket():
    """
    Mock environment variables required to verify bitbucket is the current CI.
    """
    os.environ["BITBUCKET_BRANCH"] = "master"
    assert "BITBUCKET_BUILD_NUMBER" in os.environ
    check()



# Generated at 2022-06-14 04:52:13.757519
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()
    os.environ["TRAVIS_BRANCH"] = "master2"
    os.environ["TRAVIS_PULL_REQUEST"] = "falsed"
    try:
        check()
    except CiVerificationError:
        # expected exception
        pass


# Generated at 2022-06-14 04:52:15.039512
# Unit test for function check
def test_check():
    """Unit tests for function check."""
    assert check()

# Generated at 2022-06-14 04:52:17.374035
# Unit test for function bitbucket
def test_bitbucket():
    assert bitbucket("master")
    try:
        bitbucket("newbranch")
    except CiVerificationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:52:25.381605
# Unit test for function frigg
def test_frigg():
    from unittest.mock import patch
    with patch.dict(os.environ, {"FRIGG": "true", "FRIGG_BUILD_BRANCH": "master"}):
        frigg("master")
    with patch.dict(os.environ, {"FRIGG": "true", "FRIGG_BUILD_BRANCH": "develop"}):
        with pytest.raises(CiVerificationError):
            frigg("master")
    with patch.dict(
        os.environ,
        {"FRIGG": "true", "FRIGG_BUILD_BRANCH": "master", "FRIGG_PULL_REQUEST": "true"},
    ):
        with pytest.raises(CiVerificationError):
            frigg("master")

# Generated at 2022-06-14 04:52:28.280340
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = "master"
    os.environ['TRAVIS_PULL_REQUEST'] = "false"
    check()


# Generated at 2022-06-14 04:52:42.347744
# Unit test for function gitlab
def test_gitlab():
    assert os.environ.get("GITLAB_CI") == "true"
    assert os.environ.get("CI_COMMIT_REF_NAME") == "master"
    assert not os.environ.get("CI_MERGE_REQUEST_IID")

# Generated at 2022-06-14 04:52:51.180906
# Unit test for function semaphore
def test_semaphore():
    os.environ['SEMAPHORE'] = "true"
    assert semaphore("master") is True
    assert semaphore("a") is True
    os.environ['BRANCH_NAME'] = "master"
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = "passed"
    assert semaphore("master") is True
    assert semaphore("a") is False



# Generated at 2022-06-14 04:52:54.756459
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    check()


# Generated at 2022-06-14 04:52:59.915925
# Unit test for function frigg
def test_frigg():
    assert os.environ["FRIGG_CI_WORKER_NAME"] == "SomeWorker"
    assert os.environ["FRIGG_BUILD_BRANCH"] == "master"
    assert not os.environ["FRIGG_PULL_REQUEST"]
    frigg("master")


# Generated at 2022-06-14 04:53:01.365284
# Unit test for function check
def test_check():
    """
    Runs tests
    """
    assert check("branch")

# Generated at 2022-06-14 04:53:06.204008
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    semaphore(branch="master")

# Generated at 2022-06-14 04:53:11.239706
# Unit test for function jenkins
def test_jenkins():
    # Set a Jenkins environment variable
    os.environ["JENKINS_URL"] = "https://jenkins.com"
    os.environ["BRANCH_NAME"] = "master"
    check()
    # Resetting
    os.environ.pop("JENKINS_URL")
    os.environ.pop("BRANCH_NAME")


# Generated at 2022-06-14 04:53:13.279850
# Unit test for function bitbucket
def test_bitbucket():
    branch_name = "master"
    check(branch_name)

# Generated at 2022-06-14 04:53:16.904115
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    circle("master")



# Generated at 2022-06-14 04:53:29.938160
# Unit test for function jenkins
def test_jenkins():
    import os

    # generate an environment
    os.environ["JENKINS_URL"] = "http://jenkins.io/"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = ""
    jenkins("master")

    # test with not being on the master branch
    os.environ["GIT_BRANCH"] = "not-master"
    os.environ["CHANGE_ID"] = ""
    try:
        jenkins("master")
        assert False
    except CiVerificationError:
        pass

    # test with CHANGE_ID being set
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = "1234"

# Generated at 2022-06-14 04:53:54.479437
# Unit test for function jenkins
def test_jenkins():
    """
    Unit test for function jenkins
    """

    os.environ["JENKINS_URL"] = "https://jenkins.io"
    os.environ["GIT_BRANCH"] = "branch"
    with pytest.raises(CiVerificationError):
        jenkins("master")
    os.environ["GIT_BRANCH"] = "master"
    jenkins("master")
    os.environ["BRANCH_NAME"] = "branch"
    with pytest.raises(CiVerificationError):
        jenkins("master")
    os.environ["BRANCH_NAME"] = "master"
    jenkins("master")
    os.environ["CHANGE_ID"] = "pull_request_id"

# Generated at 2022-06-14 04:54:00.546371
# Unit test for function checker
def test_checker():
    def test_function():
        raise AssertionError

    test_function = checker(test_function)

    try:
        test_function()
    except CiVerificationError as exc:
        assert str(exc) == "The verification check for the environment did not pass."
    except AssertionError:
        assert False

# Generated at 2022-06-14 04:54:03.466060
# Unit test for function jenkins
def test_jenkins():
    # Assume successful
    assert jenkins("master")
    # Assume unsuccessful
    os.environ["JENKINS_URL"] = None
    assert jenkins("master") == False

# Generated at 2022-06-14 04:54:06.427434
# Unit test for function checker
def test_checker():
    @checker
    def test_func():
        assert False

    try:
        test_func()
        assert False
    except CiVerificationError:
        assert True

# Generated at 2022-06-14 04:54:06.955362
# Unit test for function circle
def test_circle():
    circle("circle")

# Generated at 2022-06-14 04:54:17.373437
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    os.environ["CI_MERGE_REQUEST_IID"] = "1"
    try:
        gitlab("master")
    except CiVerificationError as e:
        assert(True)
    else:
        assert(False)
    del os.environ["CI_COMMIT_REF_NAME"]
    del os.environ["CI_MERGE_REQUEST_IID"]

    try:
        gitlab("master")
    except CiVerificationError as e:
        assert(False)


# Generated at 2022-06-14 04:54:23.375666
# Unit test for function semaphore
def test_semaphore():
    env_map = {
        "PULL_REQUEST_NUMBER": None,
        "BRANCH_NAME": "test_branch",
        "SEMAPHORE_THREAD_RESULT": "passed",
    }

    env = os.environ
    os.environ = env_map
    semaphore("test_branch")
    os.environ = env



# Generated at 2022-06-14 04:54:25.058980
# Unit test for function jenkins
def test_jenkins():
    result = os.environ.get("JENKINS_URL") is not None
    assert result

# Generated at 2022-06-14 04:54:30.848374
# Unit test for function check
def test_check():
    """
    Ensure travis checks work
    """
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "dev"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check("master")

# Generated at 2022-06-14 04:54:36.319797
# Unit test for function travis
def test_travis():
    """
    We need to try every possible combination and make sure that we have
    tested them all

    :return: None
    """
    env = {
        "TRAVIS_BRANCH": "master",
        "TRAVIS_PULL_REQUEST": "false",
        "TRAVIS": "true",
    }
    with env_vars(env):
        travis("master")



# Generated at 2022-06-14 04:54:56.459453
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = "master"
    assert bitbucket("master")
    os.environ['BITBUCKET_PR_ID'] = "True"
    assert not bitbucket("master")
    del os.environ['BITBUCKET_BRANCH']
    assert not bitbucket("master")
    del os.environ['BITBUCKET_PR_ID']


# Generated at 2022-06-14 04:55:00.827475
# Unit test for function gitlab
def test_gitlab():
    os.environ['GITLAB_CI'] = "true"
    os.environ['CI_COMMIT_REF_NAME'] = "master"
    os.environ['CI_MERGE_REQUEST_IID'] = ""
    check()

