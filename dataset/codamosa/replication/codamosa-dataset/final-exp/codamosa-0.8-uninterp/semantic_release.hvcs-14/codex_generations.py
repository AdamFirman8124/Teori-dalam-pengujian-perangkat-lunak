

# Generated at 2022-06-14 05:13:49.179807
# Unit test for method auth of class Github
def test_Github_auth():
    assert Github.auth() is not None


# Generated at 2022-06-14 05:13:50.542253
# Unit test for method domain of class Github
def test_Github_domain():
    assert isinstance(Github.domain(), str)



# Generated at 2022-06-14 05:14:03.473558
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class TestGitlab(Gitlab):
        def __init__(self, domain, token):
            self._domain = domain
            self._token = token

        def domain(self):
            return self._domain

        def token(self):
            return self._token

    class TestPipeline:
        def __init__(self, job_status):
            self._job_status = job_status

        def get(self, url, **kwargs):
            if url == "statuses":
                return self

            return None

        def list(self):
            return [{"status": self._job_status, "name": "test", "allow_failure": True}]

    class TestProject:
        def __init__(self, pipeline_status):
            self._pipeline_status = pipeline_status


# Generated at 2022-06-14 05:14:07.047114
# Unit test for method auth of class Github
def test_Github_auth():
    kwargs = {}
    kwargs["token"] = os.environ.get("GH_TOKEN")
    auth = TokenAuth(**kwargs)
    assert Github.auth() == auth



# Generated at 2022-06-14 05:14:11.710504
# Unit test for method api_url of class Github
def test_Github_api_url():
    try:
        conf = config.get()
        conf["hvcs_domain"] = "test"
        conf["hvcs"] = "github"
        g = Github()
        assert g.api_url() == "https://api.test"
    finally:
        del conf["hvcs_domain"]
        del conf["hvcs"]



# Generated at 2022-06-14 05:14:17.785218
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    # Initialization of TokenAuth object
    obj = TokenAuth(token='abc123')
    # Preparation for call of method __call__
    r = {'headers': {}}
    # Actual call of method __call__
    result = obj.__call__(r)
    # Verification of returned value
    assert result['headers'] == {'Authorization': 'token abc123'}


# Generated at 2022-06-14 05:14:21.400417
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    class dummy(object):
        def __init__(self):
            self.headers = {}

    token = "token"
    test_instance = TokenAuth(token)
    dummy_instance = dummy()
    result = test_instance.__call__(dummy_instance)

    assert result.headers["Authorization"] == f"token {token}"



# Generated at 2022-06-14 05:14:24.794967
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("test", "test", "test") is True
    assert Gitlab.check_build_status("test", "test", "test") is False

# Generated at 2022-06-14 05:14:26.912819
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("pypa", "pip", "999999999") == False



# Generated at 2022-06-14 05:14:28.111940
# Unit test for method auth of class Github
def test_Github_auth():
    Github.session()



# Generated at 2022-06-14 05:15:24.309157
# Unit test for method api_url of class Github
def test_Github_api_url():
    expected = "https://api.github.com"
    actual = Github.api_url()
    assert actual == expected

    os.environ["HVCS_DOMAIN"] = "example.com"
    expected = "https://api.example.com"
    actual = Github.api_url()
    assert actual == expected

    os.environ["HVCS_DOMAIN"] = "https://github.example.com"
    expected = "https://github.example.com"
    actual = Github.api_url()
    assert actual == expected

    os.environ["HVCS_DOMAIN"] = "https://api.github.example.com"
    expected = "https://api.github.example.com"
    actual = Github.api_url()
    assert actual == expected



# Generated at 2022-06-14 05:15:30.754481
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Test with a non existing project to raise an exception in get_project
    assert not Gitlab.check_build_status('non_existing_owner','non_existing_project','unknown_ref')
    # Test with an existing project
    assert not Gitlab.check_build_status('erdc-cm/vtm', 'master', '9af7cfd8b8c18f60229b1185c747d47e841ccc1a')



# Generated at 2022-06-14 05:15:32.447028
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    assert Github.check_build_status(None, None, None)



# Generated at 2022-06-14 05:15:40.669055
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    old_token = os.environ.get("GL_TOKEN")
    old_domain = config.get("hvcs_domain")

# Generated at 2022-06-14 05:15:52.918964
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    owner="d7a63a21ebc6e8f2d2d6"
    repo="test-hvcs"
    ref="6c5b6995c944e325d6a0b357f569e0b102374a8a"
    from unittest.mock import patch, MagicMock
    gitlab_mock = MagicMock()
    job = MagicMock()
    job.status = 'success'
    job.allow_failure = True
    job.name = "job_name"
    gitlab_mock.projects.get.return_value.commits.get.return_value.statuses.list.return_value = [job]

# Generated at 2022-06-14 05:16:03.190577
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    logger.debug("test_Gitlab_check_build_status")

    class TestCase:
        def __init__(self, name, url, namespace, project, ref, expected_status):
            self.name = name
            self.url = url
            self.namespace = namespace
            self.project = project
            self.ref = ref
            self.expected_status = expected_status

    # Mock a response
    class Response:
        def __init__(self, http_status, status_list):
            self.http_status = http_status
            self.status_list = status_list

        def json(self):
            return self.status_list

    get_count = 0
    get_max = 2

# Generated at 2022-06-14 05:16:06.011398
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    token = "12345"
    t = TokenAuth(token)
    assert t("requests_object") == "requests_object"



# Generated at 2022-06-14 05:16:09.644706
# Unit test for function get_hvcs
def test_get_hvcs():
    #setUp
    config["hvcs"] = "github"
    #test
    assert get_hvcs() is Github
    #tearDown
    del config["hvcs"]

# Generated at 2022-06-14 05:16:12.072768
# Unit test for method auth of class Github
def test_Github_auth():
    assert Github.auth() == TokenAuth(Github.token())



# Generated at 2022-06-14 05:16:13.620822
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"



# Generated at 2022-06-14 05:17:10.677362
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Initialize
    domain = "gitlab.com"
    repo = "gitlab-ce"
    owner = "gitlab-org"

    # Mock gitlab
    class MockGitlab(Base):
        @staticmethod
        def token():
            return "LX9OqxjKz3q3eud4H6Vk"

        @staticmethod
        def api_url():
            return f"https://gitlab/api/v4"

    with patch.dict(os.environ, {"CI_SERVER_NAME": "GitLab", "CI_SERVER_VERSION": "12.0"}):
        # Check status of a successfull build
        with patch("gitlab.Gitlab") as mock_gitlab:
            mock_gitlab.return_value = mock_gitlab
            mock_gitlab

# Generated at 2022-06-14 05:17:13.161364
# Unit test for method domain of class Github
def test_Github_domain():
    """
    This test must be run manually
    """
    # TODO: Add test
    pass


# Generated at 2022-06-14 05:17:15.819947
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.check_build_status("owner", "repo", "ref")



# Generated at 2022-06-14 05:17:18.167946
# Unit test for method api_url of class Github
def test_Github_api_url():
    expected = "https://api.github.com"
    actual = Github.api_url()
    assert actual == expected



# Generated at 2022-06-14 05:17:19.969951
# Unit test for function get_hvcs
def test_get_hvcs():
    config.show_config()
    assert(config.get("hvcs") == "github")
    assert(get_hvcs() == Github)
    assert(config.get("hvcs") == "gitlab")
    assert(get_hvcs() == Gitlab)

# Generated at 2022-06-14 05:17:24.819794
# Unit test for method domain of class Github
def test_Github_domain():
    from .helpers import get_example_package_name

    # GitHub user
    owner = "tensorflow"
    repo = get_example_package_name()
    ref = "master"

    # Check build status
    assert Github.check_build_status(owner, repo, ref)



# Generated at 2022-06-14 05:17:28.679614
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Arrange
    owner = "hookline"
    repo = "project"
    ref = "54c959a"

    # Action
    status = Gitlab.check_build_status(owner, repo, ref)

    # Assert
    assert status == True, 'Gitlab.check_build_status() has failed'

# Generated at 2022-06-14 05:17:37.462403
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    import gitlab.v4.objects
    import gitlab.v4.objects

    def mocked_requests_post(url: str, **kwargs):
        """Fake response for requests.post"""

        class MockResponse:
            """Fake response object to be returned from requests.post"""

            def __init__(self, content: str, status_code: int):
                self._content = content
                self.status_code = status_code

            def content(self) -> str:
                return self._content

        def handle_default(url: str, **kwargs) -> MockResponse:
            return MockResponse(
                '{"error": "not authenticated"}', requests.codes.unauthorized
            )


# Generated at 2022-06-14 05:17:44.937215
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    from requests import Request
    from requests.models import Response
    from semantic_release.hvcs.base import TokenAuth
    request = Request("GET", "https://www.foo.bar/")
    auth = TokenAuth(token="abcd1234")
    response = auth(request)
    assert response.headers["Authorization"] == "token abcd1234"



# Generated at 2022-06-14 05:17:47.875455
# Unit test for function get_hvcs
def test_get_hvcs():
    config.set("hvcs", "github")
    assert get_hvcs() is Github
    config.set("hvcs", "gitlab")
   

# Generated at 2022-06-14 05:18:40.728971
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    try:
        os.environ["GL_TOKEN"] = "test_token"
    except KeyError:
        pass
    assert Gitlab.check_build_status("test_owner", "test_repo"," test_ref") == False



# Generated at 2022-06-14 05:18:44.291211
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    assert Github.check_build_status("owner", "repo", "ref") == True


# Generated at 2022-06-14 05:18:55.387945
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Testing method check_build_status of class Gitlab"""
    version = "11.10.1"
    os.environ["CI_SERVER_HOST"] = "gitlab.com"
    os.environ["GL_TOKEN"] = "DyuNfjKt76-L1ec5Mo5z"
    gl = gitlab.Gitlab("https://gitlab.com", private_token="DyuNfjKt76-L1ec5Mo5z")
    gl.auth()
    jobs = gl.projects.get("tuc-photon/photon").commits.get("bsr2PJ").statuses.list()
    print(jobs[0])
    print(jobs[0]["status"])
    for job in jobs:
        print(job)
    #assert Gitlab.check

# Generated at 2022-06-14 05:18:57.357149
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() == "gitlab.com"


# Generated at 2022-06-14 05:19:01.618296
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    AuthBase.__call__(TokenAuth("token"), None)
    TokenAuth(None)(None)
    TokenAuth(None)("r")
    TokenAuth(None)("r")



# Generated at 2022-06-14 05:19:14.032420
# Unit test for method auth of class Github
def test_Github_auth():
    from requests.auth import AuthBase
    from .helpers import LoggedFunction
    from . import config
    from . import errors
    from . import settings
    from . import helpers
    from . import hvcs
    from . import version
    from .settings import ensure_configuration
    from .settings import load_configuration
    from .settings import save_configuration
    from . import config as semantic_release_config
    from .settings import config
    from .errors import ImproperConfigurationError
    import sys
    import os
    import logging
    import json
    import gitlab
    from typing import Iterable, List
    from collections import Sequence
    from enum import Enum
    import re
    import semver
    from requests.auth import AuthBase
    from urllib3 import Retry
    import mimetypes
    import pkg_resources



# Generated at 2022-06-14 05:19:16.008090
# Unit test for function get_hvcs
def test_get_hvcs():
    assert get_hvcs() == Github

# Generated at 2022-06-14 05:19:28.824677
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class TestGitlab(Gitlab):
        @staticmethod
        @LoggedFunction(logger)
        def check_build_status(owner: str, repo: str, ref: str) -> bool:
            """Check last build status

            :param owner: The owner namespace of the repository. It includes all groups and subgroups.
            :param repo: The repository name
            :param ref: The sha1 hash of the commit ref

            :return: the status of the pipeline (False if a job failed)
            """
            gl = gitlab.Gitlab(Gitlab.api_url(), private_token=Gitlab.token())
            gl.auth()
            jobs = gl.projects.get(owner + "/" + repo).commits.get(ref).statuses.list()

# Generated at 2022-06-14 05:19:34.239668
# Unit test for function get_hvcs
def test_get_hvcs():
    config.set("hvcs", "gitlab")
    assert get_hvcs().domain() == "gitlab.com"
    config.set("hvcs", "github")
    assert get_hvcs().domain() == "github.com"

    config.set("hvcs", "")
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()

# Generated at 2022-06-14 05:19:45.370936
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Unit test for method check_build_status of class Gitlab."""
    Gitlab.token = lambda: "test"
    Gitlab.api_url = lambda: "http://api.gitlab.test"
    def gitlab_test_1():
        """Unit test for method check_build_status of class Gitlab with two statuses."""
        Gitlab.check_build_status = lambda _, owner, repo, ref: [
            {"status": "success"},
            {"status": "failed"},
        ]
        assert not Gitlab.check_build_status("owner", "repo", "ref")
    def gitlab_test_2():
        """Unit test for method check_build_status of class Gitlab with pending status."""

# Generated at 2022-06-14 05:20:44.496762
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Unit test for method check_build_status of class Gitlab

    The mock is added to GL_TOKEN environment variable

    :return: None
    """
    def mock_check_build_status_no_failures(owner: str, repo: str, ref: str) -> bool:
        return True

    def mock_check_build_status_failed_no_allow_failure(
        owner: str, repo: str, ref: str
    ) -> bool:
        jobs = [
            {"name": "test_name", "status": "failed", "allow_failure": "false"}
        ]
        for job in jobs:
            if job["status"] not in ["success", "skipped", "pending"]:
                if job["status"] == "failed" and not job["allow_failure"]:
                    return False
       

# Generated at 2022-06-14 05:20:52.724137
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    from .settings import config_setter


# Generated at 2022-06-14 05:20:57.039147
# Unit test for method auth of class Github
def test_Github_auth():
    assert not Github.auth()

    config["hvcs_token"] = "123"
    assert Github.auth()
    assert Github.auth() == Github.auth()
    assert Github.auth() != TokenAuth("456")



# Generated at 2022-06-14 05:21:02.347935
# Unit test for method __call__ of class TokenAuth
def test_TokenAuth___call__():
    from requests import PreparedRequest
    from .test_helpers import random_string

    token = random_string()
    auth = TokenAuth(token)
    request = PreparedRequest()
    auth(request)
    assert request.headers["Authorization"] == f"token {token}"



# Generated at 2022-06-14 05:21:07.156283
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.check_build_status("havocdev", "hvcs.gitlab", "d7b04d815edb36ea0b1cb09d9c3cb6262ae8a0c2")


# Generated at 2022-06-14 05:21:15.129452
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    from unittest.mock import MagicMock, patch

    class mocked_job:
        def __init__(self, name, status, allow_failure):
            self.name = name
            self.status = status
            self.allow_failure = allow_failure

    mocked_jobs = [
        mocked_job("job-1", "success", False),
        mocked_job("job-2", "pending", False),
        mocked_job("job-3", "failed", False),
        mocked_job("job-4", "failed", True),
    ]

    class mocked_commits:
        def get(self, ref):
            return self

        def statuses(self):
            return self

        def list(self):
            return mocked_jobs


# Generated at 2022-06-14 05:21:20.670335
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("terraform-aws-secure-baseline", "aws-secure-baseline", "f30b1f7d3bc3bc2223c49aa2b2c846e12e56ba1c") == True


# Generated at 2022-06-14 05:21:31.748617
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    import gitlab

    # create fake response for api requests
    class FakeResponse():
        def __init__(self, text):
            self.text = text

        def json(self):
            return json.loads(self.text)

    # always return pending status
    def fake_pending(_, __, ___):
        return FakeResponse(
            json.dumps(
                {
                    "id": 1,
                    "sha": "d34db33fd43db33f",
                    "status": "pending",
                    "name": "job name",
                    "target_url": "http://example.org",
                    "ref": {"name": "latest"},
                }
            )
        )

    # always return failed status

# Generated at 2022-06-14 05:21:43.087687
# Unit test for method check_build_status of class Gitlab

# Generated at 2022-06-14 05:21:49.716567
# Unit test for function get_hvcs
def test_get_hvcs():
    class Test:
        @staticmethod
        @LoggedFunction(logger)
        def domain(self) -> str:
            return 'test_domain'
        @staticmethod
        @LoggedFunction(logger)
        def api_url(self) -> str:
            return 'test_api_url'
        @staticmethod
        @LoggedFunction(logger)
        def token(self) -> str:
            return 'test_token'
        @classmethod
        @LoggedFunction(logger)
        def check_build_status(self, owner: str, repo: str, ref: str) -> bool:
            return True