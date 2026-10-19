

# Generated at 2022-06-14 05:14:38.807065
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class Mock_Gitlab:
        def get(self, param):
            class Mock_Project:
                def __init__(self, name):
                    self.name = name

            class Mock_Commits:
                def __init__(self, sha):
                    self.sha = sha

                def get(self, sha):
                    class Mock_Statuses:
                        def __init__(self):
                            self.statuses = [['pending', False],['hidden', True]]
                            self.list = [['success', True],['failed', False]]

                    return Mock_Statuses()

            return Mock_Commits("6dcb09b5b57875f334f61aebed695e2e4193db5e")

    # If a job is hidden, the function should return True
    mock_gl = Mock_

# Generated at 2022-06-14 05:14:43.082161
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    assert Gitlab.check_build_status("hyperledger", "indy-sdk", "e4a4b4e17d4f4e4d9a9a2b1c0c769b4d425c39f4")



# Generated at 2022-06-14 05:14:50.474237
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Method should return true if all jobs of the pipeline succeeded
    ref = Gitlab.check_build_status("Radical-Cybertools", "radical.analytics", "921a5f6b7")
    assert ref==True

    # Method should return false if atleast one of the jobs of the pipeline failed
    ref = Gitlab.check_build_status("Radical-Cybertools", "radical.analytics", "4e11a4da8")
    assert ref==False

# Generated at 2022-06-14 05:14:52.460337
# Unit test for method auth of class Github
def test_Github_auth():
    # Checks the auth function returns an object of the TokenAuth class.
    assert isinstance(Github.auth(), TokenAuth)



# Generated at 2022-06-14 05:14:57.460390
# Unit test for function get_hvcs
def test_get_hvcs():
    config.set("hvcs", "github")
    assert isinstance(get_hvcs(), Github)
    config.set("hvcs", "gitlab")
    assert isinstance(get_hvcs(), Gitlab)
    with pytest.raises(ImproperConfigurationError):
        config.set("hvcs", "nonexistent")
        get_hvcs()
    config.reset()



# Generated at 2022-06-14 05:15:03.522178
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    def mock_statuses_list(*args, **kwargs):
        return [
            {"name": "job1", "status": "success", "allow_failure": False},
            {"name": "job2", "status": "pending", "allow_failure": False},
            {"name": "job3", "status": "failed", "allow_failure": True},
        ]


# Generated at 2022-06-14 05:15:04.932707
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    from tests.fixtures import commit_sha1, project_name, namespace

    assert not Gitlab.check_build_status(namespace, project_name, commit_sha1)



# Generated at 2022-06-14 05:15:10.433964
# Unit test for method auth of class Github
def test_Github_auth():
    Github.DEFAULT_DOMAIN = "github.com"
    token = os.environ.get("GH_TOKEN")
    if not token:
        raise ImproperConfigurationError(
            "GH_TOKEN environment variable is not set"
        )
    assert Github.domain() == "github.com"
    assert Github.api_url() == "https://api.github.com"
    assert Github.token() == token
    assert Github.auth() == TokenAuth(token)



# Generated at 2022-06-14 05:15:12.554819
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    # arrange
    with patch.object(
        config,
        "get",
        return_value="test.test.test"
    ):
        # act
        domain = Gitlab.domain()
        # assert
        assert domain == "test.test.test"

# Generated at 2022-06-14 05:15:18.568648
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab_check_build_status = Gitlab.check_build_status("t3", "t3", "t3")
    logger.debug(f"Gitlab_check_build_status is {Gitlab_check_build_status}")
    assert Gitlab_check_build_status == False


# Generated at 2022-06-14 05:16:36.625972
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Test with a successful build
    assert Gitlab.check_build_status("votca", "csg-tutorials", "055faf57d83ca7b2c79fdb82972d5789d30823b0")
    # Test with a pending build
    assert not Gitlab.check_build_status("votca", "votca-tools", "c5f865e6645c5e90a7f96e5cd8a5d2fe5ed52772")
    # Test with a failed build
    assert not Gitlab.check_build_status("votca", "votca-tools", "b72a9fc311393d304448c390f6b65c60289415a4")
    # Test with a failed but allowed build
    assert Gitlab.check_build

# Generated at 2022-06-14 05:16:38.914209
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    # Check if get the Gitlab domain
    assert Gitlab.domain()
    
    

# Generated at 2022-06-14 05:16:43.626968
# Unit test for function get_hvcs
def test_get_hvcs():
    hvcs = get_hvcs()
    if config.get("hvcs") == 'github':
        assert isinstance(hvcs, Github)
    elif config.get("hvcs") == 'gitlab':
        assert isinstance(hvcs, Gitlab)

# Generated at 2022-06-14 05:16:50.016641
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    domain = Github.domain()
    api_url = Github.api_url()
    token = Github.token()
    owner = config.get("HVCS_OWNER")
    repo = config.get("HVCS_REPO")
    ref = config.get("HVCS_REF")
    Github.session()
    Github.check_build_status(owner, repo, ref)

    # Create release
    tag = "v0.0.1"
    changelog = "Release notes for version 0.0.1"
    Github.create_release(owner, repo, tag, changelog)

    # Get release
    Github.get_release(owner, repo, tag)

    # Upload asset
    file = "README.md"
    release_id = 0

# Generated at 2022-06-14 05:16:51.437390
# Unit test for method auth of class Github
def test_Github_auth():
    o = Github()
    t = o.auth()
    compare = TokenAuth(Github.token())
    assert t == compare

    # Unit test for method check_build_status of class Github

# Generated at 2022-06-14 05:17:00.727411
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Build successful
    assert Gitlab.check_build_status(
        owner="pawamoy",
        repo="pymerino",
        ref="3fea3e1cad568d772f6c7b6aa2b6d744d8fe2a91"
    )

    # Build failed
    assert not Gitlab.check_build_status(
        owner="pawamoy",
        repo="pymerino",
        ref="ae7b07a41ad09ebbc31bab4af4a97b2e5a967b75"
    )



# Generated at 2022-06-14 05:17:09.561303
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Case where build status is ok
    owner = "CornellNLP"
    repo = "Cornell-Conversational-Analysis-Toolkit"
    ref = "9f7529a3f3be3d2c4a4e4a4a4b1833c0323f0424"
    assert Gitlab.check_build_status(owner, repo, ref) == True
    # Case where build status is not ok
    ref = "78752dc394f83c031d859e5f5e2f46554b353490"
    assert Gitlab.check_build_status(owner, repo, ref) == False
test_Gitlab_check_build_status()

# Generated at 2022-06-14 05:17:16.765692
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Test for the Gitlab method check_build_status"""
    owner = "julianboykov"
    repo = "Swarthmore-Events"
    ref = "d6ba13e6d5c4399ddf6b9d6eba366821e4f8c571"
    status = Gitlab.check_build_status(owner, repo, ref)
    assert status == False


# Generated at 2022-06-14 05:17:31.252035
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    import requests_mock


# Generated at 2022-06-14 05:17:33.341602
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    Gitlab.check_build_status(owner=None, repo=None, ref=None)

# Generated at 2022-06-14 05:18:42.430439
# Unit test for method domain of class Gitlab
def test_Gitlab_domain():
    assert Gitlab.domain() == "gitlab.com"


# Generated at 2022-06-14 05:18:43.277689
# Unit test for function get_hvcs
def test_get_hvcs():
    config._config.set("hvcs", "github")
    assert get_hvcs() == Github



# Generated at 2022-06-14 05:18:50.772469
# Unit test for method check_build_status of class Github
def test_Github_check_build_status():
    h1 = Github()

    owner = "test"
    repo = "test"
    ref = "test"
    if h1.check_build_status(owner=owner, repo=repo, ref=ref):
        logger.debug('Test of method "check_build_status" in class "Github" has passed')
    else:
        logger.error('Test of method "check_build_status" in class "Github" has failed')

# Generated at 2022-06-14 05:19:04.511584
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    class TestGitlab(Gitlab):
        @staticmethod
        def token():
            return os.environ.get("GL_TOKEN")

    assert TestGitlab.check_build_status(
        owner="mgeorgiou-dev", repo="test-repo-for-gitlab", ref="v7.0.0"
    ) == True
    assert TestGitlab.check_build_status(
        owner="mgeorgiou-dev", repo="test-repo-for-gitlab", ref="v6.0.0"
    ) == False
    assert TestGitlab.check_build_status(
        owner="mgeorgiou-dev", repo="test-repo-for-gitlab", ref="v5.0.0"
    ) == False
    assert TestGitlab

# Generated at 2022-06-14 05:19:15.687587
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Case 1:
    #   - owner = flamel
    #   - repo = flamel-hvcs
    #   - ref = df7b4d4b4f4b4fb4f4b4fb4b4fb4f4bf4f4b4bf4b4f
    # -> False
    print("Check that if the status of the pipeline is not success, the method will return false:")
    assert Gitlab.check_build_status(
        owner="flamel", repo="flamel-hvcs", ref="df7b4d4b4f4b4fb4f4b4fb4b4fb4f4bf4f4b4bf4b4f"
    ) == False

    # Case 2:
    #   - owner = flamel
    #   - repo = flamel-

# Generated at 2022-06-14 05:19:21.724272
# Unit test for function get_hvcs
def test_get_hvcs():
    os.environ['HVCS']='github'
    get_hvcs() == os.environ['HVCS']
    os.environ['HVCS']='gitlab'
    get_hvcs() == os.environ['HVCS']



# Generated at 2022-06-14 05:19:26.770842
# Unit test for function get_hvcs
def test_get_hvcs():
    """Test function "_get_hvcs" in "hvcs_utils.py"."""
    assert get_hvcs() is Github
    config.set("hvcs", "gitlab")
    assert get_hvcs() is Gitlab
    config.set("hvcs", "github")

# Generated at 2022-06-14 05:19:32.274784
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Unit test for class Gitlab: tests the method check_build_status
    ref_sha = "1b305934b19e39b857daf9cf6f2bb4619573c6b2"
    print(Gitlab.check_build_status("HPC-Simulation-and-Modelling", "spack", ref_sha))

# Generated at 2022-06-14 05:19:44.334810
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    p = gitlab.Gitlab(Gitlab.api_url(), private_token=Gitlab.token())
    p.auth()
    c = p.projects.get("9230141").commits.get("b3ac3be")
    jobs = c.statuses.list()
    for job in jobs:
        # Testing the following cases: still pending, fail, success
        if job["status"] == "success":
            assert Gitlab.check_build_status("9230141", "python-gitlab", "b3ac3be") is True
        elif job["status"] == "pending":
            assert Gitlab.check_build_status("9230141", "python-gitlab", "b3ac3be") is False
        elif job["status"] == "failed":
            assert Gitlab.check

# Generated at 2022-06-14 05:19:48.089398
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    #Test check_build_status with a real job in Gitlab
    return Gitlab.check_build_status("QCH", "QCH-2264-CI-CD", "e2e40b6d5ee529837b6a532f9e4d473fddc76bbb")



# Generated at 2022-06-14 05:22:12.737593
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == 'https://api.github.com'


# Generated at 2022-06-14 05:22:14.366821
# Unit test for method domain of class Github
def test_Github_domain():
    assert Github.domain() == "github.com"

# Generated at 2022-06-14 05:22:19.388995
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    """Check if the output of the method is correct"""
    logger.debug(f"Test for check build status method of class Gitlab")
    owner = "EdoardoLorenzini"
    repo = "python-repo-manager"
    ref = "0f360d94c9eb91454a85f0e1cb8cb7c0a973541a"
    assert Gitlab.check_build_status(owner, repo, ref) == True


# Generated at 2022-06-14 05:22:29.764263
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():

    # Creating an object for class Gitlab
    g=Gitlab()

    # URL for to get the commit sha
    url = "https://gitlab.com/api/v4/projects/26108112/repository/commits"

    # Get the commit sha of the latest commit from the url
    commit_sha = requests.get(url).json()[0]["id"]

    # Testing for check_build_status method
    assert g.check_build_status("luminoso", "vivoservice", commit_sha) == True

# Generated at 2022-06-14 05:22:40.065214
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    @pytest.fixture(scope="module")
    def gl(request):
        # Create a new Gitlab session
        gl = gitlab.Gitlab(Gitlab.api_url(), private_token=Gitlab.token())
        gl.auth()
        return gl

    @pytest.fixture(scope="module")
    def owner(request):
        return config.get("hvcs_owner")

    @pytest.fixture(scope="module")
    def repo(request):
        return config.get("hvcs_repo")

    def test_check_build_status_fail(gl, owner, repo):
        # Get id of last commit
        repo_obj = gl.projects.get(owner + "/" + repo)
        commits = repo_obj.commits.list()

# Generated at 2022-06-14 05:22:41.622845
# Unit test for method api_url of class Github
def test_Github_api_url():
    assert Github.api_url() == "https://api.github.com"



# Generated at 2022-06-14 05:22:54.320120
# Unit test for method check_build_status of class Gitlab
def test_Gitlab_check_build_status():
    # Mock the request call
    with patch("requests.get") as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value={"state":"something"}
        assert not Gitlab.check_build_status("owner","repo","ref")

    with patch("requests.get") as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value={"state":"success"}
        assert Gitlab.check_build_status("owner","repo","ref")

    with patch("requests.get") as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 404