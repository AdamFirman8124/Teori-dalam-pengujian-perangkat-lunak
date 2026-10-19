

# Generated at 2022-06-13 12:23:27.120975
# Unit test for function split_url
def test_split_url():
    """Test split_url function."""
    assert split_url('https://www.example.com', 'scheme') == 'https'
    assert split_url('https://www.example.com', 'netloc') == 'www.example.com'
    assert split_url('https://www.example.com', 'path') == ''
    assert split_url('https://www.example.com/test/test.jpeg', 'path') == '/test/test.jpeg'
    assert split_url('https://www.example.com/test/test.jpeg', 'query') == ''
    assert split_url('https://www.example.com/test/test.jpeg?q=test', 'query') == 'q=test'


# Generated at 2022-06-13 12:23:31.898948
# Unit test for function split_url
def test_split_url():
    assert split_url("https://www.example.com/foo/bar?a=b&c=d") == {'scheme': 'https', 'netloc': 'www.example.com', 'path': '/foo/bar', 'query': 'a=b&c=d', 'fragment': ''}


# Generated at 2022-06-13 12:23:42.693137
# Unit test for function split_url
def test_split_url():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import json
    import textwrap
    from ansible.compat.tests import unittest

    class TestSplitUrl(unittest.TestCase):
        def test_url_without_query(self):
            url = 'https://www.example.com/path?arg=value#frag'
            expected = {
                'scheme': 'https',
                'netloc': 'www.example.com',
                'path': '/path',
                'query': 'arg=value',
                'fragment': 'frag',
                'hostname': 'www.example.com',
                'port': None
            }
            self.assertDictEqual(expected, split_url(url))


# Generated at 2022-06-13 12:23:52.379453
# Unit test for function split_url
def test_split_url():

    from ansible.module_utils._text import to_text

    # Test with a full URL
    url = 'http://www.example.com:8080/path/to/something?query1=test&query2=test#fragment'
    split_result = {
        'scheme' : 'http',
        'netloc' : 'www.example.com:8080',
        'path'   : '/path/to/something',
        'query'  : 'query1=test&query2=test',
        'fragment' : 'fragment',
    }

    # Test the full dictionary return with no query
    assert split_url(url) == split_result

    # Test each component individually, making sure it matches

# Generated at 2022-06-13 12:23:59.447381
# Unit test for function split_url
def test_split_url():

    from ansible.compat.tests.mock import patch

    with patch.object(helpers, 'object_to_dict') as mock_dict:
        mock_dict.return_value = {'scheme': 'http',
                                  'netloc': 'www.example.com',
                                  'path': '/index.html',
                                  'params': '',
                                  'query': 'a=1&b=2',
                                  'fragment': ''}

        assert split_url(None) == mock_dict.return_value


# Generated at 2022-06-13 12:24:09.256405
# Unit test for function split_url

# Generated at 2022-06-13 12:24:19.934694
# Unit test for function split_url
def test_split_url():
    def test_query(query):
        test_url = 'https://myuser:mypassword@www.example.com:80/foo/bar;param?a=1&b=2#anchor'
        return split_url(test_url, query)
    assert test_query('scheme') == 'https'
    assert test_query('netloc') == 'myuser:mypassword@www.example.com:80'
    assert test_query('path') == '/foo/bar;param'
    assert test_query('query') == 'a=1&b=2'
    assert test_query('fragment') == 'anchor'
    assert test_query('username') == 'myuser'
    assert test_query('password') == 'mypassword'
    assert test_query('hostname') == 'www.example.com'

# Generated at 2022-06-13 12:24:28.546385
# Unit test for function split_url
def test_split_url():
    url = 'https://user:pass@ansible.com:8080/docs/Configuring_Remote_Hosts/Configuring_Remote_Hosts.html?option=1&option=2#fragment'
    results = split_url(value=url)

    assert results['scheme'] == 'https'
    assert results['netloc'] == 'user:pass@ansible.com:8080'
    assert results['path'] == '/docs/Configuring_Remote_Hosts/Configuring_Remote_Hosts.html'
    assert results['params'] == ''
    assert results['query'] == 'option=1&option=2'
    assert results['fragment'] == 'fragment'

    # Test with a query supplied
    assert split_url(url, 'scheme') == 'https'

# Generated at 2022-06-13 12:24:38.532293
# Unit test for function split_url
def test_split_url():

    test_url1 = "http://ansible.com/foo/bar?query=yes"
    ansible_url = split_url(test_url1)
    assert ansible_url['scheme'] == 'http'
    assert ansible_url['netloc'] == 'ansible.com'
    assert ansible_url['path'] == '/foo/bar'
    assert ansible_url['query'] == 'query=yes'
    assert ansible_url['fragment'] == ''

    assert split_url(test_url1, 'scheme') == 'http'
    assert split_url(test_url1, 'netloc') == 'ansible.com'
    assert split_url(test_url1, 'path') == '/foo/bar'

# Generated at 2022-06-13 12:24:45.663730
# Unit test for function split_url
def test_split_url():
    fixtures = [
        'scheme://netloc/path;parameters?query=argument#fragment',
        'scheme://user:pass@netloc/path;parameters?query=argument#fragment',
        'scheme://user:pass@host:80/path;parameters?query=argument#fragment',
    ]