

# Generated at 2022-06-14 05:13:53.606432
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() == "gitlab.com"

# Generated at 2022-06-14 05:13:56.109860
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Function that test the method check_build_status of the class Gitlab"""
    assert "check_build_status" in dir(Gitlab)



# Generated at 2022-06-14 05:14:02.590619
# Unit test for function get_hvcs
def test_get_hvcs():
    class TestConfig:
        @staticmethod
        def get(key):
            if key == "hvcs":
                return "gitlab"
            elif key == "hvcs_domain":
                return "gitlab.com"
            return None
    config.pop()
    config.push(TestConfig())
    hvcs = get_hvcs()
    assert hvcs.domain() == "gitlab.com"

# Generated at 2022-06-14 05:14:04.879543
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    # Just to make sure that eventually the config is taken into account
    assert Gitlab.domain() == "gitlab.com"

# Generated at 2022-06-14 05:14:06.280027
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab().domain() == "gitlab.com"



# Generated at 2022-06-14 05:14:16.970293
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    from .mock import patch_get

    # test case 1: Build status found
    mocker = patch_get(
        "https://api.github.com/repos/testowner/testrepo/commits/testref/status", json={
            "state": "success"
        }
    )

    assert Github.check_build_status("testowner", "testrepo", "testref") is True
    mocker.stop()

    # test case 2: Build status not found
    mocker = patch_get("https://api.github.com/repos/testowner/testrepo/commits/testref/status")
    assert Github.check_build_status("testowner", "testrepo", "testref") is False
    mocker.stop()



# Generated at 2022-06-14 05:14:25.175412
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Test method check_build_status of class Gitlab"""

    # reset mock logger
    logger.mock_reset()

    # checks build status of commit on Gitlab instance
    # Gitlab.check_build_status("openstax", "accounts", "2338e79891f364beb919d1c71261dc6254ad3597")

    # run test
    testargs = ["release-notes-generator.py"]
    with patch.object(sys, "argv", testargs):
        assert Gitlab.check_build_status("openstax", "accounts", "2338e79891f364beb919d1c71261dc6254ad3597") is False

    logger.debug(f"Log messages: {logger.mock_calls}")


# Generated at 2022-06-14 05:14:27.317431
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == 'https://api.github.com'


# Generated at 2022-06-14 05:14:30.912859
# Unit test for method auth of class Github
def test_Github_auth():
    # Arrange
    auth = Github.auth()

    # Act
    result = auth

    # Assert
    assert result
    assert result == TokenAuth(os.environ.get("GH_TOKEN"))


# Generated at 2022-06-14 05:14:37.223231
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    import requests
    import requests_mock
    from unittest.mock import call
    with requests_mock.mock() as m:
        m.get("http://www.google.com/", text="")
        s = requests.Session()
        t = TokenAuth("hello")
        s.get("http://www.google.com/", auth=t)
        assert m.call_count == 1
        assert m.last_request.headers == {"Authorization": "token hello"}

# Unit tests for class TokenAuth

# Generated at 2022-06-14 05:16:14.919220
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Tests the function check_build_status from the class Gitlab"""
    assert Gitlab.check_build_status("vbmisus", "contributions", "8cdb0d05bf7fffc9f5271b8d0ebe5a5c5fce12bd") \
        is True



# Generated at 2022-06-14 05:16:19.753710
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("hiveeyes", "hiveeyes-micropython-firmware", "abcdefghijklmnopqrstuvwxyz0123456789abcdef") is False
    assert Gitlab.check_build_status(
        "Hiveeyes", "hiveeyes-micropython-firmware", "abcdefghijklmnopqrstuvwxyz0123456789abcdef"
    ) is False
    assert Gitlab.check_build_status("Hiveeyes", "test", "abcd") is False



# Generated at 2022-06-14 05:16:28.908753
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """
    Test for the method check_build_status of class Gitlab
    """
    Gitlab.check_build_status = MagicMock(return_value=False)
    assert Gitlab.check_build_status(1, 2, 3) is False
    Gitlab.check_build_status.assert_called_with(1, 2, 3)
    Gitlab.check_build_status = MagicMock(return_value=True)
    assert Gitlab.check_build_status(1, 2, 3) is True
    Gitlab.check_build_status.assert_called_with(1, 2, 3)

# Generated at 2022-06-14 05:16:30.383435
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() is not None



# Generated at 2022-06-14 05:16:38.541628
# Unit test for function get_hvcs
def test_get_hvcs():
    """Test method get_hvcs"""
    config.set("hvcs", "github")

    assert get_hvcs() == Github
    config.set("hvcs", "gitlab")
    assert get_hvcs() == Gitlab

    with pytest.raises(ImproperConfigurationError):
        config.set("hvcs", "bitbucket")
        get_hvcs()

# Generated at 2022-06-14 05:16:44.745379
# Unit test for function get_hvcs
def test_get_hvcs():
    assert get_hvcs().__name__ == "Github"
    config.set("hvcs", "gitlab")
    assert get_hvcs().__name__ == "Gitlab"
    config.set("hvcs", "NotGithubOrGitlab")
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()

# Generated at 2022-06-14 05:16:54.600943
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    @classmethod
    def get_build_status(cls, status: str, allow_failure: bool) -> dict:
        return {"status": status, "allow_failure": allow_failure}

    # Success
    assert Gitlab.check_build_status("owner", "repo", "ref") is True
    assert Gitlab.check_build_status("foo", "bar", "baz") is True

    # Failure if job (non pending) with no allow_failure
    Gitlab.check_build_status = get_build_status("failed", False)
    assert Gitlab.check_build_status("owner", "repo", "ref") is False
    assert Gitlab.check_build_status("foo", "bar", "baz") is False

    # Success if job (non pending) with allow_failure
   

# Generated at 2022-06-14 05:16:57.222540
# Unit test for method auth of class Github
def test_Github_auth():
    """
    Test Github's auth method
    """
    # Build an object
    github = Github()
    assert github.auth() is None

    # Set environment variables
    os.environ["GH_TOKEN"] = "test_token"

    # Build an object and call the object
    github = Github()
    assert github.auth() == TokenAuth("test_token")

    # Delete the environment variable
    os.environ.pop("GH_TOKEN")



# Generated at 2022-06-14 05:17:03.428582
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():

    # Define project and commit sha
    owner = "joomla-cli"
    project = "joomla"
    commit = "6d5d9b3bdd31fee3e3acd6fbf1339d94a6b0502d"

    # Call method to test
    result = Gitlab.check_build_status(owner, project, commit)

    # Print result
    print("Result: " + str(result))


# Generated at 2022-06-14 05:17:08.398954
# Unit test for method auth of class Github
def test_Github_auth():
    import os
    import unittest
    from hvcs.hvcs import Github
    token = os.environ.get("GH_TOKEN")
    tokenAuth = Github.auth()
    cls_return = TokenAuth(token)
    assert tokenAuth == cls_return


# Generated at 2022-06-14 05:19:20.979230
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    import gitlab
    assert Gitlab.check_build_status(
        owner="VirgilSecurity", repo="virgil-sdk-python", ref="5bc5c5d7b5f0d849a498f"
    ) == True

# Generated at 2022-06-14 05:19:29.072645
# Unit test for method auth of class Github
def test_Github_auth():
    class TestGithub(Github):
        pass

    assert TestGithub.auth() is None

    os.environ["GH_TOKEN"] = "abc123"
    assert (
        TestGithub.auth() == TokenAuth("abc123")
    ), "Invalid GitHub credentials were given."

    os.environ["GH_TOKEN"] = ""
    assert (
        TestGithub.auth() is None
    ), "Expected TokenAuth('') to be equivalent to None"

    del os.environ["GH_TOKEN"]



# Generated at 2022-06-14 05:19:33.373318
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Test that check_build_status returns the right status"""
    assert Gitlab.check_build_status("prj_namespace", "prj_name", "ref") is True


# Generated at 2022-06-14 05:19:35.803451
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() == "gitlab.com"


# Generated at 2022-06-14 05:19:43.836202
# Unit test for function get_hvcs
def test_get_hvcs():
    config.set('hvcs', 'github', True)
    assert get_hvcs() == Github
    config.set('hvcs', 'gitlab', True)
    assert get_hvcs() == Gitlab
    config.set('hvcs', 'not_a_valid_option', True)
    with pytest.raises(ImproperConfigurationError, match=r'"not_a_valid_option" is not a valid option for hvcs\.'):
        get_hvcs()



# Generated at 2022-06-14 05:19:48.989262
# Unit test for function get_hvcs
def test_get_hvcs():
    config.set('hvcs', 'Github')
    assert get_hvcs() == Github
    config.set('hvcs', 'Gitlab')
    assert get_hvcs() == Gitlab
    with pytest.raises(ImproperConfigurationError):
        config.set('hvcs', 'NotValidHVCS')
        get_hvcs()


# Generated at 2022-06-14 05:19:51.523846
# Unit test for method api_url of class Github
def test_Github_api_url():
    r = Github.api_url()
    assert r is not None, "Did not get an object"



# Generated at 2022-06-14 05:20:04.021581
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    from unittest.mock import patch

    owner = "test"
    repo = "repo"
    ref = "12345"

    with patch.object(Github, "domain") as mock_domain:
        mock_domain.return_value = "github.com"

        with patch.object(Github, "api_url") as mock_api_url:
            mock_api_url.return_value = "https://github.com"

            with patch.object(Github, "token") as mock_token:
                mock_token.return_value = "12345"


# Generated at 2022-06-14 05:20:08.631109
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() == Gitlab.domain()
    assert Gitlab.domain() == Gitlab.api_url().split("://")[1]


# Generated at 2022-06-14 05:20:20.300275
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Tests method check_build_status of class Gitlab"""

# Generated at 2022-06-14 05:22:23.543301
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"



# Generated at 2022-06-14 05:22:36.021598
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Unit test for method check_build_status of class Gitlab"""
    class MockResponse:
        def __init__(self, text: Optional[str]):
            self.text = text

        def json(self):
            return json.loads(self.text)

    class MockRequestsSession_check_build_status:
        """Mock requests session for Gitlab check_build_status method"""

        def __init__(self):
            pass


# Generated at 2022-06-14 05:22:40.010945
# Unit test for method auth of class Github
def test_Github_auth():
    token_undef = None
    token_def = "testGithub_auth_token"
    assert Github.auth() == None
    assert Github.token() == token_undef
    assert Github.auth() != None
    assert Github.auth().token == token_def
    assert Github.token() == token_def


# Generated at 2022-06-14 05:22:42.860645
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner = "gitlab-org"
    repo = "gitlab-ce"
    ref = "6-13-stable"
    Gitlab.check_build_status(owner, repo, ref)

# Generated at 2022-06-14 05:22:48.259236
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Test check_build_status of class Gitlab"""
    assert Gitlab.check_build_status("test-repository")
    assert not Gitlab.check_build_status("test-repository-failed")