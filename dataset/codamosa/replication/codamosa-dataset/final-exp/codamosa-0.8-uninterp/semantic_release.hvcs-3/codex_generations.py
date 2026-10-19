

# Generated at 2022-06-14 05:14:22.144662
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("test_owner", "test_repo", "test_ref")
    assert Gitlab.check_build_status("jekyll", "jekyll", "ab6e11a9f4444c7b91e46f2206d33cdd07b36c30")
    assert Gitlab.check_build_status("jekyll", "jekyll", "fc0a5e18b7c5e541da9775f8452a80a9e31adc5f")
    assert Gitlab.check_build_status("jekyll", "jekyll", "965b04c2b3d29c7ee8d64becb982e7007055d1b3")

# Generated at 2022-06-14 05:14:23.891365
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"

# Generated at 2022-06-14 05:14:25.629457
# Unit test for function get_hvcs
def test_get_hvcs():
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()


# Generated at 2022-06-14 05:14:31.897617
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    # Init a TokenAuth class instance
    token_auth = TokenAuth("test_token")
    # init a request
    request = requests.Request("GET", "https://example.com")
    # Pretend to execute the request via a prepped request.
    token_auth(request)
    # Evaluate the expected result.
    assert request.headers.get("Authorization") == "token test_token"



# Generated at 2022-06-14 05:14:33.869293
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    assert Github.check_build_status('soumith', 'test-repo', 'test-ref')



# Generated at 2022-06-14 05:14:36.721787
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    r = requests.Request("GET", "https://github.com/")
    token = "mytoken"
    auth = TokenAuth(token)
    assert auth(r).headers["Authorization"] == f"token {token}"



# Generated at 2022-06-14 05:14:42.555671
# Unit test for function get_hvcs
def test_get_hvcs():
    """
    Test get_hvcs function
    """
    with pytest.raises(ImproperConfigurationError) as excinfo:
        get_hvcs()
    assert '"{0}" is not a valid option for hvcs.' in str(excinfo.value)

# Generated at 2022-06-14 05:14:46.150642
# Unit test for method auth of class Github
def test_Github_auth():
    token = "foobar"
    expected_output = TokenAuth(token)
    Github.token = lambda: token

    actual_output = Github.auth()

    assert actual_output == expected_output



# Generated at 2022-06-14 05:14:57.215634
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Test Gitlab.check_build_status method. It uses the same tests than logic in
    test_check_build_status_github.py
    """
    from test.cp2_test_case import CP2TestCase

    # Mock the requests.Session
    class Session:
        @staticmethod
        def get(url):
            """Mock method for requests.Session.get"""

# Generated at 2022-06-14 05:14:58.935907
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    assert Github.check_build_status(owner, repo, ref) == True




# Generated at 2022-06-14 05:16:47.914038
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Test a case where the last job of a pipeline is still pending
    @mock.patch('homeassistant_cli.cli.hvcs.gitapi.gitlab.Gitlab.projects.get')
    @mock.patch('homeassistant_cli.cli.hvcs.gitapi.gitlab.Gitlab.auth')
    @mock.patch('homeassistant_cli.cli.hvcs.gitapi.gitlab.Gitlab.__init__')
    def mock_get_jobs(mock_init, mock_auth, mock_get):
        mock_init.return_value = None
        mock_auth.return_value = None

        # define mock return value for the first call to jobs.list()

# Generated at 2022-06-14 05:17:01.774776
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    a = Github()
    # print(a.check_build_status("jia-yw", "test", "43c8e8bb00c7ff51a9a9d9af74b63d1b6c106a6d"))
    print(a.check_build_status("iterative", "dvc", "a8db2ebc2f93d57dade6a1794ab8cbc41f9a6f46"))
    # print(a.check_build_status("iterative", "dvc", "8da2fafb9f94d93540a32e8e3f1878a3a37d5f4e"))
    # print(a.check_build_status("iterative", "dvc", "e1d3d2e5a4aef4f4c260

# Generated at 2022-06-14 05:17:04.279711
# Unit test for method auth of class Github
def test_Github_auth():
    # Call the method
    result = Github.auth()

    # Test that the result is correct
    assert result is None



# Generated at 2022-06-14 05:17:09.056984
# Unit test for function get_hvcs
def test_get_hvcs():
    """Unit test for get_hvcs"""
    config.clear()
    config.update({"hvcs": "github"})
    assert get_hvcs() == Github
    config.clear()
    config.update({"hvcs": "gitlab"})
    assert get_hvcs() == Gitlab

# Generated at 2022-06-14 05:17:13.015819
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"
    assert Github.api_url() == config.get("github_api_url")
    assert Github.api_url() == config.get("gitlab_api_url")



# Generated at 2022-06-14 05:17:16.604097
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    status = Gitlab.check_build_status("hsldevcom", "hsl-map-generator", "7e4f4d5e7e5c74b5f5b5176e70fa0a2fa991f8da")
    assert status == False

# Generated at 2022-06-14 05:17:21.654010
# Unit test for function get_hvcs
def test_get_hvcs():
    """Test function get_hvcs"""
    # ImproperConfigurationError
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()

# Generated at 2022-06-14 05:17:24.802768
# Unit test for function get_hvcs
def test_get_hvcs():
    """test get_hvcs"""
    assert get_hvcs() == Github
    #TODO: add test for ImproperConfigurationError exception


# Generated at 2022-06-14 05:17:27.271234
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("ns", "repo", "ref")

# Generated at 2022-06-14 05:17:35.278823
# Unit test for function get_hvcs
def test_get_hvcs():
    config.config_data = {
        "hvcs":"github",
        "owner":"owner",
        "repo":"repo",
        "log_level": "DEBUG",
    }
    assert get_hvcs() == globals()["Github"]
    config.config_data = {
        "hvcs":"gitlab",
        "owner":"owner",
        "repo":"repo",
        "log_level": "DEBUG",
    }
    assert get_hvcs() == globals()["Gitlab"]



# Generated at 2022-06-14 05:19:17.990139
# Unit test for function get_hvcs
def test_get_hvcs():
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()



# Generated at 2022-06-14 05:19:21.961580
# Unit test for function get_hvcs
def test_get_hvcs():
    hvcs_g = get_hvcs()
    assert isinstance(hvcs_g, Github)
test_get_hvcs()


# Generated at 2022-06-14 05:19:23.658444
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"

# Generated at 2022-06-14 05:19:36.306853
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    jobs = [
        {
            "allow_failure": False,
            "allow_failure_reason": None,
            "name": "test-job",
            "stage": "test",
            "status": "success",
        }
    ]

    with patch("hvcs.vcs.utils.Gitlab.check_build_status") as mock_cls:
        mock_cls.return_value = True
        assert Gitlab.check_build_status("", "", "") == True

    with patch("hvcs.vcs.utils.Gitlab.check_build_status") as mock_cls:
        mock_cls.return_value = False
        assert Gitlab.check_build_status("", "", "") == False


# Generated at 2022-06-14 05:19:46.327508
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner_test = "owner_test"
    repo_test = "repo_test"
    ref_test = "ref_test"
    value_test = False

    # mock the 'gitlab' library
    gitlab.Gitlab.auth = Mock()

    # mock the 'projects' of the 'gitlab' library
    class GitlabProjects(object):
        def get(self, arg):
            class GitlabProject:
                def __init__(self):
                    self.commits = GitlabCommits()

            return GitlabProject()

    class GitlabCommits(object):
        def get(self, arg):
            class GitlabCommit:
                def __init__(self):
                    self.statuses = GitlabStatuses()

            return GitlabCommit()


# Generated at 2022-06-14 05:19:49.011494
# Unit test for function get_hvcs
def test_get_hvcs():
    assert get_hvcs() == Github
# End of unit test



# Generated at 2022-06-14 05:20:02.765148
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    # Tests if check_build_status returns a True when requests.get response.json().get(
    # 'state') is 'success'.
    # Arrange
    import requests

    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if len(args) > 0 and args[0] == "https://api.github.com/repos/test_owner/test_repo/commits/test_ref/status":
            return MockResponse({"state": "success"}, 200)

        return MockResponse(None, 404)

    requests.get = mock_get
    # Act and Assert

# Generated at 2022-06-14 05:20:06.666675
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() == config.get("hvcs_domain", os.environ.get("CI_SERVER_HOST"))


# Generated at 2022-06-14 05:20:10.001296
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("e2e-robot", "robot-e2e", "095ee5d5") == True


# Generated at 2022-06-14 05:20:20.934542
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("GL_USERNAME", "GL_REPONAME", "GL_REF") is not None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("repository_owner")
    parser.add_argument("repository_name")
    parser.add_argument("commit_ref")

    # Github specific arguments
    parser.add_argument("--github", action="store_true")
    parser.add_argument("--domain", type=str, default="github.com")
    parser.add_argument("--token", type=str, default="")

    # Gitlab specific arguments
    parser.add_argument("--gitlab", action="store_true")

    args = parser.parse_args()
