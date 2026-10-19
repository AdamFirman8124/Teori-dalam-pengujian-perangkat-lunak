

# Generated at 2024-06-03 04:14:51.048151
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():    owner = "test_owner"

# Generated at 2024-06-03 04:14:52.279928
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():    token = "test_token"

# Generated at 2024-06-03 04:14:54.330215
# Unit test for method domain of class Github
def test_Github_domain():    # Test when hvcs_domain is not set in config
    config["hvcs_domain"] = None
    assert Github.domain() == Github.DEFAULT_DOMAIN

    # Test when hvcs_domain is set in config
    config["hvcs_domain"] = "custom.github.com"
    assert Github.domain() == "custom.github.com"


# Generated at 2024-06-03 04:14:58.351759
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():    owner = "test_owner"

# Generated at 2024-06-03 04:15:01.357600
# Unit test for function get_hvcs
def test_get_hvcs():    # Mock the config to return 'github' for hvcs
    with patch('config.get', return_value='github'):
        assert isinstance(get_hvcs(), Github)

    # Mock the config to return 'gitlab' for hvcs
    with patch('config.get', return_value='gitlab'):
        assert isinstance(get_hvcs(), Gitlab)

    # Mock the config to return an invalid hvcs
    with patch('config.get', return_value='invalid_hvcs'):
        with pytest.raises(ImproperConfigurationError):
            get_hvcs()


# Generated at 2024-06-03 04:15:02.529278
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():    token = "test_token"

# Generated at 2024-06-03 04:15:05.005868
# Unit test for function get_hvcs
def test_get_hvcs():    config.set("hvcs", "github")

# Generated at 2024-06-03 04:15:06.506002
# Unit test for function get_hvcs
def test_get_hvcs():    config.set("hvcs", "github")

# Generated at 2024-06-03 04:15:07.672287
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():    token = "test_token"

# Generated at 2024-06-03 04:15:11.065378
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():    owner = "test_owner"