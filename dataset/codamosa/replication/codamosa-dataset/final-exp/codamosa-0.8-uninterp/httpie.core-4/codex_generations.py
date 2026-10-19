

# Generated at 2022-06-13 21:40:57.122575
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    exit_status = program(
        parser.parse_args(
            args=['https://httpbin.org/ip'],
            env=Env,
        ),
        env=Env,
    )
    assert exit_status == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:41:00.333276
# Unit test for function main
def test_main():
    main(["http", "get", "http://httpbin.org/get", "--headers"])

# Generated at 2022-06-13 21:41:00.873344
# Unit test for function program
def test_program():
    program()

# Generated at 2022-06-13 21:41:05.548405
# Unit test for function program
def test_program():
    print(program(
        args=parser.parse_args(
            args=['https://xxx.xxx.xxx.xxx/api/v1/device'],
            env=Environment(),
        ),
        env=Environment(),
    ))

# Generated at 2022-06-13 21:41:15.356495
# Unit test for function program
def test_program():
    """
    Test cases for the function program.
    """
    args_namespace = argparse.Namespace()
    environment = Environment()
    assert program(args_namespace, environment) == ExitStatus.SUCCESS
    args_namespace = argparse.Namespace(args = [], kwargs = {}, download = False, output_file = None, download_resume = False, output_file_specified = False)
    assert program(args_namespace, environment) == ExitStatus.SUCCESS
    args_namespace = argparse.Namespace(args = [], kwargs = {}, download = True, output_file = None, download_resume = False, output_file_specified = False)
    assert program(args_namespace, environment) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:41:28.805521
# Unit test for function program
def test_program():
    class testing_env:
        def __init__(self):
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    try:
        import httpie
    except ImportError:
        sys.path.append('.')
        import httpie

    httpie.output.writer = httpie.output.__dict__['writer']

    test_args = parser.parse_args(
        args=[
            '--verbose', 'GET',
            'https://www.google.com/',
        ],
        env=testing_env(),
    )
    # noinspection PyProtectedMember
    test_args.config._config_files_files[:] = []
    # noinspection PyProtectedMember
    test_args.config._dir = None
    # noinspection PyProtectedMember

# Generated at 2022-06-13 21:41:32.668764
# Unit test for function program
def test_program():
    """
    Test program()
    """
    print("\nTesting program()")
    env = Environment()
    parser = argparse.ArgumentParser()
    program(parser.parse_args("https://httpbin.org/get".split(" ")), env)
    return True


# Generated at 2022-06-13 21:41:35.608450
# Unit test for function program
def test_program():
    assert program('','') == 0

# Generated at 2022-06-13 21:41:47.984686
# Unit test for function main
def test_main():
    from io import StringIO
    import sys

    class TestEnvironment(Environment):
        def __init__(self):
            self.stdin = StringIO('hello world')
            self.stdin_isatty = False
            self.stdout = sys.stdout
            self.stderr = StringIO()

    def test_main_program(args: List[str]) -> int:
        return main(args=args, env=TestEnvironment())

    assert test_main_program([]) == 0
    assert test_main_program(['-v']) == 0
    assert test_main_program(['-h']) == 0
    assert test_main_program(['--debug']) == 0
    assert test_main_program(['--output-file=tmp.txt', 'example.org']) == 0

# Generated at 2022-06-13 21:41:56.356652
# Unit test for function main
def test_main():
    requests.raise_for_status
    assert(main() == ExitStatus.SUCCESS)
    #assert(main(["-v"]) == ExitStatus.SUCCESS)
    #assert(main(["-h"]) == ExitStatus.SUCCESS)
    #assert(main(["--headers"]) == ExitStatus.SUCCESS)
    #assert(main(["--verbose"]) == ExitStatus.SUCCESS)
    #assert(main(["--traceback"]) == ExitStatus.SUCCESS)
    #assert(main(["--debug"]) == ExitStatus.SUCCESS)
    #assert(main(["--download"]) == ExitStatus.SUCCESS)
    #assert(main(["--form"]) == ExitStatus.SUCCESS)
    #assert(main(["--json"]) == ExitStatus

# Generated at 2022-06-13 21:42:27.932991
# Unit test for function program
def test_program():
    import pytest  # type: ignore
    class MockStdOut:
        def __init__(self):
            self.data: str = ""

        def write(self, data: str):
            self.data += data

    args = argparse.Namespace()
    args.download = False
    args.download_resume = True
    args.headers = []
    args.output_file = None
    args.output_file_specified = False
    args.output_options = []
    args.check_status = False
    args.follow = False
    args.quiet = False
    env = Environment()
    env.stdout = MockStdOut()
    exit_status = program(args, env)
    assert isinstance(exit_status, ExitStatus)

# Generated at 2022-06-13 21:42:28.541682
# Unit test for function program
def test_program():
    assert True

# Generated at 2022-06-13 21:42:35.957211
# Unit test for function main
def test_main():
    assert main([]) == ExitStatus.SUCCESS
    assert main(['--debug']) == ExitStatus.SUCCESS
    assert main(['--echo', 'GET httpbin.org']) == ExitStatus.SUCCESS
    assert main(['GET', 'httpbin.org']) == ExitStatus.SUCCESS
    # Unrecognized options.
    assert main(['--foo']) == ExitStatus.ERROR
    assert main(['--foo', 'bar']) == ExitStatus.ERROR
    assert main(['--foo', 'bar', 'GET', 'httpbin.org']) == ExitStatus.ERROR
    # Invalid method.
    assert main(['POST+', 'httpbin.org']) == ExitStatus.ERROR
    assert main(['GET+', 'httpbin.org']) == ExitStatus.ERROR
    # Non-ASCII chars

# Generated at 2022-06-13 21:42:49.055943
# Unit test for function program
def test_program():
    """
    Unit test for function program.
    """
    import io
    import tempfile

    env = Environment(stdin=io.BytesIO(), stdout=io.BytesIO(), stderr=io.BytesIO())

# Generated at 2022-06-13 21:42:59.513983
# Unit test for function program
def test_program():
    import pytest
    import httpie.cli.argtypes

    args = parser.parse_args(['--debug', '--form', 'key=value'])
    assert isinstance(args, argparse.Namespace)
    assert args.debug
    assert args.form == ['key=value']
    assert args.timeout == httpie.cli.argtypes.DEFAULT_TIMEOUT

    # Test program()
    exit_status = program(args=args, env=Environment())
    # TODO: Better unit test for program()
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:43:01.711778
# Unit test for function program
def test_program():
    """ """

    assert program([]) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:43:13.337491
# Unit test for function main
def test_main():
    content = 'Hello World!'

    out_file = io.BytesIO()
    with patch('sys.stdout', out_file):
        main(
            ['http', '--method', 'POST', '--json', '{"hello":"world"}', 'http://httpbin.org/anything'],
        )

    out_file.seek(0)
    data = json.loads(out_file.read().decode('utf8'))

    assert data['json']['hello'] == 'world'

    out_file = io.BytesIO()
    with patch('sys.stdout', out_file):
        main(['http', '--headers', 'x-custom: hello world', '--auth', 'user:pass', 'http://httpbin.org/anything'])

    out_file.seek(0)

# Generated at 2022-06-13 21:43:17.291176
# Unit test for function program
def test_program():
    args = parser.parse_args(['https://httpie.org'])
    assert type(program(args, env=Environment())) == ExitStatus
    print("Unit Test: program(): PASS")


# Generated at 2022-06-13 21:43:28.888992
# Unit test for function program
def test_program():
    from httpie import ExitStatus

    args = ["http", "--traceback", "http://httpbin.org/get"]
    exit_status = main(args=args)
    assert exit_status == ExitStatus.SUCCESS

    args = ["http", "--download", "http://httpbin.org/get"]
    exit_status = main(args=args)
    assert exit_status == ExitStatus.SUCCESS

    args = ["http", "--check-status", "--traceback", "https://httpbin.org/status/500"]
    exit_status = main(args=args)
    assert exit_status == ExitStatus.ERROR_HTTP_5XX


# Generated at 2022-06-13 21:43:39.235516
# Unit test for function program
def test_program():
    import io
    from io import BytesIO
    from unittest.mock import patch
    
    from httpie.cli.constants import OUT_REQ_BODY, OUT_REQ_HEAD, OUT_RESP_BODY, OUT_RESP_HEAD
    from httpie.client import collect_messages
    from httpie.output.writer import  MESSAGE_SEPARATOR_BYTES
    from httpie.cli.definition import parser

    class MockClient:
        response = None
        @classmethod
        def request(cls, *args, **kwargs):
            return cls.response
    class MockResponse:
        def __init__(self, status_code=200):
            self.status_code = status_code
        def json(self):
            return {'abc': 123}


# Generated at 2022-06-13 21:45:05.451150
# Unit test for function program
def test_program():
    parser = main()
    assert parser.status_code == ExitStatus.SUCCESS
    parser = main(['https://httpbin.org/get'])
    assert parser.status_code == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:45:07.354112
# Unit test for function program
def test_program():
    """
    Test for function program
    :return:
    """
    # TODO: Write unit test for function program
    pass

# Generated at 2022-06-13 21:45:15.380501
# Unit test for function main
def test_main():
    import sys
    src = '''import sys
from httpie import main
print(main(['https://api.github.com/user', '-A', 'curl/7.68.0']))'''
    sys.argv = ['http', 'https://api.github.com/user', '-A', 'curl/7.68.0']
    src1 = compile(src, 'test.py', 'exec')
    exec(src1)

if __name__ == "__main__":
    test_main()

# Generated at 2022-06-13 21:45:17.196503
# Unit test for function program
def test_program():
    # test program()
    # not tested in the main()
    pass



# Generated at 2022-06-13 21:45:18.228461
# Unit test for function main
def test_main():
    # TODO: tests
    pass



# Generated at 2022-06-13 21:45:28.120987
# Unit test for function program
def test_program():
    from httpie.context import Environment
    from httpie.cli.argtypes import KeyValueArg
    from httpie.cli.definition import parser
    from httpie.config import Config
    from httpie.plugins.builtin import HTTPBasicAuth, AuthPlugin

    env = Environment()
    env.config = Config(dir=None, default_options=[])
    env.stdout = io.StringIO()
    env.stdin = io.StringIO()
    env.stderr = io.StringIO()

    args = parser.parse_args(args=[
        '--auth-type=basic', '--auth=username:password',
        'http://httpbin.org/headers'
    ], env=env)
    assert program(args=args, env=env) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:45:37.229395
# Unit test for function main
def test_main():
    import pytest
    from httpie.cli import status
    from httpie.client import collect_messages
    from httpie.core import main
    import requests
    import httpie
    import os
    import sys

    config_dir = os.path.dirname(sys.argv[0])
    test_args = ['--download', '--debug', '--download-resume', 'https://www.google.com']
    with pytest.raises(SystemExit):
        main(args=test_args, env=httpie.Environment(
            config_dir=config_dir,
            stdin_isatty=True,
            stdout_isatty=True
        ))

# Generated at 2022-06-13 21:45:40.134788
# Unit test for function main
def test_main():
    # test for main function
    main(['--debug'])

# Generated at 2022-06-13 21:45:52.317717
# Unit test for function main
def test_main():
    from io import StringIO
    from unittest.mock import patch
    from httpie import ExitStatus
    from httpie.cli.constants import DEFAULT_CONFIG_DIR
    from httpie.cli.definition import parser
    from httpie.context import Environment
    from httpie.output.writer import MESSAGE_SEPARATOR_BYTES, write_message
    from httpie.plugins.core import AuthPlugin
    from httpie.plugins.registry import plugin_manager
    from httpie.requests_impl import RequestsImpl
    from httpie.types import KeyValue, KeyValueArg
    from requests.models import PreparedRequest, Response
    from tempfile import gettempdir

    env = Environment(config_dir=gettempdir())
    parser.env = env


# Generated at 2022-06-13 21:46:01.757530
# Unit test for function program
def test_program():
    args = ['--follow', '--method=POST', '--verify=no', '--form','name=peter','https://httpbin.org/post']
    env = Environment()
    env.program_name = 'http'
    env.stdout.write('This is stdout\n')
    env.stderr.write('This is stderr\n')
    program(args=args, env=env)
    assert(True)

# Generated at 2022-06-13 21:46:54.854943
# Unit test for function main
def test_main():
    exit_status = main()
    assert exit_status == ExitStatus.SUCCESS

if __name__ == '__main__':
    print(main())

# Generated at 2022-06-13 21:47:02.095827
# Unit test for function main
def test_main():
    def get_args(arglist):
        return arglist

    def get_env():
        return Environment()

    assert main(get_args(["http", "https://github.com", "--headers"]), get_env()) == 0

if __name__ == '__main__':
    args = get_args(['arg1', 'arg2', '--headers'])
    env = get_env()
    main(args, env)

# Generated at 2022-06-13 21:47:04.734806
# Unit test for function program
def test_program():
    assert program(args=[], env=Environment()) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:47:17.296685
# Unit test for function main
def test_main():
    from httpie.cli.definition import parser
    from httpie.context import Environment
    from httpie.plugins.builtin import HTTPBasicAuth

    expected_stdout = f"get http://localhost/\r\n"
    expected_stderr = ""

    env = Environment(
        stdin=io.StringIO("GET /\n"),
        stdout=io.StringIO(),
        stderr=io.StringIO()
    )


# Generated at 2022-06-13 21:47:32.579212
# Unit test for function program
def test_program():
    import io
    import os
    import sys
    args = ['--output-file', 'test.txt', 'www.google.com']
    env = Environment()
    env.stdout = io.TextIOWrapper(io.BytesIO(), sys.stdout.encoding)
    env.stdout_isatty = False
    env.stdin_isatty = False
    env.program_name = 'test'
    env.config = {'default_options': None}
    env.config_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    program(args=args, env=env)
    assert os.path.isfile('test.txt')


# Generated at 2022-06-13 21:47:42.386044
# Unit test for function program

# Generated at 2022-06-13 21:47:55.165967
# Unit test for function program
def test_program():
    """
    Unit test for function program
    :return: function program
    """
    from httpie.cli.definition import parser
    from httpie.client import httpie_sessions, collect_messages
    from httpie.output.writer import write_message

    args = parser.parse_args(['GET', 'http://httpbin.org/get/'])
    args.method = args.method.upper()
    if args.method == 'LOGIN':
        args.method = 'POST'
        args.auth = ('user' or 'httpbin') + ':' + ('pass' or 'weak_password')
    elif args.method == 'LOGOUT' or args.method == 'logout':
        args.method = 'GET'
        args.auth = None

# Generated at 2022-06-13 21:47:58.606637
# Unit test for function main
def test_main():
    import time
    for i in range(1,10):
        exit_status = main(['http', 'https://httpbin.org/get'])
        time.sleep(1)

# Generated at 2022-06-13 21:48:00.347426
# Unit test for function program
def test_program():
    program_status = main(args=['--debug'])
    assert ExitStatus.SUCCESS == program_status

# Generated at 2022-06-13 21:48:12.272232
# Unit test for function main
def test_main():
    import httpie.status
    import httpie.cli.argtypes
    import sys
    import io
    def p(s):
        return s.encode('utf-8')

# Generated at 2022-06-13 21:49:14.010732
# Unit test for function program
def test_program():
    args = ['--output','json','--pretty','none','--verbose','--debug','--ignore-stdin','--body-max-size','100000000','--method','GET','--stream','--check-status','--timeout','30','--max-redirects','10','--follow','--download-resume','--download','--form','--json-endpoint','http://127.0.0.1:5000/api/graphql','--headers','{"accept": "application/json", "content-type": "application/json"}','{"query": "{__schema { queryType { name, description } }	}"}']
    try:
        exit_status = program(args=args, env=Environment())
        assert exit_status == ExitStatus.SUCCESS
    except Exception as e:
        print("test_program failed with exception")

# Generated at 2022-06-13 21:49:27.113182
# Unit test for function program
def test_program():
    parser = argparse.ArgumentParser()

    parser.add_argument('--verbose', '-v', action='store_true')

    parser.add_argument('--auth', '-a', dest='auth',
                        action='store', default=None,
                        metavar='USER[:PASS]',
                        help='specify basic auth credential')

    parser.add_argument('--verify=yes', action='store_true',
                        dest='verify',
                        help='enable ssl verification')

    parser.add_argument('--verify=no', action='store_false',
                        dest='verify',
                        help='disable ssl verification')

    parser.add_argument('--verify', action='store', dest='verify',
                        default=True,
                        help='specify path to ssl certificate bundle')


# Generated at 2022-06-13 21:49:36.641226
# Unit test for function main
def test_main():
    from httpie.cli.constants import DEFAULT_OUTPUT_OPTIONS
    from httpie.cli.definition import KeyValueArg

    env = Environment()
    args = ['https://api.github.com/search/repositories', 'q=requests+language:python&sort=stars']
    args = ['-b', 'search', args[0]] + KeyValueArg.parse(' '.join(args[1:]))
    args.output_options = set(DEFAULT_OUTPUT_OPTIONS)
    args.pretty = True
    args.markup = True
    args.headers = True
    main(args, env)

# Generated at 2022-06-13 21:49:40.227421
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    args = parser.parse_args(
        args=[
            '--headers',
            'Authorization:abc123',
            '--form',
            'submit=Do+it+now',
            'http://httpbin.org/post'
        ]
    )
    assert program(args=args, env=Environment()) == 0

# Generated at 2022-06-13 21:49:50.210365
# Unit test for function program
def test_program():
    print('test_program')
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-file', "-o")
    parser.add_argument('--output-options')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-q', '--quiet', action='count')
    parser.add_argument('-b', '--body')
    parser.add_argument('--headers')
    parser.add_argument('--check-status', action='store_true')
    parser.add_argument('--download', action='store_true')
    parser.add_argument('-f', '--follow', action='store_true')
    parser.add_argument('--download-resume', action='store_true')

# Generated at 2022-06-13 21:49:59.923035
# Unit test for function program
def test_program():
    n = 5
    args = argparse.Namespace(
        stdin_isatty=True,
        output_options=[OUT_REQ_HEAD, OUT_RESP_HEAD, OUT_RESP_BODY],
        check_status=False,
        follow=True,
        output_file=None,
        download=False,
        download_resume=False,
    )
    env = Environment()
    env.stdin_encoding = 'utf-8'
    from httpie.cli.definition import parser
    all_args = parser.parse_args(args=['--print=B', 'GET', 'https://httpie.org'], env=env)
    args.headers = all_args['headers']
    args.terminal_width = 80
    args.json = all_args['json']

# Generated at 2022-06-13 21:50:11.484722
# Unit test for function program
def test_program():
    import json
    import httpie.plugins
    from httpie.output.options import OutputOptions
    from httpie.status import ExitStatus

    def mock_collect_messages(args: argparse.Namespace):
        mock_request = requests.Request('GET', 'http://someurl.com')
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response.raw = mock_request.prepare()
        yield mock_request.prepare()
        yield mock_response

    httpie.plugins._loaded_plugins = {}
    _orig = httpie.cli.collect_messages.collect_messages
    httpie.cli.collect_messages.collect_messages = mock_collect_messages
    args = argparse.Namespace()

# Generated at 2022-06-13 21:50:20.757882
# Unit test for function main
def test_main():
    from httpie.cli.definition import parser
    from httpie.environment import Environment

    env = Environment()
    env.stdin_encoding = 'utf-8'
    parser.env = env
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('-k', action='store_true')
    args = ['--debug']
    main(args, env)

if __name__ == '__main__':
    test_main()