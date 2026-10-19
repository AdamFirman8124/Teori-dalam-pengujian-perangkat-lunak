

# Generated at 2022-06-14 05:14:37.051797
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    # Test with environment variable set
    os.environ["CI_SERVER_HOST"] = "gitlab.example.com"
    assert Gitlab.domain() == "gitlab.example.com"

    # Test with config.yaml set
    config.set("hvcs_domain", "gitlab.example.com")
    assert Gitlab.domain() == "gitlab.example.com"
    config.set("hvcs_domain", None)
    os.environ["CI_SERVER_HOST"] = None


# Generated at 2022-06-14 05:14:50.252404
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():

    os.environ["GL_TOKEN"] = "test_token"

    def mock_projects_get(*args, **kwargs):
        # mock function for class gitlab.v4.objects.ProjectManager
        class MockProject:
            def commits_get(*args, **kwargs):
                # mock function for class gitlab.v4.objects.ProjectCommit
                class MockCommit:
                    def statuses_list(*args, **kwargs):
                        # mock function for class gitlab.v4.objects.ProjectCommitStatuses
                        return [
                            {"status": "success", "name": "job1"},
                            {"status": "pending", "name": "job2"},
                        ]

                return MockCommit()

        return MockProject()

    def mock_auth(*args, **kwargs):
        return True

   

# Generated at 2022-06-14 05:14:52.001722
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == config.get("hvcs_domain", Github.DEFAULT_DOMAIN)

# Generated at 2022-06-14 05:14:55.187587
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("hail-vcs", "test", "2bcc7ff9d1e42b39eeb9a0dc69ec7b8d57d76f38") == False


# Generated at 2022-06-14 05:15:01.855437
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class FakeClass:
        class FakeSubClass:
            class FakeSubSubClass:
                pass
    gitlab.Gitlab.auth = lambda x: None
    gitlab.Gitlab.projects = FakeClass()
    gitlab.Gitlab.projects.get = lambda x: FakeClass()
    gitlab.Gitlab.projects.get.commits = FakeClass()
    gitlab.Gitlab.projects.get.commits.get = lambda x: FakeClass()
    gitlab.Gitlab.projects.get.commits.get.statuses = FakeClass()
    gitlab.Gitlab.projects.get.commits.get.statuses.list = lambda x: [
        {"status": "success"},
        {"status": "failed", "allow_failure": True},
    ]
    assert Gitlab.check

# Generated at 2022-06-14 05:15:06.946582
# Unit test for function get_hvcs
def test_get_hvcs():
    from .config import Config
    from tempfile import TemporaryDirectory
    from textwrap import dedent

    with TemporaryDirectory() as folder:
        with open(os.path.join(folder, "config.ini"), "w") as f:
            f.write(
                dedent(
                    """
                    [default]
                    hvcs: gitlab
                    """
                )
            )

        Config.load()
        assert get_hvcs() == Gitlab

        with open(os.path.join(folder, "config.ini"), "w") as f:
            f.write(
                dedent(
                    """
                    [default]
                    hvcs: github
                    """
                )
            )

        Config.load()
        assert get_hvcs() == Github

# Generated at 2022-06-14 05:15:10.536192
# Unit test for function get_hvcs
def test_get_hvcs():
    # testcase: hvcs provided is github
    config.set("hvcs", "github")
    assert type(get_hvcs()) == Github

    # testcase: hvcs provided is gitlab
    config.set("hvcs", "gitlab")
    assert type(get_hvcs()) == Gitlab

    # testcase: hvcs provided is not valid
    config.set("hvcs", "")
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()



# Generated at 2022-06-14 05:15:15.737301
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Test the case when everything is successful
    assert Gitlab.check_build_status("test_owner", "test_repo", "test_ref") is True

    # Test the case when there is only one failed job

# Generated at 2022-06-14 05:15:17.574340
# Unit test for method domain of class Github
def test_Github_domain():  
    assert(Github.domain() == 'github.com')

# Generated at 2022-06-14 05:15:28.162722
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class Gitlab_mocked(Gitlab):
        """Gitlab mocked class"""
        class Gitlab_mocked_projects():
            """Gitlab class mocked projects"""
            class Gitlab_mocked_projects_commits():
                """Gitlab class mocked projects commits"""
                class Gitlab_mocked_projects_commits_statuses():
                    """Gitlab class mocked projects commits status"""
                    def list(self):
                        return [{"status": "failed", "allow_failure": True}]
            
                def get(self,ref):
                    return self.Gitlab_mocked_projects_commits_statuses()
            def get(self,owner):
                return self.Gitlab_mocked_projects_commits()
        def projects(self):
            return self.Gitlab_mocked_projects

# Generated at 2022-06-14 05:17:51.783976
# Unit test for function get_hvcs
def test_get_hvcs():
    assert get_hvcs() == Github

# Generated at 2022-06-14 05:17:54.717969
# Unit test for function get_hvcs
def test_get_hvcs():
    config.options["hvcs"] = "github"
    assert isinstance(get_hvcs(), Github)



# Generated at 2022-06-14 05:17:59.356989
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    r = requests.Request()
    token = "this is my token"

    auth = TokenAuth(token)
    auth(r)

    assert r.headers["Authorization"] == f"token {token}"



# Generated at 2022-06-14 05:18:12.247692
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    import time

    class TestGitlab():
        def __init__(self):
            self.domain = "domain"

        def auth(self):
            pass

        class projects():
            def __init__(self):
                pass

            class get():
                def __init__(self, path):
                    self.path = path

                class commits():
                    def __init__(self):
                        pass

                    class get():
                        def __init__(self, sha):
                            self.sha = sha

                        class statuses():
                            def __init__(self):
                                pass

                            class list():
                                def __init__(self):
                                    pass


# Generated at 2022-06-14 05:18:13.859061
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("namespace", "repository", "4567890123456789012345678901234567890123") == True

# Generated at 2022-06-14 05:18:17.327728
# Unit test for method domain of class Github
def test_Github_domain():
    expected_value = "github.com"
    actual_value = Github.domain()

    assert actual_value == expected_value



# Generated at 2022-06-14 05:18:23.151439
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    token = "XXXX"
    request = "request"
    assert_token = "token {token}"
    assert_expected = {
        "Authorization": assert_token.format(token=token)
    }
    auth = TokenAuth(token)
    assert auth(request).headers == assert_expected
    auth = TokenAuth(None)
    assert auth(request).headers == {}



# Generated at 2022-06-14 05:18:24.602873
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("test", "test", "test") == True

# Generated at 2022-06-14 05:18:29.742793
# Unit test for method auth of class Github
def test_Github_auth():
    token = "token"
    auth = TokenAuth(token)
    assert auth == TokenAuth(token)
    assert auth != TokenAuth("other-token")
    assert auth != None



# Generated at 2022-06-14 05:18:31.468823
# Unit test for method domain of class Github
def test_Github_domain():
    assert 'github.com' == Github.domain()


# Generated at 2022-06-14 05:21:40.966916
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():

    gitlab = Gitlab()
    assert gitlab.check_build_status("pihizi", "golang_cli_arguments", "5b5e5b4a4bdfd4fd5caf4223a2ec3a3bfe2ec254")
    assert gitlab.check_build_status("pihizi", "golang_cli_arguments", "0ebbd9dc9e392e7b8ac8ac23d96f0d1f3a7c26d1")
    assert not gitlab.check_build_status("pihizi", "golang_cli_arguments", "d8eea34a05f9a9df891c8d1c66c7d07a96fadded")

# Generated at 2022-06-14 05:21:48.483170
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # It's unclear whether this test is useful, since the
    # only way we can test the failure condition is if we
    # fail the tests. I.e. if the tests pass, the method will return
    # True, and if we fail the tests, the method will return False.
    # For now we use the "fail" command as a crude simulation of
    # a failed job.
    #
    # Args:
    #    None
    #
    # Returns:
    #    None
    #
    # Raises:
    #    None

    result = Gitlab.check_build_status("owner", "repo", "ref")
    assert(result == True)
    sys.exit(1)


# Generated at 2022-06-14 05:21:49.772682
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("TheOwner", "TheRepo", "TheRef") == False

# Generated at 2022-06-14 05:21:50.835109
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"



# Generated at 2022-06-14 05:21:55.934997
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner = "Airship"
    repo = "airship-fuxi"
    ref = "beb911217f8be9c9e0d929a3aeeb8ec07d79f643"

    assert Gitlab.check_build_status(owner, repo, ref)

# Generated at 2022-06-14 05:21:58.819020
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    class TestConfig(Config):
        hvcs_domain = "gitlab.com"
    with Config.temporary(TestConfig):
        assert Gitlab.api_url() == "https://gitlab.com"
    assert Gitlab.domain() == "gitlab.com"


# Generated at 2022-06-14 05:22:04.655565
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    # Test with no environment variables
    Gitlab.domain()
    # Test with CI_SERVER_HOST environment variable
    os.environ["CI_SERVER_HOST"] = "host"
    Gitlab.domain()
    os.environ["CI_SERVER_HOST"] = ""



# Generated at 2022-06-14 05:22:16.231906
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # test if a status is returned by the request (the request did not fail)
    def test_check_build_status_no_fail():
        class MockGitlab:
            def __init__(self, mock):
                self.mock = mock

            def auth(self):
                pass

            def projects(self):
                return self

            def get(self, project):
                return self

            def commits(self):
                return self

            def get(self, project):
                return self

            def statuses(self):
                return self

            def list(self):
                return self.mock

        mock = [{"status": "success"}]
        gl = MockGitlab(mock)


# Generated at 2022-06-14 05:22:17.085095
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    pass

# Generated at 2022-06-14 05:22:19.627956
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"
