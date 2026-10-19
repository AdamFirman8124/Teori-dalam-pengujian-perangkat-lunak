

# Generated at 2022-06-14 05:13:34.686436
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """ Unit Test for method check_build_status of class Gitlab
    """
    class test_Gitlab(Base):
        """Class to test the Gitlab class"""

        @staticmethod
        def check_build_status(owner: str, repo: str, ref: str) -> bool:
            """Test method for Gitlab method check_build_status
            """
            return "Pending"

    assert test_Gitlab.check_build_status("owner", "repo", "ref") == "Pending"



# Generated at 2022-06-14 05:13:47.935428
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class MockSession():
        def get(self, url: str, params: dict = None) -> dict:
            return {
                "status": "failed",
                "allow_failure": False,
                "name": "test"
            }

    class MockGitlab():
        @staticmethod
        def projects():
            class MockProjects():
                def get(self, url: str):
                    class MockCommits():
                        def get(self, url: str):
                            class MockStatuses():
                                def list(self):
                                    return [MockSession().get(url)]
                            return MockStatuses()
                    return MockCommits()
            return MockProjects()

    # The build is failed
    assert Gitlab.check_build_status("owner", "repo", "ref") == False

    # The build is

# Generated at 2022-06-14 05:13:53.689150
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class Gitlab_check_build_status_test(unittest.TestCase):
        def test_Gitlab_check_build_status_success(self):
            """
            check that Gitlab.check_build_status return True when the build is successful
            """

# Generated at 2022-06-14 05:14:04.880506
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # test Github
    if Gitlab.domain() == "github.com":
        # test commit ref for this release
        owner = "bluebrain"
        repo = "nexus-publisher"
        ref = "v1.8.1"
        check_build_status = Gitlab.check_build_status(owner, repo, ref)
        assert check_build_status, "test_Gitlab_check_build_status for Github failed"
    # test Gitlab
    else:
        # test commit ref for this release
        owner = "bluebrain"
        repo = "nexus-publisher"
        ref = "v1.8.1"
        check_build_status = Gitlab.check_build_status(owner, repo, ref)

# Generated at 2022-06-14 05:14:11.675203
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    os.environ["CI_SERVER_HOST"] = ""
    config["hvcs_domain"] = ""
    assert Gitlab.domain() == "gitlab.com"

    os.environ["CI_SERVER_HOST"] = "gitlab.test"
    config["hvcs_domain"] = ""
    assert Gitlab.domain() == "gitlab.test"

    config["hvcs_domain"] = "localhost"
    assert Gitlab.domain() == "localhost"


# Generated at 2022-06-14 05:14:14.821149
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("icgc-argo", "icgc-pipeline-discovery", "4b2ac28b") is True


# Generated at 2022-06-14 05:14:22.199407
# Unit test for method auth of class Github
def test_Github_auth():
  try:
    with open('Github.token', 'r') as file:
      GH_TOKEN = file.read().replace('\n', '')
    if GH_TOKEN:
      if os.getenv('GH_TOKEN', '') == GH_TOKEN:
        print('test_Github_auth passed\n')
        return
      else:
        os.putenv('GH_TOKEN', GH_TOKEN)
  except:
    pass
  raise Exception('test_Github_auth failed')
try:
  test_Github_auth()
except:
  print('test_Github_auth failed')



# Generated at 2022-06-14 05:14:27.258513
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("i3sUnicornTeam", "dummy-project", "4a4c4b8d") == False
    assert Gitlab.check_build_status("i3sUnicornTeam", "dummy-project", "2bc88c4a") == True

# Generated at 2022-06-14 05:14:36.787305
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    import requests_mock
    import requests

    def check_build_status_mock(self, owner: str, repo: str, ref: str) -> bool:
        return True

    def check_build_status_failed_mock(self, owner: str, repo: str, ref: str) -> bool:
        return False

    @requests_mock.Mocker()
    def test_check_build_status(responses, mocker):
        responses.get(requests_mock.ANY, json={})
        responses.get(requests_mock.ANY, json={})
        responses.get(requests_mock.ANY, json={})

        mocker.patch.object(Gitlab, "check_build_status", check_build_status_mock)

# Generated at 2022-06-14 05:14:44.579282
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("gitlab-org", "gitlab", "7eaf344b13a5965bdf2c84cd1f76a1e44ee73e9d") == True
    assert Gitlab.check_build_status("gitlab-org", "gitlab", "7eaf344b13a5965bdf2c84cd1f76a1e44ee73e90") == False

# Generated at 2022-06-14 05:16:42.760912
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # we mock the gitlab.Gitlab.auth() method because we cannot authenticate on Gitlab
    # when we are running unit tests
    with mock.patch("gitlab.Gitlab.auth", return_value=None) as mock_auth, mock.patch(
        "gitlab.Gitlab.projects.get"
    ) as mock_get, mock.patch("gitlab.Gitlab.projects.list", return_value=[]) as mock_list:
        mock_project = mock.MagicMock()
        mock_get.return_value = mock_project

# Generated at 2022-06-14 05:16:49.669825
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    @patch("requests.get")
    def test(mock_get):

        test = True

        if test:
            # test all jobs with success status
            jobs = []
            for status in ["success", "skipped"]:
                job = {"status": status, "allow_failure": False}
                jobs.append(job)
            mock_get.return_value = MockResponse(jobs, 200)

        else:
            # test some jobs with success status and one with pending, failed or 0 allow_failure
            jobs = []

# Generated at 2022-06-14 05:16:56.009226
# Unit test for function get_hvcs
def test_get_hvcs():
    assert get_hvcs() == Github
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# Generated at 2022-06-14 05:16:57.568085
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == config.get("hvcs_domain")



# Generated at 2022-06-14 05:17:09.476592
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class GitlabMock(Gitlab):
        # Mock to return a list of jobs
        def check_build_status(owner: str, repo: str, ref: str):
            return [
                {
                    "status": "success",
                    "status_detail": "passed",
                    "name": "master",
                },
                {
                    "status": "failed",
                    "status_detail": "failed",
                    "name": "master",
                },
                {
                    "status": "pending",
                    "status_detail": "pending",
                    "name": "master",
                },
                {
                    "status": "failed",
                    "status_detail": "failed",
                    "name": "master",
                    "allow_failure": True,
                },
            ]

    # Expect status to be True if

# Generated at 2022-06-14 05:17:21.173782
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Tests the method check_build_status of the class Gitlab"""
    assert Gitlab.check_build_status(
        "Framework", "fc-gsoc-2019-bootstrap", "a5b5e5f5817bfd28a9f9edb94f6e2f2ebff330cc"
    ) == True
    assert Gitlab.check_build_status(
        "Framework", "fc-gsoc-2019-bootstraphash", "a5b5e5f5817bfd28a9f9edb94f6e2f2ebff330cc"
    ) == False

# Generated at 2022-06-14 05:17:22.278096
# Unit test for method auth of class Github
def test_Github_auth():
    github_instance = Github()
    github_instance.auth()



# Generated at 2022-06-14 05:17:24.287142
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    Gitlab.domain = "gitlab.com"

# Generated at 2022-06-14 05:17:26.798477
# Unit test for function get_hvcs
def test_get_hvcs():
    """Unit test for function get_hvcs"""
    assert get_hvcs() == Github



# Generated at 2022-06-14 05:17:28.255073
# Unit test for method auth of class Github
def test_Github_auth():
    assert TokenAuth(None) == TokenAuth(None)



# Generated at 2022-06-14 05:19:39.526679
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    domain = os.environ.get("CI_SERVER_HOST", "gitlab.com")
    gl = gitlab.Gitlab(
        "https://" + domain, private_token=os.environ.get("GL_TOKEN", "")
    )
    gl.auth()
    # print(gl.projects.list(owned=True))
    repo = os.environ.get("CI_PROJECT_NAME", "rndm-project")
    owner = os.environ.get("CI_PROJECT_NAMESPACE", "haxm")
    ref = os.environ.get("CI_COMMIT_SHA", "9481f1c6f370ee6226a019dbb328f2b2c76e1a07")

# Generated at 2022-06-14 05:19:44.279235
# Unit test for function get_hvcs
def test_get_hvcs():
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()
    config.set("hvcs", "gitlab")
    assert get_hvcs() == Gitlab
    config.set("hvcs", "github")
    assert get_hvcs() == Github

# Generated at 2022-06-14 05:19:53.337935
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    fake_ref = "test_sha1"
    fake_gitlab_url = "https://fake_gitlab_url"
    fake_owner = "test_owner"
    fake_repo = "test_repo"
    def mocked_statuses_list(*args, **kwargs):
        if fake_ref != args[0]:
            return []
        return [{"status": "success"}, {"status": "success"}]
    def mocked_commits_get(*args, **kwargs):
        if fake_ref != args[0]:
            return None
        return MagicMock(statuses=MagicMock(list=mocked_statuses_list))
    def mocked_projects_get(*args, **kwargs):
        if f"{fake_owner}/{fake_repo}" != args[0]:
            return None


# Generated at 2022-06-14 05:20:01.414704
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    commit_ref="aab29123974f1bede616b9842eb9b9e9e0f5086d"
    owner="test-owner"
    repo="test-repo"

    # No pipeline for the commit so the pipeline status is pending 
    # and the method check_build_status hasn't got the id of the pipeline 
    # that is why the test fails and return false
    assert Gitlab.check_build_status(owner, repo, commit_ref) == False

# Generated at 2022-06-14 05:20:07.721374
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class Gitlab_test(Gitlab):
        @staticmethod
        def check_build_status(owner: str, repo: str, ref: str) -> bool:
            return Gitlab.check_build_status(owner, repo, ref)

    import random

    class Mock_project():
        class Mock_commits():
            class Mock_statuses():
                def list(self):
                    return [{"status": random.choice(["success", "failed", "error"])}]

            def get(self, ref):
                return self.Mock_statuses()

        def get(self, name):
            return self.Mock_commits()

    gl = Gitlab_test()
    random.seed(0)
    assert not gl.check_build_status("mock", "mock", "mock")
    random.seed

# Generated at 2022-06-14 05:20:19.950634
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    import pytest

    test_gitlab_url = "https://gitlab.com/"
    test_gitlab_token = "testtoken"
    test_owner = "test namespace/test_group"
    test_repo = "test_repo"
    test_ref = "1234567890123456789012345678901234567890"
    test_status = "failed"

    # Mock the _get_gitlab_instance(self) function using the MagicMock class
    mock_gitlab_instance = MagicMock()
    mock_gitlab_instance.projects.get.return_value.commits.get.return_value.statuses.list.return_value = [
        {"status": test_status, "name": "test name", "allow_failure": False}
    ]

# Generated at 2022-06-14 05:20:22.220290
# Unit test for method auth of class Github
def test_Github_auth():
    test_instance = Github()
    test_instance.auth()



# Generated at 2022-06-14 05:20:35.260426
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    def test(owner: str, repo: str, ref: str, status: bool):
        print(f"{owner}, {repo}, {ref} : {Gitlab.check_build_status(owner, repo, ref)}")

    test("acme", "acme-rocket", "b039b5f6e5d2bfe0c8e9122af7dafc65a1a54f19", True)
    test("acme", "acme-rocket", "c6b7f6b38e1894f09b1e2d07a335c65d8ac9a9f3", True)
    test("acme", "acme-rocket", "c1b7f6b38e1894f09b1e2d07a335c65d8ac9a9f3", True)

# Generated at 2022-06-14 05:20:37.840952
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    logger.info("Testing versioneer.config.hvcs.Gitlab.check_build_status")
    print("Testing versioneer.config.hvcs.Gitlab.check_build_status")
    v = "GL_TOKEN=<>; python3 -m pytest -s --disable-pytest-warnings -vv --capture=no -rs --color=yes -k test_Gitlab_check_build_status tests/unit/test_hvcs.py"

# Generated at 2022-06-14 05:20:40.234118
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"