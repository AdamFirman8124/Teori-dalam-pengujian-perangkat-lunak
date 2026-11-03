

# Generated at 2026-11-02 16:48:53.651995
# Unit test for constructor of class LookupModule
def test_LookupModule():
    from ansible.plugins.lookup.url import LookupModule

    lookup_plugin = LookupModule()
    assert lookup_plugin is not None
    assert isinstance(lookup_plugin, LookupModule)
    # Verify it is a lookup plugin
    assert hasattr(lookup_plugin, 'run')
    assert callable(lookup_plugin.run)

# Generated at 2026-11-02 16:52:15.410469
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch

    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError
    from ansible.plugins.lookup.url import LookupModule


# Generated at 2026-11-02 16:53:38.503484
# Unit test for constructor of class LookupModule
def test_LookupModule():
    from ansible.plugins.lookup import LookupBase
    from ansible.plugins.lookup.url import LookupModule as UrlLookupModule

    # Construct with default arguments
    lookup = LookupModule()

    # Verify instance types
    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert isinstance(lookup, UrlLookupModule)

    # Construct with explicit arguments
    lookup2 = LookupModule(loader=None, templar=None, variable_manager=None)
    assert isinstance(lookup2, LookupModule)

    # Verify inherited methods exist
    assert callable(lookup.run)
    assert callable(lookup.get_option)
    assert callable(lookup.set_options)

# Generated at 2026-11-02 16:56:22.641599
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    from unittest.mock import patch, MagicMock
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    class TestLookupModuleRun(unittest.TestCase):

        def _make_lookup(self, options=None):
            from ansible.plugins.lookup.url import LookupModule
            lookup = LookupModule()
            opts = {
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
                'split_lines': True,
            }
            if options:
                opts.update(options)

            def get_option(key, *args, **kwargs):
                return opts[key]

            lookup.get_option = get_option
            lookup.set_options = MagicMock()
            return lookup

        @patch('ansible.plugins.lookup.url.Display')
        @patch('ansible.plugins.lookup.url.open_url')
        def test_run_split_lines_default(self, mock_open_url, mock_display_cls):
            mock_display_cls.side_effect = lambda *a, **kw: MagicMock()
            response = MagicMock()
            response.read.return_value = b'line1\nline2\nline3\n'
            mock_open_url.return_value = response

            lookup = self._make_lookup()
            result = lookup.run(['http://example.com/file.txt'])

            self.assertEqual(result, ['line1', 'line2', 'line3'])
            mock_open_url.assert_called_once()
            args, kwargs = mock_open_url.call_args
            self.assertEqual(args[0], 'http://example.com/file.txt')
            self.assertTrue(kwargs['validate_certs'])
            self.assertEqual(kwargs['timeout'], 10)
            self.assertEqual(kwargs['http_agent'], 'ansible-httpget')

        @patch('ansible.plugins.lookup.url.Display')
        @patch('ansible.plugins.lookup.url.open_url')
        def test_run_no_split_lines(self, mock_open_url, mock_display_cls):
            mock_display_cls.side_effect = lambda *a, **kw: MagicMock()
            response = MagicMock()
            response.read.return_value = b'one blob of text'
            mock_open_url.return_value = response

            lookup = self._make_lookup({'split_lines': False})
            result = lookup.run(['http://example.com/file.txt'])

            self.assertEqual(result, ['one blob of text'])

        @patch('ansible.plugins.lookup.url.Display')
        @patch('ansible.plugins.lookup.url.open_url')
        def test_run_multiple_terms(self, mock_open_url, mock_display_cls):
            mock_display_cls.side_effect = lambda *a, **kw: MagicMock()

            def side_effect(term, **kwargs):
                resp = MagicMock()
                resp.read.return_value = ('content for %s' % term).encode('utf-8')
                return resp

            mock_open_url.side_effect = side_effect

            lookup = self._make_lookup({'split_lines': False})
            result = lookup.run(['http://a.com', 'http://b.com'])

            self.assertEqual(result, ['content for http://a.com', 'content for http://b.com'])
            self.assertEqual(mock_open_url.call_count, 2)

        @patch('ansible.plugins.lookup.url.Display')
        @patch('ansible.plugins.lookup.url.open_url')
        def test_run_passes_all_options(self, mock_open_url, mock_display_cls):
            mock_display_cls.side_effect = lambda *a, **kw: MagicMock()
            response = MagicMock()
            response.read.return_value = b'ok'
            mock_open_url.return_value = response

            opts = {
                'validate_certs': False,
                'use_proxy': False,
                'username': 'bob',
                'password': 'hunter2',
                'headers': {'header1': 'value1'},
                'force': True,
                'timeout': 5.0,
                'http_agent': 'custom-agent',
                'force_basic_auth': True,
                'follow_redirects': 'all',
                'use_gssapi': True,
                'unix_socket': '/tmp/socket',
                'ca_path': '/tmp/ca.pem',
                'unredirected_headers': ['Authorization'],
                'split_lines': False,
            }

            lookup = self._make_lookup(opts)
            result = lookup.run(['https://some.private.site.com/file.txt'])

            self.assertEqual(result, ['ok'])
            args, kwargs = mock_open_url.call_args
            self.assertEqual(args[0], 'https://some.private.site.com/file.txt')
            self.assertFalse(kwargs['validate_certs'])
            self.assertFalse(kwargs['use_proxy'])
            self.assertEqual(kwargs['url_username'], 'bob')
            self.assertEqual(kwargs['url_password'], 'hunter2')
            self.assertEqual(kwargs['headers'], {'header1': 'value1'})
            self.assertTrue(kwargs['force'])
            self.assertEqual(kwargs['timeout'], 5.0)
            self.assertEqual(kwargs['http_agent'], 'custom-agent')
            self.assertTrue(kwargs['force_basic_auth'])
            self.assertEqual(kwargs['follow_redirects'], 'all')
            self.assertTrue(kwargs['use_gssapi'])
            self.assertEqual(kwargs['unix_socket'], '/tmp/socket')
            self.assertEqual(kwargs['ca_path'], '/tmp/ca.pem')
            self.assertEqual(kwargs['unredirected_headers'], ['Authorization'])

        @patch('ansible.plugins.lookup.url.Display')
        @patch('ansible.plugins.lookup.url.open_url')
        def test_run_http_error(self, mock_open_url, mock_display_cls):
            mock_display_cls.side_effect = lambda *a, **kw: MagicMock()
            mock_open_url.side_effect = HTTPError('http://example.com', 404, 'Not Found', None, None)

            lookup = self._make_lookup()
            with self.assertRaises(AnsibleError) as ctx:
                lookup.run(['http://example.com'])
            self.assertIn('Received HTTP error for http://example.com', str(ctx.exception))

        @patch('ansible.plugins.lookup.url.Display')
        @patch('ansible.plugins.lookup.url.open_url')
        def test_run_url_error(self, mock_open_url, mock_display_cls):
            mock_display_cls.side_effect = lambda *a, **kw: MagicMock()
            mock_open_url.side_effect = URLError('name resolution failure')

            lookup = self._make_lookup()
            with self.assertRaises(AnsibleError) as ctx:
                lookup.run(['http://nonexistent.invalid'])
            self.assertIn('Failed lookup url for http://nonexistent.invalid', str(ctx.exception))

        @patch('ansible.plugins.lookup.url.Display')
        @patch('ansible.plugins.lookup.url.open_url')
        def test_run_ssl_validation_error(self, mock_open_url, mock_display_cls):
            mock_display_cls.side_effect = lambda *a, **kw: MagicMock()
            mock_open_url.side_effect = SSLValidationError('bad certificate')

            lookup = self._make_lookup()
            with self.assertRaises(AnsibleError) as ctx:
                lookup.run(['https://example.com'])
            self.assertIn("Error validating the server's certificate for https://example.com", str(ctx.exception))

        @patch('ansible.plugins.lookup.url.Display')
        @patch('ansible.plugins.lookup.url.open_url')
        def test_run_connection_error(self, mock_open_url, mock_display_cls):
            mock_display_cls.side_effect = lambda *a, **kw: MagicMock()
            mock_open_url.side_effect = ConnectionError('connection refused')

            lookup = self._make_lookup()
            with self.assertRaises(AnsibleError) as ctx:
                lookup.run(['http://example.com'])
            self.assertIn('Error connecting to http://example.com', str(ctx.exception))

        @patch('ansible.plugins.lookup.url.Display')
        @patch('ansible.plugins.lookup.url.open_url')
        def test_run_empty_terms(self, mock_open_url, mock_display_cls):
            mock_display_cls.side_effect = lambda *a, **kw: MagicMock()
            lookup = self._make_lookup()
            result = lookup.run([])
            self.assertEqual(result, [])
            mock_open_url.assert_not_called()

        @patch('ansible.plugins.lookup.url.Display')
        @patch('ansible.plugins.lookup.url.open_url')
        def test_run_decodes_utf8(self, mock_open_url, mock_display_cls):
            mock_display_cls.side_effect = lambda *a, **kw: MagicMock()
            response = MagicMock()
            response.read.return_value = u'héllo wörld'.encode('utf-8')
            mock_open_url.return_value = response

            lookup = self._make_lookup()
            result = lookup.run(['http://example.com/unicode.txt'])
            self.assertEqual(result, [u'héllo wörld'])

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for name in dir(TestLookupModuleRun):
        if name.startswith('test_'):
            suite.addTest(TestLookupModuleRun(name))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        raise AssertionError('test_LookupModule_run failed: %s' % result)