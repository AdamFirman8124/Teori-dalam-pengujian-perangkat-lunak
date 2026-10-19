

# Generated at 2022-06-14 04:45:13.938253
# Unit test for function semaphore
def test_semaphore():
    func = semaphore
    assert func(branch = 'master') == True


# Generated at 2022-06-14 04:45:18.263671
# Unit test for function circle
def test_circle():
    os.environ.update({'CIRCLECI': 'true', 'CI_PULL_REQUEST': None, 'CIRCLE_BRANCH': 'master'})
    assert circle(branch='master')
    os.environ['CI_PULL_REQUEST'] = 'true'
    try:
        circle(branch='master')
        assert False
    except CiVerificationError:
        pass



# Generated at 2022-06-14 04:45:30.527257
# Unit test for function jenkins
def test_jenkins():
    # Set environment variables
    # This function should not raise errors
    os.environ["JENKINS_URL"] = "jenkins.com"
    os.environ["BRANCH_NAME"] = "master"

    # Reset environment variables
    del os.environ["JENKINS_URL"]
    del os.environ["BRANCH_NAME"]

    # Set environment variables
    # This function should raise errors
    os.environ["JENKINS_URL"] = "jenkins.com"
    os.environ["BRANCH_NAME"] = "not master"
    os.environ["CHANGE_ID"] = "1"

    # Reset environment variables
    del os.environ["JENKINS_URL"]
    del os.environ["BRANCH_NAME"]

# Generated at 2022-06-14 04:45:34.518873
# Unit test for function travis
def test_travis():
    branch="master"
    os.environ.clear()
    os.environ["TRAVIS_BRANCH"] = branch
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    travis(branch)


# Generated at 2022-06-14 04:45:41.490487
# Unit test for function gitlab
def test_gitlab():
    '''
    Test for the function gitlab
    '''
    os.environ["GITLAB_CI"] = "true"
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    assert gitlab(branch="master") is True
    os.environ["CI_COMMIT_REF_NAME"] = "master1"
    assert gitlab(branch="master") is False

# Generated at 2022-06-14 04:45:46.843773
# Unit test for function semaphore
def test_semaphore():
    os.environ['SEMAPHORE'] = 'true'
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'sucess'
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['BRANCH_NAME'] = 'master'
    assert check() is True
    assert check("master1") is False

# Generated at 2022-06-14 04:45:57.906968
# Unit test for function check
def test_check():
    # Fix the branch name
    branch = "master-test"

    # Fix the function name
    function = "frigg"
    # Fix the environment variable
    environment_vars = {
        "FRIGG": "true",
        "FRIGG_BUILD_BRANCH": branch,
        "FRIGG_PULL_REQUEST": "false"
    }

    # Loop over all environment variables and set it
    for key, value in environment_vars.items():
        os.environ[key] = value

    # Call the function check
    check(branch)

    # Remove the environment variables
    for key in environment_vars.keys():
        os.environ.pop(key)

    # Check if the function was called
    assert function in globals()


# Generated at 2022-06-14 04:46:03.691262
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "blah"
    os.environ["BITBUCKET_BRANCH"] = "master"
    bitbucket("master")
    os.environ["BITBUCKET_BRANCH"] = "dev"
    try:
        bitbucket("master")
    except CiVerificationError:
        pass
    os.environ["BITBUCKET_PR_ID"] = "123"
    try:
        bitbucket("master")
    except CiVerificationError:
        pass



# Generated at 2022-06-14 04:46:10.974087
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    frigg("master")
    assert os.environ.get("FRIGG_BUILD_BRANCH") == "master"
    assert os.environ.get("FRIGG_PULL_REQUEST") == "false"


# Generated at 2022-06-14 04:46:15.070717
# Unit test for function circle
def test_circle():
    os.environ['CIRCLECI'] = 'true'
    os.environ['CIRCLE_BRANCH'] = 'master'
    check('master')
    del os.environ['CIRCLECI']

# Generated at 2022-06-14 04:46:27.925206
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master")



# Generated at 2022-06-14 04:46:28.839995
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    check()

# Generated at 2022-06-14 04:46:33.277220
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"

    travis(branch="master")
    del os.environ["TRAVIS_BRANCH"]
    del os.environ["TRAVIS_PULL_REQUEST"]



# Generated at 2022-06-14 04:46:41.106755
# Unit test for function jenkins
def test_jenkins():
    assert checker(jenkins)("branch-name")
    os.environ["BRANCH_NAME"] = "branch-name"
    os.environ["GIT_BRANCH"] = "branch-name"
    os.environ["JENKINS_URL"] = "https://ci.example.com"
    assert checker(jenkins)("branch-name")
    del os.environ["JENKINS_URL"]
    assert not checker(jenkins)("branch-name")
    os.environ["JENKINS_URL"] = "https://ci.example.com"
    assert not checker(jenkins)("master")
    os.environ["JENKINS_URL"] = "https://ci.example.com"

# Generated at 2022-06-14 04:46:49.075554
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS'] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    
    branch = "master"
    
    try:
        check(branch)
    except:
        print(1)
    else:
        print(0)
        
if __name__ == '__main__':
    test_travis()

# Generated at 2022-06-14 04:46:58.814672
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["JENKINS_URL"] = "1"
    os.environ["CHANGE_ID"] = ""
    assert check()

    os.environ["JENKINS_URL"] = "1"
    os.environ["CHANGE_ID"] = "1"
    assert check() == False

    os.environ["JENKINS_URL"] = ""
    os.environ["CHANGE_ID"] = ""
    assert check() == False

# Generated at 2022-06-14 04:47:05.200664
# Unit test for function bitbucket
def test_bitbucket():
    """
    Performs a unit test for the checks performed by the bitbucket
    checker.
    """
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1"
    assert check()
    del os.environ["BITBUCKET_BUILD_NUMBER"]
    del os.environ["BITBUCKET_BRANCH"]
    assert check() is None

# Generated at 2022-06-14 04:47:08.994948
# Unit test for function check
def test_check():
    os.environ[
        "TRAVIS_BRANCH"
    ] = "master"  # type: ignore[var-annotated] # noqa: F821
    os.environ[
        "TRAVIS_PULL_REQUEST"
    ] = "false"  # type: ignore[var-annotated] # noqa: F821
    check()

# Generated at 2022-06-14 04:47:17.439558
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"

    check()
    os.environ["TRAVIS_BRANCH"] = "not master"
    try:
        check()
        assert False
    except CiVerificationError:
        assert True
        del os.environ["TRAVIS_BRANCH"]

    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        check()
        assert False
    except CiVerificationError:
        assert True

    del os.environ["TRAVIS_PULL_REQUEST"]
    del os.environ["TRAVIS"]

# Generated at 2022-06-14 04:47:28.925225
# Unit test for function check
def test_check():
    """
    Unit test for check function

    :return:
    """
    # The branch to check
    branch = "master"
    # Environment for all the test cases

# Generated at 2022-06-14 04:47:40.877930
# Unit test for function checker
def test_checker():
    # pylint: disable=unused-argument
    @checker
    def test_func(arg1, arg2=1):
        assert True
        return True
    assert test_func(1)
    try:
        assert test_func(1, 2)
    except CiVerificationError:
        assert True
    return

# Generated at 2022-06-14 04:47:42.788287
# Unit test for function checker
def test_checker():
    @checker
    def dummy_function():
        raise AssertionError

    dummy_function()

# Generated at 2022-06-14 04:47:50.645419
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ["SEMAPHORE_THREAD_COUNT"] = "1"
    semaphore(branch="master")

# Generated at 2022-06-14 04:47:54.637288
# Unit test for function bitbucket
def test_bitbucket():
    """
    Unit tests for bitbucket

    """
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = None
    check()



# Generated at 2022-06-14 04:48:01.532207
# Unit test for function semaphore
def test_semaphore():
    @checker
    def semaphore(branch: str):
        assert os.environ.get("BRANCH_NAME") == branch
        assert os.environ.get("PULL_REQUEST_NUMBER") is None
        assert os.environ.get("SEMAPHORE_THREAD_RESULT") != "failed"

    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = ''
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    semaphore('master')

    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = 'true'

# Generated at 2022-06-14 04:48:04.130645
# Unit test for function gitlab
def test_gitlab():
    os.environ['GITLAB_CI'] = "true"
    os.environ['CI_COMMIT_REF_NAME'] = "master"
    assert check()

# Generated at 2022-06-14 04:48:11.058263
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""

    bitbucket( "master" )

    del os.environ["BITBUCKET_BRANCH"]
    del os.environ["BITBUCKET_PR_ID"]

# Generated at 2022-06-14 04:48:17.889749
# Unit test for function travis
def test_travis():
    os.environ['TRAVIS_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    travis('master')
    os.environ['TRAVIS_BRANCH'] = 'unknown'
    with pytest.raises(CiVerificationError):
        travis('master')



# Generated at 2022-06-14 04:48:23.234852
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "test_url"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = "1234"

    jenkins("master")
    assert True

    del os.environ["CHANGE_ID"]

    jenkins("master")
    assert True

    os.environ["BRANCH_NAME"] = "develop"

    try:
        jenkins("master")
        assert False
    except CiVerificationError:
        assert True

    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = "1234"

    try:
        jenkins("master")
        assert False
    except CiVerificationError:
        assert True

   

# Generated at 2022-06-14 04:48:26.484467
# Unit test for function bitbucket
def test_bitbucket():
    env = "BITBUCKET_BUILD_NUMBER"
    assert env in os.environ

# Generated at 2022-06-14 04:48:44.896222
# Unit test for function jenkins
def test_jenkins():
    """Test that jenkins runs properly."""
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "jenkins"
    os.environ["CHANGE_ID"] = "pull_id"
    try:
        jenkins()
    except CiVerificationError:
        pass
    else:
        assert False
    del os.environ["CHANGE_ID"]
    os.environ["GIT_BRANCH"] = "master"
    try:
        jenkins()
    except CiVerificationError:
        assert False
    del os.environ["BRANCH_NAME"]
    del os.environ["GIT_BRANCH"]
    del os.environ["JENKINS_URL"]

# Generated at 2022-06-14 04:48:45.868492
# Unit test for function semaphore
def test_semaphore():
    assert semaphore(branch='master') == True

# Generated at 2022-06-14 04:48:55.185354
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "some_build_num"
    os.environ["BITBUCKET_BRANCH"] = "some_branch"
    bitbucket("some_branch")

    os.environ["BITBUCKET_BRANCH"] = "some_branch"
    os.environ["BITBUCKET_PR_ID"] = "some_pr_id"
    try:
        bitbucket("some_branch")
    except CiVerificationError as e:
        assert type(e) is CiVerificationError

# Generated at 2022-06-14 04:48:59.120449
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    bitbucket(branch="master")
    os.environ["BITBUCKET_BRANCH"] = "develop"
    bitbucket(branch="develop")
    del os.environ["BITBUCKET_BRANCH"]
    


# Generated at 2022-06-14 04:49:11.358139
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    # Semaphore with no pull request
    assert semaphore(branch = "master")

    os.environ["PULL_REQUEST_NUMBER"] = "10"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    # Semaphore with pull request is running on pull request
    # and the test failed

# Generated at 2022-06-14 04:49:15.042581
# Unit test for function checker
def test_checker():
    func = checker(lambda: 1)
    assert func()

    func = checker(lambda: 2/0)
    try:
        func()
    except CiVerificationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:49:20.805007
# Unit test for function jenkins
def test_jenkins():
    """
    Unit testing for jenkins variables.
    """
    os.environ["BRANCH_NAME"] = "mybranch"
    os.environ["JENKINS_URL"] = "http://example.org"
    os.environ["CHANGE_ID"] = "51"
    jenkins(branch="mybranch")

    os.environ["GIT_BRANCH"] = "mybranch"
    os.environ["JENKINS_URL"] = "http://example.org"
    os.environ["CHANGE_ID"] = "51"
    jenkins(branch="mybranch")

# Generated at 2022-06-14 04:49:26.478614
# Unit test for function semaphore
def test_semaphore():
    """
    Unit test for function semaphore
    """
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "None"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    check(branch="master")


# Generated at 2022-06-14 04:49:31.661772
# Unit test for function checker
def test_checker():
    def stub_function():
        raise AssertionError("This is a test exception.")

    try:
        stub_function()
    except AssertionError:
        pass
    else:
        assert False, "AssertionError should have been raised."

    wrapped_function = checker(stub_function)

    try:
        wrapped_function()
    except CiVerificationError:
        pass
    else:
        assert False, "CiVerificationError should have been raised."

# Generated at 2022-06-14 04:49:35.414536
# Unit test for function bitbucket
def test_bitbucket():
    os.environ.update(
        {
            "BITBUCKET_BRANCH": "master",
            "BITBUCKET_PR_ID": None
        }
    )
    bitbucket("master")



# Generated at 2022-06-14 04:49:52.773252
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()

    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    check()

    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    check()

    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    check()

    os.environ["GITLAB_CI"] = "true"

# Generated at 2022-06-14 04:49:54.049920
# Unit test for function check
def test_check():
    assert check(branch='master')

# Generated at 2022-06-14 04:49:58.484991
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = "master"
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = "success"
    semaphore("master")

# Generated at 2022-06-14 04:50:03.050640
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"]="true"
    os.environ["FRIGG_BUILD_BRANCH"]="master"
    os.environ["FRIGG_PULL_REQUEST"]="false"
    frigg('master')
    os.environ["FRIGG_PULL_REQUEST"]="true"
    frigg('master')




# Generated at 2022-06-14 04:50:09.623229
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = 'master'
    os.environ["TRAVIS_PULL_REQUEST"] = 'false'
    try:
        travis('master')
    except CiVerificationError:
        raise Exception("Travis tests failed")
    try:
        travis('dev')
    except CiVerificationError:
        return
    raise Exception("Travis tests failed for non-master branches")

# Generated at 2022-06-14 04:50:16.840257
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BUILD_NUMBER'] = '123456'
    os.environ['BITBUCKET_BRANCH'] = 'PR-32'
    with pytest.raises(CiVerificationError):
        bitbucket("master")

    os.environ['BITBUCKET_BUILD_NUMBER'] = '123456'
    os.environ['BITBUCKET_BRANCH'] = 'master'
    with pytest.raises(AssertionError):
        bitbucket("PR-32")



# Generated at 2022-06-14 04:50:18.637971
# Unit test for function checker
def test_checker():
    """
    TODO: Unit testing for function checker.
    """

# Generated at 2022-06-14 04:50:23.100974
# Unit test for function semaphore
def test_semaphore():
    """
    Test semaphore checker

    """
    os.environ["BRANCH_NAME"] = 'master'
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    semaphore(branch="master")



# Generated at 2022-06-14 04:50:25.540786
# Unit test for function travis
def test_travis():
    assert travis("master")
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("master")

# Generated at 2022-06-14 04:50:32.082513
# Unit test for function semaphore
def test_semaphore():
    env = {
        "BRANCH_NAME": "master",
        "PULL_REQUEST_NUMBER": "123",
        "SEMAPHORE_THREAD_RESULT": "",
    }
    assert semaphore("master", env) is False
    assert semaphore("develop", env) is False
    assert semaphore("master", {**env, "BRANCH_NAME": "develop"}) is False
    assert semaphore("master", {**env, "PULL_REQUEST_NUMBER": None}) is False
    assert semaphore("master", {**env, "SEMAPHORE_THREAD_RESULT": "failed"}) is False
    assert semaphore("master", {**env, "PULL_REQUEST_NUMBER": None}) is False

# Generated at 2022-06-14 04:50:56.412590
# Unit test for function semaphore
def test_semaphore():
    os.environ["SEMAPHORE"] = "true"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "failed"
    os.environ["BRANCH_NAME"] = "wrong_branch"
    os.environ["PULL_REQUEST_NUMBER"] = "1"
    success = True
    try:
        semaphore("master")
    except:
        success = False
    assert success

    os.environ["SEMAPHORE"] = "true"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "1"
    success = True

# Generated at 2022-06-14 04:51:06.505389
# Unit test for function circle
def test_circle():
    del os.environ['CIRCLE_BRANCH']
    os.environ["CIRCLE_BRANCH"] = "fake"
    os.environ["CI_PULL_REQUEST"] = "true"
    try:
        circle("master")
    except CiVerificationError as err:
        assert err.message == "The verification check for the environment did not pass."
    del os.environ['CIRCLE_BRANCH']

    os.environ["CIRCLE_BRANCH"] = "master"
    del os.environ['CI_PULL_REQUEST']
    circle("master")

# Generated at 2022-06-14 04:51:08.558702
# Unit test for function gitlab
def test_gitlab():
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    gitlab("master")
# test_gitlab()



# Generated at 2022-06-14 04:51:12.395938
# Unit test for function checker
def test_checker():
    @checker
    def check_this():
        assert False

    try:
        check_this()
    except CiVerificationError:
        pass
    else:
        raise ValueError("Expected CiVerificationError")

# Generated at 2022-06-14 04:51:15.470091
# Unit test for function check
def test_check():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()

# Generated at 2022-06-14 04:51:17.260337
# Unit test for function jenkins
def test_jenkins():
    assert jenkins() == True
test_jenkins()


# Generated at 2022-06-14 04:51:19.343961
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = 'master'
    bitbucket(branch='master')


# Generated at 2022-06-14 04:51:26.572064
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS_BRANCH"] = "branch"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    assert travis("branch")
    os.environ["TRAVIS_BRANCH"] = "not correct branch"
    assert not travis("branch")
    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    assert not travis("branch")


# Generated at 2022-06-14 04:51:31.611540
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"]="master"
    assert os.environ["BITBUCKET_BRANCH"] == "master"
    assert bitbucket(os.environ["BITBUCKET_BRANCH"])
    del os.environ["BITBUCKET_BRANCH"]



# Generated at 2022-06-14 04:51:34.446291
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    frigg("master")
    frigg("bad")


# Generated at 2022-06-14 04:51:57.057546
# Unit test for function circle
def test_circle():
    """
    Check if the circle function returns a True boolean
    """
    os.environ["CIRCLECI"] = "true"
    os.environ["CI_PULL_REQUEST"] = "true"
    os.environ["CIRCLE_BRANCH"] = "devel"
    assert circle("master") == True

    os.environ["CIRCLE_BRANCH"] = "master"
    assert circle("master") == True
    del os.environ["CIRCLECI"]
    del os.environ["CI_PULL_REQUEST"]
    del os.environ["CIRCLE_BRANCH"]


# Generated at 2022-06-14 04:51:59.303146
# Unit test for function jenkins
def test_jenkins():
    assert jenkins(branch="master") == True
    assert jenkins(branch="test") == False


# Generated at 2022-06-14 04:52:02.902230
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "branch"
    os.environ["FRIGG_PULL_REQUEST"] = "123"
    try:
        frigg("branch")
    except CiVerificationError:
        pass
    else:
        assert False


# Generated at 2022-06-14 04:52:14.198485
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ['BITBUCKET_PR_ID'] = None
    check()
    os.environ['BITBUCKET_BRANCH'] = "develop"
    check()
    try:
        check(branch="develop")
    except AssertionError:
        pass
    else:
        assert False
    try:
        check(branch="abc")
    except AssertionError:
        pass
    else:
        assert False
    # test when PR is set
    os.environ['BITBUCKET_PR_ID'] = "123"
    check(branch="develop")
    try:
        check()
    except AssertionError:
        pass
    else:
        assert False

# Generated at 2022-06-14 04:52:19.777159
# Unit test for function circle
def test_circle():
    assert os.environ.get("CIRCLECI") == None
    _env_backup = dict(os.environ)
    os.environ['CIRCLECI'] = 'true'
    os.environ['CIRCLE_BRANCH'] = 'master'
    os.environ['CI_PULL_REQUEST'] = 'false'
    circle('master')
    os.environ = _env_backup

# Generated at 2022-06-14 04:52:22.062128
# Unit test for function jenkins
def test_jenkins():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "http://localhost:8080/"

    jenkins("master")

# Generated at 2022-06-14 04:52:28.020617
# Unit test for function jenkins
def test_jenkins():
    """
        Test the jenkins function.
    """
    os.environ["JENKINS_URL"] = "http://localhost"
    os.environ["BRANCH_NAME"] = "testing"
    os.environ["GIT_BRANCH"] = "testing"
    os.environ["CHANGE_ID"] = None
    assert jenkins("testing") is True

# Generated at 2022-06-14 04:52:32.351346
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"
    check("master")

# Generated at 2022-06-14 04:52:35.313949
# Unit test for function bitbucket
def test_bitbucket():
    os.environ['BITBUCKET_BRANCH'] = 'master'
    del os.environ['BITBUCKET_PR_ID']

    check()

# Generated at 2022-06-14 04:52:40.290370
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = "1234"
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    check()

# Generated at 2022-06-14 04:52:55.893810
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = "true"
    try:
        frigg("master")
    except CiVerificationError:
        pass


# Generated at 2022-06-14 04:53:00.716949
# Unit test for function travis
def test_travis():
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check()



# Generated at 2022-06-14 04:53:11.565544
# Unit test for function frigg
def test_frigg():
    for env in ['true', 'True', '1', 'yeah']:
        os.environ['FRIGG'] = env

        for branch in ['master', 'v1.0', 'v1/2']:
            os.environ['FRIGG_BUILD_BRANCH'] = branch
            for pr in [None, 'false', 'no', '0']:
                os.environ['FRIGG_PR_ID'] = pr
                check(branch)
                os.environ['FRIGG_PR_ID'] = pr
                check(branch)

        del os.environ['FRIGG']
        del os.environ['FRIGG_BUILD_BRANCH']
        del os.environ['FRIGG_PR_ID']

# Generated at 2022-06-14 04:53:18.651030
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['PULL_REQUEST_NUMBER'] = 1
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'failed'
    # Test with correct branch but pull_request and failed thread
    assert not check()
    # Test with all correct
    os.environ['PULL_REQUEST_NUMBER'] = None
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'success'
    assert check()

# Generated at 2022-06-14 04:53:23.811996
# Unit test for function gitlab
def test_gitlab():
    os.environ['CI_COMMIT_REF_NAME'] = "master"
    os.environ['CI_MERGE_REQUEST_ID'] = "42"
    check('master')
    assert True
    del os.environ['CI_MERGE_REQUEST_ID']
    check('master')
    assert True

# Generated at 2022-06-14 04:53:33.475619
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "JENKINS_URL"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = "CHANGE_ID"
    check("master")
    assert os.environ.get("TRAVIS") != "true"
    assert os.environ.get("SEMAPHORE") != "true"
    assert os.environ.get("FRIGG") != "true"
    assert os.environ.get("CIRCLECI") != "true"
    assert os.environ.get("GITLAB_CI") != "true"
    assert os.environ.get("BITBUCKET_BUILD_NUMBER") != "true"

# Generated at 2022-06-14 04:53:41.774428
# Unit test for function frigg
def test_frigg():
    os.environ["FRIGG"] = "true"

    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    assert frigg("master") == True

    os.environ["FRIGG_BUILD_BRANCH"] = "develop"
    assert frigg("master") == False

    os.environ["FRIGG_PULL_REQUEST"] = "3"
    assert frigg("master") == False

    del os.environ["FRIGG_PULL_REQUEST"]
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    assert frigg("master") == True

    del os.environ["FRIGG"]
    assert frigg("master") == False



# Generated at 2022-06-14 04:53:49.044252
# Unit test for function semaphore
def test_semaphore():
    os.environ['BRANCH_NAME'] = 'test'
    os.environ['PULL_REQUEST_NUMBER'] = 'false'
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    semaphore('test')
    os.environ['BRANCH_NAME'] = 'test2'
    try:
        semaphore('test')
    except AssertionError as err:
        assert str(err)
    os.environ['BRANCH_NAME'] = 'test'
    os.environ['PULL_REQUEST_NUMBER'] = 'true'
    try:
        semaphore('test')
    except AssertionError as err:
        assert str(err)

# Generated at 2022-06-14 04:53:52.678723
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://jenkins.example.com"
    os.environ["BRANCH_NAME"] = "master"
    assert jenkins("master")



# Generated at 2022-06-14 04:54:01.530345
# Unit test for function bitbucket
def test_bitbucket():
    os.environ["BITBUCKET_BUILD_NUMBER"] = 1
    os.environ["BITBUCKET_BRANCH"] = "master"
    bitbucket("master")
    os.environ["BITBUCKET_BRANCH"] = "develop"
    try:
        bitbucket("master")
        assert False
    except CiVerificationError:
        pass
    os.environ["BITBUCKET_PR_ID"] = 123
    try:
        bitbucket("master")
        assert False
    except CiVerificationError:
        pass

# Generated at 2022-06-14 04:54:20.392834
# Unit test for function bitbucket
def test_bitbucket():
    assert bitbucket("master") is True



# Generated at 2022-06-14 04:54:29.200846
# Unit test for function check
def test_check():
    os.environ['TRAVIS'] = os.environ['TRAVIS_BRANCH'] = os.environ['GIT_BRANCH'] = 'master'
    os.environ['TRAVIS_PULL_REQUEST'] = 'false'
    assert check() is True
    os.environ['TRAVIS_PULL_REQUEST'] = 'true'
    assert check() is False

    os.environ['SEMAPHORE'] = 'true'
    os.environ['BRANCH_NAME'] = os.environ['GIT_BRANCH'] = 'master'
    os.environ['SEMAPHORE_THREAD_RESULT'] = 'passed'
    os.environ['PULL_REQUEST_NUMBER'] = '' 
    assert check() is True

# Generated at 2022-06-14 04:54:31.412882
# Unit test for function frigg
def test_frigg():
    """Test frigg function"""
    branch = os.environ["FRIGG_BUILD_BRANCH"]
    frigg(branch)

# Generated at 2022-06-14 04:54:35.728566
# Unit test for function circle
def test_circle():
    os.environ["CIRCLECI"] = "true"
    os.environ["TRAVIS"] = ""
    os.environ["CI_PULL_REQUEST"] = ""
    os.environ["CIRCLE_BRANCH"] = "test_branch"
    check()



# Generated at 2022-06-14 04:54:40.424845
# Unit test for function semaphore
def test_semaphore():
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = ""
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    assert semaphore("master")



# Generated at 2022-06-14 04:54:43.742562
# Unit test for function check
def test_check():
    """
    Performs function checks for the function check
    """
    assert os.environ.get("TRAVIS") == "true"
    check()

# Unit tests for function travis

# Generated at 2022-06-14 04:54:46.757082
# Unit test for function circle
def test_circle():
    """Test for function circle"""
    os.environ["CIRCLECI"] = "true"
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"

    circle('master')



# Generated at 2022-06-14 04:54:57.000246
# Unit test for function jenkins
def test_jenkins():
    os.environ["JENKINS_URL"] = "https://jenkins.com"
    os.environ["BRANCH_NAME"] = "dev"
    os.environ["GIT_BRANCH"] = "dev"
    os.environ["CHANGE_ID"] = "1"

    with pytest.raises(CiVerificationError):
        jenkins("master")

    os.environ["JENKINS_URL"] = "https://jenkins.com"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["GIT_BRANCH"] = "master"
    os.environ["CHANGE_ID"] = "1"

    with pytest.raises(CiVerificationError):
        jenkins("master")

    os.environ

# Generated at 2022-06-14 04:55:05.709028
# Unit test for function jenkins
def test_jenkins():
    try:
        os.environ["JENKINS_URL"] = "http://localhost"
        os.environ["BRANCH_NAME"] = "master"
        os.environ["BRANCH_NAME"] = "GIT_BRANCH"
        os.environ["CHANGE_ID"] = ""
        print("test_jenkins - Pass")
        jenkins("master")
    except CiVerificationError as err:
        print("test_jenkins - Fail")
        print(str(err))
