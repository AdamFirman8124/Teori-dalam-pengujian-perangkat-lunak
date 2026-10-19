

# Generated at 2022-06-14 05:14:41.719194
# Unit test for function get_hvcs
def test_get_hvcs():
    # Test that the function get_hvcs return the wanted HVCS helper class.
    hvcs = get_hvcs()
    assert hvcs is Gitlab

# Generated at 2022-06-14 05:14:48.660060
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.check_build_status("julab", "JubeatAnalyzer", "3fad3fadb0d07e096f88530a0a9f2ed1a3966de7")
    Gitlab.check_build_status("julab", "JubeatAnalyzer", "c94f8cbf8c5d359668cb2b697caa1e49aa9880ea")


# Generated at 2022-06-14 05:14:50.315280
# Unit test for function get_hvcs
def test_get_hvcs():
    """Test get_hvcs function"""
    pass

# Generated at 2022-06-14 05:14:55.257376
# Unit test for function get_hvcs
def test_get_hvcs():
    config.clear()
    config["hvcs"] = "github"
    assert get_hvcs() is Github
    config["hvcs"] = "gitlab"
    assert get_hvcs() is Gitlab
    config["hvcs"] = "bitbucket"
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()


# Generated at 2022-06-14 05:14:56.967036
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"



# Generated at 2022-06-14 05:15:01.389830
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    """Unit test for method check_build_status of class Github
    """
    print("Testing Github.check_build_status")
    assert Github.check_build_status("yandex-sysmon", "yandex-sysmon", "master") is None


# Generated at 2022-06-14 05:15:03.571060
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner = "airflow"
    repo = "airflow"
    ref = "b2a672003e5f7d05044ab1fd8a03928587b6b43f"
    assert Gitlab.check_build_status(owner, repo, ref)

# Generated at 2022-06-14 05:15:08.686454
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class Gitlab:
        def __init__(self):
            pass

        @staticmethod
        def domain():
            return "gitlab.com"

        @staticmethod
        def api_url():
            return "https://" + Gitlab.domain()

        @staticmethod
        def token():
            return os.environ.get("GL_TOKEN")

    class Pipeline:
        def __init__(self, status):
            self.status = status

    class Commit:
        def __init__(self, _id):
            self._id = _id

        def statuses(self):
            return {
                "status": [
                    Pipeline("success"),
                    Pipeline("success"),
                    Pipeline("success"),
                    Pipeline("failed"),
                    Pipeline("failed"),
                ]
            }


# Generated at 2022-06-14 05:15:11.348728
# Unit test for function get_hvcs
def test_get_hvcs():
    from release_watcher.config import _get_config
    from release_watcher.config import config_location
    from release_watcher.config import Config
    from release_watcher.config import DEFAULT_CONFIG

    conf = Config(DEFAULT_CONFIG)
    conf.update_config(config_location())
    conf.update_config(_get_config())
    Github()

# Generated at 2022-06-14 05:15:12.401186
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("foo", "bar", "123456") == True



# Generated at 2022-06-14 05:17:12.469615
# Unit test for method auth of class Github
def test_Github_auth():
    return



# Generated at 2022-06-14 05:17:14.349701
# Unit test for method api_url of class Github
def test_Github_api_url():
    url = Github.api_url()
    assert url == "https://api.github.com"



# Generated at 2022-06-14 05:17:16.652124
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("group", "project", "7dcbbf4f4d4d4c4c4b4b4b4b4b")

# Generated at 2022-06-14 05:17:24.541741
# Unit test for function get_hvcs
def test_get_hvcs():
    # Should return Github when hvcs is not set in configuration file
    assert get_hvcs() is Github

    class MockConfig:
        def get(self, key):
            if key == "hvcs":
                return "github"
            return None

    config = MockConfig()
    assert get_hvcs() is Github, "Should return Github"

# Generated at 2022-06-14 05:17:28.560785
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.check_build_status("ericcorbin", "stagediff", "81bd6b6f12ac62c16d3e10a3f3bfb1a69eb9c490")

# Generated at 2022-06-14 05:17:30.248730
# Unit test for function get_hvcs
def test_get_hvcs():
    assert get_hvcs().__name__ == "Github"

# Generated at 2022-06-14 05:17:38.093985
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """ Unit test on method check_build_status
    """
    test_status = []
    class test_Gitlab(Gitlab):
        @staticmethod
        def domain():
            return "gitlab.com"
        @staticmethod
        def api_url():
            return "https://gitlab.com"
        @staticmethod
        def token():
            return "fake token to avoid real query"
        @classmethod
        @LoggedFunction(logger)
        def check_build_status(owner, repo, ref):
            return test_status.pop(0)
        
    # Case when the pipeline has failed
    test_status = [False, False, False]
    assert test_Gitlab.check_build_status("test", "test", "test") == False
    # Case when the pipeline is pending
    test

# Generated at 2022-06-14 05:17:40.807279
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("owner", "repo", "ref") == True

# Generated at 2022-06-14 05:17:51.735072
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():

    import unittest

    class TestCheckBuildStatus(unittest.TestCase):

        def test_passing(self):
            """Check if check_build_status correctly evaluates the API response
            """
            self.assertTrue(
                Gitlab.check_build_status("dls-scisoft", "fabio", "42c9ea6")
            )

        def test_pending(self):
            """Check if check_build_status correctly evaluates the API response
            """
            self.assertFalse(
                Gitlab.check_build_status("dls-scisoft", "fabio", "9ea9b4d")
            )

        def test_failed(self):
            """Check if check_build_status correctly evaluates the API response
            """

# Generated at 2022-06-14 05:17:59.967395
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    import unittest

    class TestGitlab(unittest.TestCase):
        """Test class for Gitlab"""

        # Unit test for method check_build_status
        def test_check_build_status(self):
            self.assertTrue(Gitlab.check_build_status("GitLab", "gitlab", "abcdef0"))

    unittest.main()



# Generated at 2022-06-14 05:20:03.229425
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"



# Generated at 2022-06-14 05:20:10.708406
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    domain1 = "gitlab.com"
    domain2 = "gitlab-server.my"
    environ = {"CI_SERVER_HOST": "gitlab-server.my"}
    assert Gitlab.domain() == domain1
    with patch.dict("os.environ", environ):
        assert Gitlab.domain() == domain2


# Generated at 2022-06-14 05:20:18.426319
# Unit test for function get_hvcs
def test_get_hvcs():
    """Unit test for function get_hvcs"""
    config.set("hvcs", "github")
    assert(get_hvcs()) == Github
    config.set("hvcs", "gitlab")
    assert(get_hvcs()) == Gitlab
    config.set("hvcs", "unknown")
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()

# Generated at 2022-06-14 05:20:21.026201
# Unit test for function get_hvcs
def test_get_hvcs():
    config.set("hvcs", "github")
    assert get_hvcs() == Github
    config.set("hvcs", "gitlab")
    assert get_hvcs() == Gitlab



# Generated at 2022-06-14 05:20:34.737531
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert not Gitlab.check_build_status("hortonworks", "spec", "e5536486c729f39a9943f9b1281986fbf6ee407c")
    assert not Gitlab.check_build_status("hortonworks", "spec", "9f9b894af1b915c76eba09e46d4fb427698d4c4e")
    assert Gitlab.check_build_status("hortonworks", "spec", "3fd36ceb3eaa7b6dae00a903fa8f8bec6edc0a19")
    assert Gitlab.check_build_status("hortonworks", "spec", "8ba2cae0704b5157aafcae16b8efa8c7e1eefb69")



# Generated at 2022-06-14 05:20:42.261872
# Unit test for function get_hvcs
def test_get_hvcs():
    '''Test get_hvcs'''
    old_hvcs = config.get("hvcs")

    config.set("hvcs", "Github")
    hvcs = get_hvcs()
    assert hvcs == Github

    config.set("hvcs", "gitlab")
    hvcs = get_hvcs()
    assert hvcs == Gitlab

    config.set("hvcs", old_hvcs)

# Generated at 2022-06-14 05:20:45.276369
# Unit test for method auth of class Github
def test_Github_auth():
    expected = TokenAuth(None)

    class MyGithub(Github):
        @staticmethod
        def token():
            return None

    result = MyGithub.auth()
    assert result == expected



# Generated at 2022-06-14 05:20:51.212424
# Unit test for function get_hvcs
def test_get_hvcs():
    '''Getting hvcs returns the correct object'''
    config.hvcs = "github"
    assert isinstance(get_hvcs(), Github)
    config.hvcs = "gitlab"
    assert isinstance(get_hvcs(), Gitlab)
    config.hvcs = None
    assert get_hvcs() is None



# Generated at 2022-06-14 05:20:52.487102
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert True, "Test not implemented"

# Generated at 2022-06-14 05:20:56.984674
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    status = Gitlab.check_build_status("scality", "BuildBot", "f89c7f9d1ebc59f65728f58e54f01d9508674013")
    assert status == True
