

# Generated at 2022-06-14 05:14:40.537735
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"

# Generated at 2022-06-14 05:14:42.257224
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() == "gitlab.com"


# Generated at 2022-06-14 05:14:43.997815
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() == "gitlab.com"


# Generated at 2022-06-14 05:14:49.004160
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    import uuid
    random_domain = str(uuid.uuid4())
    os.environ["CI_SERVER_HOST"] = random_domain
    assert random_domain == Gitlab.domain()
    del os.environ["CI_SERVER_HOST"]



# Generated at 2022-06-14 05:14:56.638288
# Unit test for function get_hvcs
def test_get_hvcs():
    class TestConfig(object):
        def __init__(self, hvcs):
            self.hvcs = hvcs

        def get(self, key):
            return self.hvcs

    # Test when hvcs is not a valid option from the configuration file
    with raises(ImproperConfigurationError) as excinfo:
        config = TestConfig("not_a_valid_option")
        get_hvcs()

    # Test when hvcs is a valid option from the configuration file
    config = TestConfig("github")
    assert get_hvcs() == Github



# Generated at 2022-06-14 05:14:57.976055
# Unit test for function get_hvcs
def test_get_hvcs():
    assert get_hvcs() in [Github, Gitlab]



# Generated at 2022-06-14 05:14:59.468787
# Unit test for function get_hvcs
def test_get_hvcs():
    """Unit test for function get_hvcs"""
    assert get_hvcs() == Github



# Generated at 2022-06-14 05:15:08.131928
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"

    # Set GH_TOKEN environment variable and expect configured domain
    os.environ["GH_TOKEN"] = "0" * 40

    assert Github.domain() == "github.com"

    # Set GH_TOKEN environment variable and expect custom domain
    os.environ["GH_TOKEN"] = "0" * 40
    os.environ["HVCS_DOMAIN"] = "github.com"

    assert Github.domain() == "github.com"



# Generated at 2022-06-14 05:15:12.271800
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    os.environ["GL_TOKEN"] = "91PdUv25KED6WkU6BwU6"
    assert not Gitlab.check_build_status("sot", "sot-doc", "d3c6f0ff75b2c0a3ff44d9f9c7ba87a4d4b3fa4e")
    assert Gitlab.check_build_status("sot", "sot-robot", "d3c6f0ff75b2c0a3ff44d9f9c7ba87a4d4b3fa4e")



# Generated at 2022-06-14 05:15:17.068050
# Unit test for function get_hvcs
def test_get_hvcs():
    # hvcs is provided and is in the list of possible HVCS
    config.set("hvcs", "github")
    assert isinstance(get_hvcs(), Github)
    assert isinstance(get_hvcs(), Base)

    config.set("hvcs", "gitlab")
    assert isinstance(get_hvcs(), Gitlab)
    assert isinstance(get_hvcs(), Base)

    # hvcs is provided but is not in the list of possible HVCS
    config.set("hvcs", "foo")
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()

    # hvcs is not provided
    config.set("hvcs", None)
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()



# Generated at 2022-06-14 05:18:55.522281
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    hvcs = os.environ.get("HVCS")
    assert hvcs == "gitlab"
    owner = os.environ.get("CI_PROJECT_NAMESPACE")
    repo = os.environ.get("CI_PROJECT_NAME")
    ref = os.environ.get("CI_COMMIT_SHA")
    assert Gitlab.check_build_status(owner, repo, ref)
    # Modify the test case to test a failed build
    assert not Gitlab.check_build_status(owner, repo, "f4df1f2c932b6d5b74f16b6f5adadc9400a7b7d1")



# Generated at 2022-06-14 05:19:00.542619
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.check_build_status("francois-boulogne","cooking_upstream_CI", '35c69f503337dce31e2d348335a6632f74e1b9d9')


# Generated at 2022-06-14 05:19:04.627105
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner = 'gl1'
    repo = 'r1'
    ref = '11'
    res = Gitlab.check_build_status(owner, repo, ref)
    assert isinstance(res, bool) and res == True


# Generated at 2022-06-14 05:19:11.008143
# Unit test for method auth of class Github
def test_Github_auth():
    assert not config.get("hvcs_token"), "hvcs_token not set in config"
    assert not Github.auth()

    os.environ["GH_TOKEN"] = "abc"
    assert Github.auth() == TokenAuth("abc")

    del os.environ["GH_TOKEN"]
    assert not Github.auth()


# Generated at 2022-06-14 05:19:19.306978
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Unit test for method check_build_status of class Gitlab"""
    class UnitTestGitlab(Gitlab):
        """Test class for Gitlab.check_build_status"""
        @classmethod
        @LoggedFunction(logger)
        def check_build_status(cls, owner: str, repo: str, ref: str) -> bool:
            # Mock the call to Gitlab.check_build_status to avoid
            # https://gitlab.com/charmhub/bot/issues/15
            return True

    class UnitTestFailureGitlab(Gitlab):
        """Test class for Gitlab.check_build_status"""

# Generated at 2022-06-14 05:19:31.362493
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class MockStatus:
        def __init__(self, status):
            self.status = {"status": status}

    class MockJob:
        def __init__(self, status="success", name="test", allow_failure=False):
            self.status = MockStatus(status)
            self.name = name
            self.allow_failure = allow_failure

    class MockJobs:
        def __init__(self, job_list):
            self.jobs = [MockJob(**job) for job in job_list]

        def list(self):
            return self.jobs

    class MockCommit:
        def __init__(self, ref):
            self.ref = ref


# Generated at 2022-06-14 05:19:39.450000
# Unit test for method auth of class Github
def test_Github_auth():
    """
    GITHUB_TOKEN='' python -c "from semantic_release import hvcs; print(hvcs.Github.auth())"
    GITHUB_TOKEN='' python -c "from semantic_release import hvcs; print(hvcs.Github.auth())"
    GITHUB_TOKEN='test' python -c "from semantic_release import hvcs; print(hvcs.Github.auth())"
    """



# Generated at 2022-06-14 05:19:41.937433
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url()[:len(Github.DEFAULT_DOMAIN)] == Github.DEFAULT_DOMAIN


# Generated at 2022-06-14 05:19:47.195855
# Unit test for function get_hvcs
def test_get_hvcs():
    """
    Test function get_hvcs
    """
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()
    config._config["hvcs"] = "github"
    assert isinstance(get_hvcs(), Github)
    config._config["hvcs"] = "gitlab"
    assert isinstance(get_hvcs(), Gitlab)

# Generated at 2022-06-14 05:20:01.035248
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("pcdshub", "pcdshub", "e7543de6ee3d3cb45e64b8f6e7fca5a2918a2da6") == True
    assert Gitlab.check_build_status("pcdshub", "pcdshub", "6f7ae9e8f42a80f5bacdab7d6c82017837234f6d") == True
    assert Gitlab.check_build_status("pcdshub", "pcdshub", "5f5a5e5e5b5a5a5f4b4b4c4c4a4c4e4e4a4a4a4f3b3c3") == False



# Generated at 2022-06-14 05:22:31.897420
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.token = MagicMock(return_value="goodToken")    
    Gitlab.domain = MagicMock(return_value="https://gitlab.com") #Should be "gitlab.com/"
    Gitlab.api_url = MagicMock(return_value="https://gitlab.com/") #Should be "gitlab.com/"

    assert Gitlab.check_build_status("group", "project", "1adc55167035b2c207f96d54b19f30c1f12fe297") == True

# Generated at 2022-06-14 05:22:37.067046
# Unit test for function get_hvcs
def test_get_hvcs():
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()
    config.hvcs = "github"
    assert isinstance(get_hvcs(), Github)
    config.hvcs = "gitlab"
    assert isinstance(get_hvcs(), Gitlab)



# Generated at 2022-06-14 05:22:41.345553
# Unit test for function get_hvcs
def test_get_hvcs():
    config.configure({'hvcs': 'github'})
    hvcs = get_hvcs()
    assert hvcs.name == 'Github'
    with pytest.raises(ImproperConfigurationError):
        config.configure({'hvcs': 'gitlab'})
        hvcs = get_hvcs()
        assert False

