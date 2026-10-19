

# Generated at 2022-06-22 12:38:34.044251
# Unit test for function main
def test_main():
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1

# Generated at 2022-06-22 12:38:43.725410
# Unit test for function main
def test_main():
    import pytest
    from contextlib import redirect_stderr

    with redirect_stderr(sys.stderr):
        assert main() == 1
    with redirect_stderr(sys.stderr):
        assert main('-i', '-o', '-t') == 1
    with redirect_stderr(sys.stderr):
        assert main('input_file.py', 'output_file.py', '-t', '3.5') == 1

    pytest.raises(exceptions.InputDoesntExists,
                  main, '-i', 'input.py', '-o', 'output.py',
                  '-t', '3.5')

# Generated at 2022-06-22 12:38:44.318520
# Unit test for function main
def test_main():
	pass

# Generated at 2022-06-22 12:38:49.062277
# Unit test for function main
def test_main():
    sys.argv = ['main','-i', 'test.py', '-o', 'output.py', '-t', '3.5', '-r', 'root', '-d']
    sys.stdout = io.StringIO()
    main()
    assert sys.stdout.getvalue() == '23 line(s) compiled\n'
    sys.stdout = sys.__stdout__

# Generated at 2022-06-22 12:38:53.137781
# Unit test for function main
def test_main():
    args = ['py-backwards', r'C:\GitHub\py-backwards\examples\test.py', '-o', r'C:\GitHub\py-backwards\examples\test_out.py', '-t', '3.5']
    main()
    with open(r'examples\test_out.py', 'r', encoding='utf8') as f:
        print(f.read())

# Generated at 2022-06-22 12:39:03.845331
# Unit test for function main
def test_main():
    test_cases = [
        ({'--input': 'tests/data/with-print.py', '--output': 'test.py',
          '--target': '2.7'}, 'tests/data/with-print.2.7.py'),
        ({'--input': 'tests/data/with-print.py', '--output': 'test.py',
          '--target': '3.3'}, 'tests/data/with-print.3.3.py'),
        ({'--input': 'tests/data/with-print.py', '--output': 'test.py',
          '--target': '3.4'}, 'tests/data/with-print.3.4.py'),
    ]


# Generated at 2022-06-22 12:39:11.665384
# Unit test for function main
def test_main():
    sys.argv = ['', '-i', 'test/test_data', '-o', 'test/test_data/output',
                '-t', 'py35', '-d']
    assert main() == 0

    sys.argv = ['', '-i', 'test/test_data', '-o', 'test/test_data/output',
                '-t', 'py35', '-r', 'test', '-d']
    assert main() == 0

    sys.argv = ['', '-i', 'test/test_data', '-o', 'test/test_data/output',
                '-t', 'py35', '-d']
    assert main() == 0


# Generated at 2022-06-22 12:39:13.473601
# Unit test for function main
def test_main():
    # To create docstrings for function
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:19.182468
# Unit test for function main
def test_main():
    result_file = 'tests/test.py'
    sys.argv = ['pybw.py', '-i', 'test.py', '-o', result_file, '-t', '3.5']
    assert main() == 0, 'Compilation failed'
    assert open(result_file, 'r').read() == open('tests/expected.py', 'r').read(), 'Files do not match'


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:22.371945
# Unit test for function main
def test_main():
    sys.argv = ['-i', 'test.py', '-o', 'test_out', '-t', '3.5', '-r', 'root', '-d']
    assert main() == 0

# Generated at 2022-06-22 12:39:41.093271
# Unit test for function main
def test_main():
    parser = ArgumentParser(
        'py-backwards',
        description='Python to python compiler that allows you to use some '
                    'Python 3.6 features in older versions.')
    parser.add_argument('-i', '--input', type=str, nargs='+', required=True,
                        help='input file or folder')
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='output file or folder')
    parser.add_argument('-t', '--target', type=str,
                        required=True, choices=const.TARGETS.keys(),
                        help='target python version')
    parser.add_argument('-r', '--root', type=str, required=False,
                        help='sources root')

# Generated at 2022-06-22 12:39:41.823550
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:39:52.960986
# Unit test for function main
def test_main():
    from .utils import reset_settings
    from .tests.utils import TEST_ROOT
    import os
    import nose
    import nose.tools
    import shutil
    import tempfile
    from .tests.utils import get_file_content

    base_dir = TEST_ROOT + '/data'

    def _get_input_output_paths(input: str, output: str) -> Tuple[str, str]:
        full_input = os.path.abspath(TEST_ROOT + '/' + input)
        full_output = os.path.abspath(TEST_ROOT + '/' + output)
        return full_input, full_output

    if sys.version_info >= (3, 6):
        target_version = sys.version_info[:2]

# Generated at 2022-06-22 12:40:01.293899
# Unit test for function main
def test_main():
    from .conf import set_settings
    set_settings({
        'debug': False,
        'root': '.'
    })
    parser = ArgumentParser(
        'py-backwards',
        description='Python to python compiler that allows you to use some '
                    'Python 3.6 features in older versions.')
    parser.add_argument('-i', '--input', type=str, nargs='+', required=True,
                        help='input file or folder')
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='output file or folder')
    parser.add_argument('-t', '--target', type=str,
                        required=True, choices=const.TARGETS.keys(),
                        help='target python version')

# Generated at 2022-06-22 12:40:05.816032
# Unit test for function main
def test_main():
    input = ['fake_path']
    output = 'fake_output'
    target = '3.6'
    root = 'fake_root'
    debug = True
    args = ['-i', *input, '-o', output, '-t', target, '-r', root, '-d']
    sys.argv = [sys.argv[0]] + args
    main()
    assert sys.argv == [sys.argv[0]] + args

# Generated at 2022-06-22 12:40:07.402619
# Unit test for function main
def test_main():
    init_settings(sys.argv)
    assert main() == 1

# Generated at 2022-06-22 12:40:10.913771
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', '..', '-o', '../py36', '-t', '3.6', '-r', '../py36']
    test = main()
    assert test == 1

# Generated at 2022-06-22 12:40:15.213181
# Unit test for function main
def test_main():
    try:
        sys.argv = ['-i', 'examples/example.py', '-o', 'examples/output.py',
                    '-t', '3.4']
        main()
    except Exception as e:
        raise e

# Generated at 2022-06-22 12:40:23.666927
# Unit test for function main
def test_main():
    import unittest
    import subprocess
    import tempfile
    import shutil

    class MainTest(unittest.TestCase):

        def setUp(self):
            self.temp_path = tempfile.mkdtemp()
            self.test_file_path = self.temp_path + '/test.py'

            self.target_3x_file_path = self.temp_path + '/target_3x.py'
            self.target_27_file_path = self.temp_path + '/target_27.py'
            self.target_default_file_path = self.temp_path + '/target_default.py'


# Generated at 2022-06-22 12:40:24.167434
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:42.567752
# Unit test for function main
def test_main():
    assert main() == 0


# Generated at 2022-06-22 12:40:43.141029
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:44.535393
# Unit test for function main
def test_main():
    result = main()
    assert result == 0

# Generated at 2022-06-22 12:40:46.085689
# Unit test for function main
def test_main():
    assert(2 == 3)

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:47.757000
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:54.917169
# Unit test for function main
def test_main():
    with patch('argparse.ArgumentParser', side_effect=ArgumentParser) as argparse:
        with patch('py_backwards.main.compile_files', side_effect=TypeError) as compile_files:
            assert main() == 1
            # check if function compile_files is called
            compile_files.assert_called_once()
            # check if function ArgumentParser is called
            assert argparse.called


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:41:01.307773
# Unit test for function main
def test_main():
    # Test that it prints help message when --help flag is added
    # Return code should be 0
    assert main(["-h"]) == 0

    # Test that it prints help message when no arguments are specified
    # Return code should be 2
    assert main([]) == 2

    # Test that it prints compilation result message when all arguments
    # are correct. Return code should be 0
    import os
    input_ = os.path.join(os.path.dirname(__file__), "..", "tests", "input",
                          "print.py")
    output = os.path.join(os.path.dirname(__file__), "..", "tests", "output",
                          "print.py")
    assert main(["-i", input_, "-o", output, "-t", "2.6"]) == 0

   

# Generated at 2022-06-22 12:41:11.672500
# Unit test for function main
def test_main():
    import inspect
    import os
    import shutil
    from io import StringIO

    test_file = 'test_file.py'
    test_folder = 'test_folder'
    test_output = 'test_output.py'

    # Create testing objects
    os.mkdir(test_folder)
    with open(test_file, 'w') as f:
        f.write('# Test\n')
    os.mkdir(test_output)
    with open(os.path.join(test_output, 'test1.py'), 'w') as f:
        f.write('# Test\n')
    with open(os.path.join(test_output, 'test2.py'), 'w') as f:
        f.write('# Test\n')

    # If there's no command line arguments, then error

# Generated at 2022-06-22 12:41:13.077743
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:41:18.059586
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards','-i', 'test/test1.py', 'test/test2.py',
                'test/test3.py', 'test/test4.py', 'test/test5.py',
                '-o', 'test/test_output', '-t', '2.7', '-d']
    assert main() == 0

# Generated at 2022-06-22 12:42:05.692231
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i','in.py', '-o', 'out.py', '-t', '2.7', '-r', 'root']
    sys.argv[1:] = sys.argv[1:].append('-d')
    assert main() == 0
    sys.argv = ['py-backwards', '-i','in2.py', '-o', 'out.py', '-t', '2.7', '-r', 'root']
    assert main() == 1
    sys.argv = ['py-backwards', '-i','in.py', '-o', 'out.py', '-t', '2.7', '-r', 'root']
    assert main() == 1

# Generated at 2022-06-22 12:42:10.698057
# Unit test for function main
def test_main():
    from . import mock_io
    sys.argv = ["py-backwards", "-i", "./", "-o", "./", "-t", "python37", "-r", "./"]
    mock_io.mock_stdout()
    result = main()
    mock_io.restore_stdout()
    assert result == 0

if __name__ == '__main__':
    # test_main()
    main()

# Generated at 2022-06-22 12:42:12.628756
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-22 12:42:13.496259
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:18.759520
# Unit test for function main
def test_main():
    sys.argv = [sys.argv[0], '-i', './data.txt', '-o', './output.txt', '-t', '3.4', '-r', 'py36']
    main()

if __name__ == '__main__':

    main()

# Generated at 2022-06-22 12:42:25.171695
# Unit test for function main
def test_main():
    try:
        run_args = ['-i', 'test/test_data/test_module.py', '-o', '__pycache__', \
            '-t', '3.5']
        sys.argv = sys.argv[:1]
        sys.argv += run_args
        main_code = main()
        
        # check result
        assert main_code == 0

        assert os.path.exists('__pycache__/test_module.cpython-36.pyc')
    finally:
        # delete created file
        os.remove('__pycache__/test_module.cpython-36.pyc')
        os.removedirs('__pycache__')

# Generated at 2022-06-22 12:42:35.621391
# Unit test for function main
def test_main():
    from .arguments import test_parse_args
    from .compiler import test_compile_files
    from .consts import test_target_consts
    from .conf import test_init_settings
    from .exceptions import test_exceptions
    from .messages import test_messages
    from .visitor import test_visitor
    from .transformer import test_transformer

    test_parse_args()
    test_target_consts()
    test_compile_files()
    test_init_settings()
    test_exceptions()
    test_messages()
    test_visitor()
    test_transformer()

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:42:43.935638
# Unit test for function main
def test_main():
    # Create the argument list
    sys.argv = ["./py-backwards.py", "-i", "test/test_data/test.py", "-o", "/tmp", "-t", "2.7"]
    main()
    # Check if the output file exists
    assert os.path.isfile("/tmp/test.py")
    # Check if the output file has the correct content
    data = open("/tmp/test.py").read()
    assert 'import six' in data
    assert 'six.print_("hello world")' in data
    # Delete the output file
    os.remove("/tmp/test.py")

# Generated at 2022-06-22 12:42:54.443339
# Unit test for function main
def test_main():
    import os
    from unittest.mock import patch
    from io import TextIOWrapper
    import io
    import sys

    assert sys.argv == ['py-backwards', './py-backwards/tests/test_compiler.py']

    saved_argv = sys.argv
    saved_stdout = sys.stdout

    # Fake stdout for testing

# Generated at 2022-06-22 12:43:00.758126
# Unit test for function main
def test_main():
    from .mock.kodi import xbmcgui
    from .mock.kodi import xbmcaddon
    from .mock.kodi import xbmcplugin
    from .mock.kodi import xbmc
    from .mock.kodi import xbmcgui
    from .mock.kodi import xbmcvfs
    import sys
    sys.modules['xbmcaddon'] = xbmcaddon
    sys.modules['xbmc'] = xbmc
    sys.modules['xbmcgui'] = xbmcgui
    sys.modules['xbmcplugin'] = xbmcplugin
    sys.modules['os'] = xbmcvfs
    assert main() == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:44:33.911710
# Unit test for function main
def test_main():
    sys.argv[1] = '../tests/syntax'
    sys.argv[2] = '1'
    sys.argv[3] = '../tests/syntax'
    sys.argv[4] = '3'
    assert main() == 1

# Generated at 2022-06-22 12:44:39.605424
# Unit test for function main
def test_main():
    sys.argv.append('-i')
    sys.argv.append('test_data/test_basic.py')
    sys.argv.append('-o')
    sys.argv.append('out.py')
    sys.argv.append('-t')
    sys.argv.append('2.7')
    sys.argv.append('-d')
    sys.argv.append('True')
    sys.argv.append('-r')
    sys.argv.append('test_data')
    assert main() == 0

# Generated at 2022-06-22 12:44:44.988357
# Unit test for function main
def test_main():
    init_settings(["-i", "tests/test1.py", "-o", "test_o", "-t", "2", "-r",
                   "", "-d", ""])
    assert compile_files("tests/test1.py", "test_o", const.TARGETS["2"], "")

# Generated at 2022-06-22 12:44:45.998933
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:44:46.539427
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:44:54.093822
# Unit test for function main

# Generated at 2022-06-22 12:44:58.352676
# Unit test for function main
def test_main():

    # Setup
    sys.argv = ['pyb', '-i', 'tests/test_input.py', '-o', 'tests/test_output.py', '-t', 'py27']

    # Exercise
    ret = main()

    # Verify
    assert(ret == 0)

# Generated at 2022-06-22 12:44:59.077458
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:44:59.702818
# Unit test for function main
def test_main():
    assert main() != 0

# Generated at 2022-06-22 12:45:01.227703
# Unit test for function main
def test_main():
    from . import base_test
    assert base_test.main(__name__)