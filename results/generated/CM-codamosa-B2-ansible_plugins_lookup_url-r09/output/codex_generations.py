

# Generated at 2026-10-25 11:20:53.672334
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:20:56.903613
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:21:07.767857
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:21:13.176832
# Unit test for constructor of class LookupModule
def test_LookupModule():
    from ansible.plugins.lookup.url import LookupModule

    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupModule)

# Generated at 2026-10-25 11:21:14.507415
# Unit test for constructor of class LookupModule
def test_LookupModule():
    from ansible.plugins.lookup.url import LookupModule

    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupModule)

# Generated at 2026-10-25 11:21:24.136857
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:21:27.721679
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:21:30.793595
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:21:33.868499
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:21:36.635751
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:21:40.622736
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:21:43.796118
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:21:54.656043
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:22:04.053742
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:06.631258
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:09.038845
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:11.453672
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:13.870553
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:16.284080
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:18.701475
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:21.151724
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:23.952736
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:26.372023
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:28.781556
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:31.194921
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:33.612565
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:36.032378
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:38.452147
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:40.860224
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:43.273816
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:45.690589
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:48.108073
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:50.527008
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:52.944349
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:55.356369
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:22:57.772996
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:23:00.186761
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:23:03.201188
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:23:07.757810
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:23:10.757882
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:23:16.969931
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:23:20.978492
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:23:23.889466
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:23:28.553878
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:23:30.973291
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:23:51.489486
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-25 11:23:54.282497
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:24:00.405258
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:24:09.719216
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:24:12.769770
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:24:15.647183
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:24:18.396291
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:24:20.808031
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:24:23.309742
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:24:26.128437
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:24:28.542760
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:24:31.079381
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:24:33.492599
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:24:35.907537
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:24:38.507379
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-25 11:24:42.117883
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:24:46.691005
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:24:52.612178
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:24:55.334862
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:24:58.037906
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:00.451650
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:02.871590
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:05.285057
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:07.698826
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:10.448128
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:12.860510
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:15.282868
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:17.696654
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:20.113202
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:22.526139
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:24.944466
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:27.356142
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:29.773898
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:32.543423
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:35.628839
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:38.043610
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:40.457403
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:42.870644
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:45.282600
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:47.695883
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:50.109360
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:52.521859
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:54.936452
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:57.349249
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:25:59.766116
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:02.185021
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:04.598313
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:07.012642
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:09.427664
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:11.843689
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:14.256164
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:16.667107
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:19.080950
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:21.496000
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:23.913791
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:26.325740
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:28.739500
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:31.154828
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:33.569227
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:35.982726
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:38.397864
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:40.813441
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:43.228186
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:45.645014
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:50.115606
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:52.530179
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:54.944644
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:57.393287
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:26:59.777401
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:02.190264
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:04.605569
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:07.019598
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:09.435149
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:11.853362
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:14.268333
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:16.687486
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:19.102071
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:21.515459
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:23.933580
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:26.345763
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:28.764698
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:31.180819
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:33.595250
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:36.009296
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:38.423759
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:27:44.611108
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:27:47.672717
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:27:50.598534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:28:02.064357
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:28:05.037210
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:28:08.300879
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class FakeResponse(object):
        def __init__(self, content=b"line1\nline2\n"):
            self._content = content

        def read(self):
            return self._content

    DEFAULT_OPTIONS = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
    }

    def _make_lookup(options=None):
        from ansible.plugins.lookup.url import LookupModule
        lookup = LookupModule()
        merged = dict(DEFAULT_OPTIONS)
        if options:
            merged.update(options)
        lookup.get_option = lambda name: merged[name]
        lookup.set_options = MagicMock()
        return lookup

    # --- Test 1: default split_lines=True returns list of lines ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == ['a', 'b', 'c'], result

    # --- Test 2: split_lines=False returns a single text blob ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"a\nb\nc")):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://example.com'])
        assert result == ['a\nb\nc'], result

    # --- Test 3: multiple terms are processed in order ---
    responses = [FakeResponse(b"one"), FakeResponse(b"two")]
    with patch('ansible.plugins.lookup.url.open_url', side_effect=responses):
        lookup = _make_lookup({'split_lines': False})
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])
        assert result == ['one', 'two'], result

    # --- Test 4: options are forwarded to open_url ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(b"x")) as mock_open:
        lookup = _make_lookup({
            'validate_certs': False,
            'use_proxy': False,
            'username': 'bob',
            'password': 'hunter2',
            'headers': {'X-Test': '1'},
            'force': True,
            'timeout': 30.0,
            'force_basic_auth': True,
            'follow_redirects': 'all',
        })
        lookup.run(['http://example.com'])
        mock_open.assert_called_once_with(
            'http://example.com',
            validate_certs=False,
            use_proxy=False,
            url_username='bob',
            url_password='hunter2',
            headers={'X-Test': '1'},
            force=True,
            timeout=30.0,
            http_agent='ansible-httpget',
            force_basic_auth=True,
            follow_redirects='all',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # --- Test 5: HTTPError is wrapped into AnsibleError ---
    def _raise_http(*args, **kwargs):
        raise HTTPError('http://example.com', 404, 'Not Found', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_http):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for HTTPError")

    # --- Test 6: URLError is wrapped into AnsibleError ---
    def _raise_url(*args, **kwargs):
        raise URLError('connection refused')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_url):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for URLError")

    # --- Test 7: SSLValidationError is wrapped into AnsibleError ---
    def _raise_ssl(*args, **kwargs):
        raise SSLValidationError('bad cert')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_ssl):
        try:
            lookup = _make_lookup()
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert 'Error validating the server' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for SSLValidationError")

    # --- Test 8: ConnectionError is wrapped into AnsibleError ---
    def _raise_conn(*args, **kwargs):
        raise ConnectionError('timed out')

    with patch('ansible.plugins.lookup.url.open_url', side_effect=_raise_conn):
        try:
            lookup = _make_lookup()
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in to_native(e), to_native(e)
        else:
            raise AssertionError("AnsibleError not raised for ConnectionError")

    # --- Test 9: binary content is decoded to text ---
    with patch('ansible.plugins.lookup.url.open_url', return_value=FakeResponse(u'hÃ©llo wÃ¶rld\n'.encode('utf-8'))):
        lookup = _make_lookup()
        result = lookup.run(['http://example.com'])
        assert result == [u'hÃ©llo wÃ¶rld'], result

    # --- Test 10: empty terms list returns empty list ---
    with patch('ansible.plugins.lookup.url.open_url') as mock_open:
        lookup = _make_lookup()
        result = lookup.run([])
        assert result == [], result
        mock_open.assert_not_called()

# Generated at 2026-10-25 11:28:10.868479
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:13.573041
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:15.991129
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:18.686137
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:21.103600
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:23.518909
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:25.934177
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:28.594118
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:31.009200
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:33.424964
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:35.839216
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:38.253032
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:40.669036
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:43.084322
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:45.497975
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:47.914346
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:50.332559
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:52.743302
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:55.157368
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:57.572778
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:28:59.985423
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:16.929309
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:19.342237
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:21.756693
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:24.171554
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:26.647186
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:29.053295
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:31.468268
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:33.882096
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:36.297297
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:38.778678
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:41.174328
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:43.592285
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:46.002575
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:48.417381
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:50.830269
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:53.245947
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:55.662119
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:29:58.078059
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:00.494873
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:02.907771
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:05.321129
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:07.734623
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:10.147774
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:12.560923
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:14.981168
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:17.393682
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:19.812090
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:22.223761
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:24.635409
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:30:27.047457
# Unit test for method run of class LookupModule