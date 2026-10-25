

# Generated at 2026-10-24 10:59:40.153982
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

# Generated at 2026-10-24 10:59:42.572041
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 10:59:44.988999
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 10:59:47.545929
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 10:59:49.965259
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 10:59:52.381256
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 10:59:54.799279
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 10:59:57.218583
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 10:59:59.644854
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 11:00:02.064245
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 11:00:04.479224
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:00:06.902031
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:00:09.325974
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:00:11.748905
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:00:14.169490
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:00:16.588999
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:00:19.010711
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:00:32.173841
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-24 11:01:11.602641
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

# Generated at 2026-10-24 11:01:14.124392
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:01:16.543179
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:01:18.962393
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:01:21.846227
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

# Generated at 2026-10-24 11:01:24.705837
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

# Generated at 2026-10-24 11:01:27.367117
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

# Generated at 2026-10-24 11:01:29.991122
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

# Generated at 2026-10-24 11:01:32.624434
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

# Generated at 2026-10-24 11:01:35.275017
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

# Generated at 2026-10-24 11:01:37.902250
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

# Generated at 2026-10-24 11:01:40.541904
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

# Generated at 2026-10-24 11:01:43.354262
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

# Generated at 2026-10-24 11:01:46.019383
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

# Generated at 2026-10-24 11:01:48.649651
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:01:51.067414
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:01:53.482809
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:01:56.072143
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:01:58.489993
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:02:00.910877
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:02:03.331633
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:02:05.749082
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:02:08.170961
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:02:10.592094
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:02:13.011262
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:02:15.427493
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:02:17.846627
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:02:20.262959
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:02:22.680278
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:02:25.099045
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:03:28.208131
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

# Generated at 2026-10-24 11:03:30.880226
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

# Generated at 2026-10-24 11:03:33.519996
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

# Generated at 2026-10-24 11:03:36.194785
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

# Generated at 2026-10-24 11:03:38.940904
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

# Generated at 2026-10-24 11:03:41.524089
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

# Generated at 2026-10-24 11:03:44.293714
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

# Generated at 2026-10-24 11:03:46.959589
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

# Generated at 2026-10-24 11:03:49.632998
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

# Generated at 2026-10-24 11:03:52.580263
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

# Generated at 2026-10-24 11:03:55.256450
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

# Generated at 2026-10-24 11:03:57.927203
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

# Generated at 2026-10-24 11:04:00.701911
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:04:03.225959
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:04:05.651402
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:04:08.195936
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:04:10.714517
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:04:13.134858
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:04:15.697650
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:04:18.120417
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:04:20.762851
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:04:23.188136
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:04:25.798672
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

# Generated at 2026-10-24 11:04:28.450472
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

# Generated at 2026-10-24 11:04:31.084379
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

# Generated at 2026-10-24 11:04:33.800265
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

# Generated at 2026-10-24 11:04:36.551635
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

# Generated at 2026-10-24 11:04:39.578646
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

# Generated at 2026-10-24 11:04:42.763528
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

# Generated at 2026-10-24 11:04:45.416583
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

# Generated at 2026-10-24 11:04:48.586810
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

# Generated at 2026-10-24 11:04:51.285089
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

# Generated at 2026-10-24 11:04:53.978704
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

# Generated at 2026-10-24 11:04:56.700413
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

# Generated at 2026-10-24 11:04:59.447320
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

# Generated at 2026-10-24 11:05:02.207506
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

# Generated at 2026-10-24 11:05:04.628870
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:07.048957
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:09.470013
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:11.894899
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:14.511740
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:16.920000
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:21.563760
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:23.990363
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:26.618213
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

# Generated at 2026-10-24 11:05:29.335812
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

# Generated at 2026-10-24 11:05:32.015222
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

# Generated at 2026-10-24 11:05:34.661139
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

# Generated at 2026-10-24 11:05:37.741961
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

# Generated at 2026-10-24 11:05:40.372580
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

# Generated at 2026-10-24 11:05:43.016689
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

# Generated at 2026-10-24 11:05:45.671188
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

# Generated at 2026-10-24 11:05:48.419989
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:50.970044
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:53.495225
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:55.909964
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:05:58.329678
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:06:00.751165
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:06:07.991102
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:06:10.406928
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:06:12.824691
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:06:15.244975
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:06:17.659659
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:06:20.077411
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:06:22.641373
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:06:25.057531
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:06:27.477216
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:06:30.092213
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

# Generated at 2026-10-24 11:06:32.991123
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

# Generated at 2026-10-24 11:06:35.698957
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

# Generated at 2026-10-24 11:06:38.354040
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

# Generated at 2026-10-24 11:06:41.039798
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

# Generated at 2026-10-24 11:06:43.780862
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

# Generated at 2026-10-24 11:06:46.554130
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

# Generated at 2026-10-24 11:07:00.854577
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

# Generated at 2026-10-24 11:07:03.536876
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

# Generated at 2026-10-24 11:07:06.041887
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:08.664469
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:11.195799
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:13.617731
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:16.033304
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:18.558478
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:20.976823
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:23.549938
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:25.968923
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:28.387281
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:30.805906
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:33.224706
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:35.643094
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:38.060932
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:40.480159
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:42.905040
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:45.322184
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:47.745890
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:50.164299
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:52.585617
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:55.002335
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:57.420259
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:59.838343
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:02.257847
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:23.527197
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:25.943959
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:28.737599
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

# Generated at 2026-10-24 11:08:31.433735
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

# Generated at 2026-10-24 11:08:34.078093
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

# Generated at 2026-10-24 11:08:36.748111
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

# Generated at 2026-10-24 11:08:39.395702
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

# Generated at 2026-10-24 11:08:42.084578
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

# Generated at 2026-10-24 11:08:44.826217
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

# Generated at 2026-10-24 11:08:47.553527
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

# Generated at 2026-10-24 11:08:50.276552
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

# Generated at 2026-10-24 11:08:52.962102
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