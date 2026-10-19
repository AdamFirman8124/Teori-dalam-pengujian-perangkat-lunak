

# Generated at 2022-06-13 21:41:01.147299
# Unit test for function main
def test_main():
    assert main(["-h"]) == ExitStatus.SUCCESS
    assert main(["-v"]) == ExitStatus.SUCCESS
    assert main(["--color=never", "http://api.maif.fr/api/cert/1.0/liste-certificats/"]) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:41:08.732671
# Unit test for function program
def test_program():
    in_argv = [
        '../../http',
        '--download',
        'https://www.yazilimperver.com/wp-content/uploads/2019/07/python-tutorial.jpg',
        '-o',
        'python-tutorial.jpg'
    ]

    exit_status = main(in_argv)
    assert(exit_status == ExitStatus.SUCCESS)

# Generated at 2022-06-13 21:41:09.797493
# Unit test for function program
def test_program():
    pass

# Generated at 2022-06-13 21:41:22.697878
# Unit test for function program
def test_program():
    class Object(object):
        pass

    args = Object()
    args.headers = []
    args.output_options = [OUT_RESP_HEAD]
    args.output_file = None
    args.download = False

    class Stream(object):
        def write(self, bytes):
            print(bytes)

    env = Object()
    env.stderr = Stream()
    env.stdout = Stream()
    env.config = Object()
    env.config.directory = None

    program(args, env)

# Generated at 2022-06-13 21:41:30.543066
# Unit test for function main
def test_main():
    args = ['http', '--pretty', 'help']
    env = Environment()
    env.stdout = NamedStringIO()
    main(args=args, env=env)

# Generated at 2022-06-13 21:41:32.318455
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 21:41:32.971548
# Unit test for function program
def test_program():
    assert program() == 0

# Generated at 2022-06-13 21:41:47.282067
# Unit test for function program
def test_program():
    import io
    import unittest
    import unittest.mock
    from httpie.cli.definition import parser

    class TestCase(unittest.TestCase):
        env = Environment()

        def call(self, args):
            args = parser.parse_args(list(args), env=self.env)
            return program(args=args, env=self.env)


# Generated at 2022-06-13 21:41:56.245166
# Unit test for function program
def test_program():
    from httpie.cli.argtypes import KeyValueArg
    from httpie.cli.parser import ParseResult
    from httpie.cli.parser import ParseResult
    import httpie.config
    import httpie.output
    import httpie.output.streams
    import httpie.plugins
    import httpie.status
    import pygments

    args = ParseResult(
        headers=[KeyValueArg(key='content-type', value='image/jpeg')],
        method='GET',
        url='www.google.bg',
    )
    env = Environment()
    env.config = httpie.config.Config()
    env.config.__dict__['output_file_encoding'] = 'utf-8'
    env.config.__dict__['color'] = 'auto'

# Generated at 2022-06-13 21:42:11.861551
# Unit test for function program
def test_program():

    class MockOpen(object):
        def __init__(self, filename):
            self.filename = filename
            self.data = ''
            self.closed = False
            self.mode = 'wb'

        def write(self, line):
            self.data = self.data + line

        def close(self):
            self.closed = True

    # TODO: Improve testing for args.download
    def iterate_args():
        args = argparse.Namespace()
        args.download = False
        args.output_file = None
        args.output_file_specified = False
        args.output_options = []
        args.headers = {}
        return args

    def test_program_run():
        program_run = main(sys.argv)
        assert program_run == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:45:51.974585
# Unit test for function main
def test_main():
    from httpie.cli.definition import parser
    from httpie.status import ExitStatus
    args = [
        'http',
        '--debug',
        '--output-file=file',
        '127.0.0.1:8888',
        '--follow',
        '--check-status',
        '--timeout=10',
        '--max-redirects=8',
        '--body=@filename',
        '--body=@-',
        '--form',
        '-v',
        '--headers',
        '--verbose',
        '--output=file',
        '--download=file',
        '--download-resume',
        '--ignore-stdin',
        '--traceback'
    ]
    args = parser.parse_args(args)

# Generated at 2022-06-13 21:45:59.306899
# Unit test for function main
def test_main():

    # Test main function with valid arguments
    exit_status = main(['http', '--version'])
    assert (exit_status == 0)

    # Test main function with invalid arguments
    exit_status = main(['http', '--abc'])
    assert (exit_status == 1)


# Generated at 2022-06-13 21:46:11.709358
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    from httpie.cli import http
    import argparse
    args = parser.parse_args(['http://httpbin.org/post', '--json', '{"a": 1}'])
    env = Environment()
    env.stdout = sys.stdout
    env.stderr = sys.stderr
    program(args=args, env=env)
    args = parser.parse_args(['http://httpbin.org/post', '--json', '{"a": 1}', '--output-file', 'out.txt'])
    args.output_file = open('out.txt', 'w')
    env.stdout = sys.stdout
    program(args=args, env=env)

# Generated at 2022-06-13 21:46:16.056762
# Unit test for function main
def test_main():
    assert main(["httpie", "--json", "https://api.github.com/search/repositories", "q==httpie"]) == 0
    assert main(["httpie", "--json", "https://api.github.com/search/repositories"]) == 0

# Generated at 2022-06-13 21:46:26.444531
# Unit test for function program
def test_program():
    from httpie.cli import parse_items, items_args_to_request_items
    from httpie.cli.parser import ItemValueError
    from httpie.downloads import FileDownloader, FileDownloader
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE

    program_name = 'http'
    client_args = httpie.parse_items(['http://example.com/path'])
    client_kwargs = httpie.item_args_to_request_items(client_args)
    print(f'client_args: {client_args}')
    print(f'client_kwargs: {client_kwargs}')
    
    

# Generated at 2022-06-13 21:46:36.574583
# Unit test for function main
def test_main():
    """
    https://docs.python-guide.org/writing/tests/
    """

    class Env(Environment) :
        # Mock stderr + stdout
        def __init__(self) :
            self.stderr = io.StringIO()
            self.stdout = io.StringIO()
            super().__init__()

        # Mock argv
        @property
        def program_name(self):
            return "a"

    # Test : print_debug_info
    e = Env()
    print_debug_info(env=e)
    r = e.stderr.getvalue()
    assert(r.find("HTTPie")>-1)
    assert(r.find("Requests")>-1)
    assert(r.find("Pygments")>-1)

# Generated at 2022-06-13 21:46:37.220149
# Unit test for function main
def test_main():
    # TODO: Implement
    pass


# Generated at 2022-06-13 21:46:43.424716
# Unit test for function main
def test_main():
    import io
    import sys
    import unittest

    class Test(unittest.TestCase):
        def test(self):
            import httpie.cli.argtypes
            import contextlib
            # Discard stderr to keep pytest output clear.
            with contextlib.redirect_stderr(None):
                assert main([
                    '',
                    'https://httpbin.org/get',
                ]) == ExitStatus.SUCCESS

    unittest.main(argv=[''], exit=False)


if __name__ == '__main__':
    # Unit test for function main
    test_main()

# Generated at 2022-06-13 21:46:44.219694
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 21:46:58.134165
# Unit test for function program
def test_program():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '--check-status',
        action='store_true',
        dest='check_status',
        default=False,
        help='Check status of HTTP transactions',
    )
    parser.add_argument(
        '--download',
        '--download-dash-separated-name',
        action='store_true',
        dest='download',
        default=False,
        help='Download files',
    )
    parser.add_argument(
        '--download-dash-separated-name',
        action='store_true',
        dest='download_dash_separated_name',
        default=False,
        help='Download files',
    )