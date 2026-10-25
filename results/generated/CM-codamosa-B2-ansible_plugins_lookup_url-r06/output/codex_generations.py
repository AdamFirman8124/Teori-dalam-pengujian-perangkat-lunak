

# Generated at 2026-10-24 11:13:58.890484
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:00.317490
# Unit test for constructor of class LookupModule
def test_LookupModule():
    # constructor is inherited from LookupBase - no custom __init__
    assert LookupModule.__init__ is LookupBase.__init__

    lookup = LookupModule()
    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

    # default attrs from LookupBase
    assert lookup._loader is None
    assert lookup._templar is None

# Generated at 2026-10-24 11:14:03.088186
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:04.618923
# Unit test for constructor of class LookupModule
def test_LookupModule():
    # constructor is inherited from LookupBase - no custom __init__
    assert LookupModule.__init__ is LookupBase.__init__

    lookup = LookupModule()
    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

    # default attrs from LookupBase
    assert lookup._loader is None
    assert lookup._templar is None

# Generated at 2026-10-24 11:14:07.799417
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:10.767940
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:13.420523
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:16.206745
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:19.161959
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:21.832268
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:24.567002
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:27.273435
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:30.899636
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:33.411658
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:14:35.949276
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:14:38.365984
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:14:40.959040
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:14:42.331849
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-24 11:14:45.279931
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:47.923387
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:50.556570
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:53.189599
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:56.215180
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:14:59.000149
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:15:01.774859
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:15:04.579289
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:15:07.105470
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:09.624381
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:12.044548
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:14.465973
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:16.895301
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:19.313007
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:22.520328
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:25.201013
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:27.619567
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:30.038515
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:32.460350
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:34.879797
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:37.299415
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:39.722303
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:42.141162
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:44.559336
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:46.980088
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:49.397798
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:51.818751
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:54.240161
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:56.660903
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:15:59.077177
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:01.498158
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:03.916844
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:06.331231
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:08.749983
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:11.168038
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:13.586576
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:16.003880
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:18.422891
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:20.842300
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:23.260394
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:25.677515
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:28.096599
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:30.517535
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:32.935339
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:36.165993
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:38.585572
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:41.004732
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:43.438339
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:46.020239
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.plugins.lookup.url import LookupModule

    fake_response = MagicMock()
    fake_response.read.return_value = b"line1\nline2\n"

    with patch('ansible.plugins.lookup.url.open_url', return_value=fake_response) as mock_open:
        lookup = LookupModule()

        # split_lines defaults to True -> one list entry per line
        result = lookup.run(['https://example.com/data.txt'])
        assert result == ['line1', 'line2']
        assert mock_open.call_count == 1
        assert mock_open.call_args[0][0] == 'https://example.com/data.txt'
        assert mock_open.call_args[1]['validate_certs'] is True
        assert mock_open.call_args[1]['use_proxy'] is True
        assert mock_open.call_args[1]['timeout'] == 10
        assert mock_open.call_args[1]['http_agent'] == 'ansible-httpget'

        # split_lines=False -> whole body as a single blob
        mock_open.reset_mock()
        result = lookup.run(['https://example.com/data.txt'], split_lines=False)
        assert result == ['line1\nline2\n']
        assert mock_open.call_count == 1
        assert mock_open.call_args[0][0] == 'https://example.com/data.txt'

        # multiple terms -> one response per term, in order
        mock_open.reset_mock()
        result = lookup.run(['https://example.com/a.txt', 'https://example.com/b.txt'])
        assert result == ['line1', 'line2', 'line1', 'line2']
        assert mock_open.call_count == 2
        assert mock_open.call_args_list[0][0][0] == 'https://example.com/a.txt'
        assert mock_open.call_args_list[1][0][0] == 'https://example.com/b.txt'

        # options are forwarded to open_url
        mock_open.reset_mock()
        lookup.run(['https://example.com/secure.txt'],
                   validate_certs=False, use_proxy=False, timeout=5.5,
                   username='bob', password='hunter2', force_basic_auth=True)
        kwargs = mock_open.call_args[1]
        assert kwargs['validate_certs'] is False
        assert kwargs['use_proxy'] is False
        assert kwargs['timeout'] == 5.5
        assert kwargs['url_username'] == 'bob'
        assert kwargs['url_password'] == 'hunter2'
        assert kwargs['force_basic_auth'] is True

# Generated at 2026-10-24 11:16:48.950474
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:16:51.626492
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:16:54.406309
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:16:57.185762
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:17:00.235090
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:17:02.888125
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:17:05.518081
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:17:08.254153
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:17:16.621394
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:17:19.288508
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:17:21.710433
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:24.128247
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:26.547735
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:29.153054
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:31.670165
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:34.097275
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:36.511404
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:38.932514
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:41.494056
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:43.917915
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:46.340411
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:48.759913
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:17:51.460635
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:17:54.207631
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:17:56.851742
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:17:59.736057
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:18:12.578890
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:18:15.237055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:18:17.892071
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:18:20.498055
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:22.916368
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:25.488145
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:27.995655
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:30.415476
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:32.973925
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:35.397280
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:37.812216
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:40.234418
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:42.656803
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:45.075266
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:47.497442
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:49.919687
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:18:51.367936
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-24 11:18:54.099899
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:18:56.754746
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:19:22.499467
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:19:25.012232
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:27.434985
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:29.855739
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:32.279232
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:34.699696
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:37.121075
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:39.541721
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:41.962049
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:44.381191
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:46.800165
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:49.218744
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:51.636021
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:54.051449
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:56.468964
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:19:58.886589
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:20:01.305033
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:20:03.722490
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:20:06.138802
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:20:08.557053
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:20:10.975195
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:20:13.394546
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:20:15.810420
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:20:18.229167
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:20:20.799703
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.plugins.lookup.url import LookupModule

    fake_response = MagicMock()
    fake_response.read.return_value = b"line1\nline2\n"

    with patch('ansible.plugins.lookup.url.open_url', return_value=fake_response) as mock_open:
        lookup = LookupModule()

        # split_lines defaults to True -> one list entry per line
        result = lookup.run(['https://example.com/data.txt'])
        assert result == ['line1', 'line2']
        assert mock_open.call_count == 1
        assert mock_open.call_args[0][0] == 'https://example.com/data.txt'
        assert mock_open.call_args[1]['validate_certs'] is True
        assert mock_open.call_args[1]['use_proxy'] is True
        assert mock_open.call_args[1]['timeout'] == 10
        assert mock_open.call_args[1]['http_agent'] == 'ansible-httpget'

        # split_lines=False -> whole body as a single blob
        mock_open.reset_mock()
        result = lookup.run(['https://example.com/data.txt'], split_lines=False)
        assert result == ['line1\nline2\n']
        assert mock_open.call_count == 1
        assert mock_open.call_args[0][0] == 'https://example.com/data.txt'

        # multiple terms -> one response per term, in order
        mock_open.reset_mock()
        result = lookup.run(['https://example.com/a.txt', 'https://example.com/b.txt'])
        assert result == ['line1', 'line2', 'line1', 'line2']
        assert mock_open.call_count == 2
        assert mock_open.call_args_list[0][0][0] == 'https://example.com/a.txt'
        assert mock_open.call_args_list[1][0][0] == 'https://example.com/b.txt'

        # options are forwarded to open_url
        mock_open.reset_mock()
        lookup.run(['https://example.com/secure.txt'],
                   validate_certs=False, use_proxy=False, timeout=5.5,
                   username='bob', password='hunter2', force_basic_auth=True)
        kwargs = mock_open.call_args[1]
        assert kwargs['validate_certs'] is False
        assert kwargs['use_proxy'] is False
        assert kwargs['timeout'] == 5.5
        assert kwargs['url_username'] == 'bob'
        assert kwargs['url_password'] == 'hunter2'
        assert kwargs['force_basic_auth'] is True

# Generated at 2026-10-24 11:20:23.552306
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:21:10.864770
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:21:13.285059
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:21:15.704567
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:21:18.126423
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:21:20.546959
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:21:38.342767
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.plugins.lookup.url import LookupModule

    fake_response = MagicMock()
    fake_response.read.return_value = b"line1\nline2\n"

    with patch('ansible.plugins.lookup.url.open_url', return_value=fake_response) as mock_open:
        lookup = LookupModule()

        # split_lines defaults to True -> one list entry per line
        result = lookup.run(['https://example.com/data.txt'])
        assert result == ['line1', 'line2']
        assert mock_open.call_count == 1
        assert mock_open.call_args[0][0] == 'https://example.com/data.txt'
        assert mock_open.call_args[1]['validate_certs'] is True
        assert mock_open.call_args[1]['use_proxy'] is True
        assert mock_open.call_args[1]['timeout'] == 10
        assert mock_open.call_args[1]['http_agent'] == 'ansible-httpget'

        # split_lines=False -> whole body as a single blob
        mock_open.reset_mock()
        result = lookup.run(['https://example.com/data.txt'], split_lines=False)
        assert result == ['line1\nline2\n']
        assert mock_open.call_count == 1
        assert mock_open.call_args[0][0] == 'https://example.com/data.txt'

        # multiple terms -> one response per term, in order
        mock_open.reset_mock()
        result = lookup.run(['https://example.com/a.txt', 'https://example.com/b.txt'])
        assert result == ['line1', 'line2', 'line1', 'line2']
        assert mock_open.call_count == 2
        assert mock_open.call_args_list[0][0][0] == 'https://example.com/a.txt'
        assert mock_open.call_args_list[1][0][0] == 'https://example.com/b.txt'

        # options are forwarded to open_url
        mock_open.reset_mock()
        lookup.run(['https://example.com/secure.txt'],
                   validate_certs=False, use_proxy=False, timeout=5.5,
                   username='bob', password='hunter2', force_basic_auth=True)
        kwargs = mock_open.call_args[1]
        assert kwargs['validate_certs'] is False
        assert kwargs['use_proxy'] is False
        assert kwargs['timeout'] == 5.5
        assert kwargs['url_username'] == 'bob'
        assert kwargs['url_password'] == 'hunter2'
        assert kwargs['force_basic_auth'] is True

# Generated at 2026-10-24 11:21:41.102567
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:21:43.709572
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:21:46.364167
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:21:49.037745
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:21:51.670001
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:21:55.222619
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:21:57.997838
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:22:00.419992
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:22:02.835271
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:22:05.253794
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:22:07.785713
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:22:10.206191
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:23:37.068647
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:23:39.713409
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:23:42.410242
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:23:45.058495
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:23:47.719167
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:23:50.367185
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:23:53.007397
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:23:55.637993
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")

# Generated at 2026-10-24 11:23:58.333290
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    url = "https://example.com/data.txt"
    content = b"line1\nline2\nline3"

    def make_lookup(options):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda name: options[name])
        return lookup

    # Case 1: split_lines=True -> returns list of lines
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url])
        assert result == ["line1", "line2", "line3"], result
        lookup.set_options.assert_called_once_with(var_options=None, direct={})
        args, kwargs = __import__("unittest").mock.patch.__dict__.get("_x", (None, None)) or open_url.call_args
        assert kwargs["validate_certs"] is True
        assert kwargs["url_username"] is None
        assert kwargs["url_password"] is None
        assert kwargs["timeout"] == 10

    # Case 2: split_lines=False -> returns single text blob
    mock_response = MagicMock()
    mock_response.read.return_value = content
    with patch("__main__.open_url", return_value=mock_response):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": "bob",
            "password": "hunter2",
            "headers": {"X-Test": "1"},
            "force": False,
            "timeout": 5,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": False,
        })
        result = lookup.run([url])
        assert result == ["line1\nline2\nline3"], result
        kwargs = open_url.call_args.kwargs
        assert kwargs["url_username"] == "bob"
        assert kwargs["url_password"] == "hunter2"
        assert kwargs["headers"] == {"X-Test": "1"}
        assert kwargs["timeout"] == 5

    # Case 3: multiple terms -> results concatenated in order
    resp1 = MagicMock()
    resp1.read.return_value = b"a\nb"
    resp2 = MagicMock()
    resp2.read.return_value = b"c"
    with patch("__main__.open_url", side_effect=[resp1, resp2]):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        result = lookup.run([url, url])
        assert result == ["a", "b", "c"], result

    # Case 4: HTTPError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=HTTPError(url, 404, "Not Found", {}, None)):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("HTTPError did not raise AnsibleError")

    # Case 5: URLError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=URLError("connection refused")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("URLError did not raise AnsibleError")

    # Case 6: SSLValidationError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=SSLValidationError("bad cert")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("SSLValidationError did not raise AnsibleError")

    # Case 7: ConnectionError -> AnsibleError raised
    with patch("__main__.open_url", side_effect=ConnectionError("timeout")):
        lookup = make_lookup({
            "validate_certs": True,
            "use_proxy": True,
            "username": None,
            "password": None,
            "headers": {},
            "force": False,
            "timeout": 10,
            "http_agent": "ansible-httpget",
            "force_basic_auth": False,
            "follow_redirects": "urllib2",
            "use_gssapi": False,
            "unix_socket": None,
            "ca_path": None,
            "unredirected_headers": None,
            "split_lines": True,
        })
        try:
            lookup.run([url])
        except AnsibleError:
            pass
        else:
            raise AssertionError("ConnectionError did not raise AnsibleError")