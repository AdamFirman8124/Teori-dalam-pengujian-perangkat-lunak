

# Generated at 2022-06-14 05:15:16.229860
# Unit test for method auth of class Github
def test_Github_auth():
    token = "test_value"
    assert TokenAuth(token) == TokenAuth(token)
    assert TokenAuth(token) != TokenAuth(token="test_value2")
    assert TokenAuth(token) != None
    assert TokenAuth(token) != Exception()



# Generated at 2022-06-14 05:15:18.223025
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"



# Generated at 2022-06-14 05:15:25.482011
# Unit test for method auth of class Github
def test_Github_auth():
    dummy_token = "abcd"
    dummy_auth = TokenAuth(dummy_token)
    assert Github.domain() == "github.com"
    assert Github.api_url() == "https://api.github.com"

    # set environment variable
    os.environ["GH_TOKEN"] = dummy_token
    assert Github.token() == dummy_token

    # Run the actual function
    assert Github.auth() == dummy_auth

    # clear the environment variable
    os.environ["GH_TOKEN"] = ""
    assert Github.token() == None

# Generated at 2022-06-14 05:15:29.182835
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.check_build_status("ArkEcosystem", "desktop-wallet", "5cc5d7a5b531f7a25e2ec37d7277e44a9f8bbe11")


# Generated at 2022-06-14 05:15:30.716896
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"

# Generated at 2022-06-14 05:15:31.784359
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"

# Generated at 2022-06-14 05:15:40.603071
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class mock_Gitlab(Gitlab):
        def gitlab(self, api_url, private_token):
            self.auth = True
            self.error_auth = False
            self.api = mock_api(api_url=api_url, private_token=private_token)
            return self

        def auth(self):
            if self.error_auth:
                raise gitlab.exceptions.GitlabAuthenticationError(
                    "Could not authenticate you from GitLab because \"Invalid credentials\""
                )

    class mock_api(object):
        def __init__(self, api_url, private_token):
            self.jobs = mock_jobs(api_url=api_url, private_token=private_token)


# Generated at 2022-06-14 05:15:52.864625
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    """Check Github.check_build_status()
    """
    from git import Repo
    from .helpers import mock_git, temp_git_repo

    assert not Github.check_build_status("owner", "repo", "ref")

    assert Github.check_build_status("pypa", "pip", "d4c69a8dee7c25b9f957e8a439b821e7f3a36e20")

    with temp_git_repo() as repo:
        with mock_git(repo):
            repo = Repo(repo)
            repo.create_tag("v2.6.0")
            assert not Github.check_build_status("pypa", "pip", repo.commit("v2.6.0"))


# Generated at 2022-06-14 05:16:03.190193
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    # check domain with an alternate domain
    with patch("pypyr.utils.hvcs.config.get") as mock_config:
        # mock the config to return a different domain
        mock_config.return_value = "random.domain"
        output = Gitlab.domain()
        assert output == "random.domain", "domain is not equal to domain from config"
        mock_config.assert_called_once_with("hvcs_domain")
    # check domain with an alternate domain in CI_SERVER_HOST
    with patch("pypyr.utils.hvcs.config.get") as mock_config:
        mock_config.return_value = None
        with patch.dict(os.environ, {"CI_SERVER_HOST": "other.domain"}):
            output = Gitlab.domain()
            assert output

# Generated at 2022-06-14 05:16:05.087154
# Unit test for method domain of class Github
def test_Github_domain():
    assert str is type(Github.domain())

# Generated at 2022-06-14 05:19:18.948412
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github().domain() == "github.com"


# Generated at 2022-06-14 05:19:21.486115
# Unit test for method api_url of class Github
def test_Github_api_url():
    github = Github()
    assert isinstance(Github.api_url(), str)
    
    

# Generated at 2022-06-14 05:19:34.067046
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():

    class Job:
        def __init__(self, status, allow_failure: bool = False, name: str = ""):
            self.status = status
            self.allow_failure = allow_failure
            self.name = name

    class MockGitlabClient:
        def __init__(self):
            self.auth = lambda: True
            self.projects = MockGitlabProject()

    class MockGitlabProject:
        def __init__(self):
            self.get = lambda a: MockGitlabRepo()

    class MockGitlabRepo:
        def __init__(self):
            self.commits = MockGitlabCommits()

    class MockGitlabCommits:
        def __init__(self):
            self.get = lambda a: MockGitlabCommit()



# Generated at 2022-06-14 05:19:45.280883
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class MockGitlab(gitlab.Gitlab):
        def __init__(self, url, private_token):
            pass

        def auth(self):
            pass

        def projects(self):
            return MockProject()

    class MockProject:
        def __init__(self):
            pass

        def get(self, id):
            return MockProjectId()

    class MockProjectId:
        def __init__(self):
            pass

        def commits(self):
            return MockCommits()

    class MockCommits:
        def __init__(self):
            pass

        def get(self, sha):
            return MockSha()

    class MockSha:
        def __init__(self):
            pass

        def statuses(self):
            return MockStatuses()


# Generated at 2022-06-14 05:19:48.570044
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"



# Generated at 2022-06-14 05:19:50.955745
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("toto", "toto", "toto") is False

# Generated at 2022-06-14 05:20:03.796201
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """
    Test the method check_build_status of class Gitlab
    """

    import pytest
    from unittest.mock import patch, MagicMock

    tests = [
        (True, [{"status": "success"}, {"allow_failure": True, "status": "failed"}]),
        (True, [{"allow_failure": True, "status": "failed"}, {"status": "success"}]),
        (False, [{"status": "failed"}, {"status": "success"}]),
        (False, [{"status": "pending"}]),
        (False, [{"allow_failure": False, "status": "failed"}, {"status": "success"}]),
        (False, [{"status": "failed"}, {"allow_failure": False, "status": "failed"}]),
    ]


# Generated at 2022-06-14 05:20:17.624422
# Unit test for method auth of class Github
def test_Github_auth():
    assert getattr(Github, "auth", None) is not None

    # Test with bad value (str)
    try:
        Github.auth = "bad"
        assert False
    except TypeError:
        pass

    # Test with bad value (int)
    try:
        Github.auth = 123
        assert False
    except TypeError:
        pass

    # Test with bad value (None)
    try:
        Github.auth = None
        assert False
    except TypeError:
        pass

    # Test with proper value
    try:
        Github.auth = "test"
        assert Github.auth == "test"
        Github.auth = 123
        assert Github.auth == 123
        Github.auth = None
        assert Github.auth is None
    except TypeError:
        assert False

# Generated at 2022-06-14 05:20:20.600947
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("gitlab-org", "gitlab-ce", "d2a1a8db876d64f0f0e6002d25247c38ab7f909e")

# Generated at 2022-06-14 05:20:24.224839
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"
