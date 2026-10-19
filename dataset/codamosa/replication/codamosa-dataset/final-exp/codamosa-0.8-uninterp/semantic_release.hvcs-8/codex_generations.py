

# Generated at 2022-06-14 05:14:40.296143
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    print("Unit test for method check_build_status of class Gitlab")
    #test_ref_sha is the sha1 hash of a commit in project nuxeo/nuxeo-master-snapshot-hudson
    #which has 2 jobs both with success status
    ref_sha = "65b0e8d06c0f2dcf1c3a2f3cdfd464ba9b9aad0a"
    status = Gitlab.check_build_status("nuxeo", "nuxeo-master-snapshot-hudson", ref_sha)
    if status is True:
        print("OK")
    else:
        print("Error")

# Generated at 2022-06-14 05:14:44.465159
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner = 'GitLab-Examples'
    repo = 'ci-build-pipelines'
    ref = '0000000000000000000000000000000000000000'
    assert Gitlab.check_build_status(owner, repo, ref) == True

# Generated at 2022-06-14 05:14:46.150660
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.Gitlab.domain() is not None


# Generated at 2022-06-14 05:14:50.139718
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    '''
    Testing with a dummy Gitlab project
    '''
    owner = "edx"
    repo = "test"
    ref = "master"

    assert Gitlab.check_build_status(owner, repo, ref)



# Generated at 2022-06-14 05:14:51.921414
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    assert Github.check_build_status("owner","repo","ref") == False


# Generated at 2022-06-14 05:14:53.917264
# Unit test for method auth of class Github
def test_Github_auth():
    pass

# Generated at 2022-06-14 05:14:56.889806
# Unit test for function get_hvcs
def test_get_hvcs():
    try:
        get_hvcs()
    except Exception as e:
        assert(str(e) == '"{0}" is not a valid option for hvcs.')
    else:
        assert(0)



# Generated at 2022-06-14 05:15:02.207235
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    assert Github.check_build_status(owner, repo, ref) == False
    assert Github.check_build_status(owner, repo, ref) == False
    assert Github.check_build_status(owner, repo, ref) == False
    assert Github.check_build_status(owner, repo, ref) == False

# Generated at 2022-06-14 05:15:04.695060
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"

# Generated at 2022-06-14 05:15:09.836773
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Test if return False when job failed and not allow failure
    #  job is a list of dictionaries
    #  its status is failed
    #  it is not allow to fail
    job = [{"name":"first job", "status":"failed", "allow_failure":False}]
    assert Gitlab.check_build_status("testowner", "testrepo", "testref")==False
    # Test if return False when job failed and allow failure
    #  job is a list of dictionaries
    #  its status is failed
    #  it is allow to fail
    job = [{"name":"first job", "status":"failed", "allow_failure":True}]
    assert Gitlab.check_build_status("testowner", "testrepo", "testref")==True
    # Test if return False when job is still pending
   

# Generated at 2022-06-14 05:16:32.923730
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class Gitlab:
        DEFAULT_DOMAIN = "gitlab.com"
        _fix_mime_types()

        @staticmethod
        def domain() -> str:
            """Gitlab domain property

            :return: The Gitlab instance domain
            """
            domain = "localhost"
            return domain if domain else "gitlab.com"

        @staticmethod
        def api_url() -> str:
            """Gitlab api_url property

            :return: The Gitlab instance API url
            """
            return f"http://{Gitlab.domain()}"

        @staticmethod
        def token() -> Optional[str]:
            """Gitlab token property

            :return: The Gitlab token environment variable (GL_TOKEN) value
            """
            return os.environ.get("GL_TOKEN")


# Generated at 2022-06-14 05:16:45.750905
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():

    # test case 1
    class MockJob1:
        def __init__(self, status, name, allow_failure):
            self.status = status
            self.name = name
            self.allow_failure = allow_failure

    jobs = [
        MockJob1("success", "good job", False),
        MockJob1("pending", "job pending", False),
    ]

    class MockCommit:
        def __init__(self, ref):
            self.ref = ref
            self.statuses = self

        def list(self):
            return jobs

    class MockProject:
        def __init__(self, owner, repo):
            self.owner = owner
            self.repo = repo
            self.commits = self

        def get(self, ref):
            return MockCommit(ref)



# Generated at 2022-06-14 05:16:54.991517
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Test Gitlab_check_build_status function"""
    # Test 1: all success
    with open("./test/test_suite/gitlab_get_commits_statuses_monitor_success.json") as json_file:
        json_data = json.load(json_file)
        assert Gitlab.check_build_status("mantid", "mantid", "1e094ae4dc06102bb6245a1a8e03825f82de2cbc") == True
    # Test 2: not success and not allow_failure
    with open("./test/test_suite/gitlab_get_commits_statuses_monitor_not_success.json") as json_file:
        json_data = json.load(json_file)
        assert Gitlab.check_build_status

# Generated at 2022-06-14 05:17:01.762764
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class GitlabMock(Base):
        @staticmethod
        def check_build_status(owner: str, repo: str, ref: str) -> bool:
            return super(GitlabMock, GitlabMock).check_build_status(owner, repo, ref)

    GitlabMock.check_build_status("owner", "repo", "ref")


if __name__ == "__main__":
    main(globals(), logger)

# Generated at 2022-06-14 05:17:06.789893
# Unit test for function get_hvcs
def test_get_hvcs():
    config.init()
    config.set_hvcs("github")
    get_hvcs()
    config.set_hvcs("gitlab")
    get_hvcs()
    config.set_hvcs("GOOD")
    get_hvcs()


# Generated at 2022-06-14 05:17:11.550150
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner = os.environ.get("CI_PROJECT_NAMESPACE")
    repo = os.environ.get("CI_PROJECT_NAME")
    if owner is not None and repo is not None:
        assert Gitlab.check_build_status(owner, repo, os.environ.get("CI_COMMIT_SHA"))
    else:
        print("Cannot test Gitlab.check_build_status, CI variables are not set.")

# Generated at 2022-06-14 05:17:13.537313
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    domain = os.environ.get("CI_SERVER_HOST")
    assert Gitlab.domain() == domain


# Generated at 2022-06-14 05:17:17.349444
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner = "lsst"
    repo = "ts_xml"
    ref = "f2ab6bef076b21695d89fc601cce69bb9fbcbed5"
    assert Gitlab.check_build_status(owner, repo, ref) == False
    logger.debug("Test of method check_build_status for class Gitlab is done")


# Generated at 2022-06-14 05:17:27.215237
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    import mock
    import responses

    with mock.patch("gitlab.Gitlab") as mock_gitlab:

        instance = mock_gitlab.return_value
        instance.auth.return_value = True
        instance.projects.get.return_value.commits.get.return_value.statuses.list.return_value = [
            {"status": "pending", "name": "job1", "allow_failure": False},
            {"status": "failed", "name": "job2", "allow_failure": False},
            {"status": "success", "name": "job3", "allow_failure": False},
        ]

        assert Gitlab.check_build_status("owner", "repo", "ref") == False


# Generated at 2022-06-14 05:17:36.817529
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # type: (None) -> None
    """Unit test for Gitlab.check_build_status()
    """
    class GitlabMock():
        """Mock for class Gitlab"""
        def __init__(self, url: str, private_token: str) -> None:
            pass

        def auth(self) -> None:
            pass

        class Project():
            """Mock for class Project"""
            def __init__(self, param1: str) -> None:
                pass

            def get(self, ref: str) -> None:
                self.ref = ref
                return self

            class Commits():
                """Mock for class Commits"""
                def __init__(self, param1: str) -> None:
                    pass

                def get(self, param1: str) -> None:
                    return self

               

# Generated at 2022-06-14 05:20:14.115114
# Unit test for method auth of class Github
def test_Github_auth():
    assert Github.auth()==None
Github.auth()


# Generated at 2022-06-14 05:20:15.440212
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.check_build_status("", "", "")



# Generated at 2022-06-14 05:20:19.982280
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # check_build_status
    assert Gitlab.check_build_status("SUSE", "SUSE-Manager-Server", "f5fc2eecfa5a8afdd1f0d09e6717a29b5ad8e7ee")

# Generated at 2022-06-14 05:20:33.808286
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class MockResponse:
        def __init__(self, content):
            self.content = content

        def json(self):
            return self.content

    class MockSession:
        def __init__(self, status_code, content):
            self.status_code = status_code
            self.content = content


# Generated at 2022-06-14 05:20:37.258440
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """ Unit test for method check_build_status of class Gitlab

        :return: None
    """
    assert Gitlab.check_build_status("CI-Platform/dummy", "dummy", "") == True



# Generated at 2022-06-14 05:20:49.158732
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    def _test_check_build_status(status, expected_result):
        """Test Gitlab.check_build_status.

        :param status: A list of statuses
        :param expected_result: The expected result of the function
        """
        with patch("pygit2.Repository") as mock_Repository:
            mock_Repository.return_value.get.return_value.statuses.return_value = status
            result = Gitlab.check_build_status("owner", "repo", "ref")
            mock_Repository.assert_called_once_with("")
            mock_Repository.return_value.get.assert_called_once_with("owner/repo")

# Generated at 2022-06-14 05:20:56.700532
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    from .utils import set_environment, get_environment

    owner = "jselman"
    repo = "pulumi-azure"
    test_ref = "06c73f798b26e7a0d97e1a3a3b2aa8c9b9a9b032"
    test_token = "asdklj2lkjasdlkjASDdD"
    set_environment("GL_TOKEN", test_token)
    assert Gitlab.token() == test_token
    assert Gitlab.check_build_status(owner, repo, test_ref) is True
    del os.environ["GL_TOKEN"]
    assert Gitlab.token() is None
    del os.environ["CI_SERVER_HOST"]
    assert Gitlab.domain() == "gitlab.com"
   

# Generated at 2022-06-14 05:21:05.101206
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("apps", "galaxy", "f17b9a9a46e2780d8459c66262bf3c3fde969c89")
    assert not Gitlab.check_build_status("apps", "galaxy", "5e5b5f5d5c5b5f5d5c5b5f5d5c5b5f5d5c5b5f5d")


# Generated at 2022-06-14 05:21:10.136176
# Unit test for method api_url of class Github
def test_Github_api_url():
    from semantic_release.hvcs.github import Github

    assert Github.api_url() == 'https://api.github.com', (
        'The value of method api_url of class Github must be equals to '
        'https://api.github.com'
    )



# Generated at 2022-06-14 05:21:13.366392
# Unit test for function get_hvcs
def test_get_hvcs():
    assert type(get_hvcs()) is Github
