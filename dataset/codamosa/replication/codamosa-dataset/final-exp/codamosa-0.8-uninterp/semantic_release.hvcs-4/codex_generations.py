

# Generated at 2022-06-14 05:15:02.050459
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Build has failed
    owner = "HMS-DBMI"
    repo = "samtools"
    ref = "031bff0c4a6e3900500908661e9d179e896fb610"
    result = Gitlab.check_build_status(owner, repo, ref)
    assert not result

    # Build is pending
    ref = "c4d4ccb6c91e6e4a8d24bd6a39f6a7f6dce76bb3"
    result = Gitlab.check_build_status(owner, repo, ref)
    assert not result

    # Build has suceeded
    ref = "c1d10efcc15b937c3dc1e3510c54ecf0b94f62ec"

# Generated at 2022-06-14 05:15:06.188170
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """
    Test: Gitlab.check_build_status(owner: str, repo: str, ref: str) -> bool
    """
    # Creation of a mock object to simulate the request
    session = requests_mock.Mocker()
    session.start()

    # Creation of a test class object without environment variables
    gl = Gitlab()
    token = "mocktoken"
    api_url = "https://mockapi.url"
    gl.api_url = lambda: api_url

    # Definition of the mocked response
    response = {
        "statuses": [
            {"status": "pending"},
            {"status": "success"},
            {"status": "skipped"},
        ]
    }

    # Mocking the request

# Generated at 2022-06-14 05:15:10.230929
# Unit test for method auth of class Github
def test_Github_auth():
    test_cases = [
        {
            "hvcs_domain": "https://example.com",
            "gh_token": "Token",
            "expected_result": TokenAuth("Token"),
        },
        {"hvcs_domain": "https://example.com", "gh_token": None, "expected_result": None},
        {"hvcs_domain": None, "gh_token": "Token", "expected_result": TokenAuth("Token")},
        {"hvcs_domain": None, "gh_token": None, "expected_result": None},
    ]
    for i, test_case in enumerate(test_cases):
        test_name = "test_{}".format(i)
        with test_case["hvcs_domain"]:
            with test_case["gh_token"]:
                assert Github

# Generated at 2022-06-14 05:15:13.794528
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """
    Test Gitlab.check_build_status method
    """
    owner = "SteveLauwers"
    repo = "hello-world"
    ref = "9ed087a13bea49d782f9812a15a1f8d6e224b6a7"
    assert Gitlab.check_build_status(owner, repo, ref) == True

    repo = "hello-world-failed"
    assert Gitlab.check_build_status(owner, repo, ref) == False



# Generated at 2022-06-14 05:15:24.774017
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    print("\nTesting Gitlab.check_build_status\n")

    # test 1: repository doesn't exist
    owner = "g" + str(random.randint(100000000000, 999999999999))
    repo = "g" + str(random.randint(100000000000, 999999999999))
    ref = "1234567890123456789012345678901234567890"

    try:
        assert Gitlab.check_build_status(owner, repo, ref) == False
        print("test 1: SUCCEED")
    except:
        print("test 1: FAILED")

    # test 2: repository exists, but no job was found for the ref
    owner = "gitlab-org"
    repo = "gitlab-ce"

# Generated at 2022-06-14 05:15:33.302249
# Unit test for method api_url of class Github
def test_Github_api_url():
    """

    :return:
    """
    hvcs_domain = config.get("hvcs_domain")
    domain = hvcs_domain if hvcs_domain else Github.DEFAULT_DOMAIN
    api_url = config.get("hvcs_api_url")
    if not api_url:
        api_url = f"https://{'api.' if not hvcs_domain else ''}{domain}"
    assert Github.api_url() == api_url
    

# Generated at 2022-06-14 05:15:36.484397
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("mgrast", "mg-rast-v4-api", "6c7625747856faeb98edfa0e1e8d1fe6c9a6a0be")



# Generated at 2022-06-14 05:15:40.195850
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    domain = os.environ["CI_SERVER_HOST"]
    Gitlab.domain()
    assert Gitlab.domain() == domain, "domain should return the env variable CI_SERVER_HOST"
    Gitlab.domain()
    assert Gitlab.domain() == domain, "domain should return the env variable CI_SERVER_HOST"



# Generated at 2022-06-14 05:15:48.601601
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    with Stubber(os) as os_stubber:
        # Mock os.environ to return None
        os_stubber.add_response("environ", None)

        assert Gitlab.domain() == "gitlab.com"

        # Mock os.environ to return a specific value
        os_stubber.add_response("environ", {"CI_SERVER_HOST": "ci.server.com"})

        assert Gitlab.domain() == "ci.server.com"



# Generated at 2022-06-14 05:15:52.709167
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    """Unit test for method domain of class Gitlab"""
    assert Gitlab.domain() == "gitlab.com"


# Generated at 2022-06-14 05:19:31.459701
# Unit test for function get_hvcs
def test_get_hvcs():
    reported_error = False
    old_hvcs = config.get("hvcs")
    try:
        config.set("hvcs", "invalidhvcs")
        get_hvcs()
    except ImproperConfigurationError:
        reported_error = True
    assert reported_error
    config.set("hvcs", old_hvcs)

# Generated at 2022-06-14 05:19:33.833904
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"

# Generated at 2022-06-14 05:19:36.537856
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == 'https://api.github.com', 'Method api_url of class Github returned unexpected value.'


# Generated at 2022-06-14 05:19:39.909710
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():

    assert Gitlab.check_build_status(owner="demo", repo="example", ref="4396714645c2ab2edd70f4d0da29a856ebc0e96b") == True

# Generated at 2022-06-14 05:19:44.595534
# Unit test for function get_hvcs
def test_get_hvcs():
    with mock.patch("bump2version.config.get") as get:
        get.side_effect = lambda option: {
            "hvcs": "github",
        }.get(option, None)
        assert get_hvcs() == Github



# Generated at 2022-06-14 05:19:49.348514
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    logger = logging.getLogger()
    Gitlab.domain()
    Gitlab.token()
    Gitlab.api_url()
    Gitlab.check_build_status("tester","testapp","4f4a4b987d9bfc01cec1ec7ca8be535b8801bf2f")
    logger.info("The method check_build_status has been called with no errors")

# Generated at 2022-06-14 05:19:53.700765
# Unit test for method domain of class Github
def test_Github_domain():
    # noinspection PyUnresolvedReferences
    """Unit test for method domain of class Github """
    assert Github.domain() == "github.com"



# Generated at 2022-06-14 05:20:01.253878
# Unit test for function get_hvcs
def test_get_hvcs():
    try:
        _ = get_hvcs()
    except ImproperConfigurationError:
        assert True

    config.set(hvcs="github")
    assert isinstance(get_hvcs(), Base)
    assert isinstance(get_hvcs(), Github)

    config.set(hvcs="gitlab")
    assert isinstance(get_hvcs(), Base)
    assert isinstance(get_hvcs(), Gitlab)



# Generated at 2022-06-14 05:20:07.653608
# Unit test for function get_hvcs
def test_get_hvcs():
    from . import config
    from .config import ConfigManager
    from .exceptions import ImproperConfigurationError

    class MockedConfigManager(ConfigManager):
        def __init__(self, mocked_config):
            super().__init__()
            self._config = mocked_config

        def get(self, key: str, default=None) -> Optional[Any]:
            return self._config.get(key, default)

    config.ConfigManager = MockedConfigManager
    config.get = config.ConfigManager().get
    config.load = lambda x: None

    assert get_hvcs() is Github

    def load(path: str, defaults: Optional[dict] = None) -> None:
        config.ConfigManager({"hvcs": "gitlab"})

    config.load = load
    assert get_hvcs() is Gitlab

# Generated at 2022-06-14 05:20:19.879719
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Create a fake response to the gitlab call
    class fake_gitlab_response():
        def __init__(self, status):
            self.status = status

    # Create a list of fake responses
    fake_response_list = [fake_gitlab_response("success"), fake_gitlab_response("success")]

    # Append a failed status to the list
    test_failed_success_status = [
        fake_gitlab_response("success"),
        fake_gitlab_response("pending"),
        fake_gitlab_response("failed"),
    ]

    # Append a failure that can be ignored to the list
    test_failed_but_can_be_ignored = [
        fake_gitlab_response("success"),
        fake_gitlab_response("failed"),
    ]

    # Append a failure that can