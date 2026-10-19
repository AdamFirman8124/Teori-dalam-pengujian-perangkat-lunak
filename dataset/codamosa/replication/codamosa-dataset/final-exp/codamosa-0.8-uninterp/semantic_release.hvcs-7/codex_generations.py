

# Generated at 2022-06-14 05:14:32.879386
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner = config.get("hvcs_domain", os.environ.get("CI_SERVER_HOST")).split('.')[0]
    repo = "python-gitlab"
    ref = "61f5c1b2b5d5c3f0d1283c8f417a4f9ea7da3aeb"
    success = Gitlab.check_build_status(owner, repo, ref)
    assert success is True


# Generated at 2022-06-14 05:14:37.051080
# Unit test for function get_hvcs
def test_get_hvcs():
    # Test with a valid option
    config.config["hvcs"] = "github"
    assert isinstance(get_hvcs(), Github)
    # Test with an invalid option
    config.config["hvcs"] = "foobar"
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()

# Generated at 2022-06-14 05:14:39.750078
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"

# Generated at 2022-06-14 05:14:41.469864
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"



# Generated at 2022-06-14 05:14:47.961841
# Unit test for method api_url of class Github
def test_Github_api_url():
    hvcs_domain = "domain.com"
    config.set("hvcs_domain", hvcs_domain)
    url = Github.api_url()
    assert url == "https://api.domain.com"

    config.set("hvcs_domain", None)
    url = Github.api_url()
    assert url == "https://api.github.com"





# Generated at 2022-06-14 05:14:50.083992
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"



# Generated at 2022-06-14 05:14:55.815586
# Unit test for function get_hvcs
def test_get_hvcs():
    """Unit test for function get_hvcs"""
    # Test invalid hvcs
    with pytest.raises(ImproperConfigurationError):
        assert get_hvcs() == None

    # Test GitHub
    config.set("hvcs", "github")
    assert get_hvcs() == Github

    # Test Gitlab
    config.set("hvcs", "gitlab")
    assert get_hvcs() == Gitlab



# Generated at 2022-06-14 05:14:58.304825
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    """Unittest for Gitlab.domain()"""
    assert Gitlab.domain() == "gitlab.com"
    os.environ["CI_SERVER_HOST"] = "foo"
    assert Gitlab.domain() == "foo"

# Generated at 2022-06-14 05:15:01.122337
# Unit test for function get_hvcs
def test_get_hvcs():
    # Test if we get the right class when we provide github as a config
    assert get_hvcs() == Github
    # Test if we get the right class when we provide gitlab as a config
    config.set("hvcs", "gitlab")
    assert get_hvcs() == Gitlab



# Generated at 2022-06-14 05:15:06.532066
# Unit test for method check_build_status of class Gitlab

# Generated at 2022-06-14 05:16:35.990932
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain()

# Generated at 2022-06-14 05:16:38.229692
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"


# Generated at 2022-06-14 05:16:47.963486
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    if os.environ.get("CI_ENVIRONMENT_URL"):
        # We are in Gitlab pipeline
        # GL_TOKEN is defined in Gitlab pipeline
        test_domain = "gitlab.com"
        test_owner = "peopledoc"
        test_repo = "testing"
        test_ref = "0ef0e2e4d4b1a2dbc7f3a3f8b2098e45296f6bf7"

        # List of status from jobs of test_ref
        # This list is generated from the current pipelines

# Generated at 2022-06-14 05:16:55.178297
# Unit test for function get_hvcs
def test_get_hvcs():
    config.set_section("github")
    assert isinstance(get_hvcs(), Github)
    config.set_section("gitlab")
    assert isinstance(get_hvcs(), Gitlab)
    config.set_section("travis")
    assert isinstance(get_hvcs(), Github)


# Generated at 2022-06-14 05:17:07.097919
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Test data
    repo_info = {
        "owner": "gitlab-org",
        "repo": "gitlab-test",
        "ref": "5d5b0a37b9e0946bf9a79dc6d58ea6a856c5f5d5"
    }

    # Test case no.1: status of jobs is "pending"
    print(f"\nTest case no.1: status of jobs is 'pending'\n")
    with patch(
        "release_exporter.hvcs.gitlab.Gitlab.check_build_status",
        return_value=True
    ) as mocked_check_pending:
        assert Gitlab.check_build_status(**repo_info) == True
    mocked_check_pending.assert_called_once

# Generated at 2022-06-14 05:17:10.407036
# Unit test for method auth of class Github
def test_Github_auth():
    """Github.auth
    """
    assert Github.auth() == None

    os.environ["GH_TOKEN"] = "token"
    assert Github.auth() == TokenAuth("token")

    del os.environ["GH_TOKEN"]
    assert Github.auth() == None



# Generated at 2022-06-14 05:17:22.095145
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Create mockup of Gitlab.session()
    # Create mock object of github.Github object
    mock_gitlab_object = mock.Mock(spec=gitlab.Gitlab)
    gl = mock_gitlab_object.return_value
    gl.auth.return_value = True
    mock_project_object = mock.Mock(spec=gitlab.objects.Project)
    mock_commit_object = mock.Mock(spec=gitlab.objects.ProjectCommit)
    mock_statuses_object = mock.Mock(spec=gitlab.objects.ProjectCommitStatuses)
    gl.projects.get.return_value = mock_project_object
    mock_project_object.commits.get.return_value = mock_commit_object
    mock_commit_object.statuses.list.return_value

# Generated at 2022-06-14 05:17:24.223980
# Unit test for function get_hvcs
def test_get_hvcs():
    config._config = {"hvcs": "github"}
    assert get_hvcs() == Github

    config._config = {"hvcs": "gitlab"}
    assert get_hvcs() == Gitlab

    config._config = {"hvcs": "nokey"}
    assert_raises(ImproperConfigurationError, get_hvcs)

# Generated at 2022-06-14 05:17:28.680570
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("OWNER", "REPO", "96b0e3c4708a55fd5fdccfe5d9eb9ea5c5e5a5a5") is False
# Unit tests for class Github

# Generated at 2022-06-14 05:17:35.962792
# Unit test for method auth of class Github
def test_Github_auth():
    config["hvcs_domain"] = None
    config["hvcs_token"] = None
    assert Github.auth() == None
    config["hvcs_domain"] = "github.com"
    os.environ["GH_TOKEN"] = "some_token"
    assert Github.auth() == TokenAuth("some_token")
    config["hvcs_domain"] = "github.com"
    config["hvcs_token"] = "other_token"
    os.environ["GH_TOKEN"] = "some_token"
    assert Github.auth() == TokenAuth("other_token")

# Generated at 2022-06-14 05:20:54.492201
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """
    This test unit check the method check_build_status of class Gitlab
    """
    # TODO: Change url for test instance
    url = "https://gitlab.com/"
    # Define a function that return the json object of a given url
    def mock_request(url, *args, **kwargs):
        """
        This function return a json object from the given url
        """
        class Request:
            """
            This class define an object Request with a method json
            """
            def json(self):
                """
                This function return a json object
                """
                return {"status": "success"}
        return Request()
    import gitlab.v4.objects
    # Mock the method request of class Gitlab to return a json object
    gitlab.v4.objects.Gitlab._raw_get = mock_

# Generated at 2022-06-14 05:20:59.291344
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner = "gimelbrant"
    repo = "cloudformation-cost-estimator"
    ref = "0a45545a3d3feb82dfb3dd80be72a3bff84ceb05"
    assert Gitlab.check_build_status(owner, repo, ref) == True

# Generated at 2022-06-14 05:21:03.983571
# Unit test for method auth of class Github
def test_Github_auth():
    instance = Github()
    inst_func_auth = getattr(instance, "auth", None)
    if inst_func_auth is None:
        raise Exception('Method "auth" not implemented!')

# Generated at 2022-06-14 05:21:10.359968
# Unit test for method auth of class Github
def test_Github_auth():
    """
    Test for the class Github and it's method auth
    """
    hvcs_token = config.get("hvcs_token")
    token = hvcs_token if hvcs_token else os.environ.get("GH_TOKEN")
    assert Github.auth() == TokenAuth(token) or Github.auth() is None



# Generated at 2022-06-14 05:21:13.196994
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():  # for unit test
    r = Gitlab.check_build_status("qalab", "qalab", "2e38d3ea3a94f9e3dfff510d0b3e8dbcc13b1ed6")
    assert r is False

# Generated at 2022-06-14 05:21:17.494820
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """
    Function to test the method check_build_status of class Gitlab
    :return:
    """
    assert Gitlab.check_build_status("test", "test1", "refs/tags/test") is False


# Generated at 2022-06-14 05:21:21.007890
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    assert Github.check_build_status("tensorflow", "tensorboard", "ffa5a0f") == False



# Generated at 2022-06-14 05:21:22.577660
# Unit test for function get_hvcs
def test_get_hvcs():
    assert get_hvcs() == Github

# Generated at 2022-06-14 05:21:26.161472
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # test for positive case
    owner = "SALAB"
    repo = "test"
    ref = "123"
    assert Gitlab.check_build_status(owner, repo, ref) == True

# Generated at 2022-06-14 05:21:29.130420
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
  assert Github.check_build_status('Shubham1412200', 'semantic_release', 'd913d9de17cadb51329c34e45bfce8f17409ccc4')
