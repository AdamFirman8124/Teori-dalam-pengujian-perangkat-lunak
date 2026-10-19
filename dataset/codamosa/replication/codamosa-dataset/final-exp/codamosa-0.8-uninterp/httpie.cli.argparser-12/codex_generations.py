

# Generated at 2022-06-13 21:05:00.887111
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # HTTPieArgumentParser.parse_args(args=None, namespace=None)
    pass


# Generated at 2022-06-13 21:05:12.940855
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    arg_strings = [
        '--ignore-stdin', '--method', 'GET', '--auth-type', 'bearer',
        'https://localhost:8080/path/to/resource',
        'X-Foo:bar'
    ]

    args = HTTPieArgumentParser().parse_args(arg_strings)

    assert args.ignore_stdin
    assert args.method == 'GET'
    assert args.auth_type == 'bearer'
    assert args.url == 'https://localhost:8080/path/to/resource'
    assert args.request_items == [
        KeyValueArgType('X-Foo', 'bar')
    ]
    assert args.auth_plugin
    assert args.proxy_urls == []
    assert args.no_proxy_urls == []

# Generated at 2022-06-13 21:05:16.521227
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    def _test_HTTPieArgumentParser_parse_args(self):
        """
        Test method parse_args of class HTTPieArgumentParser
        """
        httpie_argument_parser = HTTPieArgumentParser()
        httpie_argument_parser.parse_args([])
        return True


# Generated at 2022-06-13 21:05:19.178930
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass
    # result = HTTPieArgumentParser.parse_args(self, args, namespace)
    # assert result ==



# Generated at 2022-06-13 21:05:32.399899
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """ Tests for method parse_args of class HTTPieArgumentParser """

    def test_HTTPieArgumentParser_parse_args_1():
        from requests import Session
        from httpie.plugins.builtin import HTTPBasicAuth
        assert isinstance(HTTPieArgumentParser.parse_args(['--auth', 'user:pass', '--auth-type', 'basic']).auth_plugin, HTTPBasicAuth)
        assert isinstance(HTTPieArgumentParser.parse_args(['--auth', 'user:pass']).auth_plugin, HTTPBasicAuth)
        assert isinstance(HTTPieArgumentParser.parse_args([]).auth_plugin, None)


# Generated at 2022-06-13 21:05:42.626961
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    
    args = []
    env = TestEnvironment()


    r = HTTPieArgumentParser.parse_args(args, env)
    assert r.method == 'GET'
    assert r.url == 'http://localhost'
    assert r.headers == [':authority', 'localhost']
    assert r.data == []
    assert r.files == []
    assert r.params == []
    assert r.output_file is None
    assert r.stdin_isatty is True
    assert r.output_file_specified is False
    assert r.verbose == False
    assert r.offline == False
    assert r.all is False
    assert r.stream == False
    assert r.check_status == False
    assert r.download == False
    assert r.download_resume == False
    assert r.download_as

# Generated at 2022-06-13 21:05:45.093387
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    obj = HTTPieArgumentParser()
    args = obj.parse_args()
sys.argv = ['']
HTTPieArgumentParser().parse_args()

# nosetests tests.unit.parsing.test_parser:HTTPieArgumentParserTest

# Generated at 2022-06-13 21:05:47.485294
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # just run the method to see if it throws an exception or not
    parser = HTTPieArgumentParser()
    parser.parse_args([])
# testing class HTTPDigestAuth

# Generated at 2022-06-13 21:05:57.283215
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """Test for methods parse_args of HTTPieArgumentParser"""
    # Unit test for method parse_args of class HTTPieArgumentParser

    # Testing function parse_args of HTTPieArgumentParser class
    # In the case of missing arguments

# Generated at 2022-06-13 21:06:12.308793
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """The parser unit test.

    Tests both standard and custom parser.

    """

    class MockPlugin(BasePlugin):
        """
        Plugin that mixes in custom arguments.

        """
        name = 'Mock'
        description = ''
        auth_plugin = True

        def get_parser(self):
            parser = argparse.ArgumentParser(add_help=False)
            # argparse treats all options as strings, so we need to convert
            # back to bool manually
            # noinspection PyUnresolvedReferences
            parser.add_argument('--auth-type', action='store_true')
            # noinspection PyUnresolvedReferences
            parser.add_argument('--auth-plugin-allow-netrc', action='store_true')
            # noinspection PyUnresolvedReferences

# Generated at 2022-06-13 21:06:55.254945
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    hac = HTTPieArgumentParser()
    print(hac.parse_args(args=['-e','http://httpbin.org/headers', 'Accept:text/html']))


# Generated at 2022-06-13 21:07:01.717118
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    inp = ['-h']
    assert HTTPieArgumentParser().parse_args(inp).help
    inp = ['-v']
    assert HTTPieArgumentParser().parse_args(inp).version
    inp = ['--version']
    assert HTTPieArgumentParser().parse_args(inp).version
    inp = ['--json']
    assert HTTPieArgumentParser().parse_args(inp).json
    inp = ['--form']
    assert HTTPieArgumentParser().parse_args(inp).form
    inp = ['--pretty=all']
    assert HTTPieArgumentParser().parse_args(inp).prettify == PRETTY_MAP['all']
    inp = ['--style=parakeet']

# Generated at 2022-06-13 21:07:06.029482
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    instance = HTTPieArgumentParser()
    assert isinstance(instance, HTTPieArgumentParser)

    assert isinstance(instance.args, Namespace)
    assert isinstance(instance.args.headers, CaseInsensitiveDict)
    assert isinstance(instance.args.prettify, bool)
    assert isinstance(instance.args.output_options, str)
    assert isinstance(instance.args.output_options_history, str)
    assert isinstance(instance.args.downlaod, bool)
    assert isinstance(instance.args.download_resume, bool)
    assert isinstance(instance.args.url, str)
    assert isinstance(instance.args.data, bytes)
    assert isinstance(instance.args.files, dict)
    assert isinstance(instance.args.form, bool)

# Generated at 2022-06-13 21:07:17.618969
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()

# Generated at 2022-06-13 21:07:27.643702
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser_instance = HTTPieArgumentParser(add_help=False, env=Environment(),)
    args = parser_instance.parse_args("")

    assert args.data is None
    assert args.download is False
    assert args.headers is None
    assert args.output_file is None
    assert args.output_file_specified is False
    assert args.output_options is None
    assert args.output_options_history is None
    assert args.params is None
    assert args.traceback is False
    assert args.verbose is False

    assert args.auth is None
    assert args.auth_plugin is None
    assert args.auth_type is None
    assert args.body is None
    assert args.body_columns is None
    assert args.body_disable_colors is False
    assert args.body_html is False

# Generated at 2022-06-13 21:07:35.222455
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """Tests the parsing of command line arguments."""

    httpie_cli = HTTPieArgumentParser()
    httpie_cli.parse_args([
        "http"
    ])
    httpie_cli.parse_args([
        "http",
        "httpbin.org"
    ])
    httpie_cli.parse_args([
        "http",
        "httpbin.org",
        "GET"
    ])
    httpie_cli.parse_args([
        "http",
        "httpbin.org",
        "GET",
        "name==Ada"
    ])
    httpie_cli.parse_args([
        "http",
        "httpbin.org",
        "GET",
        "name==Ada",
        "accept:text/html"
    ])

# Generated at 2022-06-13 21:07:39.948809
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    ap = HTTPieArgumentParser()
    # Add some arguments
    ap.add_argument(
        "-a", "--auth",
        type=parse_auth,
        dest=FORMAT_KEY_VALUES,
        metavar="{USERNAME:PASSWORD}",
        help="Basic HTTP auth credentials.",
    )
    ap.add_argument(
        "-b", "--body", "--data", "--data-raw",
        type=KeyValueArgType(*SEPARATOR_GROUP_ALL_ITEMS),
        dest=FORMAT_KEY_VALUES,
        metavar="<data>",
        help="HTTP request body data.",
    )

# Generated at 2022-06-13 21:07:44.036823
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = parser.parse_args(['GET', 'http://httpbin.org/'])
    assert args.method == 'GET'
    assert args.url == 'http://httpbin.org/'

# Generated at 2022-06-13 21:07:49.050968
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.parse_args(['--verbose', '--headers', 'one: 1', '--headers', 'two: 2'])
    assert parser.args.headers == CaseInsensitiveDict({'one': '1', 'two': '2'})


# Generated at 2022-06-13 21:07:54.613830
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args_as_str = '-A httpbin.org --auth-type keyword --auth test:test'
    args = HTTPieArgumentParser().parse_args(args_as_str.split())
    assert args['headers']['User-Agent'] == 'httpbin.org'
    assert args['auth'][0] == 'test:test'
    assert args['auth-type'] == 'keyword'

# Generated at 2022-06-13 21:09:13.308277
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()

# Generated at 2022-06-13 21:09:21.994955
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    with patch.object(HTTPieArgumentParser, 'error') as MockClass:
        with patch.object(HTTPieArgumentParser, '_process_format_options') as MockClass1:
            MockClass1.return_value = ['format']
            x = HTTPieArgumentParser()
            x.parse_args([])
            MockClass1.assert_called_with()
            x.parse_args(['--default'] + ['option=value', '--format=format'])
            MockClass1.assert_called_with()
            x.env = Mock()
            x.env.config = Mock()
            x.env.config.default_options = {'format':'format'}
            x.parse_args(['option=value'])

# Generated at 2022-06-13 21:09:26.591854
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    env = Environment({})
    httpie_parser = HTTPieArgumentParser(env=env)
    options = httpie_parser.parse_args(['https://httpbin.org/get'])
    assert options.url == 'https://httpbin.org/get'
    

# Generated at 2022-06-13 21:09:29.712728
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # the objective of this test is to ensure that the method define_parser of
    # class HTTPieArgumentParser is working properly
    parser = HTTPieArgumentParser()
    parser.parse_args(['http', 'httpbin.org'])
    
    

# Generated at 2022-06-13 21:09:40.754713
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # ARRANGE #
    args = [
        'http',
        'https://httpbin.org',
        'X-API-Token:42',
        'id==1',
        'status:=invalid'
    ]
    ap = HTTPieArgumentParser(prog='http', add_help=False)
    ap.add_argument('x', nargs='*')
    ap.add_argument('--ignore-stdin', dest='ignore_stdin',
                    action='store_true', default=False)
    ap.add_argument('--quiet', dest='quiet', action='store_true')
    ap.add_argument('--download-output', dest='output_file', type=argparse.FileType())
    ap.add_argument('--output', dest='output_file_specified')
    ap.add_argument

# Generated at 2022-06-13 21:09:49.190291
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser().parse_args(['http://example.com'])
    assert args.url == 'http://example.com'
    assert args.scheme == 'http'
    assert args.host == 'example.com'
    assert args.auth == None
    assert args.verify == True
    assert args.cert == None
    assert args.headers == OrderedDict()
    assert args.data == None
    assert args.params == OrderedDict()
    assert args.files == OrderedDict()


# Generated at 2022-06-13 21:09:53.296625
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass
    # run the code and check for exception
    #with pytest.raises(Exception):
    #    self.HTTPieArgumentParser.parse_args(args=None, namespace=None)



# Generated at 2022-06-13 21:10:05.415949
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from json import loads

    class _MockEnv(object):
        # noinspection PyAttributeOutsideInit
        def __init__(self):
            self.stdin = self.stdin_encoding = self.stdout_encoding = \
                self.stdout = self.stderr = self.is_windows = \
                self.stdout_isatty = self.stderr_isatty = None
            self.devnull = None

        def __call__(self):
            return self
    _env = _MockEnv()
    httpie_args = HTTPieArgumentParser(_env)
    parser_args = httpie_args.parse_args(['-d', 'a=some_data', 'url'])
    assert parser_args.debug is False

# Generated at 2022-06-13 21:10:13.114708
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.core import main

    httpie = main.HTTPie()
    httpie.argparser = httpie.create_argparser()
    httpie.args = httpie.argparser.parse_args([])
    httpie.apply_config()
    assert httpie.args.output_options_history == OUTPUT_OPTIONS_DEFAULT_OFFLINE

# Generated at 2022-06-13 21:10:15.769310
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    output = parser.parse_args(['GET', 'http://example.com/'])
    assert output

# Generated at 2022-06-13 21:13:03.808340
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie_argument_parser = HTTPieArgumentParser()
    args = httpie_argument_parser.parse_args(['https://www.google.com'])
    assert is_valid_url(args.url) == True
    args = httpie_argument_parser.parse_args(['www.google.com'])
    assert is_valid_url(args.url) == False

# Test cases for the main function

# Generated at 2022-06-13 21:13:09.835546
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ['--user', 'test', 'http://httpbin.org/get']
    parser = HTTPieArgumentParser()
    args = parser.parse_args(args)
    assert args.auth == AuthCredentials('test', None, SEPARATOR_CREDENTIALS, 'test')
    assert args.auth_type == 'Basic'
    assert args.url == 'http://httpbin.org/get'
    assert args.method == 'GET'


# Generated at 2022-06-13 21:13:26.322677
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    subparser_name = 'test_HTTPieArgumentParser_parse_args'
    parser = HTTPieArgumentParser(
        prog='http',
        epilog=None,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=False,
    )
    parser.add_argument(
        '--baz',
        action=GroupedAction,
        dest='grouped_actions',
        default=[],
        nargs='+',
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        '--foo',
        action=GroupedAction,
        dest='grouped_actions',
        default=[],
        nargs='+',
        help=argparse.SUPPRESS,
    )

# Generated at 2022-06-13 21:13:37.934606
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    no_args = ['http']
    # noinspection PyTypeChecker
    with pytest.raises(SystemExit):
        HTTPieArgumentParser().parse_args(no_args)
 
    single_arg = ['http', 'httpbin.org']
    args = HTTPieArgumentParser().parse_args(single_arg)
    assert args.url == 'httpbin.org'
    
    mutliple_args = ['http', 'httpbin.org', 
                     'Accept:application/json', 'User-Agent:curl/7.29.0']
    args = HTTPieArgumentParser().parse_args(mutliple_args)
    assert args.url == 'httpbin.org'

# Generated at 2022-06-13 21:13:49.470394
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from datetime import datetime
    from pathlib import Path
    from typing import Any
    from typing import Dict
    from typing import List
    from typing import Optional
    from typing import Sequence
    from typing import Union
    from urllib.parse import unquote
    import io
    import os
    import pdb
    import signal
    import sys
    import tempfile
    import traceback
    import urllib.request
    import platform
    import random
    import requests
    import signal
    import subprocess
    import tempfile
    import time
    import traceback
    import uuid
    import webbrowser
    import warnings
    import zipfile
    import idna
    import chardet
    import certifi
    import atomicwrites
    import attr
    import certifi
    import idna
    import requests

# Generated at 2022-06-13 21:13:55.974939
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
  hp = HTTPieArgumentParser(prog=APP_NAME)
  args = hp.parse_args(['get', 'http://localhost:5000/'])
  assert args.url == 'http://localhost:5000/'
  assert args.method == 'GET'
  print('test_HTTPieArgumentParser_parse_args passed')
test_HTTPieArgumentParser_parse_args()


# Generated at 2022-06-13 21:14:09.795842
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    sys.argv = [sys.argv[0],
                '-b',
                '--ignore-stdin',
                '--traceback',
                '--verbose',
                '--output-file',
                'cookies.txt',
                'http://example.com/',
                'a=1',
                'a==2',
                'b==]',
                'c=3']
    parser = HTTPieArgumentParser()
    pytest.raises(SystemExit, parser.parse_args)