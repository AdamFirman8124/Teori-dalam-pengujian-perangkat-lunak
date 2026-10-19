

# Generated at 2022-06-14 05:15:06.766935
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    class _Github(Github):
        @staticmethod
        def session(
            raise_for_status=True, retry: Union[Retry, bool, int] = True
        ) -> Session:
            import requests_mock

            session = build_requests_session(
                raise_for_status=raise_for_status, retry=retry
            )
            adapter = requests_mock.Adapter()
            with requests_mock.mock() as m:
                m.get(
                    "https://api.github.com/repos/somenamespace/somerepo/commits/eb4e4c4c4a4c4c4c4c4c4a4c4c4a4c4c4c4aa4c/status",
                    json={"state": "success"},
                )

# Generated at 2022-06-14 05:15:07.349249
# Unit test for function get_hvcs
def test_get_hvcs():
    assert get_hvcs() == Github

# Generated at 2022-06-14 05:15:08.145515
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.check_build_status("foo", "bar", "SHA_HASH")

# Generated at 2022-06-14 05:15:13.465426
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    from axion import config

    config.set("hvcs_domain", "gitlab.example.com")
    config.set("GL_TOKEN", "abc")

    owner = "namespace"
    repo = "repo"
    ref = "1234567"

    # TEST 1: return False
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.json_data = [
                {
                    "id": 123,
                    "status": "pending",
                    "allow_failure": False,
                    "name": "job 1",
                },
                {
                    "id": 456,
                    "status": "pending",
                    "allow_failure": False,
                    "name": "job 2",
                },
            ]


# Generated at 2022-06-14 05:15:15.858368
# Unit test for method auth of class Github
def test_Github_auth():
    print("Starting test of method auth of class Github")
    method = Github.auth
    assert method(None), "Should be callable"

# Generated at 2022-06-14 05:15:25.042159
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class Jobs:
        def list():
            return [{"status": "1", "allow_failure": "1", "name": "1"}, {"status": "2", "allow_failure": "0", "name": "2"}]

    class Commit:
        def get(a):
            return Commit

        def statuses():
            return Jobs

    class Project:
        def get(b):
            return Project

        def commits():
            return Commit

    class Gitlab:
        def auth():
            return None

        def projects():
            return Project

    assert Gitlab.check_build_status(owner="owner", repo="repo", ref="ref") == False



# Generated at 2022-06-14 05:15:31.581870
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() == os.environ.get("CI_SERVER_HOST")
    # Mock the environment variable
    os.environ["CI_SERVER_HOST"] = "myhost"
    assert Gitlab.domain() == "myhost"

    # Clean up
    os.environ.pop("CI_SERVER_HOST")


# Generated at 2022-06-14 05:15:35.314197
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() in ["gitlab.com", "gitlab.com/api/v4", "gitlab.com/api/v3", "gitlab.com/api/v2"]


# Generated at 2022-06-14 05:15:41.686377
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # In the CI environment, the commit hash is in the environment variable CI_COMMIT_SHA
    # https://docs.gitlab.com/ee/ci/variables/predefined_variables.html#ci-environment-variables
    commit_hash = os.environ.get("CI_COMMIT_SHA")
    assert commit_hash != None
    assert Gitlab.check_build_status("nsimagelab", "hypnotoad", commit_hash) == True
    assert Gitlab.check_build_status("nsimagelab", "hypnotoad", "1234567890123456789012345678901234567890") == False
    

# Generated at 2022-06-14 05:15:46.119727
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("ProjetOasis", "test-project", "ee5eba3a3dfc5d18b5e07b6c21b3cee936f2d6b0")

# Generated at 2022-06-14 05:19:07.266592
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class TestGitlab(Gitlab):
        def token(self):
            return "TestToken"

    with HTTMock(mock_github_token):
        github_client = TestGitlab()
        github_client.check_build_status(owner="TestOwner", repo="TestRepo", ref="TestRef")

# Generated at 2022-06-14 05:19:12.172310
# Unit test for function get_hvcs
def test_get_hvcs():
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()


# Generated at 2022-06-14 05:19:19.265724
# Unit test for method auth of class Github
def test_Github_auth():
    # defaults to None if no token is available
    assert not Github.auth()

    # returns instance of TokenAuth if token is available
    os.environ["GH_TOKEN"] = "myToken"
    assert isinstance(Github.auth(), TokenAuth)
    del os.environ["GH_TOKEN"]


# Generated at 2022-06-14 05:19:21.291606
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert "gitlab.com" == Gitlab.domain()



# Generated at 2022-06-14 05:19:23.484816
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    assert not Github.check_build_status("owner", "repo", "ref")



# Generated at 2022-06-14 05:19:36.131203
# Unit test for function get_hvcs
def test_get_hvcs():
    """Unit test for function get_hvcs"""
    # Set environment variables
    os.environ["GH_TOKEN"] = "12345"
    os.environ["GL_TOKEN"] = "54321"

    # Test with Github
    config.import_dict({"hvcs": "github"})
    hvcs = get_hvcs()
    assert type(hvcs).__name__ == "Github"
    assert hvcs.api_url() == "https://api.github.com"
    assert hvcs.token() == "12345"
    assert hvcs.auth() is not None

    # Test with Gitlab
    config.import_dict({"hvcs": "gitlab"})
    hvcs = get_hvcs()
    assert type(hvcs).__

# Generated at 2022-06-14 05:19:37.663006
# Unit test for function get_hvcs
def test_get_hvcs():
    assert Github == get_hvcs()


# Generated at 2022-06-14 05:19:46.949588
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    mocker.patch("gitlab.Gitlab.auth", return_value=None)
    mocker.patch("gitlab.Gitlab.projects.get", return_value=mocker.MagicMock())
    mocker.patch(
        "gitlab.Gitlab.projects.get().commits.get", return_value=mocker.MagicMock()
    )
    mocker.patch(
        "gitlab.Gitlab.projects.get().commits.get().statuses.list",
        return_value=[
            {"status": "success", "name": "build_job"},
            {"status": "success", "name": "test_job"},
        ],
    )
    assert Gitlab.check_build_status("my_owner", "my_repo", "my_ref") == True

# Generated at 2022-06-14 05:19:53.641751
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert (
        Gitlab.check_build_status(
            owner="owner",
            repo="repo",
            ref="84f5a2b63c3925eaeb87d74a25d372e3e99a9ed9",
        )
        is False
    )



# Generated at 2022-06-14 05:20:04.609410
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    #Check the status of a finished pipeline
    assert Gitlab.check_build_status(
        "ENESCTF", "DSSHelper-private", "0825fbebea232a1272e96aca8f859a7b9e9b4779"
    ) == True
    #Check the status of a pending pipeline
    assert Gitlab.check_build_status(
        "ENESCTF", "DSSHelper", "f04d46f15cc8a379a3d7c2060fd2c1bd6113ec06",
    ) == False
    #Check the status of a failed pipeline