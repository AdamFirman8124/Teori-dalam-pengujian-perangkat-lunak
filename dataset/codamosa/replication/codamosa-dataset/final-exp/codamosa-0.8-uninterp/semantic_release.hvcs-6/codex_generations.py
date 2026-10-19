

# Generated at 2022-06-14 05:13:57.317955
# Unit test for function get_hvcs
def test_get_hvcs():
    '''Unit test for function get_hvcs()'''
    assert get_hvcs().__name__ == "Gitlab"
    config.set("hvcs", "github")
    assert get_hvcs().__name__ == "Github"
    config.reset("hvcs")

# Generated at 2022-06-14 05:14:05.383337
# Unit test for function get_hvcs
def test_get_hvcs():
    with pytest.raises(ImproperConfigurationError):
        config.set("hvcs", "Unknown")
        get_hvcs()
    config.set("hvcs", "github")
    assert isinstance(get_hvcs(), Github)
    config.set("hvcs", "GitLab")
    assert isinstance(get_hvcs(), Gitlab)



# Generated at 2022-06-14 05:14:13.957577
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    status = Gitlab.check_build_status("nf-rp", "rp_to_nar", "d5a5f5a5c5b5e5a5f5b5c5d5e5a5f5b5e5f5d5")
    assert status == False

    status = Gitlab.check_build_status("nf-rp", "rp_to_nar", "d5a5f5a5c5b5e5a5f5b5c5d5e5a5f5b5e5f5a5")
    assert status == True

# Generated at 2022-06-14 05:14:21.181573
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner = "George"
    repo = "Project"
    ref = "sha1"
    response = Mock()
    response.json.return_value = {"status":"success"}
    sess = Mock()
    sess.get.return_value = response
    helper = Mock()
    helper.session.return_value = sess
    Gitlab.session = Mock(return_value=sess)
    print(Gitlab.check_build_status(owner, repo, ref))
    assert response.json.called
    assert sess.get.called
    assert Gitlab.session.called


# Generated at 2022-06-14 05:14:28.510760
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    gitlab_check_build_status = Gitlab.check_build_status("pyfqdn", "fqdn", "356154b")
    assert gitlab_check_build_status == True 
    
    gitlab_check_build_status = Gitlab.check_build_status("pyfqdn", "fqdn", "9c8a8ff")
    assert gitlab_check_build_status == False

# Generated at 2022-06-14 05:14:29.680786
# Unit test for method auth of class Github
def test_Github_auth():
    pass



# Generated at 2022-06-14 05:14:32.229590
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    get_token = TokenAuth("test")
    assert get_token(None).headers["Authorization"] == "token test"



# Generated at 2022-06-14 05:14:35.143885
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    import os
    os.environ["GL_TOKEN"] = "Your_Token"
    assert Gitlab.check_build_status("Your_Project", "Your_repo", "your_ref")

# Generated at 2022-06-14 05:14:41.852092
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    r = Session()
    r.headers = {}
    token = "7f3d2eec-7dbc-456e-9e0c-45dfd58fb1ae"
    auth = TokenAuth(token)
    auth(r)
    assert r.headers["Authorization"] == f"token {token}"



# Generated at 2022-06-14 05:14:52.931597
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """
    Unit test for Gitlab class method check_build_status(). Check return value
    depending on the different combinations of test results
    """
    # init
    owner = "lagoobernetes"
    repo = "lagoobernetes"
    ref = "6f35e6f54ce6d2b6c7783e37e8a9d98c9c86def7"

    # build a mock response as if it came from Gitlab API

# Generated at 2022-06-14 05:16:15.592408
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    # Test for the case when the hvcs_domain is set
    config.set('hvcs_domain', 'gitlab.com')
    assert Gitlab.domain() == 'gitlab.com'

    # Test for the case when the CI_SERVER_HOST is set
    config.set('hvcs_domain', '')
    os.environ['CI_SERVER_HOST'] = 'gitlab.com'
    assert Gitlab.domain() == 'gitlab.com'

    # Test for the case when hvcs_domain and CI_SERVER_HOST are not set
    config.set('hvcs_domain', '')
    os.environ['CI_SERVER_HOST'] = ''
    assert Gitlab.domain() == 'gitlab.com'


# Generated at 2022-06-14 05:16:19.422304
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    print("\nTest for Gitlab.check_build_status")
    try:
        status = Gitlab.check_build_status("hysds/hysds_commons", "9eb2c29d7063b37a5b92d7b21a6c93f73829d54e")
        print("status: %r" % status)
    except Exception as e:
        print("Exception: %s" % str(e))



# Generated at 2022-06-14 05:16:30.036471
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """
    test the check_build_status method of the Gitlab class
    """

    class MockResponse:
        def __init__(self, jobs):
            self.status_code = 200
            self.json_data = [{'name': i, 'status': 'success', 'allow_failure': False} for i in jobs]
            self.headers = {'content-type': 'json'}

        def json(self):
            return self.json_data
    # test passed
    jobs_state1 = ['branch-test', 'commit-test']
    test_data1 = MockResponse(jobs_state1)
    assert Gitlab.check_build_status('tester', 'test_pkg', 'shaxx') == True
    # test failed
    jobs_state2 = ['branch-test', 'commit-test']

# Generated at 2022-06-14 05:16:44.162162
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    import unittest

    cls = Gitlab
    class TestGitlab(unittest.TestCase):
        @unittest.mock.patch('gitlab.Gitlab.auth')
        @unittest.mock.patch('gitlab.Gitlab.projects.get')
        def test_check_build_status(self, mock_projects_get, mock_auth):
            mock_commits = unittest.mock.MagicMock()
            mock_statuses = unittest.mock.MagicMock()
            mock_statuses.list.return_value = [{
                "status": "pending",
                "allow_failure": False,
                "name": "job1",
            }]
            mock_commits.get.return_value = mock_statuses
            mock_projects

# Generated at 2022-06-14 05:16:54.560449
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # test case 1: pipeline is still running
    owner = "demo"
    repo = "demo"
    ref = "3a762a2f17428a09b0e0fdb36f1d1c98e33a1c23"
    assert Gitlab.check_build_status(owner, repo, ref) is False

    # test case 2: pipeline is stopped but still failed (ERROR)
    ref = "a4b4dd4ca64dbf830b85d7edf5b8e8d53ecee1f9"
    assert Gitlab.check_build_status(owner, repo, ref) is False

    # test case 3: pipeline is stopped but still failed (CAN FAIL)

# Generated at 2022-06-14 05:16:55.626364
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == os.environ.get("GITHUB_HOSTNAME", "github.com")


# Generated at 2022-06-14 05:16:57.506461
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    Gitlab.domain()




# Generated at 2022-06-14 05:17:00.827987
# Unit test for function get_hvcs
def test_get_hvcs():
    # Check if it returns class object
    assert get_hvcs().__class__==Github

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# Generated at 2022-06-14 05:17:12.568078
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.domain = MagicMock()
    Gitlab.domain.return_value = "gitlab.com"
    Gitlab.token = MagicMock()
    Gitlab.token.return_value = "123456"
    gl = gitlab.Gitlab("https://gitlab.com", private_token="123456")
    gl.auth = MagicMock()
    job_failed = {"id": 1, "status": "failed", "allow_failure": "false"}
    job_pending = {"id": 2, "status": "pending", "allow_failure": "false"}
    job_skipped = {"id": 3, "status": "skipped", "allow_failure": "false"}
    job_success = {"id": 4, "status": "success", "allow_failure": "false"}
    job

# Generated at 2022-06-14 05:17:14.453528
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"



# Generated at 2022-06-14 05:18:36.778711
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    """
        Unit test for method __call__ of class TokenAuth
    """
    import pytest
    from requests.auth import AuthBase
    from requests import Request
    from requests import Response

    class MockAuth(AuthBase):
        def __call__(self, r):
            return r

    custom_token = "custom_token"
    token_auth = TokenAuth(custom_token)

    mock_request = Request(method="POST", url="http://localhost")
    expected = Request(
        method="POST",
        url="http://localhost",
        headers={"Authorization": "token custom_token"},
    )

    assert token_auth(mock_request) == expected, "token auth header is wrong"

    with pytest.raises(TypeError) as error_info:
        token_auth(MockAuth())


# Generated at 2022-06-14 05:18:41.813523
# Unit test for method check_build_status of class Gitlab

# Generated at 2022-06-14 05:18:47.475444
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner = "hbmartin"
    repo = "megorepo"
    ref = "4b6caebbc6a332d6013ecf6c7b1f02fa9a9a8a88"
    assert Gitlab.check_build_status(owner, repo, ref) == True


# Generated at 2022-06-14 05:18:50.827056
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() == config.get("hvcs_domain", os.environ.get("CI_SERVER_HOST")) or "gitlab.com"


# Generated at 2022-06-14 05:18:54.099469
# Unit test for method auth of class Github
def test_Github_auth():
    """Test for method auth of class Github"""
    # Setup
    hvcs = Github()

    # Exercise
    result = hvcs.auth()

    # Verify
    assert not result



# Generated at 2022-06-14 05:19:07.492963
# Unit test for function get_hvcs
def test_get_hvcs():
    """Unit test get_hvcs"""
    config.load(
        {
            "hvcs": "github",
            "hvcs_domain": "github.com",
            "hvcs_token": "12345",
            "hvcs_organization": "mozilla",
            "hvcs_repository": "mozilla-mobile",
        }
    )
    hvcs = get_hvcs()
    assert isinstance(hvcs, Github)


# Generated at 2022-06-14 05:19:11.588656
# Unit test for function get_hvcs
def test_get_hvcs():
    config.set("hvcs", "gitlab")
    assert get_hvcs() == Gitlab
    config.set("hvcs", "github")
    assert get_hvcs() == Github

# Generated at 2022-06-14 05:19:16.573737
# Unit test for method auth of class Github
def test_Github_auth():
    """Test method auth of class Github."""
    from unittest.mock import ANY, Mock, patch

    with patch("os.environ.get") as mock_environ:
        # Case: token not set = None.
        mock_environ.return_value = None
        assert Github.auth() is None

        # Case: token set.
        mock_environ.return_value = "123456___token___"
        assert Github.auth() == TokenAuth("123456___token___")



# Generated at 2022-06-14 05:19:29.075251
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    gl = gitlab.Gitlab(Gitlab.api_url(), private_token=Gitlab.token())
    gl.auth()
    jobs = gl.projects.get("peiqi/test-api").commits.get("2c6aa8c5f5d5dc06b6a5e6ef62c33d5f6f0b6e9b").statuses.list()
    for job in jobs:
        if job["status"] not in ["success", "skipped"]:
            if job["status"] == "pending":
                logger.debug("job {0} is still in pending status".format(job["name"]))
                return False

# Generated at 2022-06-14 05:19:40.841635
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Test check_build_status method of class Gitlab"""
    def _patched_requests_post(url, *args, **kwargs):
        """patches requests.get method for getting statuses of a job"""

# Generated at 2022-06-14 05:20:53.483585
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    Gitlab.domain()


# Generated at 2022-06-14 05:20:54.338369
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("test1", "test2", "test3") == True

# Generated at 2022-06-14 05:20:56.284411
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("AAAzad", "test-project", "23f1e76bfd8c6a64d66fcbdc9b0a56e414f19553") == True


# Generated at 2022-06-14 05:21:09.999456
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Path to test module for use in individual test functions.
    test_mod_path = os.path.abspath(__file__)

    from utils.gitutils import Git

    # Open the repo in the current directory in a temporary directory.
    with TemporaryDirectory() as tmp:
        wd = os.getcwd()
        os.chdir(tmp)
        Git().run_in_repo("clone", "https://github.com/openstack/releases")
        repo_path = os.path.join(tmp, "releases")
        os.chdir(repo_path)
        Git().run_in_repo("checkout", "master")

        # Get the sha1 of the last commit of the repo
        last_commit_sha1 = Git().get_revisions(1)[0]

        # Create

# Generated at 2022-06-14 05:21:15.374556
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    assert Github.check_build_status("david-yoon", "python-semantic-release", "e24b49d86a7fbf2b9c7a1a99fbbc7ad3749b70e8") is True

# Generated at 2022-06-14 05:21:17.674089
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.check_build_status("group-name", "repo-name", "ref-name")



# Generated at 2022-06-14 05:21:30.634036
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class mock_gitlab_Gitlab:
        def __init__(self, api_url, private_token):
            self._api_url = api_url
            self._private_token = private_token
            pass

        def auth(self):
            pass


# Generated at 2022-06-14 05:21:36.966097
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    mock_github_get_response(status_code=200, json_data={"state": "success"})
    assert Gitlab.check_build_status("", "", "") is True
    mock_github_get_response(status_code=200, json_data={"state": "failed"})
    assert Gitlab.check_build_status("", "", "") is False



# Generated at 2022-06-14 05:21:45.613162
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("hg-tools", "repo", "c4e1ab") == False
    assert Gitlab.check_build_status("hg-tools", "repo", "c4e1ab22f1ab70da7a0f8e24d1a3c07a2b7e4d67") == True
    assert Gitlab.check_build_status("hg-tools", "repo", "c4e1ab22f1ab70da7a0f8e24d1a3c07a2b7e4d67") == True
    assert Gitlab.check_build_status("hg-tools", "repo", "d40fdb25") == False

# Generated at 2022-06-14 05:21:49.393551
# Unit test for function get_hvcs
def test_get_hvcs():
    """Unit test for function get_hvcs"""
    assert get_hvcs() is Github

