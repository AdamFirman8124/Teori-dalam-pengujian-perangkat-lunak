

# Generated at 2022-06-22 12:38:30.961408
# Unit test for function main
def test_main():
    """
    Test the main function from the compilers entry point
    """
    assert main(["InvalidInput.py","-o","Output"]) not in range(0,3)

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:38:37.331253
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', 'tests/code/sample.py',
                    '-o', 'test.py',
                    '-t', 'py34',
                    '-d']
    assert main() == 0

    sys.argv[1:] = ['-i', 'tests/code/sample.py',
                    '-o', '../test.py',
                    '-t', 'py34',
                    '-d']
    assert main() == 1

    sys.argv[1:] = ['-i', 'tests/code/',
                    '-o', 'test.py',
                    '-t', 'py34',
                    '-d']
    assert main() == 1


# Generated at 2022-06-22 12:38:41.025102
# Unit test for function main
def test_main():
    sys.argv = ['-i', './tests/test_files/empty_file.py',
                '-o', './empty_file_result.py',
                '-t', '3.5',
                '-d']
    assert main() == 0

# Generated at 2022-06-22 12:38:51.238201
# Unit test for function main
def test_main():
    import tempfile
    import shutil
    import os

    from .compiler import compile_files
    from . import const, messages, exceptions

    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-22 12:39:01.777915
# Unit test for function main
def test_main():
    from . import mock
    import io
    import os
    from contextlib import redirect_stdout

    # Test correct configuration
    with io.StringIO() as buf, redirect_stdout(buf):
        mock.arg_parse.get_full_config(
            '-i file1 file2 -o output -t python2.7 -r /root')
        assert buf.getvalue() == 'Hi\n'

    # Test if wrong argument doesn't break the program
    with io.StringIO() as buf, redirect_stdout(buf):
        arg_parse = mock.ArgumentParser(
            'py-backwards',
            description='Python to python compiler that allows you to use some '
                        'Python 3.6 features in older versions.')

# Generated at 2022-06-22 12:39:10.370221
# Unit test for function main
def test_main():
    from tempfile import TemporaryDirectory
    from shutil import copytree

    def run_main(input_, output, target, expected_result = True):
        with TemporaryDirectory() as d:
            if not input_.endswith('.py'):
                copytree(input_, d + "\PYBOU")
                input_ = d + "\PYBOU"
            else:
                open(d + "\PYBOU.py", 'w').write(input_)
                input_ = d + "\PYBOU.py"
            with TemporaryDirectory() as d2:
                try:
                    main(["-i", input_, "-o", d2, "-t", target])
                except SystemExit as e:
                    assert e == expected_result


# Generated at 2022-06-22 12:39:21.006097
# Unit test for function main
def test_main():
    # Invalid input file
    sys.argv = [sys.argv[0], '-i', 'idontexist', '-o', 'somefile', '-t', '3.5']
    assert main() == 1

    # Invalid output file
    sys.argv = [sys.argv[0], '-i', '../compiler.py', '-o', 'somefile', '-t', '3.5']
    assert main() == 1

    # Invalid target
    sys.argv = [sys.argv[0], '-i', '../compiler.py', '-o', 'somefile', '-t', 'some_version']
    assert main() == 1

    # Invalid input file and output file

# Generated at 2022-06-22 12:39:21.623088
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:31.184177
# Unit test for function main
def test_main():
    import unittest
    import unittest.mock
    import io

    class TestMain(unittest.TestCase):
        def setUp(self):
            self.original_args = sys.argv

        def tearDown(self):
            sys.argv = self.original_args

        def test_invalid_output_fail(self):
            sys.argv = 'py-backwards -i a/b/c.py -o '
            self.assertRaises(SystemExit, main)

        def test_input_doesnt_exists_fail(self):
            sys.argv = 'py-backwards -i a.py -o '
            self.assertRaises(SystemExit, main)


# Generated at 2022-06-22 12:39:31.823382
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:39:52.107632
# Unit test for function main
def test_main():
    # Test incorrect input
    # First test when there are not enough arguments
    # Test when input is not given
    sys.argv = ['py-backwards', '-o', 'output', '-t', '2.7']
    assert main() == 2

    # Test when output is not given
    sys.argv = ['py-backwards', '-i', 'input', '-t', '2.7']
    assert main() == 2

    # Test when target is not given
    sys.argv = ['py-backwards', '-i', 'input', '-o', 'output']
    assert main() == 2

    # Second test when there is a wrong argument

# Generated at 2022-06-22 12:40:02.007554
# Unit test for function main
def test_main():
    from filecmp import cmp
    from os import remove, listdir
    from shutil import rmtree
    from pathlib import Path

    PATH = './test_data'
    OUTPUT_PATH = './'
    target = '3.3'
    input_files = [f'{PATH}/test_files/{f}' for f in listdir(f'{PATH}/test_files')]
    root = './test_data/test_files'

    sys.argv = [
        'py-backwards',
        f'-i {PATH}/test_files/compilation_error.py',
        '-o {}/test_output'.format(OUTPUT_PATH),
        f'-t {target}',
        f'-r {root}'
    ]
    assert(main()==1)


# Generated at 2022-06-22 12:40:03.106288
# Unit test for function main
def test_main():
    assert sys.version_info >= (3,6)
    assert main() == 0

# Generated at 2022-06-22 12:40:04.896995
# Unit test for function main
def test_main():
    assert main() in [0, 1]

# Generated at 2022-06-22 12:40:05.648524
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:09.829095
# Unit test for function main
def test_main():
    args = ['-i',"tests/__pycache__/test.cpython-35.pyc", "-o",
            "tests/__pycache__/test.cpython-36.pyc", "-t", "python3.6"]
    main(args)
    assert True

# Generated at 2022-06-22 12:40:13.094740
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', '/path/to/input', '-o', '/path/to/output',
                '-t', '3.4']
    assert main() == 0

# Generated at 2022-06-22 12:40:24.704886
# Unit test for function main
def test_main():
    def get_args(input_: List[str]):
        return lambda: main(input_ + ['-t', '3.6',
                                      '-o', '/home/user/py-backwards/output'])

    assert_that(get_args([]), raises(AttributeError))
    assert_that(get_args(['-t', '3.6']), raises(AttributeError))
    assert_that(get_args(['-o', '/home/user/py-backwards/output']),
                raises(AttributeError))
    assert_that(get_args(['/home/user', '-t', '3.6']),
                raises(AttributeError))
    assert_that(get_args(['/home/user']), raises(AttributeError))

# Generated at 2022-06-22 12:40:26.464966
# Unit test for function main
def test_main():
    try:
        assert main() == 0
    except SystemExit as e:
        assert e.code == 2

# Generated at 2022-06-22 12:40:27.423408
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:40:46.564464
# Unit test for function main
def test_main():
    assert main() == 1

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:49.125402
# Unit test for function main
def test_main():
    try:
        main()
    except Exception:
        assert False
        return

    assert True

# Generated at 2022-06-22 12:40:49.738961
# Unit test for function main
def test_main():
    assert main()==0

# Generated at 2022-06-22 12:40:59.018907
# Unit test for function main
def test_main():
    # Test case 1
    # Command line: python -m py_backwards.backwards -i /home/n.fomin/PycharmProjects/py_backwards/tests/res/ -o /home/n.fomin/PycharmProjects/py_backwards/tests/res/result -t py35
    # Function main must return 0 and print no error
    sys.argv = ['-i', '/home/n.fomin/PycharmProjects/py_backwards/tests/res/',
                '-o', '/home/n.fomin/PycharmProjects/py_backwards/tests/res/result',
                '-t', 'py35']
    assert main() == 0

    # Test case 2
    # Command line: python -m py_backwards.backwards -i /home/n

# Generated at 2022-06-22 12:41:10.135004
# Unit test for function main
def test_main():
    import io
    import sys
    from contextlib import redirect_stdout

    # Test case 1
    print('TEST CASE 1')
    test1_args = ['test1.py', '-i', 'test/test1/sources/main.py',
                  '-o', 'test/test1/build', '-t', 'py27', '-r',
                  'test/test1/sources']
    with redirect_stdout(io.StringIO()):
        main(test1_args)
    with open('test/test1/expected.py', 'r') as f:
        expected1 = f.read()

    with open('test/test1/build/main.py', 'r') as f:
        actual1 = f.read()
    assert expected1 == actual1


    # Test case 2
   

# Generated at 2022-06-22 12:41:16.768854
# Unit test for function main
def test_main():
    from unittest.mock import patch
    with patch('backwards.__main__.init_settings') as init_settings_mock, \
         patch('backwards.__main__.compile_files') as compile_files_mock, \
         patch('backwards.__main__.sys'):
        main()
        assert init_settings_mock.called
        assert compile_files_mock.called

# Generated at 2022-06-22 12:41:26.303840
# Unit test for function main

# Generated at 2022-06-22 12:41:31.481860
# Unit test for function main
def test_main():
    path_ = os.path.dirname(os.path.realpath(__file__))
    path_ = os.path.join(path_, '..')
    path_ = os.path.join(path_, '_test')
    path_ = os.path.normpath(path_)
    assert main(['-i', path_, '-o', path_, '-t', 'py35']) == 0

# Generated at 2022-06-22 12:41:42.021357
# Unit test for function main
def test_main():
    import sys
    from unittest.mock import patch
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Test main function')
    parser.add_argument('-t', '--test', action='store_true', required=False,
                        help='Run unit test for main function')

    args = parser.parse_args()
    if args.test:
        print("Unit test for Main function")
        # input no exists
        with patch.object(sys, 'argv', [
            'py-backwards', '-i', 'infile', '-o', 'outfile', '-r',
            'root', '-t', 'python3.5', '-d']):
            sys.exit(main())
        # Invalid output

# Generated at 2022-06-22 12:41:48.695982
# Unit test for function main
def test_main():
    sys.argv = [
        'py-backwards',
        '-i', __file__,
        '-t', '27',
        '-o', '__init__.py',
    ]

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

# Generated at 2022-06-22 12:42:32.163008
# Unit test for function main
def test_main():
    class Args:
        def __init__(self):
            self.input = '/test/files/test1.py'
            self.output = '/test/files/test1_py3.py'
            self.target = '3.6'
            self.root = '/test/files'

    args = Args()
    init_settings(args)
    assert main() == 0


# Generated at 2022-06-22 12:42:35.956370
# Unit test for function main
def test_main():
    sys.argv = [
        'py-backwards',
        '-i', 'test/test.py',
        '-o', '/tmp/out.py',
        '-t', '3.6'
    ]
    main()

main()

# Generated at 2022-06-22 12:42:41.756838
# Unit test for function main
def test_main():
    argv = ['-i', 'test/input_file.py', '-o', 'test/output_file.py',
                    '-t', '2.6', '-r', 'test/']
    main()
    assert open('test/output_file.py', 'r').read() == 'print "test"'


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:48.115427
# Unit test for function main
def test_main():
    # Create an input arguments for test
    sys.argv = ['py-backwards.py', '-i', 'test_data/test_module.py',
                '-o', 'test_data/output', '-t', '27', '-r', 'test_data']
    sys.argv.append('-d')

    # Test that main function returns 0 when
    # compilation is successful
    assert main() == 0

# Generated at 2022-06-22 12:42:49.333845
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-22 12:42:50.636901
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:51.227353
# Unit test for function main
def test_main():
    assert main() == 1

# Generated at 2022-06-22 12:43:01.818490
# Unit test for function main
def test_main():
    # The command line arguments
    sys.argv = [
        "py-backwards",
        "-i",
        "data/example/subpackage",
        "-o",
        "data/example/subpackage",
        "-t",
        "3"
    ]
    try:
        main()
    except SystemExit as e:
        # we don't want the unit test to crash when main throws an exception
        # and we need to test that too
        pass


# Generated at 2022-06-22 12:43:09.977700
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '2.6']
    with patch('py_backwards.compiler.compile_files',
               return_value=['input.py']):
        assert main() == 0

    sys.argv = ['py-backwards', '-i', 'input.py', '-o', 'output', '-t', '2.7']
    with patch('py_backwards.compiler.compile_files',
               return_value=['input.py']):
        assert main() == 0

    sys.argv = ['py-backwards', '-i', 'input', '-o', 'output.py', '-t', '2.7']

# Generated at 2022-06-22 12:43:15.575946
# Unit test for function main
def test_main():
    input = 'tests/resources/test_input.py'
    output = 'tests/resources/test_out.py'
    target = const.TARGETS['3.5']
    root = 'tests/resources'

    result = compile_files(input, output, target, root)
    assert result == 1

# Generated at 2022-06-22 12:44:53.763726
# Unit test for function main
def test_main():
    root = os.path.dirname(os.path.dirname(__file__))
    if root == '':
        root = os.getcwd()
    # Invalid input
    assert main() == 1
    assert main(['-i', 'src/py_backwards/compiler.py']) == 1
    assert main(['-i', 'src/py_backwards/compiler.py', '-o', 'out.py',
                 '-t', 'python2.7']) == 1
    # Invalid output
    invalid_output = os.path.join(root, 'tests/fixtures/invalid_output')
    assert main(['-i', 'tests/fixtures/python3', '-o', invalid_output,
                 '-t', 'python3.6']) == 1

# Generated at 2022-06-22 12:44:54.367969
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:44:58.218910
# Unit test for function main
def test_main():
    args = ['-i', 'tests/input', '-o', 'tests/output', '-t', '3.7', '-r', 'tests']
    sys.argv = [sys.argv[0]] + args
    main()
    assert True

# Generated at 2022-06-22 12:44:59.749080
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        pass


# Generated at 2022-06-22 12:45:00.407306
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:45:00.944288
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:45:09.413181
# Unit test for function main
def test_main():
    from tempfile import TemporaryDirectory
    import os
    import shutil

    def check_exists(path):
        if not os.path.exists(path):
            raise FileNotFoundError('File not found')

    def check_not_exists(path):
        if os.path.exists(path):
            raise FileExistsError('File exists')

    examples_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..',
        'examples')
    assert os.path.isdir(examples_path)

    # mocks
    sys.argv = ['py-backwards', '-i', examples_path, '-o', 'output',
                '-t', '2.7', '-r', examples_path]

# Generated at 2022-06-22 12:45:09.957781
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:45:14.657739
# Unit test for function main
def test_main():
    # from . import const
    init_settings()
    # assert (main()==compile_files(const.TARGETS['2.7']))

# Generated at 2022-06-22 12:45:16.390362
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()