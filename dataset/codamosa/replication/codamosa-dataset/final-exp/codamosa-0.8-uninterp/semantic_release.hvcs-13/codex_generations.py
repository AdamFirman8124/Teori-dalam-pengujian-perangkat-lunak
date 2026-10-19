

# Generated at 2022-06-14 05:13:55.791818
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"


# Generated at 2022-06-14 05:13:57.211826
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("SUSE", "salt", "8dd3eed")


# Generated at 2022-06-14 05:14:00.189399
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Build success
    # ----------------------------
    # Build failed but allowed to fail
    # ----------------------------
    # Build failed and not allowed to fail
    pass


# Generated at 2022-06-14 05:14:06.677748
# Unit test for function get_hvcs
def test_get_hvcs():
    config.set_hvcs(None)
    assert get_hvcs() == Github
    config.set_hvcs('Github')
    assert get_hvcs() == Github
    config.set_hvcs('Gitlab')
    assert get_hvcs() == Gitlab
    def test_get_hvcs_incorrect_hvcs():
        config.set_hvcs('stackoverflow')
        assert get_hvcs() == ImproperConfigurationError

# Generated at 2022-06-14 05:14:17.732491
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class MockProject:
        class MockCommit:
            class MockStatuses:
                def list(self, ):
                    return [{"name": "test_job", "status": "success", "allow_failure": None}]

            def __init__(self):
                self.statuses = self.MockStatuses()

            def get(self, ref):
                self.ref = ref
                return self

        def __init__(self):
            self.commits = self.MockCommit()

        def get(self, project):
            self.project = project
            return self

    class MockGitlab:
        def __init__(self):
            self.projects = MockProject()

    gitlab.Gitlab = MockGitlab

# Generated at 2022-06-14 05:14:20.892469
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    owner = "nokbur"
    repo = "python-semantic-release"
    ref = ":ref:"
    assert Github.check_build_status(owner, repo, ref)



# Generated at 2022-06-14 05:14:23.253078
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"

# Generated at 2022-06-14 05:14:24.982728
# Unit test for method auth of class Github
def test_Github_auth():
    inst = Github()
    assert inst.auth() is None



# Generated at 2022-06-14 05:14:35.711411
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    class Gitlab(Base):
        """Gitlab helper class"""

        DEFAULT_DOMAIN = "gitlab.com"

        @staticmethod
        def domain() -> str:
            """Gitlab domain property

            :return: The Gitlab domain
            """
            hvcs_domain = config.get("hvcs_domain")
            domain = hvcs_domain if hvcs_domain else Gitlab.DEFAULT_DOMAIN
            return domain

        @staticmethod
        def api_url() -> str:
            """Gitlab api_url property

            :return: The Gitlab API URL
            """
            hvcs_domain = config.get("hvcs_domain")
            hostname = hvcs_domain if hvcs_domain else "api." + Gitlab.DEFAULT_DOMAIN

# Generated at 2022-06-14 05:14:38.334985
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain()=="gitlab.com" 

# Generated at 2022-06-14 05:15:48.482578
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status(
        "openstack", "releases", "7e2ea1b61d7dc0a8e0b7c48f96acfc5bb1d9f9b3"
    ) is True
    assert Gitlab.check_build_status(
        "openstack", "releases", "d7e2ea1b61d7dc0a8e0b7c48f96acfc5bb1d9f9b3"
    ) is not True



# Generated at 2022-06-14 05:15:53.688455
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    from semantic_release import github
    from semantic_release import analyze_commits
    from semantic_release.version_service import VersionService

    path_to_project = "/Users/subodh/Documents/workspace/semantic-release-test"
    config_path = "/Users/subodh/Documents/workspace/semantic-release-test/.config.cfg"
    # load the config file
    config.load(config_path)
    # print(config['hvcs'])

    # Read the changelog and check if the release notes can be generated
    changelog = analyze_commits.get_changelog(path_to_project)
    # print(changelog)
    assert changelog != ""

    # Get the next version number

# Generated at 2022-06-14 05:16:03.770322
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Arrange
    gitlab_vcs_domain = 'https://gitlab.com'
    gitlab_api_url = 'https://gitlab.com'
    gitlab_token = 'mock-token'
    gitlab_owner = 'mock-owner'
    gitlab_repo = 'mock-repo'
    gitlab_ref = 'mock-ref'
    mock_response = {
        "status": "failed", "name": "jobName", "allow_failure": False
    }

    with patch.object(gitlab, "Gitlab") as mock_gitlab_constructor:
        mock_gl = Mock()
        mock_gl.projects.get.return_value.commits.get.return_value.statuses.list.return_value = [mock_response]
        mock_

# Generated at 2022-06-14 05:16:14.168715
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    try:
        os.environ["GL_TOKEN"] = " "
    except KeyError:
        print("Environment variable GL_TOKEN not found")
        return
    owner = "project-h"
    repo = "h"
    ref = "a90a7a223b17cad4d9670f4f4e074a4b8f080b13"
    assert Gitlab.check_build_status(owner, repo, ref) == False
    ref = "dc0535a7a66bdfd22ddb24dfc30a8d4a4f4b4f4e"
    assert Gitlab.check_build_status(owner, repo, ref) == True
    return

# Generated at 2022-06-14 05:16:23.699124
# Unit test for function get_hvcs
def test_get_hvcs():
    # with a valid option
    config.set("hvcs", "github")
    assert get_hvcs() == Github

    # with another valid option
    config.set("hvcs", "gitlab")
    assert get_hvcs() == Gitlab

    # with an invalid option
    config.set("hvcs", "invalid")
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()



# Generated at 2022-06-14 05:16:24.916529
# Unit test for method auth of class Github
def test_Github_auth():
    assert Github.auth() is None



# Generated at 2022-06-14 05:16:28.170274
# Unit test for function get_hvcs
def test_get_hvcs():
    config.set("hvcs", "gitlab")
    assert get_hvcs() is Gitlab
    config.set("hvcs", "github")
    assert get_hvcs() is Github



# Generated at 2022-06-14 05:16:34.247743
# Unit test for function get_hvcs
def test_get_hvcs():
    """Test function get_hvcs"""
    config.set("hvcs", "GitHub")
    assert get_hvcs() == Github
    config.set("hvcs", "Gitlab")
    assert get_hvcs() == Gitlab
    # Test the exception raise if an unknown option is provided
    try:
        config.set("hvcs", "Foo")
        get_hvcs()
        assert False
    except ImproperConfigurationError:
        assert True



# Generated at 2022-06-14 05:16:39.847433
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    build_status = Gitlab.check_build_status("Qiskit", "qiskit-ignis", "4fe8e1165a648a2082a60dc9851ac8bce6289d00")
    assert build_status == True, "check_build_status method of class Gitlab failed"

# Generated at 2022-06-14 05:16:42.654432
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    token = "1"
    r = "a"
    ta = TokenAuth(token)
    assert ta(r)



# Generated at 2022-06-14 05:18:45.521566
# Unit test for function get_hvcs
def test_get_hvcs():
    """Test that get_hvcs() returns a valid object"""
    logger.info("Testing function get_hvcs()")

    class_name = "Github"
    assert get_hvcs().__class__.__name__ == class_name
    assert get_hvcs().__class__.__name__ == class_name



# Generated at 2022-06-14 05:18:51.706106
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    owner = "TensorBoard"
    repo = "tensorboard"
    ref = "f4b923a9f1d1c6b21e6c680f6a59e6dceca6a64f"
    expected = True
    response = Github.check_build_status(owner, repo, ref)
    assert response == expected



# Generated at 2022-06-14 05:18:54.441096
# Unit test for function get_hvcs
def test_get_hvcs():
    assert get_hvcs() == Github
    config.set("hvcs", "gitlab")
    assert get_hvcs() == Gitlab

# Generated at 2022-06-14 05:19:03.338919
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert(Gitlab.check_build_status("sclorg","devtoolset-8","229e6a3e88b72f6e098e5b7336a68a9a922e5c5f") == True)
    assert(Gitlab.check_build_status("sclorg","devtoolset-9","7f22d5c5f7d1e5703dc0a2a8e43b0ac2e6c9e6f1") == False)

# Generated at 2022-06-14 05:19:10.198997
# Unit test for method domain of class Github
def test_Github_domain():
    # Check if method returns correct value for default domain
    assert Github.domain() == "github.com"

    # Check if method returns correct value for custom domain
    config.set("hvcs_domain", "github.enterprise.com")
    assert Github.domain() == "github.enterprise.com"
    config.remove("hvcs_domain")



# Generated at 2022-06-14 05:19:11.414031
# Unit test for method domain of class Github
def test_Github_domain():
    return Github.domain()


# Generated at 2022-06-14 05:19:14.254829
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    domain = config.get("hvcs_domain", os.environ.get("CI_SERVER_HOST"))
    assert Gitlab.domain() == domain if domain else "gitlab.com"

# Generated at 2022-06-14 05:19:18.112057
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() == os.environ.get("CI_SERVER_HOST") or "gitlab.com"


# Generated at 2022-06-14 05:19:20.036097
# Unit test for method auth of class Github
def test_Github_auth():
    assert Github.auth() == TokenAuth("None")



# Generated at 2022-06-14 05:19:21.412457
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain()

