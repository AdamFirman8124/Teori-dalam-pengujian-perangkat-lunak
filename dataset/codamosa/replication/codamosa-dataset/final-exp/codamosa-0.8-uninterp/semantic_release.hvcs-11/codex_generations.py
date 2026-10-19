

# Generated at 2022-06-14 05:19:06.868150
# Unit test for function get_hvcs
def test_get_hvcs():
    """Test of get_hvcs function"""
    hvcs = get_hvcs()
    return isinstance(hvcs, Base)

# Generated at 2022-06-14 05:19:14.400637
# Unit test for function get_hvcs
def test_get_hvcs():
    """  test_get_hvcs : test that it returns the proper class from config file
    """
    # GitHub
    config.set("hvcs", "github")
    assert get_hvcs() == Github
    # Gitlab
    config.set("hvcs", "gitlab")
    assert get_hvcs() == Gitlab
    # Unknown
    config.set("hvcs", "bitbucket")
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()

# Generated at 2022-06-14 05:19:14.961131
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
	pass

# Generated at 2022-06-14 05:19:23.948888
# Unit test for function get_hvcs
def test_get_hvcs():
    # Test the 'github' and 'gitlab' options
    config["github"] = None
    config["gitlab"] = None
    config["hvcs"] = "github"
    assert get_hvcs() == Github
    config["hvcs"] = "gitlab"
    assert get_hvcs() == Gitlab

    # Test with an invalid option
    config["hvcs"] = "test"
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()

# Generated at 2022-06-14 05:19:34.183324
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    from common.config import Config
    from common.logger import set_logging
    import logging
    import os

    config = Config(config_dir=".")
    config.load()

    set_logging(log_level=logging.DEBUG, log_dir="tests/")

    os.environ["GL_TOKEN"] = "GL_TOKEN"

    gitlab_method_check_build_status(
        config.get("hvcs_domain", os.environ.get("CI_SERVER_HOST")),
        owner="owner",
        repo="repo",
        ref="ref",
    )


# Generated at 2022-06-14 05:19:39.700005
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    result = Gitlab.check_build_status("hyperledger", "aries-rfcs", "c2cbdde30b7c4e4600762575f192e27f552b7c2b")
    print(result)
    assert result == True


test_Gitlab_check_build_status()


# Generated at 2022-06-14 05:19:41.313958
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"

# Generated at 2022-06-14 05:19:44.677950
# Unit test for method auth of class Github
def test_Github_auth():
    import pytest
    import os
    token = os.getenv('GH_TOKEN')
    result = TokenAuth(token)
    expect = AuthBase()
    assert result != expect


# Generated at 2022-06-14 05:19:46.904902
# Unit test for function get_hvcs
def test_get_hvcs():
    assert get_hvcs.__name__ == "get_hvcs"
    assert get_hvcs.__doc__ == "Get HVCS helper class"



# Generated at 2022-06-14 05:19:50.149955
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    app = Flask(__name__)
    with app.app_context():
        assert Gitlab.domain() == "gitlab.com"



# Generated at 2022-06-14 05:22:35.740238
# Unit test for method auth of class Github
def test_Github_auth():
    # Test default github
    domain = Github.domain()
    assert domain == Github.DEFAULT_DOMAIN
    token = Github.token()
    assert token == os.environ.get("GH_TOKEN")
    api_url = Github.api_url()
    assert api_url == f"https://api.{Github.DEFAULT_DOMAIN}"

    # Test enterprise github
    domain = "github.test.com"
    token = "12345abcde"
    config["hvcs_domain"] = domain
    os.environ["GH_TOKEN"] = token
    assert Github.domain() == domain
    assert Github.token() == token
    assert Github.api_url() == f"https://{domain}"



# Generated at 2022-06-14 05:22:42.932695
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Initialize env variables
    os.environ["CI_SERVER_HOST"] = "gitlab.com"
    os.environ["GL_TOKEN"] = "token"
    os.environ['GITHUB_ACTIONS'] = 'True'

    # List of tuples containing ((owner, repo, ref, expected), ...)
    # These are the test cases:
    test_cases = ((("MultiverseOS", "multiverse", "master", False), ),
                  (("MultiverseOS", "multiverse", "master", True), ),
                  (("MultiverseOS", "multiverse", "master", True), ),)

# Generated at 2022-06-14 05:22:46.317964
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"
